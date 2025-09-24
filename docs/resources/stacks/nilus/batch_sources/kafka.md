# Apache Kafka

The Apache Kafka Batch connector ingests messages from one or more Kafka topics into Nilus destinations. Data is collected in batches (size/time-based) and written into warehouses, databases, or lakes.

Nilus Batch in Apache Kafka is used to periodically deliver messages (such as JSON, Avro, Protobuf, etc.) to analytics destinations. It optionally integrates with the Confluent Schema Registry (or compatible alternatives) to manage Avro, Protobuf, and JSON Schema serialization.

## Prerequisites

The following are the requirements for enabling Batch Data Movement in Apache Kafka:

1. **Kafka access**
     * Reachable `bootstrap_servers` from the Nilus worker environment.
     * A **consumer group** (`group_id`) provisioned for the pipeline.
     * SASL/SSL authentication is configured if required.
2. **Topic permissions**
     * Read access to source topics.
     * Consumer group commits rights if offsets are shared.
3. **Schema Registry (optional but recommended when using Avro/Protobuf)**
     * A reachable **Schema Registry URL** (e.g., `http://schemaregistry:8081`).
     * Credentials (basic auth, bearer token, or mTLS certs, depending on cluster setup).
     * Proper subject naming strategy in Kafka producers to ensure compatibility (`<topic>-value` by default).
4.  **Source Address (Kafka)**

    Nilus connects to Kafka using either:

    * **Direct connection URI**
    * **DataOS Depot**, which manages connection details, credentials, and SSL/TLS centrally.

Nilus uses a URI-style source address:

=== "Syntax"
    ```yaml
    kafka://?bootstrap_servers=localhost:9092&group_id=test_group&security_protocol=SASL_SSL&sasl_mechanisms=PLAIN&sasl_username=example_username&sasl_password=example_secret&batch_size=1000&batch_timeout=3
    ```
=== "Example without Schema Registry"
    ```yaml
    kafka://?bootstrap_servers=broker-1:9092,broker-2:9092&group_id=nilus_kafka_etl
    ```
<!-- === "Example With Schema Registry"
    ```yaml
    kafka://?bootstrap_servers=broker-1:9092&group_id=nilus_kafka_etl
      &schema_registry_url=https://schemaregistry.company.com
      &schema_registry_username=schema_user
      &schema_registry_password=secret
    ``` -->

!!! info
    Instance Secrets can securely facilitate connections to Apache Kafka within the Nilus Workflow. To create an Instance Secret for your Nilus Workflow, contact the DataOS admin or DataOS Operator.

    ??? note "Apache Kafka Instance Secret Manifest"

        ```yaml
        name: ${kafka-name}-rw # Name of the instance-secret, indicating it's for read-only access.
        version: v1 # Manifest Version           
        type: instance-secret # Resource-type
        description: ${description} # Optional: Brief description of the instance-secret's purpose.
        layer: user # DataOS Layer
        instance-secret:
            - acl: rw
            type: key-value-properties
            data:
              security_protocol: ${{SASL_SSL}} #optional
              sasl_mechanism: ${{sasl_mechanism}} #optional
              trust_store_type: ${{trust_store_type}} #optional
              trust_store_password: ${{trust_store_password}} #optional
              username: ${{username}}
              password: ${{password}}
            files: #optional
              ca_file: "{{Local File path where .pem file is located}}"
              trust_store_file: "{{Local File path where cacerts file is located}}"
        ```



## Sample Workflow Config

```yaml
name: kafka-batch-aws3
version: v1
type: workflow
tags:
    - workflow
    - nilus-batch
description: Nilus Batch Service Sample
workflow:
  dag:
    - name: kafka-aws
      spec:
        stack: nilus:1.0
        compute: runnable-default
        resources:
          requests:
            cpu: 100m
            memory: 256Mi
        logLevel: Info
        envs:
          PAGE_SIZE: 50000
          LOADER_FILE_SIZE: 50000000
        stackSpec:
          source:
            address: dataos://testkafkadepot1?acl=rw&batch_size=10&batch_timeout=30&group_id=test_group
            options:
              source-table: "test-topic-secure"
              run-in-loop: true
          sink:
            address: dataos://testawslh
            options:
              dest-table: "sandbox4.kafka_aws_batch3"
              incremental-strategy: append 
```

!!! info
    Ensure that all placeholder values and required fields (e.g., connection `addresses`, `compute`, and access credentials) are properly updated before applying the configuration to a DataOS workspace.


Deploy the manifest file using the following command:

```bash
dataos-ctl resource apply -f ${{path to the Nilus Workflow YAML}}
```

## Supported Attribute Details

Nilus supports the following source options for Apache Kafka:

| Option              | Required | Description                           |
| ------------------- | -------- | ------------------------------------- |
| `source-table`      | Yes      | Kafka topic name                      |
| `batch_size`        | No       | Number of messages per batch          |
| `batch_timeout`     | No       | Time to wait for messages (seconds)   |
| Security/SSL params | No       | Authentication and encryption options |

### **Other URI parameters**

The following are the optional parameters available:

* `batch_size` : Number of messages per batch (default: 3000)
* `batch_timeout` : Timeout (seconds) for batch completion (default: 3)
* `security_protocol` : Security protocol (e.g., `SASL_SSL`, `PLAINTEXT`)
* `sasl_mechanisms` : SASL mechanism (e.g., `PLAIN`, `SCRAM-SHA-256`)
* `sasl_username` : Username for SASL authentication
* `sasl_password` : Password for SASL authentication
* `ssl_ca_location` : Path to CA certificate
* `ssl_certificate_location` : Path to client certificate
* `ssl_key_location` : Path to client key
* `ssl_key_password` : Password for client key
* `ssl_truststore_location` : Path to truststore file (legacy Java SSL)
* `ssl_truststore_password` : Truststore password
* `ssl_truststore_type` : Truststore type (`JKS`, `PKCS12`)

!!! info "Core Concepts"

    1.  **Consumer Groups**

        Kafka ingestion in Nilus is consumer group–based, with automatic partition assignment and offset management.

    2.  **Batch Processing**

        Messages are consumed in batches, with a configurable size and timeout.

    3.  **Message Handling**

        By default, messages are deserialized as JSON, with keys, timestamps, topic, partition, and offsets preserved.

    4.  **Security**

        Kafka connections support SASL authentication, SSL/TLS encryption, and FIPS-compliant certificate management.

