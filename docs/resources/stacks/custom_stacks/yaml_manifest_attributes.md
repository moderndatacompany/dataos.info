# Attributes of Stack YAML manifest

## Structure of a Stack YAML

```yaml
# Stack-specific section
stack:

# Stack meta section
  name: {{stack name}}
  flavor: {{stack flavor}}
  version: {{stack version}}
  reconciler: {{reconciler}}

# Image specification section
  image:
    registry: {{continer registry}}
    repository: {{repository}}
    image: {{image}}
    tag: {{tag}}
    auth:
      imagePullSecret: {{secret}}

# Command and argument sections
  command:
    - {{list of commands}}
  arguments:
    - {{arguments}}

# Environment variables
  environmentVars:
		{{environment variables}}

# Port configuration
  ports:
    name: {{port name}}
    servicePort: {{service port}}
    targetPort: {{target port}}

# Stack Spec value JSON schema
  stackSpecValueSchema:
    jsonSchema: {{json schema}}

# Orchestrator configuration
  workflowJobConfig:
    configFileTemplate: {{config file template}}
    conatinerResourceTemplate: {{container resource template}}
    resourceTemplateConfig:
      resourceTemplate: {{resource template}}
      successCondition: {{success condition}}
      failureCondition: {{failure condition}}
  serviceConfig:
    configFileTemplate: {{config file template}}
    conatinerResourceTemplate: {{container resource template}}
  workerConfig:
    configFileTemplate: {{config file template}}
    conatinerResourceTemplate: {{container resource template}}
    resourceTemplate: {{resource template}}

# Secret Projection
  secretProjection:
    type: {{secret projection type}}

# DataOS Address JQ Filters
dataOsAddressJqFilters:
  - .inputs[].dataset
```

## Configuration Attributes

## **`stack`**

**Description:** Mapping for the attributes of Stack Resource

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | mandatory | none | none |

**Example Usage:**

```yaml
stack:
	{} # attributes of Stack Resource
```

---

### **`name`**

**Description:** Name of the Stack Resource

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | any string (if there is any regex check) |

**Example Usage:** 

```yaml
name: alpha
```

---

### **`flavor`**

**Description:** Flavor of the Stack Resource

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | none |

**Example Usage:** 

```yaml
flavor: rest
```

---

### **`version`**

**Description:** Version of the Stack Resource

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | ‘1.0’, ‘2.0’, or any other stack version in string format |

**Example Usage:** 

```yaml
version: '1.0'
```

---

### **`reconciler`**

**Description:** Specifies the reconciler responsible for managing this stack

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | none |

**Example Usage:** 

```yaml
reconciler: alphaLegacyStackManager
```

---

### **`dataOsAddressJqFilters`**

**Description:** DataOS Address JQ Filters specify which attributes within the YAML manifest need to be interpolated with DataOS Addresses for the retrieval of depot definitions and credentials.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | none |

**Example Usage:**

```yaml
# Example 1
dataOsAddressJqFilters:
  - .inputs[]
  - .outputs[]

# Example 2
dataOsAddressJqFilters:
  - .inputs[].dataset
  - .outputs[].depot
  - .job.inputs[].dataset
  - .job.outputs[].depot

# Example 3
dataOsAddressJqFilters:
  - .inputs[].dataset
```

---

### **`image`**

**Description:** container image configuration

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | optional | none | any other container registry |

**Example Usage:** 

```yaml
image:
  registry: docker.io
  repository: abcd
  image: random
  tag: 0.0.8-dev
  auth:
    imagePullSecret: dataos-container-registry
```

---

#### **`registry`**

**Description:** specifies the container registry name

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | any valid container registry |

**Example Usage:** 

```yaml
registry: docker.io
```

---

#### **`repository`**

**Description:** Specifies the repository where image is hosted

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | any other container registry |

**Example Usage:** 

```yaml
repository: abcd
```

---

#### **`image`**

**Description:** specifies the image name

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | any valid image name present in the specified repository |

**Example Usage:** 

```yaml
image: random
```

---

#### **`tag`**

**Description:** specifies the version tag of image

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | valid image tag |

