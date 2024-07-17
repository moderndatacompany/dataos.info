# How to Creat a Stream Monitor?

Stream Monitor is suitable to observe the streaming data E.g. Fastbase topic.

**Configuring Stream Monitor**

This sample configuration demonstrates how the Stream Monitor raises an incident whenever the temperature exceeds 24 degrees.

```yaml
version: v1beta
name: pods-stream-monitor1
type: worker
tags:
  - pod
  - stream
  - monitor
description: observing the temprature in a sample streaming data.
worker:
  stack: stream-monitor
  compute: runnable-default
  replicas: 1
  resources:
    requests:
      cpu: 100m
      memory: 100Mi
    limits:
      cpu: 200m
      memory: 200Mi
  stackSpec:
    type: stream_monitor
    incident:
      type: pulsar
      name: stream-monitor-incident
      summary: 'stream monitor incident, found a specific pod'
      category: stream
      severity: warning
    stream:
      source:
        fastbase:
          topic: persistent://public/default/data_dog_data
          maxWorkers: 100
          subscriptionName: pods-stream-monitor-125-001
          subscriptionPosition: latest
      conditions:
      - valueJqFilter: '.payload.temp'
        operator: greater_than
        value: '24.0'
```
To know more about the specific attributes, [refer to this](/resources/monitor/configurations/).