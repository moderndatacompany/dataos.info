# How to orchestrate a Hightouch pipeline using Hightouch Factory Operator?

The Hightouch Operator facilitates the programmatic orchestration and monitoring of the state cycle of the **hightouch-pipeline** from the DataOS CLI interface within the **Hightouch Factory**.

> This section outlines the steps for the Hightouch Factory Pipeline, which are analogous to the ADF Factory Pipeline. To prevent redundancy, consult the ADF Pipeline for supplementary information: <a href="/resources/operator/#how-to-create-an-operator">How to create an Operator?</a>
> 

## Prerequisite

### **Hightouch Operator Image in the Container Registry**

To manage the lifecycle of a hightouch-pipeline from DataOS, a Hightouch Factory Operator Image within the container registry of the organization is essential.

<aside class="callout">
🗣 The default Hightouch Factory Operator Image encompasses a set of functionalities, extendable by modifying the Image code. For additional information, kindly reach out to Modern’s DataOS Administrator.

</aside>

## Steps

Orchestrating a hightouch pipeline involves a series of logical steps as delineated below:

1. [YAML Manifest for Hightouch Factory Operator](#yaml-manifest-for-hightouch-factory-operator)
2. [Apply the Operator YAML](#apply-the-operator-manifest)
3. [Verify Operator creation](#verify-operator-creation)
4. [YAML Manifest for Resource (Hightouch pipeline)](#yaml-manifest-for-resource-hightouch-pipeline)
5. [Apply the Resource manifest](#apply-the-resource-yaml)
6. [Retrieve status of Resource](#get-status-of-pipeline-run)

### **YAML manifest for Hightouch Factory Operator**

The Hightouch Resource YAML manifest is provided in the codeblock below:

```yaml
# Resource meta section
name: hightouch-factory
version: v1alpha
type: operator
layer: user
description: provides management of hightouch sync resource lifecyle
tags:
  - operator
  - hightouch

# Operator-specific section
operator:
	
	# NATS cluster configuration
  natsClusterConfig:
    name: hightouchnats
    compute: runnable-default
    runAsUser: minerva-cluster

	# Computational components
  components:
    - name: hightouch-controller
      type: worker
      compute: runnable-default
      runAsUser: minerva-cluster
      image: docker.io/rubiklabs/hightouch-operator:0.0.3-dev
      imagePullSecret: dataos-container-registry
      command:
        - /opt/tmdc-io/hightouch-operator
      arguments:
        - operator
        - sync
        - --electionStateFile
        - /opt/tmdc-io/leader-election.log
      replicas: 1
      environmentVars:
        LOG_LEVEL: info
        METRIC_PORT: 30001
        ELECTION_CLUSTER_NAME: hightouch-operators
        ELECTION_CLUSTER_SIZE: 1
        OPERATOR_MAX_WORKERS: 1
        OPERATOR_RECONCILE_WORKERS_INTERVAL: 10s
        OPERATOR_MAINTENANCE_INTERVAL: 1m
        OPERATOR_PURGE_STATE_STORE_BEFORE: 5m
        OPERATOR_STATE_STORE_TYPE: jetstream_kv
        MESSAGE_DURABILITY: true
        ENTITY_OF_INTEREST_MESSAGE_QUEUE: hightouch-entities-12121
        ENTITY_OF_INTEREST_MESSAGE_STREAM: dataos-hightouch-entities
        ENTITY_OF_INTEREST_MESSAGE_COMMAND_SUBJECT: hightouch.pipeline.run
        ENTITY_OF_INTEREST_MESSAGE_QUERY_SUBJECT: hightouch.pipeline.run.query
        ENTITY_OF_INTEREST_MESSAGE_QUERY_REPLY_SUBJECT: dataos.operator.hightouch.reply
        HIGHTOUCH_SERVICE_URL: https://api.hightouch.com
        HIGHTOUCH_SERVICE_BASE_PATH: /api/v1
        HIGHTOUCH_SERVICE_SECRET: 029aa630-30d3-4320-adc3-d3879c0d0d5b
      ports:
        - name: metrics
          servicePort: 30001
          targetPort: 30001

	# Resource configuration
  resources:
    - name: hightouch
      isRunnable: true
      specSchema:
        jsonSchema: |
          {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "$id": "https://example.com/schemas/data-model-schema",
            "type": "object",
            "properties": {
              "model": {
                "type": "object",
                "properties": {
                  "name": {
                    "type": "string"
                  },
                  "slug": {
                    "type": "string"
                  },
                  "queryType": {
                    "type": "string"
                  },
                  "sourceId": {
                    "type": "string"
                  },
                  "isSchema": {
                    "type": "boolean"
                  },
                  "primaryKey": {
                    "type": "string"
                  },
                  "visual": {
                    "type": "object"
                  },
                  "custom": {
                    "type": "object"
                  },
                  "table": {
                    "type": "object"
                  },
                  "raw": {
                    "type": "object"
                  },
                  "folderId": {
                    "type": "string"
                  },
                  "dbt": {
                    "type": "object"
                  }
                },
                "required": [
                  "name",
                  "slug",
                  "queryType",
                  "sourceId",
                  "isSchema",
                  "primaryKey"
                ],
                "additionalProperties": false
              },
              "sync": {
                "type": "object",
                "properties": {
                  "slug": {
                    "type": "string"
                  },
                  "configuration": {
                    "type": "object"
                  },
                  "destinationId": {
                    "type": "string"
                  },
                  "schedule": {
                    "type": [
                      "object"
                    ]
                  },
                  "disabled": {
                    "type": "boolean"
                  }
                },
                "required": [
                  "slug",
                  "configuration",
                  "destinationId",
                  "disabled"
                ],
                "additionalProperties": false
              },
              "trigger": {
                "type": "object",
                "properties": {
                  "syncSlug": {
                    "type": "string"
                  },
                  "resetCDC": {
                    "type": "boolean"
                  },
                  "fullResync": {
                    "type": "boolean"
                  },
                  "syncId": {
                    "type": "string"
                  }
                },
                "additionalProperties": false
              }
            },
            "required": [
              "model",
              "sync",
              "trigger"
            ],
            "additionalProperties": false
          }
      natsApi:
        command:
          stream: dataos-hightouch-entities
          subject: hightouch.pipeline.run
        query:
          subject: hightouch.pipeline.run.query
          replySubject: dataos.operator.hightouch.reply

	# Workspace configuration 
  enabledWorkspaces:
    - public
    - sandbox
```

For more information about the various sections, refer to the link: [YAML manifest for Operator.](/resources/operator/#yaml-manifest-for-operator)

### **Apply the Operator manifest**

After creating the YAML file for the Operator Resource, it's time to apply it to instantiate the Resource-instance in the DataOS environment. To apply the Operator YAML file, utilize the `apply` command.

```shell
dataos-ctl apply -f {{operator yaml manifest file path}}
```

### **Verify Operator Creation**

To ensure that your operator has been successfully created, you can verify it in two ways:

Check the name of the newly created depot in the list of depots where you are named as the owner:

```shell
dataos-ctl get -t operator

# Expected Output
INFO[0000] 🔍 get...                                     
INFO[0000] 🔍 get...complete                             

         NAME        | VERSION |   TYPE   | WORKSPACE | STATUS | RUNTIME |  OWNER        
---------------------|---------|----------|-----------|--------|---------|-------------------
  hightouch-operator | v1alpha | operator |           | active |         | iamgroot    
```

Alternatively, retrieve the list of all operators created in your organization:

```shell
dataos-ctl get -t operator -a
```

You can also access the details of any created Operator through the DataOS GUI in the [Operations App.](../../../interfaces/operations.md)

### **YAML manifest for Resource (Hightouch pipeline)**

Now once we have created an Operator, we would need to create a Resource (external Resource) which is a Hightouch pipeline that would be managed by this Operator. Below is the Resource YAML for the external Hightouch pipeline Resource:

```yaml
# Resource meta section
version: v1beta
name: pipeline-01
type: resource
tags:
  - hightouch-pipeline
  - hightouch-operator
description: hightouch-pipeline resource

# Resource-specific section
resource:
  operator: hightouch-factory
  type: hightouch
  spec:
    model:
      name: "city-retail-01"
      slug: "city-retail-01"
      queryType: "raw_sql"
      sourceId: "23474"
      isSchema: false
      primaryKey: "__metadata"
      raw:
        sql: "SELECT * FROM icebase.retail.city LIMIT 10000"
    sync:
      slug: "icebase-excel-01"
      "configuration":
        "mode": "mirror"
        "driveId": "me/drive"
        "mappings": [ ]
        "workbookId": "014W54IBU6FZWIKUZNXZAYB35OCXH7DD3Z"
        "worksheetId": "{00000000-0001-0000-0000-000000000000}"
        "configVersion": 0
        "autoSyncColumns": true
        "workbookSelection": "select"
      "destinationId": "80565"
      "schedule":
        "type": "cron"
        "schedule":
          "expression": "*/5 * * * *"
#      "schedule": null
      "disabled": false
    trigger:
      "resetCDC": false
      "fullResync": false
```

### **Apply the Resource YAML**

To trigger a pipeline run, you can apply the Resource YAML using the following command:

```shell
dataos-ctl apply -f {{resource-yaml-file-path}} -w {{workspace}}

# Sample
dataos-ctl apply -f ../adf-operator/resource.yaml -w public
```

### **Get Status of Pipeline Run**

```shell
dataos-ctl get -t resource -w {{workspace}}

# Sample
dataos-ctl get -t resource -w public

# Expected Output
INFO[0000] 🔍 get...                                     
INFO[0000] 🔍 get...complete                             

      NAME       | VERSION |   TYPE   | WORKSPACE | STATUS |  RUNTIME   |   OWNER        
-----------------|---------|----------|-----------|--------|------------|-------------------
  pipeline-run-1 | v1alpha | resource | public    | active | inprogress |  iamgroot  
```