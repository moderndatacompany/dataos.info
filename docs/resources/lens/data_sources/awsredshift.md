# Connecting to AWS Redshift Depot

## Step 1: Create the Depot

If the Depot is not active, you need to create one using the provided template.

```yaml
name: ${{redshift-depot-name}}
version: v2alpha
type: depot
tags:
  - ${{redshift}}
layer: user
description: ${{Redshift Sample data}}
depot:
  type: REDSHIFT
  redshift:
    host: ${{hostname}}
    subprotocol: ${{subprotocol}}
    port: ${{5439}}
    database: ${{sample-database}}
    bucket: ${{tmdc-dataos}}
    relativePath: ${{development/redshift/data_02/}}
  external: ${{true}}
  secrets:
    - name: ${{redshift-instance-secret-name}}-r
      allkeys: true

    - name: ${{redshift-instance-secret-name}}-rw
      allkeys: true
```

## Step 2: Prepare the Lens model folder

Organize the Lens model folder with the following structure to define tables, views, and governance policies:

```
model
├── sqls
│   └── sample.sql  # SQL script for table dimensions
├── tables
│   └── sample_table.yml  # Logical table definition (joins, dimensions, measures, segments)
├── views
│   └── sample_view.yml  # Logical views referencing tables
└── user_groups.yml  # User group policies for governance
```

1. **SQL Scripts (`model/sqls`):** Add SQL files defining table structures and transformations.

2. **Tables (`model/tables`):** Define logical tables in separate YAML files. Include dimensions, measures, segments, and joins.

3. **Views (`model/views`):** Define views in YAML files, referencing the logical tables.

4. **User Groups (`user_groups.yml`):** Define access control by creating user groups and assigning permissions.

## Step 3: Deployment manifest file

Once the Lens with semantic model is prepared, create a `lens_deployment.yml` file parallel to the model folder to configure the deployment using the YAML template below.

```yaml
version: v1alpha
name: "redshiftlens"
layer: user
type: lens
tags:
  - lens
description: redshiftlens deployment on lens2
lens:
  compute: runnable-default
  secrets:
    - name: bitbucket-cred
      allKeys: true
  source:
    type: depot # source type is depot here
    name: redshiftdepot # name of the redshift depot
  repo:
    url: https://bitbucket.org/tmdc/sample
    lensBaseDir: sample/lens/source/depot/redshift/model 
    # secretId: lens2_bitbucket_r
    syncFlags:
      - --ref=lens

  api:   # optional
    replicas: 1 # optional
    logLevel: info  # optional    
    resources: # optional
      requests:
        cpu: 100m
        memory: 256Mi
      limits:
        cpu: 2000m
        memory: 2048Mi
  worker: # optional
    replicas: 2 # optional
    logLevel: debug  # optional
    resources: # optional
      requests:
        cpu: 100m
        memory: 256Mi
      limits:
        cpu: 6000m
        memory: 6048Mi
  router: # optional
    logLevel: info  # optional
    resources: # optional
      requests:
        cpu: 100m
        memory: 256Mi
      limits:
        cpu: 6000m
        memory: 6048Mi
  iris:
    logLevel: info  
    resources: # optional
      requests:
        cpu: 100m
        memory: 256Mi
      limits:
        cpu: 6000m
        memory: 6048Mi
  metric:
    logLevel: info  # Logging level for the metric component
```

Each section of the YAML template defines key aspects of the Lens deployment. Below is a detailed explanation of its components:

* **Defining the Source:**

      * **`type`:**  The `type` attribute in the `source` section must be explicitly set to `depot`.

      * **`name`:** The `name` attribute in the `source` section should specify the name of the AWS Redshift Depot created.

* **Setting Up Compute and Secrets:**

      * Define the compute settings, such as which engine (e.g., `runnable-default`) will process the data.

      * Include any necessary secrets (e.g., credentials for Bitbucket or AWS) for secure access to data and repositories.

