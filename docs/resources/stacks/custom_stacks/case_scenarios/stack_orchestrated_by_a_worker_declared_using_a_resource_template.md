# Stack orchestrated by a Worker declared using a Resource Template

```yaml
name: "function-mesh-v1"
version: v1alpha
type: stack
layer: user
description: "dataos function mesh stack alpha version 01"
stack:
  name: function-mesh
  version: "1.0"
  flavor: icebase-sink
  reconciler: stackManager
  stackSpecValueSchema:
    jsonSchema: |
      {"$schema":"http://json-schema.org/draft-04/schema#","type":"object","properties":{"image":{"type":"string"},"input":{"type":"object","properties":{"datasets":{"type":"array","items":[{"type":"string"}]},"options":{"type":"object","additionalProperties":{"type":"string"},"properties":{"cleanupSubscription":{"type":"boolean"}}}},"required":["datasets"]},"output":{"type":"object","properties":{"dataset":{"type":"string"},"options":{"type":"object","additionalProperties":{"type":"string"}}},"required":["dataset"]}},"required":["image","input","output"]}
  workerConfig:
    resourceTemplate: |
      apiVersion: compute.functionmesh.io/v1alpha1
      kind: FunctionMesh
      metadata:
        name: function-mesh{{.Stamp}}
        namespace: function-mesh
      spec:
        sinks:
          - image: {{getNested .ApplicationSpec.StackSpec "image" }}
            className: "org.apache.pulsar.ecosystem.io.lakehouse.SinkConnector"
            replicas: 1
            maxReplicas: 1          
            input:
              topics:
              {{- range $datasets := .ApplicationSpec.StackSpec.input.datasets }}
              {{- $ridataset := resolve $datasets }}
              {{- if getMapValue $ridataset.Resolution "isPersistent" }}
                - persistent://{{ $ridataset.Pulsar.Tenant }}/{{- $ridataset.Collection }}/{{- $ridataset.Dataset }}
              {{- else }}
                - non-persistent://{{ $ridataset.Pulsar.Tenant }}/{{- $ridataset.Collection }}/{{- $ridataset.Dataset }}
              {{- end }}
              {{- end }}
              typeClassName: "org.apache.pulsar.client.api.schema.GenericObject"
            tenant: "public"
            namespace: "default"
            name: {{ .Name }}
            {{- if hasNested .ApplicationSpec.StackSpec.input.options "subscriptionPosition" }}
            subscriptionPosition: {{ getNested .ApplicationSpec.StackSpec.input.options "subscriptionPosition" }}
            {{- else }}
            subscriptionPosition: "latest"
            {{- end }}
            {{- if hasNested .ApplicationSpec.StackSpec.input.options "subscriptionName" }}
            subscriptionName: {{ getNested .ApplicationSpec.StackSpec.input.options "subscriptionName" }}
            {{- else }}
            subscriptionName: "defaultsubname"
            {{- end }}
            {{- if hasNested .ApplicationSpec.StackSpec.input.options "processingGuarantee" }}
            processingGuarantee: {{ getNested .ApplicationSpec.StackSpec.input.options "processingGuarantee" }}
            {{- else }}
            processingGuarantee: "effectively_once"
            {{- end }}
            {{- if hasNested .ApplicationSpec.StackSpec.input.options "cleanupSubscription" }}
            cleanupSubscription: {{ getNested .ApplicationSpec.StackSpec.input.options "cleanupSubscription" }}
            {{- else }}
            cleanupSubscription: true
            {{- end }}
            sinkConfig:
              {{- $rodataset := resolve .ApplicationSpec.StackSpec.output.dataset }}
              {{- if eq $rodataset.Format "iceberg" }}
              type: "iceberg"
              {{- end }}
              maxCommitInterval: 10
              maxRecordsPerCommit: 1000
              catalogName: "{{ $rodataset.Depot }}"
              tableNamespace: "{{ $rodataset.Collection }}"
              tableName: "{{ $rodataset.Dataset }}"
              {{- if eq $rodataset.Type "abfss" }}
              hadoop.fs.azure.account.key.{{ $rodataset.Abfss.Account }}.dfs.core.windows.net: ""
              catalogProperties:
                warehouse: "{{- $rodataset.Type }}://{{ $rodataset.Abfss.Container }}@{{ $rodataset.Abfss.Account }}.dfs.core.windows.net/{{ $rodataset.Abfss.RelativePath }}"
                catalog-impl: "hadoopCatalog"
              {{- end }}
            pulsar:
              pulsarConfig: "pulsar-cluster"
              authSecret: "auth-secrets"
            pod:
              imagePullSecrets:
                - name: dataos-container-registry
              securityContext:
                runAsUser: 0
                fsGroup: 0
              serviceAccountName: "default"
            resources:
              limits:
                cpu: "4"
                memory: 8G
              requests:
                cpu: "2"
                memory: 2G
            java:
              jar: /pulsar/connectors/pulsar-io-lakehouse-2.11.0-dataos.1-cloud.nar
              jarLocation: ""
              log:
                level: "info"
            clusterName: pulsar
            autoAck: true
  dataOsAddressJqFilters:
    - .output.dataset[]
  secretProjection:
    type: "envVars"
```