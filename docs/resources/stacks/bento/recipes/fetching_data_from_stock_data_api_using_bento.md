# Fetching Data from Stock Data API using Bento

## Step-by-Step Guide to Fetching Stock Market Data Using Bento  

This guide outlines the process of fetching stock market data from the Polygon API and integrating it into DataOS using Bento and Pulsar.  

### **1. Create an Account and Obtain an API Key**  
To access stock market data, an API key is required. Follow these steps to obtain one:  

- Visit the [Polygon API documentation](https://polygon.io/docs/stocks/getting-started).  
- Sign up for an account or log in if an account already exists.  
- Navigate to the API key section and generate a new key.  
- Store the API key securely, as it is required for authentication in subsequent steps.  

### **2. Ingest Data into DataOS Using Pulsar**  
Apache Pulsar serves as the messaging system for streaming data into DataOS. To ingest stock market data:  

- Set up a Pulsar topic dedicated to stock market data ingestion.  
- Configure DataOS to subscribe to this topic for real-time data processing.  
- Ensure the necessary access credentials and permissions are granted for seamless data ingestion.  

### **3. Fetch Data Using Bento and Write to Pulsar**  
Bento facilitates the retrieval of stock market data and its integration with Pulsar. The process involves:  

- Writing a Bento script that interacts with the Polygon API.  
- Using the obtained API key to authenticate requests.  
- Defining the data schema and transformation logic, if needed.  
- Publishing the fetched data to the designated Pulsar topic for further processing in DataOS.  

### **4. Define a YAML Configuration File for Bento**  
A YAML configuration file is required to define the Bento stack, specifying input sources, processing logic, and output destinations. The key sections include:  

- **Input Section**: Configures the API request, specifying parameters such as stock symbols, time intervals, and authentication details.  
- **Pipeline Section**: Defines any necessary data transformations, filtering, or enrichment processes before storage.  
- **Output Section**: Specifies the Pulsar topic where the processed stock market data will be published.  
    
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
