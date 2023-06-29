# json_api

Serves metrics as JSON object with the service-wide HTTP service at the endpoints `/stats` and `/metrics`.

```yaml
# Config fields, showing default values
metrics:
  json_api: {}
  mapping: ""
```

This metrics type is useful for debugging as it provides a human-readable format that you can parse with tools such as `jq`