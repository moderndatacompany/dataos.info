# **Depot**

**DataOS Depot** eliminates the need to deal with a source system’s different protocols, credentials, and connection schemas each time you need to access data. It abstracts away these system intricacies and acts as a bridge that lets you connect to the data sources.

Through depot, you can connect and access data from managed & unmanaged object storage like Amazon S3, Azure Blob Storage, streaming sources like Pulsar, and relational & non-relational databases like PostgreSQL, MySQL, BigQuery, NoSQL.

> You can visualise depots as the registration of data locations to be made available to DataOS. Depot Service accomplishes this by assigning a unique address to every source system. This allows you to access and call the datasets within that source system using UDL (Universal Data Link). A UDL has the following format:
> 

 `dataos://[depot]:[collection]/[dataset]`

The UDL gives you direct access to the datasets without having to specify the credentials again. You can now perform operations such as transformation, assigning policies or tags, and a lot more on your dataset. 

The way this UDL address is inferred depends on the source system. For instance, a Relational Database might use the term Schema instead of Collection, and Table instead of Dataset; while for a simple file storage system, Collection can correspond to Folder and Dataset can correspond to File. The good thing about Depot is that, once you have created it, you don’t have to worry about these differing nomenclatures, it brings in uniformity. You can learn more about this under [Create Depot](Depot/Create%20Depot.md) page.

Once the depot has been created, everyone in your organisation can access the datasets present within the particular source system in a secure manner. While a depot allows you to access data, it also assigns the **default access policies** to secure it. Further, you can define and use custom Access Policies for the depot and Data Policies for a specific dataset in the depot. To learn more about it, refer to the [Security](../Security.md) page.


> 🗣️ In case you have not yet realised it, Depot gives you ‘access’ to the data, which means you are neither moving the data away from your source system nor are you creating copies of it. Of course, if you want to accomplish either of these tasks, with DataOS, you can do that too.


## **Depot Service**

Depot Service is a DataOS service that creates and manages the Depot construct. Depot Service converts the DataOS address(UDL) to an address understood by the source system. It has a Postgre-based database where it stores the information on all the created Depots.

- In simple words, you can envisage that Depot Service creates a tabulation of your data, which can now be accessed with Minerva query engine, DataOS stacks, Lens, and other components of DataOS.
- It allows you to examine or introspect the Depot, or the storage engine indicated by the Depot. In other words, once the depot is created you can get the details like datasets present within, dictionary, constraints, partition, and indexing information. To understand how this is done, check out the [Scanner](Scanner.md) stack.

To learn more about the Depot service and its functionalities, refer to this page: [Depot Service](../About%20DataOS/Primitives%20Resources/Depot%20Service%20%5BWIP%5D.md)

You are now ready to start creating and using depots.

## **Create Depot**

Depot declaration and definition are simplified using the YAML format. Basically, to create a depot, all you need to do is, write a YAML configuration file and apply it through DataOS CLI. Check out the detailed steps on how to
[Create Depot](Depot/Create%20Depot.md).

## **Use Depot**

The UDLs that get constituted whenever you create a depot help you access the data without moving it. You will use these UDLs in various stacks of DataOS. For instance, within the Flare stack, you will mention the UDLs as the addresses of your input and output datasets.

```yaml
#just a section of the complete YAML file of a Flare workflow  
       inputs:                                               
         - name: customer_connect
           dataset: dataos://crmbq:demo/customer_profiles #example of input UDL
       outputs:
         - name: output01
           depot: dataos://filebase:raw01 #example of output UDL
```

Stacks in DataOS are the Programming Paradigms & Extension Points of our Runnable Resources such as workflow & service. I can see your eyes rolling with exasperation! 

Think of Stacks as the different ways in which you should communicate with the machine to perform various actions in DataOS. We have many stacks that can be used within those primitives (workflow & service), for example, Scanner is our stack for introspecting Depots, Toolbox is our stack for managing Icebase DDL and DML, and so on. To read about them further, refer to [Stacks](../About%20DataOS/Stacks.md).

### **Compatibility of Depots with Stacks**

Take a look at the table given below. It shows which of the different Depot Types are supported with which Stacks of DataOS.

