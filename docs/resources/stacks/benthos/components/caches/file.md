# file

Tags: Local

Stores each item in a directory as a file, where an item ID is the path relative to the configured directory.

## YAML Configurations

```yaml
# Config fields, showing default values
label: ""
file:
  directory: ""
```

This type currently offers no form of item expiry or garbage collection and is intended to be used for development and debugging purposes only.

## Fields[](https://www.benthos.dev/docs/components/caches/file#fields)

### `directory`[](https://www.benthos.dev/docs/components/caches/file#directory)

The directory within which to store items.

**Type:** `string`