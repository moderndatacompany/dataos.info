# stdin

Consumes data piped to stdin as line delimited messages.

## YAML Configurations

### Common Config

```yaml
# Common config fields, showing default values
input:
  label: ""
  stdin:
    codec: lines
```

### Advanced Config

```yaml
# All config fields, showing default values
input:
  label: ""
  stdin:
    codec: lines
    max_buffer: 1000000
```

If the multipart option is set to true, then lines are interpretted as message parts, and an empty line indicates the end of the message.

If the delimiter field is left empty, then line feed (\n) is used.

## Fields

### `codec`

The way in which the bytes of a data source should be converted into discrete messages, codecs are useful for specifying how large files or continuous streams of data might be processed in small chunks rather than loading it all in memory. It's possible to consume lines using a custom delimiter with the `delim:x` codec, where x is the character sequence custom delimiter. Codecs can be chained with `/`, for example a gzip compressed CSV file can be consumed with the codec `gzip/csv`.

Type: `string`

Default: `"lines"`

| Option | Summary |
| --- | --- |
| auto | EXPERIMENTAL: Attempts to derive a codec for each file based on information such as the extension. For example, a .tar.gz file would be consumed with the gzip/tar codec. Defaults to all-bytes. |
| all-bytes | Consume the entire file as a single binary message. |
| avro-ocf:marshaler=x | EXPERIMENTAL: Consume a stream of Avro OCF datum. The marshaler parameter is optional and has the options: goavro (default), json. Use goavro if OCF contains logical types. |
| chunker:x | Consume the file in chunks of a given number of bytes. |
| csv | Consume structured rows as comma separated values, the first row must be a header row. |
| csv:x | Consume structured rows as values separated by a custom delimiter, the first row must be a header row. The custom delimiter must be a single character, e.g. the codec "csv:\t" would consume a tab delimited file. |
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

### `max_buffer`

The maximum message buffer size. Must exceed the largest message to be consumed.

Type: `int`

Default: `1000000`