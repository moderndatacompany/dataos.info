# Connectors Configuration

This article describes how you can connect to relational databases and various other data sources to query data.

Minerva query engine offers a large variety of connectors, for example, MySQL, PostgreSQL, Oracle, and Redshift. These properties in the DataOS setup file will mount the connector as the Catalog. This catalog contains schemas and references your data source via a connector.

# Define Connectors

For Minerva, you can define connectors for data sources in the following ways:

1. Depot: If you have already defined Depots to access data sources then you can include the address of these Depots in the DataOS setup YAML file to configure connectors. You can also include additional properties to optimize the Minerva performance.

2. Catalog: Here you can provide the name and properties such as connection URL, user name, and password to access the data source.

The following is an example of connector configuration using Depot definition and Catalog properties. All these definitions will be converted to catalogs which you can access on DataOS Workbench.

> Note: Replace the connection properties as appropriate for your setup.
> 

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
      depots:                        # Pre-defined Depots and their properties 
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
      
      catalogs:                     # Data source connectors and their properties              
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

# Access Catalogs from Workbench

Once the connector configuration setup is completed, you can access your data assets for a specific data source from DataOS Workbench. Workbench uses Minerva with full SQL support and provides you with an interface, allowing you to access your data sources as catalogs and discover schemas.

<img src="Connectors%20Configuration/minerva-workbench-catalog-table.png" 
        alt="minerva-workbench-catalog-table.png"
        style="display: block; margin: auto" />

To learn more, refer to
[Workbench](../../Getting%20Started%20-%20DataOS%20Documentation/Data%20Management%20Capabilities/GUI/GUI%20Applications/Workbench.md).