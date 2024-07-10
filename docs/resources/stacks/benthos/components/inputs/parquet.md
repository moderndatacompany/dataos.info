# parquet

> 🗣 EXPERIMENTAL
This component is experimental and therefore subject to change or removal outside of major version releases.

Reads and decodes [Parquet files](https://parquet.apache.org/docs/) into a stream of structured messages.

## YAML Configurations

### Common Config

```yaml
# Common config fields, showing default values
input:
  label: ""
  parquet:
    paths: []
```

### Advanced Config

```yaml
# All config fields, showing default values
input:
  label: ""
  parquet:
    paths: []
    batch_count: 1
```

By default any BYTE_ARRAY or FIXED_LEN_BYTE_ARRAY value will be extracted as a byte slice (`[]byte`) unless the logical type is UTF8, in which case they are extracted as a string (`string`).

When a value extracted as a byte slice exists within a document which is later JSON serialized by default it will be base 64 encoded into strings, which is the default for arbitrary data fields. It is possible to convert these binary values to strings (or other data types) using Bloblang transformations such as `root.foo = this.foo.string()` or `root.foo = this.foo.encode("hex")`, etc.

## Fields

### `paths`

A list of file paths to read from. Each file will be read sequentially until the list is exhausted, at which point the input will close. Glob patterns are supported, including super globs (double star).

Type: `array`

```yaml
# Examples

paths: /tmp/foo.parquet

paths: /tmp/bar/*.parquet

paths: /tmp/data//*.parquet
```

---

### `batch_count`

Optionally process records in batches. This can help to speed up the consumption of exceptionally large files. When the end of the file is reached the remaining records are processed as a (potentially smaller) batch.

Type: `int`

Default: `1`