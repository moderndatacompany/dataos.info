# Customer Data in Microsoft Azure

This article explains the steps to access data from Azure SQL Database, which is a relational database-as-a-service (DBaaS) in the Microsoft Cloud (Azure), and register metadata with DataOS Metis.

# Connect with Sample Data

In this tutorial, you learn how to use the Azure portal and connect with the sample data in it:

1. Log in to the [Azure portal](https://portal.azure.com/).
2. Set up a server-level IP firewall rule using the Azure portal.
3. Connect to the sample database. 
4. Access sample table with customer data.
5. Show the customer data.
6. Copy the connection string for the database. You will need a connection string to create a depot resource in DataOS to access this data.

The following steps are performed:

1. On Microsoft Home, click on SQL databases. 

    <img src="Customer%20Data%20in%20Microsoft%20Azure/azur_home.png" 
      alt="Picture"
        style="display: block; margin: auto" />

1. Select on the sample database.

    <img src="Customer%20Data%20in%20Microsoft%20Azure/Untitled.png" 
      alt="Picture"
        style="display: block; margin: auto" />

1. Click on Set server firewall.

    <img src="Customer%20Data%20in%20Microsoft%20Azure/Untitled%201.png" 
      alt="Picture"
        style="display: block; margin: auto" />

1. This will give you start and endpoints of access for you server.

    <img src="Customer%20Data%20in%20Microsoft%20Azure/Untitled%202.png" 
      alt="Picture"
        style="display: block; margin: auto" />

1. Login to the Query Editor.

    <img src="Customer%20Data%20in%20Microsoft%20Azure/Untitled%203.png" 
      alt="Picture"
        style="display: block; margin: auto" />

1. You can see the sample tables available. In this use case, we have used Customers and Products_data tables.

    <img src="Customer%20Data%20in%20Microsoft%20Azure/Untitled%204.png" 
        alt="Picture"
        style="display: block; margin: auto" />

1. Click on the Connection String. Copy the JDBC details for authentication.

    <img src="Customer%20Data%20in%20Microsoft%20Azure/Untitled%205.png" 
      alt="Picture"
        style="display: block; margin: auto" />

# Register the Metadata

Run the following Scanner YAML to register the metadata for your data source with Metis. It will capture schema details such as table names, constraints, primary keys, etc., for this external data source. This will allow you to run queries on the data.

```yaml
version: v1beta1
name: scanner-azure-sql-db    # Name of workflow 
type: workflow                # Type of YAML
tags:                        
  - scanner
  - azure-sql-db
description: Scans metadata of Azure SQL Database tables for dbo schema and registers them as datasets on Datanet  
workflow: 
  dag:
    - name: azure-sql-db-scanner     # Name of the job shown on Runnables(Dag)
      description: The job scans metadata of Azure SQL Database tables for dbo schema and registers them as datasets  
      spec:
        tags:                   
          - azure-sql-db
        stack: scanner               # Name of stack that will process the data
        scanner:
          depot: dataos://azuresqldb:dbo
```

To learn more, refer to
[Scanner](../../../Integration%20&%20Ingestion/Scanner.md).