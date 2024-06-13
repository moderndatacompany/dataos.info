## **Templates of Depot for different source systems**

To facilitate the creation of depots accessing commonly used data sources, we have compiled a collection of pre-defined manifest templates. These templates serve as a starting point, allowing you to quickly set up depots for popular data sources. 

To make the process of creating a Depot configuration easier, we provide a set of predefined templates for various data sources. These templates serve as a starting point for configuring your Depot based on the specific data source you are working with. Simply choose the template that corresponds to your organization's data source and follow the instructions provided to fill in the required information.

<aside class=callout>

🗣️ When using these templates, you will need to populate the key-value properties in the manifest file with the appropriate values for your data source. This requires a basic understanding of your organization's data infrastructure and the necessary credentials or connection details.

</aside>

You can access these templates by visiting the following links: 


=== "Data <br> Warehouse"

    === "Amazon Redshift"

        DataOS provides the capability to establish a connection with the Amazon Redshift database. We have provided the template for the manifest file to establish this connection. To create a Depot of type ‘REDSHIFT‘, utilize the following template:

        <aside class=callout>
        🗣️ Please note that the credentials are directly specified in the depot manifest using the `connectionSecret`, whereas credentials are referred via [Instance Secret](./instance_secret.md) as `secrets` or `dataosSecrets`.      
        </aside>

        === "Inline Credentials"
            ```yaml title="redshift_v1.yaml"
            --8<-- "examples/resources/depot/data_warehouse/redshift/redshift_v1.yaml"
            ```

            Follow these steps to create the depot: 

            - **Step 1**: Create a manifest file. 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.            

        === "Instance Secret Reference"
            ```yaml title="redshift_v2alpha.yaml" 
            --8<-- "examples/resources/depot/data_warehouse/redshift/redshift_v2alpha.yaml"
            ```

            Follow these steps to create the depot: 

            - **Step 1**: Create Instance-secret to store the credentials, for more imformation about instance secret, refer to [Instance Secret](../resources/instance_secret.md). 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.
        

        **Requirements**
        To establish a connection with Redshift, the following information is required:

        - Hostname
        - Port
        - Database name
        - User name and password

        Additionally, when accessing the Redshift Database in Workflows or other DataOS Resources, the following details are also necessary:

        - Bucket name where the data resides
        - Relative path
        - AWS access key
        - AWS secret key

    === "Google BigQuery"

        DataOS enables the creation of a Depot of type 'BIGQUERY' to read data stored in BigQuery projects. Multiple Depots can be created, each pointing to a different project. To create a Depot of type 'BIGQUERY', utilize the following template:

        <aside class=callout>
        🗣️ Please note that the credentials are directly specified in the depot manifest using the `connectionSecret`, whereas credentials are referred via [Instance Secret](./instance_secret.md) as `secrets` or `dataosSecrets`.      
        </aside>

        === "Inline Credentials"

            ```yaml title="bigquery_v2alpha.yaml" 
            --8<-- "examples/resources/depot/data_warehouse/bigquery/bigquery_v1.yaml"
            ```
            Follow these steps to create the depot: 

            - **Step 1**: Create a manifest file. 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.            

        === "Instance Secret Reference"

            ```yaml title="bigquery_v2alpha.yaml" 
            --8<-- "examples/resources/depot/data_warehouse/bigquery/bigquery_v2alpha.yaml"
            ```
            Follow these steps to create the depot: 

            - **Step 1**: Create Instance-secret to store the credentials, for more imformation about instance secret, refer to [Instance Secret](../resources/instance_secret.md). 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.


        **Requirements**
        To establish a connection with BigQuery, the following information is required:

        - Project ID: The identifier of the BigQuery project.
        - Email ID: The email address associated with the BigQuery project.
        - Credential properties in JSON file: A JSON file containing the necessary credential properties.
        - Additional parameters: Any additional parameters required for the connection.

    === "Snowflake"
        DataOS provides integration with Snowflake, allowing you to seamlessly read data from Snowflake tables using Depots. Snowflake is a cloud-based data storage and analytics data warehouse offered as a Software-as-a-Service (SaaS) solution. It utilizes a new SQL database engine designed specifically for cloud infrastructure, enabling efficient access to Snowflake databases. To create a Depot of type 'SNOWFLAKE', you can utilize the following YAML template as a starting point:

        <aside class=callout>
        🗣️ Please note that the credentials are directly specified in the depot manifest using the `connectionSecret`, whereas credentials are referred via [Instance Secret](./instance_secret.md) as `secrets` or `dataosSecrets`.      
        </aside>

        === "Inline Credentials"

            ```yaml title="snowflake_v2alpha.yaml" 
            --8<-- "examples/resources/depot/data_warehouse/snowflake/snowflake_v1.yaml"
            ```   
            Follow these steps to create the depot: 

            - **Step 1**: Create a manifest file. 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.

        === "Instance Secret Reference"

            ```yaml title="snowflake_v2alpha.yaml" 
            --8<-- "examples/resources/depot/data_warehouse/snowflake/snowflake_v2alpha.yaml"
            ```
            Follow these steps to create the depot: 

            - **Step 1**: Create Instance-secret to store the credentials, for more imformation about instance secret, refer to [Instance Secret](../resources/instance_secret.md). 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.

        **Requirements**

        To establish a connection to Snowflake and create a Depot, you will need the following information:

        - Snowflake Account URL: The URL of your Snowflake account.
        - Snowflake Username: Your Snowflake login username.
        - Snowflake User Password: The password associated with your Snowflake user account.
        - Snowflake Database Name: The name of the Snowflake database you want to connect to.
        - Database Schema: The schema in the Snowflake database where your desired table resides.    
   

