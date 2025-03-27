# Bento on DataOS

When managing continuous data streams in DataOS — such as IoT data, real-time stock trades, server logs, and event data — the Service Resource provides a scalable solution for building robust pipelines.

The Bento Stack enhances this by simplifying stream data processing with efficient and reliable handling. By combining Bento with the Service Resource, users gain access to features such as built-in orchestration, cataloging, and governance capabilities. This integration enables the creation of scalable pipelines that manage complex data flows effectively.

Bento utilizes manifest declarative programming, allowing users to define pipeline logic clearly and concisely. This approach streamlines configuration, enabling users to focus on data processing and insights rather than implementation complexities.

## Prerequisites

### **Obtain the required tag**

To run Bento Services and write data to the DataOS environment, some specific tags are required. The available tags may vary based on the environment and organizational permissions. To check the available tags, execute the following command:

```bash
dataos-ctl user get
# Output
			NAME     |     ID      |  TYPE  |        EMAIL         |              TAGS               
---------------|-------------|--------|----------------------|---------------------------------
	IamGroot   |   iamgroot  | person |  iamgroot@tmdc.io    | users:id:iamgroot,                                         
               |             |        |                      | roles:id:data-dev,              
               |             |        |                      | roles:id:system-dev,        
               |             |        |                      | roles:id:user             

```
If the required role is not available, contact the DataOS operator or submit a grant request for the respective role.

## Running a Bento Service

This process acquires data from the Random User API, a publicly accessible source for generating user data. The retrieved data undergoes transformation using the Bento Stack with Bloblang before being written to the DataOS Kafka Depot.

**Complete example manifest configuration file for Bento**

```yaml

version: v1
name: ${{randomusertest}}
type: service
service:
  compute: ${{runnable-default}}
  replicas: ${{1}}
  servicePort: ${{8080}}          # dataos port
  ingress:
    enabled: ${{true}}
    path: ${{/test007}}           # url path
    noAuthentication: ${{true}}
  stack: ${{bento:3.0}}               # dataos stack with version
  logLevel: ${{DEBUG}}
  tags:
    - ${{service}}
  stackSpec:
    input:
      http_client:
        url: ${{https://randomuser.me/api/}}
        verb: ${{GET}}
        headers:
          Content-Type: ${{application/JSON}}
    pipeline:
      processors:
        - label: my_blobl
          bloblang: |
            root.id = uuid_v4()
            root.title = this.results.0.name.title.or("")
            root.first_name = this.results.0.name.first.or("")
            root.last_name = this.results.0.name.last.or("")
            root.gender = this.results.0.gender.or("")
            root.email = this.results.0.email.or("")
            root.city = this.results.0.location.city.or("")
            root.state = this.results.0.location.state.or("")
            root.country = this.results.0.location.country.or("")
            root.postcode = this.results.0.location.postcode.or("").string()
            root.age = this.results.0.dob.age.or(0)
            root.phone = this.results.0.phone.or("")
            meta.request_time = now()
            meta.source = "randomuser.me API"
    output:
      label: ${"i_kafka"}
      dataos_kafka:
        address: ${"dataos://kafkabento:default/output02?acl=rw"}    # address of the Kafka Depot
        max_in_flight: 64
        sasl:
          mechanism: PLAIN  
```


### **Apply the YAML file**

Now save above manifest file, apply the YAML file to create a Service Resource within the DataOS environment using the following command:  

```bash
dataos-ctl resource apply -f ${{path-of-the-config-file}} -w ${{workspace}}
```

### **Check Run time**

```bash
dataos-ctl -t service -w ${{workspace}} -n ${{service-name}}  get runtime -r
# Sample
dataos-ctl -t service -w public -n randomusertest  get runtime -r
```
#### **Expected Output**