**Example Usage:** 

```yaml
tag: 0.0.8
```

---

#### **`auth`**

**Description:** authentication details for pulling the image

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | optional | none | none |

**Example Usage:** 

```yaml
auth:
  imagePullSecret: dataos-container-registry
```

---

##### **`imagePullSecret`**

**Description:** specifies the Secret Resource for the container registry

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | valid image tag |

**Example Usage:** 

```yaml
imagePullSecret: abcd-container-registry
```

---

### **`command`**

**Description:** specifies the commands mentioned within the Docker file's CMD section. This includes the commands that are to be executed within the container.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of strings | optional | none | valid command |

**Example Usage:** 

```yaml
# Example 1
command:
  - python3

# Example 2
command:
  - /opt/dataos/benthos-ds
```

---

### **`arguments`**

**Description:** specifies the additional arguments apart from the primary command specified within the Dockerfile. Addtional arguments for the command, indicating to run and specify a configuration file.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of strings | optional | none | valid command |

**Example Usage:** 

```yaml
# Example 1
arguments:
  - main.py
  - '--configuration'
  - /etc/dataos/config/jobconfig.yaml

# Example 2
arguments:
  - run
  - '-c'
  - /etc/dataos/config/jobconfig.yaml
```

---

### **`environmentVars`**

**Description:** environment variables 

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | optional | none | none |

**Example Usage:**

```yaml
environmentVars:
  PULSAR_TOPIC_NAME: persistent://system/soda/data_quality_result
  RESOURCE_DIR_PATH: /etc/dataos/resources
```

| Name | Value |
| --- | --- |
| DEPOT_SERVICE_URL | https://{{dataos-context}}/ds |
| GATEWAY_URL | https://{{dataos-context}}/gateway |
| HEIMDALL_URL | https://{{dataos-context}}/heimdall |
| HERA_URL | https://{{dataos-context}}/hera/api |
| SCS_SERVICE_URL | http://stack-exec-context-sink.poros.svc.cluster.local:39100/sink |
| METIS_URL | https://{{dataos-context}}/metis2 |
| PULSAR_SERVICE_URL | pulsar+ssl://tcp.{{dataos-context}}:6651 |
| MINERVA_JDBC_URL | jdbc:trino://tcp.{{dataos-context}}:7432 |
| DATAOS_NAME |  sanity-read-azure-nabeel-05 |
| DATAOS_RESOURCE_ID | workflow:v1:sanity-read-azure-nabeel-05:public |
| DATAOS_RUN_ID | cvi31p4sagw0 |
| DATAOS_TYPE | workflow |
| DATAOS_WORKSPACE | public |
| DATAOS_FQDN | {{dataos-context}} |
| DATAOS_TAGS | sanity,tags |
| DATAOS_DESCRIPTION | The purpose of this job is to verify if we are able to read different file formats from azure abfss or not. |
| DATAOS_CONFIG_DIR | /etc/dataos/config |
| DATAOS_TEMP_DIR | /var/dataos/temp_data |
| DATAOS_SECRET_DIR | /etc/dataos/secret |
| RUNNABLE_ARTIFACT_DIR | /etc/dataos/work |
| RUNNABLE_TYPE | workflow |
| DATAOS_RUN_AS_APIKEY | {{dataos user apikey token}} |
| DATAOS_RUN_AS_USER | {{user id of the user}} |
| DATAOS_STAMP | -boo1 |
| DATAOS_UID | 15d4b6bb-2aaa-45b3-8a57-2e302cff06fb |
| HERA_SSL | false |
| LOG_LEVEL | INFO |
| DATAOS_LOG_LEVEL | INFO |
| METIS_AUTH_PROVIDER | dataos-apikey |
| MINERVA_TCP_HOST | tcp.{{dataos-context}} |
| MINERVA_TCP_PORT | 7432 |
| SSL_KEYSTORE_PASSWORD | {{ssl keystore password}} |
| SSL_TRUSTSTORE_PASSWORD | {{ssl truststore password}} |
| DATAOS_IS_DRY_RUN | false |

---

