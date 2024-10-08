# Connector Configuration

This documentation outlines the process of establishing connections to various data sources in order to query data using the Minerva query engine. Minerva offers a diverse range of connectors, including MySQL, PostgreSQL, Oracle, and Redshift. These connectors are configured as catalogs in the DataOS setup file and facilitate the referencing and retrieval of data from the respective data sources.

## Defining Connectors

To define connectors for data sources in Minerva, you have the following options:

### **Depot**

If you have already defined Depots to access data sources, you can specify the addresses of these Depots in the DataOS YAML file to configure connectors. Additionally, you can include additional properties to optimize Minerva's performance. To know more about depots, click [here.](/resources/depot/)

### **Catalog** 
This approach involves providing the name of the connector and its associated properties, such as the connection URL, username, and password for accessing the data source.

**Sample Conector Configuration**

Below is an example of connector configuration using Depot definitions and Catalog key-value properties. These definitions will be converted into catalogs that can be accessed through DataOS Workbench.

> **Note**: Please ensure that you replace the connection properties with the appropriate values for your setup.

```yaml
cluster:
  nodeSelector:
    "dataos.io/purpose": "query"
  toleration: query
  runAsApiKey: api-key
  minerva:
    replicas: 2
    resources:
    limits:
        cpu: 2000m
        memory: 4Gi
    requests:
        cpu: 2000m
        memory: 4Gi
    debug:
    logLevel: INFO
    trinoLogLevel: ERROR
    depots:                        
# Pre-defined Depots and their properties 
      - address: dataos://icebase:default         
        properties:
            iceberg.file-format: PARQUET
            iceberg.compression-codec: GZIP
            hive.config.resources: "/usr/trino/etc/catalog/core-site.xml"
            hive.parquet.use-column-names: "true"
      - address: dataos://filebase:default
        properties:
            hive.config.resources: "/usr/trino/etc/catalog/core-site.xml"
            hive.parquet.use-column-names: "true"
# Data source connectors and their properties
    catalogs:                     
    - name: redshift
      type: redshift
      properties:
          connection-url: "jdbc:redshift://URL:PORT/DB"
          connection-user: "USERNAME"
          connection-password: "PASSWORD"
    - name: oracle
      type: oracle
      properties:
          connection-url: "jdbc:oracle:thin:@URL:PORT/DB"
          connection-user: "USERNAME"
          connection-password: "PASSWORD"
    - name: cache
      type: memory
      properties:
          memory.max-data-per-node: "128MB"
    - name: wrangler
      type: wrangler
```

# Supported Connectors


## Accessing Catalogs from Workbench

Once you have completed the setup of the connector configurations, you can access your data assets for a specific data source directly from DataOS Workbench. Workbench utilizes Minerva, which supports full SQL, and provides you with an intuitive interface for accessing your data sources as catalogs and exploring schemas.

<center>
  <div style="text-align: center;">
    <img src="/resources/cluster/connectors_configuration/minerva_workbench_catalog_table.png" alt="accessing_catalogs_from_workbench" style="width:41rem; border:1px solid black;">
    <figcaption align="center"><i>accessing_catalogs_from_workbench</i></figcaption>
  </div>
</center>



To learn more, refer to the [Workbench](/interfaces/workbench/) documentation.