```bash 
INFO[0000] 🔍 service...                                 
INFO[0002] 🔍 service...complete                         

        NAME       | VERSION |  TYPE   | WORKSPACE | TITLE |   STACK   |    OWNER     
-------------------|---------|---------|-----------|-------|-----------|--------------
  randomusertest   | v1      | service | public    |       | bento:3.0 | randomuser  


  RUNTIME | READY REPLICAS COUNT | REPLICAS COUNT  
----------|----------------------|-----------------
  running | 1                    | 1               


           REASON          |    TYPE     |               MESSAGE                |        LAST UPDATE         
---------------------------|-------------|--------------------------------------|----------------------------
  MinimumReplicasAvailable | Available   | Deployment has minimum               | 2025-03-25T08:58:55+05:30  
                           |             | availability.                        |                            
  NewReplicaSetAvailable   | Progressing | ReplicaSet                           | 2025-03-25T08:47:20+05:30  
                           |             | "randomusertest-zvs7-d-546956d8ff" |                            
                           |             | has successfully progressed.         |                            


                 NODE NAME                 |   SERVICE NAME   |                 POD NAME                 | DATA PLANE |      TYPE      |         CONTAINERS         |  PHASE   
-------------------------------------------|------------------|------------------------------------------|------------|----------------|----------------------------|----------
  randomusertest-zvs7-d-546956d8ff-6f2hl | randomusertest  | randomusertest-zvs7-d-546956d8ff-6f2hl | hub        | pod-deployment | randomusertest-zvs7-main | running  
```
It can be seen that Bento Service is successfully deployed and in the running state. 



## **Deep dive in Bento Service**

### **Configure the Service Resource Section**

The Service Resource section defines a persistent process responsible for receiving or delivering API requests. This section is configured using YAML fields and parameters. Within this configuration, the Bento Stack is invoked to execute the required data transformations.

```yaml
version: v1
name: ${{randomusertest}}
type: service
service:
  compute: ${{runnable-default}}
  replicas: ${{1}}
  servicePort: ${{8080}}  # dataos port
  ingress:
    enabled: ${{true}}
    path: ${{/test007}}   # url path
    noAuthentication: ${{true}}
  stack: ${{bento:3.0}}   # dataos stack
  logLevel: ${{DEBUG}}
  tags:
    - ${{service}}
```

For detailed information on Service and its YAML configurations, refer to the [Service documentation](/resources/service/).

### **Configuring Bento Stack-specific Section**

The Bento Stack-specific section requires configuring multiple components within the manifest file. The following example demonstrates the structure of a manifest configuration:


```yaml
  stackSpec:
    input:
      ${{input-component}}
    pipeline:
      processors:
        ${{pipeline-component}}
    output:
      ${{output-component}}
```
The Bento Stack-specific section consists of multiple components, each explained in detail on the [components](/resources/stacks/bento/components/) page.

Let's break down each component:

#### **Input Component**

The `input` component specifies the configuration for the data source. The following example demonstrates the configuration for the `http_client` input:

```yaml
http_client:
  url: ${{https://randomuser.me/api/}}
  verb: ${{GET}}
  headers:
    Content-Type: ${{application/JSON}}
```

For more details on available configuration options, refer to the `http_client` [input](/resources/stacks/bento/components/inputs/http_client/) documentation.

#### **Pipeline Component**

The `pipeline` component is responsible for applying a series of processors to the data stream. Processors allow data manipulation, transformation, or enrichment as it moves through the pipeline. The following example demonstrates a pipeline configuration using the bloblang processor:

```yaml
    pipeline:
      processors:
        - label: my_blobl
          bloblang: |
            root.id = uuid_v4()
            root.title = this.results.0.name.title.or("")
            root.first_name = this.results.0.name.first.or("")
            root.last_name = this.results.0.name.last.or("")
            root.gender = this.results.0.gender.or("")
            root.email = this.results.0.email.or("")
            root.city = this.results.0.location.city.or("")
            root.state = this.results.0.location.state.or("")
            root.country = this.results.0.location.country.or("")
            root.postcode = this.results.0.location.postcode.or("").string()
            root.age = this.results.0.dob.age.or(0)
            root.phone = this.results.0.phone.or("")
            meta.request_time = now()
            meta.source = "randomuser.me API"
```
In this example, the `bloblang` processor is applied to the data stream. It extracts specific fields from the input data and assigns them to variables for further processing. Feel free to explore the available processors and their configurations in the Bento [Processors](/resources/stacks/bento/components/processors/) documentation.

#### **Output Component**

The `output` component specifies the destination for processed data after it passes through the pipeline. Various output options can be configured, including writing to files, sending messages to message queues, or interacting with external APIs. The following example demonstrates the configuration for a Kafka Depot:

```yaml
    output:
      label: ${"i_kafka"}
      dataos_kafka:
        address: ${"dataos://kafkabento:default/output02?acl=rw"}    # address of the Kafka Depot
        max_in_flight: 64
        sasl:
          mechanism: PLAIN  

```

Feel free to explore the available output options and their configurations in the [Bento outputs](/resources/stacks/bento/components/output/) documentation.


This configuration demonstrates how to set up a Bento pipeline on DataOS with code. The Service pipeline retrieves data from an API in real-time, processes the data using a Bloblang transformation, and stores the result in the Kafka store.