# Attributes of Cluster manifest

## Structure of Cluster-specific Section

```yaml
cluster:
  compute: ${{query-default}} # mandatory
  runAsApiKey: ${{abcdefghijklmnopqrstuvwxyz}} # mandatory
  runaAsUser: ${{minerva-cluster}}
  maintenance:
    restartCron: ${{'13 1 */2 * *'}}
    timezone: ${{Asia/Kolkata}} # mandatory
    scalingCrons: 
      - cron: ${{'5/10 * * * *'}} # mandatory
        timezone: ${{Europe/Berlin}} # mandatory
        replicas: ${{2}}
        resources: 
          requests: 
            cpu: ${{800m}}
            memory: ${{1Gi}}
          limits: 
            cpu: ${{1000m}}
            memory: ${{2Gi}}	
  minerva: 
    replicas: ${{2}} # mandatory
    resources:
    secrets:
      - ${{mysecret}}
    depots: # mandatory
      - address: ${{dataos://icebase:default}} # mandatory
        properties:
          iceberg.file-format: ${{PARQUET}} 
          iceberg.compression-codec: ${{GZIP}} 
          hive.config.resources: ${{"/usr/trino/etc/catalog/core-site.xml"}}
        secrets: 
          - name: ${{newsecret}} # mandatory
            workspace: ${{curriculum}}
            key: ${{newone}}
            keys: 
              - ${{newone}}
              - ${{oldone}}
            allKeys: ${{true}}
            consumptionType: ${{envVars}}
    catalogs:
      - name: ${{cache}} # mandatory
        type: ${{memory}} # mandatory
        properties: 
          memory.max-data-per-node: ${{"128MB"}} 
        secrets: 
          - name: ${{newsecret}} # mandatory
            workspace: ${{curriculum}}
            key: ${{newone}}
            keys: 
              - ${{newone}}
              - ${{oldone}}
            allKeys: ${{true}}
            consumptionType: ${{envVars}}
    debug:
      logLevel: ${{INFO}}
      trinoLogLevel: ${{ERROR}}
    
    coordinatorEnvs:
      ${{alpha: beta}} 
    workerEnvs:
      ${{gamma: sigma}} 
    overrideDefaultEnvs: true
    spillOverVolume: twenty
    selector:
      users: # mandatory
        - ${{"**"}}
      tags: # mandatory
        - ${{alpha}}
        - ${{beta}}
      sources: # mandatory
        - ${{scanner/**}}
        - ${{flare/**}}
      match: ${{''}} # mandatory
      priority: ${{'10'}} # mandatory
      
  nats:
    replicas: ${{5}} # mandatory
    volumeType: ${{newone}} # mandatory
    volumeSize: ${{30mi}} # mandatory
    maxConnections: ${{4}} # mandatory
    roles: # mandatory
      - name: ${{newrole}} # mandatory
        permissions: 
          publish: # mandatory
            - ${{alpha}}
            - ${{beta}}
          subscribe: # mandatory
            - ${{newone}}
            - ${{develop}}
          allow_responses: ${{true}}
  jupyterHub:
    ingress: 
      enabled: ${{true}}
      path: ${{/strip/}}
      stripPath: ${{false}}
      noAuthentication: ${{true}}
      appDetailSpec: ${{random}}
      apiDetailSpec: ${{random}}
    oidcConfig: # mandatory
      clientId: ${{hellow}} # mandatory
      clientSecret: ${{delta}} # mandatory
    storageClass: ${{alpha}} # mandatory
    singleUserConfig: # mandatory
      volumeCapacity: ${{alpha}} # mandatory
```
<center><i>Structure of Cluster-specific Section</i></center>

## Configuration Attributes

## **`cluster`**

**Description:** the `cluster` mapping/section defines configurations for the Cluster Resource.

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|------------------|-----------------|-------------------|-------------------|
| mapping          | mandatory       | none       | none           |

