# Setting Up Nilus

The Nilus stack in DataOS is designed for developers and enables data movement from a source to a destination without requiring complex code. It provides built-in connectors for commonly used data sources, along with the ability to add custom sources and destinations for batch data movement.

## Prerequisites

Deployment of the Nilus Server requires appropriate access permissions. These permissions must be granted either through predefined use cases or by assigning the `operator` tag. Only users with the `operator` role are authorized to deploy Nilus Server.

> **Note:** Permission requirements may vary across organizations, depending on role configurations and access policies defined within each DataOS environment.

**Verifying User Permissions**

To verify whether the required access permissions or `operator` tag are present, execute the following command:

```bash
dataos-ctl user get

# Expected Output:

dataos-ctl user get                
INFO[0000] 😃 user get...                                
INFO[0000] 😃 user get...complete                        

      NAME     │     ID      │  TYPE  │        EMAIL         │              TAGS               
───────────────┼─────────────┼────────┼──────────────────────┼─────────────────────────────────
      Groot    │  iamgroot   │ person │   iamgroot@tmdc.io   │ roles:id:data-dev,              
               │             │        │                      │ roles:id:operator,              
               │             │        │                      │ roles:id:system-dev,            
               │             │        │                      │ roles:id:user,                  
               │             │        │                      │ users:id:iamgroot
```

In the example above, the presence of `roles:id:operator` indicates that the user is authorized to deploy the Nilus Server.

**Error on Missing Permissions**

If a deployment attempt is made without the required permissions or `operator` tag, the following error will be returned:

```bash
⚠️ Invalid Parameter - failure validating resource : could not get the secret map for the dataos address: 'dataos://nilusdb?acl=rw' err: 403 <nil>
WARN[0001] 🛠 apply...error                              
ERRO[0001] failure applying resources                   
```

!!! success "Resolution"
    If the required tags or access permissions are not assigned, contact a DataOS Administrator or Operator to request the necessary access.



## Sample Nilus Server

The Nilus Server is a FastAPI service responsible for capturing and managing pipeline metadata.
It must be deployed and running before the Nilus Stack, as the stack depends on the server’s API endpoint. The following template defines the Nilus Server service used to capture pipeline information.


??? note "Nilus Server Manifest"

    ```yaml
    name: nilus-server
    version: v1
    type: service
    tags:
      - service
      - nilus-server
    description: Nilus Server for capturing pipeline information
    workspace: system
    service:
      servicePort: 8000
      ingress:
        enabled: true
        path: /nilus/system:nilus-server
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
        image: 933570616564.dkr.ecr.us-west-2.amazonaws.com/released-images/nilus:0.1.1
        command:
          - /bin/sh
          - -c
        arguments:
          - |
            python3 /app/nilus_server/entrypoint.py run-migration \
              && exec python3 /app/nilus_server/entrypoint.py run-server
    ```

Replace all placeholder values—with the appropriate environment-specific configurations.


!!! abstract "Configuration Requirement"
    The default workspace for Nilus components is `system`. When deploying the `nilus-server` in a non-default workspace, both the `ingress.path` and the Nilus Stack YAML must be updated to reflect the correct workspace reference.
 
    **Expected Format:**
 
    ```yaml
    /nilus/${{workspace}}:nilus-server
    ```
 
    **Example:**
    For a workspace named `analytics`, the path should be:
 
    ```yaml
    /nilus/analytics:nilus-server
    ```

**Common Environment Variables in the Server**

* `NILUS_DB_DEPOT_ADDRESS`: Defines the DataOS depot location for Nilus database connections.
* `NILUS_SERVER_PORT`: Specifies the port on which the Nilus Server listens.

### **Apply the Server Manifest File**

Apply the Nilus Server by executing the command below.

```bash
dataos-ctl resource apply -f ${{file-path}} 
```


## Sample Nilus Stack

Once the Nilus Server is active, use the following template as a reference to create a Nilus Stack. This configuration utilizes the Nilus Python entry point, thereby removing the requirement for a custom wrapper script.


