# Exploration of semantic model using Python

## Using Lens APIs

!!!info
    As per the use case, utilize any of the APIs available, such as `load`, `sql`, or `meta`.

### **Step 1: Import required libraries**

First, import the necessary libraries. 

- `requests` for making HTTP requests
- `json` for handling JSON data
- `pandas` for data manipulation.

```python
import requests
import json
import pandas as pd
```

### **Step 2: Define the URL and headers**

Define the URL for the API endpoint and the headers required for the request. The headers include the content type, authorization token. Replace `<apikey>` with your `<dataos_api_token>`.

This endpoint is used to executes queries to retrieve data based on the specified dimensions, measures, and filters. When you need to perform data analysis or retrieve specific data from the semantic model.

Use this endpoint when you need to perform data analysis or retrieve specific data from the semantic model. It will retrieve data based on the specified dimensions, measures, and filters.

```python
url = "https://liberal-donkey.dataos.app/lens2/api/<WORKSPACE_NAME>:<LENS_NAME>/v2/load"
#lens name will be public:lensname
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer <apikey>'
}
```
**Code parameters:**

**URL:** 

- **`<DATAOS_FQDN>`:** Replace `<DATAOS_FQDN>` with the Fully Qualified Domain Name (FQDN) where Lens is deployed. For example,`liberal-donkey.dataos.app`. 

- **`<LENS_NAME>`:** The name of the semantic model you wish to sync. For example **`sales360`.**

**header**

- **Content-Type: application/json** This header specifies that the data being sent is in JSON format.

- **`<apikey>`:** DataOS API key used for authentication. To generate a API key use the following command:

```bash
#command

dataos-ctl user apikey get

#expected_output

INFO[0000] 🔑 user apikey get...                         
INFO[0002] 🔑 user apikey get...complete                 

                               TOKEN                               │  TYPE  │        EXPIRATION         │    NAME      
───────────────────────────────────────────────────────────────────┼────────┼───────────────────────────┼──────────────
  Abcdefghijklmnopqrstuvwxyz==     │ apikey │ 2025-06-27T15:30:00+05:30 │ tester       
  bGVuc19hcGlrZzzzzTkfyuhnodtd3NDE5 │ apikey │ 2036-10-22T10:30:00+05:30 │ lens_apikey  
```

If no API key is listed, execute the following command to create one:

```bash
dataos-ctl user apikey create #it will generate a apikey with default expiration time of 24h

#or

dataos-ctl user apikey create -n apikey_for_powerbi -d 48h
```

!!!note

    Use the API key as password.


### **Step 3: Create the query payload**

Create the payload for the POST request. This payload is a JSON object containing the query parameters, such as measures, dimensions, segments, filters, time dimensions, limit, and response format.

Choose the dimensions and measures from the Explorer Studio in the Data Product Hub tab and click on the 'Integration' button to generate a payload and paste them below. To know more about Payload click [here](/resources/lens/working_with_payload/)

```python
payload = json.dumps({
  "query": {
  "measures": [
    "customer.average_age",
    "customer.total_customers"
  ],
  "dimensions": [],
  "segments": [],
  "filters": [],
  "timeDimensions": [],
  "limit": 10,
  "responseFormat": "compact"
}
  }
)
```

### **Step 4: Send the POST request**

Send the POST request to the API endpoint using the `requests` library and store the response.

```python
response = requests.request("POST", url, headers=headers, data=payload)
```

### **Step 5: Parse the JSON response**

Parse the JSON response to extract the data.

```python
response_json = response.json()
```

### **Step 6: Extract specific fields from the response**

Extract the `members` and `dataset` fields from the JSON response. The `members` represent the columns, and the `dataset` represents the data rows.

```python
data = response_json.get('data', {})
members = data.get('members', [])
dataset = data.get('dataset', [])
```

### **Step 7: Create a DataFrame**

Create a pandas DataFrame from the extracted data. The columns of the DataFrame are defined by the `members`, and the data is populated by the `dataset`.

```python
df = pd.DataFrame(dataset, columns=members)
```

### **Step 8: Display the DataFrame**

Display the first few rows of the DataFrame to verify the data.

```python
df.head()
```

### **Complete script**

Here is the complete script for reference:

    
```python
import requests
import json
import pandas as pd

url = "https://liberal-donkey.dataos.app/lens2/api/public:flashtest/v2/load"
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer <apikey>',
  'Cookie': 'connect.sid=s%3A2chO2fMucxnKmX3BGd98hiGu4VEQhxL7.g1ud0spLM046rqygt2VANHSGr7pjjf4%2FuUyEicUVcIA'
}
payload = json.dumps({
  "query": {
    "measures": [
    "customer.average_age",
    "customer.total_customers"
    ],
    "dimensions": [],
    "segments": [],
    "filters": [],
    "timeDimensions": [],
    "limit": 10000,
    "responseFormat": "compact"
  }
})

response = requests.request("POST", url, headers=headers, data=payload)

response_json = response.json()

data = response_json.get('data', {})
members = data.get('members', [])
dataset = data.get('dataset', [])

df = pd.DataFrame(dataset, columns=members)

df.head()
```
    

<aside class="callout">
💡 For the meta API endpoint, employ the <b>`GET`</b> method, while for other endpoints, utilize the <b>`POST`</b> method. 
</aside>

## Using Postgres DB

### **Step 1: Install required libraries**

