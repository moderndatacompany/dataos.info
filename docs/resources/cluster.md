# Cluster

The Cluster Resource in DataOS is a fundamental Resource that encompasses a set of computational resources and configurations necessary for executing data engineering and analytics tasks. It relies on the [Compute](./compute.md) Resource, which provides the required processing power for the workloads executed within the Cluster. 

By decoupling compute and storage, the Cluster Resource facilitates flexibility and scalability. It can be provisioned [on-demand](./cluster/on_demand_computing.md), allowing for efficient allocation of resources based on workload-specific requirements.

<aside style="padding:15px; border-radius:5px;">

To establish a Cluster, it is mandatory to possess the roles:id:operator tag. If this tag is not present, contact the DataOS administrator or an individual with the roles:id:operator tag to obtain the required access.

</aside>


![Diagrammatic representation of a Cluster Resource](./cluster/add_a_heading.svg)

<center><i>Diagrammatic representation of a Cluster</i></center>

## Types of Clusters

DataOS supports a single type of Cluster known as "Minerva." Minerva Clusters are specifically designed to cater to exploratory, querying, and ad-hoc analytics workloads. These clusters can be created and connected to the desired Compute resource, providing the flexibility to connect different Compute configurations to various Minerva Clusters. Organizations can create multiple Minerva Clusters with diverse configurations to meet their specific analytics requirements effectively.

### **Minerva**

Minerva is an interactive query engine, based on Trino, meticulously crafted to efficiently execute analytical and exploratory workloads. It empowers data developers to effortlessly query diverse data sources using a unified, high-performance SQL interface. With Minerva, data analysis of substantial volumes becomes simpler, eliminating the need to handle intricate underlying configurations and data formats. 

To maximize performance, organizations can establish Minerva query engine clusters capable of effortlessly handling heavy workloads. These clusters enable the concurrent execution of memory-intensive, I/O-intensive, long-running, and CPU-intensive queries, ensuring efficient processing of diverse data scenarios. In cases where a single Minerva cluster proves insufficient, multiple clusters can be effortlessly created to cater to the distinct demands of different workloads. This workload distribution across clusters guarantees optimal performance and resource utilization.

#### **Querying Diverse Data Sources**

Minerva supports an extensive range of data sources, encompassing both traditional relational databases such as Oracle, PostgreSQL, MySQL, and Redshift, non-relational sources like Kafka and Cassandra, as well as object storages like Amazon S3, and Google Cloud Storage. This broad compatibility ensures seamless access to various data repositories, enabling comprehensive and integrated analyses.

#### **Query Execution Process**

When initiating a SQL query from sources such as Workbench, Atlas, Minerva-CLI, JDBC, or Lens, the query is seamlessly directed to the Gateway Service. The Gateway Service conducts a thorough analysis of the query and the associated tables, forwarding it to the Minerva clusters for execution. Furthermore, the Gateway Service facilitates data policy decisions, including Masking and Filtering policies. Once the analysis is completed, the query is seamlessly passed on to the Minerva cluster for execution.

#### **Data Policy Enforcement**

During the query execution process, Minerva collaborates with the DataOS policy manager, Heimdall. The query undergoes meticulous inspection to determine the applicable policy restrictions. Minerva actively enforces the relevant policies to ensure authorized stakeholders have secure access to the required data while safeguarding the organization's valuable data assets from unauthorized access.

#### **Managing Data Access Policies and Cluster Resources**

Minerva assumes the crucial role of executing data access policies based on user tags, proficiently managing cluster access, and providing users with comprehensive reports in case of query rejections or encountered exceptions during execution. By seamlessly handling these aspects, Minerva offers a robust and reliable environment for executing complex data queries while adhering to data governance and security protocols.

## Syntax of a Cluster YAML


## Creating a Cluster

Within DataOS, a Cluster resource can either be created either by applying the YAML using the DataOS Command Line Interface (CLI), or by using the Operations App's Graphical User Interface (GUI).

### **Creating a Cluster via CLI**

As Cluster is a Resource within DataOS. An instance of the Cluster can be created by configuring the Cluster Resource YAML and applying it via CLI.

#### **Building a Cluster Resource YAML** 

To create a Cluster resource, you need to configure the YAML file with the appropriate settings. The following sections explain the necessary configurations.

##### **Configuring the Resource Section**
A Cluster is a resource-type in DataOS. Below is the YAML configuration for the Resource Section:

```yaml
name: {{minervac}}
version: v1 
type: cluster 
tags: 
  - {{dataos:type:cluster}}
  - {{dataos:type:workspace-resource}}
description: {{this is a sample cluster configuration}}
owner: {{iamgroot}}
```

<center><i>Resource Section Configuration for a Cluster</i></center>

For detailed customization options and additional fields within the Resource Section, refer to the [Resource Grammar.](../resources/resource_grammar.md)

##### **Configuring the Cluster-specific Section**

The Cluster-specific Section contains configurations specific to the Cluster resource. The YAML syntax is provided below:

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
```
<center><i>Cluster-specific Section Configuration</i></center>

| Field | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| `cluster` | object | none | none | mandatory |
| `compute` | string | none | query-default or any other custom compute resource | mandatory |
| `runAsUser` | string | none | none | optional |
| `maintenance` | object | none | none | optional |
| `restartCrons` | string | none | any valid cron expression | optional |
| `scalingCrons` | object | none | none | optional |
| `cron` | string | none | any valid cron expression | optional |
| `replicas` | integer | 1 | positive integer | optional |
| `resources` | object | none | none | optional |
| `limits` | object | none | none | optional |
| `cpu` | string | requests: 100m, limits: 400m | number of cpu units in milliCPU(m) or cpu Core| optional |
| `memory` | string | requests: 100Mi, limits: 400Mi | memory in Mebibytes(Mi) or Gibibytes(Gi) | optional |
| `requests` | object | none | none | optional |

For additional information about attributes within the Cluster-specific Section, refer to the [link](./cluster/cluster_grammar.md)

##### **Configuring the Minerva-specific Section**

The Minerva-specific Section contains configurations specific to the Minerva Cluster. The YAML syntax is provided below:

```yaml
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

