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



Now, let's dive into the details and explore Bento further.

## Syntax of Bento YAML Configuration

![Bento YAML Configuration Syntax](/resources/stacks/bento/bento_syntax.png)

<center><i>Bento YAML Configuration Syntax</i></center>

## Getting Started with Bento

### **Setting Up Bento Locally**

Whether you're a seasoned data wrangler or a curious beginner, Bento has something for you. Ready to take the plunge? Let's start by setting up Bento locally.

[Getting Started ](/resources/stacks/bento/getting_started/)

### **Setting Up Bento on DataOS**

In DataOS, a Bento streaming pipeline is implemented using the Service resource. Bento Services allow for the quick definition of stream and event processing pipelines. To start your Bento journey on DataOS, refer to the link below

[Bento on DataOS](/resources/stacks/bento/bento_on_dataos/)

## Components of Bento Pipeline

Bento operates in a declarative manner, defining stream pipelines using a YAML configuration file. This file serves as a recipe, specifying the sources and transformation components required for data processing. Bento offers a rich set of components within the YAML file. To learn more about these components, click on the link below:

[Components](/resources/stacks/bento/components/)

## Configuration

Effective configuration is crucial for utilizing the Bento stack efficiently. With the right configuration settings, you can optimize your data processing pipelines, achieve maximum throughput, and handle errors effectively. Explore our comprehensive list on Bento configuration, covering basic setup to advanced techniques:

[Configurations](/resources/stacks/bento/configurations/)

## Bloblang Guide

Tired of cumbersome data wrangling? Bloblang, the native mapping language of Bento, provides a streamlined solution for data transformation. With its expressive and powerful syntax, Bloblang simplifies the process of transforming data without the need for complex scripts or convoluted pipelines. Discover the capabilities of Bloblang in our tutorial:

[Bloblang ](/resources/stacks/bento/bloblang/)

## Recipes

Bento, with its modular architecture and extensive range of processors, inputs/outputs, is perfect for creating real-time data processing recipes. Our collection of use cases and case scenarios demonstrates how Bento can solve common data processing challenges. Explore the possibilities with Bento:

- [Processing JSON data](/resources/stacks/bento/recipes/processing_json_data/)
- [Processing nested JSON data](/resources/stacks/bento/recipes/processing_nested_json_data/)
- [Processing JSON array of objects](/resources/stacks/bento/recipes/processing_json_array_of_objects/)
- [Fetching Data from Instagram API](/resources/stacks/bento/recipes/fetching_data_from_instagram_api/)
- [Twitter API Data Processing](/resources/stacks/bento/recipes/twitter_api_data_processing/)
- [Discord Bot](/resources/stacks/bento/recipes/discord_bot/)
- [Stock Data API to Icebase](/resources/stacks/bento/recipes/fetching_data_from_stock_data_api_using_bento/)
- [Perform Rate Limit](/resources/stacks/bento/recipes/how_to_perform_rate_limit/)
- [Performing Pagination](/resources/stacks/bento/recipes/pagination/)