---
title: Stack
search:
  boost: 4
---

# :resources-stack: Stack

Stack is a [DataOS Resource](/resources/) that acts as an execution engine and an extension point for integrating new programming paradigms within the platform. Stacks are composable and can be orchestrated using DataOS Resources such as a [Worker](/resources/worker/), [Service](/resources/service/), or within a designated job in a [Workflow](/resources/workflow/) Resource.

While certain pre-configured Stacks such as [Flare](/resources/stacks/flare/), [Bento](/resources/stacks/bento/), and [Scanner](/resources/stacks/scanner/) are natively available within DataOS, users retain the autonomy to define and deploy their own tailor-made Stacks.

<aside class="callout">

🗣️ A Stack is an <a href="/resources/types/#instance-level-resources">Instance-level</a> DataOS Resource and is a key component of DataOS's extensibility framework. This Resource-type enables the creation of custom Stacks, as exemplified by Soda, CLI, Steampipe, and DBT Stack, all of which have been introduced as a Stack within DataOS using the same development pattern. For detailed guidance on developing your own Stack within DataOS, please consult the following documentation: <a href = "/resources/stacks/custom_stacks/">How to create your own Stack in DataOS?</a>

</aside>

## Key features of Stacks

**Custom Computing Environments**

Stacks provide a means for users to define and manage custom computing environments tailored to their specific needs.

**Dynamic Transformation**

Traditionally, a static, rigid, and linear approach exists for building and deploying software images, with each transformation step requiring manual intervention and a rebuild. In contrast, Stacks enable a dynamically configured transformation approach, allowing more flexibility, where the transformation process is defined through a configuration, making it easier to adapt and extend the process as needed.

**Ensuring Consistency and Reliability**

Stacks encapsulate the necessary components, configurations, and dependencies, ensuring that each execution within a Stack adheres to predefined specifications and operates seamlessly within the broader DataOS ecosystem.

**Abstraction of Deployment Complexities**

Stacks function as an abstraction layer, obviating the need to grapple with the intricacies of deployment. This abstraction empowers data developers to concentrate on their use cases, unfettered by the burden of micromanaging low-level technical intricacies.

**Increasing Platform Team productivity**

Traditionally, data platform teams invest considerable time integrating new programming paradigms within the platform, a repetitive task recurring regularly. The introduction of Stacks delegates the responsibility of creating new Stacks to data developers, enabling them to declaratively create Stacks. For advanced capabilities requiring custom Operators, collaboration with the Platform team may be necessary. This collaborative model enhances the productivity of both teams, preventing the Platform team from becoming a bottleneck for successive capability integration requests.

**Ensures Guarantees**

Stacks assure specific guarantees, such as displaying lineage information on the specified endpoint, ensuring governance, appropriate observability, and orchestrating using DataOS Resources like Worker, Workflow, and Service. Declarative specification of these attributes replaces the extensive development efforts previously required from the Platform team.

**Reusing existing Codebases**

Data Developers can create tailor-made Stacks to incorporate their existing codebases into DataOS, eliminating the need for rewriting. This expedites onboarding and allows developers to seamlessly declare their Stacks (e.g., RClone, Great Expectations) and commence work within the DataOS ecosystem.

## Stack vs. Operator

DataOS has two distinct resources that supports its interoperability and extensibility. One is the Stack and the other is the [Operator](/resources/operator/). Though both [Resource-types](/resources/types/) are quite similar, yet they are relevant in different scenarios. The table below summarizes the difference between the two Resource-types.

| Parameter | Stack | Operator |
| --- | --- | --- |
| *Definition* | Enables orchestration of logic within the periphery of DataOS Kubernetes Cluster. The resource which the Stack manages shares the DataOS runtime, and utilizes its compute for execution of the logic. | Enables orchestration of resources or logic outside the periphery of the DataOS Kubernetes Cluster. The resource (external resource to be precise) doesn’t share the DataOS runtime, and relies on an external compute and platform for those needs. |
| *Control* | More granular control as a data developer can define the various aspects of orchestration like what K8s resources will be utilized, what secrets will be used and all that   | Constrained by the capabilities of the external platform. Lesser control |
| *Development Efforts* | Less development efforts as the creation of the a Stack only demands the understanding of that programming paradigm, no understanding of external platform required. | More development efforts as the creation of an Operator demands understanding of the intricacies of the external platform and NATS. |
| *Creator Persona* | Data Developer primarily the Data Engineer | Platform Engineering Team  |
| *Supporting capabilities* | Modularity, extensibility | Interoperability, Extensibility  |
| *Use Case* | Introduction of new programming paradigms within DataOS like Flink, Spark, Soda, DBT, Steampipe, Function Mesh | Controlling an external resource from the interface of DataOS like Azure Data Factory Pipeline, Databricks Workflow, Hightouch Factory. |
| *Scope* | Instance-Level | Instance-Level |

## Built-in Stacks in DataOS


### **Container**

[Container](/resources/stacks/container/) Stack is a declarative DevOps SDK used for seamless deployment of data applications into production environments.

### **Beacon**

[Beacon](/resources/stacks/beacon/) Stack is a standalone HTTP server that exposes API endpoints on top of a Postgres database. It offers a single flavor `beacon+rest` that enables exposure of REST APIs on Postgres database.


### **Bento**

[Bento](/resources/stacks/bento/) is a high-performance, resilient, and declarative stream processing Stack.

### **CLI**

The DataOS Command-Line Interface (CLI), known as `dataos-ctl`, also serves as a Stack within the DataOS ecosystem. It enables users to programmatically execute CLI commands through a YAML manifest. To learn more about CLI Stack, refer to the link: [CLI](/resources/stacks/cli_stack/).

### **Flare**

[Flare](/resources/stacks/flare/) is a powerful declarative Stack designed specifically for large-scale data processing tasks.


### **Scanner**

The [Scanner](/resources/stacks/scanner/) Stack in DataOS is a Python-based framework that allows developers to extract metadata from external source systems (such as RDBMS, Data Warehouses, Messaging services, etc.) as well as components/services within the DataOS environment.

### **Soda**

Soda is a declarative Stack integrated into DataOS, specifically for data quality testing and profiling across one or more datasets. To learn more about Soda, refer to the link: [Soda](/resources/stacks/soda/).


These built-in Stacks offer a wide range of capabilities, empowering data developers to efficiently build, process, and manage data within the DataOS ecosystem.



## How to create your own Stack?

Aside from the pre-defined Stacks within DataOS, data developers retain the autonomy to create their own tailor made Stacks to extend the existing capabilities of the platform and introduce new programming paradigms within DataOS. To learn more refer to the following link: [How to create your own custom Stack?](/resources/stacks/custom_stacks/)


