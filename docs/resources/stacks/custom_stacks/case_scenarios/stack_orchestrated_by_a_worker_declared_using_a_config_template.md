# Stacks orchestrated by a Worker declared using a Config Template

## Sample 1

### **Stack YAML manifest**

```yaml
name: "pulsar-function-v3"
version: v1alpha
type: stack
layer: user
description: "dataos pulsar function stack alpha version 02"
stack:
  name: pulsar-function
  version: "3.0"
  flavor: icebase-sink
  reconciler: stackManager
  dataOsAddressJqFilters:
    - .input.datasets[]
    - .output.datasets[]
  secretProjection:
    type: "propFile"
  image:
    registry: docker.io
    repository: rubiklabs
    image: pulsar-io-lakehouse
    tag: 2.10.2-d6
    auth:
      imagePullSecret: dataos-container-registry
  command:
    - java
  arguments:
    - -cp
    - '/pulsar/instances/java-instance.jar:lib/*'
    - -Dpulsar.functions.instance.classpath='lib/*'
    - -Dpulsar.log.level=INFO
    - -Dbk.log.level=INFO
    - io.dataos.pulsar.functions.init.PulsarFunctionInit
    - /etc/dataos/config/jobconfig.yaml
  stackSpecValueSchema:
    jsonSchema: |
      {"$schema":"http://json-schema.org/draft-04/schema#","type":"object","properties":{"input":{"type":"object","properties":{"datasets":{"type":"array","items":[{"type":"string"}]},"options":{"type":"object","additionalProperties":{"type":"string"},"properties":{"cleanupSubscription":{"type":"boolean"},"subscriptionPosition":{"type":"string","enum":["EARLIEST","LATEST"]},"processingGuarantees":{"type":"string","enum":["EFFECTIVELY_ONCE","ATLEAST_ONCE","ATMOST_ONCE"]}}}},"required":["datasets"]},"output":{"type":"object","properties":{"datasets":{"type":"array","items":[{"type":"string"}]},"options":{"type":"object","additionalProperties":{"type":"string"},"properties":{"iceberg":{"type":"object","properties":{"properties":{"type":"object","additionalProperties":{"type":"string"}}}},"hudi":{"type":"object","properties":{"properties":{"type":"object","additionalProperties":{"type":"string"}}}},"delta":{"type":"object","properties":{"properties":{"type":"object","additionalProperties":{"type":"string"}}}}}}},"required":["datasets"]}},"required":["input","output"]}
  workerConfig:
    configFileTemplate: |
      jobconfig.yaml: |
        tenant: public
        namespace: default
        name: {{ .Name }}
        className: org.apache.pulsar.functions.api.utils.IdentityFunction
        {{- if hasNested .ApplicationSpec.StackSpec.input.options "processingGuarantees" }}
        processingGuarantees: {{ getNested .ApplicationSpec.StackSpec.input.options "processingGuarantees" }}
        {{- else }}
        processingGuarantees: "EFFECTIVELY_ONCE"
        {{- end }}
        autoAck: true
        source:
          typeClassName: org.apache.pulsar.client.api.schema.GenericObject
          subscriptionType: FAILOVER
          inputSpecs:
          {{- range $datasets := .ApplicationSpec.StackSpec.input.datasets }}
          {{- $ridataset := resolve $datasets }}
          {{- if getMapValue $ridataset.Resolution "isPersistent" }}
            persistent://{{ $ridataset.Pulsar.Tenant }}/{{- $ridataset.Collection }}/{{- $ridataset.Dataset }}: {}
          {{- else }}
            - non-persistent://{{ $ridataset.Pulsar.Tenant }}/{{- $ridataset.Collection }}/{{- $ridataset.Dataset }}
          {{- end }}
          {{- end }}
          {{- if hasNested .ApplicationSpec.StackSpec.input.options "subscriptionPosition" }}
          subscriptionPosition: {{ getNested .ApplicationSpec.StackSpec.input.options "subscriptionPosition" }}
          {{- else }}
          subscriptionPosition: "LATEST"
          {{- end }}
          {{- if hasNested .ApplicationSpec.StackSpec.input.options "subscriptionName" }}
          subscriptionName: {{ getNested .ApplicationSpec.StackSpec.input.options "subscriptionName" }}
          {{- else }}
          subscriptionName: "defaultsubname"
          {{- end }}
          {{- if hasNested .ApplicationSpec.StackSpec.input.options "cleanupSubscription" }}
          cleanupSubscription: {{ getNested .ApplicationSpec.StackSpec.input.options "cleanupSubscription" }}
          {{- else }}
          cleanupSubscription: false
          {{- end }}
        sink:
          className: org.apache.pulsar.ecosystem.io.lakehouse.SinkConnector
          typeClassName: org.apache.pulsar.client.api.schema.GenericObject
          configs: 
            {{- $output := .ApplicationSpec.StackSpec.output }}
            {{- range $outdatasets := $output.datasets }}
            {{- $dataset := resolve $outdatasets }}
            {{- if or (eq $dataset.Format "iceberg") (eq $dataset.Format "ICEBERG") }}
            type: "iceberg"
            maxCommitInterval: 10
            maxRecordsPerCommit: 1000
            catalogName: "{{ $dataset.Depot }}"
            tableNamespace: "{{ $dataset.Collection }}"
            tableName: "{{ $dataset.Dataset }}"
            {{- if or (eq $dataset.Type "abfss") (eq $dataset.Type "ABFSS") }}
            catalogProperties:
              warehouse: "{{- $dataset.Type }}://{{ $dataset.Abfss.Container }}@{{ $dataset.Abfss.Account }}.dfs.core.windows.net/{{ $dataset.Abfss.RelativePath }}"
              catalog-impl: "hadoopCatalog"
            {{- end }}
            {{- if or (eq $dataset.Type "gcs") (eq $dataset.Type "GCS") }}
            catalogProperties:
              warehouse: "gs://{{ $dataset.Gcs.Bucket }}/{{ $dataset.Gcs.RelativePath }}"
              catalog-impl: "hadoopCatalog"
            {{- end }}
            {{- if or (eq $dataset.Type "s3") (eq $dataset.Type "S3") }}
            catalogProperties:
              warehouse: "s3a://{{ $dataset.S3.Bucket }}/{{ $dataset.S3.RelativePath }}"
              catalog-impl: "hadoopCatalog"
            {{- end }}      
            {{- end }}  
            {{- end }}
            {{- range $conf, $value := getNested $output.options.iceberg "properties" }}
            tableProperties:
              {{ $conf | quote }}: {{ $value | quote }}
            {{- end }}
        componentType: SINK
```

