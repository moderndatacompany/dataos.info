# How to cache the dataset using Flash?
In this section, we'll guide you to cache the data using Flash Service.


## Pre-requisites

Ensure the Flash Stack exists in the DataOS environment by executing the following command:
    
```bash
dataos-ctl develop stack versions
```
    
Make sure you have the appropriate access permission use case to execute the above command.
    
**Expected Output:**
  
```bash
➜  ~ dataos-ctl develop stack versions                  

        STACK      │ FLAVOR  │ VERSION │                       IMAGE                       │     IMAGE PULL SECRET      
──────────────────┼─────────┼─────────┼───────────────────────────────────────────────────┼────────────────────────────
  beacon          │ rest    │ 1.0     │ docker.io/postgrest/postgrest:v7.0.1              │ dataos-container-registry  
  benthos         │         │ 3.0     │ docker.io/rubiklabs/benthos-ds:0.8.28             │ dataos-container-registry  
  container       │         │ 1.0     │                                                   │                            
  dataos-ctl      │         │ 1.0     │ docker.io/rubiklabs/dataos-ctl:2.25.2-dev         │ dataos-container-registry  
  dataos-ctl      │         │ 2.0     │ docker.io/rubiklabs/dataos-ctl:2.24.7             │ dataos-container-registry  
  fastfun         │ alpha   │ 1.0     │ docker.io/rubiklabs/fastbase-functions:2.10.2-d2  │ dataos-container-registry  
  flare           │         │ 4.0     │ docker.io/rubiklabs/flare4:7.2.42                 │ dataos-container-registry  
  flare           │         │ 5.0     │ docker.io/rubiklabs/flare5:7.3.15                 │ dataos-container-registry  
  flash           │ python  │ 1.0     │ docker.io/rubiklabs/flash:0.0.9-dev               │ dataos-container-registry 
  scanner         │         │ 1.0     │ docker.io/rubiklabs/dataos-scanner:0.1.28         │ dataos-container-registry  
  scanner         │         │ 2.0     │ docker.io/rubiklabs/dataos-scanner:0.1.28         │ dataos-container-registry  
  soda            │ python  │ 1.0     │ docker.io/rubiklabs/dataos-soda:0.0.17            │ dataos-container-registry  
  stream-monitor  │         │ 1.0     │ docker.io/rubiklabs/monitor-api:0.13.13           │ dataos-container-registry               
  talos           │         │ 2.0     │ docker.io/rubiklabs/talos:0.1.8                   │ dataos-container-registry  
  toolbox         │         │ 1.0     │ docker.io/rubiklabs/dataos-tool:0.3.9             │ dataos-container-registry  
```
        
    
If the Flash Stack is available in the list above, proceed to the [next step](/resources/stacks/flash/flash_service/#create-a-flash-service-manifest-file). If it is not listed, deploy a new Stack by applying the below Stack manifest using the DataOS CLI.
    
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
    - .datasets[].address
  secretProjection:
    type: "propFile"
  image:
    registry: docker.io
    repository: rubiklabs
    image: flash
    tag: 0.0.9
    auth:
      imagePullSecret: dataos-container-registry
  environmentVars:
    CONFIG_FILE_PATH: /etc/dataos/config/serviceconfig.yaml
    INIT_SQLS: "set azure_transport_option_type = 'curl'"
    OFFICIAL_DUCKDB_EXTENSIONS: httpfs,aws,azure,iceberg
    PG_HOST: 0.0.0.0
    PG_PORT: 5433
    FLASH_DB_FILE_PATH: /var/dataos/temp_data/duckdb/main.duckdb
#    FLASH_DB_TEMP_FILE_PATH: /var/dataos/temp_data/tmp
  command:
    - python
  arguments:
    - -m
    - buenavista.examples.duckdb_postgres
  stackSpecValueSchema:
    jsonSchema: |
      { "$schema": "http://json-schema.org/draft-04/schema#", "type": "object", "properties": { "datasets": { "type": "array", "items": { "type": "object", "properties": { "address": { "type": "string" }, "name": { "type": "string" } }, "required": [ "address", "name" ] } }, "init": { "type": "array", "items": { "type": "string" } }, "schedule": { "type": "array", "items": { "type": "object", "properties": { "expression": { "type": "string" }, "sql": { "type": "string" } }, "required": [ "sql", "expression" ] } } }, "required": [ "datasets" ] }
  serviceConfig:
    configFileTemplate: |
      serviceconfig.yaml: |
      {{ toYaml .ApplicationSpec.StackSpec | indent 2 }}
```
    
**Apply the Flash Stack manifest file**
    
To deploy the Stack, execute the following command on the DataOS CLI.

```bash
dataos-ctl resource apply -f ${flash-stack-manifest-path} --disable-interpolation
```

Alternatively, you can also use:

```bash
dataos-ctl apply -f ${flash-stack-manifest-path} --disable-interpolation
```

**Validate Stack creation**

To check whether the Stack is successfully created, execute the following command:

```bash
dataos-ctl resource get -t stack
```

Alternatively, you can also check the stacks created by all users in the organization:

```bash
dataos-ctl resource get -t stack -a
```
    

## Create a Flash Service manifest file

Once you have the Flash Stack, follow the below steps to create the Flash Service:

1. Identify the datasets you want to cache in Flash. Flash supports BigQuery, Snowflake, Redshift, and Iceberg types of Depots.

2. Create a Flash Service manifest file specifying the datasets to be cached, the schedule, and initialization. A sample is provided below:
    
    ```yaml
    name: ${{flash-test}}
    version: v1
    type: service
    tags:
      - ${{service}}
    description: ${{flash service}}
    workspace: ${{public}}
    service:
      servicePort: ${{8080}}
      servicePorts:
      - name: ${{backup}}
        servicePort: ${{5433}}
      ingress:
        enabled: ${{true}}
        stripPath: ${{false}}
        path: ${{/flash/public:flash-test-6}}
        noAuthentication: ${{true}}
      replicas: ${{1}}
      logLevel: ${{info}}
      compute: ${{runnable-default}}
      envs:
        APP_BASE_PATH: ${{'dataos-basepath'}}
        FLASH_BASE_PATH: ${{/flash/public:flash-test-6}}
      resources:
        requests:
          cpu: ${{500m}}
          memory: ${{512Mi}}
        limits:
          cpu: ${{1000m}}
          memory: ${{1024Mi}}
      stack: flash+python:2.0
      stackSpec:
        datasets:
          - name: ${{records}}
            address: ${dataos://icebase:flash/records}}

          - name: ${{f_sales}}
            depot: ${{dataos://bigquery}}
            sql: ${{SELECT * FROM sales_360.f_sales}}
            meta:
              bucket: ${{tmdcdemogcs}}
            refresh:
              expression: ${{"*/2 * * * *"}}
              sql: ${{SELECT MAX(invoice_dt_sk) FROM sales_360.f_sales}}
              where: ${{invoice_dt_sk > PREVIOUS_SQL_RUN_VALUE}}
    
          - name: ${{duplicate_sales}}
            depot: ${{dataos://bigquery}}
           sql: ${{SELECT * FROM sales_360.f_sales}}
            meta:
              bucket: ${{tmdcdemogcs}}
            refresh:
              expression: ${{"*/4 * * * *"}}
              sql: ${{SELECT MAX(invoice_dt_sk) FROM sales_360.f_sales}}
              where: ${{invoice_dt_sk > CURRENT_SQL_RUN_VALUE}}


        init:
          - ${{create table f_sales as (select * from records)}}

        schedule:
          - expression: ${{"*/2 * * * *"}}
            sql: ${{INSERT INTO f_sales BY NAME (select * from records);}}
    ```
    
    The following table provides the details of attributes to be declared in the Flash Stack-specific section:
    
    | **Attribute** | **Description** | **Data Type** | **Possible Value** | **Requirement** |
    | --- | --- | --- | --- | --- |
    | `datasets` | The datasets section is a list of mapping each specifying the name and address of the specific dataset. | list of mapping | none | mandatory |
    | `address`  | UDL address of the dataset to be cached in Flash | string | valid DataOS UDL address | mandatory |
    | `name`  | Name of the dataset to be cached | string | alphanumeric values with the RegEx `[a-z0-9]([-a-z0-9]*[a-z0-9])`; ``a hyphen/dash is allowed as a special character | mandatory |
    | `init` | List of PostgreSQL statements for initialization | list of strings | valid PostgreSQL statements. You can create either tables or views | mandatory |
    | `schedule` | List of mappings specifying the schedule expression and SQL query | list of mapping | none | optional |
    | `expression` | Valid cron expression for the schedule | string | valid cron expression | mandatory |
    | `sql` | SQL statement for refreshing | string | valid PostgreSQL statement | mandatory |
    
    To know more about each attribute, please [refer to this](/resources/stacks/flash/configurations/).

## Apply the Flash Service

Run the Service and load those datasets into the Flash layer by applying the manifest file using DataOS CLI. Use the following command for execution:

```yaml
dataos-ctl resource apply -f ${flash-service-manifest-file-path} -w ${workspace}
```

Alternatively, you can also use

```yaml
dataos-ctl apply -f ${flash-service-manifest-file-path} -w ${workspace}
```

**Example Usage:**

```yaml
dataos-ctl resource apply -f ./flash/service_manifest.yaml -w curriculum
```

Expected Output:

```bash
INFO[0000] 🛠 apply...                                   
INFO[0000] 🔧 applying(public) flash-service-test:v1:service... 
INFO[0008] 🔧 applying(public) flash-service-test:v1:service...created 
INFO[0008] 🛠 apply...complete
```

## [What is Next?](/resources/stacks/flash/#recipes)
