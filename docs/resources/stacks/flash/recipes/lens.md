# How to create Lens model with cached dataset?

To optimize data retrieval and enhance performance, cached datasets in Flash can be leveraged to construct Lens logical tables. This strategy minimizes data querying from the source by storing frequently accessed or queried Lenses in Flash, which avoids repeated source access and scanning of large datasets. As a result, queries can be processed faster, delivering responses in seconds.

## When to cache logical tables in Flash?

Consider the following criteria to determine if the logical tables of a Lens should be cached in Flash:

- **Complexity of the SQL View:** Caching is beneficial for SQL operations involving complex aggregate functions, multiple joins, and subqueries, which may result in resource-intensive queries.
- **Data Volume:** Lens models that handle large datasets from the source can benefit significantly from caching, as it expedites query processing.
- **Source Optimization:** If the source system experiences prolonged query execution times or frequent timeouts, caching in Flash can improve overall performance.

## Steps to use Flash datasets in Lens

### **1. Define Flash as the data source**

Configure the Flash service as the data source in the Lens deployment manifest file. Below is an example configuration:

```yaml
source:
  type: flash  # Specifies the data source type as Flash
  name: flash-test  # Name of the Flash service
  catalog: icebase
```

### **2. Add environment variables**

To enable Lens to interact with the Flash service, specify the following environment variables in the `Worker`, `API`, and `Router` sections of the Lens deployment manifest:

```yaml
envs:
  LENS2_SOURCE_WORKSPACE_NAME: public
  LENS2_SOURCE_FLASH_PORT: 5433
```

### **3. Sample Lens deployment manifest**

Below is a sample Lens deployment manifest that uses Flash as the data source for further clarity:

```yaml
version: v1alpha
name: "lens-test01"
layer: user
type: lens
tags:
  - lens
description: A sample Lens containing entities, views, and measures for testing
lens:
  compute: runnable-default
  secrets:
    - name: gitsecret-r
      allKeys: true
  source:
    type: flash  # Specifies Flash as the data source
    name: flash-test01  # Name of the Flash service
  repo:
    url: https://github.com/iamgroot/lens-flash
    lensBaseDir: lens-flash/flash/model  # Directory where Lens models are stored
    syncFlags:
      - --ref=main
  api:
    replicas: 1
    logLevel: debug
    envs:
      LENS2_SCHEDULED_REFRESH_TIMEZONES: "UTC,America/Vancouver,America/Toronto"
      LENS2_SOURCE_WORKSPACE_NAME: public
      LENS2_SOURCE_FLASH_PORT: 5433
    resources:
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
    resources:
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
    resources:
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
    resources:
      requests:
        cpu: 100m
        memory: 256Mi
      limits:
        cpu: 6000m
        memory: 6048Mi
```

### **3. Create and deploy the Lens model**

Once the manifest file is ready and Flash is configured as the data source, proceed to create and deploy the [Lens](/resources/lens/) model according to your deployment procedures.

This approach ensures optimal performance by leveraging cached datasets, minimizing data retrieval times, and improving query efficiency.