=== "Lakehouse or <br> Data Lake"

    === "Amazon S3"
        DataOS provides the capability to establish a connection with the Amazon S3 buckets. We have provided the template for the manifest file to establish this connection. To create a Depot of type ‘S3‘, utilize the following template:

        <aside class=callout>
        🗣️ Please note that the credentials are directly specified in the depot manifest using the `connectionSecret`, whereas credentials are referred via [Instance Secret](./instance_secret.md) as `secrets` or `dataosSecrets`.      
        </aside>

        === "Inline Credentials"

            ```yaml title="s3_v1.yaml" 
            --8<-- "examples/resources/depot/lakehouse/amazon_s3/s3_v1.yaml"
            ```  
            Follow these steps to create the depot: 

            - **Step 1**: Create a manifest file. 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.

        === "Instance Secret Reference"

            ```yaml title="s3_v2alpha.yaml" 
            --8<-- "examples/resources/depot/lakehouse/amazon_s3/s3_v2alpha.yaml"
            ```
            Follow these steps to create the depot: 

            - **Step 1**: Create Instance-secret to store the credentials, for more imformation about instance secret, refer to [Instance Secret](../resources/instance_secret.md). 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.

        **Requirements**

        To establish a connection with Amazon S3, the following information is required:

        - AWS access key ID
        - AWS bucket name
        - Secret access key
        - Scheme
        - Relative Path
        - Format


    
    === "ABFSS"

        DataOS enables the creation of a Depot of type 'ABFSS' to facilitate the reading of data stored in an Azure Blob Storage account. This Depot provides access to the storage account, which can consist of multiple containers. A container serves as a grouping mechanism for multiple blobs. It is recommended to define a separate Depot for each container. To create a Depot of type ‘ABFSS‘, utilize the following template:

        <aside class=callout>
        🗣️ Please note that the credentials are directly specified in the depot manifest using the `connectionSecret`, whereas credentials are referred via [Instance Secret](./instance_secret.md) as `secrets` or `dataosSecrets`.      
        </aside>

        === "Inline Credentials"

            ```yaml title="abfss_v1.yaml" 
            --8<-- "examples/resources/depot/lakehouse/abfss/abfss_v1.yaml"
            ``` 
            Follow these steps to create the depot: 

            - **Step 1**: Create a manifest file. 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.

        === "Instance Secret Reference"

            ```yaml title="abfss_v2alpha.yaml" 
            --8<-- "examples/resources/depot/lakehouse/abfss/abfss_v2alpha.yaml"
            ```
            Follow these steps to create the depot: 

            - **Step 1**: Create Instance-secret to store the credentials, for more imformation about instance secret, refer to [Instance Secret](../resources/instance_secret.md). 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.

        **Requirements**

        To establish a connection with Azure ABFSS, the following information is required:

        - Storage account name
        - Storage account key
        - Container
        - Relative path
        - Data format stored in the container    

    === "WASBS"

        DataOS enables the creation of a Depot of type 'WASBS' to facilitate the reading of data stored in Azure Data Lake Storage. This Depot enables access to the storage account, which can contain multiple containers. A container serves as a grouping of multiple blobs. It is recommended to define a separate Depot for each container.To create a Depot of type ‘WASBS‘, utilize the following template:

        <aside class=callout>
        🗣️ Please note that the credentials are directly specified in the depot manifest using the `connectionSecret`, whereas credentials are referred via [Instance Secret](./instance_secret.md) as `secrets` or `dataosSecrets`.      
        </aside>

        === "Inline Credentials"

            ```yaml title="wasbs_v1.yaml" 
            --8<-- "examples/resources/depot/lakehouse/wasbs/wasbs_v1.yaml"
            ``` 
            Follow these steps to create the depot: 

            - **Step 1**: Create a manifest file. 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.

        === "Instance Secret Reference"

            ```yaml title="wasbs_v2alpha.yaml" 
            --8<-- "examples/resources/depot/lakehouse/wasbs/wasbs_v2alpha.yaml"
            ```
            Follow these steps to create the depot: 

            - **Step 1**: Create Instance-secret to store the credentials, for more imformation about instance secret, refer to [Instance Secret](../resources/instance_secret.md). 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.

        **Requirements**

        To establish a connection with Azure WASBS, the following information is required:

        - Storage account name
        - Storage account key
        - Container
        - Relative path
        - Format            



    === "GCS"

        DataOS provides the capability to connect to Google Cloud Storage data using Depot. To create a Depot of Google Cloud Storage, in the type field you will have to specify type 'GCS', and utilize the following template:

        <aside class=callout>
        🗣️ Please note that the credentials are directly specified in the depot manifest using the `connectionSecret`, whereas credentials are referred via [Instance Secret](./instance_secret.md) as `secrets` or `dataosSecrets`.      
        </aside>

        === "Inline Credentials"

            ```yaml title="gcs_v1.yaml" 
            --8<-- "examples/resources/depot/lakehouse/gcs/gcs_v1.yaml"
            ```
            Follow these steps to create the depot: 

            - **Step 1**: Create a manifest file. 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.

        === "Instance Secret Reference"

            ```yaml title="gcs_v2alpha.yaml" 
            --8<-- "examples/resources/depot/lakehouse/gcs/gcs_v2alpha.yaml"
            ```
            Follow these steps to create the depot: 

            - **Step 1**: Create Instance-secret to store the credentials, for more imformation about instance secret, refer to [Instance Secret](../resources/instance_secret.md). 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.

        The Depot facilitates access to all documents that are visible to the specified user, allowing for text queries and analytics.

        **Requirements**

        To establish a connection with Google Cloud Storage (GCS), the following information is required:

        - GCS Bucket
        - Relative Path
        - GCS Project ID
        - GCS Account Email
        - GCS Key

    === "Icebase"

        DataOS provides the capability to establish a connection with the Icebase Lakehouse over Amazon S3 or other object storages. We have provided the template for the manifest file to establish this connection. To create a Depot of type ‘S3‘, utilize the following template:

        <aside class=callout>
        🗣️ Please note that the credentials are directly specified in the depot manifest using the `connectionSecret`, whereas credentials are referred via [Instance Secret](./instance_secret.md) as `secrets` or `dataosSecrets`.      
        </aside>

        === "Inline Credentials"

            ```yaml title="icebase_v1.yaml" 
            --8<-- "examples/resources/depot/lakehouse/icebase/icebase_v1.yaml"
            ``` 
            Follow these steps to create the depot: 

            - **Step 1**: Create a manifest file. 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.

        === "Instance Secret Reference"

            ```yaml title="icebase_v2alpha.yaml" 
            --8<-- "examples/resources/depot/lakehouse/icebase/icebase_v2alpha.yaml"
            ```
            Follow these steps to create the depot: 

            - **Step 1**: Create Instance-secret to store the credentials, for more imformation about instance secret, refer to [Instance Secret](../resources/instance_secret.md). 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.


        **Requirements**

        To establish a connection with Amazon S3, the following information is required:

        - AWS access key ID
        - AWS bucket name
        - Secret access key
        - Scheme
        - Relative Path
        - Format    

