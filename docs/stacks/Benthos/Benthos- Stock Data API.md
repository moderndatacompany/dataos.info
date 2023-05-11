# Benthos- Stock Data API

This use case demonstrates the creation of the Benthos service to ingest data into DataOS from the stock market API, using Pulsar.

There are two stages to achieve this:

1. Stock Data API  - > Pulsar
    
    Read the data using stock market API and store it in Pulsar.
    
2. Pulsar - > Icebase 
    
    Read the data from Pulsar and write it in Icebase.
    

Polygon API is used to get the data. You need to follow each API's own documentation to get the API response. Below is the link for reference.

[https://polygon.io/docs/stocks/getting-started](https://polygon.io/docs/stocks/getting-started)

# Prerequisites

You need to generate the API key or access token which acts as a password. Once authorized by the ‘GET’ request, you will be able to fetch data. 

Below is the link to generate the API key.

[https://polygon.io/docs/stocks/getting-started](https://polygon.io/docs/stocks/getting-started)

Here are the steps to create the pipeline.

Step 1: Create a Benthos service in DataOS for storing stock market data and writing to Pulsar.

Step 2: Create a [Policy for Benthos service](../Benthos.md) for ingesting data into DataOS.

Step 3: Create a [Flare](../Flare.md) for reading data from Pulsar and writing into Icebase.

## Create a Benthos Service in DataOS

Create the YAML file for Benthos service to fetch the data from stock market API and write to Pulsar. To learn more about what sections you need to create, refer to [Benthos](../Benthos.md). 

```yaml
version: v1beta1
name: pulsar-data-stream
type: service
tags:
  - api
description: API gateway server
service:
  title: API Data
  replicas: 1
  servicePort: 8098
  autoScaling:
    enabled: true
    minReplicas: 2
    maxReplicas: 4
    targetMemoryUtilizationPercentage: 80
    targetCPUUtilizationPercentage: 80
  ingress:
    enabled: true
    path: /stockdatapple
    noAuthentication: false
    annotations:
      konghq.com/strip-path: "false"
      kubernetes.io/ingress.class: kong
  tags:
    - wbi
    - trigger
# dataOS env link
  envs:
    METIS_REGISTRY_URL: http://metis-api.metis.svc.cluster.local:5000/api/v2
#assigning the resources  
resources:
    requests:
      cpu: 100m
      memory: 128Mi
    limits:
      cpu: 1000m
      memory: 1024Mi
# benthos stack starts
  stack: benthos
  logLevel: DEBUG
  benthos:
#used HTTP server to get the data in the 0.0.0.0:8098/stockdataapple 
    input:
      label: ""
      http_server:
        address: 0.0.0.0:8098
        path: /stockdatapple
        allowed_verbs:
          - POST
          - GET
        timeout: 60s
#rate limit is used for pagination purpose
        rate_limit: ""
        sync_response:
          status: ${! meta("http_status_code") }
#pipeline section here we call the API
    pipeline:
      processors:
        - log:
            level: DEBUG
            message: "Meta: ${! meta() } Payload: ${! json() }"
        - http:
            url: https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2022-03-01/2022-04-02?apiKey=v4ampHWSVZCwBDD55cVF5
            verb: GET
            headers:
              Content-Type: application/json
              rate_limit: ""
              timeout: 30s
              parallel: true
# we assign a condition here if the HTTP status code is less than 300 and greater than 300 we will get error notification
        - switch:
            - check: meta("http_status_code").number() <= 300
              processors:
                - log:
                    level: DEBUG
                    message: 'Stock Response: ${! json() } Status: ${! meta("http_status_code")}'
            - check: meta("http_status_code").number() > 300
              processors:
                - log:
                    level: ERROR
                    message: 'Stock Error Response: ${! json() } Status: ${! meta()}'
                - bloblang: |
                    root = error()
      threads: 1
#sending the data to pulsar
    output:
      broker:
        pattern: fan_out
        outputs:
          - broker:
              pattern: fan_out
              outputs:
                - type: dataos_depot
                  plugin:
                    metadata:
                      title: "Apple Stock exchange data"
                      description: "Apple Stock exchange data in a stream"
                      format: AVRO
                      type: STREAM
                      schemaLocation: "http://registry.url/schemas/ids/1"                  
                      tls:
                        enabled: true
                        tls_allow_insecure_connection: true
                        tls_validate_hostname: false
                      auth:
                        token:
                          enabled: true
                          token: <generated token>
                      schema: "{\"type\":\"record\",\"name\":\"defaultName\",\"namespace\":\"defaultNamespace\",\"fields\":[{\"name\":\"ticker\",\"type\":\"string\"},{\"name\":\"queryCount\",\"type\":\"int\"},{\"name\":\"resultsCount\",\"type\":\"int\"},{\"name\":\"adjusted\",\"type\":\"boolean\"},{\"name\":\"results\",\"type\":{\"type\":\"array\",\"items\":{\"name\":\"results_record\",\"type\":\"record\",\"fields\":[{\"name\":\"v\",\"type\":\"double\"},{\"name\":\"vw\",\"type\":\"float\"},{\"name\":\"o\",\"type\":\"float\"},{\"name\":\"c\",\"type\":\"float\"},{\"name\":\"h\",\"type\":\"float\"},{\"name\":\"l\",\"type\":\"float\"},{\"name\":\"t\",\"type\":\"long\"},{\"name\":\"n\",\"type\":\"int\"}]}}},{\"name\":\"status\",\"type\":\"string\"},{\"name\":\"request_id\",\"type\":\"string\"},{\"name\":\"count\",\"type\":\"int\"}]}"
                    address: dataos://publicstreams:default/stockdatapple
                - type: sync_response
            processors:
              - bloblang: root = if errored() { deleted() }
```

## Create a Policy for Benthos Service

Create the following YAML file to apply the policy for ingesting the data into DataOS. To learn more, refer to [Define Policy for Benthos Service](../Benthos.md).

```yaml
name: "stockdata-gateway-paths"
version: v1beta1
type: policy
layer: system
description: "stockdata gateway policy allowing users to access stock gateway paths"
policy:
  access:
    subjects:
      tags:
        - - "dataos:u:user"
    predicates:
      - "POST"
      - "GET"
    objects:
      paths:
        - "/stockdatapple"
    allow: true
```

## Create a Flare Workflow

Create the following YAML file to read data from Pulsar and write to Icebase. To learn more about how to write Flare workflow, refer to

[Flare](../Flare.md).

```yaml
---
version: v1beta1
name: pulsar-applestock-data
type: workflow
tags:
  - pulsar
  - read
  - applestock
description: this jobs reads data from pulsar and writes to icebase

#ingestion YAML starts
workflow:
  dag:
    - name: pulsar-appledata
      title: read avro data from pulsar
      description: read avro data from pulsar
      spec:
        tags:
          - Connect
        stack: flare:1.0

# a dataos APIkey is required of operator tag.
        envs: 
          DATAOS_RUN_AS_APIKEY: <API KEY>
        flare:
          job:
            explain: true
#enter the name of depo "/stockdatapple" is the pulsar topic name
#publicstreams is the depo of pulsar which is created in DataOS
            inputs:
              - name: input
                dataset: dataos://publicstreams:default/stockdatapple
                options:
                    startingOffsets: earliest
                isStream: false
            logLevel: INFO
            outputs:
              - name: stockdata
                depot: dataos://icebase:sample?acl=rw
            steps:
              - sink:
                  - sequenceName: input
                    datasetName: stock_pulsar
                    outputName: stockdata
                    outputType: Iceberg
                    description: stockdata data ingested from pulsar
                    outputOptions:
                      saveMode: overwrite
                      iceberg:
                        properties:
                          write.format.default: parquet
                          write.metadata.compression-codec: gzip
                    tags:
                      - Connect
                    title: Apple Stock Data 

# here we run the data tool to bring data into icebase, since its a file system , inorder to ingest it we run the data tool
    - name: dataos-tool-pulsar
      spec:
        stack: toolbox
        toolbox:
          dataset: dataos://icebase:sample/stock_pulsar?acl=rw
          action:
            name: set_version
            value: latest
      dependencies:
        - pulsar-appledata
```