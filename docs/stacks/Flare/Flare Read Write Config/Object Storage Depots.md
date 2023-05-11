# Object Storage Depots

To execute Flare Jobs on top of object storage depots, you first need to create a depot. If you have already created a depot, then continue reading else proceed to one of the below links based on storage type

Add Link for Google Cloud Storage

By creating depots on top of Object Stores interaction can be done in a uniform way with all supported storages i.e. Azure Blob File System, Google Cloud Storage, and Amazon S3. To run a Flare Job all you need is the UDL address of the input or output dataset for the reading and writing scenarios respectively. Apart from this you also need the file `format` of the data.

## Read Config

| Scenario | Syntax | Supported File Formats |
| --- | --- | --- |
| Inputs (while readingfrom a depot) | `inputs:` <br>&nbsp;&nbsp;&nbsp;&nbsp; `- name: <name-of-input>` <br>&nbsp;&nbsp;&nbsp;&nbsp; `dataset: dataos://[depot]:[collection]/[dataset]` <br>&nbsp;&nbsp;&nbsp;&nbsp; `format: <file-format>` | `avro`, `csv`, `json`, `orc`, `parquet`, `txt`, `xlsx`, `xml` |

For reading the data, we need to configure the `name`, `dataset`, and `format` properties in the `inputs` section of the YAML. For instance, if your dataset name is `city_connect`, UDL address dataset stored in Azure Blob Storage is `dataos://thirdparty01:sampledata/avro` and the file format is `avro`. Then the `inputs` section will be as follows-

```yaml
inputs:
	- name: city_connect # name of the dataset
    dataset: dataos://thirdparty01:sampledata/avro # address of the input dataset
    format: avro # file format
```

Sample Read configuration YAML

Let’s take a case scenario where the dataset is stored in Azure Blob File System (ABFSS) and you have to read data from the source, perform some transformation steps and write it to the Icebase which is a managed depot within the DataOS. The read config YAML will be as follows

```yaml
version: v1
name: abfss-read-avro
type: workflow
tags:
  - Connect
  - City
description: The job ingests city data from dropzone into raw zone
workflow:
  title: Connect City avro
  dag:
    - name: city-abfss-read-avro
      title: City Dimension Ingester
      description: The job ingests city data from dropzone into raw zone
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
              - name: city_connect # dataset name
                dataset: dataos://thirdparty01:sampledata/avro # dataset UDL
                format: avro # file format

            logLevel: INFO
            outputs:
              - name: output01
                dataset: dataos://icebase:retail/abfss_read_avro01?acl=rw
                format: iceberg
                options:
                  saveMode: append
            steps:
              - sequence:
                - name: output01
                  sql: SELECT * FROM city_connect
```

## Write Config

| Scenario | Syntax | Supported File Formats |
| --- | --- | --- |
| Outputs (while writingto a depot) | `outputs:` <br>&nbsp;&nbsp;&nbsp;&nbsp; `- name: <name-of-output>` <br>&nbsp;&nbsp;&nbsp;&nbsp; `dataset: dataos://[depot]:[collection]/[dataset]?acl=rw` <br>&nbsp;&nbsp;&nbsp;&nbsp; `format: <file-format>` | `avro`,` csv`, `json`, `orc`, `parquet`, `txt`, `xlsx`, `xml` |

> Note: the `?acl=rw` after the UDL signifies Access Control List with Read Write Access. You can also specify the address of the output dataset in the format `dataos://[depot]:[collection]?acl=rw.` The name of the output dataset will automatically get appended to it.
> 

For writing the data to a depot on an object store, we need to configure the `name`,  `dataset` and `format` properties in the `outputs` section of the YAML. For instance, if your dataset is to be stored at the UDL address  `dataos://thirdparty01:sampledata`  by the name `output01` and the file format is `avro`. Then the `outputs` section will be as follows

```yaml
outputs:
  - name: output01 # output name
    dataset: dataos://thirdparty01:sampledata?acl=rw # address where the output is to be stored
    format: avro # file format
```

Sample Write configuration YAML

Let’s take a case scenario where the output dataset is to be stored in Azure Blob File System Depot (ABFSS) and you have to read data from the Icebase depot within the DataOS. The write config YAML will be as follows

```yaml
version: v1
name: abfss-write-avro
type: workflow
tags:
  - Connect
  - City
description: The job ingests city data from dropzone into raw zone
workflow:
  title: Connect City avro
  dag:
    - name: city-abfss-write-avro
      title: City Dimension Ingester
      description: The job ingests city data from dropzone into raw zone
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
                dataset: dataos://icebase:retail/city
                format: iceberg

            logLevel: INFO
            outputs:
              - name: output01 #output dataset name
                dataset: dataos://thirdparty01:sampledata?acl=rw #output dataset address
                format: avro # file format
            steps:
              - sequence:
                  - name: output01
                    sql: SELECT * FROM city_connect
```