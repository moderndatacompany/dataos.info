# mapping

Executes a Bloblang mapping on messages, creating a new document that replaces (or filters) the original message.

```yaml
# Config fields, showing default values
label: ""
mapping: ""
```

Bloblang is a powerful language that enables a wide range of mapping, transformation, and filtering tasks. For more information, check out the docs.

If your mapping is large and you'd prefer for it to live in a separate file, then you can execute a mapping directly from a file with the expression `from "<path>"`, where the path must be absolute or relative from the location that Benthos is executed from.

Note: This processor is equivalent to the bloblang one. The latter will be deprecated in a future release.

## Input Document Immutability

Mapping operates by creating an entirely new object during assignments, this has the advantage of treating the original referenced document as immutable and, therefore, queryable at any stage of your mapping. For example, with the following mapping:

```go
root.id = this.id
root.invitees = this.invitees.filter(i -> i.mood >= 0.5)
root.rejected = this.invitees.filter(i -> i.mood < 0.5)
```

Notice that we mutate the value of `invitees` in the resulting document by filtering out objects with a lower mood. However, even after doing so, we're still able to reference the unchanged original contents of this value from the input document in order to populate a second field. Within this mapping, we also have the flexibility to reference the mutable mapped document by using the keyword `root` (i.e. `root.invitees`) on the right-hand side instead.

Mapping documents is advantageous in situations where the result is a document with a dramatically different shape to the input document since we are effectively rebuilding the document in its entirety and might as well keep a reference to the unchanged input document throughout. However, in situations where we are only performing minor alterations to the input document, the rest of which is unchanged, it might be more efficient to use the `mutation` processor instead.

## Error Handling

Bloblang mappings can fail, in which case the message remains unchanged, errors are logged, and the message is flagged as having failed, allowing you to use standard processor error handling patterns.

However, Bloblang itself also provides powerful ways of ensuring your mappings do not fail by specifying desired fallback behavior, which you can read about in this section.

## Mapping

Given JSON documents containing an array of fans:

```json
{
  "id":"foo",
  "description":"a show about foo",
  "fans":[
    {"name":"bev","obsession":0.57},
    {"name":"grace","obsession":0.21},
    {"name":"ali","obsession":0.89},
    {"name":"vic","obsession":0.43}
  ]
}
```

We can reduce the documents down to just the ID and only those fans with an obsession score above 0.5, giving us:

```json
{
  "id":"foo",
  "fans":[
    {"name":"bev","obsession":0.57},
    {"name":"ali","obsession":0.89}
  ]
}
```

With the following config:

```yaml
pipeline:
  processors:
    - mapping: |
        root.id = this.id
        root.fans = this.fans.filter(fan -> fan.obsession > 0.5)
```