* **Defining Repository:**

      * **`url`** The `url` attribute in the repo section specifies the Git repository where the Lens model files are stored. For instance, if your repo name is lensTutorial then the repo `url` will be  [https://bitbucket.org/tmdc/lensTutorial](https://bitbucket.org/tmdc/lensTutorial)

      * **`lensBaseDir`:**  The `lensBaseDir` attribute refers to the directory in the repository containing the Lens model. Example: `sample/lens/source/depot/awsredshift/model`.

      * **`secretId`:**  The `secretId` attribute is used to access private repositories (e.g., Bitbucket, GitHub). It specifies the secret needed to authenticate and access the repository securely.

      * **`syncFlags`**:  Specifies additional flags to control repository synchronization. Example: `--ref=dev` specifies that the Lens model resides in the dev branch.

* **Configure API, Worker, and Metric Settings (Optional):** Set up replicas, logging levels, and resource allocations for APIs, workers, routers, and other components.

## Step 4: Apply the Lens deployment manifest file

After configuring the deployment file with the necessary settings and specifications, apply the manifest using the following command:


=== "Command"

    ```bash 
    dataos-ctl resource apply -f ${manifest-file-path}
    ```
=== "Alternative command"

    ```bash 
    dataos-ctl apply -f ${manifest-file-path}
    ```
=== "Example usage"

    ```bash 
    dataos-ctl apply -f /lens/lens_deployment.yml -w curriculum
    # Expected output
    INFO[0000] 🛠 apply...                                   
    INFO[0000] 🔧 applying(curriculum) sales360:v1alpha:lens... 
    INFO[0001] 🔧 applying(curriculum) sales360:v1alpha:lens...created 
    INFO[0001] 🛠 apply...complete
    ```


## Docker compose manifest file

<details>

  <summary>Docker compose manifest file for local testing</summary>

```yaml hl_lines="14-16"
version: "2.2"

x-lens2-environment: &lens2-environment
  # DataOS
  DATAOS_FQDN: liberal-donkey.dataos.app

  # Overview
  LENS2_NAME: ${redshiftlens}
  LENS2_DESCRIPTION: "Ecommerce use case on Adventureworks sales data"
  LENS2_TAGS: "lens2, ecom, sales and customer insights"
  LENS2_AUTHORS: "iamgroot"
  LENS2_SCHEDULED_REFRESH_TIMEZONES: "UTC,America/Vancouver,America/Toronto"
  # Data Source
  LENS2_SOURCE_TYPE: ${depot}  
  LENS2_SOURCE_NAME: ${redshiftdepot}
  LENS2_SOURCE_CATALOG_NAME: ${redshiftdepot}
 
  # Log
  LENS2_LOG_LEVEL: error
  CACHE_LOG_LEVEL: "trace"
  # Operation
  #LENS_DB_QUERY_TIMEOUT: 15m
  LENS2_DEV_MODE: true
  LENS2_DEV_MODE_PLAYGROUND: false
  LENS2_REFRESH_WORKER: true
  LENS2_SCHEMA_PATH: model
  LENS2_PG_SQL_PORT: 5432
  CACHE_DATA_DIR: "/var/work/.store"
  NODE_ENV: production
  LENS2_ALLOW_UNGROUPED_WITHOUT_PRIMARY_KEY: "true"
services:
  api:
    restart: always
    image: rubiklabs/lens2:0.35.41-02
    ports:
      - 4000:4000
      - 25432:5432
      - 13306:13306
    environment:
      <<: *lens2-environment   
    volumes:
      - ./model:/etc/dataos/work/model
```
</details>

<!-- 

### **Environment Variables**

| Environment Variable   | Description                                                                                                                      | Possible Values | Required | When should these env variables be used                                                                                                        |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------|-----------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------|
| **LENS2_DB_SSL**        | If true, enables SSL encryption for database connections from Cube                                                              | true, false     | ❌        | When you need to ensure the security and encryption of database connections.                                                                   |
| **LENS2_CONCURRENCY**   | The number of concurrent connections each queue has to the database. Default is 4                                                | A valid number  | ❌        | When you need to adjust the number of parallel operations or queries to the database, to optimize performance based on workload and capabilities. |
| **LENS2_DB_MAX_POOL**   | The maximum number of concurrent database connections to pool. Default is 16                                                     | A valid number  | ❌        | When you need to manage the maximum number of database connections that can be open at one time, ensuring efficient resource utilization.        |

       -->

## Check query statistics for AWSRedshift


> Note: Ensure the user has AWS console access before proceeding.
> 

### **1. Log in to AWS Console and access Redshift**

  a. Login to the AWS Console.<br>
  b. Search for 'Redshift' in the AWS Console search bar.

<div style="text-align: center;">
    <img src="/resources/lens/data_sources/awsredshift/Untitled1.png" alt="Untitled" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

### **2. Select Redshift Cluster**

  a. Click on 'Amazon Redshift' from the search results.You will be directed to the Redshift dashboard.<br>
  b. Select the appropriate region and choose the desired cluster name from the list.

<div style="text-align: center;">
    <img src="/resources/lens/data_sources/awsredshift/Untitled2.png" alt="Untitled" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

### **3. Access Query Monitoring**

  a. Select the cluster you want to monitor.<br>
  b. Navigate to the 'Query monitoring' tab to view query statistics.

<div style="text-align: center;">
    <img src="/resources/lens/data_sources/awsredshift/Untitled3.png" alt="Untitled" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

### **4. View running and completed queries**

  a. In the 'Query monitoring' tab, you will see a list of running  and completed queries.

<div style="text-align: center;">
    <img src="/resources/lens/data_sources/awsredshift/Untitled4.png" alt="Untitled" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

### **5. Monitor specific query**

  a. Click on the query you want to monitor.
  b. View the query statistics, as shown in the example below.

<div style="text-align: center;">
    <img src="/resources/lens/data_sources/awsredshift/Untitled5.png" alt="Untitled" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>


<div style="text-align: center;">
    <img src="/resources/lens/data_sources/awsredshift/Untitled6.png" alt="Untitled" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>
