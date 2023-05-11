# On-Demand Computing

On-demand computing is a delivery model in which computing resources such as computing power, storage, and memory are made available to the user as needed. The resources are provided on an as-needed and when-needed basis for specific data processing/exploratory analytical workloads.

The on-demand computing model overcomes the common challenge of efficiently meeting fluctuating computational requirements. Now you don't have to over-provision resources upfront to handle peak levels of business activity in the future. Instead, you provision the number of resources that you actually need. You can scale these resources up or down as your business needs change.

## Tightly coupled storage and compute

The traditional data warehouses always come with a compute on top of the data; the nodes deployed in the cluster are used for storing data and computation. However, the requirement of Storage and Compute is not always linear, and it varies for different workloads. Some workloads are compute-intensive; others may require a large data storage volume. With the nodes doing both, the enterprise must scale both simultaneously.

This tight coupling leads to underutilized or scarce resources either on Storage or Compute, not giving the optimal use of provisioned capacity.

There are situations when the enterprise needs to grow compute capabilities while keeping storage relatively constant, such as during high-traffic periods like popular annual shopping events or at the end of the quarter consolidation. Scaling these functions independently frees the enterprise to pay only for what it uses, as it uses it.

To work with the data stored in the warehouse, you have to go via the data warehouse's compute tier that creates performance issues while simultaneously trying to load and query data.

Traditional cluster configuration does not have a shared data cluster. Therefore, if multiple clusters are to be provisioned for different types of workloads e.g., ELT/ELT, BI & Reporting on same data- the only option is to copy or move the required data to their respective workload clusters leading to data duplication.

## Decoupled Compute and Storage

With decoupling the storage and compute, each of these can be scaled independently to each other.

You can bring larger or smaller compute based on your needs.  So, for example, imagine a reporting query that you have to run, which is going to last for six hours because it's going to scan six months' worth of data. You can bring a larger cluster for six hours to run that query.  For complex queries you have to wait until data is completely loaded into the warehouse.

Imagine that your team is trying to do ad-hoc analysis to understand what data they have, and typically, they're running queries on a smaller set of data. You need a smaller cluster, which is long-running. So, you have the ability to design your compute, which will work on the data to suffice the need that you're trying to address.

You can manage two kinds of workloads – Batch and Interactive. Even in the case of Batch, there are ETL, dashboards queries, periodic reports, etc. In the case of ad hoc queries, the requirements might be specific to the user and use cases. For a data scientist, the data set and cluster capabilities requirements might be completely different from an analyst use case. The decoupling of storage and compute also works with individual departments as well. Many teams have their own budgeting constraints and work on different data sets. They like to have their own analytics setup and manage it according to their application lifecycle.

This brings in huge cost savings and operational efficiencies as the resources are stood up only when they are required, only for the amount of resources that are required and only for the time they are required, after which they are terminated.

## On-Demand Compute in DataOS

DataOS enables you to define and maintain a pool of resources that contains networks, servers, storage, applications, and services. This pool can serve the varying demand of resources and computing for various workload requirements.

When you work with data in the  DataOS storage built on top of Iceberg table format, you can bring whatever compute you want. Data storage in DataOS, essentially a lake house pattern, gives you an open data format.

DataOS maintains data as single source of truth, the Business and IT teams executing various workloads can now have access to the required data (as per the governance policies) without having to move it to their local cluster. This creates a much streamlined, effective and optimized approach to provisioning of data across the organization.

You can create a Minerva query engine cluster, which allows you to query the data through depots that you have in the system. You can attach and create your own cluster within the DataOS instance.  The billing for that cluster can be attributed to you for your use case, and you can keep it private to yourself. So, you can be more cost-efficient.

So, when you deploy your jobs for bringing data, like your Flare data processing jobs or querying your data on Workbench, you can ask for required compute.

To create an on-demand compute type, you need to know which cluster needs to run on a specific kind of machine. You need to understand what kind of compute works best on various types of queries. Then you will be able to decide do you want to run it faster or cheaper? And based on that, you can adjust the compute.