# Stack orchestrated by a Workflow declared using a Config Template

```yaml
name: "soda-v2"
version: v1alpha
type: stack
layer: user
description: "soda workflow stack version 2"
stack:
  name: soda
  version: "2.0"
  flavor: "python"
  reconciler: "stackManager"
  dataOsAddressJqFilters:
    - .inputs[].dataset
  secretProjection:
    type: "envVars"
  image:
    registry: docker.io
    repository: rubiklabs
    image: dataos-soda
    tag: 0.0.11-dev
    auth:
      imagePullSecret: dataos-container-registry
  command:
    - python3
  arguments:
    - main.py
    - --configuration
    - /etc/dataos/config/jobconfig.yaml
  environmentVars:
    PULSAR_TOPIC_ADDRESS: dataos://systemstreams:soda/data_quality_result
    RESOURCE_DIR_PATH: "/etc/dataos/resources"
  stackSpecValueSchema:
    jsonSchema: |
      {"$schema":"http://json-schema.org/draft-04/schema#","type":"object","properties":{"inputs":{"type":"array","items":[{"type":"object","properties":{"dataset":{"type":"string"},"checks":{"type":"array","additionalProperties":{"type":"object"}},"options":{"type":"object","additionalProperties":{"type":"string"}},"profile":{"type":"object","properties":{"columns":{"type":"array","minItems":1,"items":[{"type":"string"}]}},"required":["columns"]}},"required":["dataset"],"oneOf":[{"required":["checks","profile"]},{"required":["checks"],"not":{"allOf":[{"required":["profile"]}]}},{"required":["profile"],"not":{"allOf":[{"required":["checks"]}]}}]}]}},"required":["inputs"]}
  workflowJobConfig:
    configFileTemplate: |
      jobconfig.yaml: |
      {{ toYaml .ApplicationSpec.StackSpec | indent 2 }}
```