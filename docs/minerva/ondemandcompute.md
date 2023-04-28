# On Demand Computing [In Progress]

## Introduction

In an enterprise system, demand for computing resources varies from time to time. In such a scenario, resources need to be provisioned to handle the increase/decrease in demand.

On-demand computing is a delivery model in which computing resources such as computing power, storage, and memory are made available to the user as needed. The resources are provided on an as-needed and when-needed basis for specific data processing/exploratory analytical workloads.  

The on-demand compute model overcomes the common challenge of efficiently meeting fluctuating computational requirements. Now you don't have to over-provision resources upfront to handle peak levels of business activity in the future. Instead, you provision the number of resources that you actually need. You can scale these resources up or down as your business needs change.

## Tightly coupled storage and compute

The traditional data warehouses always come with a compute on top of the data; the nodes deployed in the cluster are used for storing data and computation. However, the requirement of Storage and Compute is not always linear, and it varies for different workloads. Some workloads are compute-intensive; others may require a large data storage volume. With the nodes doing both, the enterprise must scale both simultaneously.
This tight coupling leads to underutilized or scarce resources either on Storage or Compute, not giving the optimal use of provisioned capacity.

There are situations when the enterprise needs to grow compute capabilities while keeping storage relatively constant, such as during high-traffic periods like popular annual shopping events or at the end of the quarter consolidation. Scaling these functions independently frees the enterprise to pay only for what it uses, as it uses it.

To work with the data stored in the warehouse, you have to go via the data warehouse's compute tier that creates performance issues while simultaneously trying to load and query data. 

Traditional cluster configuration does not have a shared data cluster. Therefore, if multiple clusters are to be provisioned for different types of workloads e.g., ELT/ELT, BI & Reporting on same data- the only option is to copy or move the required data to their respective workload clusters leading to data duplication.

## Power of separation between compute and storage

With decoupling the storage and compute, each of these can be scaled independent to each other.
You can bring larger or smaller compute based on your needs.  So, for example, imagine a reporting query that you have to run, which is going to last for six hours because it's going to scan six months' worth of data. You can bring a larger cluster for six hours to run that query.  For complex queries you have to wait until data is completely loaded into the warehouse. 

Imagine that your team is trying to do ad-hoc analysis to understand what data they have, and typically, they're running queries on a smaller set of data. You need a smaller cluster, which is long-running. So, you have the ability to design your compute, which will work on the data to suffice the need that you're trying to address.

You can manage two kinds of workloads – Batch and Interactive. Even in the case of Batch, there are ETL, dashboards queries, periodic reports, etc. In the case of ad hoc queries, the requirements might be specific to the user and use cases. For a data scientist, the data set and cluster capabilities requirements might be completely different from an analyst use case. The decoupling of storage and compute also works with individual departments as well. Many teams have their own budgeting constraints and work on different data sets. They like to have their own analytics setup and manage it according to their application lifecycle.

This brings in huge cost savings and operational efficiencies as the resources are stood up only when they are required, only for the amount of resources that are required and only for the time they are required, after which they are terminated.

## On-Demand Compute in DataOS 

DataOS enables you to define and maintain a pool of resources that contains networks, servers, storage, applications, and services. This pool can serve the varying demand of resources and computing for various workload requirements. 

When you work with data in the  DataOS storage built on top of Iceberg table format, you can bring whatever compute you want. Data storage in DataOS, essentially a lake house pattern, gives you an open data format. 

DataOS maintains data as single source of truth, the Business and IT teams executing various workloads can now have access to the required data (as per the governance policies) without having to move it to their local cluster. This creates a much streamlined, effective and optimized approach to provisioning of data across the organization.

You can create a Minerva query engine cluster, which allows you to query the data through depots that you have in the system. You can attach and create your own cluster within the DataOS instance.  The billing for that cluster can be attributed to you for your use case, and you can keep it private to yourself. So, you can be more cost-efficient.

So, when you deploy your jobs for bringing data, like your Flare data processing jobs or querying your data on Workbench, you can ask for required compute.   

To create an on-demand compute type, you need to know which cluster needs to run on a specific kind of machine. You need to understand what kind of compute works best on various types of queries. Then you will be able to decide do you want to run it faster or cheaper? And based on that, you can adjust the compute.

