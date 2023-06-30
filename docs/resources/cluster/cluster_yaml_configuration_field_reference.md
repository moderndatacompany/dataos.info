# Cluster-specific Section YAML Configuration Field Reference

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