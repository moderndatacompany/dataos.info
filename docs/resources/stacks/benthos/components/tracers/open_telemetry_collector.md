# open_telemetry_collector

> 🗣 EXPERIMENTAL
This component is experimental and, therefore, subject to change or removal outside of major version releases.

Send tracing events to an [Open Telemetry collector](https://opentelemetry.io/docs/collector/).

## YAML Configurations

### Common Config

```yaml
# Common config fields, showing default values
tracer:
  open_telemetry_collector:
    http: []
    grpc: []
```

### Advanced Config

```yaml
# All config fields, showing default values
tracer:
  open_telemetry_collector:
    http: []
    grpc: []
    tags: {}
```

## Fields

### `http`

A list of http collectors.

Type: `array`

---

### `http[].url`

The URL of a collector to send tracing events to.

Type: `string`

Default: `"localhost:4318"`

---

### `grpc`

A list of grpc collectors.

Type: `array`

---

### `grpc[].url`

The URL of a collector to send tracing events to.

Type: `string`

Default: `"localhost:4317"`

---

### `tags`

A map of tags to add to all tracing spans.

Type: `object`

Default: `{}`