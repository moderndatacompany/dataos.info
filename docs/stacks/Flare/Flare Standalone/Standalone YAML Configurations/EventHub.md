# **EventHub**

# **Read Config**

**Input Section Configuration for Reading from Pulsar Data Source**

```yaml
inputs:
  - name: input
    inputType: eventhub
    isStream: true
    eventhub:
      endpoint: ""
      eventhubName: "eventhub01"
      sasKeyName: ""
      sasKey: ""
      options:
        eventhubs.startingposition: "{\"offset\":\"-1\",\"seqNo\":-1,\"enqueuedTime\":null,\"isInclusive\":true}"
        eventhubs.consumergroup: "sample"
```

**Sample YAML for Reading from EventHub Data Source**

```yaml
version: v1
name: standalone-read-eventhub
type: workflow
tags:
  - standalone
  - readJob
  - eventhub
description: this jobs reads data from eventhub to iceberg
workflow:
  dag:
    - name: eventhub-write-b-02
      title: write data to eventhub
      description: write data from eventhub to iceberg
      spec:
        tags:
          - stanalone
          - readJob
          - eventhub
        stack: flare:3.0
        compute: runnable-default
        flare:
          job:
            explain: true
            logLevel: INFO

            streaming:
              checkpointLocation: /tmp/checkpoints/development01
              forEachBatchMode: false

            inputs:
              - name: input
                inputType: eventhub
                isStream: true
                eventhub:
                  endpoint: ""
                  eventhubName: "eventhub01"
                  sasKeyName: ""
                  sasKey: ""
                  options:
                    eventhubs.startingposition: "{\"offset\":\"-1\",\"seqNo\":-1,\"enqueuedTime\":null,\"isInclusive\":true}"
                    eventhubs.consumergroup: "sample"

            outputs:
              - name: input
                outputType: file
                file:
                  schemaName: retail
                  tableName: transactions_standalone_read
                  format: Iceberg
                  warehousePath: /data/examples/dataout/localFileDataSourceOutput/
                  options:
                    saveMode: append

            steps:
              - sequence:
                  - name: finalDf
                    sql: SELECT * FROM input
```

# **Write Config**

**Output Section Configuration for Writing to EventHub Data Source**

```yaml
outputs:
  - name: finalDf
    outputType: eventhub
    eventhub:
      endpoint: "{{ Namespace Name }}.servicebus.windows.net/"
      eventhubName: "eventhub01"
      sasKeyName: ""
      sasKey: ""
```

**Sample YAML for Writing to EventHub Data Source**

```yaml
version: v1
name: standalone-write-eventhub
type: workflow
tags:
  - standalone
  - writeJob
  - eventhub
description: this jobs reads data from file and writes to eventhub
workflow:
  dag:
    - name: standalone-eventhub-write
      title: write data to eventhub
      description: write data to eventhub
      spec:
        tags:
          - standalone
          - writeJob
          - eventhub
        stack: flare:3.0
        compute: runnable-default
        flare:
          job:
            explain: true
            logLevel: INFO

            streaming:
              checkpointLocation: /tmp/checkpoints/devd01
              forEachBatchMode: "true"

            inputs:
              - name: input
                inputType: file
                file:
                  path: /data/examples/default/transactions
                  format: json

            outputs:
              - name: finalDf
                outputType: eventhub
                eventhub:
                  endpoint: "{{ Namespace Name }}.servicebus.windows.net/"
                  eventhubName: "eventhub01"
                  sasKeyName: ""
                  sasKey: ""

            steps:
              - sequence:
                  - name: finalDf
                    sql: SELECT * FROM input
```