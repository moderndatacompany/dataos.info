# Fetching Data from Stock Data API using Bento

Here's a more detailed step-by-step guide to fetching data from the Stock data API using Bento:

1. Create an account and obtain an API key from the Polygon API documentation from [this link](https://polygon.io/docs/stocks/getting-started).
2. Ingest the data into DataOS from the stock market API using Pulsar.
3. Use Bento to fetch the data from the stock market API and write it to Pulsar.
4. Create a YAML file to specify the input, pipeline, and output sections of the Bento stack.
    
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
    # DataOS env link
      envs:
        METIS_REGISTRY_URL: http://metis-api.metis.svc.cluster.local:5000/api/v2
    # Assigning the resources
      resources:
        requests:
          cpu: 100m
          memory: 128Mi
        limits:
          cpu: 1000m
          memory: 1024Mi
      stack: bento
      logLevel: DEBUG
      stackSpec:
    # Use HTTP server to get the data in the 0.0.0.0:8098/stockdataapple
        input:
          label: ""
          http_server:
            address: 0.0.0.0:8098
            path: /stockdatapple
            allowed_verbs:
              - POST
              - GET
            timeout: 60s
    # Use rate limit for pagination purposes
            rate_limit: ""
            sync_response:
              status: ${! meta("http_status_code") }
    # Pipeline section here we call the API
        pipeline:
          processors:
            - log:
                level: DEBUG
                message: "Meta: ${! meta() } Payload: ${! json() }"
            - http:
                url: https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2022-03-01/2022-04-02?apiKey=vPN3I7pGcKag2ampTWSVZCwBDD55cVF5
                verb: GET
                headers:
                  Content-Type: application/json
                  rate_limit: ""
                  timeout: 30s
                  parallel: true
    # Assign a condition here if the HTTP status code is less than 300 and greater than 300, we will get an error notification
            - switch:
                - check: meta("http_status_code").number() <= 300
                  processors:
                    - log:
                        level: DEBUG
                        message: 'Stock Response: ${! json() } Status: ${! meta("http_status_code")}'
                - check: meta("http_status_code").number() > 300
                  processors:
                    - log:
                        level
    ```
    
5. Reading data from pulsar and writing to icebase
    
    ```yaml
    version: v1
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
            stack: flare:5.0
    
    # a dataos APIkey is required of operator tag.
            envs: 
              DATAOS_RUN_AS_APIKEY: dG9rZW5fc29jaWFsbHlfdHlwaWNhbGx5X2dyYXRlZnVsX3NuYWlsLjAyYzhiZWU4LWJkNzctNDQ2Zi1hMzJlLTJhZGNjMjg5OGM3Ng==
            stackSpec:
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
    ```