### **`ports`**

**Description:** port specification

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | optional | none | none |

**Example Usage:**

```yaml
ports:
	name: newport
	servicePort: 9876
	targetPort: 7658
```

---

#### **`name`**

**Description:** port name declaration

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | none |

**Example Usage:**

```yaml
name: newport
```

---

#### **`servicePort`**

**Description:** service port declaration

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| integer | optional | none | none |

**Example Usage:**

```yaml
servicePort: 9876
```

---

#### **`targetPort`**

**Description:** target port declaration

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| integer | optional | none | none |

**Example Usage:**

```yaml
targetPort: 7698
```

---

### **`stackSpecValueSchema`**

**Description:** schema for the value used in the Stack’s specification

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | mandatory | none | none |

**Example Usage:** 

```yaml
stackSpecValueSchema:
  jsonSchema: ''
```

---

#### **`jsonSchema`**

**Description:** JSON schema specifying the structure of the Stack's configuration values

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | valid json schema |

**Example Usage:** 

```yaml
# Example 1
jsonSchema: >
  {"$schema":"http://json-schema.org/draft-04/schema#","type":"object","properties":{"inputs":{"type":"array","items":[{"type":"object","properties":{"dataset":{"type":"string"},"checks":{"type":"array","additionalProperties":{"type":"object"}},"options":{"type":"object","additionalProperties":{"type":"string"}},"profile":{"type":"object","properties":{"columns":{"type":"array","minItems":1,"items":[{"type":"string"}]}},"required":["columns"]}},"required":["dataset"],"oneOf":[{"required":["checks","profile"]},{"required":["checks"],"not":{"allOf":[{"required":["profile"]}]}},{"required":["profile"],"not":{"allOf":[{"required":["checks"]}]}}]}]}},"required":["inputs"]}

# Example 2
jsonSchema: |
  {
    "$schema": "http://json-schema.org/draft-04/schema",
    "type": "object",
    "properties": {
      "input": {
        "type": "object"
      },
      "metrics": {
        "type": "object"
      },
      "logger": {
        "type": "object"
      },
      "http": {
        "type": "object"
      },
      "pipeline": {
        "type": "object"
      },
      "output": {
        "type": "object"
      }
    },
    "required": [
      "input"
    ]
  }

# Example 3
jsonSchema: >
  {"$schema":"http://json-schema.org/draft-07/schema#","$id":"https://dataos.io/v1.0/sparkapplication","type":"object","properties":{"driver":{"type":"object","properties":{"coreLimit":{"type":"string"},"cores":{"type":"integer"},"memory":{"type":"string"}},"required":["coreLimit","cores","memory"]},"executor":{"type":"object","properties":{"coreLimit":{"type":"string"},"cores":{"type":"integer"},"instances":{"type":"integer"},"memory":{"type":"string"}},"required":["coreLimit","cores","instances","memory"]},"sparkConf":{"type":"object","additionalProperties":{"type":"string"}},"jarFile":{"type":"string"},"mainClass":{"type":"string"},"image":{"type":"string"},"inputs":{"type":"array","items":{"type":"string"}},"outputs":{"type":"array","items":{"type":"string"}}},"required":["driver","executor","jarFile","mainClass","image","inputs","outputs"]}

# Example 4
jsonSchema: >
      {"$schema":"http://json-schema.org/draft-04/schema#","type":"object","properties":{"inputs":{"type":"array","items":[{"type":"object","properties":{"dataset":{"type":"string"},"checks":{"type":"array","additionalProperties":{"type":"object"}},"options":{"type":"object","additionalProperties":{"type":"string"}},"profile":{"type":"object","properties":{"columns":{"type":"array","minItems":1,"items":[{"type":"string"}]}},"required":["columns"]}},"required":["dataset"],"oneOf":[{"required":["checks","profile"]},{"required":["checks"],"not":{"allOf":[{"required":["profile"]}]}},{"required":["profile"],"not":{"allOf":[{"required":["checks"]}]}}]}]}},"required":["inputs"]}
```

---

### **`workflowJobConfig`**

