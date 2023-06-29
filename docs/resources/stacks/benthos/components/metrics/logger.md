# logger

> 🗣 BETA

This component is mostly stable but breaking changes could still be made outside of major version releases if a fundamental problem with the component is found.

Prints aggregated metrics through the logger.

```yaml
# Config fields, showing default values
metrics:
  logger:
    push_interval: ""
    flush_metrics: false
  mapping: ""
```

Prints each metric produced by Benthos as a log event (level `info` by default) during shutdown, and optionally on an interval.

This metrics type is useful for debugging pipelines when you only have access to the logger output and not the service-wide server. Otherwise it's recommended that you use either the `prometheus` or `json_api`types.

## Fields

### `push_interval`

An optional period of time to continuously print all metrics.

Type: `string`

Default: `""`

---

### `flush_metrics`

Whether counters and timing metrics should be reset to 0 each time metrics are printed.

Type: `bool`

Default: `false`