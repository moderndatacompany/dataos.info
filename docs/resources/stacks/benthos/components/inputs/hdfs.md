# hdfs

Reads files from an HDFS directory, where each discrete file will be consumed as a single message payload.

```yaml
# Config fields, showing default values
input:
  label: ""
  hdfs:
    hosts: []
    user: ""
    directory: ""
```

### Metadata

This input adds the following metadata fields to each message:

```
- hdfs_name
- hdfs_path
```

You can access these metadata fields using function interpolation.

## Fields

### `hosts`

A list of target host addresses to connect to.

Type: `array`

Default: `[]`

---

### `user`

A user ID to connect as.

Type: `string`

Default: `""`

---

### `directory`

The directory to consume from.

Type: `string`

Default: `""`