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
### **Lifecycle and Deployment**

- On deployment, the Nilus stack initializes with a **Migration step** that creates the required database tables. This step is idempotent; tables are only created if they don't exist.
- After a successful migration, the **Nilus Server** process is started.
- Table schema updates require a code change, engineering effort, and a new Nilus stack image.

#### **Table Schemas**

**`runs_info`**

Tracks the high-level metadata and health of pipeline runs.

??? note "Schema"
    | Column Name | Data Type | Description |
    | --- | --- | --- |
    | `id` | String (PK) | Unique identifier for the entry |
    | `run_id` | String | ID of the pipeline run |
    | `dataos_resource_id` | String | Associated DataOS resource |
    | `run_as_user` | String | User initiating the run |
    | `load_id` | String | Identifier for the load cycle |
    | `source_depot` | String | Source depot name |
    | `destination_depot` | String | Destination depot name |
    | `destination_uri` | String | URI of the destination |
    | `destination_schema` | String | Schema at destination |
    | `started_at` | DateTime (TZ) | Start time of run |
    | `finished_at` | DateTime (TZ) | End time of run |
    | `duration_sec` | Numeric | Duration of the run in seconds |
    | `records_count` | JSONB | Record counts per stage |
    | `files_size_mb` | Numeric | Total file size in MB |
    | `memory_mb` | Numeric | Memory used in MB |
    | `cpu_percent` | Numeric | CPU utilization percentage |
    | `first_run` | Boolean | Flag if it's the first pipeline run |
    | `is_success` | Boolean | Run success indicator |
    | `error` | JSONB | Error details, if any |
    | `pipeline_state` | JSONB | Summary of pipeline status |

??? note "Indices"      
    | **Index Name** | **Columns** | **Purpose** |
    | --- | --- | --- |
    | `runs_info_pkey` | `id` | Primary key ensuring row-level uniqueness and fast direct access. |
    | `idx_runs_info_run_load` | `run_id`, `load_id` | Optimizes JOINs with extract/normalize/load tables based on run-load keys. |
    | `idx_runs_info_started_at_desc` | `started_at DESC` | Speeds up retrieval of latest runs |
    | `idx_runs_info_success_time` | `is_success`, `started_at DESC` | Supports operational queries filtered by run success with recent-first order. |
    | `idx_runs_info_user_time` | `run_as_user`, `started_at DESC` | Improves user-specific history views sorted by time. |
    | `idx_runs_info_resource_time` | `dataos_resource_id`, `started_at DESC` | Enables recent run tracking based on dataos_resource_id |

**`extract_info`**

Captures metadata about the extract phase.

??? note "Schema"
    | Column Name | Data Type | Description |
    | --- | --- | --- |
    | `run_id` | String | Associated pipeline run ID |
    | `load_id` | String (PK) | Unique ID for extract-load cycle |
    | `table_name` | ARRAY(String) | List of tables extracted |
    | `started_at` | DateTime (TZ) | Extract start time |
    | `finished_at` | DateTime (TZ) | Extract end time |
    | `duration_sec` | Numeric | Duration of extract step |
    | `records_count` | Integer | Number of records extracted |
    | `files_size_mb` | Numeric | Size of extracted files in MB |
    | `memory_mb` | Numeric | Memory consumed during extraction (MB) |
    | `cpu_percent` | Numeric | CPU usage percentage during extraction |
    | `state` | String | State of extract phase (e.g., completed, failed) |

??? note "Indices"    
    | **Index Name** | **Columns** | **Purpose** |
    | --- | --- | --- |
    | `extract_info_pkey` | `load_id` | Primary key to uniquely identify each extract entry. |
    | `idx_extract_info_run_load` | `run_id`, `load_id` | Supports JOINs with `runs_info` table based on composite identifiers. |
    | `idx_extract_info_run_load_started_at_desc` | `run_id`, `load_id`, `started_at DESC` | Enables optimized filtering and ordering by time for a specific run+load. |

**`normalize_info`**

