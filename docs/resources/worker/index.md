---
title: Worker
search:
  boost: 4
---

# :resources-worker: Worker

A Worker [Resource](/resources/) in DataOS is a long-running process responsible for performing specific tasks or computations indefinitely. To understand the key characteristics and what differentiates a Worker from a Workflow and a Service, refer to the following link: [Core Concepts](/resources/worker/core_concepts/).

!!!tip "Worker in the Data Product Lifecycle"

    Worker Resources are integral to the **build phase** in the [Data Product Lifecycle](/products/data_product/). It forms part of the 'code' component in the data product definition and is essential for carrying out prolonged transformations. They are particularly useful when your transformation involves:

    - **Indefinite Execution**: Continuously processing or transforming stream or batch data without a defined endpoint. For example, a Worker processing live sensor data from IoT devices and storing it in a dataset. 
    - **Child/ Processes**: Creating child processes for a main process, allowing for modular and scalable task execution. Employing a Worker to handle background jobs in a web application.
    - **Independent Processing**: Performing long-running transformations without requiring external network communication. Example, employing a Worker to continuously monitor independent data streams.

<center>
![Worker overview](/resources/worker/worker.png)
<figcaption><i>Worker Resource in DataOS</i></figcaption>
</center>

## Structure of Worker manifest

<!-- === "Syntax"
    ![Worker manifest](/resources/worker/worker_annotated.png) -->

=== "Code"
    ```yaml title="worker_manifest_structure.yml"
    --8<-- "examples/resources/worker/sample_worker.yml"
    ```

## First Steps

Worker Resource in DataOS can be created by applying the manifest file using the DataOS CLI. To learn more about this process, navigate to the link: [First steps](/resources/worker/first_steps/).

## Configuration

Workers can be configured to autoscale and match varying workload demands, reference pre-defined Secrets and Volumes, and more. The specific configurations may vary depending on the use case. For a detailed breakdown of the configuration options and attributes, please refer to the documentation: [Attributes of Worker manifest](/resources/worker/configurations/).

<!-- ## Recipes

Workers orchestrate Stacks to accomplish myriad tasks. Below are some recipes to help you configure and utilize Workers effectively:

- [How to declare a Worker configuration within a Stack definition for seamless orchestration?](/resources/worker/how_to_guide/declare_a_stack_for_operation_with_a_worker/)
- [How to use a Worker for syncing data from Fastbase Stream to Icebase using the Fast Fun Stack?](/resources/worker/how_to_guide/syncing_data_from_fastbase_stream_to_icebase/)
- [How to use Workers for transforming Stream data using Bento Stack?](/resources/worker/how_to_guide/transforming_stream_data/)
- [How to autoscale Workers?](/resources/worker/how_to_guide/autoscale_workers/)
- [How to refer Secrets in Worker configuration?](/resources/worker/how_to_guide/referring_secrets_in_worker/) -->




