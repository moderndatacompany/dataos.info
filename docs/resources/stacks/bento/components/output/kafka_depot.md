# Kafka Depot

The Kafka Depot output type writes messages to a Kafka cluster and waits for acknowledgment before returning control to the input. It supports standard Kafka configurations such as brokers, topics, and authentication through SASL. A broker can be used to fan messages out to multiple outputs, including Kafka and optional debug sinks.

## YAML Configuration

```yaml
output:
  - broker:
      pattern: fan_out
      outputs:
        - kafka:
            addresses:
              - 20.193.133.234:9092
            topic: kafka_test01
            sasl:
              mechanism: PLAIN
              user: admin
              password: ${KAFKA_PASSWORD}   # supply via secret or env var
```

## Fields


### **`output`**

Root list of one or more outputs. A broker can be used to fan messages out to multiple sinks.

Type: `array`

---

### **`broker`**

Container for multiple outputs executed according to a pattern.

Type: `object`

---

### **`broker.pattern`**

Execution pattern for child outputs. The `fan_out` pattern writes each message to all listed outputs.

Type: `string`
Default: `fan_out`

---

### **`broker.outputs`**

Child outputs to execute under the broker.

Type: `array`

---

### **`kafka`**

Kafka output configuration. Messages are written to a Kafka topic using the provided broker list and authentication settings.

Type: `object`

---

### **`kafka.addresses`**

List of Kafka broker addresses to connect to. Each item must be in `host:port` format. Multiple brokers may be specified for high availability.

Type: `array`

```yaml
# Examples
addresses:
  - localhost:9092

addresses:
  - kafka1:9092
  - kafka2:9092
```

---

### **`kafka.topic`**

The Kafka topic to which messages are written.

Type: `string`

```yaml
# Example
topic: kafka_test01
```

---

### **`kafka.sasl`**

SASL authentication settings for connecting to Kafka.

Type: `object`

---

### **`kafka.sasl.mechanism`**

SASL mechanism used for authentication.

Type: `string`
Default: `PLAIN`

---

### **`kafka.sasl.user`**

SASL username.

Type: `string`

---

### **`kafka.sasl.password`**

SASL password. It must be provided securely (for example, through a secret or environment variable).

Type: `string`

```yaml
# Example
sasl:
  mechanism: PLAIN
  user: admin
  password: ${KAFKA_PASSWORD}
```
