---
title: Bento Stack
search:
  boost: 2
---

# Bento Stack

Bento is a stream processing [Stack](/resources/stacks/) within DataOS that enables the definition of data transformations using a declarative YAML-based approach. It streamlines common data engineering tasks, including transformation, mapping, schema validation, filtering, hydrating, multiplexing, etc.

Bento employs stateless, chained processing steps, allowing stream data pipelines to adapt efficiently as requirements evolve. It integrates seamlessly with other services and provides built-in connectors for writing to various destinations.  

!!!tip "Bento Stack in the Data Product Lifecycle"

    Bento operates as a Stack and can be orchestrated using either a [Worker](/resources/worker/) or a [Service](/resources/service/) Resource, depending on the use case.  Bento-powered Workers and Services support the build phase of the Data Product Lifecycle by enabling:  

    - **Stream data transformation** – Continuous real-time processing, such as ingesting IoT sensor data into a messaging queue like Kafka and Pulsar.  
    - **Independent processing** – Long-running data transformations that do not require external network communication, such as standalone data processing streams.  


<center>

<img src="/resources/stacks/bento/bento_architecture.jpg" style="width:31rem; box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.3);" />

<i>Placement of Bento stack within DataOS</i>

</center>



## Key features of Bento

Bento offers a wide range of features that make it an ideal solution for stream processing, which are as follows:

| **Feature**                 | **Description** |
|-----------------------------|---------------|
| **No Runtime Dependencies** | Uses static binaries with no runtime library dependencies, simplifying deployment. |
| **Resilient**               | Ensures at-least-once delivery without persisting messages during transit and gracefully handles back pressure. |
| **Scalability**             | Designed for horizontal scalability to handle increasing data volume. |
| **Declarative Configuration** | Eliminates the need for code compilation or building through a declarative approach. |
| **Observability**           | Integrates with Prometheus for logs and metrics collection. |
| **Cloud Native**            | Compatible with integration frameworks, log aggregators, and ETL workflow engines. |
| **Extensible**              | Supports extension through Go plugins or subprocesses. |
| **Stateless and Fast**      | Stateless design with horizontal scalability and support for stateful operations via external services. |
| **Flexibility**             | Connects to various sources and sinks using different brokering patterns. Supports mapping, validation, filtering, and enrichment. |
| **Bloblang**                | Built-in mapping language for deep exploration of nested structures. |
| **Payload Agnostic**        | Supports structured data formats like JSON, Avro, and binary formats. |
| **Real-time Data Processing** | Enables real-time ingestion and processing of data. |
| **High Configurability**    | Allows construction of complex data pipelines for transformation and enrichment during ingestion. |


Now, let's dive into the details and explore Bento further.

## Syntax of Bento Manifest Configuration

<center>

<img src="/resources/stacks/bento/bento_syntax.jpg" style="width:50rem; box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.3);" />

<i>Placement of Bento stack within DataOS</i>

</center>
s
## Getting Started with Bento

### **Setting Up Bento Locally**

Bento offers functionality suitable for both experienced data professionals and those new to data management. Follow the steps below to set up Bento in a local environment.

[Getting Started ](/resources/stacks/bento/getting_started/)

### **Setting Up Bento on DataOS**

In DataOS, a Bento streaming pipeline is implemented using the Service resource. Bento Services facilitate the efficient definition of stream and event processing pipelines. For detailed instructions on starting with Bento in DataOS, refer to the following link:

[Bento on DataOS](/resources/stacks/bento/bento_on_dataos/)

## Components of Bento Pipeline

Bento operates in a declarative manner, defining stream pipelines using a YAML configuration file. This file serves as a recipe, specifying the sources and transformation components required for data processing. Bento offers a rich set of components within the YAML file. To learn more about these components, click on the link below: 
[Components](/resources/stacks/bento/components/)

## Configuration

Effective configuration is essential for maximizing the efficiency of the Bento stack. Proper configuration settings enhance data processing performance, improve throughput, and ensure effective error handling. Refer to the comprehensive Bento configuration guide for details on both basic setup and advanced techniques: 
[Configurations](/resources/stacks/bento/configurations/)

## Bloblang Guide

Tired of cumbersome data wrangling? Bloblang, the native mapping language of Bento, provides a streamlined solution for data transformation. With its expressive and powerful syntax, Bloblang simplifies the process of transforming data without the need for complex scripts or convoluted pipelines. Discover the capabilities of Bloblang in the following tutorial: 
[Bloblang](/resources/stacks/bento/bloblang/walkthrough/)

<!-- (/resources/stacks/bento/bloblang/) is now/changed to (/resources/stacks/bento/bloblang/bloblang_core_features/)-->

## Recipes

Bento, with its modular architecture and extensive range of processors, inputs/outputs, is perfect for creating real-time data processing recipes. Following collection of use cases and case scenarios demonstrates how Bento can solve common data processing challenges:

- [How can rate limiting be performed in Bento pipelines?](/resources/stacks/bento/recipes/how_to_perform_rate_limit/)
- [What techniques enable effective pagination in Bento workflows?](/resources/stacks/bento/recipes/pagination/)
- [What is the process for fetching stock data from an API to Icebase with Bento?](/resources/stacks/bento/recipes/fetching_data_from_stock_data_api_using_bento/)
- [What steps are involved in processing Twitter API data with Bento?](/resources/stacks/bento/recipes/twitter_api_data_processing/)
- [How can data be fetched from the Instagram API using Bento?](/resources/stacks/bento/recipes/fetching_data_from_instagram_api/)
- [How can a Discord bot be integrated using Bento?](/resources/stacks/bento/recipes/discord_bot/)

<!-- - [How can JSON data be processed using Bento?](/resources/stacks/bento/recipes/processing_json_data/) 
- [What is the best approach for processing nested JSON data?](/resources/stacks/bento/recipes/processing_nested_json_data/) -->