First, install the `psycopg2` library, which is a PostgreSQL adapter for Python. This allows Python code to interact with PostgreSQL databases

```python
!pip install psycopg2
#or 
!pip install psycopg2-binary
```

### **Step 2: Import Libraries**

Import the necessary libraries. `psycopg2` is used for database connections and interactions, and `pandas` is used for data manipulation and visualization.

```python
import psycopg2
import pandas as pd
```

### Step 3: **Define database connection details**

Define the connection details for the database, including username (DataOS ID), password (API key), host, port, and database name.

To retrieve your DataOS ID (used as the username), run:

```bash
#command

dataos-ctl user get

#expected_output

        NAME      │       ID       │  TYPE  │          EMAIL          │              TAGS               
──────────────────┼────────────────┼────────┼─────────────────────────┼─────────────────────────────────
  Iamgroot        │ iamgroot       │ person │ iamgroot@tmdc.io        │ `roles:id:data-dev`,              
                  │                │        │                         │ `roles:id:system-dev`,            
                  │                │        │                         │ `roles:id:user`,                  
                  │                │        │                         │ `users:id:iamgroot`
```

!!!note

    Use the value under 'ID' column (e.g., `iamgroot`) as username.

To retrieve your API key (used as the password), run:

```shell
dataos-ctl user apikey get 
```

If no API key is listed, execute the following command to create one:

```bash
# Generate an API key with the default expiration time of 24 hours
dataos-ctl user apikey create

# OR

# Generate an API key with a custom name and expiration time of 48 hours
dataos-ctl user apikey create -n apikey_for_powerbi -d 48h
```


=== "Syntax"                                                                       

    ```python
    db_username = <DATAOS_USERNAME>               #Copied ID from dataos-ctl user get
    db_password = <DATAOS_APIKEY>                 #Copied apikey from dataos-ctl user apikey get
    db_host = 'tcp.<DATAOS_FQDN>.dataos.app'
    db_port = '6432'
    db_name = 'lens:<WORKSPACE_NAME>:<LENS_NAME>'  # The name of semantic model
    ```
=== "Example"   

    ```python
    db_username = iamgroot                         #Copied ID from dataos-ctl user get
    db_password = eyawbejweiyY==
    db_host = 'tcp.liberal-donkey.dataos.app'      #Copied apikey from dataos-ctl user apikey get
    db_port = '6432'
    db_name = 'lens:public:sales360'               # The name of semantic model
    ```

### **Step 4: Create connection string**

Using the defined connection details, create a connection string to connect to the PostgreSQL database.

```python
conn = psycopg2.connect(
        host=db_host,
        database=db_name,
        user=db_username,
        password=db_password,
        port=db_port
    )
print("Connection successful")
```

### **Step 5: Create a cursor object**

A cursor object is created using the connection. The cursor allows us to execute SQL queries.

```python
cur = conn.cursor()
```

### **Step 6: Show the tables**

We execute a query to retrieve the names of all tables in the `public` schema of the database. The result is fetched and printed in a readable format using `pandas`

```python
cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")
tables = cur.fetchall()

# Convert the result to a readable format using pandas
tables_df = pd.DataFrame(tables, columns=['Table Name'])
print(tables_df)

```

### **Step 7: Retrieve column names and data types from a specific table**

We query the `information_schema.columns` to get the column names and data types of a specific table (`customer`). The result is then converted to a DataFrame for better readability.

```python
query = f"""SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'customer';"""
cur.execute(query)
result = cur.fetchall()
result_df = pd.DataFrame(result, columns=['Column Name', 'Data Type'])
result_df
```

### **Step 8: Query specific columns from a table**

We execute a query to fetch specific columns (`customer_id` and `degree_of_loyalty`) from the `customer` table and convert the result to a DataFrame.

```python
query = f"SELECT customer_id, degree_of_loyalty FROM customer;"
cur.execute(query)
result = cur.fetchall()
result_df = pd.DataFrame(result, columns=['customer_id', 'degree_of_loyalty'])
result_df

# Close the cursor and connection
cur.close()
conn.close()
```

### **Complete script**

Here is the complete script for reference:
    
```python
!pip install psycopg2
import psycopg2
import pandas as pd

# Define your lens connection details
db_username = '**'                        #dataos id copied from 'dataos-ctl user get' command
db_password = '***'                       #apikey copied fromm 'dataos-ctl user apikey get' command
db_host = 'tcp.liberal-donkey.dataos.app' 
db_port = '6432'
db_name = 'lens:public:customer'  # The name of semantic model

# Create the connection string
conn = psycopg2.connect(
        host=db_host,
        database=db_name,
        user=db_username,
        password=db_password,
        port=db_port
    )
print("Connection successful")
# Create a cursor object
cur = conn.cursor()

# Show the tables
cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")
tables = cur.fetchall()

# Convert the result to a readable format using pandas
tables_df = pd.DataFrame(tables, columns=['Table Name'])
print(tables_df)

#Column Names in Table with Data Type
query = f"""SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'customer';"""
cur.execute(query)
result = cur.fetchall()
result_df = pd.DataFrame(result, columns=['Column Name', 'Data Type'])
result_df

#Query the Table with Column Name
query = f"SELECT customer_id,degree_of_loyalty FROM customer;"
cur.execute(query)
result = cur.fetchall()
result_df = pd.DataFrame(result, columns=['customer_id','degree_of_loyalty'])
result_df

# Close the cursor and connection
cur.close()
conn.close()
```