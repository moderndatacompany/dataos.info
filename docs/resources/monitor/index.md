---
title: Monitor
search:
  boost: 4
---

# :resources-monitor: Monitor

The Monitor [Resource](/resources/) is an integral part of DataOS’ Observability system, designed to trigger incidents based on specific [events](/resources/) or metrics. By leveraging the Monitor Resource alongside the [Pager](/resources/pager/) Resource for sending alerts, DataOS users can achieve comprehensive observability and proactive incident management, ensuring high system reliability and performance. To understand the key concepts associated with a Monitor, refer to the following link: [Core Concepts](/resources/monitor/core_concepts/).

!!!tip "Monitor in the Data Product Lifecycle"

    Monitors form the part of the  are integral to the **transformation phase** in the [Data Product Lifecycle](/products/data_product/). They are particularly useful when your transformation involves:

    - **Indefinite Execution**: Continuously processing or transforming stream or batch data without a defined endpoint. For example, a Worker processing live sensor data from IoT devices and storing it in a dataset. 
    - **Child/ Processes**: Creating child processes for a main process, allowing for modular and scalable task execution. Employing a Worker to handle background jobs in a web application.
    - **Independent Processing**: Performing long-running transformations without requiring external network communication. Example, employing a Worker to continuously monitor

<center>
![Worker overview](/resources/worker/worker.png)
<i>Worker Resource in DataOS</i>
</center>

## Structure of Monitor manifest

=== "Syntax"
    ![Monitor manifest](/resources/worker/worker_annotated.png)

=== "Code"
    ```yaml title="monitor_manifest_structure.yml"
    --8<-- "examples/resources/monitor/equation_manifest.yaml"
    ```

## First Steps

Monitor Resource in DataOS can be created by applying the manifest file using the DataOS CLI. To learn more about this process, navigate to the link: [First steps](/resources/monitor/first_steps/).

## Configuration

Monitors can be configured to autoscale and match varying workload demands, reference pre-defined Secrets and Volumes, and more. The specific configurations may vary depending on the use case. For a detailed breakdown of the configuration options and attributes, please refer to the documentation: [Attributes of Monitor manifest](/resources/monitor/configuration/).





