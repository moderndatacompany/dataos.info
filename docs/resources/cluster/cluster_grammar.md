# Cluster Grammar

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
        - "**"
      sources: 
      - scanner/**
      - flare/**
    replicas: 2 
    match: '' 
    priority: '10' 
    runAsApiKey: <api-key> 
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
      - address: dataos://yakdevbq:default 
    catalogs: 
      - name: cache 
        type: memory 
        properties: 
          memory.max-data-per-node: "128MB" 
```

## Configuration Attributes

### **`cluster`**

**Description:** specifies the cluster-specific section<br>
**Data Type:** object<br>
**Requirement:** mandatory<br>
**Default Value:** none<br>
**Possible Value:** none<br>
**Example Usage:**<br>
```yaml
cluster:
  {}
```

### **`compute`**

**Description:** compute to be referred by the cluster<br>
**Data Type:** string<br>
**Requirement:** mandatory<br>
**Default Value:** none<br>
**Possible Value:** query-default or any other custom compute resource<br>
**Example Usage:**<br>
```yaml
compute: query-default
```

### **`runAsUser`**

**Description:** when the `runAsUser` field is configured with the UserID of the use-case assignee, it grants the authority to perform operations on behalf of that user.<br>
**Data Type:** string<br>
**Requirement:** optional<br>
**Default Value:** user-id of the user<br>
**Possible Value:** user-id of the use-case assignee<br>
**Example Usage:**<br>
```yaml
cluster:
  runAsUser: iamgroot
```

### **`maintenance`**

**Description:** this property specifies the cluster maintenance section<br>
**Data Type:** object<br>
**Requirement:** optional<br>
**Default Value:** none<br>
**Possible Value:** none<br>
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

### **`restartCron`**

**Description:** by specifying the cron expression into this designated field, Poros will restart the cluster based on the specified schedule.<br>
**Data Type:** string<br>
**Requirement:** optional<br>
**Default Value:** none<br>
**Possible Value:** a valid cron expression<br>
**Example Usage:**<br>
```yaml
restartCron: '13 1 */2 * *'
```

### **`scalingCrons`**

**Description:** Poros can horizontally and/or vertically scale the cluster based on the provided schedules by specifying the cron, replicas, and/or resources.<br>
**Data Type:** object<br>
**Requirement:** optional<br>
**Default Value:** none<br>
**Possible Value:** none<br>
**Example Usage:**<br>
```yaml
cluster:
  maintenance:
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

### **`cron`**

**Description:** Specifies the cron schedule for scaling tasks in the cluster.<br>
**Data Type:** string<br>
**Requirement:** mandatory<br>
**Default Value:** '5/10 * * * *'<br>
**Possible Value:** Any valid cron expression.<br>
**Example Usage:**<br>
```yaml
cluster:
  maintenance:
    scalingCrons:
    - cron: {{'5/10 * * * *'}}
```

### **`cluster.maintenance.scalingCrons.replicas`**

**Description:** Specifies the number of replicas for scaling tasks in the cluster.<br>
**Data Type:** integer<br>
**Requirement:** mandatory<br>
**Default Value:** 3<br>
**Possible Value:** Any valid positive integer.<br>
**Example Usage:**<br>
```yaml
cluster:
  maintenance:
    scalingCrons:
    - replicas: {{3}}
```

### **`cluster.maintenance.scalingCrons.resources`**

**Description:** Resource allocation configuration for scaling tasks in the cluster.<br>
**Data Type:** dictionary<br>
**Requirement:** mandatory<br>
**Default Value:** none<br>
**Possible Value:** Dictionary containing limits and requests configurations.<br>
**Example Usage:**<br>
```yaml
cluster:
  maintenance:
    scalingCrons:
    - resources:
        limits:
          cpu: {{1000m}}
          memory: {{2Gi}}
        requests:
          cpu: {{800m}}
          memory: {{1Gi}}
```

### **`cluster.maintenance.scalingCrons.resources.limits`**