=== "Streaming <br> Source"

    === "Apache pulsar"

        DataOS provides the capability to create a Depot of type 'PULSAR' for reading topics and messages stored in Pulsar. This Depot facilitates the consumption of published topics and processing of incoming streams of messages. To create a Depot of type 'PULSAR,' utilize the following template:

        === "Inline Credentials"

            ```yaml title="pulsar_v1.yaml" 
            --8<-- "examples/resources/depot/streaming_source/apache_pulsar/pulsar_v1.yaml"
            ``` 
            Follow these steps to create the depot: 

            - **Step 1**: Create a manifest file. 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.

        **Requirements**

        To establish a connection with Pulsar, the following information is required:

        - Admin URL
        - Service URL

    === "Eventhub"

        DataOS provides the capability to connect to Eventhub data using Depot. The Depot facilitates access to all documents that are visible to the specified user, allowing for text queries and analytics. To create a Depot of Eventhub, in the type field you will have to specify type 'EVENTHUB', and utilize the following template:

        <aside class=callout>
        🗣️ Please note that the credentials are directly specified in the depot manifest using the `connectionSecret`, whereas credentials are referred via [Instance Secret](./instance_secret.md) as `secrets` or `dataosSecrets`.      
        </aside>

        === "Inline Credentials"

            ```yaml title="eh_v1.yaml" 
            --8<-- "examples/resources/depot/streaming_source/eventhub/eh_v1.yaml"
            ``` 
            Follow these steps to create the depot: 

            - **Step 1**: Create a manifest file. 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.

        === "Instance Secret Reference"

            ```yaml title="eh_v2alpha.yaml" 
            --8<-- "examples/resources/depot/streaming_source/eventhub/eh_v2alpha.yaml"
            ```
            Follow these steps to create the depot: 

            - **Step 1**: Create Instance-secret to store the credentials, for more imformation about instance secret, refer to [Instance Secret](../resources/instance_secret.md). 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.

        **Requirements**

        To establish a connection with Eventhub, the following information is required:

        - Endpoint
        - Eventhub Shared Access Key Name
        - Eventhub Shared Access Key   

    === "Kafka"

        DataOS allows you to create a Depot of type 'KAFKA' to read live topic data. This Depot enables you to access and consume real-time streaming data from Kafka. To create a Depot of type 'KAFKA', utilize the following template:

        === "Inline Credentials"

            ```yaml title="kafka_v1.yaml" 
            --8<-- "examples/resources/depot/streaming_source/kafka/kafka.yaml"
            ``` 
            Follow these steps to create the depot: 

            - **Step 1**: Create a manifest file. 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.

        **Requirements**

        - To connect to Kafka, you need:

        - To establish a connection to Kafka, you need to provide the following information:

        - KAFKA broker list: The list of brokers in the Kafka cluster. The broker list enables the Depot to fetch all the available topics in the Kafka cluster.
        Schema Registry URL

