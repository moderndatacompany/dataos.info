# Attributes of Operator YAML

## Structure of Operator YAML configuration

```yaml
operator:
	components: # mandatory
	  - name: todo-reconciler # mandatory
	    type: worker # mandatory
	    compute: runnable-default # mandatory
	    runAsApiKey: abcdefghijklmnopqrstuvwxyz # mandatory
	    runAsUser: iamgroot
	    image: abirani/todo-operator:0.0.4 # mandatory
			imagePullSecret: hello
	    command:
	      - /opt/tmdc-io/todo-operator
	    arguments:
	      - operator
	      - todo
	      - --electionStateFile
	      - /opt/tmdc-io/leader-election.log
	    replicas: 1 # mandatory
	    environmentVars:
	      LOG_LEVEL: info
	      METRIC_PORT: 30001
	      ELECTION_CLUSTER_NAME: todo-operators
	      ELECTION_CLUSTER_SIZE: 1
	      OPERATOR_MAX_WORKERS: 1
	      OPERATOR_RECONCILE_WORKERS_INTERVAL: 10s
	      OPERATOR_MAINTENANCE_INTERVAL: 1m
	      OPERATOR_PURGE_STATE_STORE_BEFORE: 5m
	      OPERATOR_STATE_STORE_TYPE: jetstream_kv
	      MESSAGE_DURABILITY: true
	      ENTITY_OF_INTEREST_MESSAGE_QUEUE: todo-entities-78787
	      ENTITY_OF_INTEREST_MESSAGE_STREAM: dataos-todo-entities
	      ENTITY_OF_INTEREST_MESSAGE_COMMAND_SUBJECT: todo.todo
	      ENTITY_OF_INTEREST_MESSAGE_QUERY_SUBJECT: todo.query
	      ENTITY_OF_INTEREST_MESSAGE_QUERY_REPLY_SUBJECT: dataos.operator.todo.reply
	      TODO_SERVICE_SECRET: 889292929201929jksddjskd
	      TODO_SERVICE_URL: https://3dc0-150-129-144-242.ngrok-free.app/
			secrets:
				- name: risa # mandatory
					workspace: random # mandatory
					key: rex
					keys:
						- alpha
						- rex
					allKeys: false
					consumptionType: leo    
	    ports:
		    - name: metrics # mandatory
		      servicePort: 30001 # mandatory
		      targetPort: 30001 # mandatory
  resources: # mandatory
	  - name: todo # mandatory
			nameJqFilter: abcd
	    isRunnable: false # mandatory
	    specSchema:
	      jsonSchema: |
	        {
	          "$schema": "https://json-schema.org/draft/2020-12/schema",
	          "$id": "https://dataos.io/v1.0/todo-factory/todo",
	          "title": "todo",
	          "type": "object",
	          "properties": {
	            "title": {
	              "type": "string"
	            },
	            "uuid": {
	              "type": "string"
	            },
	            "description": {
	              "type": "string"
	            },
	            "status": {
	              "type": "string"
	            },
	            "done": {
	              "type": "boolean"
	            }
	          },
	          "required": [
	            "title",
	            "uuid"
	          ],
	          "additionalProperties": false
	        } # mandatory
	    natsApi:
	      command: # mandatory
	        stream: dataos-todo-entities # mandatory
	        subject: todo.todo # mandatory
	      query: # mandatory
	        subject: todo.query # mandatory
	        replySubject: dataos.operator.todo.reply # mandatory
  enabledWorkspaces: # mandatory
	  - public
	  - sandbox
  natsClusterConfig: # mandatory
    name: todo-nats # mandatory
    compute: runnable-default # mandatory
    runAsUser: amrosebirani
    runAsApiKey: abcdefghijklmnopqrstuvwxyz # mandatory
```

## Configuration Attributes

### **`operator`**

**Description:** Mapping for the attributes of Operator

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | mandatory | none | none |

**Example Usage:**

```yaml
operator:
	{} # Operator-specific attributes
```

---

### **`components`**

**Description:** mapping for the attributes of components

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of mappings | mandatory | none | none |

**Example Usage:** 

