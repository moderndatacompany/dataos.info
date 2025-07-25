# How to cache a dataset using Flash?

This section provides guidance for caching datasets using the Flash Service in DataOS.

## Prerequisites

Ensure that the Flash Stack is available in the DataOS environment by executing the following command:

```bash
dataos-ctl develop stack versions
```

Ensure that appropriate access permissions are available to execute this command.

**Expected output:**

```bash
➜  ~ dataos-ctl develop stack versions                  

       STACK      │ FLAVOR  │ VERSION │                       IMAGE                       │     IMAGE PULL SECRET      
──────────────────┼─────────┼─────────┼───────────────────────────────────────────────────┼────────────────────────────
  beacon          │ graphql │ 1.0     │ docker.io/rubiklabs/beacon:postgraphile-4.10.0.d1 │ dataos-container-registry  
  beacon          │ rest    │ 1.0     │ docker.io/postgrest/postgrest:v7.0.1              │ dataos-container-registry  
  bento         │         │ 3.0     │ docker.io/rubiklabs/bento-ds:0.8.28             │ dataos-container-registry  
  container       │         │ 1.0     │                                                   │                            
  dataos-ctl      │         │ 1.0     │ docker.io/rubiklabs/dataos-ctl:2.26.18            │ dataos-container-registry  
  dataos-resource │ apply   │ 1.0     │ docker.io/rubiklabs/dataos-ctl:2.26.18            │ dataos-container-registry  
  dataos-resource │ delete  │ 1.0     │ docker.io/rubiklabs/dataos-ctl:2.26.18            │ dataos-container-registry  
  dataos-resource │ run     │ 1.0     │ docker.io/rubiklabs/dataos-ctl:2.26.18            │ dataos-container-registry  
  fastfun         │ alpha   │ 1.0     │ docker.io/rubiklabs/fastbase-functions:2.10.2-d2  │ dataos-container-registry  
  flare           │         │ 5.0     │ docker.io/rubiklabs/flare5:7.3.17                 │ dataos-container-registry  
  flare           │         │ 6.0     │ docker.io/rubiklabs/flare6:8.0.9                  │ dataos-container-registry  
  flash           │ python  │ 1.0     │ docker.io/rubiklabs/flash:0.0.36                   │ dataos-container-registry  
  flash           │ python  │ 2.0     │ docker.io/rubiklabs/flash:0.0.37-dev              │ dataos-container-registry  
  lakesearch      │         │ 1.0     │ docker.io/rubiklabs/lakesearch:0.1.11             │ dataos-container-registry  
  scanner         │         │ 1.0     │ docker.io/rubiklabs/dataos-scanner:0.1.28         │ dataos-container-registry  
  scanner         │         │ 2.0     │ docker.io/rubiklabs/dataos-scanner:0.1.28         │ dataos-container-registry  
  soda            │ python  │ 1.0     │ docker.io/rubiklabs/dataos-soda:0.0.19.3          │ dataos-container-registry  
  stream-monitor  │         │ 1.0     │ docker.io/rubiklabs/monitor-api:0.13.13           │ dataos-container-registry  
  talos           │         │ 2.0     │ docker.io/rubiklabs/talos:0.1.22                  │ dataos-container-registry  
```