=== "NoSQL <br> Database"

    === "Elasticsearch"

        DataOS provides the capability to connect to Elasticsearch data using Depot. The Depot facilitates access to all documents that are visible to the specified user, allowing for text queries and analytics. To create a Depot of type ‘ELASTICSEARCH‘, utilize the following template:

        <aside class=callout>
        🗣️ Please note that the credentials are directly specified in the depot manifest using the `connectionSecret`, whereas credentials are referred via [Instance Secret](./instance_secret.md) as `secrets` or `dataosSecrets`.      
        </aside>

        === "Inline Credentials"

            ```yaml title="es_v1.yaml" 
            --8<-- "examples/resources/depot/nosql_db/elasticsearch/es_v1.yaml"
            ``` 
            Follow these steps to create the depot: 

            - **Step 1**: Create a manifest file. 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.

        === "Instance Secret Reference"

            ```yaml title="es_v2alpha.yaml" 
            --8<-- "examples/resources/depot/nosql_db/elasticsearch/es_v2alpha.yaml"
            ```  
            Follow these steps to create the depot: 

            - **Step 1**: Create Instance-secret to store the credentials, for more imformation about instance secret, refer to [Instance Secret](../resources/instance_secret.md). 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.

        **Requirements**

        To establish a connection with Elasticsearch, the following information is required:

        - Username
        - Password
        - Nodes (Hostname/URL of the server and ports)


    === "MongoDB"

        DataOS allows you to connect to MongoDB using Depot, enabling you to interact with your MongoDB database and perform various data operations. You can create a MongoDB Depot in DataOS by providing specific configurations. To create a Depot of type 'MONGODB', use the following template:

        <aside class=callout>
        🗣️ Please note that the credentials are directly specified in the depot manifest using the `connectionSecret`, whereas credentials are referred via [Instance Secret](./instance_secret.md) as `secrets` or `dataosSecrets`.      
        </aside>

        === "Inline Credentials"

            ```yaml title="mongo_v1.yaml" 
            --8<-- "examples/resources/depot/nosql_db/mongodb/mongo_v1.yaml"
            ```  
            Follow these steps to create the depot:

            - **Step 1**: Create a manifest file. 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.


        === "Instance Secret Reference"

            ```yaml title="mongo_v2alpha.yaml" 
            --8<-- "examples/resources/depot/nosql_db/mongodb/mongo_v2alpha.yaml"
            ```  
            Follow these steps to create the depot:

            - **Step 1**: Create Instance-secret to store the credentials, for more imformation about instance secret, refer to [Instance Secret](../resources/instance_secret.md). 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.


        **Requirements**

        To connect to MongoDB using DataOS and create a MongoDB Depot, the following information is required:

        - Subprotocol: The Subprotocol of the MongoDB Server
        - Nodes: Node
        - Username: The username for authentication.
        - Password: The password for authentication.


    === "Opensearch"

        DataOS provides the capability to connect to Opensearch data using Depot. The Depot facilitates access to all documents that are visible to the specified user, allowing for text queries and analytics. To create a Depot of Opensearch, in the type field you will have to specify type ‘ELASTICSEARCH‘, and utilize the following template:

        <aside class=callout>
        🗣️ Please note that the credentials are directly specified in the depot manifest using the `connectionSecret`, whereas credentials are referred via [Instance Secret](./instance_secret.md) as `secrets` or `dataosSecrets`.      
        </aside>

        === "Inline Credentials"

            ```yaml title="os_v2alpha.yaml" 
            --8<-- "examples/resources/depot/nosql_db/opensearch/os_v1.yaml"
            ```  
            Follow these steps to create the depot:

            - **Step 1**: Create a manifest file. 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.


        === "Instance Secret Reference"

            ```yaml title="os_v1.yaml" 
            --8<-- "examples/resources/depot/nosql_db/opensearch/os_v2alpha.yaml"
            ```
            Follow these steps to create the depot:

            - **Step 1**: Create Instance-secret to store the credentials, for more imformation about instance secret, refer to [Instance Secret](../resources/instance_secret.md). 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.

        **Requirements**

        To establish a connection with Opensearch, the following information is required:

        - Username
        - Password
        - Nodes (Hostname/URL of the server and ports)