## Compute structures in DataOS
Create compute clusters on-demand for varied data processing/querying needs.
This section describes the steps to define and create various compute for the different workload requirements. To define compute structures in DataOS, follow the three steps process given below:

1. Provisioning VMs ​

3. Define compute resource in DataOS​

4. Refer compute resource in Flare job or Minerva cluster​

### Provisioning VMs

DataOS uses Kubernetes for cluster and container management. It supports creating/defining groups of VMs (node pools) that have a certain profile- a specific CPU,  memory, and disk capacity. You need to provision a group of VMs, register those with Kubernetes, and then with the DataOS as a compute resource. 

You can also create a group of VMs that use GPUs or a group of VMs with very small CPUs.  Then once you have these groups created, you can register them with the DataOS. So now they're known what computes you have. 

> :material-alert: **Note**: Please contact your administrator for creating node pool.

### Define compute resources in DataOS

Compute in the DataOS context is just another primitive. You can define and name these compute resourcesin a  YAML file. You can run applications in the DataOS by allocating memory through the resource manager.

By Default, DataOS has two separate computes:

1) runnable for running resources which are essentially our workflows and services 
2) queries which are Minerva clusters 

When DataOS is deployed, these two computes are registered by default with the DataOS. So they are part of the default install. DataOS allows you to add new groups of VMs and make them known to the DataOS and addressable via a name. 

```yaml
- name: configure-dataos-resources-system
    values:
      install_and_upgrade:
        - name: "runnable-default"
          version: v1beta1
          type: compute
          layer: system
          description: "default runnable compute"
          compute:
            type: K8SNodePoolLocal
            defaultFor: runnable
            nodePool:
              nodeSelector:
                "dataos.io/purpose": "runnable"
              tolerations:
                - key: "dedicated"
                  operator: "Equal"
                  value: "runnable"
                  effect: "NoSchedule"
        - name: "query-default"
          version: v1beta1
          type: compute
          layer: system
          description: "default query compute"
          compute:
            type: K8SNodePoolLocal
            defaultFor: query
            nodePool:
              nodeSelector:
                "dataos.io/purpose": "query"
              tolerations:
                - key: "dedicated"
                  operator: "Equal"
                  value: "query"
                  effect: "NoSchedule"
```
 
### Create Minerva clusters

When you define a cluster,  you specify the node type. The node type determines each node's CPU, RAM, storage capacity, and storage drive type.
For example,

16 cores | 128 GB RAM | 2 TB of local storage

The above specifications are just a minimum recommendation. You should consider increasing these specifications based on your workloads and the amount of data you are processing.
Various data processing requirements force data engineering teams to create multiple clusters.

#### Define Cluster groups 

To learn more refer-  [Minerva Cluster Tuning](tuneminerva.md)

## Self-service access to on-demand compute on Workbench


### Selecting clusters for your query
Default clusters
You can choose to connect to Minerva clusters from Workbench as per the compute requirement.

### Running queries status
Minerva usage statistics dashboard
Query status, statistics

### List of Clusters
List of Minerva Clusters added to the gateway. 

### Managing Clusters

You can add or delete clusters as per the query workload.
How to do that, Workbench??

The resources may be maintained within the DataOS environment and made available by a cloud service provider. The complexity of managing cluster performance to meet business requirements is complex. You want best-in-class performance to meet the short and long-running, interactive workloads while reducing and controlling costs.

## Cluster usage status

## RoutingPolicy

RoutingPolicy determines the criteria for a cluster to be qualified for a query. The default RoutingPolicy is RANDOM, which means any cluster can be chosen randomly to execute the query.
- if it maintains a queue
- As per query, load

The routing of requests can be controlled by implementing RoutingRule.
### Adding your own rules
By default, it has location-based, random, and static routing rules.

##  Policies around cluster access
As per the access policy, the gateway will forward the query to the assigned clusters and continue the entire query process.

DataGateway is a service that sits between clients and Minerva clusters. It is essentially an intelligent HTTP proxy server that is an abstraction layer on top of the Minerva clusters that handles the following actions:

1. Parse incoming SQL statements to get requested datasets
2. Manage data access policy to limit users' data access by checking against the SQL results.
3. Manage users' cluster access.
4. Redirect users' queries to the authorized clusters.
5. Inform users about the errors whenever the query is rejected, or exceptions from clusters are encountered.
 












