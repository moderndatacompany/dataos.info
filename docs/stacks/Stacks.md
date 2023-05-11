# Stacks

Within DataOS, Stacks are the programming paradigms used to support processing and management of data. They also act as the extension points of our runnable resources, Workflow and Service.

In simple terms, you can think of stacks as the way we are able to bring in new processing engines, frameworks or programmes, and host them in accordance with the norms and conventions of our operating system. A user can then refer to and use these stacks in the same declarative manner they use to interact with the system. 

A stack is called upon and used by declaring it in the configuration file of DataOS resource, Workflow or Service. In a given Workflow you can also use more than one stack to accomplish different jobs.

Here’s the list of all the stacks you can currently use within DataOS:

## Scanner
Metadata retrieval or extraction is the process of requesting and retrieving metadata from a metadata endpoint. These metadata endpoints can be data sources, dashboards, messaging, and lineage services.

Metadata extraction is accomplished by the *DataOS Scanner* stack. You can write Scanner workflows in the form of a sequential YAML for a pull-based metadata extraction system built into DataOS for a wide variety of sources in your data stack.
To know the details, refer to
[Scanner](./Scanner/Scanner.md).

## Flare
Flare is a declarative stack for large-scale data processing. Flare allows you to build data pipelines and create reasonably complex workflows to carry out the data processing tasks in sequential YAML. It is a powerful tool for Analytical & Data engineers and eliminates the need to understand the protocols/procedures of Spark & Scala. Click on the page to learn about the myriad tasks you can accomplish using
[Flare](./Flare/Flare.md).

## Benthos
It is used for Stream Analytics/Event Stream Processing. It allows you to extract & transform streaming data using ‘Bloblang’ within your YAML file itself. To learn how Benthos can be used in DataOS, refer to
[Benthos](./Benthos/Benthos.md) 

## Beacon
The application development framework of DataOS leverages our core value pillars, such as Governance and Observability, while allowing you to build data apps in an agile manner. This way, DataOS becomes an end-to-end development & deployment environment for all your data-related products.
[Beacon](./Beacon/Beacon.md) 

## Alpha
A stack within DataOS that helps you connect with web-server-based application images developed on top of DataOS. It allows you to use compute resources of DataOS to run an external tool or application, irrespective of the programming language used to create the application. To learn more, refer to
[Alpha](./Alpha.md) 

## Airbyte
Airbyte allows you to *ingest data* from pre-built as well as custom-made connectors, from high-volume databases to the long tail of API sources. You can directly access and start using Airbyte from DataOS GUI itself, refer to the documentation:
[Airbyte](./Airbyte/Airbyte.md) 

## Data Toolbox
The Toolbox stack plays a vital role when the output dataset is stored in the Icebase depot. To know more about the Toolbox stack, refer to
[Toolbox](../Transformation/Toolbox.md)

## Rclone

Enable data movement into the cloud or between cloud storages with additional abilities like backup, restore, mirror, etc.
Impatience is never a good look. Information coming in soon!

## Surge

Used for Complex Event Processing (CEP). It is an abstraction over Apache Flink.