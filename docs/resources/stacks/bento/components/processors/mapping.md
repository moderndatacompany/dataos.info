### Mapping Processor

Executes a [Bloblang](/resources/stacks/bento/bloblang/walkthrough/) mapping on each message, generating a new document that replaces or filters the original message.

```yaml
# Config fields with default values
label: ""
mapping: ""
```

Bloblang is a domain-specific language designed for performing transformations, mappings, and filtering on structured message data. It enables the creation of complex document transformations in a concise and declarative manner.

Larger mappings can be placed in external files and referenced using the expression `from "<path>"`, where the path must be absolute or relative to the directory from which Bento is executed.

This processor is equivalent to the legacy `bloblang` processor. The `bloblang` identifier remains valid but is planned for deprecation in a future release.

### Input Document Immutability

The mapping processor generates a new document during assignment operations. This approach treats the original input document as immutable and allows it to be queried throughout the mapping. For example:

```go
root.id = this.id
root.invitees = this.invitees.filter(i -> i.mood >= 0.5)
root.rejected = this.invitees.filter(i -> i.mood < 0.5)
```

In the above example, although the `invitees` field is modified in the output document, the original value remains available for subsequent operations. This design is especially useful when constructing output documents with a structure significantly different from the input. In contrast, for minor changes where most of the document remains unaltered, the `mutation` processor may provide a more efficient alternative.

### Example: Filtering Array Elements

Given the following JSON input:

```json
{
  "id": "foo",
  "description": "a show about foo",
  "fans": [
    {"name": "bev", "obsession": 0.57},
    {"name": "grace", "obsession": 0.21},
    {"name": "ali", "obsession": 0.89},
    {"name": "vic", "obsession": 0.43}
  ]
}
```

To produce a document containing only the `id` and fans with an obsession score greater than 0.5:

```yaml
pipeline:
  processors:
    - mapping: |
        root.id = this.id
        root.fans = this.fans.filter(fan -> fan.obsession > 0.5)
```

Resulting output:

```json
{
  "id": "foo",
  "fans": [
    {"name": "bev", "obsession": 0.57},
    {"name": "ali", "obsession": 0.89}
  ]
}
```

### Example: Aggregating Field Values

Given the following input:

```json
{
  "locations": [
    {"name": "Seattle", "state": "WA"},
    {"name": "New York", "state": "NY"},
    {"name": "Bellevue", "state": "WA"},
    {"name": "Olympia", "state": "WA"}
  ]
}
```

To extract the city names from Washington and combine them into a single string field:

```yaml
pipeline:
  processors:
    - mapping: |
        root.Cities = this.locations.
                        filter(loc -> loc.state == "WA").
                        map_each(loc -> loc.name).
                        sort().
                        join(", ")
```

Resulting output:

```json
{"Cities": "Bellevue, Olympia, Seattle"}
```

### Error Handling

Bloblang also supports explicit fallback behavior within mappings to minimize failure risk. Refer to the error handling section in the documentation for usage examples.
If a Bloblang mapping fails, the original message remains unchanged, the error is logged, and the message is marked as failed. Standard [error handling mechanisms](/resources/stacks/bento/configurations/error_handling) can be applied to manage such failures.