**Description:** Specifies the resource limits for scaling tasks in the cluster.<br>
**Data Type:** dictionary<br>
**Requirement:** mandatory<br>
**Default Value:** none<br>
**Possible Value:** Dictionary containing CPU and memory limits.<br>
**Example Usage:**<br>
```yaml
cluster:
  maintenance:
    scalingCrons:
    - resources:
        limits:
          cpu: {{1000m}}
          memory: {{2Gi}}
```

### **`cluster.maintenance.scalingCrons.resources.limits.cpu`**

**Description:** Specifies the CPU limit for scaling tasks in the cluster.<br>
**Data Type:** string<br>
**Requirement:** mandatory<br>
**Default Value:** 1000m<br>
**Possible Value:** Any valid string representing CPU limit.<br>
**Example Usage:**<br>
```yaml
cluster:
  maintenance:
    scalingCrons:
    - resources:
        limits:
          cpu: {{1000m}}
```

### **`cluster.maintenance.scalingCrons.resources.limits.memory`**

**Description:** Specifies the memory limit for scaling tasks in the cluster.<br>
**Data Type:** string<br>
**Requirement:** mandatory<br>
**Default Value:** 2Gi<br>
**Possible Value**:** Any valid string representing memory limit.<br>
**Example Usage:**<br>
```yaml
cluster:
  maintenance:
    scalingCrons:
    - resources:
        limits:
          memory: {{2Gi}}
```

### **`cluster.maintenance.scalingCrons.resources.requests`**

**Description:** Specifies the resource requests for scaling tasks in the cluster.<br>
**Data Type:** dictionary<br>
**Requirement:** mandatory<br>
**Default Value:** none<br>
**Possible Value:** Dictionary containing CPU and memory requests.<br>
**Example Usage:**<br>
```yaml
cluster:
  maintenance:
    scalingCrons:
    - resources:
        requests:
          cpu: {{800m}}
          memory: {{1Gi}}
```

### **`cluster.maintenance.scalingCrons.resources.requests.cpu`**

**Description:** Specifies the CPU request for scaling tasks in the cluster.<br>
**Data Type:** string<br>
**Requirement:** mandatory<br>
**Default Value:** 800m<br>
**Possible Value:** Any valid string representing CPU request.<br>
**Example Usage:**<br>
```yaml
cluster:
  maintenance:
    scalingCrons:
    - resources:
        requests:
          cpu: {{800m}}
```

### **`cluster.maintenance.scalingCrons.resources.requests.memory`**

**Description:** Specifies the memory request for scaling tasks in the cluster.<br>
**Data Type:** string<br>
**Requirement:** mandatory<br>
**Default Value:** 1Gi<br>
**Possible Value:** Any valid string representing memory request.<br>
**Example Usage:**<br>
```yaml
cluster:
  maintenance:
    scalingCrons:
    - resources:
        requests:
          memory: {{1Gi}}
```

### **`cluster.minerva`**

**Description:** Configuration for the Minerva component in the cluster resource.<br>
**Data Type:** dictionary<br>
**Requirement:** mandatory<br>
**Default Value:** none<br>
**Possible Value:** Dictionary containing various Minerva configurations.<br>
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
    replicas: 2
    match: ''
    priority: '10'
    runAsApiKey: <api-key>
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
      - address: dataos://yakdevbq:default
    catalogs:
      - name: cache
        type: memory
        properties:
          memory.max-data-per-node: "128MB"
```

### **`cluster.minerva.selector`**

**Description:** Configuration for the Minerva selector in the cluster resource.<br>
**Data Type:** dictionary<br>
**Requirement:** mandatory<br>
**Default Value:** none<br>
**Possible Value:** Dictionary containing user and source selectors.<br>
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

### **`cluster.minerva.selector.users`**

**Description:** Specifies the users for Minerva selector in the cluster resource.<br>
**Data Type:** list of strings<br>
**Requirement:** mandatory<br>
**Default Value:** None<br>
**Possible Value:** List of strings representing user selectors.<br>
**Example Usage:**<br>
```yaml
cluster:
  minerva:
    selector:
      users:
        - "**"