```yaml
components:
	{} # Components-specific attributes
```

---

### **`name`**

**Description:** component name

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | none |

**Example Usage:** 

```yaml
name: todo-reconciler
```

---

### **`type`**

**Description:** type of long-running runnable-Resource

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | service/worker |

**Example Usage:** 

```yaml
type: worker
```

---

### **`compute`**

**Description:** Specifies the Compute Resource name

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | runnable-default or any other custom Compute Resource name |

**Example Usage:** 

```yaml
compute: runnable-default
```

---

### **`runAsApiKey`**

**Description:** DataOS Apikey specification

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | Apikey of User | valid DataOS Apikey |

**Example Usage:** 

```yaml
runAsApiKey: abcdefghijklmnopqrstuvwxyz
```

---

### **`runAsUser`**

**Description:** user-id of Use Case assignee

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | user-id of Use Case Assignee |

**Example Usage:** 

```yaml
registry: docker.io
```

---

### **`image`**

**Description:** specifies the image name

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | any valid image name  |

**Example Usage:** 

```yaml
image: random
```

---

### **`imagePullSecret`**

**Description:** specifies the Secret Resource for pulling images from a private container registry

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | valid Secret Resource for pulling image from Private Container Registry |

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

### **`replicas`**

**Description:** specifies the number of replicas

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| integer | mandatory | none | any integer |

**Example Usage:** 

```yaml
replicas: 2
```

---

### **`environmentVars`**

**Description:** environment variables. These environment variables vary from Operator to Operator. Some of these are for NATS configuration while other are specific to the Operator.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | optional | none | list of available environment variables given here |

**Example Usage:**

```yaml
environmentVars:
  LOG_LEVEL: info
  METRIC_PORT: 30001
  ELECTION_CLUSTER_NAME: todo-operators
  ELECTION_CLUSTER_SIZE: 1
  OPERATOR_MAX_WORKERS: 1
  OPERATOR_RECONCILE_WORKERS_INTERVAL: 10s
  OPERATOR_MAINTENANCE_INTERVAL: 1m
  OPERATOR_PURGE_STATE_STORE_BEFORE: 5m
  OPERATOR_STATE_STORE_TYPE: jetstream_kv
  MESSAGE_DURABILITY: true
  ENTITY_OF_INTEREST_MESSAGE_QUEUE: todo-entities-78787
  ENTITY_OF_INTEREST_MESSAGE_STREAM: dataos-todo-entities
  ENTITY_OF_INTEREST_MESSAGE_COMMAND_SUBJECT: todo.todo
  ENTITY_OF_INTEREST_MESSAGE_QUERY_SUBJECT: todo.query
  ENTITY_OF_INTEREST_MESSAGE_QUERY_REPLY_SUBJECT: dataos.operator.todo.reply
  TODO_SERVICE_SECRET: 889292929201929jksddjskd
  TODO_SERVICE_URL: https://3dc0-150-129-144-242.ngrok-free.app/
```

