# Flash

[Flash](/resources/stacks/flash/) is designed to optimize query performance by leveraging in-memory execution. When used with DataOS Lakehouse and Iceberg-format depots, it enables efficient handling of large-scale queries by reducing latency and optimizing resource usage. The following explains how to configure Lens using Flash.


### **Prerequisites**

To create a Lens using Flash, ensure that the Flash is running as given in the below manifest. Ensure to replace the placeholders and modify the configurations as needed. Make sure a Persistent volume is attached with the Flash. It helps Flash to spill data over disk, which helps with the performance.

## Create Persistent Volume manifest file

Copy the template below and replace <name> with your desired resource name and <size> with the appropriate volume size (e.g., 100Gi, 20Gi, etc.), according to your available storage capacity. Make sure the configuration is aligned with both your storage and performance requirements. For the accessMode, you can choose ReadWriteOnce (RWO) for exclusive read-write access by a single node, or ReadOnlyMany (ROX) if the volume needs to be mounted as read-only by multiple nodes.

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

## Apply the Volume manifest file

Apply the persistent volume manifest file, using the following command in terminal:

```
dataos-ctl apply -f <file path of persistent volume>
```
This will deploy the Persistent Volume Resource, making it available for use by Flash Service.


## Create Service manifest file

Ensure that the name of the Persistent Volume you created is referenced correctly in the name attribute of the persistentVolume section. The name used here should match exactly with the name you assigned to the Persistent Volume during its creation.

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

  persistentVolume:
    name: <persistent_volume_name>
    directory: p_volume

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
      - create table if not exists f_sales as (select * from sales)  #table
      - create table if not exists m_customers as (select * from customer_data_master)
      - create table if not exists m_sites as (select * from site_check1)
      - create table if not exists table m_products as (select * from product_data_master)
```


### **How does this process work?**

The flow of Flash operates as follows:

**Data loading:** The `datasets` attribute specifies the depot `address` of the source data to be loaded into Flash. A dataset `name` is also provided, which Flash uses to generate a view of the source data.

**View creation:** Flash creates a view based on the assigned name, allowing for interaction with the source data without directly querying it.

**Table creation:** Specific columns from the generated view can be selected to define tables for further operations using `init` attribute. The `if not exists` clause ensures that the tables are created only if they don't already exist. If they are already present, the process skips creation.

**Usage in Lens model(SQL):** The tables created through the `init` attribute are used in SQL queries within Lens.

For example, in the manifest referenced, the `f_sales` table is first loaded from the source, and a view named `sales` is created. A table called `f_sales` is then defined using this sales view. This table is then referenced in SQL models within Lens.

> <b>Note</b> Flash directly uses the deployment.yml manifest file to create a Lens.

## Apply the Flash manifest file

To apply the Flash Service configuration, use the following command:

```bash
dataos-ctl apply -f <file path of flash service>
```

## Create an Instance-secrets manifest file

After successfully deploying the Persistent Volume and Flash Service, the next step is to deploy Secrets for securely managing your credentials. These credentials are essential for performing actions like pulling and pushing commits to your repository. They will be used to authenticate your identity and grant the necessary access permissions to deploy Lens-2.


```yaml
# RESOURCE META SECTION
name: <secret-name> # Secret Resource name (mandatory)
version: v1 # Secret manifest version (mandatory)
type: instance-secret # Type of Resource (mandatory)
description: demo-secret read secrets for code repository # Secret Resource description (optional)
layer: user # DataOS Layer (optional)

# INSTANCE SECRET-SPECIFIC SECTION
instance-secret:
  type: key-value # Type of Instance-secret (mandatory)
  acl: r # Access control list (mandatory)
  data: # Data (mandatory)
    GITSYNC_USERNAME: <code_repository_username>
    GITSYNC_PASSWORD: <code_repository_password>
```

## Apply the Instance-secret manifest file

To apply the Instance-secret configuration, use the following command:

```bash
dataos-ctl apply -f <file path of the instance-secret>
```

## Create Lens manifest file

### **1. Define Flash as the data source**

Configure the Flash service as the data source in the Lens deployment manifest file.

**`Source`**

- **`type`** The source section specifies that Flash is used as the data source (`type: flash`). This indicates that data for the Lens model will be loaded from the Flash service.

- **`name`**: The Flash service is identified by the `name` attribute, here it is flash-service-lens. This name should match the deployed Flash service used for data ingestion. Below is an example configuration.

```bash
source:
  type: flash  # Specifies the data source type as Flash
  name: flash-test  # Name of the Flash service
```

### **2. Add environment variables**

To enable Lens to interact with the Flash service, specify the following environment variables in the Worker, API, and Router sections of the Lens deployment manifest.

**`envs`**

The following environment variables are defined under multiple components, including api, worker, router, and iris

- **`LENS2_SOURCE_WORKSPACE_NAME`**  It refers to the workspace where the Flash service is deployed. 

- **`LENS2_SOURCE_FLASH_PORT`** The port number `5433` is specified for the Flash service. This port is used by Lens to establish communication with the Flash service. It ensures that all components—API, worker, router, and iris—can access the Flash service consistently.

```bash
envs:
  LENS2_SOURCE_WORKSPACE_NAME: public
  LENS2_SOURCE_FLASH_PORT: 5433
```
Following is the Lens manifest file:

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

## Apply Lens manifest file

Apply the Lens manifest file by using the following command in terminal:

```bash
dataos-ctl apply -f <lens-file-path>
```