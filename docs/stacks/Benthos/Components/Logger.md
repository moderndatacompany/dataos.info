# Logger

Benthos logging prints to stdout (or stderr if your output is stdout) and is formatted as [logfmt](https://brandur.org/logfmt) by default. Use these configuration options to change both the logging formats as well as the destination of logs.

## YAML Configurations

### Logfmt to Stdout

```yaml
logger:
  level: INFO
  format: logfmt
  add_timestamp: false
  static_fields:
    '@service': benthos
```

### JSON to File

```yaml
logger:
  level: WARN
  format: json
  file:
    path: ./logs/benthos.ndjson
    rotate: true
```

## Fields

### `level`

Set the minimum severity level for emitting logs.

Type: `string`

Default: `"INFO"`

Options: `OFF`, `FATAL`, `ERROR`, `WARN`, `INFO`, `DEBUG`, `TRACE`, `ALL`, `NONE`.

---

### `format`

Set the format of emitted logs.

Type: `string`

Default: `"logfmt"`

Options: `json`, `logfmt`.

---

### `add_timestamp`

Whether to include timestamps in logs.

Type: `bool`

Default: `false`

---

### `timestamp_name`

The name of the timestamp field added to logs when `add_timestamp` is set to `true` and the `format` is `json`.

Type: `string`

Default: `"time"`

---

### `message_name`

The name of the message field added to logs when the the `format` is `json`.

Type: `string`

Default: `"msg"`

---

### `static_fields`

A map of key/value pairs to add to each structured log.

Type: map of `string`

Default: `{"@service":"benthos"}`

---

### `file`

<aside>
🗣 EXPERIMENTAL

</aside>

Specify fields for optionally writing logs to a file.

Type: `object`

---

### `file.path`

The file path to write logs to, if the file does not exist it will be created. Leave this field empty or unset to disable file based logging.

Type: `string`

Default: `""`

---

### `file.rotate`

Whether to rotate log files automatically.

Type: `bool`

Default: `false`

---

### `file.rotate_max_age_days`

The maximum number of days to retain old log files based on the timestamp encoded in their filename, after which they are deleted. Setting to zero disables this mechanism.

Type: `int`

Default: `0`