??? note "Nilus Stack Manifest"

    ```yaml
    name: "nilus-stack"
    version: "v1alpha"
    type: "stack"
    layer: "user"
    description: "DataOS nilus stack v1alpha version 2 with schema enforcement"
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
        tag: "0.1.1"
      command:
        - python3
      arguments:
        - /app/nilus/main.py
      environmentVars:
        DATAOS_WORK_DIR: /etc/dataos/work
        BASE_CONFIG_FILE_DIR: /etc/dataos/config
        DEBEZIUM_PROPS_PATH: /etc/dataos/debezium
        NILUS_SERVICE_URL: "http://nilus-server.system.svc.cluster.local:8000/nilus/system:nilus-server"
        NILUS_HOSTNAME_VERIFICATION_ENABLED: "false"
      stackSpecValueSchema:
        jsonSchema: |
          { "$schema": "http://json-schema.org/draft-07/schema#", "type": "object", "properties": { "source": { "type": "object", "properties": { "address": { "type": "string" }, "options": { "type": "object", "properties": { "extract-parallelism": { "type": "integer" }, "incremental-key": { "type": "string" }, "interval-end": { "type": "string" }, "interval-start": { "type": "string" }, "mask": { "type": "object" }, "max-table-nesting": { "type": "string" }, "page-size": { "type": "integer" }, "primary-key": { "type": "string" }, "source-table": { "type": "string" }, "sql-exclude-columns": { "type": "string" }, "sql-limit": { "type": "integer" }, "sql-reflection-level": { "type": "string" }, "type-hints": { "type": "object" }, "yield-limit": { "type": "integer" }, "type": { "type": "string" }, "engine": { "type": "string" } }, "additionalProperties": true } }, "required": [ "address" ] }, "sink": { "type": "object", "properties": { "address": { "type": "string" }, "options": { "type": "object", "properties": { "cluster-by": { "items": { "type": "string" }, "type": "array" }, "dest-table": { "type": "string" }, "full-refresh": { "type": "boolean" }, "incremental-strategy": { "type": "string", "enum": [ "replace", "append", "merge" ] }, "loader-file-size": { "type": "integer" }, "partition-by": { "type": "array", "items": { "type": "object", "properties": { "column": { "type": "string" }, "type": { "type": "string", "enum": [ "year", "month", "day", "hour", "bucket", "identity" ] }, "name": { "type": "string" }, "index": { "type": "integer" }, "bucket-count": { "type": "integer" } }, "required": [ "column", "type", "index", "name" ] } }, "staging-bucket": { "type": "string" } }, "additionalProperties": false } }, "required": [ "address" ] }, "repo": { "type": "object", "properties": { "url": { "type": "string" }, "syncFlags": { "type": "array", "items": { "type": "string" } }, "baseDir": { "type": "string" } }, "required": [ "url", "baseDir" ] } }, "required": [ "source", "sink" ] }
      workflowJobConfig:
        configFileTemplate: |
          config.yaml: |
          {{ toYaml .ApplicationSpec.StackSpec | indent 2 }}
        containerResourceTemplate: |
          {{- if .ApplicationSpec.StackSpec.repo }}
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

Replace all placeholder values—including image, registry, and URLs—with the appropriate environment-specific configurations.

### **Apply the Stack Manifest File**

!!! warning
    Using the `--disable-interpolation` flag is mandatory while applying Stack manifest. If the manifest file is applied without this flag, DataOS will attempt to substitute placeholders—such as values wrapped in `${{ }}`—with environment variables during runtime. This behavior can lead to unintended replacements or deployment errors. By specifying `--disable-interpolation`, you ensure the manifest is applied exactly as written, preserving all template variables and preventing misconfigurations.

Apply the Nilus Stack by executing the command below.

```bash
dataos-ctl resource apply -f ${{file-path}} --disable-interpolation
```

!!! abstract  "Configuration Requirement"
    If the `nilus-server` deployed in a non-default workspace, the `NILUS_SERVICE_URL` environment variable in the Nilus Stack must be updated to target the appropriate workspace.

    **Expected Format:**

    ```yaml
    http://nilus-server.${{WORKSPACE}}.svc.cluster.local:8000/nilus/${{WORKSPACE}}:nilus-server
    ```

    **Example:** For a workspace named `analytics`, the environment variable should be:

    ```yaml
    http://nilus-server.analytics.svc.cluster.local:8000/nilus/analytics:nilus-server
    ```


**Common Environment Variables in the Stack**

* `DATAOS_WORK_DIR` : Specifies the working directory used for runtime operations and intermediate files.

* `BASE_CONFIG_FILE_DIR` : Defines the directory containing configuration files mounted into the container.

* `DEBEZIUM_PROPS_PATH` : Indicates the location of Debezium properties used for CDC integration.

* `NILUS_SERVICE_URL` : Sets the internal service endpoint for communication with the `nilus-server`. Must follow the DataOS service URL format.

* `NILUS_HOSTNAME_VERIFICATION_ENABLED` : Controls hostname verification for internal service communication. Set to `"false"` to disable verification.


