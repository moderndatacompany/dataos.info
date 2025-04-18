# logs in Bento

Prints a log event for each message. Messages always remain unchanged. The log message can be set using function interpolations described in the documentation which allows to log the contents and metadata of messages.

```yaml
# Config fields, showing default values
label: ""
log:
  level: INFO
  fields_mapping: ""
  message: ""
```

The `level` field determines the log level of the printed events and can be any of the following values: TRACE, DEBUG, INFO, WARN, ERROR.

### Structured Fields

It's also possible add custom fields to logs when the format is set to a structured form such as `json` or `logfmt` with the config field [`fields_mapping`](#fields_mapping):

```yaml
pipeline:
  processors:
    - log:
        level: DEBUG
        message: hello world
        fields_mapping: |
          root.reason = "cus I wana"
          root.id = this.id
          root.age = this.user.age
          root.kafka_topic = meta("kafka_topic")
```

## Fields

### `level`

The log level to use.

Type: `string`

Default: `"INFO"`

Options: `FATAL`, `ERROR`, `WARN`, `INFO`, `DEBUG`, `TRACE`, `ALL`.

---

### `fields_mapping`

An optional [Bloblang mapping](/resources/stacks/bento/components/processors/mapping) that can be used to specify extra fields to add to the log. If log fields are also added with the `fields` field then those values will override matching keys from this mapping.

Type: `string`

Default: `""`

```yaml
# Examples

fields_mapping: |-
  root.reason = "cus I wana"
  root.id = this.id
  root.age = this.user.age.number()
  root.kafka_topic = meta("kafka_topic")
```

---

### `message`

The message to print. This field supports [interpolation functions](/resources/stacks/bento/configurations/interpolation).

Type: `string`

Default: `""`