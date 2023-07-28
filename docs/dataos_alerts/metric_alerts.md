# Setting up Metric Alerts

Imagine a scenario where your sales are booming but you don't realize that your inventory is running low.. This guide will demonstrate how to how to use DataOS with Python and SQL to set up alerts for
key metrics such as inventory, sales, or pipeline leakages. This way, you can stay informed and take action when needed.

In this example, an alert is created that triggers when the total revenue for a specific country surpasses $10,000. The alert will notify the country manager about the significant revenue milestone. This alert system will be established through a Python script dockerized and deployed using Alpha Stack on DataOS, interacting with the Icebase depot, where the relevant data is stored.

## DataOS Alerts: Setting the Stage

For demonstration, a sports items database containing tables such as `customer`, `sales`, `product`, `return`, and `territory` is used. Sales data is fetched using a `LENS` query which retrieves `customer key`, `total revenue`, and `country`. Additionally, `email addresses` of respective country managers are mapped for alert notifications.

## Prerequisites

### **Getting the apikey for the user**

The DataOS API key for the user can be obtained by executing the command below.

```bash
dataos-ctl user apikey get
```

## Procedure

### **Step 1: Construct the Query**

The SQL query is designed to extract necessary data and conditionally assign manager email addresses based on the country. If the `total revenue` exceeds the set threshold, the alert is triggered.

```sql
SELECT
  *,
  CASE
    WHEN "territory.country" = 'France' THEN 'manager_france@mail.com'
    WHEN "territory.country" = 'Germany' THEN 'manager_deutsch@mail.com'
  END AS manager_mail
FROM
  LENS (
    SELECT
      "sales.total_revenue",
      "customer.customer_key",
      "territory.country"
    FROM
      sportsdata
    LIMIT
      50000
  )
WHERE
  "sales.total_revenue" > 10000
```

### **Step 2: Establish Python-DataOS Connection**

Python, with its robust library support, is used to generate alerts and establish a connection with the depot. A  Python script `alert.py` is created  and a connection to DataOS using a connector cursor is established.

```python
# Libraries used
import pandas as pd
from function import send_mail  ##function.py in the same folder
from trino.auth import BasicAuthentication
from trino.dbapi import connect
import openpyxl
import sys

# Credentials to connect with trino
dataos_id = {{id}}
cluster_name  = {{clusterID}}
dataos_api_key   =  {{apikey}}

# DO NOT FORGET `tcp` BEFORE DOMAIN NAME
env_name = 'tcp.{{dataos-context}}'

conn = connect(host= env_name,
               port="7432",
               auth=BasicAuthentication(dataos_user_name, dataos_api_key),
               http_scheme="https",
               http_headers={"cluster-name": cluster_name}
               )
cur = conn.cursor()
```

The following query is written to fetch all the entries from the database, creating a dataframe.

```python
cur.execute("""
SELECT
  *,
  CASE
    WHEN "territory.country" = 'France' THEN 'iamgroot@tmdc.io'
    WHEN "territory.country" = 'Germany' THEN 'thor@tmdc.io'
END AS manager_mail
FROM
  LENS (
    SELECT
      "sales.total_revenue",
      "customer.customer_key",
      "territory.country"
    FROM
      sportsdata
    LIMIT
      50000
  )
WHERE
  "sales.total_revenue" > 10000""")

data = cur.fetchall()
print('Data fetch successful')

# Creating a pandas DataFrame
df = pd.DataFrame(data, columns =['sales.total_revenue',
                                  'customer.customer_key',
                                  'territory.country',
                                  'manager_mail'])
```

### **Step 3: Compose Mail and Alert Dispatch**

The `Redmail` library is used to send alerts via email. In case you have your own SMTP server, configure it accordingly.

`Redmail` is compatible with `Outlook` and `G-mail`. `Jinja` templates can be used to send customized alerts. For example, Python variables like {{manager_mail}} is used in HTML code.

