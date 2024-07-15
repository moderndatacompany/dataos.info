# Flare Optimizations

> Tuning, Debugging, and much more
> 

## Why Optimize at all?

Flare at its core is a compute engine built atop Apache Spark. Flare out-of-the-box comes with the default Spark configurations that are configured to make sure that jobs can be submitted on very small clusters, and are not recommended for production. Other factors like inefficient Spark SQL queries, using fewer and larger executors, etc, create a bottleneck by not utilizing the available resources effectively. 

To process big data workloads, most often these settings will need to be changed to utilize the resources that you
have available and often to allow the job to run at all. Spark provides fairly finite control of how your environment is configured, and we can often improve the performance of a job at scale by adjusting these settings.

In this section, the aim is not to give a comprehensive introduction to submitting or configuring your Flare Jobs. Instead, we want to focus on providing some context and advice about how to leverage the settings that have a significant impact on performance. 

## Introspection and Debugging

There are different ways in which you can investigate a running/completed Flare Workflow, monitor its progress, and take actions

### **DataOS Operations App**

When a Flare Workflow is deployed on the Kubernetes Cluster, the real-time information regarding the run-time status like Pods, Logs, etc. can be viewed on the Operations App. 

### **DataOS Hera App**

Hera App captures the historical and lineage information related to Flare Workflow deployments, topology etc.  It stores all this information within Blob storage. To know more, navigate to the below page

[Observability of Workflow ](/resources/stacks/flare/optimizations/observability_of_workflow/)

## Spark Web UI

Flare abstracts the complexities of Spark, but at the same time, it amplifies the useful features of Spark. One such is the Spark UI. Spark includes a graphical user interface to inspect or monitor jobs in their various stages of decomposition. A good understanding of what to look for in the Spark UI, such as whether shuffles are spilling to disk or include retries, may help you carve out the best strategy for submitting your Flare Job. 

[Inspecting the Spark UI](/resources/stacks/flare/optimizations/inspecting_the_spark_ui/)

## Flare Job Performance Tuning

Configuring a Flare job is as much an art as a science. Choosing a configuration depends on the size and setup of the data storage solution, the size of the jobs being run (how much data is processed), and the kind of jobs. For example, jobs that cache a lot of data and perform many iterative computations have different requirements than those that contain a few very large shuffles. Tuning also depends on the goals of your team. In some instances, if you are using shared resources, you might want to configure the job that uses the fewest resources and still succeeds. Other times, you may want to maximize the resources available to give your job the best possible performance. 

[Performance Tuning](/resources/stacks/flare/optimizations/performance_tuning/)

## Flare Errors

Stuck with Errors, check out the below link to resolve frequent errors

[Flare Errors and Issues](/resources/stacks/flare/optimizations/errors_and_issues/)