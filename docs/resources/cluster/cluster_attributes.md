# Attributes of Cluster-specific Section

```yaml
cluster: 
  compute: {{query-default}} 
  runAsUser: {{minerva-cluster}} 
  maintenance: 
    restartCron: {{'13 1 */2 * *'}} 
    scalingCrons: 
    - cron: {{'5/10 * * * *'}} 
      replicas: {{3}} 
      resources: 
        limits: 
          cpu: {{1000m}} 
          memory: {{2Gi}} 
        requests: 
          cpu: {{800m}} 
          memory: {{1Gi}}
  minerva: 
    selector: 
      users: 
        {{-"**"}}
      sources: 
      {{- scanner/**}}
      {{- flare/**}}
    replicas: {{2}}
    match: {{''}}
    priority: {{'10'}}
    runAsApiKey: {{dataos apikey}}
    runAsUser: {{iamgroot}}
    resources: 
      limits: 
        cpu: {{4000m}}
        memory: {{8Gi}}
      requests: 
        cpu: {{1200m}}
        memory: {{2Gi}}
    debug: 
      logLevel: {{INFO}}
      trinoLogLevel: {{ERROR}}
    depots: 
      - address: {{dataos://icebase:default}}
        properties: 
          iceberg.file-format: {{PARQUET}} 
          iceberg.compression-codec: {{GZIP}} 
          hive.config.resources: {{"/usr/trino/etc/catalog/core-site.xml"}} 
      - address: {{dataos://bqdepot:default}} 
    catalogs: 
      - name: {{cache}} 
        type: {{memory}} 
        properties: 
          memory.max-data-per-node: {{"128MB"}} 
```

## Configuration Attributes/Fields

### **`cluster`**

**Description:** specifies the cluster-specific section<br>

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|------------------|-----------------|-------------------|-------------------|
| mapping          | mandatory       | none       | none           |

**Example Usage:**<br>
```yaml
cluster:
  {}
```

---

### **`compute`**

**Description:** compute to be referred by the Cluster Resource<br>

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|------------------|-----------------|-------------------|-------------------|
| string          | mandatory       | none              | query-default or any other query type custom Compute Resource              |

**Example Usage:**<br>
```yaml
compute: query-default
```

---

### **`runAsUser`**

**Description:** when the `runAsUser` attribute is configured with the UserID of the use-case assignee, it grants the authority to perform operations on behalf of that user.<br>

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|------------------|-----------------|-------------------|-------------------|
| string          | optional       | user-id of the user              | user-id of the use-case assignee             |

**Example Usage:**<br>
```yaml
runAsUser: iamgroot
```

---

### **`maintenance`**

> Available in DataOS CLI Version 2.8.2 and DataOS Version 1.10.41

**Description:** this property provides a set of features to assist with various operator activities that need to be simplified and automated by Poros. The maintenance features are invoked on a cron schedule. This triggers a restart or a scale which is very specific to the Cluster in purview.<br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------ | ------------------- |
| mapping        | optional         | none                | none                |

**Example Usage:**<br>
```yaml
maintenance:
  restartCron: {{'13 1 */2 * *'}}
  scalingCrons:
    - cron: {{'5/10 * * * *'}}
      replicas: {{3}}
      resources:
        limits:
          cpu: {{1000m}}
          memory: {{2Gi}}
        requests:
          cpu: {{800m}}
          memory: {{1Gi}}
```

---

### **`restartCron`**

**Description:** by specifying the cron expression into this designated attribute, Poros will restart the cluster based on the specified schedule.<br>

| **Data Type**     | **Requirement** | **Default Value** | **Possible Value**       |
| ----------------- | --------------   | ------------------ | ------------------------  |
| string             | optional          | none               | a valid cron expression   |

**Example Usage:**

- To restart the Cluster at 1:13am every other day, specify.
  ```yaml
  cluster:
    maintenance:
      restartCron: '13 1 */2 * *'
  ```

---

### **`scalingCrons`**

**Description:** Poros can horizontally and/or vertically scale the Cluster based on the provided schedules by specifying the cron, replicas, and/or resources.<br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------ | ------------------- |
| mapping        | optional         | none                | none                |

**Additional Information:** A `scalingCron` overrides the default provided `replicas` and/or `resources` in a cluster like Minerva while in an "active" cron window.   When a cron schedule is triggered, the supplied replicas and resources are put into effect until another cron schedule occurs. To clear an active scalingCron, clear out the `scalingCrons` section and apply the resource again.<br>
**Example Usage:**

- Horizontal Scaling: To scale the Cluster horizontally every 5 minutes, specify.
  ```yaml
  cluster:
    maintenance:
      scalingCrons:
      - cron: '5/10 * * * *'
        replicas: 3
      - cron: '10/10 * * * *'
        replicas: 0
  ```
