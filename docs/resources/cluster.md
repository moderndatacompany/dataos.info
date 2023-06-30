# Cluster

In DataOS, a Cluster is a Primitive/resource that encompasses a set of computational resources and configurations used to run data engineering and analytics tasks. A Cluster is powered by a [Compute](./compute.md), another resource which provides the necessary processing power for the workloads executed on the Cluster.

<aside>

🗣️ To establish a Cluster, `roles:id:operator` tag is required. If you do not possess this tag, contact the DataOS administrator within your organization or any other individual with `roles:id:operator` tag to grant you the tag.

</aside>

![Diagrammatic representation of a Cluster ](./cluster/add_a_heading.svg)

<center><i>Diagrammatic representation of a Cluster</i></center>

DataOS primarily has just one type of Cluster, known as "Minerva.” For exploratory, querying, and ad-hoc analytics workloads, Minerva Clusters can be created and attached to the desired Compute. DataOS provides flexibility to connect Compute of different configurations with different Minerva Clusters. Multiple such clusters can be made of diverse configurations to meet various analytics requirements.

A Cluster refers to a Compute, which is essentially a node pool of homogenous Virtual Machines (VMs) belonging to the same cloud provider. All VMs (or nodes) within a node pool should have the same CPU, RAM, Storage Capacity, Network Protocols, and Storage Drive Types. 

As an example, a recommended minimum specification could be:

<center>

| CPU | RAM | Hard Disk | Type of Storage |
| --- | --- | --- | --- |
| 16 cores | 128 GB | 2 TB | Local Storage |

</center>

However, these specifications should be adjusted based on the workloads and amount of data being processed. 

## Syntax of a Cluster YAML

```yaml
version: v1 
name: minrevanew 
type: cluster 
description: a minerva cluster that changes resources and replicas 
tags: 
  - cluster
  - minerva
cluster: 
  compute: query-default 
  runAsUser: minerva-cluster 
  maintenance: 
    restartCron: '13 1 */2 * *' 
    scalingCrons: 
    - cron: '5/10 * * * *' 
      replicas: 3 
      resources: 
        limits: 
          cpu: 1000m 
          memory: 2Gi 
        requests: 
          cpu: 800m 
          memory: 1Gi 
    - cron: '10/10 * * * *' 
      replicas: 1 
      resources: 
        limits: 
          cpu: 3000m 
          memory: 7Gi 
        requests: 
          cpu: 1500m 
          memory: 3Gi 
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

## Creating a Cluster within DataOS

Within DataOS, we can create a Cluster via two mechanisms: either by creating a YAML file and applying it via CLI or using the Operation App UI. Check out the pages below to explore how you create a cluster via these two methods.

[Creating a Cluster Using CLI ](./cluster/creating_a_cluster_using_cli.md)

[Creating Cluster Using Operations App UI ](./cluster/creating_cluster_using_operations_app_ui.md)

[Cluster Maintenance ](./cluster/cluster_maintenance.md)

# Building Blocks of Cluster

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
| restartCron | By inputting a cron string into this designated field, Poros will restart the cluster based on the specified schedule.  | restartCron: '13 1 */2 * *’ | NA | A valid cron string | To know more, click https://www.notion.so/Cluster-Maintenance-8b9a27662cbc4f53a664eacfe4b7d88d?pvs=21. | Optional |
| scalingCrons | Poros can horizontally and/or vertically scale the cluster based on the provided schedules by specifying the cron, replicas, and/or resources. | # Horizontal Scaling
cluster:
maintenance:
scalingCrons:
- cron: '5/10 * * * *'
replicas: 3
- cron: '10/10 * * * *'
replicas: 0 | NA | The corn should be valid and the value of replicas must be non-negative. | A scalingCron overrides the default provided replicas and/or resources in a cluster like minerva while in an "active" cron window. To know more, click https://www.notion.so/Cluster-Maintenance-8b9a27662cbc4f53a664eacfe4b7d88d?pvs=21. | Optional |
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