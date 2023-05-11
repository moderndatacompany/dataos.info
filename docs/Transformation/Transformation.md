# Transformation

With DataOS, you can build and monitor data pipelines (ELT & ETL both) with minimal movement of original data and run workloads on both batch & stream data. By using workflows/services as primitives any data process such as extraction, transformation, syndication, etc. can be executed by calling stacks to perform the actual workload.

# Workflow

Workflow is a Primitive/Resource within the DataOS. It defines a pipeline involving a sequence of jobs, each utilizing stacks behind the scenes to accomplish myriad tasks. To learn more about workflows, refer to
[Workflow](Transformation/Workflow.md).

For transformation, we can define workflows that call Flare and Toolbox stack to accomplish a particular job. While Flare is a declarative stack for large-scale data processing, the Toolbox stack is used for metadata registration in the case of Icebase depots. If you'd like to know more, please feel free to just go through the sections below.

## Flare

Flare is a declarative stack for large-scale data processing. Flare allows you to build data pipelines and create reasonably complex workflows to carry out the data processing tasks in sequential YAML. It is a powerful tool for Analytical & Data engineers and eliminates the need to understand the protocols/procedures of Spark & Scala. Click on the below page to learn about the myriad tasks you can accomplish using
[Flare](Transformation/Flare.md).

## Toolbox

The Toolbox stack plays a vital role when the output dataset is stored in the Icebase depot. To know more about the Toolbox stack, refer to
[Toolbox](Transformation/Toolbox.md).

# Service

Service is a primitive/resource in the DataOS ecosystem for the use cases that need a continuous flow of real-time data to keep up with modern business requirements such as handling event processing, streaming IoT, network devices log processing, real-time stock trades, etc. DataOS service makes it easy to collect, process, and analyze streaming data so you can get timely insights and react quickly to the latest information. refer to
[Service](Transformation/Service.md).

## Benthos

It is used for Stream Analytics/Event Stream Processing. It allows you to extract & transform streaming data using ‘Bloblang’ within your YAML file itself. To learn how Benthos can be used in DataOS, refer to
[Benthos](Transformation/Benthos.md).

## Surge

Used for Complex Event Processing (CEP). It is an abstraction over Apache Flink.