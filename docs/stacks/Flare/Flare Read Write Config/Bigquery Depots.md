# **Bigquery Depots**

To execute Flare Jobs on top of the Bigquery data source, you first need to create a depot. If you have already created a depot, then continue reading else proceed to one of the below links based on storage type

To run a Flare Job all you need is the UDL address of the input or output dataset for the reading and writing scenarios respectively.

# **Read Config**

| Scenario | Syntax | Format Value |
| --- | --- | --- |
| Inputs (while reading from a depot) | `inputs:` <br> `- name: <name-of-input>` <br> `dataset: dataos://[depot]:[collection]/[dataset]` <br> `format: Bigquery` | `Bigquery` |

For reading the data, we need to configure the `name`, `dataset` and `format` properties in the `inputs` section of the YAML. For instance, if your dataset name is `city_connect`, UDL address is `dataos://yakdevbq:dev/city_bq`. Then the inputs section will be as follows-

```yaml
inputs:
	- name: city_connect # name of the dataset
    dataset: dataos://yakdevbq:dev/city_bq # address of the input dataset
    format: Bigquery # format
```

**Sample Read configuration YAML**

Let’s take a case scenario where the dataset is stored in Big Query Depot and you have to read data from the source, perform some transformation steps and write it to the Icebase which is a managed depot within the DataOS. The read config YAML will be as follows

```yaml
version: v1
name: bq-read-02
type: workflow
tags:
  - bq
  - City
description: This job read data from azure and writes to S3
title: Write bq
workflow:
  dag:
    - name: city-read-bq-02
      title: City read bq
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

# **Write Config**

| Scenario | Syntax | Format Value | Additional Properties |
| --- | --- | --- | --- |
| Outputs (while writing to a depot) | `outputs:` <br>&nbsp;&nbsp;&nbsp;&nbsp; `- name: <name-of-output>` <br>&nbsp;&nbsp;&nbsp;&nbsp; `dataset: dataos://[depot]:[collection]/[dataset]?acl=rw` <br>&nbsp;&nbsp;&nbsp;&nbsp; `format: Bigquery` | `Bigquery` | `options:` <br>&nbsp;&nbsp;&nbsp;&nbsp; `bigquery:` <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `temporaryBucket: <name>` |

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