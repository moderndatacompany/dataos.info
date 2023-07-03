# azure_blob_storage

> 🗣 BETA
This component is mostly stable, but breaking changes could still be made outside of major version releases if a fundamental problem with the component is found.

Downloads objects within an Azure Blob Storage container, optionally filtered by a prefix.

```yaml
# Common config fields, showing default values
input:
  label: ""
  azure_blob_storage:
    storage_account: ""
    storage_access_key: ""
    storage_sas_token: ""
    storage_connection_string: ""
    container: ""
    prefix: ""
    codec: all-bytes
```

Downloads objects within an Azure Blob Storage container, optionally filtered by a prefix.

## Downloading Large Files

When downloading large files, it's often necessary to process it in streamed parts in order to avoid loading the entire file in memory at a given time. In order to do this, a `codec` can be specified that determines how to break the input into smaller individual messages.

## Metadata

This input adds the following metadata fields to each message:

```yaml
- blob_storage_key
- blob_storage_container
- blob_storage_last_modified
- blob_storage_last_modified_unix
- blob_storage_content_type
- blob_storage_content_encoding
- All user defined metadata
```

You can access these metadata fields using function interpolation.

## Fields

### `storage_account`

The storage account to download blobs from. This field is ignored if  `storage_connection_string`  is set.

Type: `string`

Default: `""`

---

### `storage_access_key`

The storage account access key. This field is ignored if `storage_connection_string` is set.

Type: `string`

Default: `""`

---

### `storage_sas_token`

The storage account SAS token. This field is ignored if  `storage_connection_string`  or  `storage_access_key` are set.

Type: `string`

Default: `""`

---

### `storage_connection_string`

A storage account connection string. This field is required if `storage_account` and `storage_access_key` / `storage_sas_token` are not set.

Type: `string`

Default: `""`

---

### `container`

The name of the container from which to download blobs.

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
| csv | Consume structured rows as comma-separated-values, the first row must be a header row. |
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

Whether to delete downloaded objects from the blob once they are processed.

Type: `bool`

Default: `false`