# Scanner for DataOS Resources Metadata 

DataOS Resources Metadata Scanner Worker is a continuous running service to read the metadata across Workflows, Services, Clusters, Depots, etc., including their historical runtime and operations data, and saves it to the Metis DB whenever a DataOS Resource is created, deleted within DataOS.

This worker operates reactively to scan specific DataOS Resource information from Poros whenever a lifecycle event is triggered. It captures relevant details and publishes them to the Metis DB, ensuring an up-to-date repository of DataOS Resources metadata. The manifest configuration for the DataOS Resources Metadata Scanner are as follows:

```yaml
name: poros-indexer
version: v1beta
type: worker
tags: 
  - Scanner
description: 
  The purpose of this worker is to reactively scan metadata for DataOS Resources whenever a
  lifecycle event is triggered.
owner: metis
workspace: system
worker: 
  title: Workflow Indexer
  tags: 
    - Scanner
  replicas: 2
  autoScaling: 
    enabled: true
    minReplicas: 2
    maxReplicas: 3
    targetMemoryUtilizationPercentage: 120
    targetCPUUtilizationPercentage: 120
  stack: scanner:2.0
  stackSpec: 
    type: worker
    worker: poros_indexer
  logLevel: INFO
  compute: runnable-default
  runAsUser: metis

```
The above sample manifest file is deployed using the following command:

```bash
dataos-ctl resource apply -f ${{path to the Scanner YAML}}
```


**Updating the Scanner Workflow**:

If the Depot or Scanner configurations are updated, the Scanner must be redeployed after deleting the previous instance. Use the following command to delete the existing Scanner:

```bash 
  dataos-ctl delete -f ${{path-to-Scanner-YAML}}]
```

**OR**

```bash
  dataos-ctl delete -t workflow -n ${{name of Scanner}} -w ${{name of workspace}}
```


!!! info "**Best Practice**"

    As part of best practices, it is recommended to regularly delete Resources that are no longer in use. This practice offers several benefits, including saving time and reducing costs.