If the Flash Stack is listed, proceed to the [next step](/resources/stacks/flash/flash_service/#create-a-flash-service-manifest-file). If not, deploy a new Stack using the following manifest and the DataOS CLI:

```yaml
name: "flash-v1"
version: v1alpha
type: stack
layer: user
description: "flash stack version 1"
stack:
  name: flash
  version: "1.0"
  flavor: "python"
  reconciler: "stackManager"
  dataOsAddressJqFilters:
    - .datasets[] | select(type == "object") | [.address, .depot] | map(select(. != null)) | .[]
  secretProjection:
    type: "propFile"
  image:
    registry: docker.io
    repository: rubiklabs
    image: flash
    tag: 0.0.44
    auth:
      imagePullSecret: dataos-container-registry
  environmentVars:
    DUCKDB_EXTENSIONS_PATH: /src/extensions
    CONFIG_FILE_PATH: /etc/dataos/config/serviceconfig.yaml
    FLASH_DB_FILE_PATH: /var/dataos/temp_data/duckdb/main.duckdb
    PROMETHEUS_URL: http://thanos-query-frontend.sentinel.svc.cluster.local:9090
    DEV_MODE: 'true'
  command:
    - python
  arguments:
    - -m
    - flash.main.duckdb_postgres
  stackSpecValueSchema:
    jsonSchema: |
      { "$schema": "http://json-schema.org/draft-04/schema#", "type": "object", "properties": { "datasets": { "type": "array", "items": { "type": "object", "properties": { "name": { "type": "string" }, "address": { "type": "string" }, "depot": { "type": "string" }, "meta": { "type": "object", "additionalProperties": true }, "sql": { "type": "string" }, "refresh": { "type": "object", "properties": { "expression": { "type": "string" }, "sql": { "type": "string" }, "where": { "type": "string" } }, "required": [ "expression" ] } }, "required": [ "name" ] } }, "init": { "type": "array", "items": { "type": "string" } }, "schedule": { "type": "array", "items": { "type": "object", "properties": { "expression": { "type": "string" }, "sql": { "type": "string" } }, "required": [ "expression", "sql" ] } } } }
  serviceConfig:
    configFileTemplate: |
      serviceconfig.yaml: |
      {{ toYaml .ApplicationSpec.StackSpec | indent 2 }}
```

**Apply the Flash Stack manifest file:**

To deploy the Stack, run the following command:

```bash
dataos-ctl resource apply -f ${flash-stack-manifest-path} --disable-interpolation
```

Alternatively, use:

```bash
dataos-ctl apply -f ${flash-stack-manifest-path} --disable-interpolation
```

**Validate Stack creation:**

Check if the Stack is created successfully:

```bash
dataos-ctl resource get -t stack
```

To view Stacks created by all users in the organization:

```bash
dataos-ctl resource get -t stack -a
```

## Create a Flash Service manifest file

Once the Flash Stack is available, follow these steps to create a Flash Service:

1. Identify the datasets to be cached in Flash. Flash supports BigQuery, Snowflake, Redshift, and Iceberg types of Depots.
2. Create a Flash Service manifest file that specifies the datasets to be cached, the schedule, and initialization. A sample is provided below:

    ```yaml
    name: flash-test
    version: v1
    type: service
    tags:
      - service
    description: flash service
    workspace: public
    service:
      servicePort: 8080
      servicePorts:
      - name: backup
        servicePort: 5433
      ingress:
        enabled: true
        stripPath: false
        path: /flash/public:flash-test-6
        noAuthentication: true
      replicas: 1
      logLevel: info
      compute: runnable-default
      envs:
        APP_BASE_PATH: 'dataos-basepath'
        FLASH_BASE_PATH: /flash/public:flash-test-6
      resources:
        requests:
          cpu: 500m
          memory: 512Mi
        limits:
          cpu: 1000m
          memory: 1024Mi
      stack: flash+python:1.0
      stackSpec:
        datasets:
          - name: records
            address: dataos://icebase:flash/records

          - name: f_sales
            depot: dataos://bigquery
            sql: SELECT * FROM sales_360.f_sales
            meta:
              bucket: tmdcdemogcs
            refresh:
              expression: "*/2 * * * *"
              sql: SELECT MAX(invoice_dt_sk) FROM sales_360.f_sales
              where: invoice_dt_sk > PREVIOUS_SQL_RUN_VALUE
    
          - name: duplicate_sales
            depot: dataos://bigquery
            sql: SELECT * FROM sales_360.f_sales
            meta:
              bucket: tmdcdemogcs
            refresh:
              expression: "*/4 * * * *"
              sql: SELECT MAX(invoice_dt_sk) FROM sales_360.f_sales
              where: invoice_dt_sk > CURRENT_SQL_RUN_VALUE

        init:
          - create table f_sales as (select * from records)

        schedule:
          - expression: "*/2 * * * *"
            sql: INSERT INTO f_sales BY NAME (select * from records);
    ```

    Below is a description of key attributes in the Flash Stack-specific section:

    | **Attribute** | **Description** | **Data Type** | **Requirement** |
    | ------------- | ----------------| --------------| ----------------|
    | `datasets`    | List of mappings specifying the name and address of datasets to be cached. | List of mapping | Mandatory |
    | `address`     | UDL address of the dataset to be cached in Flash. | String | Mandatory |
    | `name`        | Name of the dataset to be cached. | String | Mandatory |
    | `init`        | List of PostgreSQL statements for initialization. | List of strings | Mandatory |
    | `schedule`    | List of mappings for schedule expressions and SQL queries. | List of mapping | Optional |
    | `expression`  | Cron expression for scheduling. | String | Mandatory |
    | `sql`         | SQL statement for refreshing data. | String | Mandatory |

    For more information on each attribute, refer to [this section](/resources/stacks/flash/configurations/).

## Apply the Flash Service

To run the Service and load the datasets into the Flash layer, apply the manifest file using the DataOS CLI:

```bash
dataos-ctl resource apply -f ${flash-service-manifest-file-path} -w ${workspace}
```

Alternatively, use:

```bash
dataos-ctl apply -f ${flash-service-manifest-file-path} -w ${workspace}
```

**Example usage:**

```bash
dataos-ctl resource apply -f ./flash/service_manifest.yaml -w curriculum
```

**Expected output:**

```bash
INFO[0000] 🛠 apply...                                   
INFO[0000] 🔧 applying(public) flash-service-test:v1:service... 
INFO[0008] 🔧 applying(public) flash-service-test:v1:service...created 
INFO[0008] 🛠 apply...complete
```

## Next steps


- [Monitor the cached dataset](/resources/stacks/flash/recipes/monitor/)

- [Use cached datasets in Lens models](/resources/stacks/flash/recipes/lens/)

- [Consume cached datasets via Talos](/resources/stacks/flash/recipes/talos/)

- [Best Practices for Flash](/resources/stacks/flash/best_practices/)