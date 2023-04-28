# **Creating a Cluster Using CLI**

Within the DataOS, we can create a Cluster using the Command Line Interface. Follow the below steps to create a cluster via this method:

## **Step 1: Create a YAML for Cluster**

The first and foremost step is to create a YAML file. The [properties](../Cluster.md) to be defined in the YAML are elaborated in the section at the end. The syntax of the YAML is given below:

```yaml
version: v1 # Version
name: minervac # Name of the Resource (Here its a Cluster)
type: cluster # Type of Resource (Here its a Cluster)
description: The yaml file for cluster # Description of the Resource (Cluster)
tags: # Tags
  - cluster
  - minerva
cluster: # Cluster Specific Section
  compute: query-default01  # Compute referred by the Cluster
  runAsApiKey: <API KEY> # Run
	minerva: 
    replicas: 2 # Number of Replicas
    resources: # Resources (CPU and Memory)
      limits: # Maximum Limit of the Resources
        cpu: 4000m 
        memory: 8Gi
      requests: # Requested Resources
        cpu: 2000m
        memory: 4Gi
    debug: # Debug Level
      logLevel: INFO # Log Level
      trinoLogLevel: ERROR # Trino Log Level
    depots: # Depots 
      - address: dataos://icebase:default # Depot Address
```

## **Step 2: Apply the Cluster YAML using DataOS CLI**

To create a Cluster resource, you need to use the apply command on the CLI. The apply command for cluster is given below:

```bash
dataos-ctl apply -f <cluster-yaml-file-path>
```

> 🗣️ You cannot create separate clusters for different workspaces, a Cluster resource is defined defined globally in the DataOS.