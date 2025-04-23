# Postgres integration

You can develop data applications on top of your Data Product by PostgreSQL API endpoint, to do so follow the below steps:

1. Go to the Access Options tab of your Data Product, and navigate to the App Development section.
    
    <center>
    <img src="/interfaces/data_product_hub/activation/access.png" alt="DPH" style="width:50rem; border: 1px solid black;" />
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