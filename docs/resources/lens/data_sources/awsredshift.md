# Connecting to AWS Redshift Depot

## Prerequisites

Ensure that you have an active AWS Redshift Depot.

## Deployment manifest file

The below manifest is intended for source type depot named `awsredshift`, created on the redshift source.

```yaml hl_lines="13-16"
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
    catalog: redshiftdepot  # catalog name/redshift depot name
  repo:
    url: https://bitbucket.org/tmdc/sample
    lensBaseDir: sample/lens/source/depot/redshift/model 
    # secretId: lens2_bitbucket_r
    syncFlags:
      - --ref=lens

  api:   # optional
    replicas: 1 # optional
    logLevel: info  # optional
    envs:
      LENS2_SCHEDULED_REFRESH_TIMEZONES: "UTC,America/Vancouver,America/Toronto"
      LENS2_DEV_MODE: "true"
      LENS2_CONCURRENCY: 10
      LENS2_DB_MAX_POOL: 15
      LENS2_DB_TIMEOUT: 1500000
      
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
    envs:
      LENS2_SCHEDULED_REFRESH_TIMEZONES: "UTC,America/Vancouver,America/Toronto"
      LENS2_DEV_MODE: "true"


    resources: # optional
      requests:
        cpu: 100m
        memory: 256Mi
      limits:
        cpu: 6000m
        memory: 6048Mi
  router: # optional
    logLevel: info  # optional
    envs:
      LENS2_SCHEDULED_REFRESH_TIMEZONES: "UTC,America/Vancouver,America/Toronto"
      LENS2_DEV_MODE: "true"
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
```



**Required AWS Redshift Depot Source Attributes**

```yaml
LENS2_SOURCE_TYPE: ${depot}  
LENS2_SOURCE_NAME: ${redshiftdepot}
LENS2_SOURCE_CATALOG_NAME: ${redshiftdepot}
```


## Docker compose Manifest file

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
