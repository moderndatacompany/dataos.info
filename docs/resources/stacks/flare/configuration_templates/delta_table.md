# Flare Jobs on Delta Table

To execute Flare Jobs on Delta tables using object storage depots, such as Amazon S3, Azure ABFSS, or Google Cloud Storage, a depot must first be created. The format parameter in the Depot configuration file must be set to `DELTA`, as demonstrated in the following example:

???tip "Sample Depot configuration manifest"

    ```yaml title="abfssdelta.yml"
    version: v1
    name: "abfssdelta"
    type: depot
    tags:
        - Iceberg
        - Sanity
    layer: user
    depot:
    type: ABFSS
    description: "ABFSS Iceberg depot for sanity"
    compute: runnable-default
    spec:
        "account": mockdataos
        "container": dropzone001
        "relativePath": /sanity
        "format": "DELTA"
        "endpointSuffix": dfs.core.windows.net

    ```



Flare supports reading from and writing to Delta tables. To enable this functionality, the value delta must be assigned to the format parameter in the inputs section for reading operations, and in the outputs section for writing operations, within the stackSpec. Examples are provided below:

## Read Configuration

Following is the config file to read data from Delta tables using Flare:

```yaml
version: v1
name: abfss-delta-read
type: workflow
tags:
  - Connect
  - City
description: The job ingests city data from dropzone into raw zone
workflow:
  title: Connect City csv
  dag:
    - name: abfss-delta-read-01
      title: City Dimension Ingester
      description: The job ingests city data from dropzone into raw zone
      spec:
        tags:
          - Connect
          - City
        stack: flare:7.0
        compute: runnable-default
        stackSpec:
          job:
            explain: true
            inputs:
              - name: city_connect
                dataset: dataos://abfssdelta:abcd/delta_abfss_wr_jun19_01?acl=rw
                format: delta
                options:
                  headers: true                
                # schemaPath: dataos://sanitys3:none/schemas/avsc/city.avsc

            logLevel: INFO
            outputs:
              - name: finalDf
                dataset: dataos://lakehouse:abcd/delta_abfss_re_jun19_01?acl=rw
                format: Iceberg
                options:
                  saveMode: overwrite
            steps:
              - sequence:
                  - name: finalDf
                    sql: SELECT * FROM city_connect limit 10

```


## Write Configuration

Following is the config file to write data to Delta tables using Flare:

```yaml

version: v1
name: abfss-delta-write
type: workflow
tags:
  - Connect
  - City
description: The job ingests city data from dropzone into raw zone

workflow:
  title: Connect City
  dag:
    - name: abfss-delta-write-01
      title: City Dimension Ingester
      description: The job ingests city data from dropzone into raw zone
      spec:
        tags:
          - Connect
          - City
        stack: flare:7.0
        compute: runnable-default
        stackSpec:
          job:
            explain: true
            inputs:
              - name: city_connect
                dataset: dataos://thirdparty01:none/city
                format: csv
                schemaPath: dataos://thirdparty01:none/schemas/avsc/city.avsc

            logLevel: INFO
            outputs:
              - name: finalDf
                dataset: dataos://abfssdelta:abcd/delta_abfss_wr_jun19_01?acl=rw
                format: delta
            steps:
              - sequence:
                  - name: finalDf
                    sql: SELECT * FROM city_connect limit 10

```