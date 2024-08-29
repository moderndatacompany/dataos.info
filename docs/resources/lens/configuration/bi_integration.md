# BI Integraions 

## Pre-requisites

- **Curl**: Ensure you have `curl` installed on your system. For Windows users, you may need to use `curl.exe`. 
- **Lens 2.0 API Endpoint**: The API endpoint provided by Lens 2.0 to sync the data with meta endpoint access.
- **Access Credentials**: For Superset, you will need access credentials such as username, password, and host.

## Superset

The following `curl` command is used to synchronize data from Lens to a Superset. It posts configuration details required for integration.

To sync your Lens 2.0 model with Superset, execute the following curl command:

=== "Syntax"

    ```bash
    curl --location --request POST 'https://<DATAOS_FQDN>/lens2/sync/api/v1/superset/public:<LENS-NAME>' \
    --header 'apikey: <apikey>' \
    --header 'Content-Type: application/json' \
    --data-raw '
    {
        "username": "<superset username>",
        "password": "<superset password>",
        "host": "https://superset-<DATAOS_FQDN>"
    }
    ```

=== "Example"

    ```bash
    curl --location --request POST 'https://liberal-donkey.dataos.app/lens2/sync/api/v1/superset/public:company-intelligence' \
    --header 'apikey: aueniekQa==' \
    --header 'Content-Type: application/json' \
    --data-raw '
    {
        "username": "adder_1",
        "password": "adder_1",
        "host": "https://superset-liberal-donkey.dataos.app""
    }
    ```

**Command Parameters:**

- **`URL`**: `https://liberal-donkey.dataos.app/lens2/sync/api/v1/superset/public:sales360` This is the endpoint for syncing with Superset.

- **`DataOS FQDN`: any current DataOS  FQDN. For example,** `liberal-donkey.dataos.app`

- **`--header 'Content-Type: application/json'`**: This specifies the content type as JSON.

- **`Lens_Name`: Your lens name. Example `sample360`.**

- **`API_Key`: Your DataOS API key in your `docker-compose.yaml`.**

Upon initiation, you will receive a response:

```bash
{
    "message": "started"
}
```

Upon successful completion, you will receive a response:

```bash
{
    "message": "Superset project creation and sync completed successfully."
}
```

**Terminal**

<div style="text-align: center;">
    <img src="/resources/lens/configuration/superset1.png" alt="Superset Configuration" style="max-width: 100%; height: auto; border: 1px solid #000;">
    <figcaption> Superset Curl Command executed in Terminal
</div>


Once you execute the command in the terminal, the results will be visible in the Superset app, as demonstrated below:

Please follow the steps outlined to see the result:

1. **Go to Environment**: Select Superset.

<div style="text-align: center;">
    <img src="/resources/lens/configuration/superset2.png" alt="Superset Configuration" style="max-width: 100%; height: auto; border: 1px solid #000;">
</div>

1. **Navigate to Datasets Tab**: Here, each entity will be available in the form of datasets.

<div style="text-align: center;">
    <img src="/resources/lens/configuration/superset3.png" alt="Superset Configuration" style="max-width: 100%; height: auto; border: 1px solid #000;">
</div>

Everything is set up now. Explore and perform further analysis in Superset.

## Tableau

To sync your Lens 2.0 model with Tableau, execute the following curl command:

### **Step 1: Run the curl command**

To sync your Lens 2.0 model with Tableau, you need the following credentials:

```bash
curl --location --request POST 'http://127.0.0.1:5000/lens2/sync/api/v1/tableau/public:company-intelligence' \
--header 'apikey: <apikey>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "project_name": "sample",
    "username": "user1",
    "password": "password1",
    "site_id": "site1",
    "server_address": "https://prod-apnortheast-a.online.tableau.com"
}'
```

You can obtain these when you **log in** to Tableau. You’ll see the **URL** like below:

[**https://prod-apnortheast-a.online.tableau.com/#/site/](https://prod-apnortheast-a.online.tableau.com/#/site/piyushjoshi704a51af6e)site_id**

```bash
{
"project_name": "tableau project name" ,
"username": "tableau username", 
"password": "tableau password",
"site_id": "tableau site id",
"server_address": "https://prod-apnortheast-a.online.tableau.com"
}
```

<aside class="callout">
💡 Tableau server config are only needed in case of user wants to publish generated tds files at tableau server.

</aside>

### **Step 2: Go to tableau**

Go to the Explore tab on the left side. You’ll see the required tables and views in your project.

In the screenshot below, there are three sources: one for tables and two for views.

<div style="text-align: center;">
    <img src="/resources/lens/configuration/tableau1.png" alt="Superset Configuration" style="max-width: 100%; height: auto; border: 1px solid #000;">
</div>

### **Step 3: Explore and Create Visualizations**

Go to the Home tab on the left side and click on 'New'. Under it, click on 'Workbook'.


<div style="text-align: center;">
    <img src="/resources/lens/configuration/tableau2.png" alt="Superset Configuration" style="max-width: 100%; height: auto; border: 1px solid #000;">
</div>

### **Step 4: Connect to Data**

Once you click on 'Workbook', it’ll take you to 'Connect to Data'. Select either views or tables and click on 'Connect'.


<div style="text-align: center;">
    <img src="/resources/lens/configuration/tableau3.png" alt="Superset Configuration" style="max-width: 100%; height: auto; border: 1px solid #000;">
</div>


As you click on 'Connect', it’ll ask you for username and password. Enter the **DataOS username and API key**


<div style="text-align: center;">
    <img src="/resources/lens/configuration/tableau4.png" alt="Superset Configuration" style="max-width: 100%; height: auto; border: 1px solid #000;">
</div>

**### Step 5: Start Using the Model**

Once you enter the credentials and click on 'Sign In', you’re ready to use the model for your visualization purposes.

<div style="text-align: center;">
    <img src="/resources/lens/configuration/tableau5.png" alt="Superset Configuration" style="max-width: 100%; height: auto; border: 1px solid #000;">
</div>

**Note:**

-  For views and tables, you need to build the connection two times.
- If any entity in the model lacks a relationship, an error will occur. To resolve this, you can hide the entity.
- The connection is live, so any changes to the underlying data or measure logic will reflect in Tableau cloud.
- If there are schema changes, such as adding new dimensions and measures, you will need to repeat the steps above.

<aside class="callout">
💡 Tableau does not support cyclic dependencies within the data model. Ensure that your data model is free of any cyclic dependencies before attempting to sync with Tableau.

</aside>