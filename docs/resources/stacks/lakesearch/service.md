---
title: Lakesearch
search:
  boost: 1
---


# How to create a Lakesearch Service?

## Pre-requisites

A user must have the following requirements met before setting up a Lakesearch Service.

- A user is required to have knowledge of Python.

- Ensure that DataOS CLI is installed and initialized in the system. If not the user can install it by referring to [this section.](https://dataos.info/interfaces/cli/installation/)
- A user must have the following tags assigned.
    
    ```bash
    dataos-ctl user get                
    INFO[0000] 😃 user get...                                
    INFO[0001] 😃 user get...complete                        
    
          NAME     │     ID      │  TYPE  │        EMAIL         │              TAGS               
    ───────────────┼─────────────┼────────┼──────────────────────┼─────────────────────────────────
        Iamgroot   │   iamgroot  │ person │  iamgroot@tmdc.io    │ roles:id:data-dev,                            
                   │             │        │                      │ roles:id:user,                  
                   │             │        │                      │ users:id:iamgroot
    ```
    
- If the above tags are not available, a user can contact a DataOS operator to assign the user with one of the following use cases using the Bifrost Governance. A DataOS operator can create new usecases as per the requirement.

    <div style="text-align: center;">
    <figure>
    <img src="/resources/stacks/lakesearch/images/usecase.png" alt="usecases" style="border:1px solid black; width: 100%; height: auto;">
    <figcaption style="margin-top: 8px; font-style: italic;">Bifrost Governance</figcaption>
    </figure>
    </div>

    
- Ensure the Lakesearch Stack is available in the DataOS Environment.

- Configure Volume Resource for storage allocation. Follow the below steps to configure a Volume Resource.

    1. Copy the template below and replace <name> with your desired Resource name and <size> with the appropriate volume size (e.g., 100Gi, 20Gi, etc.), according to your available storage capacity. Make sure the configuration is aligned with both your storage and performance requirements. For the accessMode, you can choose ReadWriteOnce (RWO) for exclusive read-write access by a single node, or ReadOnlyMany (ROX) if the volume needs to be mounted as read-only by multiple nodes.

        ```yaml
        name: <name>  # Name of the Resource
        version: v1beta  # Manifest version of the Resource
        type: volume  # Type of Resource
        tags:  # Tags for categorizing the Resource
          - volume
        description: Common attributes applicable to all DataOS Resources
        layer: user
        volume:
          size: <size>  # Example: 100Gi, 50Mi, 10Ti, 500Mi, 20Gi
          accessMode: <accessMode>  # Example: ReadWriteOnce, ReadOnlyMany
          type: temp
        ```

        <aside class="callout">
        💡The persistent volume size should be at least 2.5 times the total dataset size, rounded to the nearest multiple of 10.

        To check the dataset size, use the following query:

        ```sql
        SELECT sum(total_size) FROM "<catalog>"."<schema>"."<table>$partitions";
        ```
        The resultant size will be in the bytes.
        </aside>

    2. Apply the Volume manifest file

        Apply the persistent volume manifest file, using the following command in terminal:

        ```
        dataos-ctl apply -f <file path of persistent volume>
        ```
        This will deploy the Persistent Volume Resource, making it available for use by Lakesearch Service.

## Configure Lakesearch Service

<aside class="callout">

🗣️ This section utilizes the city table stored in the DataOS Lakehouse as an example.

</aside>

### **1. Create a Lakesearch Service manifest file**

Create a manifest file for Lakesearch Service. The below given manifest file of Lakesearch Service creates a simple indexer for city table.

<details>
  <summary>lakesearch_service.yaml</summary>
  ```yaml
  name: testingls
  version: v1
  type: service
  tags:
    - service
    - dataos:type:resource
    - dataos:resource:service
    - dataos:layer:user
  description: Lakesearch Service Simple Index Config
  workspace: public
  service:
    servicePort: 4080
    ingress:
      enabled: true
      stripPath: false
      path: /lakesearch/public:testingls
      noAuthentication: true
    replicas: 1
    logLevel: 'DEBUG'
    compute: runnable-default
    envs:
      LAKESEARCH_SERVER_NAME: "public:testingls"
      DATA_DIR: public/testingls/sample
      USER_MODULES_DIR: /etc/dataos/config
    persistentVolume:
      name: ls-v2-test-vol
      directory: public/testingls/sample
    resources:
      requests:
        cpu: 1000m
        memory: 1536Mi
    stack: lakesearch:6.0
    stackSpec:
      lakesearch:
        source:
          datasets:
            - name: city
              dataset: dataos://icebase:retail/city
              options:
                region: ap-south-1
        index_tables:
          - name: city
            description: "index for cities"
            tags:
              - cities
            properties:
              morphology: stem_en
            columns:
              - name: city_id
                type: keyword
              - name: zip_code
                type: bigint  
              - name: id
                description: "mapped to row_num"
                tags:
                  - identifier
                type: bigint
              - name: city_name
                type: keyword
              - name: county_name
                type: keyword
              - name: state_code
                type: keyword
              - name: state_name
                type: text
              - name: version
                type: text
              - name: ts_city
                type: timestamp
        indexers:
          - index_table: city
            base_sql: |
              SELECT 
                city_id,
                zip_code,
                zip_code as id,
                city_name,
                county_name,
                state_code,
                state_name,
                version,
                cast(ts_city as timestamp) as ts_city
              FROM 
                city
            options:
              start: 1734979551
              step: 86400
              batch_sql: |
                WITH base AS (
                    {base_sql}
                ) SELECT 
                  * 
                FROM 
                  base 
                WHERE 
                  epoch(ts_city) >= {start} AND epoch(ts_city) < {end}
              throttle:
                min: 10000
                max: 60000
                factor: 1.2
                jitter: true
  ```
    
</details>


<aside class="callout">

🗣️ If the dataset is very large, users can divide it into multiple indexes, naming each part accordingly. When accessing the endpoint, they can search by the index partition’s name. This approach helps reduce the time required to index a large dataset.

</aside>

<details>
  <summary>lakesearch_service_partitioned.yaml</summary>
  
  ```yaml
  name: ls-test-plain-part
  version: v1
  type: service
  tags:
    - service
    - dataos:type:resource
    - dataos:resource:service
    - dataos:layer:user
  description: Lakesearch Service Simple Index Config
  workspace: public
  service:
    servicePort: 4080
    ingress:
      enabled: true
      stripPath: false
      path: /lakesearch/public:ls-test-plain-part
      noAuthentication: true
    replicas: 1
    logLevel: 'DEBUG'
    compute: runnable-default
    envs:
      LAKESEARCH_SERVER_NAME: "public:ls-test-plain"
      DATA_DIR: public/ls-test-plain-part/datanew01
      USER_MODULES_DIR: /etc/dataos/config
    persistentVolume:
      name: ls-v2-test-vol
      directory: public/ls-test-plain-part/datanew01
    resources:
      requests:
        cpu: 1000m
        memory: 1536Mi
    stack: lakesearch:1.0
    stackSpec:
      lakesearch:
        source:
          datasets:
            - name: devices
              dataset: dataos://icebase:_ls_data/devices_with_d
              options:
                region: ap-south-1
        index_tables:
          - name: devices
            description: "index for devices"
            tags:
              - devices
            properties:
              morphology: stem_en
            partitions:
              - devices_before_25122024
              - devices_after_25122024
            columns:
              - name: row_num
                type: bigint
              - name: id
                description: "mapped to row_num"
                tags:
                  - identifier
                type: bigint
              - name: device_id
                type: text
              - name: org_id
                type: keyword
              - name: device_name
                type: text
              - name: serial_number
                type: bigint
              - name: model_type
                type: text
              - name: family
                type: text
              - name: category
                type: keyword
              - name: model_name
                type: text
              - name: platform
                type: keyword
              - name: manufacturer
                type: text
              - name: subscription_id
                type: text
              - name: created_at
                type: timestamp
              - name: updated_at
                type: timestamp
              - name: is_active
                type: bool
              - name: _deleted
                type: bool
        indexers:
          - index_table: devices_before_25122024
            base_sql: |
              SELECT 
                row_num,
                row_num as id,
                device_id,
                org_id,
                device_name,
                serial_number,
                model_type,
                family,
                category,
                model_name,
                platform,
                platform as platform_vec,
                manufacturer,
                subscription_id,
                cast(created_at as timestamp) as created_at,
                cast(updated_at as timestamp) as updated_at,
                is_active,
                _delete as _deleted
              FROM 
                devices
            options:
              start: 1735084800
              step: -86400
              batch_sql: |
                WITH base AS (
                    {base_sql}
                ) SELECT 
                  * 
                FROM 
                  base 
                WHERE 
                  epoch(updated_at) >= {end} AND epoch(updated_at) < {start}
              throttle:
                min: 10000
                max: 60000
                factor: 1.2
                jitter: true
  
          - index_table: devices_after_25122024
            base_sql: |
              SELECT 
                row_num,
                row_num as id,
                device_id,
                org_id,
                device_name,
                serial_number,
                model_type,
                family,
                category,
                model_name,
                platform,
                platform as platform_vec,
                manufacturer,
                subscription_id,
                cast(created_at as timestamp) as created_at,
                cast(updated_at as timestamp) as updated_at,
                is_active,
                _delete as _deleted
              FROM 
                devices
            options:
              start: 1735084800
              step: 86400
              batch_sql: |
                WITH base AS (
                  {base_sql}
                ) SELECT 
                  * 
                FROM 
                  base 
                WHERE 
                  epoch(updated_at) >= {start} AND epoch(updated_at) < {end}
              throttle:
                min: 10000
                max: 60000
                factor: 1.2
                jitter: true
  
  ```
</details>

To know more about each attribute in detail, please refer to [this link.](/resources/stacks/lakesearch/configurations/)  

    
### **2. Apply the manifest file**

Apply the manifest file by executing the below command.
    
```bash
dataos-ctl resource apply -f ${{path-to-manifest-file}}
```
    
### **3. Validate the Lakesearch Service**

Validate the Service by executing the below command.
    
```bash
dataos-ctl resource get -t service -n testingls -w public
```

Expected output:

```bash
dataos-ctl resource get -t service -n testingls -w public 
INFO[0000] 🔍 get...                                     
INFO[0000] 🔍 get...complete                             

    NAME    | VERSION |  TYPE   | WORKSPACE | STATUS |  RUNTIME  |    OWNER     
------------|---------|---------|-----------|--------|-----------|--------------
  testingls | v1      | service | public    | active | running:1 |  iamgroot  
```

<aside class="callout">

🗣️ After applying the Service, its runtime status will initially appear as `pending`. If everything is configured correctly, it will transition to `running` after some time, so don’t panic!

</aside>
    

If the Lakesearch Service’s runtime status appears pending for a long time then check the Service logs for any possible errors by executing the below command.
    
```bash
dataos-ctl log -t service -n testingls -w public -r
```

<details>
  <summary>Expected output</summary>

    
  ```bash
  dataos-ctl log -t service -n testingls -w public -r
  INFO[0000] 📃 log(public)...                             
  INFO[0002] 📃 log(public)...complete                     
  
                NODE NAME             │     CONTAINER NAME     │ ERROR  
  ────────────────────────────────────┼────────────────────────┼────────
    testingls-96b2-d-597d7c9f4c-r87b2 │ testingls-96b2-indexer │        
  
  -------------------LOGS-------------------
  8:42AM DBG pkg/searchd/raw_sql_query.go:29 > [8.152977ms] << SHOW TABLE city STATUS; took=8.152977
  8:42AM DBG pkg/routes/accesslog.go:18 > /lakesearch/public:testingls/metrics code=200 method=GET took=1037855
  8:42AM DBG pkg/searchd/raw_sql_query.go:29 > [8.106225ms] << SHOW TABLE city STATUS; took=8.106225
  8:42AM DBG pkg/routes/accesslog.go:18 > /lakesearch/public:testingls/metrics code=200 method=GET took=1111317
  8:42AM DBG pkg/searchd/raw_sql_query.go:29 > [8.425655ms] << SHOW TABLE city STATUS; took=8.425655
  8:42AM DBG pkg/routes/accesslog.go:18 > /lakesearch/public:testingls/metrics code=200 method=GET took=1408504
  8:42AM DBG pkg/searchd/raw_sql_query.go:29 > [8.535937ms] << SHOW TABLE city STATUS; took=8.535937
  8:43AM DBG pkg/routes/accesslog.go:18 > /lakesearch/public:testingls/metrics code=200 method=GET took=1104167
  8:43AM DBG pkg/searchd/raw_sql_query.go:29 > [8.172188ms] << SHOW TABLE city STATUS; took=8.172188
  8:43AM DBG pkg/routes/accesslog.go:18 > /lakesearch/public:testingls/metrics code=200 method=GET took=1053376
  8:43AM DBG pkg/searchd/raw_sql_query.go:29 > [8.043104ms] << SHOW TABLE city STATUS; took=8.043104
  8:43AM INF pkg/searchd/indexer.go:90 > 56/ Start --->> city Indexer=city
  8:43AM DBG pkg/searchd/raw_sql_query.go:29 > [973.294µs] << SELECT `start`, `end` FROM `__indexer_state` WHERE `indexname` = 'city' took=0.973294
  8:43AM INF pkg/searchd/indexer.go:155 > {start}:1736448351, {end}:1839177951
  8:43AM DBG pkg/searchd/raw_sql_query.go:29 > [587.614µs] << DESC city took=0.587614
  8:43AM DBG pkg/source/connection.go:119 > [526.949321ms] << WITH base AS (
      SELECT 
    city_id,
    zip_code,
    zip_code as id,
    city_name,
    county_name,
    state_code,
    state_name,
    version,
    cast(ts_city as timestamp) as ts_city
  
  FROM 
    city
  
  ) SELECT 
    * 
  FROM 
    base 
  WHERE 
    epoch(ts_city) >= 1736448351 AND epoch(ts_city) < 1839177951 Source=datasets took=526.949321
  8:43AM DBG pkg/searchd/bulk_insert.go:70 > BulkInsert <<-- [500] {"items":[],"current_line":1,"skipped_lines":1,"errors":true,"error":""}
  8:43AM DBG pkg/searchd/bulk_insert.go:81 > BulkInsert performed of empty payload
  8:43AM DBG pkg/searchd/bulk_insert.go:37 > BulkInsert took [751.708µs] took=0.751708
  8:43AM DBG pkg/searchd/raw_sql_query.go:29 > [810.819µs] << REPLACE INTO `__indexer_state` VALUES (18003902094994090146, 'city', 1736448351, 1839264351) took=0.810819
  8:43AM INF pkg/searchd/indexer.go:127 > 56/ city <<--- Done #created=0 #deleted=0 #rows=0 Indexer=city
  8:43AM INF pkg/searchd/indexer.go:141 > Sleeping... Indexer=city duration=60000
  
  ```
</details>

For a detailed breakdown of the configuration options and attributes of a Lakesearch Service, please refer to the documentation: [Attributes of Lakesearch Service manifest](/resources/stacks/lakesearch/configurations/)