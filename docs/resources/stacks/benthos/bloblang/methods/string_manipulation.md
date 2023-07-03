# String Manipulation

## String Manipulation[](https://www.benthos.dev/docs/guides/bloblang/methods#string-manipulation)

### `capitalize`[](https://www.benthos.dev/docs/guides/bloblang/methods#capitalize)

Takes a string value and returns a copy with all Unicode letters that begin words mapped to their Unicode title case.

### Examples[](https://www.benthos.dev/docs/guides/bloblang/methods#examples-6)

```python
root.title = this.title.capitalize()

# In:  {"title":"the foo bar"}
# Out: {"title":"The Foo Bar"}
```


Creates a "slug" from a given string. Wraps the github.com/gosimple/slug package. See its [docs](https://pkg.go.dev/github.com/gosimple/slug) for more information.

### Parameters[](https://www.benthos.dev/docs/guides/bloblang/methods#parameters-17)

**`lang`** <(optional) string, default `"en"`>

### Examples[](https://www.benthos.dev/docs/guides/bloblang/methods#examples-28)

Creates a slug from an English string

```python
root.slug = this.value.slug()

# In:  {"value":"Gopher & Benthos"}
# Out: {"slug":"gopher-and-benthos"}
```

Creates a slug from a French string

```python
root.slug = this.value.slug("fr")

# In:  {"value":"Gaufre & Poisson d'Eau Profonde"}
# Out: {"slug":"gaufre-et-poisson-deau-profonde"}
```

---

### `split`[](https://www.benthos.dev/docs/guides/bloblang/methods#split)

Split a string value into an array of strings by splitting it on a string separator.

### Parameters[](https://www.benthos.dev/docs/guides/bloblang/methods#parameters-18)

**`delimiter`** <string> The delimiter to split with.

### Examples[](https://www.benthos.dev/docs/guides/bloblang/methods#examples-29)

```python
root.new_value = this.value.split(",")

# In:  {"value":"foo,bar,baz"}
# Out: {"new_value":["foo","bar","baz"]}
```

---

### `strip_html`[](https://www.benthos.dev/docs/guides/bloblang/methods#strip_html)

Attempts to remove all HTML tags from a target string.

### Parameters[](https://www.benthos.dev/docs/guides/bloblang/methods#parameters-19)

**`preserve`** <(optional) array> An optional array of element types to preserve in the output.

### Examples[](https://www.benthos.dev/docs/guides/bloblang/methods#examples-30)

```python
root.stripped = this.value.strip_html()

# In:  {"value":"<p>the plain <strong>old text</strong></p>"}
# Out: {"stripped":"the plain old text"}
```

It's also possible to provide an explicit list of element types to preserve in the output.

```python
root.stripped = this.value.strip_html(["article"])

# In:  {"value":"<article><p>the plain <strong>old text</strong></p></article>"}
# Out: {"stripped":"<article>the plain old text</article>"}
```

---

### `trim`[](https://www.benthos.dev/docs/guides/bloblang/methods#trim)

Remove all leading and trailing characters from a string that are contained within an argument cutset. If no arguments are provided then whitespace is removed.

### Parameters[](https://www.benthos.dev/docs/guides/bloblang/methods#parameters-20)

**`cutset`** <(optional) string> An optional string of characters to trim from the target value.

### Examples[](https://www.benthos.dev/docs/guides/bloblang/methods#examples-31)

```python
root.title = this.title.trim("!?")
root.description = this.description.trim()

# In:  {"description":"  something happened and its amazing! ","title":"!!!watch out!?"}
# Out: {"description":"something happened and its amazing!","title":"watch out"}
```

---

### `trim_prefix`[](https://www.benthos.dev/docs/guides/bloblang/methods#trim_prefix)

Remove the provided leading prefix substring from a string. If the string does not have the prefix substring, it is returned unchanged.

### Parameters[](https://www.benthos.dev/docs/guides/bloblang/methods#parameters-21)

**`prefix`** <string> The leading prefix substring to trim from the string.

### Examples[](https://www.benthos.dev/docs/guides/bloblang/methods#examples-32)

```python
root.name = this.name.trim_prefix("foobar_")
root.description = this.description.trim_prefix("foobar_")

# In:  {"description":"unchanged","name":"foobar_blobton"}
# Out: {"description":"unchanged","name":"blobton"}
```

---

### `trim_suffix`[](https://www.benthos.dev/docs/guides/bloblang/methods#trim_suffix)

Remove the provided trailing suffix substring from a string. If the string does not have the suffix substring, it is returned unchanged.

### Parameters[](https://www.benthos.dev/docs/guides/bloblang/methods#parameters-22)

**`suffix`** <string> The trailing suffix substring to trim from the string.

### Examples[](https://www.benthos.dev/docs/guides/bloblang/methods#examples-33)

```python
root.name = this.name.trim_suffix("_foobar")
root.description = this.description.trim_suffix("_foobar")

# In:  {"description":"unchanged","name":"blobton_foobar"}
# Out: {"description":"unchanged","name":"blobton"}
```

---

### `unescape_html`[](https://www.benthos.dev/docs/guides/bloblang/methods#unescape_html)

Unescapes a string so that entities like `&lt;` become `<`. It unescapes a larger range of entities than `escape_html` escapes. For example, `&aacute;` unescapes to `á`, as does `&#225;` and `&xE1;`.

### Examples[](https://www.benthos.dev/docs/guides/bloblang/methods#examples-34)

```python
root.unescaped = this.value.unescape_html()

# In:  {"value":"foo &amp; bar"}
# Out: {"unescaped":"foo & bar"}
```

---

### `unescape_url_query`[](https://www.benthos.dev/docs/guides/bloblang/methods#unescape_url_query)

Expands escape sequences from a URL query string.

### Examples[](https://www.benthos.dev/docs/guides/bloblang/methods#examples-35)

```python
root.unescaped = this.value.unescape_url_query()

# In:  {"value":"foo+%26+bar"}
# Out: {"unescaped":"foo & bar"}
```

---

### `unquote`[](https://www.benthos.dev/docs/guides/bloblang/methods#unquote)

Unquotes a target string, expanding any escape sequences (`\t`, `\n`, `\xFF`, `\u0100`) for control characters and non-printable characters.

### Examples[](https://www.benthos.dev/docs/guides/bloblang/methods#examples-36)

```python
root.unquoted = this.thing.unquote()

# In:  {"thing":"\"foo\\nbar\""}
# Out: {"unquoted":"foo\nbar"}
```

---

### `uppercase`[](https://www.benthos.dev/docs/guides/bloblang/methods#uppercase)

Convert a string value into uppercase.

### Examples[](https://www.benthos.dev/docs/guides/bloblang/methods#examples-37)

```python
root.foo = this.foo.uppercase()

# In:  {"foo":"hello world"}
# Out: {"foo":"HELLO WORLD"}
```