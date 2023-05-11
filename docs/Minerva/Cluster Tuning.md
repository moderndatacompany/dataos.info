# Cluster Tuning

This article describes how you can create the Minerva clusters with optimized resources and tune them as per the query workload. With a properly tuned Minerva cluster, you can significantly improve the query execution and reduce the response time.

## Tune Minerva Cluster

To create and tune the Minerva cluster, provide the configuration properties for the cluster. These properties are saved in a DataOS setup YAML file stored in the DataOS configuration directory.

## Cluster Properties

The default Minerva settings should work well for most workloads. You may adjust the following properties such as replicas, resources, etc. to ensure optimal performance:

```yaml
- version: v1beta1
  name: minervab                    # Name of the Minerva cluster
  type: cluster
  description: the default minerva cluster b
  tags:
    - cluster
    - minerva
  cluster:                          # Minerva cluster properties 
    nodeSelector:
      "dataos.io/purpose": "query"
    toleration: query
    runAsApiKey: api-key
    minerva:                        # Tune these values for optimal performance
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
```

## Multi-Cluster Setup

Various data processing requirements force data engineering teams to create multiple clusters. You can add more clusters when a single cluster can not handle the query load or If your cluster is facing a specific performance problem. The following YAML file is an example of a typical Minerva multi-cluster configuration. Replicate the complete code in the DataOS installation setup file(dataos.install.core.kernel.values.yaml) as shown. Give a unique name to each cluster.

```yaml
- version: v1beta1                           # cluster- 1
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

- version: v1beta1
        name: minervabc                          # cluster- 2
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