Stores metadata about the normalization phase, which is destination-specific.

??? note "Schema"
    | Column Name | Data Type | Description |
    | --- | --- | --- |
    | `run_id` | String | Associated pipeline run ID |
    | `load_id` | String (PK) | Unique ID for normalization load cycle |
    | `table_name` | ARRAY(String) | List of normalized tables |
    | `started_at` | DateTime (TZ) | Normalize start time |
    | `finished_at` | DateTime (TZ) | Normalize end time |
    | `duration_sec` | Numeric | Duration of normalization phase |
    | `records_count` | Integer | Number of normalized records |
    | `files_size_mb` | Numeric | Size of normalized files in MB |
    | `memory_mb` | Numeric | Memory usage in normalization |
    | `cpu_percent` | Numeric | CPU usage during normalization |
    | `state` | String | State of normalization phase |

??? note "Indices"    
    | **Index Name** | **Columns** | **Purpose** |
    | --- | --- | --- |
    | `normalize_info_pkey` | `load_id` | Primary key to uniquely identify each normalize entry. |
    | `idx_normalize_info_run_load` | `run_id`, `load_id` | Supports efficient JOINs with `runs_info` on composite identifiers. |
    | `idx_normalize_info_run_load_started_at_desc` | `run_id`, `load_id`, `started_at DESC` | Enables optimized filtering and ordering by time for a specific run+load. |

**`load_info`**

Logs all metadata about the data load step.

??? note "Schema"
    | Column Name | Data Type | Description |
    | --- | --- | --- |
    | `run_id` | String | Associated pipeline run ID |
    | `load_id` | String (PK) | Unique ID for the load cycle |
    | `table_name` | ARRAY(String) | Tables loaded |
    | `started_at` | DateTime (TZ) | Load start time |
    | `finished_at` | DateTime (TZ) | Load end time |
    | `duration_sec` | Numeric | Duration of load phase |
    | `files_loaded` | Integer | Number of files loaded |
    | `files_size_mb` | Numeric | File size in MB |
    | `memory_mb` | Numeric | Memory used during load |
    | `cpu_percent` | Numeric | CPU used during load |
    | `schema` | JSONB | Loaded schema definition |
    | `state` | String | State of load phase |
    

??? note "Indices"    
    | **Index Name** | **Columns** | **Purpose** |
    | --- | --- | --- |
    | `load_info_pkey` | `load_id` | Primary key to uniquely identify each load entry. |
    | `idx_load_info_run_load` | `run_id`, `load_id` | Facilitates efficient JOINs with `runs_info` and lookups by run/load combo. |
    | `idx_load_info_run_load_started_at_desc` | `run_id`, `load_id`, `started_at DESC` | Enables optimized filtering and ordering by time for a specific run+load. |

#### **Observability and Monitoring**

- Metrics are pushed to Prometheus via the Pushgateway.
    