- Vertical Scaling: To scale the Cluster vertically every 5 minutes, specify the following attributes/fields.
  ```yaml
  cluster:
    maintenance:
      scalingCrons:
      - cron: '5/10 * * * *'
        resources:
          limits:
            cpu: 1000m
            memory: 2Gi
          requests:
            cpu: 800m
            memory: 1Gi
      - cron: '10/10 * * * *'
        resources:
          limits:
            cpu: 3000m
            memory: 7Gi
          requests:
            cpu: 1500m
            memory: 3Gi

  ```
---

### **`cron`**

**Description:** specifies the cron schedule for scaling tasks in the cluster.<br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------ | ------------------- |
| string        | optional       | '5/10 * * * *'    | any valid cron expression |

**Example Usage:**<br>
```yaml
cluster:
  maintenance:
    scalingCrons:
      - cron: {{'5/10 * * * *'}}
```

---

### **`replicas`**

**Description:** specifies the number of replicas for scaling tasks in the cluster.<br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------ | ------------------- |
| integer       | mandatory      | 1                  | 1-4               |

**Example Usage:**<br>
```yaml
cluster:
  maintenance:
    scalingCrons:
      - replicas: 3
```

---

### **`resources`**

**Description:** resource allocation of CPU and Memory configuration for the cluster.<br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------ | ------------------- |
| mapping       | optional       | none               | none               |

**Example Usage:**<br>
```yaml
resources:
  limits:
    cpu: 1000m
    memory: 2Gi
  requests:
    cpu: 800m
    memory: 1Gi
```

---

### **`limits`**

**Description:** specifies the resource limits for CPU and memory for the specific cluster.<br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------ | ------------------- |
| mapping          | optional       | none               | none               |

**Example Usage:**<br>
```yaml
limits:
  cpu: 4000m
  memory: 8Gi
```

---

### **`cpu`**

**Description:** specifies the CPU resource configuration for the cluster.<br>

| **Data Type** | **Requirement** | **Default Value**       | **Possible Value**             |
| ------------- | -------------- | ------------------------ | ------------------------------- |
| string        | optional       | requests: 100m, limits: 400m | cpu units in milliCPU(m) or CPU Core |

**Example Usage:**<br>
```yaml
cpu: 1000m
```

---

### **`memory`**

**Description:** specifies the memory limit for scaling tasks in the cluster.<br>

| **Data Type** | **Requirement** | **Default Value**              | **Possible Value**                    |
| ------------- | -------------- | ------------------------------- | -------------------------------------- |
| string        | optional       | requests: 100Mi, limits: 400Mi | memory in Mebibytes(Mi) or Gibibytes(Gi) |

**Example Usage:**<br>
```yaml
memory: 2Gi
```

---

### **`requests`**

**Description:** Specifies the resource requests for the cluster.<br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------ | ------------------- |
| mapping       | optional       | none               | none               |

**Example Usage:**<br>
```yaml
requests:
  cpu: 800m
  memory: 1Gi
```

---

### **`minerva`**

**Description:** this attribute consists of key-value properties for the Minerva Cluster<br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------ | ------------------- |
| mapping       | mandatory      | none               | none               |

**Example Usage:**<br>
```yaml
minerva:
  {}
```

---

### **`selector`**

**Description:** selector declaration<br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------ | ------------------- |
| mapping       | mandatory      | none               | none               |

**Example Usage:**<br>
```yaml
cluster:
  minerva:
    selector:
      users:
        - "**"
      sources:
        - scanner/**
        - flare/**
```

---

### **`users`**

**Description:** specifies a user identified by a tag or regex patterns. They can also be a group of tags defined as a list.<br>

| **Data Type**       | **Requirement** | **Default Value** | **Possible Value**                              |
| ------------------- | -------------- | ------------------ | ---------------------------------------------- |
| list of strings     | mandatory      | none               | a valid subset of all available<br> users within DataOS |

**Example Usage:**<br>
```yaml
users:
  - "**"
```

---

### **`tags`**

**Description:** the cluster is accessible exclusively to users who possess specific tags.<br>

| **Data Type**     | **Requirement** | **Default Value** | **Possible Value**         |
| ----------------- | -------------- | ------------------ | --------------------------- |
| list of strings   | optional       | none               | any valid tag or pattern    |

