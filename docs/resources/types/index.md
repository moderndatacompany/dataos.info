---
title: Types of DataOS Resources
search:
  boost: 2
tags:
  - Resource-types
  - Type
hide:
  - tags
---

# Types of DataOS Resources

The categorization of Resources in DataOS is based on the concept of Workspace. **Workspace** is like a tenant in DataOS. You can use it to create isolated work environments for your or your team’s work. By default, all Resources are created in the *public Workspace*.

## Workspace-level Resources

These Resources are defined, applied and updated in a specific Workspace. This allows the Workspace operators to limit their usage to that specific Workspace. Concurrently, it also provides them with the flexibility to allow the users of a different Workspace to use the same Resources.

The following Resources are considered Workspace-level Resources:

### **Cluster**

A DataOS Resource to create, manage and optimize computational resources & configurations for both simple & advanced analytics and data processing. You will find the details on the following link: [Cluster](/resources/cluster/).

### **Database**

A Database Resource acts as a repository for storing transaction data, utilizing a managed Postgres relational database. To learn more about Database Resource, please refer to the link: [Database](/resources/database/).


### **Lakehouse** 

<!-- >🔔 Components labeled as **[𝛼 alpha]** are in their Alpha release phase. This stage is primarily for testing and evaluation; therefore, we advise against using these components for critical production tasks. Availability in all environments is not guaranteed. For further information and confirmation of their accessibility, please consult with your DataOS administrator. -->

DataOS Lakehouse integrates Apache Iceberg table format with cloud object storage to offer a fully managed storage solution. It replicates traditional data warehouse functionalities, such as table creation with defined schemas and data manipulation via various tools. To learn more about Lakehouse, refer to the following link: [Lakehouse](/resources/lakehouse/).

### **Lens**

Lens Resource is a logical modelling layer within DataOS desgined for accessing tabular data in data warehouses or lakehouses. To learn more about Lens, refer to the following link: [Lens](/resources/lens/).

### **Monitor**

The Monitor is a DataOS Resource that allows one to raise incidents corresponding to the occurrence of certain events or metrics in the system. More details about the Monitor are available on the following page: [Monitor](/resources/monitor/).

### **Pager**

A Pager Resource enables users to specify criteria for identifying an incident from the incident stream and delivering it to a user-specified destination. Learn more about Pager on the following link: [Pager](/resources/pager/).


### **Secret**

The Resource to store sensitive information such as passwords, tokens or keys in the internal vault of DataOS, and use this information later without sharing the sensitive data itself. Secrets are confined to a Workspace, unlike Instance Secrets whose scope spans across the entire DataOS Instance. Read about Secret on the following page: [Secret](/resources/secret/).

### **Service**

Service can be conceptualized as a long-running process that is receiving or/and serving an API, or even a UI. It can be used for scenarios that need a continuous flow of real-time data, such as event processing, streaming IoT and more. You will find the details of this *runnable resource* here: [Service](/resources/service/).

### **Volume**

A Volume Resource in DataOS offers persistent and shared storage solutions for containerized applications. Learn more about Volume on the following link: [Volume](/resources/volume/).

### **Worker**

A Worker Resource in DataOS is a long-running process responsible for performing specific tasks or computations indefinitely. Workers are designed to run continuously without a defined end time, focusing on throughput-based tasks rather than synchronous responses. They are lightweight, robust, and autoscalable, making them ideal for specialized execution within the DataOS ecosystem. Read more about Workers on the following page: [Worker](/resources/worker/).

### **Workflow**

Workflow is a manifestation of a Directed Acyclic Graph, which helps you to streamline and automate the process of working with big data. A data ingestion or processing task carried out as a batch is referred to as a *job*. Jobs are defined and executed through Workflow. Learn the details of the Workflow here: [Workflow](/resources/workflow/).



---

## Instance-level Resources

These Resources can be visualized as being global throughout the operating system. They cannot be defined just for a particular Workspace. Once created, they become available to authorized users of all Workspaces.

The following Resources come into this category:

### **Bundle** 

<!-- >🔔 Components labeled as **[𝛼 alpha]** are in their Alpha release phase. This stage is primarily for testing and evaluation; therefore, we advise against using these components for critical production tasks. Availability in all environments is not guaranteed. For further information and confirmation of their accessibility, please consult with your DataOS administrator. -->

The Bundle Resource is a Resource management construct that streamlines the deployment and management of multiple DataOS Resources. Within a Bundle each entity represents a unique DataOS Resource, interconnected through dependency relationships and conditions. To learn more about Bundles, click on the link: [Bundle](/resources/bundle/).

### **Compute**

Compute is essentially a node pool of homogeneous virtual machines. They allow you to configure the processing power associated with your data workloads. Read about them in detail on the following page: [Compute](/resources/compute/).


### **Depot**

Depots provide you with a uniform way to connect with the variety of data sources in your organization. Depots abstract away the different protocols and complexities of the source systems to present a common taxonomy and method to address these source systems. Learn how to create & use depots on this link: [Depot](/resources/depot/).

### **Grant**

A Grant Resource enables administrators assign use cases to subjects either as users or roles, granting them access to specific parts of the system or data. To learn more about Grant, refer to the following link: [Grant](/resources/grant/).

### **Instance Secret**

An Instance Secret is a Resource within DataOS for securely storing confidential information at the DataOS Instance level. Its scope spans the entire DataOS Instance, enabling access across all Workspaces. Conversely, a Secret is limited in accessibility, allowing access solely to Resources within the Workspace where it's created. 

### **Operator**

<!-- >🔔 Components labeled as **[𝛼 alpha]** are in their Alpha release phase. This stage is primarily for testing and evaluation; therefore, we advise against using these components for critical production tasks. Availability in all environments is not guaranteed. For further information and confirmation of their accessibility, please consult with your DataOS administrator. -->

Operator is a DataOS Resource that offers a standardized interface for orchestrating resources located outside the DataOS cluster. It enables data developers to programmatically control these external resources through DataOS interfaces. Central to its function is allowing DataOS’s orchestrator, *Poros*, to manage external resources using custom Operators. To know more about Operator, refer to the link: [Operator](/resources/operator/).

### **Policy**

Policy is a set of rules which governs the behavior of a user(person or application/service). Broadly, you can create and manage two kinds of policies in DataOS - *Access Policy* & *Data Policy*. They have been elaborated on this page: [Policy](/resources/policy/).

### **Stack**

<!-- >🔔 Components labeled as **[𝛼 alpha]** are in their Alpha release phase. This stage is primarily for testing and evaluation; therefore, we advise against using these components for critical production tasks. Availability in all environments is not guaranteed. For further information and confirmation of their accessibility, please consult with your DataOS administrator. -->

Stacks are the programming paradigms used to support the processing and management of data. They also act as the secondary extension points for our runnable resources, Workflow, Worker and Service. The following page contains detailed information on all the stacks you can currently leverage in DataOS: [Stacks](/resources/stacks/).
