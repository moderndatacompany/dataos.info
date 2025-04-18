# Metadata in Bento

In Bento, each message has raw contents and metadata, which is a map of key/value pairs representing an arbitrary amount of complementary data.

When an input protocol supports attributes or metadata, they will automatically be added to your messages, refer to the respective input documentation for a list of metadata keys. When an output supports attributes or metadata, any metadata key/value pairs in a message will be sent (subject to service limits).

## Editing Metadata

Bento allows you to add and remove metadata using the [`mapping` processor](/resources/stacks/bento/components/processors/mapping). For example, you can do something like this in your pipeline:

```yaml
pipeline:
  processors:
  - mapping: |
      # Remove all existing metadata from messages
      meta = deleted()

      # Add a new metadata field `time` from the contents of a JSON
      # field `event.timestamp`
      meta time = event.timestamp
```

Bloblang can also be used to delete individual metadata keys with:

```go
meta foo = deleted()
```

Or do more interesting things like remove all metadata keys with a certain prefix:

```go
meta = @.filter(kv -> !kv.key.has_prefix("kafka_"))
```

## Using Metadata

Metadata values can be referenced in any field that supports [interpolation functions](/resources/stacks/bento/configurations/interpolation). For example, you can route messages to Kafka topics using interpolation of metadata keys:

```yaml
output:
  kafka:
    addresses: [ TODO ]
    topic: ${! meta("target_topic") }
```

Bento also allows you to conditionally process messages based on their metadata with the  `switch` processor:

```yaml
pipeline:
  processors:
  - switch:
    - check: '@doc_type == "nested"'
      processors:
        - sql_insert:
            driver: mysql
            dsn: foouser:foopassword@tcp(localhost:3306)/foodb
            table: footable
            columns: [ foo, bar, baz ]
            args_mapping: |
              root = [
                this.document.foo,
                this.document.bar,
                @kafka_topic,
              ]
```

## Restricting Metadata

Outputs that support metadata, headers, or some other variant of enriched fields on messages will attempt to send all metadata key/value pairs by default. However, sometimes it's useful to refer to metadata fields at the output level even though we do not wish to send them with our data. In this case, it's possible to restrict the metadata keys that are sent with the field `metadata.exclude_prefixes` within the respective output config.

For example, if we were sending messages to Kafka using a metadata key `target_topic` to determine the topic but we wished to prevent that metadata key from being sent as a header, we could use the following configuration:

```yaml
output:
  kafka:
    addresses: [ TODO ]
    topic: ${! meta("target_topic") }
    metadata:
      exclude_prefixes:
        - target_topic
```

And when the list of metadata keys that we do *not* want to send is large it can be helpful to use a [Bloblang mapping](/resources/stacks/bento/components/processors/mapping) in order to give all of these "private" keys a common prefix:

```yaml
pipeline:
  processors:
    # Has an explicit list of public metadata keys, and everything else is given
    # an underscore prefix.
    - mapping: |
        let allowed_meta = [
          "foo",
          "bar",
          "baz",
        ]
        meta = @.map_each_key(key -> if !$allowed_meta.contains(key) {
          "_" + key
        })

output:
  kafka:
    addresses: [ TODO ]
    topic: ${! meta("_target_topic") }
    metadata:
      exclude_prefixes: [ "_" ]
```