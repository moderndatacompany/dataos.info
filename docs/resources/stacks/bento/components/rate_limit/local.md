# local

The local rate limit is a simple X every Y type rate limit that can be shared across any number of components within the pipeline but does not support distributed rate limits across multiple running instances of Bento.

```yaml
# Config fields, showing default values
label: ""
local:
  count: 1000
  interval: 1s
```

## Fields

### `count`

The maximum number of requests to allow for a given period of time.

Type: `int`

Default: `1000`

---

### `interval`

The time window to limit requests by.

Type: `string`

Default: `"1s"`