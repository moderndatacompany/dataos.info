# Bento on DataOS

When dealing with never-ending streams of data within DataOS - for e.g. IoT, real-time stock trades, server logs, and event data - the Service resource is the answer to your prayers. But let's face it, stream data can be a tough nut to crack, and that's where Bento comes in as your trusty sidekick. It's the perfect stack to help you process your stream data quickly and efficiently without breaking a sweat.

With Bento Service, you can enjoy the best of both worlds: the inherent benefits of the Service resource, which effortlessly enables you to create scalable and robust pipelines enriched with features such as built-in orchestration, cataloging, and governance capabilities, while the Bento stack takes care of all the heavy lifting when it comes to your stream data. 

And the best part? You can do it all with ease thanks to YAML declarative programming, which lets you focus on what really matters - processing your data and getting those precious insights - rather than worrying about the nitty-gritty details of how to fit the pieces of the puzzle together.

## Prerequisites

### **Get the DataOS API Key**

For writing data to Fastbase depots, you must obtain the user API key. Execute the following command to retrieve it:

```bash
dataos-ctl user apikey get
```

### **Obtain the Pulsar-admin tag**

In order to work with Pulsar format, you will require the pulsar-admin tag to write data to the DataOS Pulsar environment. To check your available tags, execute the following command:

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


## Let’s Begin!

As we commence our exciting new venture, we will be acquiring the data from the Random User API, a remarkably user-friendly and easily accessible API. To transform this API data, we will be leveraging the capabilities of the Bento stack by applying some Bloblang transformation, followed by writing the data to the DataOS Fastbase depot. So let's dive in and get the show on the road, shall we?

### **Create a Bento Service YAML**

#### **Configure the Service resource Section**

At the core of any Bento Service lies the Service resource section, which is responsible for defining a Service resource through a set of YAML fields and configurations. A Service is a persistent process that either receives or delivers API requests. The Bento stack is then invoked within the Service to effectuate the requisite transformations. 

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
    annotations:
      konghq.com/strip-path: "false"
      kubernetes.io/ingress.class: kong
  stack: ${{bento}}   # dataos stack
  logLevel: ${{DEBUG}}
  tags:
    - ${{service}}
```

For a deeper understanding of Service and its associated YAML configurations, please refer to the [Service](/resources/service/) page.

#### **Configuring Bento Stack-specific Section**

To configure the Bento Stack-specific section, you need to configure several components within the YAML configuration file. Here's an example of how you can structure the YAML configuration:

 A sample YAML Configuration is provided below:

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
The Bento Stack-specific Section comprises of several components each of which have been elaborated in detail on the [components](/resources/stacks/bento/components/) page.

Let's break down each component:

##### **Input Component**

The `input` component specifies the configuration for the data source. Here's an example configuration for the `http_client` input:

```yaml
http_client:
  url: ${{https://randomuser.me/api/}}
  verb: ${{GET}}
  headers:
    Content-Type: ${{application/JSON}}
```

You can refer to the `http_client` [input](/resources/stacks/bento/components/inputs/http_client/) documentation for more details on available configuration options.

##### **Pipeline Component**

The `pipeline` component is responsible for applying a series of processors to the data stream. Processors enable you to manipulate, transform, or enrich the data as it flows through the pipeline. Here's an example of a pipeline configuration using the bloblang processor:

```yaml
pipeline:
  processors:
    - label: my_blobl
      bloblang: |
        page = this.info.page
        age = this.results.0.dob.age
        dob = this.results.0.dob.date
        page = this.info.page
        seed = this.info.seed
        email = this.results.0.email
        gender = this.results.0.gender
        name = this.results.0.id.name
        city = this.results.0.location.city
```
In this example, the `bloblang` processor is applied to the data stream. It extracts specific fields from the input data and assigns them to variables for further processing. Feel free to explore the available processors and their configurations in the Bento [Processors](/resources/stacks/bento/components/processors/) documentation.

##### **Output Component**

The `output` component determines where the processed data will be sent after passing through the pipeline. You can configure various output options such as writing to files, sending messages to message queues, or interacting with external APIs. Here's an example configuration for Fastbase depot:

```yaml
output:
  broker: 
    outputs:
    - broker:
        pattern: fan_out
        outputs:
        - plugin:
            address: ${{dataos://fastbase:default/test007}}
            metadata:
              auth:
                token:
                  enabled: true
                  token: ${{DataOS-User-API-Key}}
              description: ${{Random users data}}
              format: AVRO
              schema: ${{"{\"name\":\"default\",\"type\":\"record\",\"namespace\":\"defaultNamespace\",\"fields\":[{\"name\":\"age\",\"type\":\"int\"},{\"name\":\"city\",\"type\":\"string\"},{\"name\":\"dob\",\"type\":\"string\"},{\"name\":\"email\",\"type\":\"string\"},{\"name\":\"gender\",\"type\":\"string\"},{\"name\":\"name\",\"type\":\"string\"},{\"name\":\"page\",\"type\":\"int\"},{\"name\":\"seed\",\"type\":\"string\"}]}"}}
              schemaLocation: http://registry.url/schemas/ids/12 
              title: ${{Random Uses Info}}
              type: STREAM
          type: dataos_depot
        - stdout: {}
```

In this example, the `output` is configured to use the `broker` pattern with a `fan_out` strategy. The data will be sent to both the `dataos_depot` plugin, specifically to the `fastbase:default/test007` address, and the `stdout` output for logging purposes.

Feel free to explore the available output options and their configurations in the Bento [outputs](/resources/stacks/bento/components/output/) documentation.

### **Apply the YAML file**

You can apply the YAML file, to create a Service resource within the DataOS environment using the command given below:

```bash
dataos-ctl apply -f ${{path-of-the-config-file}} -w ${{workspace}}
```

### **Check Topic Consume in Fastbase Depot**

#### **Check Run time**

```bash
dataos-ctl -t service -w ${{workspace}} -n ${{service-name}}  get runtime -r
# Sample
dataos-ctl -t service -w public -n pulsar-random  get runtime -r
```

#### **List all tenants**

```bash
dataos-ctl fastbase tenant list
```

#### **List all Namespaces within the Public Tenant**

```bash
dataos-ctl fastbase namespace list -t ${{tenant}}
```

#### **List all topics in public/default namespace**

```bash
dataos-ctl fastbase topic list -n ${{namespace}}
# Sample
dataos-ctl fastbase topic list -n public/default
```

#### **Check Topic Consume**

```bash
dataos-ctl fastbase topic consume -p -s -t persistent://${{tenant}}/${{namespace}}/${{topic}}
# Sample
dataos-ctl fastbase topic consume -p -s -t persistent://public/default/test12
```