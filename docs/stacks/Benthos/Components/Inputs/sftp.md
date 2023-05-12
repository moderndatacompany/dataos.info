# sftp

> 🗣 BETA
This component is mostly stable but breaking changes could still be made outside of major version releases if a fundamental problem with the component is found.

Consumes files from a server over SFTP.

## YAML Configurations

### Common Config

```yaml
# Common config fields, showing default values
input:
  label: ""
  sftp:
    address: ""
    credentials:
      username: ""
      password: ""
      private_key_file: ""
      private_key_pass: ""
    paths: []
    codec: all-bytes
    watcher:
      enabled: false
      minimum_age: 1s
      poll_interval: 1s
      cache: ""
```

### Advanced Config

```yaml
# All config fields, showing default values
input:
  label: ""
  sftp:
    address: ""
    credentials:
      username: ""
      password: ""
      private_key_file: ""
      private_key_pass: ""
    paths: []
    codec: all-bytes
    delete_on_finish: false
    max_buffer: 1000000
    watcher:
      enabled: false
      minimum_age: 1s
      poll_interval: 1s
      cache: ""
```

## Metadata

This input adds the following metadata fields to each message:

```
- sftp_path
```

You can access these metadata fields using function interpolation.

## Fields

### `address`

The address of the server to connect to that has the target files.

Type: `string`

Default: `""`

---

### `credentials`

The credentials to use to log into the server.

Type: `object`

---

### `credentials.username`

The username to connect to the SFTP server.

Type: `string`

Default: `""`

---

### `credentials.password`

The password for the username to connect to the SFTP server.

> 🗣 SECRET
This field contains sensitive information that usually shouldn't be added to a config directly.

Type: `string`

Default: `""`

---

### `credentials.private_key_file`

The private key for the username to connect to the SFTP server.

Type: `string`

Default: `""`

---

### `credentials.private_key_pass`

Optional passphrase for private key.

> 🗣 SECRET
This field contains sensitive information that usually shouldn't be added to a config directly.

Type: `string`

Default: `""`

---

### `paths`

A list of paths to consume sequentially. Glob patterns are supported.

Type: `array`

Default: `[]`

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

### `delete_on_finish`

Whether to delete files from the server once they are processed.

Type: `bool`

Default: `false`

---

### `max_buffer`

The largest token size expected when consuming delimited files.

Type: `int`

Default: `1000000`

---

### `watcher`

An experimental mode whereby the input will periodically scan the target paths for new files and consume them, when all files are consumed, the input will continue polling for new files.

Type: `object`

---

### `watcher.enabled`

Whether file watching is enabled.

Type: `bool`

Default: `false`

---

### `watcher.minimum_age`

The minimum period of time since a file was last updated before attempting to consume it. Increasing this period decreases the likelihood that a file will be consumed whilst it is still being written to.

Type: `string`

Default: `"1s"`

```yaml
# Examples

minimum_age: 10s

minimum_age: 1m

minimum_age: 10m
```

---

### `watcher.poll_interval`

The interval between each attempt to scan the target paths for new files.

Type: `string`

Default: `"1s"`

```yaml
# Examples

poll_interval: 100ms

poll_interval: 1s
```

---

### `watcher.cache`

A cache resource for storing the paths of files already consumed.

Type: `string`

Default: `""`