# Benthos-Pulsar-DataOS

This use case demonstrates the creation of the Benthos service to ingest streaming data from an API and populate Pulsar via topic and finally ingest the streamed data into icebase depot i.e DataOS.

There are two stages to achieve this:

1. Data from API  - > Pulsar
    
    Read the data using API, apply transformations using bloblang and store it in Pulsar.
    
2. Pulsar - > Icebase 
    
    Read the data from Pulsar and write it in Icebase.
    

## Prerequisites

JsonPlaceholder API is used as the source of streaming which sends JSON data. 

You need to follow each API's own documentation to get the API response. Below is the link for reference.

[https://jsonplaceholder.typicode.com/](https://jsonplaceholder.typicode.com/) 


>💡 Most APIs require access via API keys (similar to passwords) or have complex authentication and authorization methods. Some APIs like JsonPlaceholder API provides sample data for testing purposes, so you do not need to generate API keys.


Here are the steps to create the pipeline.

Step 1: Create a Benthos service in DataOS for storing data fetched from API and writing to Pulsar.

Step 2: Create a [Policy for Benthos Service](./Benthos.md) for ingesting data into DataOS.

Step 3: Create a [Flare Workflow](../Flare/Flare.md) for reading data from Pulsar and writing into Icebase.

## Create a Benthos Service in DataOS

Create the YAML file for the Benthos service to fetch the data from JsonPlaceholder API and write to Pulsar Depot. To learn more about what sections you need to create, refer to [Benthos Service](./Benthos.md) in DataOS. 

> Note : `address: dataos://publicstreams:default/testjph` where `testjph` is the Pulsar topic created on the fly, where all the streaming data will be pushed as Pulsar works on a pub-sub mechanism where the topic is required to run the service.
> 

```yaml
version: v1beta1 
name: testjph 
type: service 
tags: 
  - api
  - test 
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
    path: /testjph 
    noAuthentication: false 
    annotations: 
      konghq.com/strip-path: "false" 
      kubernetes.io/ingress.class: kong 
  tags: 
    - test 
    - trigger 
# dataOS link
  envs: 
    METIS_REGISTRY_URL: <http://metis-api.metis.svc.cluster.local:5000/api/v2> 
#Resources Allocation   
  resources: 
    requests: 
      cpu: 100m 
      memory: 128Mi 
    limits: 
      cpu: 1000m 
      memory: 1024Mi 
  stack: benthos            # benthos config starts from this point
  logLevel: INFO 
  benthos: 
    input:
      http_client:
        url: "https://jsonplaceholder.typicode.com/posts"
        verb: GET
        timeout: 5s
        retry_period: 1s
        ma.x_retry_backoff: 300s
        retries: 3
        proxy_url: ""
        payload: ""
        drop_empty_bodies: true
        stream:
          enabled: false
          reconnect: true
          codec: lines
          max_buffer: 10000
    pipeline:
      processors:
        - bloblang: root = content().uppercase()
    output: 
      broker: 
        outputs: 
          - broker:
              outputs: 
              - type: dataos_depot 
                plugin:
                  # pulsar depot url
                  address: dataos://publicstreams:default/testjph 
                  metadata: 
                    title: "Test JPH" 
                    description: "JSON Placeholder API Testd" 
                    type: STREAM
                    format: json
                    # Json Schema generated and registry url to register schema
                    schema: "{\"type\":\"record\",\"name\":\"defaultName\",\"namespace\":\"defaultNamespace\",\"fields\": [{\"name\": \"USERID\",\"type\": \"int\"},{\"name\": \"ID\",\"type\": \"int\"},{\"name\": \"TITLE\",\"type\": \"string\"},{\"name\": \"BODY\",\"type\": \"string\"}]}"
                    schemaLocation: "http://registry.url/schemas/ids/1"   
                    tags: 
                    - testjph  
                    title: Test json placholder api
                    tls: 
                      enabled: true 
                      tls_allow_insecure_connection: true 
                      tls_validate_hostname: false 
                    auth: 
                      token: 
                        enabled: true 
                        token: "< operator token required  >"
```

## Create a Policy for Benthos Service

Create the following YAML file to apply the policy for ingesting the data into DataOS. To learn more, refer to [Define Policy for Benthos Service](./Benthos.md).

```yaml

name: "testjph"
version: v1beta1
type: policy
layer: system
description: "policy allowing users to access testjph"
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
        - "/testjph"
    allow: true
```

## Create a Flare Workflow

Create the Flare workflow YAML file to read data from Pulsar and write to Icebase. To learn more about how to write Flare workflow, refer to [Flare Stack](../Flare/Flare.md).         

```yaml
---
version: v1beta1
name: pulsar-icebase
type: workflow
tags:
  - json-api
  - json-placeholder
description: This jobs ingest Data from pulsar to icebase
workflow:
  dag:
    - name: jph
      title: Data from json placeholder api for testing
      description: This json data for testing
      spec:
        tags:
          - test    
        stack: flare:1.0  
        tier: connect
        flare:
          driver:
            coreLimit: 2000m
            cores: 1
            memory: 2000m
          executor:
            coreLimit: 2000m
            cores: 1
            instances: 1
            memory: 2000m
          job:
            explain: true
            inputs:
             - name: jph
               dataset: dataos://publicstreams:default/testjph
               options:
                   startingOffsets: earliest
               isStream: false               
            logLevel: INFO
            outputs:
              - name: output01 # http client data
                depot: dataos://icebase:sample?acl=rw
            steps:
              - sink: 
                  - sequenceName: jph
                    datasetName: testjph
                    outputName: output01
                    outputType: Iceberg
                    outputOptions:
                      saveMode: Overwrite
                      
          
# data tool
    - name: dt-jph
      spec:
        stack: toolbox
        toolbox:
          dataset: dataos://icebase:sample/testjph?acl=rw
          action:
            name: set_version
            value: latest
      dependencies:
        - jph
```

##