```python
from redmail import gmail
from pretty_html_table import build_table
# # Credentials for mailing
gmail.username = 'alertDataOS@mail.com'
gmail.password = '<password>'

print('Connection established, initiating email alerts')

def send_mail(df):
  for country in df['territory.country'].unique():
    data = df.loc[df['territory.country'] == country,:]
    data = data.dropna(axis = 1)  # Dropping unnecessary columns
    data['html_table_grey_light'] = build_table(data.iloc[:,5:], 'grey_dark',font_family='Calibri',font_size='small')

    gmail.send(subject= 'Total revenue > limit',
      receivers=data['manager_mail'].iloc[0],
      html="""
          <p><h3> Alert Notification 🔔 </h3></p>
          <p> Hi {{ manager_name }} ,
            </p> <p> An alert from DataOS is triggered due to a surge in revenue. Please find the details in the below table. </p>
            <P class=”oneandhalf”></P>
            {{html_table_grey_light}}
            <br>
            <p>Regards,<br>DataOS Team</p>
            <p>&ensp;</p>
            <p><i><small>Confidential: This message is confidential and intended only for the recipient. It is strictly forbidden to share this message with any third party, without written consent from the sender. This email is auto-generated by Modern DataOS. Please do not reply.</i></small></p>
          """,
      attachments={"Details.xlsx":data.iloc[:,:]},
      body_params={"manager_name": data['manager_mail'].iloc[0] ,"html_table_grey_light":data['html_table_grey_light'].iloc[0]})
    print(country, 'alert dispatched')

# Initiate the mailing process
send_mail(df)
```

### **Step 4: Dockerization of alert.py**

Standard Docker procedures are followed to containerize the code.

```docker
### Save this as Dockerfile
FROM python:3.10
COPY alert.py .
COPY function.py .
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
CMD [ "python3", "alert.py", "function.py"]
```

**a. Build the Docker Image**

In your terminal, navigate to the directory containing the Dockerfile and run the following command to build your Docker image. Replace `<image-name>` with the name you want to give your Docker image.

```bash
docker build -t <image-name> .
```

**b. Tag the Docker Image**

Before you can push the image to Docker Hub, you need to tag it with your Docker Hub username and the repository name you want to push it to. Replace the DockerHub Username with your one.

```bash
docker tag workflowalert:latest <dockerhub-username>/<image-name>:latest 
```

**c. Log in to Docker Hub**

Log in to Docker Hub from your command line. You'll be prompted to enter your Docker Hub username and password.

```
docker login
```


**d. Push the Docker Image to Docker Hub**

You can push your image to your Docker Hub repository using the following command.

```bash
docker push <dockerhub-username>/<image-name>:latest
```

Replace `<dockerhub-username>` with your Docker Hub username and `<image-name>` with the name you want to give your Docker image.

Your Metric Alert is now packaged in a Docker image and available on Docker Hub.

### **Step 5: Construct the Metric Alert Workflow**

After building the Docker container, a workflow-service connection is established where the Docker image is supplied.

```yaml
## alerts-config.yaml
version: v1
name: wf-alert-01
type: workflow
workflow:
  dag:
    - name: alpha-alert
      spec:
        stack: alpha
        compute: runnable-default
        alpha:
          image: <hubUsername>/<dockerTag>
          command: 
			- python
          arguments:
            - alert_daily.py
            - function.py
```
[Notification in Email](metric_alert.png)

<aside class="callout"> The workflow can be scheduled to run at your preferred frequency (e.g., every minute, hourly, daily) using CRON jobs in the `schedule` tag. </aside>

Now, apply this YAML configuration to DataOS.

```bash
dataos-ctl apply -f alerts-config.yaml
### output ###
INFO[0000] 🛠 apply...
INFO[0000] 🔧 applying(public) wf-alert-01:v1:workflow...
INFO[0005] 🔧 applying(public) wf-alert-01:v1:workflow...created
INFO[0005] 🛠 apply...complete

# Check status
dataos-ctl -t workflow -w public get
### output ###

INFO[0000] 🔍 get...
INFO[0001] 🔍 get...complete

     NAME     | VERSION |   TYPE   | WORKSPACE | STATUS | RUNTIME |   OWNER
--------------|---------|----------|-----------|--------|---------|-------------
  wf-alert-01 | v1      | workflow | public    | active | running | <id>

```

After the workflow successfully completes, an email alert mechanism is ready to send emails whenever the threshold condition is met.