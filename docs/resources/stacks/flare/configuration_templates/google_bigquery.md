# Google Bigquery Depots

Flare stack enables execution of jobs on top of Google Bigquery data source. To do so, you first need to create a Bigquery depot. If you have already created a depot, you can proceed with the following instructions. Otherwise, please refer to the [Biguery Depot Configuration](../../../depot/depot_config_templates/google_bigquery.md).

## Read Configuration

For reading data using Flare stack, the `name`, `dataset`, and `format` properties in the `inputs` section of the YAML configuration need to be configured. Here's an example configuration for the `inputs` section:

```yaml
inputs:
  - name: city_connect # name of the dataset
    dataset: dataos://bqdepot:state/city # address of the input dataset
    format: bigquery # format
```

<details><summary>Sample Read configuration YAML</summary>

Consider a scenario where the dataset named `city` is stored in a BigQuery Depot at the address `dataos://bqdepot:state/city`, and you need to read this data from the source Bigquery depot, perform some transformation steps, and write it to Icebase, a managed depot within DataOS. The read config YAML will be as follows:

```yaml
name: bq-read-01
version: v1
type: workflow
tags:
  - bq
  - City
description: This job read data from azure and writes to S3
title: Write bq
workflow:
  dag:
    - name: city-read-bq-01
      title: City read bq
      description: This job read data from azure and writes to Sbq
      spec:
        tags:
          - Connect
          - City
        stack: flare:4.0
        compute: runnable-default
        flare:
          job:
            explain: true
            inputs:
              - name: city
                dataset: dataos://bqdepot:state/city
                format: bigquery
            logLevel: INFO
            outputs:
              - name: finalDf
                dataset: dataos://icebase:sanity/city?acl=rw
                format: iceberg
                options:
                  saveMode: overwrite
            steps:
              - sequence:
                  - name: finalDf
                    sql: SELECT * FROM city_connect
```
</details>

## Write Configuration

For writing the data to a depot on a Bigquery depot, we need to configure the `name`,  `dataset` and `format` properties in the `outputs` section of the YAML. For instance, if your dataset is to be stored at the UDL address is `dataos://yakdevbq:dev/city_bq?acl=rw`  by the name `finaldf` and the file format is `Bigquery`. Then the outputs section will be as follows

```yaml
outputs:
	- name: finalDf
    dataset: dataos://yakdevbq:dev/city_bq?acl=rw
    format: Bigquery
    options:
	    saveMode: append
      bigquery:
	      temporaryBucket: tmdc-development-new
```

**Sample Write configuration YAML**

Let’s take a case scenario where the output dataset is to be stored in Bigquery Depot and you have to read data from the Icebase depot within the DataOS The write config YAML will be as follows

```yaml
version: v1
name: bq-read-write-02
type: workflow
tags:
  - bq
  - City
title: Write bq
workflow:
  dag:
    - name: city-write-bq-02
      title: City write bq
      description: This job read data from azure and writes to Sbq
      spec:
        tags:
          - Connect
          - City
        stack: flare:3.0
        compute: runnable-default
        flare:
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
                dataset: dataos://yakdevbq:dev/city_bq?acl=rw
                format: Bigquery
                options:
                  saveMode: append
                  bigquery:
                    temporaryBucket: tmdc-development-new
            steps:
              - sequence:
                  - name: finalDf
                    sql: SELECT * FROM city_connect
```



## Read Config

For reading data, the `name`, `dataset`, and `format` properties in the `inputs` section of the YAML configuration need to be configured. Here's an example configuration for the inputs section:

```yaml
inputs:
  - name: city_connect
    dataset: dataos://yakdevbq:dev/city_bq
    format: Bigquery
```

**Sample Read Configuration YAML:**

Consider a scenario where the dataset is stored in a BigQuery Depot, and you need to read data from the source, perform some transformation steps, and write it to Icebase, a managed depot within DataOS. The read config YAML will be as follows:

```yaml
version: v1
name: bq-read-02
type: workflow
tags:
  - bq
  - City
description: This job reads data from Azure and writes to S3
title: Write bq
workflow:
  dag:
    - name: city-read-bq-02
      title: City read bq
      description: This job reads data from Azure and writes to Sbq
      spec:
        tags:
          - Connect
          - City
        stack: flare:3.0
        compute: runnable-default
        flare:
          job:
            explain: true
            inputs:
              - name: city_connect
                dataset: dataos://yakdevbq:dev/city_bq
                format: Bigquery

            logLevel: INFO
            outputs:
              - name: finalDf
                dataset: dataos://icebase:retail/read_bq?acl=rw
                format: Iceberg
                options:
                  saveMode: append
            steps:
              - sequence:
                  - name: finalDf
                    sql: SELECT * FROM city_connect
```

## Write Config

To write data to a BigQuery depot, the `name`, `dataset`, and `format` properties in the `outputs` section of the YAML configuration need to be set. Here's an example configuration for the outputs section:

```yaml
outputs:
  - name: finalDf
    dataset: dataos://yakdevbq:dev/city_bq?acl=rw
    format: Bigquery
    options:
      saveMode: append
      bigquery:
        temporaryBucket: tmdc-development-new
```

**Sample Write Configuration YAML:**

Consider a scenario where the output dataset needs to be stored in a BigQuery Depot, and you need to read data from the Icebase depot within DataOS. The write config YAML will be as follows:

```yaml
version: v1
name: bq-read-write-02
type: workflow
tags:
  - bq
  - City
title: Write bq
workflow:
  dag:
    - name: city-write-bq-02
      title: City write bq
      description: This job reads data from Azure and writes to Sbq
      spec:
        tags:
          - Connect
          - City
        stack: flare:3.0
        compute: runnable-default
        flare:
          job:
            explain: true
            inputs