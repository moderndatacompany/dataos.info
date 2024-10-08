# Jupyter Notebook Integration

You can consume a Data Product to build the AI/ML models using Jupyter Notebook. Following are the steps to connect the Data Product to the Jupyter Notebooks.

1. Go to the **Access Options tab** of your Data Product, on the **App Development** section, and click on the **Download**, it will download a `.ipynb` file.

    <center>
    <img src="/interfaces/data_product_hub/activation/image%20(26).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>


1. Download the file and open it in any IDE, such as VS Code or PyCharm. This `ipynb` file contains the templates to consume the Data Product via Rest APIs, PostgreSQL interface, and GraphQL APIs, and source native interface.
    
    <center>
    <img src="/interfaces/data_product_hub/activation/image%20(27).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>

2. To consume the Data Product via **Rest APIs**, you first need to create the API using Talos Stack. Follow the steps listed in the [Talos Stack documentation](/resources/stacks/talos/) to create the API. 

3. Edit the template by providing, the API URL and API key and your actual query by taking help from the query example given in the template as shown below and run the code.
    - Rest APIs template
        
        ```python
        # Import necessary libraries
        import requests
        import pandas as pd
        import json
        
        # API URL and API key
        api_url = "https://lucky-possum.dataos.app/lens2/api/public:corp-market-performance/v2/load"
        apikey = 'api key here'
        
        # API payload, enter YOUR_QUERY here.
        payload = json.dumps({
            "query": {
                YOUR_QUERY
            }
        })
        
        # Query Example: This is how your query should look like.
        
            # "query": {
            #     "measures": [
            #         "sales.total_quantities_sold", 
            #         "sales.proof_revenue"
            #     ],
            #     "dimensions": [
            #         "inventory.warehouse"
            #     ],
            #     "timeDimensions": [
            #         {
            #             "dimension": "sales.invoice_date",
            #             "granularity": "day"
            #         }
            #     ],
            #     "limit": 1000,
            #     "responseFormat": "compact"
            # }
        
        # Headers
        headers = {
            'Content-Type': 'application/json',
            'apikey': apikey
        }
        
        # Fetch data from API
        def fetch_data_from_api(api_url, payload, headers=None):
            response = requests.post(api_url, headers=headers, data=payload)
            
            if response.status_code == 200:
                data = response.json()
                df = pd.json_normalize(data['data'])  # Create DataFrame
                return df
            else:
                print(f"Error: {response.status_code}")
                return None
        
        # Main execution
        if __name__ == "__main__":
            data = fetch_data_from_api(api_url, payload, headers=headers)
            
            if data is not None:
                print("Data Frame Created:")
                print(data.head())  # Show the first few rows of the DataFrame
                print("Ready for AI/ML model building.")
            else:
                print("Failed to fetch data.")
        ```
        
4.  To consume the Data Product via the **PostgreSQL** interface, you need to provide the `dbname`,  `user`, `password`,  `host`, and `port` of your PostgreSQL server in the code, also write the query in the query section, and run the code.
    - PostgreSQL template
        
        ```python
        # Import libraries
        import psycopg2
        import pandas as pd
        from sqlalchemy import create_engine
        
        # Database connection details
        dbname = "postgres"
        user = "postgres"
        password = "***********************"
        host = "tcp.lucky-possum.dataos.app"
        port = "6432"
        
        # SQL query
        query = " YOUR_SQL_QUERY_HERE "
        # Your query should look like this: query = "SELECT total_quantities_sold, product_id FROM sales;"
        
        # Function to connect to the database and execute the query
        def connect_and_query(dbname, user, password, host, port, query):
            conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
            df = pd.read_sql(query, conn)
            conn.close()
            return df
        
        # Main execution
        if __name__ == "__main__":
            data = connect_and_query(dbname, user, password, host, port, query)
            
            if data is not None:
                print("Data Frame Created:")
                print(data.head())
                
                # Ready for AI/ML model building
            else:
                print("Failed to fetch data.")
        
        ```
        
5. To consume the Data Product via **GraphQL**, you must provide your GraphQL API URL,  API key, and GraphQL query as shown in the template.
    - GraphQL template
        
        ```python
        # Import libraries
        import requests
        import pandas as pd
        import json
        
        # API URL and API key
        graphql_url = "https://lucky-possum.dataos.app/lens2/api/public:corp-market-performance/v2/graphql"
        apikey = 'api key here'
        
        # Placeholder for the GraphQL query
        graphql_query = """
        {
          inventoryData {
            YOUR_FIELDS_HERE  # Replace this with actual fields
          }
        }
        """
        
        # Your GraphQL query should look similar to this
        # graphql_query = """
        # {
        #   inventoryData {
        #     {}  # Using the measure variable
        #     sales_proof_revenue
        #     inventory_total_bottles_on_hand
        #     inventory_total_cases_on_hand
        #     sales_invoice_date
        #   }
        # }
        # """
        
        # Convert the query to JSON payload
        payload = json.dumps({
            "query": graphql_query
        })
        
        headers = {
            'Content-Type': 'application/json',
            'apikey': apikey
        }
        
        # Function to fetch data from GraphQL API
        def fetch_data_from_graphql(graphql_url, payload, headers=None):
            response = requests.post(graphql_url, headers=headers, data=payload)
            
            if response.status_code == 200:
                data = response.json()
                df = pd.json_normalize(data['data']['inventoryData'])  # Normalize the JSON data to create a DataFrame
                return df
            else:
                print(f"Error: {response.status_code}")
                return None
        
        # Main execution
        if __name__ == "__main__":
            data = fetch_data_from_graphql(graphql_url, payload, headers=headers)
            
            if data is not None:
                print("Data Frame Created:")
                print(data.head())  # Display the first few rows of the DataFrame
                
                # Extend this code for AI/ML use cases
                # You can now preprocess the 'data' DataFrame for AI/ML tasks
                # Example: from sklearn.model_selection import train_test_split, etc.
            else:
                print("Failed to fetch data.")
        ```
        
6. After executing the code, you are ready to build AI/ML models.

## An alternative way to consume the Data Product via Jupyter Notebooks

1. Download the Postman collection and open it on the Postman application. 
    
    <center>
    <img src="/interfaces/data_product_hub/activation/annotely_image%20(28).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>
   
2. Hit the endpoint. 
    
    <center>
    <img src="/interfaces/data_product_hub/activation/image%20(28).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>
  
3. Navigate to the ‘Code’ icon.

    <center>
    <img src="/interfaces/data_product_hub/activation/image%20(29).png" alt="DPH" style="width:15rem; border: 1px solid black;" />
    </center>

4. From the drop-down menu, select ‘Python - Requests’ as shown below.

    <center>
    <img src="/interfaces/data_product_hub/activation/image%20(30).png" alt="DPH" style="width:30rem; border: 1px solid black;" />
    </center>

5. Copy the code snippet and paste it on your Jupyter Notebook.
    
    <center>
    <img src="/interfaces/data_product_hub/activation/image%20(31).png" alt="DPH" style="width:30rem; border: 1px solid black;" />
    </center>

6. Execute the code and you are ready to build your AI/ML model. Successful execution will look like the following.
    
    <center>
    <img src="/interfaces/data_product_hub/activation/image%20(32).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>   