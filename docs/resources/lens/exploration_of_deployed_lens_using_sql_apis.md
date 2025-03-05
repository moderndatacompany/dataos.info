# Exploration of Lens using SQL APIs

Lens exposes a PostgreSQL-compatible interface, enabling interaction with the semantic model(Lens) using SQL API. The PostgreSQL client tool `psql` is required to query the database and manage Lens data.


## Prerequisites

- **Active Lens:** Ensure the Lens is active and properly set up if deployed on DataOS to interact with it.

- **DataOS API Key:** When prompted for a password, use the DataOS API Key as the password. To retrieve the API Key, run the following command in the terminal:

    ```bash
    dataos-ctl user apikey get

    #Expected Output

    TOKEN                                                   │  TYPE  │        EXPIRATION         │                   NAME                     
    ───────────────────────────────────────────────────────────────────────────────────────────────────────────┼────────┼───────────────────────────┼────────────────────────────────────────────
    dG9rZW5fdXJnZW50bHlfZ2VuZXJhbGx5X2J1cnN0aW5nX2dvYmJsZXIuOGU1Yjg5MDktZjk5My00ZDkyLTkzMGQtZTMxZDYxYTRhMjAz │ apikey │ 2024-12-06T05:30:00+05:30 │ token_urgently_generally_bursting_gobbler  
    ```

    If the API Key is not already available, create one using the following command:

    ```bash
    dataos-ctl user apikey create -n ${name-of-apikey} -i ${user-id} -d ${duration}
    ```

    For example, if the user name is iamgroot:

    ```bash
    dataos-ctl user apikey create -n test_api_key -i aayushisolanki -d 24h

    #Expected_Output
    INFO[0000] 🔑 user apikey...                             
    INFO[0003] 🔑 user apikey...complete                     

                                    TOKEN                                 │  TYPE  │        EXPIRATION         │     NAME      
    ───────────────────────────────────────────────────────────────────────┼────────┼───────────────────────────┼───────────────
    dGVzdF9hcGlfa2V5LjZjYmE2Nzg0LTIyNDktNDBjMy1hZmNhLTc1MmZlNjM3OWExZA== │ apikey │ 2024-11-29T12:30:00+05:30 │ test_api_key  
    ```

To interact with Lens, the following options are available:

- **Postgreql client (psql):** The `psql` command-line tool enables direct interaction with a PostgreSQL database. It is used to run queries, manage the database, and perform various administrative tasks. Ensure that postgresql-client-16 is installed. If it is not already installed, download and install postgresql-client-16 for your operating system using [this link](https://www.postgresql.org/download/).

- **VS Code extension:** Use the PostgreSQL Client extension for Visual Studio Code. This extension enables SQL query execution and database management within VS Code.

## Postgresql client (psql)

The `psql` command-line tool is required to interact with Lens through PostgreSQL. Specifically, `postgresql-client-16` must be installed, as this version includes the necessary tools to connect and query the database. 

### **Retrieve Lens**

Before using SQL APIs to explore a Lens, the Lens needs to be retrieved from the workspace. This can be done in different ways depending on whether the Lens is running locally or is deployed on DataOS.

- **Deployed Lens**

    If a user has created a Lens, he can verify its name in the `deployment.yml` file or retrieve it by running the following command:

    === "Command"

        ```bash
        dataos-ctl resource get -t lens -w ${workspace} 
        ```
    === "Example"

        ```bash
        # For a workspace named "curriculum", the command and its expected output are as follows:
        dataos-ctl resource get -t lens -w curriculum
        # Expected Output
        INFO[0000] 🔍 get...                                     
        INFO[0000] 🔍 get...complete                             

                    NAME             | VERSION |  TYPE   | WORKSPACE  | STATUS |   RUNTIME   |     OWNER        
        -------------------------------|---------|---------|------------|--------|-------------|-------------------
                productaffinity              | v1      | cluster | curriculum | active | running:1   |     ironman  
        ```

    To explore the Lens created by someone else in a particular worksapce use the following command:

    === "Command"

        This command requires specifying the workspace name to filter the Lens accordingly.

        ```bash
        dataos-ctl resource get -t lens -w ${workspace} -a
        ```

    === "Example"

        ```bash
        # For a workspace named "curriculum", the command and its expected output are as follows:
        dataos-ctl resource get -t lens -w curriculum -a
        # Expected Output
        INFO[0000] 🔍 get...                                     
        INFO[0000] 🔍 get...complete                             

                    NAME             | VERSION |  TYPE   | WORKSPACE  | STATUS |   RUNTIME   |     OWNER        
        -------------------------------|---------|---------|------------|--------|-------------|-------------------
                sales-analysis               | v1      | cluster | curriculum | active | running:1   |     ironman  
                productaffinity             | v1      | cluster | curriculum | active | running:2   |     thanos  
        ```


### **Connect to Lens using `psql`**

After retrieving the name of the Lens, the following steps describe how to connect to it using the `psql` command. Again, the host parameter depends on whether the Lens is running locally or deployed on DataOS.


1. Open the terminal.

2. Use the following command to connect to the Lens using `psql`:
    
    ```bash
    psql -h ${host_name} -p 6432 -U ${user-name} -d ${lens:<workspace-name>:<lens-name>} 
    ```
    
    For deployed environment, use the following connection string:
    
    ```bash
    psql -h tcp.liberal-monkey.dataos.app -p 6432 -U iamgroot -d lens:curriculum:product360
    ```
    Replace <context> with the appropriate context for the deployed Lens. For example, in `liberal-monkey.dataos.app`, the context is `liberal-monkey`. Additionally, replace the workspace name with the name of the actual workspace where Lens is deployed. For instance, `public`, `sandbox` etc.

3. When prompted, enter the DataOS API Key as the password.

4. The connection is successful. Verify the connection by listing the available relations using the `\dt` command:
    
    ```sql
    iamgroot=> \dt
    ```
    
    **Expected output**
    
    ```bash
    Password for user iamgroot: 
    psql (16.3 (Ubuntu 16.3-1.pgdg22.04+1), server 14.2 (Lens2/sales400 v0.35.41-01))
    Type "help" for help.
    
    iamgroot=> \dt
                    List of relations
     Schema |          Name           | Type  |     Owner      
     --------+-------------------------+-------+----------------
     public | customer                | table | aayushisolanki
     public | customer_lifetime_Value | table | aayushisolanki
     public | product                 | table | aayushisolanki
     public | repeat_purchase_rate    | table | aayushisolanki
     public | sales                   | table | aayushisolanki
     public | stock_status            | table | aayushisolanki
     public | warehouse_inventory     | table | aayushisolanki
     (7 rows)
    ```
    
5. To exit `psql`, type:
    
    ```sql
    iamgroot=> \q
    ```

## Postgresql VS Code extension

One can also use the PostgreSQL extension on VS Code. Use the following details to connect to the Postgresql interface:

1. Install the PostgreSQL Client extension.

2. Click the 'Create Connection' button on the left side panel.

3. Configure the connection with the following details and click '+connect':

    | **POSTGRES PROPERTY** | **DESCRIPTION** | **EXAMPLE** |
    | --- | --- | --- |
    | Host  | host name | `localhost` |
    | Port | port name | `25432` |
    | Database | database name | `postgres` |
    | Username | dataos-username | `postgres` or `iamgroot` |
    | Password | dataos-user-apikey | `dskhcknskhknsmdnalklquajzZr=` |

4. Once connected, hover over the postgres folder and click the terminal icon to open the terminal for querying.

5. Execute queries in the terminal as needed. For example:

```bash
postgres=> \dt #listing all the tables in the connected database.

#Expected_output
 Schema |         Name         | Type  |  Owner   
--------+----------------------+-------+----------
 public | channel              | table | postgres
 public | customer             | table | postgres
 public | product_analysis     | table | postgres
 public | products             | table | postgres
 public | transaction_analysis | table | postgres
 public | transactions         | table | postgres
(6 rows)
```

## Commands

One can also introspect the semantic model in a Postgres-native way by querying tables in information_schema or using backslash commands(opens in a new tab):

Here are some more commands for reference.

| Command Description                              | Command Example                 |
|--------------------------------------------------|---------------------------------|
| Show the schema and details of a specific table  | `\d [table_name]` E.g.,`\d customers`|
| List all databases in the PostgreSQL server      | `\l`                            |
| List all roles and users                         | `\du`                           |
| List all schemas in the database                 | `\dn`                           |
| List all views in the connected database         | `\dv`                           |
| Exit the PostgreSQL prompt                       | `\q`                            |

After connecting, one can run queries in the Postgres dialect, just like the following one:

```sql
SELECT 
	 customer.country,
	 purchase.purchase_date,
	 MEASURE(purchase.total_spend)
 FROM
	 customer
	 CROSS JOIN purchase
 WHERE
	 (purchase.purchase_date BETWEEN '2024-01-01T15:37:55' AND '2024-12-31T15:38:02' AND (customer.country = 'Australia'))
 GROUP BY 1,2
 LIMIT 
	 10
 OFFSET 
	 0
```

## Query format

Please refer to the  [SQL API reference](/resources/lens/sql_apis/query_format/) to explore the query format and
see whether a specific expression or function is supported and whether it can be used in selection (e.g., `WHERE`) or projection (e.g., `SELECT`) parts of SQL queries. 

