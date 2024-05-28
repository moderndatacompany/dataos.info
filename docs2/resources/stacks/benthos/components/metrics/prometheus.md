# prometheus

Host endpoints (`metrics` and `stats`) for Prometheus scraping.

## YAML Configurations

### Common Config

```yaml
# Common config fields, showing default values
metrics:
  prometheus: {}
  mapping: ""
```

### Advanced Config

```yaml
# All config fields, showing default values
metrics:
  prometheus:
    use_histogram_timing: false
    histogram_buckets: []
    add_process_metrics: false
    add_go_metrics: false
    push_url: ""
    push_interval: ""
    push_job_name: benthos_push
    push_basic_auth:
      username: ""
      password: ""
    file_output_path: ""
  mapping: ""
```

## Fields

### `use_histogram_timing`

Whether to export timing metrics as a histogram, if `false` a summary is used instead. When exporting histogram timings, the delta values are converted from nanoseconds into seconds in order to better fit within bucket definitions. For more information on histograms and summaries, refer to [this page.](https://prometheus.io/docs/practices/histograms/)

Type: `bool`

Default: `false`

---

### `histogram_buckets`

Timing metrics histogram buckets (in seconds). If left empty defaults to [DefBuckets](https://pkg.go.dev/github.com/prometheus/client_golang/prometheus#pkg-variables)

Type: `array`

Default: `[]`

---

### `add_process_metrics`

Whether to export process metrics such as CPU and memory usage in addition to Benthos metrics.

Type: `bool`

Default: `false`

---

### `add_go_metrics`

Whether to export Go runtime metrics such as GC pauses in addition to Benthos metrics.

Type: `bool`

Default: `false`

---

### `push_url`

An optional Push Gateway URL to push metrics to.

Type: `string`

Default: `""`

---

### `push_interval`

The period of time between each push when sending metrics to a Push Gateway.

Type: `string`

Default: `""`

---

### `push_job_name`

An identifier for push jobs.

Type: `string`

Default: `"benthos_push"`

---

### `push_basic_auth`

The Basic Authentication credentials.

Type: `object`

---

### `push_basic_auth.username`

The Basic Authentication username.

Type: `string`

Default: `""`

---

### `push_basic_auth.password`

The Basic Authentication password.

> 🗣 SECRET
This field contains sensitive information that usually shouldn't be added to a config directly, read our secrets page for more info.


Type: `string`

Default: `""`

---

### `file_output_path`

An optional file path to write all prometheus metrics on service shutdown.

Type: `string`

Default: `""`

---

## Push Gateway

The field `push_url` is optional and, when set, will trigger a push of metrics to a [Prometheus Push Gateway](https://prometheus.io/docs/instrumenting/pushing/) once Benthos shuts down. It is also possible to specify a `push_interval` which results in periodic pushes.

The Push Gateway is useful for when Benthos instances are short-lived. Do not include the "/metrics/jobs/..." path in the push URL.

If the Push Gateway requires HTTP Basic Authentication, it can be configured with `push_basic_auth`.