**Example Usage:**<br>
```yaml
cluster: 
  compute: query-default 
  runAsUser: minerva-cluster
  minerva: 
    selector: 
      users: 
        -"**"
      sources: 
        - scanner/**
        - flare/**
    replicas: 2
    match: ''
    priority: '10'
    runAsApiKey: dataos apikey
    runAsUser: iamgroot
    resources: 
      limits: 
        cpu: 4000m
        memory: 8Gi
      requests: 
        cpu: 1200m
        memory: 2Gi
    debug: 
      logLevel: INFO
      trinoLogLevel: ERROR
    depots: 
      - address: dataos://icebase:default
        properties: 
          iceberg.file-format: PARQUET
          iceberg.compression-codec: GZIP
          hive.config.resources: "/usr/trino/etc/catalog/core-site.xml"
      - address: dataos://bqdepot:default
    catalogs: 
      - name: cache
        type: memory
        properties: 
          memory.max-data-per-node: "128MB"
```

---

### **`compute`**

**Description:** the `compute` attribute specifies the name of the [Compute](/resources/compute/) Resource-instance referred by the Cluster.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| string | mandatory | query-default | any valid [query-type](/resources/compute/#query-compute) Compute Resource-instance name |

**Example Usage:**<br>
```yaml
cluster:
  compute: query-default
```

---

### **`runAsApiKey`**

**Description:** the `runAsApiKey` attribute allows a user to assume the identity of another user through the provision of the latter's API key.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| string | mandatory | abcdefghijklmnopqrstuvwxyz | any valid DataOS user API key |

**Additional Details**: The apikey can be obtained by executing the following command from the [CLI](/interfaces/cli/):

```shell
dataos-ctl user apikey get
```

In case no apikey is available, the below command can be run to create a new apikey

```shell
dataos-ctl user apikey create -n ${{name of the apikey}} -d ${{duration for the apikey to live}}
```

**Example Usage:**<br>
```yaml
cluster:
  runAsApiKey: abcdefghijklmnopqrstuvwxyz
```

---

### **`runAsUser`**

**Description:** when the `runAsUser` attribute is configured with the UserID of the use-case assignee, it grants the authority to perform operations on behalf of that user.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| string | optional | user-id of the user | user-id of the use-case assignee |

**Example Usage:**<br>
```yaml
cluster:
  runAsUser: iamgroot
```

---

### **`maintenance`**

> Available in DataOS CLI Version 2.8.2 and DataOS Version 1.10.41

**Description:** The `maintenance` section provides a set of Cluster maintenance-related configurations that assist with various operator activities that need to be simplified and automated by Poros, the DataOS orchestrator. The Cluster maintenance features are invoked on a `cron` schedule. This triggers a restart or a scale which is very specific to the Cluster in purview.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------ | ------------------- |
| mapping        | optional         | none                | none                |

**Example Usage:**<br>
```yaml
cluster:
  maintenance:
    restartCron: '13 1 */2 * *'
    timezone: Europe/Berlin # mandatory
    scalingCrons: 
      - cron: '5/10 * * * *' # mandatory
        timezone: Europe/Berlin # mandatory
        replicas: 2
        resources: 
          requests: 
            cpu: 800m
            memory: 1Gi
          limits: 
            cpu: 1000m
            memory: 2Gi
```

---

#### **`restartCron`**

**Description:** The `restartCron` attribute specifies the cron schedule for cluster restart. Poros, the DataOS orchestrator will restart the Cluster based on the specified schedule.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| string | mandatory | none | any valid cron expression |

**Example Usage:**<br>
- To restart the Cluster at 1:13am every other day, specify.
  ```yaml
  cluster:
    maintenance:
      restartCron: '13 1 */2 * *'
  ```

---

#### **`timezone`**

**Description:** The `timezone` attribute specifies the Cluster's timezone.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| string | mandatory | none | any valid timezone from the [tz database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) |

**Example Usage:**<br>
```yaml
cluster:
  maintenance:
    timezone: Asia/Kolkata
```

---

#### **`scalingCrons`**

**Description:** The `scalingCrons` attribute defines configurations for scaling the Cluster. Poros can horizontally and/or vertically scale the Cluster based on the provided configuration.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------ | ------------------- |
| mapping        | optional         | none                | none                |

Each scaling cron includes the following attributes:

- [**`cron`**](#cron): The cron schedule for the job.
- [**`timezone`**](#timezone): The timezone for the job.
- [**`replicas`**](#replicas): The number of replicas.
- [**`resources`**](#resources): Resource specifications for the job, including [`requests`](#requests) and [`limits`](#limits) for CPU and memory.

**Additional Information:** A `scalingCron` overrides the default provided `replicas` and/or `resources` in a cluster like Minerva while in an "active" cron window. When a cron schedule is triggered, the supplied replicas and resources are put into effect until another cron schedule occurs. To clear an active scalingCron, clear out the `scalingCrons` section and apply the Resource again.<br>
**Example Usage:**

- **Horizontal Scaling:** To scale the Cluster horizontally every 5 minutes, specify.
  ```yaml
  cluster:
    maintenance:
      scalingCrons:
      - cron: '5/10 * * * *'
        timezone: Europe/Berlin
        replicas: 3
      - cron: '10/10 * * * *'
        timezone: Europe/Berlin
        replicas: 0
  ```
- **Vertical Scaling:** To scale the Cluster vertically every 5 minutes, specify the following attributes/fields.
  ```yaml
  cluster:
    maintenance:
      scalingCrons:
      - cron: '5/10 * * * *'
        timezone: Europe/Berlin
        resources:
          limits:
            cpu: 1000m
            memory: 2Gi
          requests:
            cpu: 800m
            memory: 1Gi
      - cron: '10/10 * * * *'
        timezone: Europe/Berlin
        resources:
          limits:
            cpu: 3000m
            memory: 7Gi
          requests:
            cpu: 1500m
            memory: 3Gi

  ```
---

##### **`cron`**

**Description:** specifies the cron schedule for scaling tasks in the Cluster.<br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------ | ------------------- |
| string        | optional       | none    | any valid cron expression |

**Example Usage:**<br>
```yaml
cluster:
  maintenance:
    scalingCrons:
      - cron: '5/10 * * * *'
```

---

##### **`replicas`**

**Description:** specifies the number of replicas for scaling tasks in the Cluster.<br>

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

##### **`resources`**

**Description:** resource allocation of CPU and Memory configuration for the Cluster.<br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------ | ------------------- |
| mapping       | optional       | none               | none               |

**Example Usage:**<br>
```yaml
cluster:
  maintenance:
    scalingCrons:
      resources:
        limits:
          cpu: 1000m
          memory: 2Gi
        requests:
          cpu: 800m
          memory: 1Gi
```

---

###### **`limits`**

**Description:** specifies the resource limits for CPU and memory for the specific Cluster.<br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------ | ------------------- |
| mapping          | optional       | none               | none               |

**Example Usage:**<br>
```yaml
cluster:
  maintenance:
    scalingCrons:
      resources:
        limits:
          cpu: 1000m
          memory: 2Gi
```


---

###### **`requests`**

**Description:** Specifies the resource requests for the cluster.<br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------ | ------------------- |
| mapping       | optional       | none               | none               |

**Example Usage:**<br>
```yaml
cluster:
  maintenance:
    scalingCrons:
      resources:
        requests:
          cpu: 800m
          memory: 1Gi
```


**`cpu`**

**Description:** specifies the CPU resource configuration for the Cluster.<br>

| **Data Type** | **Requirement** | **Default Value**       | **Possible Value**             |
| ------------- | -------------- | ------------------------ | ------------------------------- |
| string        | optional       | requests: 100m, limits: 400m | cpu units in milliCPU(m) or CPU Core |

**Example Usage:**<br>
```yaml
cluster:
  maintenance:
    scalingCrons:
      resources:
        limits:
          cpu: 1000m
```

---

**`memory`**

**Description:** specifies the requested memory for scaling tasks in the Cluster.<br>

| **Data Type** | **Requirement** | **Default Value**              | **Possible Value**                    |
| ------------- | -------------- | ------------------------------- | -------------------------------------- |
| string        | optional       | requests: 100Mi, limits: 400Mi | memory in Mebibytes(Mi) or Gibibytes(Gi) |

**Example Usage:**<br>
```yaml
cluster:
  maintenance:
    scalingCrons:
      resources:
        limits:
          cpu: 1000m
          memory: 2Gi
```

---

### **`minerva`**

**Description:** The `minerva` attribute defines configurations for the Minerva Cluster.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------ | ------------------- |
| mapping       | mandatory      | none               | none               |

**Example Usage:**<br>
```yaml
cluster:
  minerva: 
    replicas: 2 # mandatory
    resources:
    secrets:
      - mysecret
    depots: # mandatory
      - address: dataos://icebase:default # mandatory
        properties:
          iceberg.file-format: PARQUET 
          iceberg.compression-codec: GZIP 
          hive.config.resources: "/usr/trino/etc/catalog/core-site.xml"
```

---

#### **`replicas`**

**Description:** The `replicas` attribute specifies the number of Minerva Cluster replicas.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| string | mandatory | 1 | any valid postive integer |

**Example Usage:**<br>
```yaml
cluster:
  minerva:
    replicas: 2
```

#### **`secrets`**

**Description:** The `secrets` attribute is a list of secrets referred by Minerva Cluster.

**Example Usage:**<br>
```yaml
cluster:
  minerva:
    secrets:
      - mysecret
```

---

#### **`depots`**

**Description:** The `depots` attribute is a list of depots configurations. Its a specification of sources to be queried. This includes only those sources on which a depot can be created and support querying from Minerva Cluster.

| **Data Type**      | **Requirement** | **Default Value** | **Possible Value** |
| ------------------ | -------------- | ------------------ | ------------------- |
| list of mappings   | optional       | none               | none               |

Each depot configuration comprises of the following attributes:

- [**`address`**](#address): The depot's address.
- [**`properties`**](#properties): Properties specific to the depot.
- [**`secrets`**](#secrets): List of Secret Resource referred by the depot.

**Example Usage:**<br>
```yaml
cluster:
  minerva:
    depots:
      - address: dataos://icebase:default
        properties:
          iceberg.file-format: PARQUET
          iceberg.compression-codec: GZIP
          hive.config.resources: "/usr/trino/etc/catalog/core-site.xml"
        secrets:
          - name: newsecret
            workspace: curriculum
            key: newone
            keys:
              - newone
              - oldone
            allKeys: true
            consumptionType: envVars
```

---

###### **`address`**

**Description:** specifies the address for a depot<br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value**        |
| ------------- | -------------- | ------------------ | -------------------------- |
| string        | optional       | none               | valid depot udl address   |

**Example Usage:**<br>
```yaml
cluster:
  minerva:
    depots:
      - address: dataos://icebase:default
```

---

###### **`properties`**

**Description:** additional properties for a depot<br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------ | ------------------- |
| mapping       | optional       | none               | none               |

**Example Usage:**<br>
```yaml
cluster:
  minerva:
    depots:
      - properties:
          iceberg.file-format: PARQUET
          iceberg.compression-codec: GZIP
          hive.config.resources: "/usr/trino/etc/catalog/core-site.xml"
```
---

##### **`secrets`**

**Description:** Secret Resource referred by the depot/catalog.

**Additional Information**: For more information, refer to the link [Secrets](/resources/secret/#referencing-a-secret-in-a-depot)

---

##### **`catalogs`**

**Description:** The `catalogs` attribute for specification of sources in scenarios where it is not possible to create a depot, but a Trino connector is available and supported for the source.

| **Data Type**      | **Requirement** | **Default Value** | **Possible Value** |
| ------------------ | -------------- | ------------------ | ------------------- |
| list of mappings   | optional       | none               | none               |

**Example Usage:**<br>
```yaml
cluster:
  minerva:
    catalogs:
      - name: cache
        type: memory
        properties:
          memory.max-data-per-node: "128MB"
```

Each catalog configuration includes the following attributes:

- [**`name`**](#name): The catalog name.
- [**`type`**](#type): The catalog type.
- [**`properties`**](#properties-1): Catalog-specific properties.
- [**`secrets`**](#secrets-1): List of secrets used by the catalog.

**Example Usage:**<br>
```yaml
cluster:
  minerva:
    catalogs:
      - name: cache
        type: memory
        properties:
          memory.max-data-per-node: "128MB"
        secrets:
          - name: newsecret
            workspace: curriculum
            key: newone
            keys:
              - newone
              - oldone
            allKeys: true
            consumptionType: envVars
```

---
###### **`name`**

**Description:** specifies the name of a catalog<br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value**    |
| ------------- | -------------- | ------------------ | ---------------------- |
| string        | optional       | none               | any valid string       |

**Example Usage:**<br>
```yaml
cluster:
  minerva:
    catalogs:
      - name: cache
```

---

###### **`type`**

**Description:** specifies the type of a catalog<br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value**                                       |
| ------------- | -------------- | ------------------ | --------------------------------------------------------- |
| string        | optional       | none               | [View the list of all possible catalog types here](/resources/cluster/connectors_configuration/) |

**Example Usage:**<br>
```yaml
cluster:
  minerva:
    catalogs:
      - type: memory
```
---

###### **`properties`**

**Description:** additional properties for a catalog<br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value**         |
| ------------- | -------------- | ------------------ | --------------------------- |
| mapping       | optional       | none               | valid connector properties |

**Example Usage:**<br>
```yaml
cluster:
  minerva:
    catalogs:
      - properties:
          memory.max-data-per-node: "128MB"
```

---

##### **`debug`**

**Description:** The `debug` section includes debug-related configurations for Minerva.

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

###### **`logLevel`**

**Description:** The `logLevel` attribute specifies the log level for Minerva's logs.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| string | optional | INFO | INFO/DEBUG/ERROR |

**Example Usage:**<br>
```yaml
cluster:
  minerva:
    debug:
      logLevel: INFO
```

---

###### **`trinoLogLevel`**

**Description:** The `trinoLogLevel` attribute specifies the log level for Trino logs within Minerva.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| string | optional | INFO | INFO/DEBUG/ERROR |

**Example Usage:**<br>
```yaml
cluster:
  minerva:
    debug:
      trinoLogLevel: ERROR
```

---

#### **`coordinatorEnvs`**

**Description:** The `coordinatorEnvs` section includes environment variables for the coordinator node.

**Example Usage:**<br>
```yaml
cluster:
  minerva:
    coordinatorEnvs:
      alpha: beta
```

---

#### **`workerEnvs`**

**Description:** The `workerEnvs` section includes environment variables for worker nodes.

**Example Usage:**<br>
```yaml
cluster:
  minerva:
    workerEnvs:
      gamma: sigma
```

---

#### **`overrideDefaultEnvs`**

**Description:** The `overrideDefaultEnvs` attribute specifies whether to override default environment variables.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| boolean | optional | true | true or false |

**Example Usage:**<br>
```yaml
cluster:
  minerva:
    overrideDefaultEnvs: true
```

---

#### **`spillOverVolume`**

**Description:** The `spillOverVolume` attribute specifies the spill-over volume.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| string | optional | twenty | any valid string |

**Example Usage:**<br>
```yaml
cluster:
  minerva:
    spillOverVolume: twenty
```

---

#### **`selector`**

**Description:** The `selector` section defines a selector for users, tags, sources, match, and priority.

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

##### **`users`**

**Description:** the `users` attribute specifies a user identified by a tag or regex patterns. They can also be a group of tags defined as a list.

| **Data Type**       | **Requirement** | **Default Value** | **Possible Value**                              |
| ------------------- | -------------- | ------------------ | ---------------------------------------------- |
| list of strings     | mandatory      | none               | a valid subset of all available<br> users within DataOS |

**Example Usage:**<br>
```yaml
cluster:
  minerva:
    selector:
      users:
        - "**"
```

---

##### **`tags`**

**Description:** The `tags` attribute specifies a list of tags. The cluster is accessible exclusively to users who possess specific tags.

| **Data Type**     | **Requirement** | **Default Value** | **Possible Value**         |
| ----------------- | -------------- | ------------------ | --------------------------- |
| list of strings   | optional       | none               | any valid tag or pattern    |

**Additional Information:** Multiple users can be specified using AND/OR Logical Rules. To know more, click [here](/resources/policy/rules_for_and_or_relationship/).<br>

**Example Usage:**<br>
```yaml
cluster:
  minerva:
    selector:
      tags:
        - alpha
        - beta
```

---


##### **`sources`**

**Description:** the `sources` attribute specifies sources that can redirect queries to Cluster.

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

##### **`match`**

**Description:** The `match` attribute specifies the match condition.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| string | mandatory | any | any/all |

**Additional Information:** 
- `any` - must match at least one tag
- `all` - must match all tags<br>

**Example Usage:**<br>
```yaml
cluster:
  minerva:
    selector:
      match: any
```
---

##### **`priority`**

**Description:** The `priority` attribute specifies the priority level. Workloads will be redirected to Cluster with a lower priority level (inverse relationship).

| **Data Type** | **Requirement** | **Default Value** | **Possible Value**     |
| ------------- | -------------- | ------------------ | ----------------------- |
| integer       | mandatory      | 10                 | any value between 1-5000 |

**Example Usage:**<br>
```yaml
cluster:
  minerva:
    selector:
      priority: 10
```

---

### **`nats`**

**Description:** The `nats` section defines configurations for NATS Cluster.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------ | ------------------- |
| mapping       | mandatory      | none               | none               |

**Example Usage:**<br>
```yaml
cluster:
  nats:
    replicas: 5 
    volumeType: newone 
    volumeSize: 30mi 
    maxConnections: 4 
    roles: 
      - name: newrole 
        permissions: 
          publish: 
            - alpha
            - beta
          subscribe: 
            - newone
            - develop
          allow_responses: true
```

---

#### **`replicas`**

**Description:** The `replicas` attribute specifies the number of NATS Cluster replicas.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| integer | mandatory | 1 | positive integer |

**Example Usage:**<br>
```yaml
cluster:
  nats:
    replicas: 5
```

---

#### **`volumeType`**

**Description:** The `volumeType` attribute specifies the volume type for NATS.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| string | mandatory | none | valid string |

**Example Usage:**<br>
```yaml
cluster:
  nats:
    volumeType: newone
```

---

##### **`volumeSize`**

**Description:** The `volumeSize` attribute specifies the volume size for NATS.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| string | mandatory | none | valid string |

**Example Usage:**<br>
```yaml
cluster:
  nats:
    volumeSize: 30mi
```

---

##### **`maxConnections`**

**Description:** The `maxConnections` attribute specifies the maximum number of NATS connections.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| integer | mandatory | 1 | positive integer |

**Example Usage:**<br>
```yaml
cluster:
  nats:
    maxConnections: 2
```
---

##### **`roles`**

**Description:** The `roles` attribute defines roles and permissions for NATS.

Each role includes the following attributes:

- **`name`**: The role name.
- **`permissions`**: The permissions for the role, including `publish`, `subscribe`, and `allow_responses`.

**Example Usage:**<br>
```yaml
cluster:
  nats:
    roles:
      - name: newrole
        permissions:
          publish:
            - alpha
            - beta
          subscribe:
            - newone
            - develop
        allow_responses: true
```

---

### **`jupyterHub`**

**Description:** The `jupyterHub` section defines configurations for JupyterHub.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------ | ------------------- |
| mapping       | mandatory      | none               | none               |

**Example Usage:**<br>

```yaml
cluster:
  jupyterHub:
    ingress: 
      enabled: true
      path: /strip/
      stripPath: false
      noAuthentication: true
      appDetailSpec: random
      apiDetailSpec: random
    oidcConfig: 
      clientId: hellow 
      clientSecret: delta
    storageClass: alpha
    singleUserConfig:
      volumeCapacity: alpha 
```

---

#### **`ingress`**

**Description:** The `ingress` section specifies configurations for the JupyterHub ingress.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| `enabled` | boolean | optional | true | true or false |
| `path` | string | optional | none | valid path |
| `stripPath` | boolean | optional | false | true or false |
| `noAuthentication` | string | optional | true | true or false |
| `appDetailSpec` | string | optional | random | json spec |

**Example Usage:**<br>
```yaml
cluster:
  jupyterHub:
    ingress:
      enabled: true
      path: /strip/
      stripPath: false
      noAuthentication: true
      appDetailSpec: {}
```

---

#### **`oidcConfig`**

**Description:** The `oidcConfig` section specifies OIDC (OpenID Connect) configurations for JupyterHub.

| **Attribute** | **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- | ----|
| `clientId` | string | mandatory | none | valid string |
| `clientSecret` | string | mandatory | none | valid string |

**Example Usage:**<br>
```yaml
cluster:
  jupyterHub:
    oidcConfig:
      clientId: hellow
      clientSecret: delta
```

---

#### **`storageClass`**

**Description:** The `storageClass` attribute specifies the storage class for JupyterHub.

| **Data Type** | **Requirement**| **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| string | mandatory | none | valid string |

**Example Usage:**<br>
```yaml
cluster:
  jupyterHub:
    storageClass: alpha
```
---

#### **`singleUserConfig`**

**Description:** The `singleUserConfig` section specifies configurations for single users in JupyterHub.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| mapping | mandatory | none | none |

**Example Usage:**<br>
```yaml
cluster:
  jupyterHub:
    singleUserConfig:
      volumeCapacity: alpha
```

---

##### **`volumeCapacity`**

**Description:** The `volumeCapacity` attribute specifies the volume capacity for single users.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| string | mandatory | alpha | valid string |

**Example Usage:**<br>
```yaml
cluster:
  jupyterHub:
    singleUserConfig:
      volumeCapacity: alpha
```