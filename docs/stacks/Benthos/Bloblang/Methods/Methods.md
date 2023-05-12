# Methods

## Bloblang Methods

Methods provide most of the power in Bloblang as they allow you to augment values and can be added to any expression (including other methods):

```python
root.doc.id = this.thing.id.string().catch(uuid_v4())
root.doc.reduced_nums = this.thing.nums.map_each(num -> if num < 10 {
  deleted()
} else {
  num - 10
})
root.has_good_taste = ["pikachu","mewtwo","magmar"].contains(this.user.fav_pokemon)
```

Methods support both named and nameless style arguments:

```python
root.foo_one = this.(bar | baz).trim().replace_all(old: "dog", new: "cat")
root.foo_two = this.(bar | baz).trim().replace_all("dog", "cat")
```

## General

### `apply`

Apply a declared mapping to a target value.

### Parameters

`mapping` <string> The mapping to apply.

### Examples

```python
map thing {
  root.inner = this.first
}

root.foo = this.doc.apply("thing")

# In:  {"doc":{"first":"hello world"}}
# Out: {"foo":{"inner":"hello world"}}
```

```python
map create_foo {
  root.name = "a foo"
  root.purpose = "to be a foo"
}

root = this
root.foo = null.apply("create_foo")

# In:  {"id":"1234"}
# Out: {"foo":{"name":"a foo","purpose":"to be a foo"},"id":"1234"}
```

---

### `catch`

If the result of a target query fails (due to incorrect types, failed parsing, etc) the argument is returned instead.

### Parameters

`fallback` <query expression> A value to yield, or query to execute, if the target query fails.

### Examples

```python
root.doc.id = this.thing.id.string().catch(uuid_v4())
```

The fallback argument can be a mapping, allowing you to capture the error string and yield structured data back.

```python
root.url = this.url.parse_url().catch(err -> {"error":err,"input":this.url})

# In:  {"url":"invalid %&# url"}
# Out: {"url":{"error":"field `this.url`: parse \"invalid %&\": invalid URL escape \"%&\"","input":"invalid %&# url"}}
```

When the input document is not structured, attempting to reference structured fields with `this` will result in an error. Therefore, a convenient way to delete non-structured data is with a catch.

```python
root = this.catch(deleted())

# In:  {"doc":{"foo":"bar"}}
# Out: {"doc":{"foo":"bar"}}

# In:  not structured data
# Out: <Message deleted>
```

---

### `exists`

Checks that a field, identified via a dot path, exists in an object.

### Parameters

`path` <string> A dot path to a field.

### Examples

```python
root.result = this.foo.exists("bar.baz")

# In:  {"foo":{"bar":{"baz":"yep, I exist"}}}
# Out: {"result":true}

# In:  {"foo":{"bar":{}}}
# Out: {"result":false}

# In:  {"foo":{}}
# Out: {"result":false}
```

---

### `from`

Modifies a target query such that certain functions are executed from the perspective of another message in the batch. This allows you to mutate events based on the contents of other messages. Functions that support this behavior are `content`, `json`, and `meta`.

### Parameters

`index` <integer> The message index to use as a perspective.

### Examples

For example, the following map extracts the contents of the JSON field `foo` specifically from message index `1` of a batch, effectively overriding the field `foo` for all messages of a batch to that of message 1:

```python
root = this
root.foo = json("foo").from(1)
```

---

### `from_all`

Modifies a target query such that certain functions are executed from the perspective of each message in the batch, and returns the set of results as an array. Functions that support this behavior are `content`, `json`, and `meta`.

### Examples

```python
root = this
root.foo_summed = json("foo").from_all().sum()
```

---

### `or`

If the result of the target query fails or resolves to `null`, returns the argument instead. This is an explicit method alternative to the coalesce pipe operator `|`.

### Parameters

`fallback` <query expression> A value to yield, or query to execute, if the target query fails or resolves to `null`.

### Examples

```python
root.doc.id = this.thing.id.or(uuid_v4())
```

## Specific Methods

[String Manipulation](Methods/String%20Manipulation.md)

[Regular Expressions](Methods/Regular%20Expressions.md)

[Number Manipulation](Methods/Number%20Manipulation.md)

[Timestamp Manipulation](./Methods/Timestamp%20Manipulation.md)

[Type Coercion](./Methods/Type%20Coercion.md)