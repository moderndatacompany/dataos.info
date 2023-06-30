# Creating a Cluster Using CLI

Within the DataOS, we can create a Cluster using the Command Line Interface. Follow the below steps to create a cluster via this method:

## Create a YAML for Cluster

The first and foremost step is to create a YAML file. The properties to be defined in the YAML are elaborated here. The syntax of the YAML is given below:

```yaml
version: v1 
name: minervac 
type: cluster 
description: The yaml file for cluster 
tags: 
  - cluster
  - minerva
cluster: 
  compute: query-default01  
  runAsApiKey: <API KEY> 
	minerva: 
    replicas: 2 
    resources: 
      limits: 
        cpu: 4000m 
        memory: 8Gi
      requests: 
        cpu: 2000m
        memory: 4Gi
    debug: 
      logLevel: INFO 
      trinoLogLevel: ERROR 
    depots: 
      - address: dataos://icebase:default 
```

## Apply the Cluster YAML using DataOS CLI

To create a Cluster resource, you need to use the apply command on the CLI. The apply command for Cluster is given below:

```bash
dataos-ctl apply -f <cluster-yaml-file-path>
```

<aside>
🗣️ You cannot create separate clusters for different workspaces; a Cluster resource is defined globally in the DataOS.

</aside>