|   |   |   |   |   |
|---|---|---|---|---|
| **Depot Type** | **Flare** | **Benthos** | **Minerva** | **Scanner** |
Amazon S3 | RW/PUSHDOWN^ | <span style="color:maroon">WIP</span> | <span style="color:green">READ</span> | <span style="color:blue">YES</span> |
Amazon Redshift	| RW/PUSHDOWN	| <span style="color:maroon">WIP</span>	| <span style="color:green">READ</span> | <span style="color:blue">YES</span> |
Apache Kafka	| RW	| <span style="color:green">READ</span>	| <span style="color:green">READ</span>	| <span style="color:blue">YES</span> |
Apache Pulsar	| RW/PUSHDOWN |	<span style="color:green">READ</span>	| <span style="color:green">READ</span>	| <span style="color:blue">YES</span> |
Azure Blob File Storage	| RW/PUSHDOWN^	| <span style="color:maroon">WIP</span>	| <span style="color:green">READ</span>	| <span style="color:blue">YES</span> |
BigQuery |	RW/PUSHDOWN	| <span style="color:maroon">WIP</span>	| <span style="color:green">READ</span> |	<span style="color:blue">YES</span> |
Elasticsearch |	RW/PUSHDOWN |	<span style="color:maroon">WIP</span> |	<span style="color:green">READ</span>	| <span style="color:blue">YES</span> |
Google Cloud Storage |	RW/PUSHDOWN^ |	<span style="color:maroon">WIP</span> |	<span style="color:green">READ</span> |	<span style="color:blue">YES</span> |
JDBC |	RW/PUSHDOWN |	<span style="color:maroon">WIP</span> |	<span style="color:green">READ</span> |	<span style="color:blue">YES</span> |
MSSQLSERVER |	RW/PUSHDOWN |	<span style="color:maroon">WIP</span> |	<span style="color:green">READ</span> |	<span style="color:blue">YES</span> |
MySQL |	RW/PUSHDOWN |	<span style="color:maroon">WIP</span> |	<span style="color:green">READ</span> |	<span style="color:blue">YES</span> |
Oracle |	RW/PUSHDOWN |	<span style="color:maroon">WIP</span> |	<span style="color:green">READ</span> |	<span style="color:blue">YES</span> |
PostgreSQL |	RW/PUSHDOWN |	<span style="color:maroon">WIP</span> |	<span style="color:green">READ</span> |	<span style="color:blue">YES</span> |
Redis |	WIP |	<span style="color:maroon">WIP</span> |	<span style="color:green">READ</span> |	<span style="color:blue">YES</span> |
Snowflake |	RW/PUSHDOWN |	<span style="color:maroon">WIP</span> |	<span style="color:green">READ</span> |	<span style="color:blue">YES</span> |


**RW**: read & write  |  **WIP**: work in progress  |  **PUSHDOWN**: Is pushdown of queries supported  |  **PUSHDOWN^**: Pushdown is supported only for Parquet format

In case you do not know what Pushdown is, do not worry. We got you! Learn it here: [Minerva](../Analytics/Minerva/Performance%20Tuning.md)
If you create a depot for a relational database, you can include it in a cluster and run SQL queries on the data by using [Workbench](../Getting%20Started%20-%20DataOS%20Documentation/Data%20Management%20Capabilities/GUI/GUI%20Applications/Workbench.md).

> Furthermore, using Depots significantly reduces the data breach risks and makes the life of the Infosec division of your enterprise easier.

### **Limit File Format**

Another important function that a Depot can play is to limit the file type which you can read from and write to a particular data source. In the ‘spec’ section of YAML config file, simply mention the ‘format’ of the files you want to allow access for.

```yaml
depot:
  type: S3
  description: <description>
  external: true
    spec:
       scheme: <s3a>                      
       bucket: <bucket-name>               ****
       relativePath: "raw" 
       format: <format>  **#Mention the file format, such as JSON, to only allow that file type**
```

## **Managed/Unmanaged Depots**

Managed depot is the term we use for the depots pointing to some of the internal storage options you get within DataOS. By default, we currently provide you with three different types of managed depots:

1. Icebase: To store data on which you might want to perform OLAP processes. 
We call it a managed depot because with it we provide certain in-built functionalities such as Data Maintenance, Schema evolution, Time-travel on the dataset, etc. You can directly perform these actions through DataOS CLI, without using stacks like Flare or Data Toolbox. Learn more about this on the Storage page: [Storage](../Storage.md) 
2. Fastbase: To handle streaming data workloads. 
Being a managed depot, you can again execute commands such as create datasets, list topics, etc. directly from DataOS CLI. Learn more about this on the Storage page: [Storage](../Storage.md) 
3. Dropzone: You can use this managed depot as a sink for all the different types of data you don’t currently want to perform ELT/ETL processes on, such as file formats of the kind parquet, csv, pdfs; audio-video files, etc. Think of it as a raw data or a file store. While Icebase-type depot enforces structure, Dropzone does not.

For an unmanaged depot, the supported functionalities depend on the source system with which the depot connects.

## **Delete Depot**

You can delete the depot through DataOS CLI. Simply run the command mentioned below.

```yaml
dataos-ctl delete -t depot -n <name of depot>
```

> 📖 Best Practice: It is part of the best practice to delete the Resources which are no longer in use. They save you both time and money!

## **Depot Templates**

We have curated a list of ready-to-use YAML configuration files to create depots accessing commonly used data sources. To find this list, refer to 
[Depot Config Templates](Depot/Depot%20Config%20Templates.md).