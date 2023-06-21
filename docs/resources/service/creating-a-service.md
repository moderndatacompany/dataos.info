# Creating a Service
    
## Diagrammatic Representation of Sample Service
    
![Blank diagram.svg](./blank_diagram.svg)

## Service YAML

```yaml
version: v1 # Version
name: hit-collector-service # Service Name
type: service # Type here is Service
tags: # Tags
    - collector
    - hit
    - gtm
    - event
    - service
description: Receives Hit data and Sinks to DataOS stream # Description

service: # Service Section
    title: "Hit Collector Service" # Title of the Service
    replicas: 1 # Replicas

    autoScaling: # Autoscaler
    enabled: true
    minReplicas: 2
    maxReplicas: 4
    targetMemoryUtilizationPercentage: 80
    targetCPUUtilizationPercentage: 80

    ingress: # Ingress
    enabled: true
    stripPath: false
    path: /hit-collector
    noAuthentication: true

    stack: benthos # Stack Name
    logLevel: INFO
    dryRun: true
    servicePort: 8099 # Service Port

# Benthos Stack-Specific Properties
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

## Running a Service

Run the `apply` command on DataOS CLI to create the service resource in DataOS environment.

```shell
dataos-ctl apply -f <filename.yaml> -w <name of the workspace>
```

To learn more about `apply` command, refer to the [CLI](../../interfaces/cli/command_reference.md) section.