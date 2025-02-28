# Kafka

```yaml
output:
    broker:
      pattern: fan_out
      outputs:
      - kafka:
          addresses:
            - 20.193.133.234:9092
          topic: kafka_test01
          sasl:
            mechanism: PLAIN
            user: admin
            password: 0b9c4dd98ca9cc944160
```