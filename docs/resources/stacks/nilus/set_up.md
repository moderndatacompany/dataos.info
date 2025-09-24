# Set Up

The Nilus stack in DataOS is designed for developers and enables data movement from a source to a destination without requiring complex code. It provides built-in connectors for commonly used data sources, along with the ability to add custom sources and destinations for batch data movement.

## Prerequisites

* A running **Nilus Server** (FastAPI) with its database (**PostgreSQL**).
* Access to **Depot Service** and **Heimdall** (for secret/permission resolution in **DataOS**).
* For **Change Data Capture (CDC),** ensure that all required database prerequisites are configured. This includes enabling features such as **PostgreSQL Write-Ahead Logging (WAL), SQL Server (change table), MySQL binary logging (binlog), and supplemental logging in Oracle.**

### **Sample Nilus Stack**

Use the following template as a reference to create Nilus Stack. This configuration leverages the Nilus Python entry point, eliminating the need for a custom wrapper script.

??? note "Nilus Stack Manifest"

    ```yaml
    name: "nilus-stack"
    version: "v1alpha"
    type: "stack"
    layer: "user"
    description: "dataos nilus stack v1alpha version 1"
    stack:
      name: "nilus"
      version: "1.0"
      reconciler: "stackManager"
      dataOsAddressJqFilters:
        - .source.address
        - .sink.address
      secretProjection:
        type: "propFile"
      image:
        registry: "933570616564.dkr.ecr.us-west-2.amazonaws.com"
        repository: "released-images"
        image: "nilus"
        tag: "0.0.17"
      command:
        - python3
      arguments:
        - /app/nilus/main.py
      environmentVars:
        DATAOS_WORK_DIR: /etc/dataos/work
        BASE_CONFIG_FILE_DIR: /etc/dataos/config
        DEBEZIUM_PROPS_PATH: /etc/dataos/debezium
        NILUS_SERVICE_URL: "http://nilus-server.public.svc.cluster.local:8000/nilus/public:nilus-server"
        NILUS_HOSTNAME_VERIFICATION_ENABLED: "false"
      stackSpecValueSchema:
        jsonSchema: |
          { "$schema": "http://json-schema.org/draft-07/schema#", "type": "object", "properties": { "source": { "type": "object", "properties": { "address": { "type": "string" }, "options": { "type": "object" } }, "required": [ "address" ] }, "sink": { "type": "object", "properties": { "address": { "type": "string" }, "options": { "type": "object" } }, "required": [ "address" ] }, "repo": { "type": "object", "properties": { "url": { "type": "string" }, "syncFlags": { "type": "array", "items": { "type": "string" } }, "baseDir": { "type": "string" } }, "required": [ "url", "baseDir" ] } }, "required": [ "source", "sink" ] }
      workflowJobConfig:
        configFileTemplate: |
          config.yaml: |
          {{ toYaml .ApplicationSpec.StackSpec | indent 2 }}
        containerResourceTemplate: |
          {{- if hasKey .ApplicationSpec.StackSpec "repo" }}
          {{- $repo := .ApplicationSpec.StackSpec.repo }}
          initContainers:
            - command:
              - /git-sync
              args:
              - --repo={{ getNested $repo "url" }}
              - --one-time=true
              - --root=/etc/dataos/work
              {{- if hasKey $repo "syncFlags" }}
              {{- range $flag := getNested $repo "syncFlags" }}
              - {{ $flag }}
              {{- end }}
              {{- end }}
              image: 933570616564.dkr.ecr.us-west-2.amazonaws.com/released-images/git-sync:latest
              imagePullPolicy: IfNotPresent
              name:  "{{.Name}}{{.Stamp}}-ic"
              {{ if .ApplicationSpec.Resources -}}
              resources:
            {{toYaml .ApplicationSpec.Resources | indent 4}}
              {{- end }}
              volumeMounts:
              - mountPath: /etc/dataos/work
                name: workdir
              envFrom:
              - secretRef:
                  name: "{{.Name}}-{{.Type}}{{.Stamp}}-env"
              {{ if .EnvironmentVarsFromSecret }}
              {{- range $secName := .EnvironmentVarsFromSecret }}
              - secretRef:
                  name: "{{$secName}}"
              {{- end }}
              {{- end }}
          {{- end }}
          container:
            name: {{.Name}}{{.Stamp}}-main
            image: "{{.Image}}"
            imagePullPolicy: IfNotPresent
            command:
            - python
            args:
            - /app/nilus/main.py
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
            - mountPath: "{{.DataOsSecretMountPath}}"
              name: dataos-secret-mount
              readOnly: true
            - name: workdir
              mountPath: /etc/dataos/work
            {{ if .HasConfigConfs }}
            - name: dataos-config-mount
              mountPath: "{{.DataOsConfigMountPath}}"
              readOnly: true
            {{- end }}
            {{ if .ApplicationSpec.TempVolume -}}
            - name: {{.Name}}-{{.Type}}{{.Stamp}}-tdm
              mountPath: "{{.DataTempMountPath}}"
              subPath: {{.Name}}{{.Stamp}}
            {{- end }}
            {{ if .ApplicationSpec.PersistentVolume -}}
            - name: {{.Name}}-{{.Type}}{{.Stamp}}-pdm
              mountPath: "{{.DataPersistentMountPath}}/{{.ApplicationSpec.PersistentVolume.Directory}}"
              subPath: "{{.ApplicationSpec.PersistentVolume.Directory}}"
            {{- end }}
            {{ if .Volumes }}
            {{- range $volume := .Volumes }}
            - name: {{$volume.Name}}
              mountPath: "{{$volume.MountPath}}"
              readOnly: {{$volume.ReadOnly}}
              {{ if $volume.SubPath }}
              subPath: "{{$volume.SubPath}}"
              {{- end }}
            {{- end }}
            {{- end }}
            {{ if .ApplicationSpec.Resources -}}
            resources:
          {{toYaml .ApplicationSpec.Resources | indent 4}}
            {{- end }}
            env:
              - name: POD_NAME
                valueFrom:
                  fieldRef:
                    fieldPath: metadata.name
            {{ if .ApplicationSpec.EnvironmentVars }}
              {{- range $conf, $value := .ApplicationSpec.EnvironmentVars }}
              - name: {{$conf}}
                value: {{ $value | quote }}
              {{- end }}
            {{- end}}
      serviceConfig:
        configFileTemplate: |
          config.yaml: |
          {{ toYaml .ApplicationSpec.StackSpec | indent 2 }}
        containerResourceTemplate: |
          {{- if hasKey .ApplicationSpec.StackSpec "repo" }}
          {{- $repo := .ApplicationSpec.StackSpec.repo }}
          initContainers:
            - command:
              - /git-sync
              args:
              - --repo={{ getNested $repo "url" }}
              - --one-time=true
              - --root=/etc/dataos/work
              {{- if hasKey $repo "syncFlags" }}
              {{- range $flag := getNested $repo "syncFlags" }}
              - {{ $flag }}
              {{- end }}
              {{- end }}
              image: 933570616564.dkr.ecr.us-west-2.amazonaws.com/released-images/git-sync:latest
              imagePullPolicy: IfNotPresent
              name:  "{{.Name}}{{.Stamp}}-ic"
              {{ if .ApplicationSpec.Resources -}}
              resources:
            {{toYaml .ApplicationSpec.Resources | indent 4}}
              {{- end }}
              volumeMounts:
              - mountPath: /etc/dataos/work
                name: workdir
              envFrom:
              - secretRef:
                  name: "{{.Name}}-{{.Type}}{{.Stamp}}-env"
              {{ if .EnvironmentVarsFromSecret }}
              {{- range $secName := .EnvironmentVarsFromSecret }}
              - secretRef:
                  name: "{{$secName}}"
              {{- end }}
              {{- end }}
          {{- end }}
          container:
            name: {{.Name}}{{.Stamp}}-main
            image: "{{.Image}}"
            imagePullPolicy: IfNotPresent
            command:
            - python
            args:
            - /app/nilus/main.py
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
            - mountPath: "{{.DataOsSecretMountPath}}"
              name: dataos-secret-mount
              readOnly: true
            - name: workdir
              mountPath: /etc/dataos/work
            {{ if .HasConfigConfs }}
            - name: dataos-config-mount
              mountPath: "{{.DataOsConfigMountPath}}"
              readOnly: true
            {{- end }}
            {{ if .ApplicationSpec.TempVolume -}}
            - name: {{.Name}}-{{.Type}}{{.Stamp}}-tdm
              mountPath: "{{.DataTempMountPath}}"
              subPath: {{.Name}}{{.Stamp}}
            {{- end }}
            {{ if .ApplicationSpec.PersistentVolume -}}
            - name: {{.Name}}-{{.Type}}{{.Stamp}}-pdm
              mountPath: "{{.DataPersistentMountPath}}/{{.ApplicationSpec.PersistentVolume.Directory}}"
              subPath: "{{.ApplicationSpec.PersistentVolume.Directory}}"
            {{- end }}
            {{ if .Volumes }}
            {{- range $volume := .Volumes }}
            - name: {{$volume.Name}}
              mountPath: "{{$volume.MountPath}}"
              readOnly: {{$volume.ReadOnly}}
              {{ if $volume.SubPath }}
              subPath: "{{$volume.SubPath}}"
              {{- end }}
            {{- end }}
            {{- end }}
            {{ if .ApplicationSpec.Resources -}}
            resources:
          {{toYaml .ApplicationSpec.Resources | indent 4}}
            {{- end }}
            env:
              - name: POD_NAME
                valueFrom:
                  fieldRef:
                    fieldPath: metadata.name
            {{ if .ApplicationSpec.EnvironmentVars }}
              {{- range $conf, $value := .ApplicationSpec.EnvironmentVars }}
              - name: {{$conf}}
                value: {{ $value | quote }}
              {{- end }}
            {{- end}}
    ```