**Additional Information:** Multiple users can be specified using AND/OR Logical Rules. To know more, click [here](../policy/policy_specific_section_grammar.md#tags)<br>
**Example Usage:**<br>
```yaml
users:
  tags:
    - "*"
```

---

### **`sources`**

**Description:** Specifies the sources that can redirect queries to Cluster.<br>

| **Data Type**       | **Requirement** | **Default Value** | **Possible Value**                                            |
| ------------------- | -------------- | ------------------ | ------------------------------------------------------------ |
| list of strings     | mandatory      | none               | list of strings representing source. For all sources, specify “**”. |

**Example Usage:**<br>
```yaml
cluster:
  minerva:
    selector:
      sources:
        - scanner/**
        - flare/**
```

---

### **`match`**

**Description:** specifies the match condition<br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------ | ------------------- |
| string        | mandatory      | none               | any/all            |

**Additional Information:** 
- `any` - must match at least one tag
- `all` - must match all tags<br>

**Example Usage:**<br>
```yaml
match: any
```

---

### **`priority`**

**Description:** specifies the priority level. Workloads will be redirected to Cluster with a lower priority level (inverse relationship).<br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value**     |
| ------------- | -------------- | ------------------ | ----------------------- |
| integer       | mandatory      | 10                 | any value between 1-5000 |

**Example Usage:**
```yaml
priority: 100
```

---

### **`runAsApiKey`**

**Description:** this attribue allows a user to assume the identity of another user through the provision of the latter's API key.<br>

| **Data Type** | **Requirement** | **Default Value**   | **Possible Value**         |
| ------------- | -------------- | -------------------- | --------------------------- |
| string        | mandatory      | user's dataos api key | any valid dataos api key   |

**Example Usage:**<br>
```yaml
runAsApiKey: abcdefghijklmnopqrstuvwxyz1234567890
```

---

### **`debug`**

**Description:** debug configuration for the Minerva cluster.<br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------ | ------------------- |
| mapping       | mandatory      | none               | none               |

**Example Usage:**<br>
```yaml
debug:
  logLevel: INFO
  trinoLogLevel: ERROR
```

---

### **`logLevel`**

**Description:** specifies the log level<br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value**  |
| ------------- | -------------- | ------------------ | ------------------- |
| string        | optional       | INFO               | INFO/DEBUG/ERROR   |

**Example Usage:**<br>
```yaml
logLevel: INFO
```

---

### **`trinoLogLevel`**

**Description:** specifies the Trino log level for the Minerva cluster.<br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value**  |
| ------------- | -------------- | ------------------ | ------------------- |
| string        | optional       | INFO               | INFO/DEBUG/ERROR   |

**Example Usage:**<br>
```yaml
trinoLogLevel: ERROR
```

---

### **`depots`**

**Description:** specification of sources to be queried. This includes only those sources on which a depot can be created and support querying from Minerva Cluster. <br>

| **Data Type**      | **Requirement** | **Default Value** | **Possible Value** |
| ------------------ | -------------- | ------------------ | ------------------- |
| list of mappings   | optional       | none               | none               |

**Example Usage:**<br>
```yaml
depots:
  - address: dataos://icebase:default
    properties:
      iceberg.file-format: PARQUET
      iceberg.compression-codec: GZIP
      hive.config.resources: "/usr/trino/etc/catalog/core-site.xml"
  - address: dataos://yakdevbq:default
```

---

### **`address`**

**Description:** specifies the address for a depot<br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value**        |
| ------------- | -------------- | ------------------ | -------------------------- |
| string        | optional       | none               | valid depot udl address   |

**Example Usage:**<br>
```yaml
address: dataos://icebase:default
```

---

### **`properties`**

**Description:** additional properties for a depot<br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------ | ------------------- |
| mapping       | optional       | none               | none               |

**Example Usage:**<br>
```yaml
properties:
  iceberg.file-format: PARQUET
  iceberg.compression-codec: GZIP
  hive.config.resources: "/usr/trino/etc/catalog/core-site.xml"
```
---
### **`catalogs`**

**Description:** attribute for catalog specification in scenarios where it is not possible to create a depot for certain sources, but a Trino connector is available and supported.<br>

| **Data Type**      | **Requirement** | **Default Value** | **Possible Value** |
| ------------------ | -------------- | ------------------ | ------------------- |
| list of mappings   | optional       | none               | none               |

**Example Usage:**<br>
```yaml
catalogs:
  - name: cache
    type: memory
    properties:
      memory.max-data-per-node: "128MB"
```
---
### **`name`**

**Description:** specifies the name of a catalog<br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value**    |
| ------------- | -------------- | ------------------ | ---------------------- |
| string        | optional       | none               | any valid string       |

**Example Usage:**<br>
```yaml
name: cache
```

---

### **`type`**

**Description:** specifies the type of a catalog<br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value**                                       |
| ------------- | -------------- | ------------------ | --------------------------------------------------------- |
| string        | optional       | none               | [View the list of all possible catalog types here](./connectors_configuration.md) |

**Example Usage:**<br>
```yaml
type: memory
```
---

### **`properties`**

**Description:** additional properties for a catalog<br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value**         |
| ------------- | -------------- | ------------------ | --------------------------- |
| mapping       | optional       | none               | valid connector properties |

**Example Usage:**<br>
```yaml
properties:
  memory.max-data-per-node: "128MB"
```