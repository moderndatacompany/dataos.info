# Cluster

In DataOS, a Cluster is a Primitive/resource that encompasses a set of computational resources and configurations used to run data engineering and analytics tasks. A Cluster is powered by a [Compute](./compute.md), another resource which provides the necessary processing power for the workloads executed on the Cluster.

<aside style="padding:15px; border-radius:5px;">

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

For more information related to the Cluster-specific section YAML Configuration Field Reference, click [here.](./cluster/cluster_yaml_configuration_field_reference.md)

## Creating a Cluster within DataOS

Within DataOS, we can create a Cluster via two mechanisms: either by creating a YAML file and applying it via CLI or using the Operation App UI. Check out the pages below to explore how you create a cluster via these two methods.

[Creating a Cluster Using CLI ](./cluster/creating_a_cluster_using_cli.md)

[Creating Cluster Using Operations App UI ](./cluster/creating_cluster_using_operations_app_ui.md)

[Cluster Maintenance ](./cluster/cluster_maintenance.md)

---

# Cluster

In DataOS, a Cluster is a resource that encompasses a set of computational resources and configurations used to run data engineering and analytics tasks. A Cluster is powered by a [Compute](./compute.md), another resource which provides the necessary processing power for the workloads executed on the Cluster.

<aside style="padding:15px; border-radius:5px;">

🗣️ To establish a Cluster, `roles:id:operator` tag is required. If you do not possess this tag, contact the DataOS administrator within your organization or any other individual with `roles:id:operator` tag to grant you the tag.

</aside>

![Diagrammatic representation of a Cluster ](./cluster/add_a_heading.svg)

<center><i>Diagrammatic representation of a Cluster</i></center>

DataOS primarily has just one type of Cluster, known as "Minerva.” For exploratory, querying, and ad-hoc analytics workloads, Minerva Clusters can be created and attached to the desired Compute. DataOS provides flexibility to connect Compute of different configurations with different Minerva Clusters. Multiple such clusters can be made of diverse configurations to meet various analytics requirements.

A Cluster refers to a Compute, which is essentially a node pool of homogenous Virtual Machines (VMs) belonging to the same cloud provider. All VMs (or nodes) within a node pool should have the same CPU, RAM, Storage Capacity, Network Protocols, and Storage Drive Types.

## Minerva

Minerva is our query engine that will enable you to access your data for business insights. Minerva query engine gives users the ability to query various datasets through a single platform.

You can also run your analytical/exploration workloads with long-running queries. Minerva is an interactive query engine based on Trino.

Minerva makes it easy to analyze big data using SQL; you can query data across different databases without worrying about their configuration and data formats. It enables high-performance SQL access to various heterogeneous data sources, including traditional relational databases Oracle, PostgreSQL, MySQL, and Redshift, and other data sources such as Kafka and Cassandra.

Minerva enables you to run hundreds of memory, I/O, and CPU-intensive queries concurrently. For such a query load, a single Minerva cluster is insufficient, and you must create multiple clusters which can scale to hundreds of worker nodes while efficiently utilizing cluster resources.

Minerva enables you to concurrently run hundreds of memory, I/O, and CPU-intensive queries. For such query load, a single Minerva cluster is not sufficient, and you need to create multiple clusters. It can scale to hundreds of worker nodes while efficiently utilizing cluster resources.