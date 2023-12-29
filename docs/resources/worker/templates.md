# Worker Templates

## Template 1

```yaml
name: benthos3-worker-sample-replicas
version: v1beta
type: worker
tags:
  - worker
  - dataos:type:resource
  - dataos:resource:worker
  - dataos:layer:user
  - dataos:workspace:public
description: Random User Console
owner: iamgroot
workspace: public
worker:
  tags:
    - worker
    - random-user
  replicas: 3
  stack: benthos-worker:3.0
  logLevel: DEBUG
  compute: runnable-default
  resources:
    requests:
      cpu: 100m
      memory: 128Mi
    limits:
      cpu: 1000m
      memory: 1024Mi
  runAsApiKey: '****************************************************************'
  runAsUser: iamgroot
  stackSpec:
    input:
      http_client:
        headers:
          Content-Type: application/octet-stream
        url: https://randomuser.me/api/
        verb: GET
    output:
      stdout:
        codec: |
          delim:
          -----------GOOD------------
```

## Template 2

```yaml
name: poros-indexer-worker
version: v1beta
type: worker
tags:
  - Scanner
description: >-
  The purpose of this workflow is to reactively scan workflows whenever a
  lifecycle event is triggered in hera.
owner: metis
workspace: public
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
  logLevel: INFO
  envs:
    DATAOS_RESOURCE_LIFECYCLE_EVENT_TOPIC: '****************************************************'
    DATAOS_RESOURCE_LIFECYCLE_EVENT_TOPIC_SUBS_NAME: '********************'
    DATAOS_TOPIC_COLLATED_RESOURCE_OFFSET: '******'
  compute: runnable-default
  resources:
    requests:
      cpu: 1000m
      memory: 1024Mi
    limits: {}
  runAsApiKey: '****************************************************************************'
  runAsUser: metis
  stackSpec:
    type: worker
    worker: poros_indexer
```