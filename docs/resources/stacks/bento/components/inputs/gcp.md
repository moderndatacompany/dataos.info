# gcp_bigquery_select

Category: GCP, Services

<aside>
🗣 **BETA**

This component is mostly stable, but breaking changes could still be made outside of major version releases if a fundamental problem with the component is found.

</aside>

Executes a `SELECT` query against BigQuery and creates a message for each row received.

```yaml
# Config fields, showing default values
input:
  label: ""
  gcp_bigquery_select:
    project: ""
    table: ""
    columns: []
    where: ""
    job_labels: {}
    priority: ""
    args_mapping: ""
    prefix: ""
    suffix: ""

```

Once the rows from the query are exhausted, this input shuts down, allowing the pipeline to gracefully terminate (or the next input in a sequence to execute).

## Examples

### Word counts

Here we query the public corpus of Shakespeare's works to generate a stream of the top 10 words that are 3 or more characters long:

```yaml
input:
  gcp_bigquery_select:
    project: sample-project
    table: bigquery-public-data.samples.shakespeare
    columns:
      - word
      - sum(word_count) as total_count
    where: length(word) >= ?
    suffix: |
      GROUP BY word
      ORDER BY total_count DESC
      LIMIT 10
    args_mapping: |
      root = [ 3 ]

```

## Fields

### `project`

GCP project where the query job will execute.

**Type:** `string`

---

### `table`

Fully-qualified BigQuery table name to query.

**Type:** `string`

```yaml
# Examples

table: bigquery-public-data.samples.shakespeare
```

---

### `columns`

A list of columns to query.

**Type:** `array`

---

### `where`

An optional where clause to add. Placeholder arguments are populated with the `args_mapping`  field. Placeholders should always be question marks (`?`).

**Type:** `string`

```yaml
# Examples

where: type = ? and created_at > ?

where: user_id = ?
```

---

### `job_labels`

A list of labels to add to the query job.

**Type:** `object`

**Default:** `{}`

---

### `priority`

The priority with which to schedule the query.

**Type:** `string`

**Default:** `""`

---

### `args_mapping`

An optional Bloblang mapping which should evaluate to an array of values matching in size to the number of placeholder arguments in the field `where`.

**Type:** `string`

```yaml
# Examples

args_mapping: root = [ "article", now().ts_format("2006-01-02") ]
```

---

### `prefix`

An optional prefix to prepend to the select query (before SELECT).

**Type:** `string`

---

### `suffix`

An optional suffix to append to the select query.

**Type:** `string`