=== "Relational <br> Database"

    === "JDBC"

        DataOS provides the capability to establish a connection to a database using the JDBC driver in order to read data from tables using a Depot. The Depot facilitates access to all schemas visible to the specified user within the configured database. To create a Depot of type ‘JDBC‘, utilize the following template:

        <aside class=callout>
        🗣️ Please note that the credentials are directly specified in the depot manifest using the `connectionSecret`, whereas credentials are referred via [Instance Secret](./instance_secret.md) as `secrets` or `dataosSecrets`.      
        </aside>

        === "Inline Credentials"

            ```yaml title="jdbc_v1.yaml" 
            --8<-- "examples/resources/depot/relational_db/jdbc/jdbc_v1.yaml"
            ``` 
            Follow these steps to create the depot:

            - **Step 1**: Create a manifest file.
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.

        === "Instance Secret Reference"

            ```yaml title="jdbc_v2alpha.yaml" 
            --8<-- "examples/resources/depot/relational_db/jdbc/jdbc_v2alpha.yaml"
            ```  
            Follow these steps to create the depot:

            - **Step 1**: Create Instance-secret to store the credentials, for more imformation about instance secret, refer to [Instance Secret](../resources/instance_secret.md). 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.

        **Requirements**
        To establish a JDBC connection, the following information is required:

        - Database name: The name of the database you want to connect to.
        - Subprotocol name: The subprotocol associated with the database (e.g., MySQL, PostgreSQL).
        - Hostname/URL of the server, port, and parameters: The server's hostname or URL, along with the - port and any additional parameters needed for the connection.
        - Username: The username to authenticate the JDBC connection.
        - Password: The password associated with the provided username.

        **Self-signed Certificate (SSL/TLS) Requirement**

        If you are connecting to relational databases using the JDBC API and encounter self-signed certificate (SSL/TLS) requirements, you can disable encryption by modifying the YAML configuration file. Simply provide the necessary details for the subprotocol, host, port, database, and use the params field to specify the appropriate parameters for your specific source system as shown below:

        === "v1"

            ``` yaml
            spec:             # version v1
              subprotocol:
              host: 
              port: 
              database:
              params:
            #use params for JDBC type connections where self-signed certificates have been enabled
            ```
        === "v2alpha"

            ``` yaml
            jdbc:             # version v2alpha
              subprotocol:
              host: 
              port: 
              database:
              params:
            #use params for JDBC type connections where self-signed certificates have been enabled

            ```

        The particular specifications to be filled within params depend on the source system.

    === "MySQL"

        DataOS allows you to connect to a MySQL database and read data from tables using Depots. A Depot provides access to all tables within the specified schema of the configured database. You can create multiple Depots to connect to different MySQL servers or databases. To create a Depot of type ‘MYSQL‘, utilize the following template:

        <aside class=callout>
        🗣️ Please note that the credentials are directly specified in the depot manifest using the `connectionSecret`, whereas credentials are referred via [Instance Secret](./instance_secret.md) as `secrets` or `dataosSecrets`.      
        </aside>

        **Use this template, if self-signed certificate is enabled.**


        === "Inline Credentials"

            ```yaml title="mysql_v1.yaml" 
            --8<-- "examples/resources/depot/relational_db/mysql/mysql_v1.yaml"
            ``` 
            Follow these steps to create the depot:

            - **Step 1**: Create a manifest file. 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI. 

        === "Instance Secret Reference"

            ```yaml title="mysql_v2alpha.yaml" 
            --8<-- "examples/resources/depot/relational_db/mysql/mysql_v2alpha.yaml"
            ```  
            Follow these steps to create the depot:

            - **Step 1**: Create Instance-secret to store the credentials, for more imformation about instance secret, refer to [Instance Secret](../resources/instance_secret.md). 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.

        **Requirements**

        To connect to a MySQL database, you need the following information:

        - Host URL and parameters: The URL or hostname of the MySQL server along with any additional parameters required for the connection.
        - Port: The port number used for the MySQL connection.
        - Username: The username for authentication.
        - Password: The password for authentication.

        **If self-signed certificates are not being used** by your organization, you can omit the params section within the spec:
            
        === "Inline Credentials"
        
            ``` yaml

            name: {{"mysql01"}}
            version: v1
            type: depot
            tags:
              - {{dropzone}}
              - {{mysql}}
            layer: user
            depot:
              type: MYSQL
              description: {{"MYSQL Sample data"}}
              spec:
                host: {{host}}
                port: {{port}}
              external: true
              connectionSecret:
                - acl: rw
                  type: key-value-properties
                  data:
                    username: {{username}}
                    password: {{password}}
            ```      

        === "Instance Secret Reference"

            ``` yaml
            name: {{"mysql01"}}
            version: v2alpha
            type: depot
            tags:
              - {{dropzone}}
              - {{mysql}}
            layer: user
            depot:
              type: MYSQL
              description: {{"MYSQL Sample data"}}
              mysql:
                host: {{host}}
                port: {{port}}
              external: true
              secrets:
                - name: {{nstance-secret-name}}-r
                  allkeys: true

                - name: {{instance-secret-name}}-rw
                  allkeys: true
            ```


    === "Microsoft SQL server"

        DataOS allows you to connect to a Microsoft SQL Server database and read data from tables using Depots. A Depot provides access to all tables within the specified schema of the configured database. You can create multiple Depots to connect to different SQL servers or databases. To create a Depot of type ‘SQLSERVER‘, utilize the following template:

        <aside class=callout>
        🗣️ Please note that the credentials are directly specified in the depot manifest using the `connectionSecret`, whereas credentials are referred via [Instance Secret](./instance_secret.md) as `secrets` or `dataosSecrets`.      
        </aside>

        **Use this template, if self-signed certificate is enabled.**

        === "Inline Credentials"

            ```yaml title="mssql_v1.yaml" 
            --8<-- "examples/resources/depot/relational_db/mssql_server/mssql_v1.yaml"
            ```         
            Follow these steps to create the depot:

            - **Step 1**: Create a manifest file. 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.            

        === "Instance Secret Reference"

            ```yaml title="mssql_v2alpha.yaml" 
            --8<-- "examples/resources/depot/relational_db/mssql_server/mssql_v2alpha.yaml"
            ```  
            Follow these steps to create the depot:

            - **Step 1**: Create Instance-secret to store the credentials, for more imformation about instance secret, refer to [Instance Secret](../resources/instance_secret.md). 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.
      

        **Requirements**
        To connect to a Microsoft SQL Server database, you need the following information:

        - Host URL and parameters: The URL or hostname of the SQL Server along with any additional parameters required for the connection.
        - Database schema: The schema in the database where your tables are located.
        - Port: The port number used for the SQL Server connection.
        - Username: The username for authentication.
        - Password: The password for authentication.

        If self-signed certificates are not being used by your organization, you can omit the params section within the spec:

        === "Inline Credentials"

            ``` yaml
            name: {{mssql01}}
            version: v1
            type: depot
            tags:
              - {{dropzone}}
              - {{mssql}}
            layer: user
            depot:
              type: JDBC
              description: {{MSSQL Sample data}}
              spec:
                subprotocol: sqlserver
                host: {{host}}
                port: {{port}}
                database: {{database}}
                params: {{'{"key":"value","key2":"value2"}'}}
              external: {{true}}
              connectionSecret:
                - acl: rw
                  type: key-value-properties
                  data:
                    username: {{username}}
                    password: {{password}}
            ```

        === "Instance Secret Reference"

            ``` yaml
            name: {{mssql01}}
            version: v2alpha
            type: depot
            tags:
              - {{dropzone}}
              - {{mssql}}
            layer: user
            depot:
              type: JDBC
              description: {{MSSQL Sample data}}
              jdbc:
                subprotocol: sqlserver
                host: {{host}}
                port: {{port}}
                database: {{database}}
                params: {{'{"key":"value","key2":"value2"}'}}
              external: {{true}}
              secrets:
                - name: {{nstance-secret-name}}-r
                  allkeys: true

                - name: {{instance-secret-name}}-rw
                  allkeys: true
            ```

    === "Oracle"

        DataOS allows you to connect to an Oracle database and access data from tables using Depots. A Depot provides access to all schemas within the specified service in the configured database. You can create multiple Depots to connect to different Oracle servers or databases. To create a Depot of type ‘ORACLE‘, you can use the following template:

        <aside class=callout>
        🗣️ Please note that the credentials are directly specified in the depot manifest using the `connectionSecret`, whereas credentials are referred via [Instance Secret](./instance_secret.md) as `secrets` or `dataosSecrets`.      
        </aside>

        === "Inline Credentials"

            ```yaml title="oracle_v1.yaml" 
            --8<-- "examples/resources/depot/relational_db/oracle/oracle_v1.yaml"
            ```  
            Follow these steps to create the depot:

            - **Step 1**: Create a manifest file. 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.
                  
        === "Instance Secret Reference"

            ```yaml title="oracle_v2alpha.yaml" 
            --8<-- "examples/resources/depot/relational_db/oracle/oracle_v2alpha.yaml"
            ```  
            Follow these steps to create the depot:

            - **Step 1**: Create Instance-secret to store the credentials, for more imformation about instance secret, refer to [Instance Secret](../resources/instance_secret.md). 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.
      


        **Requirements**

        To connect to an Oracle database, you need the following information:

        - URL of your Oracle account: The URL or hostname of the Oracle database.
        - User name: Your login user name.
        - Password: Your password for authentication.
        - Database name: The name of the Oracle database.
        - Database schema: The schema where your table belongs.



    === "PostgreSQL"

        DataOS allows you to connect to a PostgreSQL database and read data from tables using Depots. A Depot provides access to all schemas visible to the specified user in the configured database. To create a Depot of type ‘POSTGRESQL‘, use the following template:

        <aside class=callout>
        🗣️ Please note that the credentials are directly specified in the depot manifest using the `connectionSecret`, whereas credentials are referred via [Instance Secret](./instance_secret.md) as `secrets` or `dataosSecrets`.      
        </aside>

        **Use this templates, if self-signed certificate is enabled.**

        === "Inline Credentials"

            ```yaml title="ps_v1.yaml" 
            --8<-- "examples/resources/depot/relational_db/postgre/ps_v1.yaml"
            ```
            Follow these steps to create the depot:

            - **Step 1**: Create a manifest file. 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.
      
        === "Instance Secret Reference"

            ```yaml title="ps_v2alpha.yaml" 
            --8<-- "examples/resources/depot/relational_db/postgre/ps_v2alpha.yaml"
            ```  
            Follow these steps to create the depot:

            - **Step 1**: Create Instance-secret to store the credentials, for more imformation about instance secret, refer to [Instance Secret](../resources/instance_secret.md). 
            - **Step 2**: Copy the template from above and paste it in a code.
            - **Step 3**: Fill the values for the atttributes/fields declared in the YAML-based manifest file. 
            - **Step 4**: Apply the file through DataOS CLI.
      

        **Requirements**
        To create a Depot and connect to a PostgreSQL database, you need the following information:

        - Database name: The name of the PostgreSQL database.
        - Hostname/URL of the server: The hostname or URL of the PostgreSQL server.
        - Parameters: Additional parameters for the connection, if required.
        - Username: The username for authentication.
        - Password: The password for authentication.

        **If self-signed certificates are not being used** by your organization, for connection to these storage systems, then you do not need to write additional parameters within the spec section.

        === "Inline Credentials"

            ``` yaml
            name: {{depot-name}}
            version: v1
            type: depot
            tags:
              - {{tag1}}
            owner: {{owner-name}}
            layer: user
            depot:
              type: POSTGRESQL
              description: {{description}}
              external: true
              connectionSecret:                               
                - acl: rw
                  type: key-value-properties
                  data:
                    username: {{posgresql-username}}
                    password: {{posgresql-password}}
                - acl: r
                  type: key-value-properties
                  data:
                    username: {{posgresql-username}}
                    password: {{posgresql-password}}
              spec:                                          
                host: {{host}}
                port: {{port}}
                database: {{database-name}}
                params: # Optional
                  {{"key1": "value1"}}
                  {{"key2": "value2"}}
            ```

        === "Instance Secret Reference"

            ``` yaml
            name: {{depot-name}}
            version: v2alpha
            type: depot
            tags:
              - {{tag1}}
            owner: {{owner-name}}
            layer: user
            depot:
              type: POSTGRESQL
              description: {{description}}
              external: true
              secrets:
                - name: {{nstance-secret-name}}-r
                  allkeys: true

                - name: {{instance-secret-name}}-rw
                  allkeys: true
              postgresql:                                          
                host: {{host}}
                port: {{port}}
                database: {{database-name}}
                params: # Optional
                  {{"key1": "value1"}}
                  {{"key2": "value2"}}
            ```