**Description:** specifies Workflow Resource’s Job config for a Stack

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | mandatory | none | none |

**Example Usage:** 

```yaml
workflowJobConfig: {}
```

---

#### **`configFileTemplate`**

**Description:** specifies config file template

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | none |

**Example Usage:** 

```yaml
configFileTemplate: |
  jobconfig.yaml: |
  {{ toYaml .ApplicationSpec.StackSpec | indent 2 }}

# Service Config File Template (Example 1)
configFileTemplate: |
  jobconfig.yaml: |
  {{ toYaml .ApplicationSpec.StackSpec | indent 2 }}
    logger:
      level: {{.ApplicationSpec.LogLevel}}
      add_timestamp: true
      format: json
      static_fields:
        '@service': {{.Name}}
    http:
      address: 0.0.0.0:{{.MetricPort}}
      root_path: /dataos-benthos
      debug_endpoints: false
    metrics:
      prometheus:
        push_url: "http://prometheus-pushgateway.sentinel.svc.cluster.local:9091"
        push_interval: "5s"
        push_job_name: "{{ .Name }}-{{ .Type }}{{ .Stamp }}"

# Service Config File Template (Example 2)
configFileTemplate: |
  jobconfig.yaml: |
  {{ toYaml .ApplicationSpec.StackSpec | indent 2 }}
    logger:
     level: {{.ApplicationSpec.LogLevel}}
     add_timestamp: true
     format: json
     static_fields:
       '@service': {{.Name}}
    http:
     address: 0.0.0.0:{{.MetricPort}}
     root_path: /dataos-benthos
     debug_endpoints: false
    metrics:
     prometheus:
        use_histogram_timing: false
        histogram_buckets: []
        add_process_metrics: false
        add_go_metrics: false
        push_url: "http://prometheus-pushgateway.sentinel.svc.cluster.local:9091"
        push_interval: "5s"
        push_job_name: "{{ .Name }}-{{ .Type }}{{ .Stamp }}"

# Worker Config File Template (Example 1)
configFileTemplate: |
  jobconfig.yaml: |
  {{ toYaml .ApplicationSpec.StackSpec | indent 2 }}
    logger:
     level: {{.ApplicationSpec.LogLevel}}
     add_timestamp: true
     format: json
     static_fields:
       '@service': {{.Name}}
    http:
     address: 0.0.0.0:{{.MetricPort}}
     root_path: /dataos-benthos
     debug_endpoints: false
    metrics:
     prometheus:
        use_histogram_timing: false
        histogram_buckets: []
        add_process_metrics: false
        add_go_metrics: false
        push_url: "http://prometheus-pushgateway.sentinel.svc.cluster.local:9091"
        push_interval: "5s"
        push_job_name: "{{ .Name }}-{{ .Type }}{{ .Stamp }}"

# Worker Config File Template (Example 2)
configFileTemplate: |
  jobconfig.yaml: |
  {{ toYaml .ApplicationSpec.StackSpec | indent 2 }}
    logger:
     level: {{.ApplicationSpec.LogLevel}}
     add_timestamp: true
     format: json
     static_fields:
       '@service': {{.Name}}
    http:
     address: 0.0.0.0:{{.MetricPort}}
     root_path: /dataos-benthos
     debug_endpoints: false
    metrics:
     prometheus:
        push_url: "http://prometheus-pushgateway.sentinel.svc.cluster.local:9091"
        push_interval: "5s"
        push_job_name: "{{ .Name }}-{{ .Type }}{{ .Stamp }}"

# Workflow Config File Template (Example 1)
configFileTemplate: |
  jobconfig.yaml: |
  {{ toYaml .ApplicationSpec.StackSpec | indent 2 }}
```

---

#### **`containerResourceTemplate`**

**Description:** specifies container resource template

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | none |

**Example Usage:** 

```yaml
containerResourceTemplate: 
	{}
```

---

#### **`resourceTemplateConfig`**

**Description:** specifies resource template configuration

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | mandatory | none | none |

**Example Usage:** 

```yaml
resourceTemplateConfig:
  resourceTemplate: {}
```

---