??? note "Exposed Prometheus Metrics"
    | **Metric** | **Type** | **Category** | **Description** | **Insights / Use-Cases** |
    | --- | --- | --- | --- | --- |
    | `python_gc_objects_collected_total` | counter | Garbage Collection | Number of objects collected by the Python GC, per generation. | Indicates object churn; frequent collections may signal memory pressure. |
    | `python_gc_objects_uncollectable_total` | counter | Garbage Collection | Number of objects that the GC could not collect. | Detects potential memory leaks or improper object references. |
    | `python_gc_collections_total` | counter | Garbage Collection | Total number of GC cycles executed, per generation. | Useful to monitor memory cleanup frequency over time. |
    | `process_virtual_memory_bytes` | gauge | Resource Usage | Total virtual memory used by the process. | Helps track memory allocation and detect memory bloat or leaks. |
    | `process_resident_memory_bytes` | gauge | Resource Usage | Actual physical memory (RAM) used by the process. | Critical for container resource sizing and threshold alerting. |
    | `process_start_time_seconds` | gauge | Runtime Info | UNIX timestamp for when the process started. | Useful to determine uptime and detect unexpected restarts. |
    | `process_cpu_seconds_total` | counter | Resource Usage | Total accumulated CPU time used by the process. | Tracks CPU-bound behavior and supports workload tuning. |
    | `process_open_fds` | gauge | Resource Usage | Number of open file descriptors. | Surging values may indicate resource leakage; supports alerting. |
    | `process_max_fds` | gauge | Resource Usage | Maximum number of file descriptors allowed. | Baseline for alerting on open file descriptors. |
    | `python_info` | gauge | Runtime Info | Metadata about the Python environment (version, implementation). | Useful for environment validation, debugging, and audit. |
    | `http_requests_total` | counter | HTTP Requests | Count of HTTP requests by endpoint, method, and status code. | Tracks endpoint usage, detects spikes, supports SLI/SLO monitoring. |
    | `http_requests_created` | gauge | HTTP Requests | Timestamp when a request counter was initialized. | Helps correlate uptime and metric lifecycle. |
    | `http_request_duration_seconds` | histogram | HTTP Requests | Distribution of HTTP request latencies in seconds. | Enables latency tracking, SLO alerting, and endpoint performance optimization. |
    | `http_request_duration_seconds_created` | gauge | HTTP Requests | Timestamp for when latency tracking began. | Assists in diagnosing metric setup timing relative to deploys. |
    
- Dashboards and alerting mechanisms are configured in Grafana using Prometheus metrics as the data source.
- Metrics data is persisted in PostgreSQL tables for a configurable retention period of 30, 60, or 90 days.
- All data is archived in object storage using a wide-row format for deep storage.
- API endpoints are exposed for data access and integration.
    
??? note "Observability API Endpoints"

    `{{base_url}}`: *<dataos_context_url>/nilus/<workspace>:nilus-server*

    **Example: ***https://dataos-training.dataos.app/nilus/system:nilus-server*

    *All endpoints are protected using **Bearer Authentication**.*
 

    <!-- [nilus.postman_collection.json](attachment:9584c9c1-2e37-4926-9fd5-94460e5452ac:nilus.postman_collection.json) -->

    | **Endpoint** | **Method** | **Description** |
    | --- | --- | --- |
    | `{{base_url}}/health` | **GET** | Service and DB connectivity health |
    | `{{base_url}}/metrics` | **GET** | Prometheus metrics |
    | `{{base_url}}/info` | **GET** | Server name and Nilus image version |
    | `{{base_url}}/api/v1/pipelines` | **GET** | List pipeline runs (filters: run_as_user, is_success, dataos_resource_id, started_at, started_at_gte, started_at_lte, limit, offset) |
    | `{{base_url}}/api/v1/pipelines/{resource_id}/runs` | **GET** | List runs for a specific DataOS resource (limit, offset) |
    | `{{base_url}}/api/v1/pipelines/{resource_id}/latest` | **GET** | Most recent run for a specific DataOS resource |
    | `{{base_url}}/api/v1/pipelines/stats` | **GET** | Overall pipeline stats for a time period (period) |
    | `{{base_url}}/api/v1/pipelines/{resource_id}/stats` | **GET** | Pipeline stats for a resource over a period (period) |
    | `{{base_url}}/api/v1/cdc/offset-storage` | **GET** | List CDC offset storage records (filters: offset_key, record_insert_ts_gte, record_insert_ts_lte, limit, offset) |
    | `{{base_url}}/api/v1/cdc/schema-history` | **GET** | List CDC schema history (filters: id, record_insert_ts_gte, record_insert_ts_lte, limit, offset) |
    | `{{base_url}}/api/v1/cdc/offset-keys` | **GET** | Debug list of all CDC offset keys |


**Additional Notes**

- Each pipeline run consists of one or more extract-normalize-load cycles.
    
    - Change Data Capture (CDC) pipelines involve multiple cycles.

    - Batch pipelines involve a single cycle.

- The `load_id` value uniquely identifies each cycle.
- The `alembic_version` table is required and must retain its original name.


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


