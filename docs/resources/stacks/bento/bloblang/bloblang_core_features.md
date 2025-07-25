# Bloblang Core Features

[Bloblang](/resources/stacks/bento/bloblang/walkthrough), or blobl for short, is a language designed for mapping data across a wide range of formats. It enables safe, high-performance document mapping within Bento. A Go API is available for developing custom functions and methods as plugins.

Bloblang is implemented as a processor and supports usage within function interpolations through blobl queries.

Mappings can also be executed from the command line using the `blobl` subcommand.

```bash
$ cat data.jsonl | bento blobl 'foo.(bar | baz).buz'
```
The document describes the core features of the Bloblang language. For users unfamiliar with Bloblang, it is recommended to visit [Bloblang Overview](/resources/stacks/bento/bloblang/walkthrough) prior to proceeding.

## Assignment

A [Bloblang mapping](/resources/stacks/bento/components/processors/mapping/) expresses how to create a new document by extracting data from an existing input document. Assignments consist of a dot separated path segments on the left-hand side describing a field to be created within the new document, and a right-hand side query describing what the content of the new field should be.

The keyword root on the left-hand side refers to the root of the new document, the keyword this on the right-hand side refers to the current context of the query, which is the read-only input document when querying from the root of a mapping:

```go
root.id = this.thing.id
root.type = "yo"

# Both `root` and `this` are optional, and will be inferred in their absence.
content = thing.doc.message

# In:  {"thing":{"id":"wat1","doc":{"title":"wut","message":"hello world"}}}
# Out: {"content":"hello world","id":"wat1","type":"yo"}
```

Since the document being created starts off empty it is sometimes useful to begin a mapping by copying the entire contents of the input document, which can be expressed by assigning this to root.

```go
root = this
root.foo = "added value"

# In:  {"id":"wat1","message":"hello world"}
# Out: {"id":"wat1","message":"hello world","foo":"added value"}
```

If the new document root is never assigned to or otherwise mutated then the original document remains unchanged.

### **Special Characters in Paths**

Quotes can be used to describe sections of a field path that contain whitespace, dots or other special characters:

```go
# Use quotes around a path segment in order to include whitespace or dots within
# the path
root."foo.bar".baz = this."buz bev".fub

# In:  {"buz bev":{"fub":"hello world"}}
# Out: {"foo.bar":{"baz":"hello world"}}
```

### **Non-structured Data**

Bloblang is able to map data that is unstructured, whether it's a log line or a binary blob, by referencing it with the content function, which returns the raw bytes of the input document:

```go
# Parse a base64 encoded JSON document
root = content().decode("base64").parse_json()

# In:  eyJmb28iOiJiYXIifQ==
# Out: {"foo":"bar"}
```

The newly mapped document can be unstructured by assigning a value type to the root of the document.

```go
root = this.foo

# In:  {"foo":"hello world"}
# Out: hello world
```

The resulting message payload will consist of the raw value that has been assigned.

### **Deleting**

It's possible to selectively delete fields from an object by assigning the function deleted() to the field path:

```go
root = this
root.bar = deleted()

# In:  {"id":"wat1","message":"hello world","bar":"remove me"}
# Out: {"id":"wat1","message":"hello world"}
```

### **Variables**

Another type of assignment is a let statement, which creates a variable that can be referenced elsewhere within a mapping. Variables are discarded at the end of the mapping and are mostly useful for query reuse. Variables are referenced within queries with $:

```go
# Set a temporary variable
let foo = "yo"

root.new_doc.type = $foo
```

### **Metadata**

Bento messages contain metadata that is separate from the main payload. In Bloblang, the metadata of the resulting message can be modified using the `meta` assignment keyword. Metadata values are referenced within queries using the `@` prefix.

```go
# Reference a metadata value
root.new_doc.bar = @kafka_topic

# Delete all metadata
meta = deleted()

# Set metadata values
meta bar = "hello world"
meta baz = {
  "something": "structured"
}

# Get an object of key/values for all metadata
root.meta_obj = @
```

## Coalesce

The pipe operator (`|`), when used within brackets, enables coalescing of multiple candidates for a path segment. The first field that exists and contains a non-null value is selected.

```go
root.new_doc.type = this.thing.(article | comment | this).type

# In:  {"thing":{"article":{"type":"foo"}}}
# Out: {"new_doc":{"type":"foo"}}

# In:  {"thing":{"comment":{"type":"bar"}}}
# Out: {"new_doc":{"type":"bar"}}

# In:  {"thing":{"type":"baz"}}
# Out: {"new_doc":{"type":"baz"}}
```

