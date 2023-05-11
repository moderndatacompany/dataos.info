# Creating Minerva Clusters

# Steps for creating a Minerva cluster

### Create a YAML file with the following configuration properties.

```yaml
version: v1
name: <Joe can be an example>
type: cluster
description: the default minerva cluster c
tags:
  - cluster
  - minerva
cluster:
  compute: query-default01    #This name is from the compute file 
  runAsApiKey: <API KEY>
    replicas: 2
    spillOverVolume: 25Gi
    resources:
      limits:
        cpu: 4000m
        memory: 8Gi
      requests:
        cpu: 2000m
        memory: 4Gi
    debug:
      logLevel: INFO
      trinoLogLevel: ERROR
    depots:                  # Pre-defined Depots and their properties
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
      - address: dataos://blender:default
    catalogs:               # Data source connectors and their properties
      - name: cache
        type: memory
        properties:
          memory.max-data-per-node: "128MB"
```

### Use the `apply` command to run the above YAML to create the compute resource in the DataOS environment.

```yaml
dataos-ctl apply -f <path/file-name>
```