# Flare


Flare is a stack used for building end-to-end data pipelines within DataOS. Utilizing a YAML-based declarative programming paradigm built as an abstraction over Apache Spark, Flare offers an all-in-one solution for performing diverse data ingestion, transformation, enrichment, and syndication processes on both batch and streaming data.


![diagram 02.jpg](./flare/flare.jpg)

<center><i>Placement of Flare stack within DataOS</i>
</center>


[Basic Concepts of Flare Workflow](./flare/basic_concepts_of_flare_workflow.md)

## Getting Started with Flare Stack

### **Elements of Flare Stack**

A Flare Workflow comprises various configuration settings tailored to suit different use cases. These settings govern the reading, writing, and transformation of data from a wide range of sources and destinations. At its core, a Flare Workflow comprises of two key components: the building blocks, which comprise the configuration settings that underpin the Flare Workflow YAML, and the Flare Functions, which allow users to execute complex tasks with minimal coding requirements by leveraging pre-defined functions. 

[Building Blocks of Flare Workflow](./flare/building_blocks_of_flare_workflow.md)

[Flare Functions](./flare/flare_functions.md)

### **Creating Workflows upon Flare Stack**

Embark on a hands-on experience in crafting your first Workflow using Flare. This tutorial will guide you through the process of creating a Flare workflow from start to finish. For further information, please refer to the link provided below.

[Create your first Flare Workflow](./flare/create_your_first_flare_workflow.md)

### **Testing the Workflow**

Prior to deploying your logic into production, it is considered a best practice to thoroughly test it. Flare Standalone provides a convenient, powerful, and reliable testing interface, that enables you to test your code locally on your system, allowing you to identify and address any potential issues before deployment. Further information regarding Flare Standalone can be accessed by clicking the link below.

[Flare Standalone](./flare/flare_standalone.md)

## Flare Optimizations

In the present scenario, the conventional "one size fits all" approach is no longer sufficient. Given the diverse nature of data and the multitude of variations within the data landscape, each Flare Job necessitates fine-tuning and optimization to achieve peak performance in accordance with the user's specifications. For a comprehensive understanding of the numerous optimization techniques, kindly refer to the link provided below.

[Flare Optimizations](./flare/flare_optimizations.md)

## Flare Config Templates

To check out the list of all the connecting depots available in Flare, you can go to the page below to learn more about their configurations.

[Flare Read/Write Config](./flare/flare_read_write_config.md)

## Case Scenarios

[Case Scenario](./flare/case_scenario.md)