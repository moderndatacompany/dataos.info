# csv

Reads one or more CSV files as structured records following the format described in RFC 4180.

## YAML Configurations

### Common Config

```yaml
# Common config fields, showing default values
input:
  label: ""
  csv:
    paths: []
    parse_header_row: true
    delimiter: ','
    lazy_quotes: false
```

### Advanced Config

```yaml
# All config fields, showing default values
input:
  label: ""
  csv:
    paths: []
    parse_header_row: true
    delimiter: ','
    lazy_quotes: false
    delete_on_finish: false
    batch_count: 1
```

This input offers more control over CSV parsing than the [`file` input](../inputs/file.md).

When parsing with a header row, each line of the file will be consumed as a structured object, where the key names are determined from the header now. For example, the following CSV file:

```
foo,bar,baz
first foo,first bar,first baz
second foo,second bar,second baz
```

Would produce the following messages:

```json
{"foo":"first foo","bar":"first bar","baz":"first baz"}
{"foo":"second foo","bar":"second bar","baz":"second baz"}
```

If, however, the field `parse_header_row` is set to `false`, then arrays are produced instead, like follows:

```json
["first foo","first bar","first baz"]
["second foo","second bar","second baz"]
```

### Metadata

This input adds the following metadata fields to each message:

```yaml
- header
- path
- mod_time_unix
- mod_time (RFC3339)
```

You can access these metadata fields using function interpolation.

Note: The `header` field is only set when `parse_header_row` is `true`.

### Output CSV column order

When creating CSV from Benthos messages, the columns must be sorted lexicographically to make the output deterministic. Alternatively, when using the `csv` input, one can leverage the `header` metadata field to retrieve the column order:

```yaml
input:
  csv:
    paths:
      - ./foo.csv
      - ./bar.csv
    parse_header_row: true

  processors:
    - mapping: |
        map escape_csv {
          root = if this.re_match("[\"\n,]+") {
            "\"" + this.replace_all("\"", "\"\"") + "\""
          } else {
            this
          }
        }

        let header = if count(@path) == 1 {
          @header.map_each(c -> c.apply("escape_csv")).join(",") + "\n"
        } else { "" }

        root = $header + @header.map_each(c -> this.get(c).string().apply("escape_csv")).join(",")

output:
  file:
    path: ./output/${! @path.filepath_split().index(-1) }
```

## Fields

### `paths`

A list of file paths to read from. Each file will be read sequentially until the list is exhausted, at which point the input will close. Glob patterns are supported, including super globs (double star).

Type: `array`

Default: `[]`

```yaml
# Examples

paths:
  - /tmp/foo.csv
  - /tmp/bar/*.csv
  - /tmp/data//*.csv
```

---

### `parse_header_row`

Whether to reference the first row as a header row. If set to true, the output structure for messages will be an object where field keys are determined by the header row. Otherwise, each message will consist of an array of values from the corresponding CSV row.

Type: `bool`

Default: `true`

---

### `delimiter`

The delimiter to use for splitting values in each record. It must be a single character.

Type: `string`

Default: `","`

---

### `lazy_quotes`

If set to `true`, a quote may appear in an unquoted field and a non-doubled quote may appear in a quoted field.

Type: `bool`

Default: `false`

---

### `delete_on_finish`

Whether to delete input files from the disk once they are fully consumed.

Type: `bool`

Default: `false`

---

### `batch_count`

Optionally process records in batches. This can help to speed up the consumption of exceptionally large CSV files. When the end of the file is reached, the remaining records are processed as a (potentially smaller) batch.

Type: `int`

Default: `1`

This input is particularly useful when consuming CSV from files too large to parse entirely within memory. However, in cases where CSV is consumed from other input types, it's also possible to parse them using the Bloblang `parse_csv` method.