| Field | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| `minerva` | object | none | none | mandatory |
| `selector` | string | none | query-default or any other custom compute resource | mandatory |
| `users` | string | none | none | optional |
| `sources` | object | none | none | optional |
| `replicas` | string | none | any valid cron expression | optional |
| `match` | object | none | none | optional |
| `priority` | string | none | any valid cron expression | optional |
| `runAsApiKey` | integer | 1 | positive integer | optional |
| `runAsUser` | object | none | none | optional |
| `resources` | object | none | none | optional |
| `limits` | object | none | none | optional |
| `cpu` | string | requests: 100m, limits: 400m | number of cpu units in milliCPU(m) or cpu Core| optional |
| `memory` | string | requests: 100Mi, limits: 400Mi | memory in Mebibytes(Mi) or Gibibytes(Gi) | optional |
| `requests` | object | none | none | optional |
| `debug` | object | none | none | optional |
| `logLevel` | object | none | none | optional |
| `trinoLogLevel` | object | none | none | optional |
| `depots` | object | none | none | optional |
| `address` | object | none | none | optional |
| `properties` | object | none | none | optional |
| `catalogs` | object | none | none | optional |
| `name` | object | none | none | optional |
| `type` | object | none | none | optional |
| `properties` | object | none | none | optional |

For additional information about attributes within the Minerva-specific Section, refer to the [link](./cluster/cluster_grammar.md)


#### **Apply the Cluster YAML using DataOS CLI**

To create a Cluster resource, you need to use the apply command on the CLI. The apply command for Cluster is given below:

```bash
dataos-ctl apply -f <cluster-yaml-file-path>
```

### **Creating a Cluster Using Operations App**

The Operations App UI provides a convenient way to create a cluster in DataOS. 

> This functionality is available in versions above DataOS® centaurus-1.8.72.
> 

To create a cluster using the Operations App UI, follow these steps:

#### **Open the Operations App**

Open the Operations App by either accessing the graphical user interface (GUI) or using the command-line interface (CLI) with the following command:

```bash
dataos-ctl view -a operations
```

![Untitled](./cluster/creating_cluster_using_operations_app_ui/untitled.png)

#### **Navigate to the ‘Create Resource’ Section**

In the Operations App, click the '+ Create Resource' button. This action will open a window with various fields, as shown below:

![Untitled](./cluster/creating_cluster_using_operations_app_ui/untitled_1.png)

#### **Fill in the Required Fields**

Provide the necessary details in the required properties fields and click 'Create Cluster'. For more information on these properties, refer to the documentation here.

![Untitled](./cluster/creating_cluster_using_operations_app_ui/untitled_4.png)

#### **View the Created Cluster in the Operations App**

After clicking 'Create Cluster', a Cluster Resource will be created. You can observe the created cluster in the User Kernel section of the DataOS Operations App.

![Untitled](./cluster/creating_cluster_using_operations_app_ui/untitled_5.png)


[Cluster Maintenance ](./cluster/cluster_maintenance.md)

## Interacting with Minerva

Minerva offers multiple methods for interacting with its features and functionalities. The available options are provided below.

### **Minerva CLI**
The Minerva CLI is a command-line-based interactive interface that enables users to run queries effectively. To learn more about how to setup Minerva CLI, click [here](./cluster/minerva_client.md)

### **Workbench**

Workbench is a user interface (UI)-based query interface designed for data manipulation and exploration. Learn more about Workbench [here](../interfaces/workbench.md)

### **Connect via Tableau, SPSS and Power BI**

Users can leverage popular BI analytics platforms like Tableau, SPSS and Power BI to access data from DataOS via Minerva URL. To learn more about integration with Tableau, Power BI and SPSS, click [here](../interfaces/atlas/bi_tools.md#integrations-with-external-applications).

## Query Execution Optimization

To achieve enhanced performance and cost efficiency when working with analytical workloads in DataOS, it is crucial to optimize your query execution on Minerva. The following considerations can assist you in accelerating your queries. For detailed information and guidance, please refer to the provided link: [Query Optimization](./cluster/query_optimization.md)


## Performance Tuning

The Performance Tuning section is dedicated to enhancing the execution efficiency of queries within Minerva Clusters. It provides data developers with the means to attain optimal performance for analytical and exploratory workloads. By employing proven techniques for performance tuning, developers can streamline query execution, minimize resource consumption, and expedite data analysis. For more information, consult our [Performance Tuning Guide](./cluster/performance_tuning.md).

> Recommended [Cluster Configuration](./cluster/configuration_recommendations.md)
>

## Connectors Configuration

The Minerva query engine supports a wide range of connectors, including MySQL, PostgreSQL, Oracle, and Redshift. These connectors are configured in a YAML file, where they are mounted as catalogs. The catalogs store schemas and enable referencing of data sources through the respective connectors.

By utilizing these connectors, you can perform data analyses directly on the data sources without the need to transfer the data to DataOS. This approach allows for efficient querying and exploration of data, minimizing data movement. To know more, click [here](./cluster/connectors_configuration.md)



## Case Scenarios

Refer to the Cluster Resource [Case Scenarios](./cluster/case_scenarios.md) documentation for a comprehensive understanding of how Cluster can be utilized. It provides detailed examples and practical implementations to help data developers leverage the Cluster Resource efficiently.