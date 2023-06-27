# Creating a Service

This section covers a Service YAML file structure,configuration options, and applying the YAML to create a Service resource.


## Service YAML

To create a Service resource, you need to configure the YAML file with the appropriate settings. The following sections explain the necessary configurations.

### **Configuring the Resource Section**

A Service is a type of resource in DataOS. Below is the YAML configuration for the Resource Section:
```yaml
name: {{my-workflow}}
version: v1 
type: service 
tags: 
  - {{dataos:type:resource}}
  - {{dataos:type:workspace-resource}}
description: {{This is a sample service YAML configuration}}
owner: {{iamgroot}}
```
<center><i>Resource Section Configuration for a Service</i></center>

For detailed customization options and additional fields within the Resource Section, refer to the [Resource Configuration](../../resources.md).

### **Configuring the Service-specific Section**

The Service-specific Section contains configurations specific to the Service resource. The YAML syntax is provided below:

```yaml
service: 
    title: {{"Hit Collector Service"}}
    replicas: {{1}}
    autoScaling: 
        enabled: {{true}}
        minReplicas: {{2}}
        maxReplicas: {{4}}
        targetMemoryUtilizationPercentage: {{80}}
        targetCPUUtilizationPercentage: {{80}}
    ingress: 
        enabled: {{true}}
        stripPath: {{false}}
        path: {{/hit-collector}}
        noAuthentication: {{true}}
    stack: {{stack}} # Specify stack here
    logLevel: {{INFO}}
    dryRun: {{true}}
    servicePort: {{8099}}
    {{Stack-specific-section}}
```
<center><i>Service-specific Section Configuration</i></center>

### **Configuring the Stack-specific Section**

The Stack-specific Section allows you to specify the desired stack for executing your service. Depending on your requirements, you can choose from the following supported stacks:

- [Benthos Stack](../stacks/benthos.md): The Benthos stack provides advanced capabilities for stream data processing and analysis.

- [Alpha Stack](../stacks/alpha.md): The Alpha stack offers a powerful environment for hosting web-appliation, and custom Docker images atop DataOS.

- [Beacon Stack](../stacks/beacon.md): The Beacon stack provides a comprehensive set of tools and utilities for managing PostsgreSQL Database.

To configure the Stack-specific Section, refer to the appropriate stack documentation for detailed instructions on setting up and customizing the stack according to your needs. Each stack has its unique features and configurations that can enhance the functionality of your workflow. A sample is provided below.

<details>
<summary>
Click here to view a sample service
</summary>

The sample service ingests product data from the thirdparty01 depot and store it in the icebase depot. This workflow leverages the Flare stack to efficiently execute the necessary data ingestion tasks. The provided YAML code snippet outlines the configuration and specifications of this workflow.

#### **Sample Stack-specific Section for Benthos Stack**

<center><i>Sample Stack-specific Section Configuration for Benthos</i></center>

<center>

![Blank diagram.svg](./blank_diagram.svg)

<i> Diagrammatic Representation of Above Service </i>

</center>



```yaml
name: my-workflow
version: v1 
type: service 
tags: 
  - dataos:type:resource
  - dataos:type:workspace-resource
description: This is a sample service YAML configuration
owner: iamgroot
service: 
    title: "Hit Collector Service" 
    replicas: 1 
    autoScaling: 
        enabled: true
        minReplicas: 2
        maxReplicas: 4
        targetMemoryUtilizationPercentage: 80
        targetCPUUtilizationPercentage: 80
    ingress: 
        enabled: true
        stripPath: false
        path: /hit-collector
        noAuthentication: true
    stack: benthos 
    logLevel: INFO
    dryRun: true
    servicePort: 8099
    benthos:
        # Input (From Google Tag Manager API)
        input:
            http_server:
            address: 0.0.0.0:8099
            path: /hit-collector
            allowed_verbs:
                - POST
            timeout: 5s
            processors:
            - log:
                level: INFO
                message: hit collector - received hit...

        # Pipeline (Processing)
        pipeline:
            processors:
            - log:
                level: DEBUG
                message: processing message...
            - log:
                level: DEBUG
                message: ${! meta() }
            - bloblang: meta status_code = 200
            - for_each:
            - conditional:
                condition:
                    type: processor_failed
                processors:
                - log:
                    level: ERROR
                    message: 'Schema validation failed due to: ${!error()}'
                - bloblang: meta status_code = 400
                - log:
                    level: DEBUG
                    message: ${! meta() }
                - bloblang: |
                    root.payload = this.string().encode("base64").string()
                    root.received_at = timestamp("2006-01-02T15:04:05.000Z")
                    root.metadata = meta()
                    root.id = uuid_v4()
            - log:
                level: DEBUG
                message: processing message...complete
            threads: 1

        # Output (Into Kafka Depot)
        output:
            broker:
            outputs:
            - broker:
                outputs:
                - type: dataos_depot
                    plugin:
                    address: dataos://kafkapulsar:default/gtm_hits_dead_letter01
                    metadata:
                        type: STREAM
                        description: The GTM Hit Error Data Stream
                        format: json
                        schema: '{"type":"record","name":"default","namespace":"default","fields":[]}'
                        tags:
                        - hit
                        - gtm
                        - stream
                        - error-stream
                        - dead-letter
                        title: GTM Hit Error Stream
                - type: sync_response
                pattern: fan_out
                processors:
                - bloblang: root = if !errored() { deleted() }
            - broker:
                outputs:
                - type: dataos_depot
                    plugin:
                    address: dataos://kafkapulsar:default/gtm_hits01
                    metadata:
                        type: STREAM
                        description: The GTM Hit Data Stream
                        format: json
                        schema: '{"type":"record","name":"default","namespace":"default","fields":[]}'
                        tags:
                        - hit
                        - gtm
                        - event
                        - stream
                        title: GTM Hit Stream
                - type: sync_response
                pattern: fan_out
                processors:
                - bloblang: root = if errored() { deleted() }
            pattern: fan_out
```


## Apply a Service YAML

Run the `apply` command on DataOS CLI to create the service resource in DataOS environment.

```shell
dataos-ctl apply -f <filename.yaml> -w <name of the workspace>
```

To learn more about `apply` command, refer to the [CLI](../../interfaces/cli/command_reference.md) section.