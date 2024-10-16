---
title: Cluster
search:
  boost: 2
---

# :resources-cluster: Cluster

A Cluster in DataOS is a [Resource](/resources/) that encompasses a set of computational resources and configurations necessary for executing data engineering and analytics tasks. It relies on the [Compute](/resources/compute/) Resource, which provides the required processing power for the workloads executed within the Cluster. 

A Cluster Resource can be provisioned [on-demand](/resources/cluster/on_demand_computing/), allowing for efficient allocation of resources based on workload-specific requirements. This decoupling of computation and storage, facilitates flexibility, cost-efficiency and scalability.

<div class="grid cards" markdown>

-   :material-card-bulleted-settings-outline:{ .lg .middle } **How to create a Cluster Resource in DataOS?**

    ---

    Learn how to create a Cluster Resource in DataOS.

    [:octicons-arrow-right-24: Create a Cluster](#how-to-create-a-cluster-resource)


-   :material-list-box-outline:{ .lg .middle } **How to configure the manifest file of Cluster?**

    ---

    Discover how to configure the manifest file of a Cluster by adjusting its attributes.

    [:octicons-arrow-right-24: Cluster attributes](/resources/cluster/configurations/)

-   :material-network-pos:{ .lg .middle } **How to interact with a Cluster?**

    ---

    Understand how to interact with a Cluster in DataOS.
    
    [:octicons-arrow-right-24: Interacting with a Cluster](#interacting-with-clusters)

-   :material-content-duplicate:{ .lg .middle } **How to tune a Cluster's performance?**

    ---

    Explore how to tune a Cluster's performance in various scenarios.

    [:octicons-arrow-right-24:  Performance tuning](#performance-tuning)

</div>

<aside class="callout">
🗣️ To establish a Cluster, it is mandatory to possess the <code>roles:id:operator</code> tag. If this tag is not present, contact the DataOS Operator within your organization to assign you the specific use-case or the requisite tag to obtain the required access.
</aside>

<center>
  <div style="text-align: center;">
    <img src="/resources/cluster/cluster.png" alt="Diagrammatic representation of a Cluster Resource" style="width:80%; border:1px solid black;">
    <figcaption align="center"><i>Diagrammatic representation of a Cluster Resource</i></figcaption>
  </div>
</center>


## Query Engines on Clusters

Within a Cluster, a group of provisioned machines collaborates to process queries submitted to a query engine. DataOS supports two types of query engines:

- [Minerva](#minerva)
- [Themis](#themis)

These Clusters can be created and connected to the desired [Compute Resource](/resources/compute/). If a single Cluster is inadequate, multiple Clusters can be effortlessly created to accommodate the specific requirements of different workloads. Distributing workloads across clusters ensures optimal performance and resource utilization.

### **Minerva**

Minerva is an interactive static query engine, meticulously crafted to efficiently execute analytical and exploratory workloads. It empowers data developers to effortlessly query diverse data sources using a unified, high-performance SQL interface. With Minerva, data analysis of substantial data volumes becomes simpler, eliminating the need to handle intricate underlying configurations and data formats. 

To maximize performance, organizations can establish Minerva query engine clusters capable of effortlessly handling heavy workloads. These clusters enable the concurrent execution of memory-intensive, I/O-intensive, long-running, and CPU-intensive queries, ensuring efficient processing of diverse data scenarios. 

**Querying Diverse Data Sources**

Minerva supports an extensive range of data sources, encompassing both traditional relational databases such as Oracle, PostgreSQL, MySQL, and Redshift, non-relational sources like Kafka and Cassandra, as well as object storages like Amazon S3, and Google Cloud Storage. This broad compatibility ensures seamless access to various data sources, enabling comprehensive and integrated analyses. To know more about the various data sources supported by Minerva, click on the following link: [Connectors Configuration](/resources/cluster/connectors_configuration/).

**Query Execution Process**

When initiating a SQL query from sources such as Workbench, Minerva-CLI, JDBC, or Lens App UI, the query is seamlessly directed to the Minerva Gateway Service. The Gateway Service conducts a thorough analysis of the query and the associated tables, forwarding it to the Minerva Clusters for execution. Furthermore, the Gateway Service facilitates data policy decisions, including Masking and Filtering policies. Once the analysis is completed, the query is seamlessly passed on to the Minerva Cluster for execution.
<!-- 
**Managing Data Access Policies and Cluster Resources**

Minerva assumes the crucial role of executing access policies based on user tags, proficiently managing Cluster access, and providing users with comprehensive reports in case of query rejections or encountered exceptions during execution. By seamlessly handling these aspects, Minerva offers a robust and reliable environment for executing complex data queries while adhering to data governance and security protocols. -->

### **Themis**

Themis is an elastic SQL query engine optimized for fast, distributed querying across large datasets. As a modern JDBC server, Themis offers a comprehensive interface for various database management systems (DBMS), distinguishing itself through high performance, versatility, scalability, availability, and security measures, making it ideal for large-scale enterprise applications.

**Key Characteristics of Themis**

Themis excels in its domain with several notable features:

- **Elasticity**: In contrast to Minerva, which is a static query engine, Themis operates as an elastic query engine, adapting dynamically to varying workload demands.
- **Extensive Data Source Compatibility**: Themis supports a broad array of data sources, notably Hive, HBase, and Cassandra. Its compatibility extends to HDFS, Apache Hive, Kafka, and Cassandra, among others, streamlining the process of interfacing with diverse data sources.
- **Concurrent Processing and Scalability**: Designed with a multi-threaded architecture, Themis excels in demanding enterprise environments that require high concurrency and scalability. It is compatible with major big data frameworks, including Apache Hadoop, Spark, and Kubernetes.
- **Enhanced Security**: Themis incorporates Apache Hive's security features and supports advanced security protocols such as Kerberos, LDAP, and Active Directory, enabling straightforward integration with existing security infrastructures.
- **Optimized Performance**: Advanced caching and memory management techniques in Themis significantly enhance SQL query performance and efficiency.
- **JDBC and ODBC Connectivity**: Themis offers native JDBC and ODBC connectivity, facilitating straightforward integration with a range of programming languages and tools.
- **High Availability**: With inherent load balancing and failover mechanisms, Themis ensures consistent availability and reliability.
- **Efficient Memory Usage**: Its design prioritizes efficiency, resulting in a smaller memory footprint.

### **Comparative Analysis: Minerva vs. Themis**

Themis and Minerva, both SQL query engines, are designed for efficient, distributed querying in large datasets. The key differences are summarized in the table below:

| Feature | Minerva | Themis | Remarks |
| --- | --- | --- | --- |
| *Query Engine Type* | Static | Elastic | Minerva operates with a fixed allocation of resources, while Themis dynamically allocates resources based on workload demands. |
| *SQL Dialect* | TrinoSQL | SparkSQL | Different SQL dialects indicate compatibility with various data processing paradigms. |
| *Scalability* | Limited | High | Themis offers superior scalability compared to Minerva, accommodating fluctuating workloads efficiently. |
| *Resource Utilization* | Constant | Adaptive | Themis adjusts resource usage in real-time, unlike Minerva's consistent resource requirement. |
| *Performance in Variable Workloads* | Consistent | Optimal | Themis excels in environments with variable data queries, providing enhanced performance. |
| *Data Source Compatibility* | Basic | Extensive | Themis supports a wider range of data sources than Minerva, making it more versatile for diverse data environments. |
| *Security Features* | Standard | Advanced | Themis integrates more sophisticated security protocols, beneficial for environments with stringent security requirements. |
| *Concurrency Handling* | Moderate | High | Themis is designed to handle higher levels of concurrency, suitable for large-scale enterprise applications. |
| *Flexibility in Deployment* | Fixed | Flexible | Themis offers more flexibility in deployment, adapting to various big data platforms like Hadoop, Spark, and Kubernetes. |
| *Use Case Suitability* | Best for environments with predictable, consistent workloads. For example, predictable data processing needs, such as monthly financial reporting or static data analysis. | Ideal for dynamic, varying workloads and large-scale deployments. For example, dynamic environments such as e-commerce platforms, where real-time data analysis is crucial for customer behavior tracking, inventory management, and personalized recommendations. | Depending on the workload consistency and scale, the choice between Minerva and Themis can be determined. |

<!-- ## Structure of a Cluster manifest

<center>

![Cluster Structure](/resources/cluster/cluster_syntax.png)

</center>
<center><i>Structure of a Cluster manifest</i></center> -->

## How to create a Cluster Resource?

### **Prerequisites**

#### **Get access permission**

Before setting up a Cluster instance, ensure that you have the `roles:id:operator` tag assigned or the appropriate use case permissions granted by the DataOS Operator.

#### **Query-type Compute**

Ensure that a query-type Compute has been set up by the DataOS Operator before initiating the Cluster setup process. To learn more about Compute, click [here](/resources/compute/).

### **Setting up a Cluster**

To create a Cluster Resource within DataOS, you have two options:

1. **Using the DataOS Command Line Interface (CLI):** You can create a Cluster Resource by applying the Cluster manifest through the CLI. 

2. **Using the Operations App's Graphical User Interface (GUI):** Alternatively, you can create a Cluster Resource by utilizing the GUI in the Operations App.

=== "Using DataOS CLI"

    ### **Create a Cluster manifest** 

    In DataOS, users have the capability to instantiate Cluster Resources by creating manifest files (YAML configuration files) and applying them via the DataOS CLI. The code block below provides the sample Cluster manifests for the two different Cluster-types:

    ???tip "Themis Cluster manifest"

        ```yaml
        # Resource meta section (1)
        name: themiscluster
        version: v1
        type: cluster
        description: We are using this cluster to check the monitor and pager stuff with the help of themis cluster. 
        tags:
          - cluster
          - themis

        # Cluster-specific section (2)
        cluster:
          compute: query-default
          type: themis
        # Themis-specific section (3)
          themis:
            themisConf:  
              "kyuubi.frontend.thrift.binary.bind.host": "0.0.0.0"
              "kyuubi.frontend.thrift.binary.bind.port": "10101"
              driver:
                memory: '4096M'
              executor:
                memory: '4096M'
            depots:
              - address: dataos://icebase
        ``` 

    ???tip "Minerva Cluster manifest"

        ```yaml
        # Resource meta section
        name: minervacluster
        version: v1
        type: cluster
        description: We are using this cluster to check the monitor and pager stuff with the help of themis cluster. 
        tags:
          - cluster
          - themis

        # Cluster-specific section
        cluster:
          compute: query-default
          type: minerva

          # Minerva-specific section
          minerva:
            replicas: 1
            resources:
              limits:
                cpu: 2000m
                memory: 4Gi
              requests:
                cpu: 2000m
                memory: 4Gi
            debug:
              logLevel: INFO
              trinoLogLevel: ERROR
            depots:
              - address: dataos://icebase
        ``` 

    The structure of a Cluster Resource manifest encompasses the following sections:

    - [Resource Meta Section](#resource-meta-section)
    - [Cluster-specific Section](#cluster-specific-section)

    #### **Resource meta section**

    The Resource meta section is a standardized component across all DataOS Resource manifests, detailing essential metadata attributes necessary for Resource identification, classification, and management. This metadata is organized within the Poros Database. Below is the syntax for the Resource meta section:

    ```yaml
    name: ${{minervac}}
    version: v1 
    type: cluster 
    tags: 
      - ${{dataos:type:cluster}}
      - ${{dataos:type:workspace-resource}}
    description: ${{this is a sample cluster configuration}}
    owner: ${{iamgroot}}
    cluster: 
    ```

    <center><i>Resource meta section of a Cluster manifest file</i></center>

    For further details on each attribute, refer to the documentation: [Attributes of Resource-specific section](/resources/manifest_attributes/).

    #### **Cluster-specific section**

    The Cluster-specific Section contains configurations specific to the Cluster Resource-type. The YAML syntax is provided below:

    === "Basic configuration"

        The basic configuration of a manifest snippet includes only the essential attributes required for establishing a Cluster.

        === "Syntax"
            ```yaml
            cluster: 
              compute: ${{compute-name}}
              type: ${{cluster-type}}

              # Minerva/Themis-specific section
              minerva/themis: 
                # attributes specific to the Cluster-type
            ```

        === "Example"
            ```yaml
            cluster: 
              compute: query-default
              type: themis

              # Themis-specific section
              themis: 
                # attributes specific to the Themis Cluster-type
            ```

            | Field | Data Type | Default Value | Possible Value | Requirement |
            | --- | --- | --- | --- | --- |
            | [`cluster`](/resources/cluster/configurations/#cluster) | mapping | none | none | mandatory |
            | [`compute`](/resources/cluster/configurations/#compute) | string | none | query-default or any other query type custom Compute Resource | mandatory |
            | [`type`](/resources/cluster/configurations/#type) | string | none | minerva/themis | mandatory |

    === "Advanced configuration"

        The advanced configuration covers the full spectrum of attributes that can be specified within the Cluster-specific section a manifest for comprehensive customization.

        === "Syntax"

            ```yaml
            cluster: 
              compute: ${{compute-name}}
              type: ${{cluster-type}} 
              runAsUser: ${{run-as-user}} 
              maintenance: 
                restartCron: ${{restaart-cron-expression}} 
                scalingCrons: 
                - cron: ${{scalling-cron-expression}} 
                  replicas: ${{number-of-replicas}} 
                  resources: 
                    limits: 
                      cpu: ${{cpu-limits}} 
                      memory: ${{memory-limits}} 
                    requests: 
                      cpu: ${{cpu-requests}} 
                      memory: ${{memory-requests}}
              minerva/themis:
                # attributes specific to the Cluster-type
            ```

        === "Example"

            ```yaml
            cluster: 
              compute: query-default
              type: themis
              runAsUser: iamgroot
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
              themis:
                # attributes specific to the Themis Cluster-type
            ``` 

            <center><i>Cluster-specific Section Configuration</i></center>

            | Field | Data Type | Default Value | Possible Value | Requirement |
            | --- | --- | --- | --- | --- |
            | [`cluster`](/resources/cluster/configurations#cluster) | mapping | none | none | mandatory |
            | [`compute`](/resources/cluster/configurations#compute) | string | none | query-default or any other query type custom Compute Resource | mandatory |
            | [`runAsUser`](/resources/cluster/configurations#runasuser) | string | none | userid of the use case assignee | optional |
            | [`maintenance`](/resources/cluster/configurations#maintenance) | mapping | none | none | optional |
            | [`restartCron`](/resources/cluster/configurations#restartcron) | string | none | any valid cron expression | optional |
            | [`scalingCrons`](/resources/cluster/configurations#scalingcrons) | mapping | none | none | optional |
            | [`cron`](/resources/cluster/configurations#cron) | string | none | any valid cron expression | optional |
            | [`replicas`](/resources/cluster/configurations#replicas) | integer | 1 | positive integer | optional |
            | [`resources`](/resources/cluster/configurations#resources) | mapping | none | none | optional |
            | [`limits`](/resources/cluster/configurations#limits) | mapping | none | none | optional |
            | [`cpu`](/resources/cluster/configurations#cpu) | string | requests: 100m, limits: 400m | number of cpu units in milliCPU(m) or cpu Core| optional |
            | [`memory`](/resources/cluster/configurations#memory) | string | requests: 100Mi, limits: 400Mi | memory in Mebibytes(Mi) or Gibibytes(Gi) | optional |
            | [`requests`](/resources/cluster/configurations#requests) | mapping | none | none | optional |

    For additional information about attributes within the Cluster-specific section, refer to the link: [Attributes of Cluster-specific section.](/resources/cluster/configurations#cluster)

    For the two different types of Cluster the configuration varies, which are elucidated in the sections below:

    === "Minerva"

        The Minerva-specific Section contains configurations specific to the Minerva Cluster. The YAML syntax is provided below:

        ```yaml
        minerva: 
          replicas: ${{2}} 
          match: '' 
          priority: ${{'10'}} 
          runAsApiKey: ${{dataos api key}} 
          runAsUser: ${{iamgroot}} 
          resources: 
            limits: 
              cpu: ${{4000m}} 
              memory: ${{8Gi}} 
            requests: 
              cpu: ${{1200m}} 
              memory: ${{2Gi}} 
          debug: 
            logLevel: ${{INFO}} 
            trinoLogLevel: ${{ERROR}} 
          depots: 
            - address: ${{dataos://icebase:default}} 
              properties: 
                iceberg.file-format: ${{PARQUET}} 
                iceberg.compression-codec: ${{GZIP}} 
                hive.config.resources: ${{"/usr/trino/etc/catalog/core-site.xml"}} 
            - address: ${{dataos://yakdevbq:default}} 
          catalogs: 
            - name: ${{cache}} 
              type: ${{memory}} 
              properties: 
                memory.max-data-per-node: ${{"128MB"}} 

        ```

        Certainly, here's the table with only the attribute names and their corresponding data types, requirements, default values, and possible values:                                          


        | Field | Data Type | Default Value | Possible Value | Requirement |
        | --- | --- | --- | --- | --- |
        | [`minerva`](/resources/cluster/configurations#minerva) | mapping | none | none | mandatory |
        | [`replicas`](/resources/cluster/configurations#replicas) | integer | 1 | 1-4 | mandatory |
        | [`match`](/resources/cluster/configurations#match) | string | none | any/all | mandatory |
        | [`priority`](/resources/cluster/configurations#priority) | integer | 10 | 1-5000 | mandatory |
        | [`runAsApiKey`](/resources/cluster/configurations#runasapikey) | string | users dataos api key | any valid dataos api key | mandatory |
        | [`runAsUser`](/resources/cluster/configurations#runasuser) | string | none | userid of the use case assignee | optional |
        | [`resources`](/resources/cluster/configurations#resources) | mapping | none | none | optional |
        | [`limits`](/resources/cluster/configurations#limits) | mapping | none | none | optional |
        | [`cpu`](/resources/cluster/configurations#cpu) | string | requests: 100m, limits: 400m | number of cpu units in milliCPU(m) or cpu Core| optional |
        | [`memory`](/resources/cluster/configurations#memory) | string | requests: 100Mi, limits: 400Mi | memory in Mebibytes(Mi) or Gibibytes(Gi) | optional |
        | [`requests`](/resources/cluster/configurations#requests) | mapping | none | none | optional |
        | [`debug`](/resources/cluster/configurations#debug) | mapping | none | none | mandatory |
        | [`logLevel`](/resources/cluster/configurations#loglevel) | mapping | INFO | INFO/DEBUG/ERROR | optional |
        | [`trinoLogLevel`](/resources/cluster/configurations#trinologlevel) | mapping | INFO | INFO/DEBUG/ERROR | optional |
        | [`depots`](/resources/cluster/configurations#depots) | list of mappings | none | none | optional |
        | [`address`](/resources/cluster/configurations#address) | string | none | valid depot udl address | optional |
        | [`properties`](/resources/cluster/configurations#properties) | mapping | none | none | optional |
        | [`catalogs`](/resources/cluster/configurations#catalogs) | list of mappings | none | none | optional |
        | [`name`](/resources/cluster/configurations#name) | string | none | any valid string | optional |
        | [`type`](/resources/cluster/configurations#type) | string | none | oracle/memory/wrangler/redshift | mandatory |
        | [`properties`](/resources/cluster/configurations#properties_1) | mapping | none | valid connector properties | optional |

        For additional information about attributes above attributes, refer to the [Attributes of Minerva-specific section.](/resources/cluster/configurations#minerva)

    === "Themis"

        Attributes particular to the Themis Cluster are defined here. This includes configurations such as Pod Resources, Spark settings, Depot specifications, and Environment variables.

        Example YAML syntax for the Themis-specific section:

        ```yaml
        themis:
          resources: # Pod Resources specification 
            {}
          envs: # Environment variables
            {}
          themisConf: # Themis configurations
            {}
          spark:
            {} # Spark configuration
          depots:
            {} # Depots specification
        ```

        **Pod Resources**

        Specifies the requested and maximum CPU and memory limits for Pod Resources.

        ```yaml
        themis: # Themis mapping (mandatory)
          resources: # Pod Resources (optional)
            requests: # Requested CPU and memory resources (optional)
              cpu: ${{1000m}} # (optional)
              memory: ${{2Gi}} # (optional)
            limits: # Maximum limit of CPU and memory resources (optional)
              cpu: ${{2000m}} # (optional)
              memory: ${{4Gi}} # (optional)
        ```

        **Spark environment configuration**

        Details the memory size, cores, and other configurations for Spark drivers and executors.

        ```yaml
        themis: # Themis mapping (mandatory)
          spark:
            driver: # Spark driver memory and core configuration (mandatory)
              memory: ${{4096M}} # (mandatory)
              cores: ${{1}} # (mandatory)
            executor: # Spark executor memory, core, and instanceCount configuration (mandatory)
              memory: ${{4096M}} # (mandatory)
              cores: ${{1}} # (mandatory)
              instanceCount: ${{1}} # (mandatory)
              maxInstanceCount: ${{5}} # (mandatory)
            sparkConf: # Spark configurations (optional)
              ${{spark.dynamicAllocation.enabled: true}} 
        ```

        The list of Spark configuration that can be configured within this section are specified in the toggle below.

        <details>
            <summary>Spark Configurations</summary>
            The Spark Configuration can be specified within the <code>sparkConf</code> attribute. The list of spark configurations is provided below:
            <ul>
                <li><code>spark.eventLog.dir = location of folder/directory</code></li>
                <li><code>spark.ui.port = 4040</code></li>
                <li><code>spark.driver.memory=6g</code></li>
                <li><code>spark.driver.cores=2</code></li>
                <li><code>spark.driver.memoryOverhead=1g</code></li>
                <li><code>spark.executor.memory=4g</code></li>
                <li><code>spark.executor.cores=2g</code></li>
            </ul>
            <p>For more information, refer to the following <a href="https://spark.apache.org/docs/latest/configuration.html">link.</a></p>
        </details>

        **Depot specification**

        Defines the Depots targeted by the Themis Cluster.

        ```yaml
        themis: # Themis mapping (mandatory)
          depots: # mandatory
            - address: ${{dataos://icebase}} # Depot UDL address (mandatory)
              properties: # Depot properties (optional)
                ${{properties attributes}} 
        ```

        **Themis Configuration**

        Allows for additional key-value pair configurations specific to the Themis Cluster.

        ```yaml
        themis: # Themis mapping (mandatory)
          themisConf:  # Themis configuration specification (optional)
            ${{"kyuubi.frontend.thrift.binary.bind.host": "0.0.0.0"}} # (optional)
            ${{"kyuubi.frontend.thrift.binary.bind.port": "10101"}} # (optional)
        ```

        The list of the available Themis Cluster configurations is provided in the toggle below.

        <details>
            <summary>Themis Cluster configuration</summary>
            The Themis configuration can be supplied using the <code>themisConf</code> attribute. The configurations are provided below:
            <ul>
                <li><code>kyuubi.operation.incremental.collect=true</code> : To get paginated data.</li>
                <li><code>kyuubi.frontend.thrift.worker.keepalive.time=PT30S</code> : TTL for spark engine, this indicated that after 30 seconds of idle time spark engine is terminated.</li>
                <li><code>kyuubi.engine.hive.java.options</code> : The extra Java options for the Hive query engine</li>
                <li><code>kyuubi.frontend.thrift.worker.keepalive.time=PT1M</code> : Keep-alive time (in milliseconds) for an idle worker thread</li>
                <li><code>kyuubi.frontend.thrift.login.timeout=PT10S</code> : Timeout for Thrift clients during login to the thrift frontend service.</li>
                <li><code>kyuubi.metadata.cleaner.interval=PT30M</code> : The interval to check and clean expired metadata.</li>
                <li><code>kyuubi.metadata.max.age=PT72H</code> : The maximum age of metadata, the metadata exceeding the age will be cleaned.</li>
                <li><code>kyuubi.server.periodicGC.interval</code> : How often to trigger a garbage collection</li>
                <li><code>kyuubi.server.redaction.regex</code> : Regex to decide which Kyuubi contain sensitive information. When this regex matches a property key or value, the value is redacted from the various logs.</li>
            </ul>
            <p>For more information, refer to the following <a href="https://kyuubi.readthedocs.io/en/master/configuration/settings.html">link.</a></p>
        </details>


        **Environment Variables**

        Configures the Themis Cluster for various environments through key-value pair environment variables.

        ```yaml
        themis: # Themis mapping (mandatory)
          envs: # Environment variables (optional)
            ${{key-value pairs of environment variables}}
        ```


    ### **Apply the Cluster manifest**

    To create a Cluster Resource, you need to use the apply command on the CLI. The apply command for Cluster is given below:

    ```shell
    dataos-ctl resource apply -f ${{cluster-yaml-file-path}} -w ${{workspace name}}
    # Sample
    dataos-ctl resource apply -f dataproduct/themis-cluster.yaml -w curriculum
    ```

    ### **Verify Cluster creation**

    To ensure that your Cluster has been successfully created, you can verify it in two ways:

    Check the name of the newly created Cluster in the list of clusters created by you in a particular Workspace:

    ```shell
    dataos-ctl resource get -t cluster - w ${{workspace name}}
    # Sample
    dataos-ctl resource get -t cluster -w curriculum
    ```

    Alternatively, retrieve the list of all Workers created in the Workspace by appending `-a` flag:

    ```shell
    dataos-ctl resource get -t cluster -w ${{workspace name}} -a
    # Sample
    dataos-ctl resource get -t cluster -w curriculum
    ```

    You can also access the details of any created Cluster through the DataOS GUI in the Resource tab of the  [Operations App.](/interfaces/operations/)

=== "Using Operations App"

    The Operations App UI provides a convenient way to create a Cluster in DataOS. 

    > This functionality is available in versions above DataOS® centaurus-1.8.72.

    To create a cluster using the Operations App UI, follow these steps:

    **Open the Operations app**

    Open the Operations App by either accessing the DataOS graphical user interface (GUI) or using the command-line interface (CLI) with the following command:

    ```shell
    dataos-ctl view -a operations
    ```

    <center>
      <div style="text-align: center;">
        <img src="/resources/cluster/creating_cluster_using_operations_app_ui/cluster_0.png" alt="Creating a Cluster Using Operations App UI" style="width:80%; border:1px solid black;">
        <figcaption align="center"><i>Creating a Cluster Using Operations App UI</i></figcaption>
      </div>
    </center>

    <center><i>Operations App UI</i></center>

    <center>
      <div style="text-align: center;">
        <img src="/resources/cluster/cluster.png" alt="Diagrammatic representation of a Cluster Resource" style="width:80%; border:1px solid black;">
        <figcaption align="center"><i>Diagrammatic representation of a Cluster Resource</i></figcaption>
      </div>
    </center>


    **Navigate to the ‘Create Resource’ section**

    In the Operations App, click the '+ Create Resource' button. This action will open a window with various fields, as shown below:

    <div style="text-align: center;">
      <img src="/resources/cluster/creating_cluster_using_operations_app_ui/cluster_1.png" alt="Create Resource Section" style="border:1px solid black; width: 80%; height: auto;">
      <figcaption><i>Create Resource Section</i></figcaption>
    </div>


    **Fill in the Required Fields**

    Provide the necessary details in the required properties fields and click 'Create Cluster'. For more information on these properties, refer to the documentation [here.](/resources/cluster/configurations/)

    <div style="text-align: center;">
      <img src="/resources/cluster/creating_cluster_using_operations_app_ui/cluster_4.png" alt="Fill in the required fields" style="border:1px solid black; width: 80%; height: auto;">
      <figcaption><i>Fill in the required fields</i></figcaption>
    </div>


    **View the Created Cluster in the Operations App**

    After clicking 'Create Cluster', a Cluster Resource will be created. You can observe the created cluster in the User Kernel section of the DataOS Operations App.

    <div style="text-align: center;">
      <img src="/resources/cluster/creating_cluster_using_operations_app_ui/cluster_5.png" alt="Created Cluster in Operations App" style="border:1px solid black; width: 80%; height: auto;">
      <figcaption><i>Created Cluster in Operations App</i></figcaption>
    </div>


## Interacting with Clusters

Clusters offers multiple methods for interacting with its features and functionalities. The available options are provided below.

### **Using CLI client**

The Trino client is a command-line-based interactive interface that enables users to connect to both the Minerva and Themis Clusters. To learn more, click on the link: [How to setup CLI client.](/resources/cluster/cli_client/)


### **Using Workbench**

To interact with Clusters using the Workbench, execute the following steps:

- **Accessing the Cluster:** Upon launching the Workbench application, the user is required to select the desired Cluster. In this instance, the cluster identified as `themisog` is chosen.

<div style="text-align: center;">
  <img src="/resources/cluster/cluster_selection.png" alt="Selecting a Cluster from Workbench" style="border:1px solid black; width: 80%; height: auto;">
  <figcaption><i>Selecting a Cluster from Workbench</i></figcaption>
</div>


- **Execution of Queries**:
    - **Catalog, Schema, and Table Selection**: The user must select the appropriate catalog, schema, and tables within the Workbench interface.
    - **Query Execution**: After formulating the query, the user executes it by clicking the 'Run' button.
    - **Result Retrieval**: The outcomes of the executed query are displayed in the pane situated below the query input area.

<div style="text-align: center;">
  <img src="/resources/cluster/executed_query.png" alt="Query result set" style="border:1px solid black; width: 80%; height: auto;">
  <figcaption><i>Query result set</i></figcaption>
</div>


For comprehensive details on the features and capabilities of Workbench, refer to the dedicated [Workbench](/interfaces/workbench/) documentation.

### **Using Tableau, SPSS and Power BI**

Users can leverage popular BI analytics platforms like Tableau, SPSS and Power BI to access data from DataOS via Cluster URL. To learn more, navigate to the link: [How to connect Cluster with Tableau, SPSS, and Power BI](/resources/cluster/bi_tools/).

### **Using Spark Integration (Themis only)**

For more control over data and transformations, developers can utilize Spark sessions. This can be done in Scala, Python, or Java. Spark integration allows for complex data manipulation and analysis, leveraging Themis's capabilities within a Spark environment.

## Query Execution Optimization

To achieve enhanced performance and cost efficiency when working with analytical workloads in DataOS, it is crucial to optimize your query execution on Minerva Clusters. The following considerations can assist you in accelerating your queries. For detailed information and guidance, please refer to the provided link: [How to optimize query execution.](/resources/cluster/query_optimization/)


## Performance Tuning

The Performance Tuning section is dedicated to enhancing the execution efficiency of queries within Minerva Clusters. It provides data developers with the means to attain optimal performance for analytical and exploratory workloads. By employing proven techniques for performance tuning, developers can streamline query execution, minimize resource consumption, and expedite data analysis. For more information, consult our [Performance Tuning](/resources/cluster/performance_tuning/) page.

The [Recommend Cluster Configuration](/resources/cluster/configuration_recommendations/) contains recommendations specifically curated to maximize the efficiency and effectiveness of Minerva Cluster for specific scenarios.


## Connectors Configuration

The Minerva query engine supports a wide range of connectors, including MySQL, PostgreSQL, Oracle, and Redshift. These connectors are configured in a YAML file, where they are mounted as catalogs. The catalogs store schemas and enable referencing of data sources through the respective connectors.

By utilizing these connectors, you can perform data analyses directly on the data sources without the need to transfer the data to DataOS. This approach allows for efficient querying and exploration of data, minimizing data movement. To know more, click on the link: [Connectors Configuration.](/resources/cluster/connectors_configuration/)


## Cluster Usage Examples

Refer to the Cluster Resource Usage Examples documentation for a comprehensive understanding of how Cluster can be utilized. It provides detailed examples and practical implementations to help data developers leverage the Cluster Resource efficiently.

- [How to restart and scale the Cluster on a pre-defined schedule?](/resources/cluster/examples/cluster_maintenance/)

- [How to create multiple Cluster using a single manifest file?](/resources/cluster/examples/multiple_cluster_setup/)