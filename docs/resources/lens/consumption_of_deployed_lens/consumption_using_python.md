# Consumption of Lens using Python

## Using Lens APIs

> As per the use case, utilize any of the APIs available, such as load, SQL, or meta.
> 

### **Step 1: Import Required Libraries**

First, import the necessary libraries. You need `requests` for making HTTP requests, `json` for handling JSON data, and `pandas` for data manipulation.

```python
import requests
import json
import pandas as pd
```

### **Step 2: Define the URL and Headers**

Define the URL for the API endpoint and the headers required for the request. The headers include the content type, authorization token. Replace `<apikey>` with your `<dataos_api_token>`.

```python
url = "https://liberal-donkey.dataos.app/lens2/api/public:flashtest/v2/load"
#lens name will be public:lensname
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer <apikey>'
}
```

### **Step 3: Create the Payload**

Create the payload for the POST request. This payload is a JSON object containing the query parameters, such as measures, dimensions, segments, filters, time dimensions, limit, and response format.

You can choose the necessary elements from Lens Explorer and then paste them into the payload below.

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

### **Step 4: Send the POST Request**

Send the POST request to the API endpoint using the `requests` library and store the response.

```python
response = requests.request("POST", url, headers=headers, data=payload)
```

### **Step 5: Parse the JSON Response**

Parse the JSON response to extract the data.

```python
response_json = response.json()
```

### **Step 6: Extract Specific Fields from the Response**

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

### **Complete Script**

Here is the complete script for reference:

    
```python
import requests
import json
import pandas as pd

url = "https://liberal-donkey.dataos.app/lens2/api/public:flashtest/v2/load"
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer apikey',
  'Cookie': 'connect.sid=s%3A2chO2fMucxnKmX3BGd98hiGu4VEQhxL7.g1ud0spLM046rqygt2VANHSGr7pjjf4%2FuUyEicUVcIA'
}
payload = json.dumps({
  "query": {
    "measures": [
      "sales.cumm_sum",
      "sales.cumm_sum_lead",
      "sales.current_month_sum",
      "sales.current_month_sum_lead",
      "sales.first_invoiced_date",
      "sales.month_over_month_ratio",
      "sales.monthly_units_sales_2024",
      "sales.previous_month_sum",
      "sales.previous_month_sum_lead",
      "sales.rolling_count_month",
      "sales.total_revenue",
      "sales.year_over_year_ratio"
    ],
    "dimensions": [
      "product.brand",
      "product.category",
      "product.class",
      "product.class_description",
      "product.flavor",
      "product.item_no",
      "product.product_name",
      "product.sub_class",
      "product.varietal",
      "product.vintage",
      "sales.customer_id",
      "sales.source",
      "sales.year",
      "sales.month",
      "sales.week"
    ],
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
💡 <b>For the meta API endpoint, employ the `GET` method, while for other endpoints, utilize the `POST` method. </b>

</aside>

## Using Postgres DB

### **Step 1: Install Required Libraries**

First, we need to install the `psycopg2` library, which is a PostgreSQL adapter for Python. This allows Python code to interact with PostgreSQL databases

```python
!pip install psycopg2
#or 
!pip install psycopg2-binary
```

### **Step 2: Import Libraries**

We import the necessary libraries. `psycopg2` is used for database connections and interactions, and `pandas` is used for data manipulation and visualization.

```python
import psycopg2
import pandas as pd
```

### Step 3: **Define Database Connection Details**

We define the connection details for the database. This includes the username, password, host, port, and database name.

=== "Syntax"                                                                       

    ```python
    db_username = dataos username
    db_password = dataos apikey
    db_host = 'tcp.liberal-donkey.dataos.app'
    db_port = '6432'
    db_name = 'lens:<workspace_name>:<lens_name>'  # The name of your lens
    ```
=== "Example"   

    ```python
    db_username = iamgroot
    db_password = eyawbejweiyY==
    db_host = 'tcp.liberal-donkey.dataos.app'
    db_port = '6432'
    db_name = 'lens:public:sales360'  # The name of your lens
    ```

### **Step 4: Create Connection String**

Using the defined connection details, we create a connection string to connect to the PostgreSQL database.

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

### **Step 5: Create a Cursor Object**

A cursor object is created using the connection. The cursor allows us to execute SQL queries.

```python
cur = conn.cursor()
```

### **Step 6: Show the Tables**

We execute a query to retrieve the names of all tables in the `public` schema of the database. The result is fetched and printed in a readable format using `pandas`

```python
cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")
tables = cur.fetchall()

# Convert the result to a readable format using pandas
tables_df = pd.DataFrame(tables, columns=['Table Name'])
print(tables_df)

```

### **Step 7: Retrieve Column Names and Data Types from a Specific Table**

We query the `information_schema.columns` to get the column names and data types of a specific table (`customer`). The result is then converted to a DataFrame for better readability.

```python
query = f"""SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'customer';"""
cur.execute(query)
result = cur.fetchall()
result_df = pd.DataFrame(result, columns=['Column Name', 'Data Type'])
result_df

```

### **Step 8: Query Specific Columns from a Table**

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

### **Complete Script**

Here is the complete script for reference:

    
```python
!pip install psycopg2
import psycopg2
import pandas as pd

# Define your lens connection details
db_username = '**' #dataos username
db_password = '***' #apikey
db_host = 'tcp.liberal-donkey.dataos.app' 
db_port = '6432'
db_name = 'lens:public:customer'  # The name of your lens

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