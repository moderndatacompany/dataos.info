# How to create multiple Cluster using a single manifest file?

In scenarios where a single cluster is insufficient to handle the query load or specific performance issues arise, multiple Minerva clusters can be created. The following example demonstrates a typical configuration for a multi-cluster setup:

**Manifest file**

```yaml
- version: v1                           # Cluster 1
  name: minervab
  type: cluster
  description: the default minerva cluster b
  tags:
    - cluster
    - minerva
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
        - address: dataos://kafka:default
          properties:
            kafka.empty-field-strategy: "ADD_DUMMY"
            kafka.table-description-supplier: "confluent"
            kafka.default-schema: "default"
            kafka.confluent-subjects-cache-refresh-interval: "5s"
            kafka.confluent-schema-registry-url: "http://schema-registry.caretaker.svc.cluster.local:8081"
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

- version: v1
  name: minervabc                          # Cluster 2
  type: cluster
  description: the default minerva cluster c
  tags:
    - cluster
    - minerva
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
```


