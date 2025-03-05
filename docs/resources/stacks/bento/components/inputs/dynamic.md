# dynamic

A special broker type where the inputs are identified by unique labels and can be created, changed, and removed during runtime via a REST HTTP interface.

```yaml
# Config fields, showing default values
input:
  label: ""
  dynamic:
    inputs: {}
    prefix: ""
```

To GET a JSON map of input identifiers with their current uptimes, use the `/inputs` endpoint.

To perform CRUD actions on the inputs themselves, use POST, DELETE, and GET methods on the `/inputs/{input_id}` endpoint. When using POST, the body of the request should be a YAML configuration for the input; if the input already exists it will be changed.

## Fields

### `inputs`

A map of inputs to statically create.

Type: `object`

Default: `{}`

---

### `prefix`

A path prefix for HTTP endpoints that are registered.

Type: `string`

Default: `""`