##### **`resourceTemplate`**

**Description:** specifies resource template

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | optional | none | none |

**Example Usage:** 

```yaml
    resourceTemplateConfig:
      resourceTemplate: |
        apiVersion: sparkoperator.k8s.io/v1beta2
        kind: SparkApplication
        metadata:
          name: {{.Name}}{{.Stamp}}-{{`{{workflow.creationTimestamp.m}}{{workflow.creationTimestamp.d}}{{workflow.creationTimestamp.H}}{{workflow.creationTimestamp.M}}{{workflow.creationTimestamp.S}}`}}
          namespace: {{ .Workspace }}
          labels:
            app: {{.Name}}
            app.kubernetes.io/name: '{{.Name}}'
            app.kubernetes.io/component: 'application'
            spark.application/name: '{{.Name}}{{.Stamp}}'
            workflow/stamp: '{{`{{workflow.creationTimestamp.m}}{{workflow.creationTimestamp.d}}{{workflow.creationTimestamp.H}}{{workflow.creationTimestamp.M}}{{workflow.creationTimestamp.S}}`}}'
        spec:
          image: "{{getNested .ApplicationSpec.StackSpec "image"}}"
          imagePullPolicy: IfNotPresent
          imagePullSecrets:
          - dataos-container-registry
          mainApplicationFile: "{{getNested .ApplicationSpec.StackSpec "jarFile"}}"
          mainClass: "{{getNested .ApplicationSpec.StackSpec "mainClass"}}"
          mode: cluster
          {{ if .NodeSelector }}
          nodeSelector:
          {{- range $key, $value := .NodeSelector }}
            {{$key | quote }}: {{ $value | quote }}
          {{- end }}
          {{- end }}
          sparkConf:
            "spark.driverEnv.spark.app.name": "{{.Name}}"
            "spark.kubernetes.executor.podNamePrefix": "{{.Name}}-{{.Stamp}}"     
          {{- if .ApplicationSpec.StackSpec.sparkConf }}
          {{- range $conf, $value := getNested .ApplicationSpec.StackSpec "sparkConf" }}
            {{ $conf | quote }}: {{ $value | quote }}
          {{- end }}
          {{- end }}   
          sparkVersion: 3.3.0
          type: Scala
          volumes:
            - name: dataos-config-mount
              configMap:
                name: "{{.Name}}-{{.Type}}{{.Stamp}}"
            - name: dataos-secret-mount
              projected:
                defaultMode: 420
                sources:
                - secret:
                    name: {{ .Name }}-ds-{{ .Type }}{{ .Stamp }}
            {{- if .ApplicationSpec.Secrets }}
            - name: dataos-secret-mount
               projected:
                sources:
                {{- range $data := .ApplicationSpec.Secrets }}
                - secret:
                    name: {{ $data | quote }}
                {{- end }}
            {{- end }}
            {{- if .ApplicationSpec.TempVolume -}}
            - name: {{.Name}}-{{.Type}}{{.Stamp}}-tdm
              persistentVolumeClaim:
                claimName: "{{.Name}}-{{.Type}}{{.Stamp}}-tv"
            {{- end }}
            {{- if .ApplicationSpec.PersistentVolume -}}
            - name: {{list .Name "persistent-data-mount" | join "-"}}
              persistentVolumeClaim:
                claimName: "{{.ApplicationSpec.PersistentVolume.Name}}"
            {{- end }}
            {{- if .Volumes }}
            {{- range $volume := .Volumes }}
            - name: {{$volume.Name}}
              {{ if $volume.IsPvc }}
              persistentVolumeClaim:
                claimName: "{{$volume.Name}}"
              {{ else }}
              projected:
                sources:
                {{- range $data := $volume.Secrets }}
                  - secret:
                      name: {{ $data | quote }}
                {{- end }}
                {{- range $data := $volume.ConfigMaps }}
                  - configMap:
                      name: {{ $data | quote }}
                {{- end }}
              {{- end }}
            {{- end }}
            {{- end }}
          driver:
            coreLimit: "{{getNested .ApplicationSpec.StackSpec "driver.coreLimit"}}"
            cores: {{getNested .ApplicationSpec.StackSpec "driver.cores"}}
            env:
            - name: DEPOT_SERVICE_URL
              value: "https://{{.DataOsFqdn}}/ds"
            - name: METIS_URL
              value: "https://{{.DataOsFqdn}}/metis"
            - name: STORE_URL
              value: "https://{{.DataOsFqdn}}/stores/api/v1"
            {{ if not .IsDryRun }}
            - name: RUNNABLE_NAME
              value: "{{`{{inputs.parameters.name}}`}}"
            - name: RUNNABLE_RUN_ID
              value: "{{`{{inputs.parameters.run-id}}`}}"
            - name: RUNNABLE_WORKFLOW_NAME
              value: "{{`{{inputs.parameters.workflow-name}}`}}"
            - name: RUNNABLE_WORKFLOW_RUN_ID
              value: "{{`{{inputs.parameters.workflow-run-id}}`}}"
            {{- end}}
            - name: METIS_JOB_NAME
              value: "{{.Name}}"
            - name: METIS_JOB_OWNER_NAME
              value: "{{.Owner}}"
            - name: DATAOS_JOB_TAGS
              value: "{{.PivotTags}}"
            - name: DATAOS_JOB_DESCRIPTION
              value: "{{.Description}}"
            - name: NAMESPACE
              value: "{{.Workspace}}"
            - name: PULSAR_SSL
              value: "false"
            - name: FLARE_AUDIT_MODE
              value: "{{.AuditMode}}"
            - name: IOSA_RECEIVER_URL
              value: "{{.IosaReceiverUrl}}"
            - name: MINERVA_JDBC_URL
              value: "{{.MinervaJdbcUrl}}"
            - name: GATEWAY_BASE_URL
              value: "{{.GatewayPublicBaseUrl}}"
            - name: MINERVA_SSL
              value: "{{.MinervaJdbcSsl}}"
            - name: DATAPOLICY_GATEWAY_SSL
              value: "{{.DatapolicyGatewaySsl}}"
            {{- range $conf, $value := .ApplicationSpec.EnvironmentVars }}
            - name: {{$conf}}
              value: {{ $value | quote }}
            {{- end }}
            envFrom:
              - secretRef:
                  name: "{{.Name}}-{{.Type}}{{.Stamp}}-env"
              {{ if .EnvironmentVarsFromSecret }}
              {{- range $secName := .EnvironmentVarsFromSecret }}
              - secretRef:
                  name: "{{$secName}}"
              {{- end }}
              {{- end }}
            memory: "{{getNested .ApplicationSpec.StackSpec "driver.memory"}}"
            volumeMounts:
              - mountPath: "{{.DataOsSecretMountPath}}"
                name: dataos-secret-mount
                readOnly: true
              {{- if .ApplicationSpec.Secrets }}
              - name: dataos-secret-mount
                mountPath: "{{.DataOsSecretMountPath}}"
                readOnly: true
              {{- end }}
              {{- if .Volumes }}
              {{- range $volume := .Volumes }}
              - name: {{$volume.Name}}
                mountPath: "{{$volume.MountPath}}"
                readOnly: {{$volume.ReadOnly}}
                {{ if $volume.SubPath }}
                subPath: "{{$volume.SubPath}}"
                {{- end }}
              {{- end }}
              {{- end }}
            {{- if .Tolerations }}
            tolerations:
        {{toYaml .Tolerations | indent 6}}
            {{- end }}
            serviceAccount: "{{.RunnableServiceAccount}}"
          executor:
            coreLimit: "{{getNested .ApplicationSpec.StackSpec "executor.coreLimit"}}"
            cores: {{getNested .ApplicationSpec.StackSpec "executor.cores"}}
            env:
            - name: DEPOT_SERVICE_URL
              value: "https://{{.DataOsFqdn}}/ds"
            - name: METIS_URL
              value: "https://{{.DataOsFqdn}}/metis"
            - name: STORE_URL
              value: "https://{{.DataOsFqdn}}/stores/api/v1"
            {{ if not .IsDryRun }}
            - name: RUNNABLE_NAME
              value: "{{`{{inputs.parameters.name}}`}}"
            - name: RUNNABLE_RUN_ID
              value: "{{`{{inputs.parameters.run-id}}`}}"
            - name: RUNNABLE_WORKFLOW_NAME
              value: "{{`{{inputs.parameters.workflow-name}}`}}"
            - name: RUNNABLE_WORKFLOW_RUN_ID
              value: "{{`{{inputs.parameters.workflow-run-id}}`}}"
            {{- end}}
            - name: METIS_JOB_NAME
              value: "{{.Name}}"
            - name: METIS_JOB_OWNER_NAME
              value: "{{.Owner}}"
            - name: DATAOS_JOB_TAGS
              value: "{{.PivotTags}}"
            - name: DATAOS_JOB_DESCRIPTION
              value: "{{.Description}}"
            - name: GATEWAY_BASE_URL
              value: "{{.GatewayPublicBaseUrl}}"
            - name: NAMESPACE
              value: "{{.Workspace}}"
            - name: FLARE_AUDIT_MODE
              value: "{{.AuditMode}}"
            - name: IOSA_RECEIVER_URL
              value: "{{.IosaReceiverUrl}}"
            {{- range $conf, $value := .ApplicationSpec.EnvironmentVars }}
            - name: {{$conf}}
              value: {{ $value | quote }}
            {{- end }}
            envFrom:
              - secretRef:
                  name: "{{.Name}}-{{.Type}}{{.Stamp}}-env"
              {{ if .EnvironmentVarsFromSecret }}
              {{- range $secName := .EnvironmentVarsFromSecret }}
              - secretRef:
                  name: "{{$secName}}"
              {{- end }}
              {{- end }}
            volumeMounts:
              {{- if .ApplicationSpec.Secrets }}
              - name: dataos-secret-mount
                mountPath: "{{.DataOsSecretMountPath}}"
                readOnly: true
              {{- end }}
              {{- if .Volumes }}
              {{- range $volume := .Volumes }}
              - name: {{$volume.Name}}
                mountPath: "{{$volume.MountPath}}"
                readOnly: {{$volume.ReadOnly}}
                {{ if $volume.SubPath }}
                subPath: "{{$volume.SubPath}}"
                {{- end }}
              {{- end }}
              {{- end }}
            instances: {{getNested .ApplicationSpec.StackSpec "executor.instances"}}
            memory: "{{getNested .ApplicationSpec.StackSpec "executor.memory"}}"
            {{- if .Tolerations }}
            tolerations:
        {{toYaml .Tolerations | indent 6}}
            {{- end }}
```

