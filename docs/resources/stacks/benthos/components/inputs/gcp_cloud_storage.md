# gcp_cloud_storage

> 🗣 BETA
This component is mostly stable, but breaking changes could still be made outside of major version releases if a fundamental problem with the component is found.


Downloads objects within a Google Cloud Storage bucket, optionally filtered by a prefix.

## YAML Configurations

### Common Config

```yaml
# Common config fields, showing default values
input:
  label: ""
  gcp_cloud_storage:
    bucket: ""
    prefix: ""
    codec: all-bytes
```

### Advanced Config

```yaml
# All config fields, showing default values
input:
  label: ""
  gcp_cloud_storage:
    bucket: ""
    prefix: ""
    codec: all-bytes
    delete_objects: false
```

## Downloading Large Files

When downloading large files, it's often necessary to process it in streamed parts in order to avoid loading the entire file in memory at a given time. In order to do this, a `codec` can be specified that determines how to break the input into smaller individual messages.

## Metadata

This input adds the following metadata fields to each message:

```yaml
- gcs_key
- gcs_bucket
- gcs_last_modified
- gcs_last_modified_unix
- gcs_content_type
- gcs_content_encoding
- All user defined metadata
```

You can access these metadata fields using function interpolation.

### Credentials

By default, Benthos will use a shared credentials file when connecting to GCP services. You can find out more in this document.

## Fields

### `bucket`

The name of the bucket from which to download objects.

Type: `string`

Default: `""`

---

### `prefix`

An optional path prefix, if set, only objects with the prefix are consumed.

Type: `string`

Default: `""`

---

### `codec`

The way in which the bytes of a data source should be converted into discrete messages, codecs are useful for specifying how large files or continuous streams of data might be processed in small chunks rather than loading it all in memory. It's possible to consume lines using a custom delimiter with the `delim:x` codec, where x is the character sequence custom delimiter. Codecs can be chained with `/`, for example, a gzip compressed CSV file can be consumed with the codec `gzip/csv`.

Type: `string`

Default: `"all-bytes"`

| Option | Summary |
| --- | --- |
| auto | EXPERIMENTAL: Attempts to derive a codec for each file based on information such as the extension. For example, a .tar.gz file would be consumed with the gzip/tar codec. Defaults to all-bytes. |
| all-bytes | Consume the entire file as a single binary message. |
| avro-ocf:marshaler=x | EXPERIMENTAL: Consume a stream of Avro OCF datum. The marshaler parameter is optional and has the options: goavro (default), json. Use goavro if OCF contains logical types. |
| chunker:x | Consume the file in chunks of a given number of bytes. |
| csv | Consume structured rows as comma-separated values, the first row must be a header row. |
| csv:x | Consume structured rows as values separated by a custom delimiter, the first row must be a header row. The custom delimiter must be a single character, e.g. the codec "csv:\t" would consume a tab-delimited file. |
| delim:x | Consume the file in segments divided by a custom delimiter. |
| gzip | Decompress a gzip file, this codec should precede another codec, e.g. gzip/all-bytes, gzip/tar, gzip/csv, etc. |
| lines | Consume the file in segments divided by linebreaks. |
| multipart | Consumes the output of another codec and batches messages together. A batch ends when an empty message is consumed. For example, the codec lines/multipart could be used to consume multipart messages where an empty line indicates the end of each batch. |
| regex:(?m)^\d\d:\d\d:\d\d | Consume the file in segments divided by regular expression. |
| tar | Parse the file as a tar archive, and consume each file of the archive as a message. |

```yaml
# Examples

codec: lines

codec: "delim:\t"

codec: delim:foobar

codec: gzip/csv
```

---

### `delete_objects`

Whether to delete downloaded objects from the bucket once they are processed.

Type: `bool`

Default: `false`