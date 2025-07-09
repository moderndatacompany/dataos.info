# Advanced Bloblang

## Map Parameters

A [map](/resources/stacks/bento/components/processors/mapping) definition only has one input parameter, which is the context that it is called upon:

```go
map formatting {
  root = "(%v)".format(this)
}

root.a = this.a.apply("formatting")
root.b = this.b.apply("formatting")

# In:  {"a":"foo","b":"bar"}
# Out: {"a":"(foo)","b":"(bar)"}
```

Object literals can be used to supply multiple parameters to the mapping function. For example, to replicate the map behavior described previously but apply the pattern `[%v]` instead, an object containing both the value to be mapped and a pattern field specifying the desired format can be provided. This approach also supports extensibility for future pattern variations.


```go
map formatting {
  root = this.pattern.format(this.value)
}

root.a = {
  "value":this.a,
  "pattern":this.pattern,
}.apply("formatting")

root.b = {
  "value":this.b,
  "pattern":this.pattern,
}.apply("formatting")

# In:  {"a":"foo","b":"bar","pattern":"[%v]"}
# Out: {"a":"[foo]","b":"[bar]"}
```

## Walking the Tree

Sometimes it's necessary to perform a mapping on all values within an unknown tree structure. You can do that easily with recursive mapping:

```go
map unescape_values {
  root = match {
    this.type() == "object" => this.map_each(item -> item.value.apply("unescape_values")),
    this.type() == "array" => this.map_each(ele -> ele.apply("unescape_values")),
    this.type() == "string" => this.unescape_html(),
    this.type() == "bytes" => this.unescape_html(),
    _ => this,
  }
}
root = this.apply("unescape_values")

# In:  {"first":{"nested":"foo &amp; bar"},"second":10,"third":["1 &lt; 2",{"also_nested":"2 &gt; 1"}]}
# Out: {"first":{"nested":"foo & bar"},"second":10,"third":["1 < 2",{"also_nested":"2 > 1"}]}
```

## Message Expansion

Expanding a single message into multiple messages can be done by mapping messages into an array and following it up with an `unarchive` processor. For example, given documents of this format:

```json
{
  "id": "foobar",
  "items": [
    {"content":"foo"},
    {"content":"bar"},
    {"content":"baz"}
  ]
}
```

The `items` field can be promoted to the root level by configuring the `mapping` processor with `root = items`. Subsequently, the unarchive processor can be applied to transform each element within the array into a separate, individual message.

```yaml
pipeline:
  processors:
    - mapping: root = this.items
    - unarchive:
        format: json_array
```

However, most of the time, mapping the elements before expanding them is also needed, and often that includes copying fields outside of our target array. This can done with methods such as `map_each` and `merge`:

```go
root = this.items.map_each(ele -> this.without("items").merge(ele))

# In:  {"id":"foobar","items":[{"content":"foo"},{"content":"bar"},{"content":"baz"}]}
# Out: [{"content":"foo","id":"foobar"},{"content":"bar","id":"foobar"},{"content":"baz","id":"foobar"}]
```

The mapping described above introduces inefficiency by duplicating the source object for each element due to the use of `this.without("items")`. A more efficient approach involves assigning the result of this query to a variable, thereby avoiding repeated evaluation and redundant object copying.

```go
let doc_root = this.without("items")
root = this.items.map_each($doc_root.merge(this))

# In:  {"id":"foobar","items":[{"content":"foo"},{"content":"bar"},{"content":"baz"}]}
# Out: [{"content":"foo","id":"foobar"},{"content":"bar","id":"foobar"},{"content":"baz","id":"foobar"}]
```

It should also be noted that setting `doc_root` results in the removal of the `items` field from the target document. The complete configuration is as follows:

```yaml
pipeline:
  processors:
    - mapping: |
        let doc_root = this.without("items")
        root = this.items.map_each($doc_root.merge(this))
    - unarchive:
        format: json_array
```

## Creating CSV

Bento has a few different ways of outputting a stream of CSV data. However, the best way to do it is by converting the documents into CSV rows with Bloblang as this gives the full control over exactly how the schema is generated, erroneous data is handled, and escaping of column data is performed.

A common and simple use case is to simply flatten documents and write out the column values in alphabetical order. The initial row generated should be prefixed with a row containing the corresponding column names. This can be achieved by employing a `count` function within the mapping to identify the first invocation in the stream pipeline. The following mapping demonstrates this behavior:



```go
map escape_csv {
  root = if this.re_match("[\"\n,]+") {
    "\"" + this.replace_all("\"", "\"\"") + "\""
  } else {
    this
  }
}

# Extract key/value pairs as an array and sort by the key
let kvs = this.key_values().sort_by(v -> v.key)

# Create a header prefix for our output only on the first row
let header = if count("rows_in_file") == 1 {
  $kvs.map_each(kv -> kv.key.apply("escape_csv")).join(",") + "\n"
} else { "" }

root = $header + $kvs.map_each(kv -> kv.value.string().apply("escape_csv")).join(",")
```

And with this mapping, the data to a newly created CSV file can be written using an output with a simple `lines` codec:

```yaml
output:
  file:
    path: ./result.csv
    codec: lines
```

Perhaps the first expansion of this mapping that would be worthwhile is to add an explicit list of column names, or at least confirm that the number of values in a row matches an expected count.