# Stack orchestrated by a Workflow declared using a Resource Template


```yaml

name: "flare-sdk-v1"
version: v1alpha
type: stack
layer: user
description: "dataos flare stack alpha version 01"
stack:
  name: flare-sdk
  version: "1.0"
  flavor: java
  reconciler: stackManager
  stackSpecValueSchema:
    jsonSchema: |
      {"$schema":"http://json-schema.org/draft-07/schema#","$id":"https://dataos.io/v1.0/sparkapplication","type":"object","properties":{"driver":{"type":"object","properties":{"coreLimit":{"type":"string"},"cores":{"type":"integer"},"memory":{"type":"string"}},"required":["coreLimit","cores","memory"]},"executor":{"type":"object","properties":{"coreLimit":{"type":"string"},"cores":{"type":"integer"},"instances":{"type":"integer"},"memory":{"type":"string"}},"required":["coreLimit","cores","instances","memory"]},"sparkConf":{"type":"object","additionalProperties":{"type":"string"}},"jarFile":{"type":"string"},"mainClass":{"type":"string"},"image":{"type":"string"},"inputs":{"type":"array","items":{"type":"string"}},"outputs":{"type":"array","items":{"type":"string"}}},"required":["driver","executor","jarFile","mainClass","image","inputs","outputs"]}
  workflowJobConfig:
    resourceTemplateConfig:
      successCondition: "status.jobStatus.state == FINISHED,status.lifecycleState == STABLE"
      failureCondition: "status.jobManagerDeploymentStatus == ERROR"
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
              value: "https://{{DataOsFqdn}}/ds"
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
              value: "https://{{DataOsFqdn}}/ds"
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
  dataOsAddressJqFilters:
    - .inputs[]
    - .outputs[]
  secretProjection:
    type: "propFile"

```