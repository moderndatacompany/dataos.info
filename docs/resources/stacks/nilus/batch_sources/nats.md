# NATS

NATS is an open-source messaging system designed for lightweight, secure, and high-performance communication. Its persistence layer, JetStream, provides capabilities for streaming, message replay, and work queue processing.

Nilus supports NATS with JetStream as a batch source, enabling ingestion of messages from a NATS subject into downstream systems.

## Prerequisites

The following are required to enable Batch Data Movement from NATS using Nilus:


1. **Permissions**

    The connecting client must be configured with the following access permissions:

    - Authorization to establish a connection with the NATS server
    - Authorization to subscribe to the specified subject
    - Access privileges for the associated JetStream stream
    

2. **Authentication**
  
    Nilus supports the following authentication methods:

    - **Username / Password**

        ```bash
        nats+jetstream://username:password@localhost:4222
        ```

    - **Token**

        ```bash
        nats+jetstream://token123@localhost:4222
        # or
        nats+jetstream://localhost:4222?token=token123
        ```

    - **NKeys**

        ```bash
        nats+jetstream://localhost:4222?nkeys_seed=SUAIBDPBAUTWCWBKIO6XHQNINK5FWJW4OHLXC3HQ2KFE4PEJUA44CNHTC4
        ```

3. **Source Address (NATS)**
   
    Nilus connects to NATS using a URI-style address as shown below:

    === "Syntax"
        ```yaml
        nats+jetstream://<auth>@<host>:<port>?subject=<subject>&batch_size=<batch_size>&timeout=<timeout>
        ```

    === "Example"
        ```yaml
        nats+jetstream://localhost:4222?subject=test&batch_size=100&timeout=10
        ```

<!-- !!! info
    Instance Secrets can securely facilitate connections to NATS within the Nilus Workflow. To create an Instance Secret for your Nilus Workflow, contact the DataOS admin or DataOS Operator.

    ??? note "NATS Instance Secret Manifest"
        ```yaml
        name: ${nats-name}-rw
        version: v1
        type: instance-secret
        description: ${description}
        layer: user
        instance-secret:
          - acl: rw
            type: key-value-properties
            data:
              username: ${{username}}
              password: ${{password}}
              nkeys_seed: ${{nkeys_seed}}
              host: ${{host}}
              port: ${{port}}
        ``` -->

## Sample Workflow Config

```yaml
name: nats-batch-pg3
version: v1
type: workflow
tags:
  - workflow
  - nilus-batch
description: Nilus Batch Service Sample
workflow:
  dag:
    - name: nats-pg
      spec:
        stack: nilus:1.0
        compute: runnable-default
        resources:
          requests:
            cpu: 100m
            memory: 256Mi
        logLevel: Info

        stackSpec:
          source:
            address: nats+jetstream://<host>:<port>?subject=test&batch_size=10000&timeout=10
            options:
              source-table: sample-stream-test
              run-in-loop: true
          sink:
            address: dataos://ncdcpostgres3
            options:
              dest-table: "abc_testing.nats_pg_batch3"
              incremental-strategy: append 
```

!!! info
    Ensure that all placeholder values and required fields (such as `host`, `subject`, `compute`, and credentials) are correctly updated before deploying in a DataOS workspace.

Deploy the manifest using the following command:

```bash
dataos-ctl resource apply -f ${{path to the Nilus Workflow YAML}}
```


## Supported Attribute Details 

Configure NATS as a **batch source** by defining the connection string (`nats+jetstream://...`) and setting the `source-table`, which maps to the JetStream stream name.


| Option           | Required | Default | Description                               |
| ---------------- | -------- | ------- | ----------------------------------------- |
| `subject`        | Yes      | —       | NATS subject to consume messages from     |
| `source-table`   | Yes      | —       | Used as the JetStream stream name         |
| `batch_size`     | No       | `100`   | Number of messages processed per batch    |
| `timeout`        | No       | `10`    | Timeout (seconds) for batch fetch         |
| `start_sequence` | No       | `1`     | Starting sequence for message consumption |
| `host` / `port`  | No       | —       | NATS server connection parameters         |


**Examples**

=== "Basic Connection"
    ```yaml
    source:
      address: nats+jetstream://localhost:4222?subject=test
      options:
        source-table: sample-stream
    ```

=== "With Username/Password and Batch Tuning"
    ```yaml
    source:
      address: nats+jetstream://user:pass@localhost:4222?subject=test&batch_size=1000&timeout=30
      options:
        source-table: sample-stream
    ```

=== "With Token Authentication"
    ```yaml
    source:
      address: nats+jetstream://localhost:4222?subject=test&token=your_token
      options:
        source-table: sample-stream
    ```



<!--

## Other Source Options

Nilus supports the following source options for NATS + JetStream:

| Option           | Required | Description                                 |
| ---------------- | -------- | ------------------------------------------- |
| `batch_size`     | No       | Number of messages per batch (default: 100) |
| `timeout`        | No       | Batch timeout in seconds (default: 10)      |
| `start_sequence` | No       | Starting JetStream sequence (default: 1)    |
| `host` / `port`  | No       | NATS server connection parameters           |


## Sink Configuration (Optional)

| Option                 | Required           | Description                                                | Callouts                       |
| ---------------------- | ------------------ | ---------------------------------------------------------- | ------------------------------ |
| `dest-table`           | Yes                | Destination table name (`schema.table`)                    | —                              |
| `incremental-strategy` | Yes                | Write mode (`append`, `replace`, or `merge`)               | `merge` requires `primary-key` |
| `primary-key`          | Required for merge | Column(s) used for deduplication                           | —                              |
| `create-table`         | No                 | Auto-create destination table if missing (default: `true`) | —                              |

**Example Sink Config**

```yaml
sink:
  address: dataos://testawslh
  options:
    dest-table: athena_retail.orders_snapshot
    incremental-strategy: replace
``` -->


### **Best Practices**

- Use **dedicated subjects** for ingestion to isolate ETL pipelines.
- Tune **batch_size** and **timeout** based on message volume and downstream capacity.
- Monitor **JetStream stream metrics** (e.g., pending messages, sequence lag).
- Ensure **replay policies** in NATS align with Nilus expectations for message delivery.
- Keep authentication credentials secure using **Instance Secrets**.


!!! info "Core Concepts"

    1. **Sequence-Based Consumption**

        Nilus implements a sequence-based consumption model, functionally equivalent to offset-based consumption in distributed messaging systems.

        - Messages are identified and processed using sequence numbers.
        - Explicit ACKs are not required; message positions are auto-committed.
        - Batch pulling is supported with configurable batch sizes.
        - Resume functionality is enabled through persisted sequence tracking.

    2. **Consumer Behavior**

        Nilus provisions **ephemeral JetStream consumers** with the following configuration:

        - **Delivery Policy:** Start at a specified sequence number.
        - **Acknowledgment Policy:** None (auto-commit enabled).
        - **Replay Policy:** Immediate message delivery.
        - **Filter Subject:** Defined by the configured `subject` value.

