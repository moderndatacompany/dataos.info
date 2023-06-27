# Pulsar


# Pre-requisites

## Get the `pulsar-admin` tag

To read/write from environment pulsar within the DataOS you require the pulsar-admin tags. To check the list of available tags, execute the command

```bash
dataos-ctl user get
# Output
			NAME     |     ID      |  TYPE  |        EMAIL         |              TAGS               
---------------|-------------|--------|----------------------|---------------------------------
	  IamGroot   |   iamgroot  | person |  iamgroot@tmdc.io    | roles:direct:collated,                                          
               |             |        |                      | roles:id:data-dev,              
               |             |        |                      | roles:id:depot-manager,         
               |             |        |                      | roles:id:depot-reader,          
               |             |        |                      | **roles:id:pulsar-admin**,    # this is the Pulsar-admin tag     
               |             |        |                      | roles:id:system-dev,            
               |             |        |                      | roles:id:user,                  
               |             |        |                      | users:id:iamgroot
```

In case you don’t have the required tag please contact the system-administrator

## Environment Variables for Pulsar

```yaml
envs:
	PULSAR_SSL: <boolean>
	ENABLE_PULSAR_AUTH: <boolean>
```

Without these environment variables, the job will fail to establish a connection with the Pulsar in standalone mode.

# Read Config

**Input Section Configuration for Reading from Pulsar Data Source**

```yaml
inputs:
  - name: transactions_connect
    inputType: pulsar
    pulsar:
			# the <ip> and <port> for serviceUrl and adminUrl can be obtained from Operations App
      serviceUrl: pulsar://<ip>:<port> # e.g. pulsar://192.168.1.190:6500
      adminUrl: http://<ip>:<port> # e.g. http://192.168.1.190x:6500
			DATAOS_RUN_AS_APIKEY: <dataos-apikey> # can be obtained from `dataos-ctl user apikey get` command
    topic: transactions
```

**Sample YAML for Reading from Pulsar Data Source**

```yaml
version: v1
name: standalone-read-pulsar
type: workflow
tags:
  - standalone
  - readJob
  - pulsar
description: Sample job
workflow:
  dag:
    - name: customer
      title: Sample Transaction Data Ingester
      description: The job ingests customer data from pulsar topic to file source
      spec:
        tags:
          - standalone
          - readJob
          - pulsar

        envs: # Environment Variables
          PULSAR_SSL: true
          ENABLE_PULSAR_AUTH: true
					DATAOS_RUN_AS_APIKEY: <apikey> #can be obtained from `dataos-ctl user apikey get` command

        stack: flare:3.0
        compute: runnable-default
        tier: connect
        flare:
          job:
            explain: true
            logLevel: INFO

            streaming:
              checkpointLocation: /tmp/checkpoints/pulsar
              forEachBatchMode: true

            inputs: # Read from Pulsar
              - name: transactions_connect
                inputType: pulsar
                pulsar:
                  serviceUrl: pulsar+ssl://tcp.<dataos-context-full-name>:<port>
                  adminUrl: https://tcp.<ip>:<port>
                  tenant: public
                  namespace: default
                  topic: transactions123
                  isBatch: true

            outputs: # Write to Local
              - name: finalDf
                outputType: file
                file:
                  format: iceberg
                  warehousePath: /data/examples/dataout/pulsardata/
                  schemaName: default
                  tableName: trans_oms_data3
                  options:
                    saveMode: append

            steps:
              - sequence:
                  - name: finalDf
                    sql: SELECT * FROM transactions_connect
```

# Write Config

**Output Section Configuration for Writing to Pulsar Data Source**

```yaml
outputs: 
	- name: finalDf
	  outputType: pulsar
	  pulsar:
      serviceUrl: pulsar://<ip>:<port> # e.g. pulsar://192.168.1.190:6500
      adminUrl: http://<ip>:<port> # e.g. http://192.168.1.190x:6500
	    topic: transactions
```

**Sample YAML for Writing to Pulsar Data Source**

```yaml
version: v1
name: standalone-write-pulsar
type: workflow
tags:
  - standalone
  - writeJob
  - pulsar
title: Write to pulsar in standalone mode
description: |
  The purpose of this workflow is to read data from local and write to pulsar

workflow:
  dag:
    - name: standalone-pulsar-write
      title: Write to pulsar using standalone mode
      description: |
        The purpose of this job is to read data from local and write to pulsar
      spec:
        tags:
          - standalone
          - writeJob
          - pulsar

        envs: # Environment Variables
          PULSAR_SSL: true
          ENABLE_PULSAR_AUTH: true
					DATAOS_RUN_AS_APIKEY: <apikey> # can be obtained from `dataos-ctl user apikey get` command

        stack: flare:3.0
        compute: runnable-default
        flare:
          job:
            explain: true
            logLevel: INFO

            inputs: # Read from Local
              - name: oms_transactions_data
                inputType: file
                file:
                  path: /data/examples/default/transactions/
                  format: json

            outputs: # Write to Pulsar
              - name: finalDf
                outputType: pulsar
                pulsar:
						      serviceUrl: pulsar://<ip>:<port> # e.g. pulsar://192.168.1.190:6500
						      adminUrl: http://<ip>:<port> # e.g. http://192.168.1.190x:6500
                  topic: transactions123

            steps:
              - sequence:
                  - name: finalDf
                    sql: SELECT * FROM oms_transactions_data LIMIT 10
```

Table of Contents