Replace all placeholder values—including image, registry, secrets, and URLs—with the appropriate environment-specific configurations.

**Common Environment Variables in the Stack**

* `DATAOS_RUN_AS_USER` **or** `DATAOS_RUN_AS_APIKEY` – identity under which the stack runs.
* `NILUS_SERVICE_URL` – URL for Nilus Server (used for pushes/reads).
* `PUSHGATEWAY_URL`, `PUSHGATEWAY_INTERVAL_SECONDS` – Prometheus push.
* `DATAOS_SECRET_DIR`, `DATAOS_WORK_DIR`, `DATAOS_TEMP_DIR` – DataOS runtime paths.
* `BASE_CONFIG_FILE_DIR` – optional base dir for config resolution.

### **Sample Nilus Server**

The following template defines the Nilus Server service used to capture pipeline information.

??? note "Nilus Server Manifest"

    ```yaml
    name: nilus-server
    version: v1
    type: service
    tags:
      - service
      - nilus-server
    description: Nilus Server for capturing pipeline information
    workspace: public
    service:
      servicePort: 8000
      ingress:
        enabled: true
        path: /nilus/public:nilus-server
        stripPath: false
        noAuthentication: false
      replicas: 1
      logLevel: INFO
      compute: runnable-default
      resources:
        requests:
          cpu: 1000m
          memory: 1000Mi
        limit:
          cpu: 2000m
          memory: 2000Mi
      stack: container
      envs:
        NILUS_DB_DEPOT_ADDRESS: dataos://nilusdb?acl=rw
        NILUS_SERVER_PORT: 8000
      stackSpec:
        image: 933570616564.dkr.ecr.us-west-2.amazonaws.com/released-images/nilus:0.0.17
        command:
          - /bin/sh
          - -c
        arguments:
          - |
            python3 /app/nilus_server/entrypoint.py run-migration \
              && exec python3 /app/nilus_server/entrypoint.py run-server
    ```

**Common Environment Variables in the Server**

* `NILUS_DB_DEPOT_ADDRESS`: Defines the DataOS depot location for Nilus database connections.
* `NILUS_SERVER_PORT`: Specifies the port on which the Nilus Server listens.