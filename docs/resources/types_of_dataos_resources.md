# Types of DataOS Resources

The categorization of Resources in DataOS is based on the concept of Workspace. **Workspace** is like a tenant in DataOS. You can use it to create isolated work environments for your or your team’s work. By default, all Resources are created in the *public workspace*.

## Workspace-level Resources

These Resources are defined, applied and updated in a specific Workspace. This allows the Workspace operators to limit their usage to that specific Workspace. Concurrently, it also provides them with the flexibility to allow the users of a different Workspace to use the same Resources.

The following Resources are considered Workspace-level Resources:

### **Cluster**

A DataOS Resource to create, manage and optimize computational resources & configurations for both simple & advanced analytics and data processing. You will find the details on the following link: [Cluster.](./cluster.md)

### **Secret**

The Resource to store sensitive information such as passwords, tokens or keys in the internal vault of DataOS, and use this information later without sharing the sensitive data itself.
Read about Secret on the following page: [Secret.](./secret.md)

### **Service**

Service can be conceptualized as a long-running process that is receiving or/and serving an API, or even a UI. It can be used for scenarios that need a continuous flow of real-time data, such as event processing, streaming IoT and more. You will find the details of this *runnable resource* here: [Service.](./service.md)

### **Workflow**

Workflow is a manifestation of a Directed Acyclic Graph, which helps you to streamline and automate the process of working with big data. A data ingestion or processing task carried out as a batch is referred to as a *job*. Jobs are defined and executed through Workflow. Learn the details of the Workflow here: [Workflow.](./workflow.md)

---

## Cluster-level Resources

These Resources can be visualized as being global throughout the operating system. They cannot be defined just for a particular Workspace. Once created, they become available to authorized users of all Workspaces.

The following Resources come into this category:

### **Compute**

Compute is essentially a node pool of homogeneous virtual machines. They allow you to configure the processing power associated with your data workloads. Read about them in detail on the following page: [Compute.](./compute.md)

### **Depot**

Depots provide you with a uniform way to connect with the variety of data sources in your organization. Depots abstract away the different protocols and complexities of the source systems to present a common taxonomy and method to address these source systems. Learn how to create & use depots on this link: [Depot.](./depot.md)

### **Policy**

Policy is a set of rules which governs the behavior of a user(person or application/service). Broadly, you can create and manage two kinds of policies in DataOS - **Access Policy** & **Data Policy**. They have been elaborated on this page: [Policy.](./policy.md)

### **Stack**

Stacks are the programming paradigms used to support the processing and management of data. They also act as the secondary extension points for our runnable resources, Workflow and Service. The following page contains detailed information on all the stacks you can currently leverage in DataOS: [Stacks.](./stacks.md)
