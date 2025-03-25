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

![Bento within DataOS](/resources/stacks/bento/bento_overview.png){: style="width:31rem;" }

<i>Placement of Bento stack within DataOS</i>

</center>


## Key features of Bento

Bento offers a wide range of features that make it an ideal solution for stream processing, including:

- **No Runtime Dependencies:** Bento utilizes static binaries with no runtime library dependencies, simplifying deployment.

- **Resilient:** Built with an in-process transaction model, Bento ensures at-least-once delivery without persisting messages during transit. It gracefully handles back pressure by temporarily stopping consumption when output targets block traffic.

- **Scalability:** Bento is designed for horizontal scalability, allowing seamless scaling as data volume increases.

- **Declarative Configuration:** Bento employs a declarative approach, eliminating the need for code compilation or building.

- **Observability:** Integration with Prometheus enables the collection of logs and metrics for better observability.

- **Cloud Native:** Bento is compatible with integration frameworks, log aggregators, and ETL workflow engines, making it a cloud-native solution that can complement traditional data engineering tools or serve as a simpler alternative.

- **Extensible:** Bento supports extension through Go plugins or subprocesses.

- **Stateless and Fast:** Bento is designed to be stateless and horizontally scalable. However, it can interact with other services to perform stateful operations.

- **Flexibility:** Bento allows connectivity with various sources and sinks using different brokering patterns. It facilitates single message transformation, mapping, schema validation, filtering, hydrating, and enrichment through interactions with other services, such as caching.

- **Bloblang:** Bento includes a built-in lit mapping language, Bloblang, which enables deep exploration of nested structures for extracting required information.

- **Payload Agnostic:** Bento supports structured data in JSON, Avro, or even binary formats, providing flexibility in data processing.

- **Real-time Data Processing:** Bento is designed for real-time data processing, making it suitable for scenarios requiring immediate ingestion and processing of generated data.

- **High Configurability:** Bento offers high configurability, allowing the construction of complex data processing pipelines that transform and enrich data during ingestion.

Now, let's dive into the details and explore Bento further.

## Syntax of Bento YAML Configuration

![Bento YAML Configuration Syntax](/resources/stacks/bento/bento_syntax.png)

<center><i>Bento YAML Configuration Syntax</i></center>

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

<!-- (/resources/stacks/bento/bloblang/) it going to (/resources/stacks/bento/bloblang/bloblang_core_features/)-->

## Recipes

Bento, with its modular architecture and extensive range of processors, inputs/outputs, is perfect for creating real-time data processing recipes. Following collection of use cases and case scenarios demonstrates how Bento can solve common data processing challenges:

- [How can rate limiting be performed in Bento pipelines?](/resources/stacks/bento/recipes/how_to_perform_rate_limit/)
- [What is the process for fetching stock data from an API to Icebase with Bento?](/resources/stacks/bento/recipes/fetching_data_from_stock_data_api_using_bento/)
- [What steps are involved in processing Twitter API data with Bento?](/resources/stacks/bento/recipes/twitter_api_data_processing/)
- [How can JSON data be processed using Bento?](/resources/stacks/bento/recipes/processing_json_data/)
- [What is the best approach for processing nested JSON data?](/resources/stacks/bento/recipes/processing_nested_json_data/)
- [How can data be fetched from the Instagram API using Bento?](/resources/stacks/bento/recipes/fetching_data_from_instagram_api/)
- [How can a Discord bot be integrated using Bento?](/resources/stacks/bento/recipes/discord_bot/)
- [What techniques enable effective pagination in Bento workflows?](/resources/stacks/bento/recipes/pagination/)