```

### **`cluster.minerva.selector.sources`**

**Description:** Specifies the sources for Minerva selector in the cluster resource.<br>
**Data Type:** list of strings<br>
**Requirement:** mandatory<br>
**Default Value:** None<br>
**Possible Value:** List of strings representing source selectors.<br>
**Example Usage:**<br>
```yaml
cluster:
  minerva:
    selector:
      sources:
      - scanner/**
      - flare/**
```

### **`cluster.minerva.replicas`**

**Description:** Specifies the number of replicas for the Minerva component in the cluster resource.<br>
**Data Type:** integer<br>
**Requirement:** mandatory<br>
**Default Value:** 2<br>
**Possible Value:** Any valid positive integer.<br>
**Example Usage:**<br>
```yaml
cluster:
  minerva:
    replicas: 2
```

### **`cluster.minerva.match`**

**Description:** Specifies the match configuration for the Minerva component in the cluster resource.<br>
**Data Type:** string<br>
**Requirement:** mandatory<br>
**Default Value:** ''<br>
**Possible Value:** Any valid string.<br>
**Example Usage:**<br>
```yaml
cluster:
  minerva:
    match: ''
```

### **`cluster.minerva.priority`**

**Description:** Specifies the priority for the Minerva component in the cluster resource.<br>
**Data Type:** string<br>
**Requirement:** mandatory<br>
**Default Value:** '10'<br>
**Possible Value:** Any valid string.<br>
**Example Usage:**<br>
```yaml
cluster:
  minerva:
    priority: '10'
```

### **`cluster.minerva.runAsApiKey`**

**Description:** Specifies the API key for the Minerva component in the cluster resource to run as.<br>
**Data Type:** string<br>
**Requirement:** mandatory<br>
**Default Value:** \<api-key\><br>
**Possible Value:** Any valid string representing an API key.<br>
**Example Usage:**<br>
```yaml
cluster:
  minerva:
    runAsApiKey: <api-key>
```

### **`cluster.minerva.runAsUser`**

**Description:** Specifies the user for the Minerva component in the cluster resource to run as.<br>
**Data Type:** string<br>
**Requirement:** mandatory<br>
**Default Value:** iamgroot<br>
**Possible Value:** Any valid string.<br>
**Example Usage:**<br>
```yaml
cluster:
  minerva:
    runAsUser: iamgroot
```

### **`cluster.minerva.resources`**

**Description:** Resource allocation configuration for the Minerva component in the cluster resource.<br>
**Data Type:** dictionary<br>
**Requirement:** mandatory<br>
**Default Value:** none<br>
**Possible Value:** Dictionary containing limits and requests configurations.<br>
**Example Usage:**<br>
```yaml
cluster:
  minerva:
    resources:
      limits:
        cpu: 4000m
        memory: 8Gi
      requests:
        cpu: 1200m
        memory: 2Gi
```

### **`cluster.minerva.resources.limits`**

**Description:** Specifies the resource limits for the Minerva component in the cluster resource.<br>
**Data Type:** dictionary<br>
**Requirement:** mandatory<br>
**Default Value:** none<br>
**Possible Value:** Dictionary containing CPU and memory limits.<br>**Example Usage:**<br>
```yaml
cluster:
  minerva:
    resources:
      limits:
        cpu: 4000m
        memory: 8Gi
```

### **`cluster.minerva.resources.limits.cpu`**

**Description:** Specifies the CPU limit for the Minerva component in the cluster resource.<br>
**Data Type:** string<br>
**Requirement:** mandatory<br>
**Default Value:** 4000m<br>
**Possible Value:** Any valid string representing CPU limit.<br>
**Example Usage:**<br>
```yaml
cluster:
  minerva:
    resources:
      limits:
        cpu: 4000m
```

### **`cluster.minerva.resources.limits.memory`**

**Description:** Specifies the memory limit for the Minerva component in the cluster resource.<br>
**Data Type:** string<br>
**Requirement:** mandatory<br>
**Default Value:** 8Gi<br>
**Possible Value:** Any valid string representing memory limit.<br>
**Example Usage:**<br>
```yaml
cluster:
  minerva:
    resources:
      limits:
        memory: 8Gi
```

### **`cluster.minerva.resources.requests`**

**Description:** Specifies the resource requests for the Minerva component in the cluster resource.<br>
**Data Type:** dictionary<br>
**Requirement:** mandatory<br>
**Default Value:** none<br>
**Possible Value:** Dictionary containing CPU and memory requests.<br>
**Example Usage:**<br>
```yaml
cluster:
  minerva:
    resources:
      requests:
        cpu: 1200m
        memory: 2Gi
```

### **`cluster.minerva.resources.requests.cpu`**

**Description:** Specifies the CPU request for the Minerva component in the cluster resource.<br>
**Data Type:** string<br>
**Requirement:** mandatory<br>
**Default Value:** 1200m<br>
**Possible Value:** Any valid string representing CPU request.<br>
**Example Usage:**<br>
```yaml
cluster:
  minerva:
    resources:
      requests:
        cpu: 1200m
```

### **`cluster.minerva.resources.requests.memory`**

**Description:** Specifies the memory request for the Minerva component in the cluster resource.<br>
**Data Type:** string<br>
**Requirement:** mandatory<br>
**Default Value:** 2Gi<br>
**Possible Value:** Any valid string representing memory request.<br>
**Example Usage:**<br>
```yaml
cluster:
  minerva:
    resources:
      requests:
        memory: 2Gi
```

### **`cluster.minerva.debug`**

**Description:** Debug configuration for the Minerva component in the cluster resource.<br>
**Data Type:** dictionary<br>
**Requirement:** mandatory<br>
**Default Value:** none<br>
**Possible Value:** Dictionary containing logLevel and trinoLogLevel configurations.<br>
**Example Usage:**<br>
```yaml
cluster:
  minerva:
    debug:
      logLevel: INFO
      trinoLogLevel: ERROR
```

### **`cluster.minerva.debug.logLevel`**

**Description:** Specifies the log level for the Minerva component in the cluster resource.<br>
**Data Type:** string<br>
**Requirement:** mandatory<br>
**Default Value:** INFO<br>
**Possible Value:** Any valid string representing the log level.<br>
**Example Usage:**<br>
```yaml
cluster:
  minerva:
    debug:
      logLevel: INFO
```

### **`cluster.minerva.debug.trinoLogLevel`**

**Description:** Specifies the Trino log level for the Minerva component in the cluster resource.<br>
**Data Type:** string<br>
**Requirement:** mandatory<br>
**Default Value:** ERROR<br>
**Possible Value:** Any valid string representing the Trino log level.<br>
**Example Usage:**<br>
```yaml
cluster:
  minerva:
    debug:
      trinoLogLevel: ERROR
```

### **`cluster.minerva.depots`**

**Description:** List of depots for the Minerva component in the cluster resource.<br>
**Data Type:** list of dictionaries<br>
**Requirement:** mandatory<br>
**Default Value:** none<br>
**Possible Value:** List of dictionaries containing depot configurations.<br>
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
      - address: dataos://yakdevbq:default
```

### **`cluster.minerva.depots.address`**

**Description:** Specifies the address for a depot in the Minerva component of the cluster resource.<br>
**Data Type:** string<br>
**Requirement:** mandatory<br>
**Default Value:** None<br>
**Possible Value:** Any valid string representing the depot address.<br>
**Example Usage:**<br>
```yaml
cluster:
  minerva:
    depots:
      - address: dataos://icebase:default
```

### **`cluster.minerva.depots.properties`**

**Description:** Additional properties for a depot in the Minerva component of the cluster resource.<br>
**Data Type:** dictionary<br>
**Requirement:** mandatory<br>
**Default Value:** none<br>
**Possible Value:** Dictionary containing various depot properties.<br>
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
```

### **`cluster.minerva.catalogs`**

**Description:** List of catalogs for the Minerva component in the cluster resource.<br>
**Data Type:** list of dictionaries<br>
**Requirement:** mandatory<br>
**Default Value:** none<br>
**Possible Value:** List of dictionaries containing catalog configurations.<br>
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

### **`cluster.minerva.catalogs.name`**

**Description:** Specifies the name of a catalog in the Minerva component of the cluster resource.<br>
**Data Type:** string<br>
**Requirement:** mandatory<br>
**Default Value:** None<br>
**Possible Value:** Any valid string representing the catalog name.<br>
**Example Usage:**<br>
```yaml
cluster:
  minerva:
    catalogs:
      - name: cache
```

### **`cluster.minerva.catalogs.type`**

**Description:** Specifies the type of a catalog in the Minerva component of the cluster resource.<br>
**Data Type:** string<br>
**Requirement:** mandatory<br>
**Default Value:** None<br>
**Possible Value:** Any valid string representing the catalog type.<br>
**Example Usage:**<br>
```yaml
cluster:
  minerva:
    catalogs:
      - type: memory
```

### **`cluster.minerva.catalogs.properties`**

**Description:** Additional properties for a catalog in the Minerva component of the cluster resource.<br>
**Data Type:** dictionary<br>
**Requirement:** mandatory<br>
**Default Value:** none<br>
**Possible Value:** Dictionary containing various catalog properties.<br>
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

### **`cluster.minerva.catalogs.properties.memory.max-data-per-node`**

**Description:** Specifies the maximum data per node for a catalog in the Minerva component of the cluster resource.<br>
**Data Type:** string<br>
**Requirement:** mandatory<br>
**Default Value:** "128MB"<br>
**Possible Value:** Any valid string representing the maximum data per node.<br>
**Example Usage:**<br>
```yaml
cluster:
  minerva:
    catalogs:
      - properties:
          memory.max-data-per-node: "128MB"
```


| Property | Description | Example | Default Value | Possible Value | Rules/ Additional Details | Field (Optional / Mandatory) |
| --- | --- | --- | --- | --- | --- | --- |
| version | Manifest Version. It allows iteration on the schema.  | version: v1  | NA | v1 | Configure all the properties according to the manifest version. Currently, it's v1. | Mandatory |
| name | Defines the name of the resource (Here, it’s the name of the cluster) | name: query-default | runnable-default,query-default | Any string that conforms to the rule given in the next cell. | The name must be less than 48 characters and conform to the following regex: [a-z]([a-z0-9]*) | Mandatory |
| type | Resource type is declared here. In the current case, it’s a cluster. | type: cluster | NA | Any of the available resources in DataOS | The name of the primitive/resource should be only in lowercase characters. Else it will throw an error. | Mandatory |
| description | Text describing the Cluster. | description: default query compute | NA | Any string | There is no limit on the length of the string | Optional |
| tags | Tags are arrays of strings. These are attributes and keywords. They are used in access control and for quick searches within Metis. | tags:
  - Connect
  - Customer | NA | NA | The tags are case-sensitive, so Compute and COMPUTE will be different tags. There is no limit on the length of the tag.  | Optional |
| cluster | Cluster section | cluster:
  {} | NA | NA | NA | Mandatory |
| compute | Compute to be referred within the Cluster. | compute:runnable-default | NA | runnable-default, query-default, gpu, or any other custom compute that you have created | NA | Mandatory |
| runAsUser | UserID of the use case assignee. | runAsUser: minerva-cluster | NA | UserID of Use Case Assignee | Must be a valid UserID. | Optional |
| runAsApiKey | This property allows a user to assume the identity of another user through the provision of the latter's API key. | runAsApiKey: <api-key> | NA | DataOS API Key  | To get API Key execute, dataos-ctl apikey get in the Terminal after logging into DataOS. | Mandatory |
| maintenance | Cluster Maintenance Section | maintenance:
  {} | NA | NA | NA | Optional |
| restartCron | By inputting a cron string into this designated field, Poros will restart the cluster based on the specified schedule.  | restartCron: '13 1 */2 * *’ | NA | A valid cron string | To know more, click [here.](../cluster/cluster_maintenance.md) | Optional |
| scalingCrons | Poros can horizontally and/or vertically scale the cluster based on the provided schedules by specifying the cron, replicas, and/or resources. | # Horizontal Scaling
cluster:
maintenance:
scalingCrons:
- cron: '5/10 * * * *'
replicas: 3
- cron: '10/10 * * * *'
replicas: 0 | NA | The corn should be valid and the value of replicas must be non-negative. | A scalingCron overrides the default provided replicas and/or resources in a cluster like minerva while in an "active" cron window. To know more, click [here](../cluster/cluster_maintenance.md). | Optional |
| minerva | Minerva Section | minerva: 
  {} | NA | NA | NA | Mandatory |
