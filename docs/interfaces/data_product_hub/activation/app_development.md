# Postgres and GraphQL integration

You can develop data applications on top of your Data Product either by PostgreSQL or GraphQL API endpoint, to do so follow the below steps:

1. Go to the Access Options tab of your Data Product, and navigate to the App Development section.
    
    <center>
    <img src="/interfaces/data_product_hub/activation/image%20(33).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>
  
2. To develop data applications using **PostgreSQL** API, You need to choose a PostgreSQL client like `psql` or any other client tool (e.g., pgAdmin, DBeaver) to connect to the database.

3. The connection string below is what you’ll need to connect to the PostgreSQL database. Execute the given string on your terminal, when prompted for a password, you'll enter your DataOS API key. 
    
    <center>
    <img src="/interfaces/data_product_hub/activation/image%20(34).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>

4. After entering the necessary details, ensure your connection is successful by testing. This makes sure you're connected and ready to start querying data. A successful connection will look like the following where you can start querying:
    
    ```bash
    psql -h tcp.lucky-possum.dataos.app -p 6432 -U iamgroot -d lens:public:company-intelligence~  
    Password for user iamgroot
    psql (14.13 (Ubuntu 14.13-0ubuntu0.22.04.1), server 14.2 (Lens2/public:company-intelligence v0.35.60-8))
    Type "help" for help.
    lens:public:company-intelligence~=> 
    ```
    
5. To develop the data application using **GraphQL**, click on the ‘Explore’ button as shown below. 
    
    <center>
    <img src="/interfaces/data_product_hub/activation/image%20(35).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>

6. Navigate to the GraphQL tab, start by building your GraphQL query. 
    
    <center>
    <img src="/interfaces/data_product_hub/activation/image%20(36).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>

7. You can also try out the sample query, by clicking on the ‘Try it out’ link in the **Sample Query** section in the **Access Options** tab. It will open the GraphQL playground with a sample query which you can test and then write your queries.
    
    <center>
    <img src="/interfaces/data_product_hub/activation/image%20(37).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>

8. When you run your query, verify that the data returned matches your expectations. Since GraphQL lets you be very specific in requesting fields, double-check to ensure your query retrieves exactly what you need.
    
    <center>
    <img src="/interfaces/data_product_hub/activation/image%20(38).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>

9. Copy the provided GraphQL endpoint and the necessary authentication details (DataOS API key) and integrate them into your application, so your app can access the data.
    
    <center>
    <img src="/interfaces/data_product_hub/activation/image%20(39).png" alt="DPH" style="width:50rem; border: 1px solid black;" />
    </center>