# Flash

## Connecting to Depot using Flash Service


### **Prerequisites**

- Flash Service

```yaml
name: flash-service-99
version: v1
type: service
tags:
  - service
description: flash service
workspace: public
service:
  servicePort: 5433
  replicas: 1
  logLevel: info
  compute: runnable-default
  resources:
    requests:
      cpu: 1000m
      memory: 1024Mi
  stack: flash+python:2.0
  stackSpec:
    datasets:
      - address: dataos://icebase:sales360/f_sales    #view
        name: sales
    
      - address: dataos://icebase:sales360/customer_data_master
        name: customer_data_master
    
      - address: dataos://icebase:sales360/site_check1
        name: site_check1
    
      - address: dataos://icebase:sales360/product_data_master
        name: product_data_master
    
    init:
      - create or replace table f_sales as (select * from sales)  #table
      - create or replace table m_customers as (select * from customer_data_master)
      - create or replace table m_sites as (select * from site_check1)
      - create or replace table m_products as (select * from product_data_master)
```

How does this work??

The flow of Flash works like this:

**Loading the Data:** In the datasets attribute, you provide the depot address of the source data you want to load into Flash. You also assign a name to this dataset, which Flash uses to create a view of the source data.

**Creating Views:** Flash creates a view using the name you specified. This view allows you to reference the source data without directly querying the source itself. 

**Creating Tables:** Using this view, you can choose specific columns from this view for further operations.

**Used in Lens Model in SQL:** Once initialized, the tables created in the init attribute are used in SQL queries within Lens.

For example, in the manifest provided above, we first load the f_sales table from the source and create a view named sales from it. We then define a table called f_sales using this sales view.

Subsequently, in Lens, we create an SQL model that references the f_sales table defined earlier.

> <b>Note</b> Flash directly uses deployment.yml manifest file to create a lens.


## Deployment Manifest File

``` title="lens_deployment.yml" hl_lines="13-15"
version: v1alpha
name: "lens-flash-test-99"
layer: user
type: lens
tags:
  - lens
description: A sample lens that contains three entities, a view and a few measures for users to test
lens:
  compute: runnable-default
  secrets: # Referred Instance-secret configuration (**mandatory for private code repository, not required for public repository)
    - name: githubr # Referred Instance Secret name (mandatory)
      allKeys: true # All keys within the secret are required or not (optional)
  source:
    type: flash # minerva, themis and depot
    name: flash-service-99 # flash service name
  repo:
    url: https://github.com/iamgroot/Lens
    lensBaseDir: Lens/flash/model     # location where lens models are kept in the repo
    syncFlags:
      - --ref=main
  api:
    replicas: 1
    logLevel: debug
    envs:
      LENS2_SCHEDULED_REFRESH_TIMEZONES: "UTC,America/Vancouver,America/Toronto"
      LENS2_SOURCE_WORKSPACE_NAME: public
      LENS2_SOURCE_FLASH_PORT: 5433
    resources: # optional
      requests:
        cpu: 100m
        memory: 256Mi
      limits:
        cpu: 2000m
        memory: 2048Mi

  worker:
    replicas: 1
    logLevel: debug
    envs:
      LENS2_SCHEDULED_REFRESH_TIMEZONES: "UTC,America/Vancouver,America/Toronto"
      LENS2_SOURCE_WORKSPACE_NAME: public
      LENS2_SOURCE_FLASH_PORT: 5433
    resources: # optional
      requests:
        cpu: 100m
        memory: 256Mi
      limits:
        cpu: 6000m
        memory: 6048Mi

  router:
    logLevel: info
    envs:
      LENS2_SCHEDULED_REFRESH_TIMEZONES: "UTC,America/Vancouver,America/Toronto"
      LENS2_SOURCE_WORKSPACE_NAME: public
      LENS2_SOURCE_FLASH_PORT: 5433
    resources: # optional
      requests:
        cpu: 100m
        memory: 256Mi
      limits:
        cpu: 6000m
        memory: 6048Mi

  iris:
    logLevel: info  
    envs:
      LENS2_SCHEDULED_REFRESH_TIMEZONES: "UTC,America/Vancouver,America/Toronto"
      LENS2_SOURCE_WORKSPACE_NAME: public
      LENS2_SOURCE_FLASH_PORT: 5433
    resources: # optional
      requests:
        cpu: 100m
        memory: 256Mi
      limits:
        cpu: 6000m
        memory: 6048Mi
```