# rate_limit

Throttles the throughput of a pipeline according to a specified [`rate_limit`](../../components/rate_limit.md) resource. Rate limits are shared across components and therefore apply globally to all processing pipelines.

```yaml
# Config fields, showing default values
label: ""
rate_limit:
  resource: ""
```

## Fields

### `resource`

The target [`rate_limit` resource](../../components/rate_limit.md).

Type: `string`

Default: `""`