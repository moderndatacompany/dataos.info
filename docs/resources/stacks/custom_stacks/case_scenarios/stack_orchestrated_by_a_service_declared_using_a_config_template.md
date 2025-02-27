# Stack orchestrated by a Service declared using a Config Template

The following YAML manifest declares the Benthos Stack and orchestrates it via a Service as a containerized resource:

```yaml
name: "bento-v4"
version: v1alpha
type: stack
layer: user
description: "bento stack version 4"
stack:
  name: bento
  version: "4.0"
  reconciler: "stackManager"
  secretProjection:
    type: "propFile"
  image:
    registry: docker.io
    repository: rubiklabs
    image: benthos4
    tag: 0.0.20
    auth:
      imagePullSecret: dataos-container-registry
  command:
    - /opt/dataos/bento-ds
  arguments:
    - run
    - -c
    - /etc/dataos/config/jobconfig.yaml
  stackSpecValueSchema:
    jsonSchema: |
      {"$schema":"http://json-schema.org/draft-04/schema#","type":"object","properties":{"input":{"type":"object"},"metrics":{"type":"object"},"logger":{"type":"object"},"http":{"type":"object"},"pipeline":{"type":"object"},"output":{"type":"object"}},"required":["input"]}
  serviceConfig:
    configFileTemplate: |
      jobconfig.yaml: |
      {{ toYaml .ApplicationSpec.StackSpec | indent 2 }}
        logger:
         level: {{.ApplicationSpec.LogLevel}}
         add_timestamp: true
         format: json
         static_fields:
           '@service': {{.Name}}
        http:
         address: 0.0.0.0:{{.MetricPort}}
         root_path: /dataos-bento
         debug_endpoints: false
        metrics:
         prometheus:
            use_histogram_timing: false
            histogram_buckets: []
            add_process_metrics: false
            add_go_metrics: false
            push_url: "http://prometheus-pushgateway.sentinel.svc.cluster.local:9091"
            push_interval: "5s"
            push_job_name: "{{ .Name }}-{{ .Type }}{{ .Stamp }}"

  workerConfig:
    configFileTemplate: |
      jobconfig.yaml: |
      {{ toYaml .ApplicationSpec.StackSpec | indent 2 }}
        logger:
         level: {{.ApplicationSpec.LogLevel}}
         add_timestamp: true
         format: json
         static_fields:
           '@service': {{.Name}}
        http:
         address: 0.0.0.0:{{.MetricPort}}
         root_path: /dataos-bento
         debug_endpoints: false
        metrics:
         prometheus:
            use_histogram_timing: false
            histogram_buckets: []
            add_process_metrics: false
            add_go_metrics: false
            push_url: "http://prometheus-pushgateway.sentinel.svc.cluster.local:9091"
            push_interval: "5s"
            push_job_name: "{{ .Name }}-{{ .Type }}{{ .Stamp }}"
```