### **Orchestrator Manifest**

```yaml
version: v1beta
name: porosclusterresources
type: worker
tags:
  - function-mesh
  - sdk
  - sampletest
description: This is sample worker for function mesh dataos
worker:
  replicas: 1
  title: function-mesh Sample Test Job
  tags:
    - function-mesh
    - worker
  stack: pulsar-function+icebase-sink:3.0
  autoScaling:
    enabled: true
    minReplicas: 1
    maxReplicas: 5
    targetMemoryUtilizationPercentage: 80
    targetCPUUtilizationPercentage: 80
  compute: runnable-default
  resources:
    requests:
      cpu: 2000m
      memory: 2048Mi
    limits:
      cpu: 4000m
      memory: 8192Mi
  stackSpec:
    input:
      datasets:
        - "dataos://systemstreams:poros/clusterdataosresources"
      options:
        subscriptionPosition: "EARLIEST"
        subscriptionName: "clusterdataosresources"
        processingGuarantees: "EFFECTIVELY_ONCE"
        cleanupSubscription: true
    output:
      datasets:
        - "dataos://lakehouses3:meshsink/clusterdataosresources"
      options:
        iceberg:
          properties:
            "write.format.default" : "parquet"
            "write.metadata.compression-codec" : "gzip"
```

## Sample 2

```yaml
name: "soda-worker-v1"
version: v1alpha
type: stack
layer: user
description: "soda worker stack version 1"
stack:
  name: sodaworker
  version: "1.0"
  flavor: "python"
  reconciler: "stackManager"
  dataOsAddressJqFilters:
    - .inputs[].dataset
  secretProjection:
    type: "envVars"
  image:
    registry: docker.io
    repository: rubiklabs
    image: dataos-soda
    tag: 0.0.11-dev
    auth:
      imagePullSecret: dataos-container-registry
  command:
    - python3
  arguments:
    - main.py
    - --configuration
    - /etc/dataos/config/jobconfig.yaml
  environmentVars:
    PULSAR_TOPIC_ADDRESS: dataos://systemstreams:soda/data_quality_result
    RESOURCE_DIR_PATH: "/etc/dataos/resources"
  stackSpecValueSchema:
    jsonSchema: |
      {"$schema":"http://json-schema.org/draft-04/schema#","type":"object","properties":{"inputs":{"type":"array","items":[{"type":"object","properties":{"dataset":{"type":"string"},"checks":{"type":"array","additionalProperties":{"type":"object"}},"options":{"type":"object","additionalProperties":{"type":"string"}},"profile":{"type":"object","properties":{"columns":{"type":"array","minItems":1,"items":[{"type":"string"}]}},"required":["columns"]}},"required":["dataset"],"oneOf":[{"required":["checks","profile"]},{"required":["checks"],"not":{"allOf":[{"required":["profile"]}]}},{"required":["profile"],"not":{"allOf":[{"required":["checks"]}]}}]}]}},"required":["inputs"]}
  workerConfig:
    configFileTemplate: |
      jobconfig.yaml: |
      {{ toYaml .ApplicationSpec.StackSpec | indent 2 }}
```