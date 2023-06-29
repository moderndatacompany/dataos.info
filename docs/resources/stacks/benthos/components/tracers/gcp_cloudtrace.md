# gcp_cloudtrace

> 🗣 EXPERIMENTAL
This component is experimental and, therefore, subject to change or removal outside of major version releases.

Send tracing events to a [Google Cloud Trace](https://cloud.google.com/trace).

## YAML Configurations

### Common Config

```yaml
# Common config fields, showing default values
tracer:
  gcp_cloudtrace:
    project: ""
    sampling_ratio: 1
    flush_interval: ""
```

### Advanced Config

```yaml
# All config fields, showing default values
tracer:
  gcp_cloudtrace:
    project: ""
    sampling_ratio: 1
    tags: {}
    flush_interval: ""
```

## Fields

### `project`

The google project with Cloud Trace API enabled. If this is omitted, then the Google Cloud SDK will attempt auto-detect it from the environment.

Type: `string`

Default: `""`

---

### `sampling_ratio`

Sets the ratio of traces to sample. Tuning the sampling ratio is recommended for high-volume production workloads.

Type: `float`

Default: `1`

```yaml
# Examples

sampling_ratio: 1
```

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