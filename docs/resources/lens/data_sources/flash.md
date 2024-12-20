# Flash

This section provides guidance on configuring the Lens using [Flash](/resources/stacks/flash/) [Service](/resources/service/).


### **Prerequisites**

To create a Lens using Flash Service, ensure that the Flash Service is running as given in the below manifest. Ensure to replace the placeholders and modify the configurations as needed.

## Example Service manifest file

Below is an example of the YAML configuration for the Flash Service:

```yaml
name: flash-service-lens
version: v1
type: service
tags:
  - service
description: flash service
workspace: curriculum
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

### **How Does This Process Work?**

The flow of Flash operates as follows:

**Data Loading:** The `datasets` attribute specifies the depot `address` of the source data to be loaded into Flash. A dataset `name` is also provided, which Flash uses to generate a view of the source data.

**View Creation:** Flash creates a view based on the assigned name, allowing for interaction with the source data without directly querying it.

**Table Creation:** Specific columns from the generated view can be selected to define tables for further operations using `init` attribute.

**Usage in Lens Model(SQL):** The tables created through the `init` attribute are used in SQL queries within Lens.

For example, in the manifest referenced, the `f_sales` table is first loaded from the source, and a view named `sales` is created. A table called `f_sales` is then defined using this sales view. This table is then referenced in SQL models within Lens.

> <b>Note</b> Flash directly uses the deployment.yml manifest file to create a Lens.


## Deployment Manifest File

```yaml title="lens_deployment.yml" hl_lines="13-15 25-26"
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
    name: flash-service-lens # flash service name
  repo:
    url: https://github.com/tmdc/sample    # repo address
    lensBaseDir: sample/source/flash/model     # location where lens models are kept in the repo
    syncFlags:
      - --ref=main
  api:
    replicas: 1
    logLevel: debug
    envs:
      LENS2_SOURCE_WORKSPACE_NAME: curriculum
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
      LENS2_SOURCE_WORKSPACE_NAME: curriculum
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
      LENS2_SOURCE_WORKSPACE_NAME: curriculum
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
      LENS2_SOURCE_WORKSPACE_NAME: curriculum
      LENS2_SOURCE_FLASH_PORT: 5433
    resources: # optional
      requests:
        cpu: 100m
        memory: 256Mi
      limits:
        cpu: 6000m
        memory: 6048Mi
```

### **Key configurations**

#### **`Source`**

- **`type`** The source section specifies that Flash is used as the data source (`type: flash`). This indicates that data for the Lens model will be loaded from the Flash service.

- **`name`**: The Flash service is identified by the `name` attribute, here it is flash-service-lens. This name should match the deployed Flash service used for data ingestion.

#### **`envs`**

The following environment variables are defined under multiple components, including api, worker, router, and iris

- **`LENS2_SOURCE_WORKSPACE_NAME`**  It refers to the workspace where the Flash service is deployed. 

- **`LENS2_SOURCE_FLASH_PORT`** The port number `5433` is specified for the Flash service. This port is used by Lens to establish communication with the Flash service. It ensures that all components—API, worker, router, and iris—can access the Flash service consistently.