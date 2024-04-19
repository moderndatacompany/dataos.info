# jaeger

Send tracing events to a [Jaeger](https://www.jaegertracing.io/) agent or collector.

## YAML Configurations

### Common Config

```yaml
# Common config fields, showing default values
tracer:
  jaeger:
    agent_address: ""
    collector_url: ""
    sampler_type: const
    flush_interval: ""
```

### Advanced Config

```yaml
# All config fields, showing default values
tracer:
  jaeger:
    agent_address: ""
    collector_url: ""
    sampler_type: const
    sampler_param: 1
    tags: {}
    flush_interval: ""
```

## Fields

### `agent_address`

The address of a Jaeger agent to send tracing events to.

Type: `string`

Default: `""`

```yaml
# Examples

agent_address: jaeger-agent:6831
```

---

### `collector_url`

The URL of a Jaeger collector to send tracing events to. If set, this will override `agent_address`.

Type: `string`

Default: `""`

```yaml
# Examples

collector_url: https://jaeger-collector:14268/api/traces
```

---

### `sampler_type`

The sampler type to use.

Type: `string`

Default: `"const"`

| Option | Summary |
| --- | --- |
| const | Sample a percentage of traces. 1 or more means all traces are sampled, 0 means no traces are sampled, and anything in between means a percentage of traces are sampled. Tuning the sampling rate is recommended for high-volume production workloads. |

---

### `sampler_param`

A parameter to use for sampling. This field is unused for some sampling types.

Type: `float`

Default: `1`

---

### `tags`

A map of tags to add to tracing spans.

Type: `object`

Default: `{}`

---

### `flush_interval`

The period of time between each flush of tracing spans.

Type: `string`

Default: `""`