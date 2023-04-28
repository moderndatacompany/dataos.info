# Benthos

Benthos stack in DataOS is used to create a service that enables you to process data from one or more streaming sources of data.

# About Benthos

Benthos is a declarative data streaming service that solves various Data Engineering issues with simple chained stateless processing steps. It can do single message transformation, mapping, schema validation, filtering, hydrating, and enrichment by interacting with other services like caching and then can write to one or more sinks.

Benthos works on message processing. It comes with a wide range of connectors, which allows for establishing connections with various sources and sinks. It implements a Transaction-based restoring force with back pressure. This means if your output target starts blocking traffic, Benthos will gracefully stop consuming stream data until the issue is resolved. 

It comes with Bloblang, a [powerful mapping language](https://www.benthos.dev/docs/guides/bloblang/about), easy to deploy and monitor, and ready to drop into your pipeline either as a static binary, docker image, or [serverless function](https://www.benthos.dev/docs/guides/serverless/about). Bloblang can dig deep into nested structures and bring the information needed.

# Core Features of Benthos

- **No runtime dependencies:** Its deployed static binaries have no runtime library dependencies.
- **Declarative configuration:** Don't have to compile or build the code.
- **Stateless and fast:** Benthos is totally stateless and can be horizontally scalable but at the same time, it can do stateful things by interacting with other services.
- **Payload agnostic:** Payload can be structured data JSON, Avro, or even binary data if needed. No limitation on the type of data.
- **Observability:** With the Prometheus matrix, logs and metrics can be traced.

# Define Configurations

In DataOS, your Benthos pipelines are configured in a YAML file that consists of a number of root sections.

A typical configuration file (filename.yaml) consists of the following:

**service**: For defining resources and configuration properties for service.

**ingress**: For using Benthos with DataOS, you need to configure the incoming port for the service to allow access to DataOS resources from external links.

i**nput**: Inputs consumed from storage or message streaming services such as aws_kinesis, aws_s3, Kafka, Pulsar, GCP, etc.

**output**: The output section is used to specify output location to write processed data.

**pipeline/processors**: A pipeline consists of processors that specialize in restructuring messages thereby performing various tasks of mapping, integration, and parsing.

## Service

While creating the Benthos service, you need to define certain fields like:

**replicas**: “copies” of service, one service runs parallelly in multiple replicas, so if one replica stops the other keeps running.

**autoScaling**: if set True, it automatically scales the infrastructure.

**targetCPUUtilizationPercentage**: This is the average CPU utilization of all the pods, so if you have given CPU as `200` in the resource `requests` and `targetCPUUtilizationPercentage` as `80%`, then at `160` value of the threshold, it will scale out the pod. It will create a new replica. Same goes for **`targetMemoryUtilizationPercentage`**

**METIS_REGISTRY_URL:** to register the service in DataOS Metis.

```yaml
version: v1beta1
name: bored-system
type: service
tags:
  - api
description: Get
service:
  title: API Data
  replicas: 1
  servicePort: 8098
  autoScaling:
    enabled: true
    minReplicas: 1
#     maxReplicas: 4
    targetMemoryUtilizationPercentage: 80
    targetCPUUtilizationPercentage: 80
  tags:
    - wbi
    - trigger
  envs:
    METIS_REGISTRY_URL: http://metis-api.metis.svc.cluster.local:5000/api/v2
  resources:
    requests:
      cpu: 100m
      memory: 128Mi
    limits:
      cpu: 1000m
      memory: 1024Mi
  stack: benthos
  logLevel: DEBUG
  benthos:
```

## Ingress (Using benthos with DataOS)

You need to configure the incoming port for the service to allow access to DataOS resources from external links. Ingress exposes HTTP and HTTPS routes from outside the cluster to services within the cluster. 

Provide the following properties.

- enable ingress port.
- enable the `stripPath` to strip the specified path and then forward the request to the upstream service.
- provide a public URL path to access the service externally, from outside DataOS (eg: `path: /swagger-ui)`
- set `noAuthentication` to false if authentication is needed.

 

```yaml
ingress:
    enabled: true
    noAuthentication: true
    path: <path>                  
    stripPath: true
```

## Input

It includes various sources for input, that is, from where the data has to be fetched.

1. The data may be stored in a cloud bucket.
    1. GCP
    2. AWS
    3. Azure 
2. Data may be fetched from an API, Social networking sites like Twitter, or Discord.
    1. HTTP
    2. Social
    3. Local
    4. File

The example given below is for **File** as the input source on which the data transformations have to be applied.

Here you need to pass a path i.e location of the file on which operation has to be performed. Codec is to specify that the large part of data has to be processed in small parts rather than stored in the memory.

```yaml
  # taking input of json file
benthos:
  input:
    label: "my_json"
    file:
      paths:
        - /path_to_json/experiment_2.json
      codec: lines
   
```

The example below has input as **http_client,** which connects to a server and continuously performs requests for a single message. 

**url**: The URL we want to connect to.

**verb**: ‘GET‘ to fetch data, we can also use ‘POST’ or ‘DELETE’ as per the requirement.

**timeout**: if there are no responses, the duration to close the session.

**stream**: it allows you to set streaming data.

```yaml
benthos:
    input:
      http_client:
        url: "https://www.boredapi.com/api/activity"
        verb: GET
        timeout: 10s
        stream:
          enabled: true
          reconnect: true
```

You can use more fields like headers, rate_limit , payload etc. 

To learn more about additional properties, refer [here](https://www.benthos.dev/docs/components/inputs/http_client.).

## Output

An output is a sink where we are sending our data, storage, or message streaming services such as aws_s3, GCP, SQL, etc. The data can also be sent after applying transformations.

You need to provide the following properties:

**broker**: it allows us to send the output into multiple output locations.

**pattern**: it explains the brokering pattern to be used as in this example, **fan_out** which allows Benthos to pass output to multiple locations parallelly.

**output address:** The example YAML below specifies the two output locations :

1. **dataos_depot** where you need certain credentials like token, address (path for output).
2. **stdout:** It helps us to see the output in the terminal.

**metadata:** it includes the output format, schema, and schema location. 

```yaml
		benthos:
      output:
        broker:
          pattern: fan_out
          outputs:
            - type: dataos_depot
              plugin:
                metadata:
                  title: "bored data"
                  format: AVRO
                  type: STREAM
                  schemaLocation: "http://registry.url/schemas/ids/1"
                  schema: "{\"type\":\"record\",\"name\":\"default\",\"namespace\":\"default\",\"fields\":[{\"name\":\"activity\", \"type\":\"string\"},{\"name\":\"type\", \"type\":\"string\"},{\"name\":\"participants\", \"type\":\"int\"},{\"name\":\"price\", \"type\":\"double\"},{\"name\":\"link\", \"type\":\"string\"},{\"name\":\"key\", \"type\":\"string\"},{\"name\":\"accessibility\", \"type\":\"double\"}]}"
                  tls:
                    enabled: true
                    tls_allow_insecure_connection: true
                    tls_validate_hostname: false
                  auth:
                    token:
                      enabled: true
                      token: "dG9rZW5fdmlzdWFsbHlfbGlnaHRseV9zcXVhcmVfb3dsLjAwZjBlZDAxLlNzhkZWUzZQ=="
                address: dataos://systemstreams:caretaker/boringdata_system
            - stdout:
                delimiter: "\n-----------message-----------\n"
```

These properties depend on the output type. 

To learn more, refer [here](https://www.benthos.dev/docs/components/outputs/about.).

## Pipeline / Processors in Benthos

This includes transformations to be performed on data and restructuring the messages. It has `bloblang` as the language which is used to perform transformations on the data or response that we receive from an API call.

```yaml
pipeline:
	processors:
		- bloblang: |
					root = this   # it shows that whatever data is coming from input without transformation its going in output
					root.length_string = this.activity.length()       # in this step we created a column called length_string which is storing the value of length of string in activity
					root.split_activit = this.activity.split(" ")     #  in this step we are creating a array of words in activity which are separated by spaceroot.split_activit = this.activity.split(" ")     #
```

To learn more, refer [here](https://www.benthos.dev/docs/components/processors/about.).

In the pipeline, transformations are applied to the messages which are coming through input sections, there are a lot of processors in Benthos but `bloblang` is the most popular. You can use `bloblang` to filter, transform and map the data.

There are more processors like aws_lambda where you can invoke those functions for the message, or group_by which splits the messages into the n number of batches that contains a group of messages determined by the query.

So, every message which contains accessibility = 0 is eventually grouped into a single batch.

```yaml
pipeline:
  processors:
    - group_by:
      - check: this.accessibility == 0
```

### **Error Handling**

Some processors have conditions where they can fail so it's better to throw these messages into the logs. Benthos still attempts to send these messages onwards and has mechanisms for filtering, recovering, or queuing messages that have failed.

```yaml
pipeline:

  processors:
    - bloblang: |
        root = this #this is a reference for a json object
        root.ad_id = deleted() #this is used to delete a key in json object
        root.age = this.age.replace("30-34","50") # to replace a value of json key
        root.interest1 = this.interest1.number() * 2 #typecasting and multiplying the string
        root.interest2 = this.interest2.number()
        root.merge_objects = this.merge(this.gender) #merging into json
        root.is_exists = this.exists("ad_id")
        #root.i = range(start: 0, stop: this.interest2.number(), step: 2)

        # to check the data type of number and performing multiplication and addition on json value
        # this will also throw error if the number is not in integer type
        #error handling
       root.interest2 = if (this.interest2.number()<10){
          this.interest2.number() + 10
        }else{
         this.interest2.number()*100
        }
        root.foos = if this.interest2.type() == "string"{
          this.interest2.number()
        }else{
          throw("this should be in interger form not string")
        }
```

# Define Policy for Benthos Service

Define policy for allowing users to access the DataOS resources using the Benthos service.

A policy in DataOS should be created for performing desired functionality using the Benthos service by authorized users.

```yaml
name: <name>
version: v1beta1
type: policy
layer: system
description: <policy description>
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
        - <path>                   **# path exposed by the service to acccess it**
    allow: true
```

# **Use Cases**

[Benthos- Twitter Data Processing](Benthos/Benthos-%20Twitter%20Data%20Processing.md)

[Benthos- Stock Data API](Benthos/Benthos-%20Stock%20Data%20API.md)

[Benthos-Pulsar-DataOS](Benthos/Benthos-Pulsar-DataOS.md)