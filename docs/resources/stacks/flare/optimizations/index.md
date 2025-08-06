# Flare Optimizations

<!-- > Tuning, Debugging, and much more
>  -->

## Why Optimize at all?

Flare at its core is a compute engine built atop Apache Spark. Flare out-of-the-box comes with the default Spark configurations that are configured to make sure that jobs can be submitted on very small clusters, and are not recommended for production. Other factors like inefficient Spark SQL queries, using fewer and larger executors, etc, create a bottleneck by not utilizing the available resources effectively. 

To process big data workloads, most often these settings will need to be changed to utilize the resources that you
have available and often to allow the job to run at all. Spark provides fairly finite control of how your environment is configured, and we can often improve the performance of a job at scale by adjusting these settings.

In this section, the aim is not to give a comprehensive introduction to submitting or configuring your Flare Jobs. Instead, it focus on providing some context and advice about how to leverage the settings that have a significant impact on performance. 

<!-- ## Introspection and Debugging

There are different ways in which you can investigate a running/completed Flare Workflow, monitor its progress, and take actions

### **DataOS Operations App**

When a Flare Workflow is deployed on the Kubernetes Cluster, the real-time information regarding the run-time status like Pods, Logs, etc. can be viewed on the Operations App. 

 ### **DataOS Hera App**

Hera App captures the historical and lineage information related to Flare Workflow deployments, topology etc.  It stores all this information within Blob storage. To know more, navigate to the below page

[Observability of Workflow ](/resources/stacks/flare/optimizations/observability_of_workflow/) -->


## Spark Web UI

Flare abstracts the complexities of Apache Spark while exposing its diagnostic capabilities, such as the Spark Web UI. This graphical interface enables monitoring and inspection of jobs across various execution stages. A thorough review of Spark UI metrics—such as shuffle spill events or task retries—can inform an effective strategy for submitting Flare jobs. For detailed inspection guidelines, refer to [Inspecting the Spark UI](/resources/stacks/flare/optimizations/inspecting_the_spark_ui/).

## Flare Job Performance Tuning

Flare job configuration requires consideration of data volume, storage architecture, and job characteristics. Jobs with extensive caching and iterative computations require different configurations compared to jobs with large shuffle operations. Tuning also depends on operational objectives, such as optimizing for minimal resource usage in shared environments or maximizing resource allocation for performance. For additional configuration strategies, see [Performance Tuning](/resources/stacks/flare/optimizations/performance_tuning/).

## Flare Errors

Common errors encountered during Flare job execution can often be resolved by referencing standardized issue patterns and resolutions. To address frequently observed failures, visit [Flare Errors and Issues](/resources/stacks/flare/troubleshooting/).