| Name | Value |
| --- | --- |
| DEPOT_SERVICE_URL | https://profound-wallaby.dataos.app/ds |
| GATEWAY_URL | https://profound-wallaby.dataos.app/gateway |
| HEIMDALL_URL | https://profound-wallaby.dataos.app/heimdall |
| HERA_URL | https://profound-wallaby.dataos.app/hera/api |
| SCS_SERVICE_URL | http://stack-exec-context-sink.poros.svc.cluster.local:39100/sink |
| METIS_URL | https://profound-wallaby.dataos.app/metis2 |
| PULSAR_SERVICE_URL | pulsar+ssl://tcp.profound-wallaby.dataos.app:6651 |
| MINERVA_JDBC_URL | jdbc:trino://tcp.profound-wallaby.dataos.app:7432 |
|  |  |
| DATAOS_NAME |  sanity-read-azure-nabeel-05 |
| DATAOS_RESOURCE_ID | workflow:v1:sanity-read-azure-nabeel-05:public |
| DATAOS_RUN_ID | cvi31p4sagw0 |
| DATAOS_TYPE | workflow |
| DATAOS_WORKSPACE | public |
| DATAOS_FQDN | profound-wallaby.dataos.app |
|  |  |
| DATAOS_TAGS | sanity,tags |
| DATAOS_DESCRIPTION | The purpose of this job is to verify if we are able to read different file formats from azure abfss or not. |
|  |  |
| DATAOS_CONFIG_DIR | /etc/dataos/config |
| DATAOS_TEMP_DIR | /var/dataos/temp_data |
| DATAOS_SECRET_DIR | /etc/dataos/secret |
| RUNNABLE_ARTIFACT_DIR | /etc/dataos/work |
|  |  |
| RUNNABLE_TYPE | workflow |
| DATAOS_RUN_AS_APIKEY | dG9rZW5fZ2VbGx5X3llYXJseVsds9ubdsd3ZlbF9taXRlLjRjOGY0MGIyLTFjYzktNDVmMy05ZmMzLWY2N2RlOTdlNmEzYw== |
| DATAOS_RUN_AS_USER | mohammadnabeelqureshi |
| DATAOS_STAMP | -boo1 |
| DATAOS_UID | 15d4b6bb-2aaa-45b3-8a57-2e302cff06fb |
| HERA_SSL | false |
| LOG_LEVEL | INFO |
| DATAOS_LOG_LEVEL | INFO |
| METIS_AUTH_PROVIDER | dataos-apikey |
| MINERVA_TCP_HOST | tcp.profound-wallaby.dataos.app |
| MINERVA_TCP_PORT | 7432 |
| SSL_KEYSTORE_PASSWORD | <password> |
| SSL_TRUSTSTORE_PASSWORD | <password> |
| DATAOS_IS_DRY_RUN | false |

---

### **`secrets`**

**Description:** list of mappings for referencing Secret Resource 

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of mappings | optional | none | none |

**Example Usage:** 

```yaml
secrets:
	{}
```

---

### **`name`**

**Description:** secret name

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | valid secret name |

**Example Usage:**

```yaml
name: mysecret
```

---

### **`workspace`**

**Description:** workspace name

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | none |

**Example Usage:**

```yaml
name: newport
```

---

### **`servicePort`**

**Description:** service port declaration

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| integer | optional | none | none |

**Example Usage:**

```yaml
servicePort: 9876
```

---

### **`resources`**

**Description:** target port declaration

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| integer | optional | none | none |

**Example Usage:**

```yaml
targetPort: 7698
```

---

### **`name`**

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

### **`nameJqFilter`**

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

### **`isRunnable`**

**Description:** specifies Workflow Resource’s Job config for a Stack

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | mandatory | none | none |

**Example Usage:** 

```yaml
workflowJobConfig: {}
```

---

### **`specSchema`**

**Description:** defines the resource’s specification schema

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

### **`jsonSchema`**

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

### **`natsApi`**

**Description:** defines the NATS Cluster configuration for use for interaction from Poros

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | mandatory | none | none |

**Example Usage:** 

```yaml
resourceTemplateConfig:
  resourceTemplate: {}
```

---

### **`command`**

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

### **`stream`**

**Description:** specifies success condition

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | none |

**Example Usage:** 

```yaml
successCondition: status.jobStatus.state == COMPLETED
```

---

### **`subject`**

**Description:** specifies failure condition

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | none |

**Example Usage:** 

```yaml
failureCondition: status.applicationState.state == FAILED
```

---

### **`query`**

**Description:** specifies Service Resource’s Job config for a Stack

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | mandatory | none | none |

**Example Usage:** 

```yaml
workerConfig: {}
```

---

### **`subject`**

**Description:** specifies Resource Template

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | none |

**Example Usage:** 

```yaml
resourceTemplate: {}
```

---

### **`replySubject`**

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

### **`enabledWorkspaces`**

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

### **`replySubject`**

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

### **`enabledWorkspaces`**

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

### **`natsClusterConfig`**

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

### **`name`**

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

### **`compute`**

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

### **`runAsUser`**

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

### **`runAsApiKey`**

**Description:** describes how secrets are projected for this Stack

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | mandatory | none | none |

**Example Usage:** 

```yaml
secretProjection:
  type: propFile
```