---

##### **`successCondition`**

**Description:** specifies success condition

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | none |

**Example Usage:** 

```yaml
successCondition: status.jobStatus.state == COMPLETED
```

---

##### **`failureCondition`**

**Description:** specifies failure condition

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | none |

**Example Usage:** 

```yaml
failureCondition: status.applicationState.state == FAILED
```

---

### **`workerConfig`**

**Description:** specifies Worker Resource’s configuration for a Stack

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | mandatory | none | none |

**Example Usage:** 

```yaml
workerConfig: {}
```

---

#### **`configFileTemplate`**

---

#### **`containerResourceTemplate`**

---

### **`serviceConfig`**

**Description:** specifies Service Resource’s configuration for a Stack

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | mandatory | none | none |

**Example Usage:** 

```yaml
workerConfig: {}
```

---

#### **`configFileTemplate`**

---

#### **`containerResourceTemplate`**

---

#### **`resourceTemplate`**

**Description:** specifies Resource Template

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | none |

**Example Usage:** 

```yaml
resourceTemplate: {}
```

---

### **`secretProjection`**

**Description:** describes how secrets are projected for this Stack

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | mandatory | none | none |

**Example Usage:** 

```yaml
secretProjection:
  type: propFile
```

---

#### **`type`**

**Description:** specifies the type of secret projection

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | propFile |

**Example Usage:** 

```yaml
# Example 1
type: propFile

# Example 2
type: envVars
```

