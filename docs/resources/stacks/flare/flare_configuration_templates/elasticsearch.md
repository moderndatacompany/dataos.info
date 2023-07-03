# Elasticsearch Depots

To start executing Flare Jobs on Elasticsearch Depots, you first need to set up an Elasticsearch Depot. If you haven’t done it, navigate to the below link

## Read Configuration


For reading the data from an Elasticsearch depot, we need to configure the following property `name`, `dataset`, `format`, and Elasticsearch-specific property `es.nodes.wan.only` within `options` in the `inputs` section of the YAML. For instance, if your dataset name is `input`, the UDL address is `dataos://elasticsearch:default/elastic_write`  and the `format` set to `elasticsearch`. Then the inputs section will be as follows-

```yaml
inputs:
   - name: input
     dataset:  dataos://elasticsearch:default/elastic_write
     format: elasticsearch
     options:
        es.nodes.wan.only: 'true'
```
By setting `es.nodes.wan.only`, the connector will limit its network usage and instead of connecting directly to the target resource shards, it will make connections to the Elasticsearch cluster only.

**Sample Read configuration YAML**

Let’s take a case scenario where we read the dataset from Elasticsearch depot and store it in the Icebase depot within the DataOS. The read config YAML will be as follows

```yaml
version: v1
name: read-elasticsearch-01
type: workflow
tags:
  - elasticsearch
  - read
description: this jobs reads data from elasticsearch and writes to icebase
workflow:
  dag:
    - name: elasticsearch-read-b-01
      title: read data from elasticsearch
      description: read data from elasticsearch
      spec:
        tags:
          - Connect
        stack: flare:3.0
        compute: runnable-default
        flare:
          job:
            explain: true
            inputs:
              - name: input
                dataset:  dataos://elasticsearch:default/elastic_write
                format: elasticsearch
                options:
                  es.nodes.wan.only: 'true'
            logLevel: INFO
            outputs:
              - name: output02
                dataset: dataos://icebase:sample/read_elasticsearch?acl=rw
                format: iceberg
                options:
                  saveMode: append
            steps:
              - sequence:
                  - name: output02
                    sql: SELECT * FROM input
```

## Write Configuration

For writing the data to an Elasticsearch depot, we need to configure the `name`, `dataset`, `format`, in the `outputs` section of the YAML. For instance, if your dataset name is `output01`, the dataset is to be stored at the location `dataos://elasticsearch:default/elastic_write` and the file format is `elasticsearch`. Then the inputs section will be as follows-

```yaml
outputs:
	- name: output01
	  dataset: dataos://elasticsearch:default/elastic_write?acl=rw
    format: elasticsearch
```

**Sample Read configuration YAML**

Let’s take a case scenario where we have to write the dataset to the an Elasticsearch depot from the thirdparty depot. The write config YAML will be as follows

```yaml
version: v1
name: write-elasticsearch-b-0001
type: workflow
tags:
  - elasticsearch
  - write
description: this jobs reads data from thirdparty and writes to elasticsearch
workflow:
  title: Connect City
  dag:
    - name: elasticsearch-write-b-01
      title: write data to elasticsearch
      description: write data to elasticsearch
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
              - name: output01
                dataset: dataos://elasticsearch:default/elastic_write?acl=rw
                format: elasticsearch
                options:
                  saveMode: append
            steps:
              - sequence:
                  - name: output01
                    sql: SELECT * FROM city_connect
```