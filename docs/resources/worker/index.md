---
title: Worker
search:
  boost: 2
---

# :resources-worker: Worker

A Worker [Resource](/resources/) in DataOS is a long-running process responsible for performing specific tasks or computations indefinitely. To understand the key characteristics and what differentiates a Worker from a Workflow and a Service, refer to the following link: [Core Concepts](/resources/worker/core_concepts/).

<center>
![Worker overview](/resources/worker/worker.png)
<i>Worker Resource in DataOS</i>
</center>

## First Steps

Worker Resource in DataOS can be created by applying the manifest file using the DataOS CLI. To learn more about this process, navigate to the link: [First steps](/resources/worker/first_steps/).

## Configuration

Workers can be configured to autoscale and match varying workload demands, reference pre-defined Secrets and Volumes, and more. The specific configurations may vary depending on the use case. For a detailed breakdown of the configuration options and attributes, please refer to the documentation: [Attributes of Worker manifest](/resources/worker/configuration/).

## Recipes

Workers orchestrate Stacks to accomplish myriad tasks. Below are some recipes to help you configure and utilize Workers effectively:

- [How to declare a Worker configuration within a Stack definition for seamless orchestration?](/resources/worker/how_to_guide/declare_a_stack_for_operation_with_a_worker/)
- [How to use a Worker for syncing data from Fastbase Stream to Icebase using the Fast Fun Stack?](/resources/worker/how_to_guide/syncing_data_from_fastbase_stream_to_icebase/)
- [How to use Workers for transforming Stream data using Benthos Stack?](/resources/worker/how_to_guide/transforming_stream_data/)
- [How to autoscale Workers?](/resources/worker/how_to_guide/autoscale_workers/)
- [How to refer Secrets in Worker configuration?](/resources/worker/how_to_guide/referring_secrets_in_worker/)




