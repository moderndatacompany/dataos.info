# AWS Redshift

## Prerequisites

Ensure that you have the following credentials available for [AWSRedshift Depot](/resources/depot/#amazon-redshift):

- The [hostname](https://docs.aws.amazon.com/redshift/latest/mgmt/configuring-connections.html#connecting-drivers) for the [AWS Redshift](https://aws.amazon.com/redshift/) cluster
- The [username/password](https://docs.aws.amazon.com/redshift/latest/dg/r_Users.html) for the AWS Redshift  cluster
- The name of the database to use within the AWS Redshift cluster

### **Docker Compose Manifest file**

The highlighted attributes are all the required attributes.

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
Follow these steps to create the `docker-compose.yml`:

- Step 1: Create a `docker-compose.yml` manifest file.
- Step 2: Copy the template from above and paste it in a code.
- Step 3: Fill the values for the atttributes/fields declared in the manifest file as per the AWS Redshift source.

**Required AWS Redshift Depot Source Attributes**

```yaml
LENS2_SOURCE_TYPE: ${depot}  
LENS2_SOURCE_NAME: ${redshiftdepot}
LENS2_SOURCE_CATALOG_NAME: ${redshiftdepot}
```

<!-- 

### **Environment Variables**

| Environment Variable   | Description                                                                                                                      | Possible Values | Required | When should these env variables be used                                                                                                        |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------|-----------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------|
| **LENS2_DB_SSL**        | If true, enables SSL encryption for database connections from Cube                                                              | true, false     | ❌        | When you need to ensure the security and encryption of database connections.                                                                   |
| **LENS2_CONCURRENCY**   | The number of concurrent connections each queue has to the database. Default is 4                                                | A valid number  | ❌        | When you need to adjust the number of parallel operations or queries to the database, to optimize performance based on workload and capabilities. |
| **LENS2_DB_MAX_POOL**   | The maximum number of concurrent database connections to pool. Default is 16                                                     | A valid number  | ❌        | When you need to manage the maximum number of database connections that can be open at one time, ensuring efficient resource utilization.        |

       -->

> Note: Ensure the user has AWS console access before proceeding.
> 

## Check Query Stats fo AWSRedshift

### 1. **Log in to AWS Console and Access Redshift**

1. **Login to the AWS Console.**
2. **Search for "Redshift" in the AWS Console search bar.**

<div style="text-align: center;">
    <img src="/resources/lens/data_sources/awsredshift/Untitled1.png" alt="Untitled" style="max-width: 100%; height: auto; border: 1px solid #000;">
</div>

### 2. **Select Redshift Cluster**

1. **Click on "Amazon Redshift" from the search results.** You will be directed to the Redshift dashboard.
2. **Select the appropriate region** and **choose the desired cluster name** from the list.

<div style="text-align: center;">
    <img src="/resources/lens/data_sources/awsredshift/Untitled2.png" alt="Untitled" style="max-width: 100%; height: auto; border: 1px solid #000;">
</div>

### 3. Access Query Monitoring

1. **Select the cluster** you want to monitor.
2. **Navigate to the "Query monitoring" tab** to view query statistics

<div style="text-align: center;">
    <img src="/resources/lens/data_sources/awsredshift/Untitled3.png" alt="Untitled" style="max-width: 100%; height: auto; border: 1px solid #000;">
</div>

### 4. View Running and Completed Queries

1. **In the "Query monitoring" tab**, you will see a list of running  and completed queries.

<div style="text-align: center;">
    <img src="/resources/lens/data_sources/awsredshift/Untitled4.png" alt="Untitled" style="max-width: 100%; height: auto; border: 1px solid #000;">
</div>

### 5. Monitor Specific Query

1. **Click on the query** you want to monitor.
2. **View the query statistics**, as shown in the example below.

<div style="text-align: center;">
    <img src="/resources/lens/data_sources/awsredshift/Untitled5.png" alt="Untitled" style="max-width: 100%; height: auto; border: 1px solid #000;">
</div>


<div style="text-align: center;">
    <img src="/resources/lens/data_sources/awsredshift/Untitled6.png" alt="Untitled" style="max-width: 100%; height: auto; border: 1px solid #000;">
</div>
