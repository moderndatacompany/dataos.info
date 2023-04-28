# DataOS Flare

## Introduction

Flare is a declarative stack for Apache Spark workflows/ jobs.  Flare makes creating and triggering a job much easier and enables the engineer to create fairly complex workflows to carry out the data processing tasks. The workflows can have one or more jobs, and are defined in the form of a sequential yaml.
 

## Essential concepts and terminology 


YAML, essentially a data serialization language, works here as a file holding key-value pairs needed to run the workflow. 

The yaml for a Flare workflow involves many inputs which you have to provide in key-value pair.

Sample YAML:

```yaml
version: v1beta1
name: connect-ny-taxi
type: workflow
tags:
- Connect
- NY-Taxi
description: The job ingests NY-Taxi data small files and write with partitioning on vendor_id
workflow:
  title: Connect NY Taxi
  dag:
    - name: customer
      title: Customer Dimension Ingester Data Iceberg
      description: The job ingests customer data from dropzone into raw zone using hive catalog
      spec:
        tags:
          - Connect
          - Customer
        stack: flare:1.0
        tier: connect
        flare:
          driver:
            coreLimit: 1200m
            cores: 1
            memory: 1024m
          executor:
            coreLimit: 1200m
            cores: 1
            instances: 1
            memory: 1024m
          job:
            explain: true
            inputs:
              - name: transactions_connect
                dataset: /datadir/transactions?acl=r
                format: json

              - name: querydata
                dataset: /datadir/querydata?acl=r
                format: json
            #                format: csv
            #                schemaPath: dataos://thirdparty01:default/schemas/avsc/customer.avsc

            logLevel: ERROR
            outputs:
              - name: output01
                depot: dataos://raw01:default?acl=rw
            steps:
              - sink:
                  - sequenceName: customers
                    datasetName: customer_iceberg_02
                    outputName: output01
                    outputType: Iceberg
                    description: Customer data ingested from external csv to Iceberg using hive catalog
                    outputOptions:
                      saveMode: overwrite
```

|**Property**| **Value** | 
| ------ | -------- |  
version| Holds the current version of Flare|
name|Name of the job/ workflow|
type|The type could be a workflow, job, Depot etc
tags|Any attributes qualifying the workflow/ job
description| Text describing the workflow/ job
owner| The ID of the author of the job
workflow| An array of essential key-value pairs
dag| Directed acyclic graph, since the workflow is acyclic
stack| Flare stack to run the workflow
tier| Job type; Connect/ Rio/ Syndicate
driver| The controller node of the operation
executor| The worker node of the operation
inputs| This section can be multiple in number, an array of 3 or more key-value pairs, multiple datasets can be passed in the same format. Following are the key-value pairs <ul><li>name: Name of the dataset, this name will be used for reference later, this is mandatory</li> <li>format: File format of the dataset, parquet is considered by default</li><li>dataset: Address of the dataset</li></ul>
|outputs| An array of 2 key-value pairs. Following are the key-value pairs<ul><li>name: Name to be provided to the new dataset; the name can be used for reference later</li><li>depot: A Depot is a container which can have multiple datasets. Here, the address of the target Depot(where the dataset will belong) is passed.</li></ul>
|steps| The steps of the operation; these steps can be referenced via a separate yaml as well. This involves multiple key-value pairs<ul><li>sequence: Order or operations, further has two key-value pairs:<ul><li>name: Sequence name, to be used as reference for the output of the SQL query it has, in the form of a table or a view</li><li>sql: SQL query of the operation in Spark SQL format</li></ul></ul>
|sink| Details of the output dataset, following are the key-value pairs for the sink<ul><li>sequenceName: The name of the sequence relevant for the sink</li><li>datasetName: Name assigned to the new dataset</li><li>outputName: Name defined in the outputs section above</li><li>outputType: New dataset's file format</li><li>outputOptions: Different options depending on different outputTypes</li><li>partitionBy: Column used for partitioning the data. A good practice dictates partitioning at the Timestamp column</li></ul>| 


