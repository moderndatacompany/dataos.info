# statsd

Pushes metrics using the [StatsD protocol](https://github.com/statsd/statsd). Supported tagging formats are 'none', 'datadog', and 'influxdb'.

```yaml
# Config fields, showing default values
metrics:
  statsd:
    address: ""
    flush_period: 100ms
    tag_format: none
  mapping: ""
```

The underlying client library has recently been updated in order to support tagging.

## Fields

### `address`

The address to send metrics to.

Type: `string`

Default: `""`

---

### `flush_period`

The time interval between metrics flushes.

Type: `string`

Default: `"100ms"`

---

### `tag_format`

Metrics tagging is supported in a variety of formats.

Type: `string`

Default: `"none"`

Options: `none`, `datadog`, `influxdb`.