Opening brackets on a field begins a query where the context of this changes to value of the path it is opened upon, therefore in the above example this within the brackets refers to the contents of this.thing.

## Literals
Bloblang supports number, boolean, string, null, array and object literals:

```go
root = [
  7, false, "string", null, {
    "first": 11,
    "second": {"foo":"bar"},
    "third": """multiple
lines on this
string"""
  }
]

# In:  {}
# Out: [7,false,"string",null,{"first":11,"second":{"foo":"bar"},"third":"multiple\nlines on this\nstring"}]
```

The values within literal arrays and objects can be dynamic query expressions, as well as the keys of object literals.

## Comments

Comments are started with a hash (#) and end with a line break:

```go
root = this.some.value # And now this is a comment
```

## Boolean Logic and Arithmetic

Bloblang supports a range of boolean operators !, >, >=, ==, <, <=, &&, || and mathematical operators +, -, *, /, %:

```go
root.is_big = this.number > 100
root.multiplied = this.number * 7

# In:  {"number":50}
# Out: {"is_big":false,"multiplied":350}

# In:  {"number":150}
# Out: {"is_big":true,"multiplied":1050}
```

For more information about these operators and how they work check out the arithmetic page.

## Conditional Mapping

Use if expressions to perform maps conditionally:

```go
root = this
root.sorted_foo = if this.foo.type() == "array" { this.foo.sort() }

# In:  {"foo":"foobar"}
# Out: {"foo":"foobar"}

# In:  {"foo":["foo","bar"]}
# Out: {"foo":["foo","bar"],"sorted_foo":["bar","foo"]}
```

Multiple `if`–`else` queries can be added as needed, followed by an optional final fallback `else`.

```go
root.sound = if this.type == "cat" {
  this.cat.meow
} else if this.type == "dog" {
  this.dog.woof.uppercase()
} else {
  "sweet sweet silence"
}

# In:  {"type":"cat","cat":{"meow":"meeeeooooow!"}}
# Out: {"sound":"meeeeooooow!"}

# In:  {"type":"dog","dog":{"woof":"guurrrr woof woof!"}}
# Out: {"sound":"GUURRRR WOOF WOOF!"}

# In:  {"type":"caterpillar","caterpillar":{"name":"oleg"}}
# Out: {"sound":"sweet sweet silence"}
```

## Pattern Matching

A `match` expression enables conditional mappings on a value. Each case must be either a boolean expression, a literal value for comparison against the target value, or an underscore (`_`) to capture any value not matched by a previous case.

```go
root.new_doc = match this.doc {
  this.type == "article" => this.article
  this.type == "comment" => this.comment
  _ => this
}

# In:  {"doc":{"type":"article","article":{"id":"foo","content":"qux"}}}
# Out: {"new_doc":{"id":"foo","content":"qux"}}

# In:  {"doc":{"type":"comment","comment":{"id":"bar","content":"quz"}}}
# Out: {"new_doc":{"id":"bar","content":"quz"}}

# In:  {"doc":{"type":"neither","content":"some other stuff unchanged"}}
# Out: {"new_doc":{"type":"neither","content":"some other stuff unchanged"}}
```

Within a match block the context of this changes to the pattern matched expression, therefore this within the match expression above refers to this.doc.

Match cases can specify a literal value for simple comparison:

```go
root = this
root.type = match this.type { "doc" => "document", "art" => "article", _ => this }

# In:  {"type":"doc","foo":"bar"}
# Out: {"type":"document","foo":"bar"}
```

The match expression can also be left unset which means the context remains unchanged, and the catch-all case can also be omitted:

```go
root.new_doc = match {
  this.doc.type == "article" => this.doc.article
  this.doc.type == "comment" => this.doc.comment
}

# In:  {"doc":{"type":"neither","content":"some other stuff unchanged"}}
# Out: {"doc":{"type":"neither","content":"some other stuff unchanged"}}
```

If no case matches then the mapping is skipped entirely, which result in the original document in this case.

## Functions

Functions can be used in any position within a mapping to extract information from the environment, generate values, or access data from the underlying message.

```go
root.doc.id = uuid_v4()
root.doc.received_at = now()
root.doc.host = hostname()
```
Functions support both named and nameless style arguments:

```go
root.values_one = range(start: 0, stop: this.max, step: 2)
root.values_two = range(0, this.max, 2)
```

A complete list of functions and their parameters is available on the functions page.

## Methods

Methods operate similarly to functions but are applied to a target value. They provide most of the expressive capability in Bloblang by enabling augmentation of query values. Methods can be appended to any expression, including other methods.

```go
root.doc.id = this.thing.id.string().catch(uuid_v4())
root.doc.reduced_nums = this.thing.nums.map_each(num -> if num < 10 {
  deleted()
} else {
  num - 10
})
root.has_good_taste = ["pikachu","mewtwo","magmar"].contains(this.user.fav_pokemon)
```

Methods also support both named and nameless style arguments:

```go
root.foo_one = this.(bar | baz).trim().replace_all(old: "dog", new: "cat")
root.foo_two = this.(bar | baz).trim().replace_all("dog", "cat")
```

A complete list of methods and their parameters is available on the methods page.

## Maps

Named maps can be defined to enable reuse of common mappings on values using the `apply` method.

```go
map things {
  root.first  = this.thing_one
  root.second = this.thing_two
}

root.foo = this.value_one.apply("things")
root.bar = this.value_two.apply("things")

# In:  {"value_one":{"thing_one":"hey","thing_two":"yo"},"value_two":{"thing_one":"sup","thing_two":"waddup"}}
# Out: {"foo":{"first":"hey","second":"yo"},"bar":{"first":"sup","second":"waddup"}}
```

Within a map, the keyword `root` refers to a newly created document that will replace the target of the map, while `this` refers to the original value of the target. The argument of `apply` is a string, allowing dynamic resolution of the mapping to apply.

## Import Maps

It's possible to import maps defined in a file with an import statement:

```go
import "./common_maps.blobl"

root.foo = this.value_one.apply("things")
root.bar = this.value_two.apply("things")
```

Imports from a Bloblang mapping within a Bento config are relative to the process running the config. Imports from an imported file are relative to the file that is importing it.

## Filtering

Assigning the root of a mapped document to the `deleted()` function deletes the message entirely.

```go
# Filter all messages that have fewer than 10 URLs.
root = if this.doc.urls.length() < 10 { deleted() }
```

## Error Handling

Functions and methods can fail under certain circumstances, such as when they receive types they aren't able to act upon. These failures, when not caught, will cause the entire mapping to fail. However, the method catch can be used in order to return a value when a failure occurs instead:

```go
# Map an empty array to `foo` if the field `bar` is not a string.
root.foo = this.bar.split(",").catch([])
```

Since `catch` is a method it can also be attached to bracketed map expressions:

```go
# Map `false` if any of the operations in this boolean query fail.
root.thing = ( this.foo > this.bar && this.baz.contains("wut") ).catch(false)
```

And one of the more powerful features of Bloblang is that a single catch method at the end of a chain of methods can recover errors from any method in the chain:

```go
# Catch errors caused by:
# - foo not existing
# - foo not being a string
# - an element from split foo not being a valid JSON string
root.things = this.foo.split(",").map_each( ele -> ele.parse_json() ).catch([])

# Specifically catch a JSON parse error
root.things = this.foo.split(",").map_each( ele -> ele.parse_json().catch({}) )
```

However, the catch method only acts on errors, sometimes it's also useful to set a fall back value when a query returns null in which case the method or can be used the same way:

```go
# Map "default" if either the element index 5 does not exist, or the underlying
# element is `null`.
root.foo = this.bar.index(5).or("default")
```

## Unit Testing

Bloblang mappings can be tested using the standard Bento unit test capabilities described in this document.

## Trouble Shooting

**Error:** *unable to reference message as structured (with 'this')* when running mappings with `bento blobl`.

This error indicates that the mapping is unable to parse the input as a valid JSON document. It is necessary to ensure that the input data is correctly formatted as JSON and that the documents do not contain line breaks. The `bento blobl` command parses each line as an individual document.

Bloblang supports non-JSON formats; therefore, it does not use a streaming JSON parser to delimit documents. Instead, line breaks are used to determine the boundaries of each message.

[Walkthrough](/resources/stacks/bento/bloblang/walkthrough/)

[Functions](/resources/stacks/bento/bloblang/functions/)

[Methods](/resources/stacks/bento/bloblang/methods/)

[Arithmetic](/resources/stacks/bento/bloblang/arithmetic/)

[Advanced Bloblang](/resources/stacks/bento/bloblang/advanced_bloblang/)