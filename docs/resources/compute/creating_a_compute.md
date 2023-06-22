# Creating a Compute

This section covers a Compute YAML file structure,configuration options, and applying the YAML to create a Compute resource.

## Prerequisites

DataOS uses Kubernetes for cluster and container management. It supports creating/defining groups of VMs (node pools) that have a particular profile - A specific CPU, memory, and disk capacity. To get started with creating a Compute resource, you first need to provision a group of VMs and register those with Kubernetes.

<aside style="background-color:#FAF3DD; padding:15px; border-radius:5px;">
🗣️ Please get in touch with the Kubernetes administrator in your organization to create a node pool.

</aside>

## Compute YAML File
Once the node pool is established, you can associate it with DataOS by configuring a Compute resource using a YAML file. The YAML file requires appropriate settings to create the Compute resource. The subsequent sections elaborate on the necessary configurations.

### **Configuring the Resource Section**

A Compute is a type of resource in DataOS. Below is the YAML configuration for the Resource Section:
```yaml
name: {{my-workflow}}
version: v1 
type: workflow 
tags: 
  - {{dataos:type:resource}}
description: {{This is a sample workflow YAML configuration}}
owner: {{iamgroot}}
```
<center><i>Resource Section Configuration</i></center>

For detailed customization options and additional fields within the Resource Section, refer to the [Resource Configuration](../../resources.md).

### **Configuring the Compute-specific Section**

The Compute-specific Section contains configurations specific to the Compute resource. The general syntax for the Compute-specific section is provided below:

```yaml
compute:
  dataplane: {{hub}}
  purpose: {{runnable}}
  nodePool:
    nodeSelector:
      {{"dataos.io/purpose": "runnable"}}
    tolerations:
      - key: {{"dedicated"}}
        operator: {{"Equal"}}
        value: {{"runnable"}}
        effect: {{"NoSchedule"}}
```
DataOS supports three different categories of Compute: runnable, query, and gpu type. Each has its own YAML syntax, which is given [here.](./compute_templates.md)

## Applying the YAML to Create a Compute resource

Once the Compute YAML file is prepared, you can utilize the apply command to create a Compute resource within the DataOS environment. 

```bash
dataos-ctl apply -f <path/file-name>
```

After successfully creating a Compute resource, you can reference it in Minerva Clusters for query workloads and incorporate it within data processing workloads (such as workflows and services) using the compute field.