| selector | Selector Section | selector: 
  {} | NA | NA | NA | Optional |
| users | Specify a user identified by a tag. They can be a group of tags defined as an array.  | users: 
- "**”  | NA | A valid subset of all available users within DataOS | NA | Mandatory |
| tags | The Cluster is accessible exclusively to users who possess specific tags. | tags:
- "**" | NA | Any valid tag or pattern | NA | Optional |
| sources | Sources that can redirect queries to Cluster. | sources: 
- scanner/**
- flare/** | NA | List of all available sources. For all sources, specify “**”. | NA | Mandatory |
| replicas | Number of replicas of the Cluster | replicas: 2 | NA | A minimum value of 1 and a maximum value of 4 | NA | Mandatory |
| match | You can specify two operators here. any (must match at least one tag) and all(match all tags) | match: ‘’ | NA | NA | any, all | Optional |
| priority | Priority Level. Workloads will be redirected to Cluster with a lower priority level (inverse relationship). | priority: '10’ | priority: '100’ | Any value between 1 and 5000.  | If two Clusters have the same priority, the one created earlier will be considered of foremost importance.  | Optional |
| resources | The CPU and memory resources, to be allocated. This includes the requested ones as well as the maximum limits. | resources:
  limits:
    cpu: 4000m
    memory: 8Gi
  requests:
    cpu: 2000m
    memory: 4Gi | resources:
  limits:
    cpu: NA
    memory: NA
  requests:
    cpu: NA
    memory: NA | resources:
  limits:
    cpu: # Maximum value of 6000m
    memory: # Maximum value of 6Gi
  requests:
    cpu: # Maximum value of 6000m
    memory: # Maximum value of 6Gi | limits: The maximum limit of the CPU and memory
requests: The maximum requested CPU and memory | Mandatory (All Properties) |
| debug | The debug level. This includes both the logLevel and the trinoLoglevel | debug:
  logLevel: INFO
  trinoLogLevel: ERROR | debug:
  logLevel: INFO
  trinoLogLevel: ERROR | debug:
  logLevel: INFO/DEBUG/ERROR
  trinoLogLevel: ERROR/DEBUG/ERROR | logLevel: A log level is a piece of information from a given log message that distinguishes log events from each other. 
trinoLogLevel: This log level is specific to Trino. | Optional (Both) |
| depots | Specification of sources to be queried. This includes only those sources ion which a depot can be created and support querying from Minerva Cluster.  | depots:
- address: dataos://icebase:default
properties:
hive.config.resources: ‘’
iceberg.compression-codec: ‘’
iceberg.file-format: ''
- address: dataos://gateway:default
- address: dataos://metisdb:default
- address: dataos://lensdb:default | NA | Any valid depot UDl address | NA | Optional |
| catalogs | In cases where it is not possible to create a depot for certain sources, but a Trino connector is available and supported, the specification of said sources can be performed here. | catalogs:
- name: cache
type: memory
properties:
memory.max-data-per-node: '128MB’ | NA | Trino connector specification should be valid. | NA | Optional |