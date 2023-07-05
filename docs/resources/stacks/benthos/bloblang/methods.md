# Methods

Methods provide most of the power in Bloblang as they allow you to augment values and can be added to any expression (including other methods):

```yaml
root.doc.id = this.thing.id.string().catch(uuid_v4())
root.doc.reduced_nums = this.thing.nums.map_each(num -> if num < 10 {
  deleted()
} else {
  num - 10
})
root.has_good_taste = ["pikachu","mewtwo","magmar"].contains(this.user.fav_pokemon)
```

Methods support both named and nameless style arguments:

```yaml
root.foo_one = this.(bar | baz).trim().replace_all(old: "dog", new: "cat")
root.foo_two = this.(bar | baz).trim().replace_all("dog", "cat")
```

## General

### **`apply`**

Apply a declared mapping to a target value.

**Parameters**

**`mapping`** \<string\> The mapping to apply.

**Examples**

```yaml
map thing {
  root.inner = this.first
}

root.foo = this.doc.apply("thing")

# In:  {"doc":{"first":"hello world"}}
# Out: {"foo":{"inner":"hello world"}}
```

```yaml
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

### **`catch`**

If the result of a target query fails (due to incorrect types, failed parsing, etc) the argument is returned instead.

**Parameters**

**`fallback`** \<query expression\> A value to yield, or query to execute, if the target query fails.

**Examples**

```yaml
root.doc.id = this.thing.id.string().catch(uuid_v4())
```

The fallback argument can be a mapping, allowing you to capture the error string and yield structured data back.

```yaml
root.url = this.url.parse_url().catch(err -> {"error":err,"input":this.url})

# In:  {"url":"invalid %&# url"}
# Out: {"url":{"error":"field `this.url`: parse \"invalid %&\": invalid URL escape \"%&\"","input":"invalid %&# url"}}
```

When the input document is not structured attempting to reference structured fields with this will result in an error. Therefore, a convenient way to delete non-structured data is with a catch.

```yaml
root = this.catch(deleted())

# In:  {"doc":{"foo":"bar"}}
# Out: {"doc":{"foo":"bar"}}

# In:  not structured data
# Out: <Message deleted>
```

---

### **`exists`**

Checks that a field, identified via a dot path, exists in an object.

**Parameters**

**`path`** \<string\> A dot path to a field.

**Examples**
```yaml
root.result = this.foo.exists("bar.baz")

# In:  {"foo":{"bar":{"baz":"yep, I exist"}}}
# Out: {"result":true}

# In:  {"foo":{"bar":{}}}
# Out: {"result":false}

# In:  {"foo":{}}
# Out: {"result":false}
```

---

### **`from`**

Modifies a target query such that certain functions are executed from the perspective of another message in the batch. This allows you to mutate events based on the contents of other messages. Functions that support this behaviour are content, json and meta.

**Parameters**

**`index`** \<integer\> The message index to use as a perspective.

**Examples**

For example, the following map extracts the contents of the JSON field foo specifically from message index 1 of a batch, effectively overriding the field foo for all messages of a batch to that of message 1:

```yaml
root = this
root.foo = json("foo").from(1)
```

---

### **`from_all`**

Modifies a target query such that certain functions are executed from the perspective of each message in the batch, and returns the set of results as an array. Functions that support this behaviour are content, json and meta.

**Examples**

```yaml
root = this
root.foo_summed = json("foo").from_all().sum()
```

---

### **`or`**

If the result of the target query fails or resolves to null, returns the argument instead. This is an explicit method alternative to the coalesce pipe operator |.

**Parameters**

**`fallback`** \<query expression\> A value to yield, or query to execute, if the target query fails or resolves to null.

**Examples**
```yaml
root.doc.id = this.thing.id.or(uuid_v4())
```

## String Manipulation

### **`capitalize`**

Takes a string value and returns a copy with all Unicode letters that begin words mapped to their Unicode title case.

**Examples**
```yaml
root.title = this.title.capitalize()

# In:  {"title":"the foo bar"}
# Out: {"title":"The Foo Bar"}
```
---


### **`compare_argon2`**

Checks whether a string matches a hashed secret using Argon2.

**Parameters**

**hashed_secret** \<string\> The hashed secret to compare with the input. This must be a fully-qualified string which encodes the Argon2 options used to generate the hash.

**Examples**

```yaml
root.match = this.secret.compare_argon2("$argon2id$v=19$m=4096,t=3,p=1$c2FsdHktbWNzYWx0ZmFjZQ$RMUMwgtS32/mbszd+ke4o4Ej1jFpYiUqY6MHWa69X7Y")

# In:  {"secret":"there-are-many-blobs-in-the-sea"}
# Out: {"match":true}
```
```yaml
root.match = this.secret.compare_argon2("$argon2id$v=19$m=4096,t=3,p=1$c2FsdHktbWNzYWx0ZmFjZQ$RMUMwgtS32/mbszd+ke4o4Ej1jFpYiUqY6MHWa69X7Y")

# In:  {"secret":"will-i-ever-find-love"}
# Out: {"match":false}
```
---

### **`compare_bcrypt`**

Checks whether a string matches a hashed secret using bcrypt.

**Parameters**

**hashed_secret** \<string\> The hashed secret value to compare with the input.

**Examples**
```yaml
root.match = this.secret.compare_bcrypt("$2y$10$Dtnt5NNzVtMCOZONT705tOcS8It6krJX8bEjnDJnwxiFKsz1C.3Ay")

# In:  {"secret":"there-are-many-blobs-in-the-sea"}
# Out: {"match":true}
```

```yaml
root.match = this.secret.compare_bcrypt("$2y$10$Dtnt5NNzVtMCOZONT705tOcS8It6krJX8bEjnDJnwxiFKsz1C.3Ay")

# In:  {"secret":"will-i-ever-find-love"}
# Out: {"match":false}
```
---

### **`contains`**

Checks whether a string contains a substring and returns a boolean result.

**Parameters**

**value** \<unknown\> A value to test against elements of the target.

**Examples**
```yaml
root.has_foo = this.thing.contains("foo")

# In:  {"thing":"this foo that"}
# Out: {"has_foo":true}

# In:  {"thing":"this bar that"}
# Out: {"has_foo":false}
```
---

### **`escape_html`**

Escapes a string so that special characters like < to become &lt;. It escapes only five such characters: <, >, &, ' and " so that it can be safely placed within an HTML entity.

**Examples**
```yaml
root.escaped = this.value.escape_html()

# In:  {"value":"foo & bar"}
# Out: {"escaped":"foo &amp; bar"}
```
---
### **`escape_url_query`**
Escapes a string so that it can be safely placed within a URL query.

**Examples**

```yaml
root.escaped = this.value.escape_url_query()

# In:  {"value":"foo & bar"}
# Out: {"escaped":"foo+%26+bar"}
```
---

### **`filepath_join`**
Joins an array of path elements into a single file path. The separator depends on the operating system of the machine.

**Examples**
```yaml
root.path = this.path_elements.filepath_join()

# In:  {"path_elements":["/foo/","bar.txt"]}
# Out: {"path":"/foo/bar.txt"}
```
---

### **`filepath_split`**
Splits a file path immediately following the final Separator, separating it into a directory and file name component returned as a two element array of strings. If there is no Separator in the path, the first element will be empty and the second will contain the path. The separator depends on the operating system of the machine.

**Examples**
```yaml
root.path_sep = this.path.filepath_split()

# In:  {"path":"/foo/bar.txt"}
# Out: {"path_sep":["/foo/","bar.txt"]}

# In:  {"path":"baz.txt"}
# Out: {"path_sep":["","baz.txt"]}
```
---

### **`format`**
Use a value string as a format specifier in order to produce a new string, using any number of provided arguments. Please refer to the Go fmt package documentation for the list of valid format verbs.

**Examples**
```yaml
root.foo = "%s(%v): %v".format(this.name, this.age, this.fingers)

# In:  {"name":"lance","age":37,"fingers":13}
# Out: {"foo":"lance(37): 13"}
```
---

### **`has_prefix`**

Checks whether a string has a prefix argument and returns a bool.

**Parameters**

**value** \<string\> The string to test.

**Examples**
```yaml
root.t1 = this.v1.has_prefix("foo")
root.t2 = this.v2.has_prefix("foo")

# In:  {"v1":"foobar","v2":"barfoo"}
# Out: {"t1":true,"t2":false}
```
---

### **`has_suffix`**
Checks whether a string has a suffix argument and returns a bool.

**Parameters**

**`value`** \<string\> The string to test.

**Examples**
```yaml
root.t1 = this.v1.has_suffix("foo")
root.t2 = this.v2.has_suffix("foo")

# In:  {"v1":"foobar","v2":"barfoo"}
# Out: {"t1":false,"t2":true}
```
---

### **`index_of`**

Returns the starting index of the argument substring in a string target, or -1 if the target doesn't contain the argument.

**Parameters**

**value** \<string\> A string to search for.

**Examples**

```yaml
root.index = this.thing.index_of("bar")

# In:  {"thing":"foobar"}
# Out: {"index":3}
```

```yaml
root.index = content().index_of("meow")

# In:  the cat meowed, the dog woofed
# Out: {"index":8}
```
---

### **`length`**

Returns the length of a string.

**Examples**
```yaml
root.foo_len = this.foo.length()

# In:  {"foo":"hello world"}
# Out: {"foo_len":11}
```
---

### **`lowercase`**

Convert a string value into lowercase.

**Examples**
```yaml
root.foo = this.foo.lowercase()

# In:  {"foo":"HELLO WORLD"}
# Out: {"foo":"hello world"}
```
---

### **`parse_jwt_hs256`**
Parses a claims object from a JWT string encoded with HS256. This method does not validate JWT claims.

**Parameters**

**signing_secret** \<string\> The HMAC secret that was used for signing the token.

**Examples**
```yaml
root.claims = this.signed.parse_jwt_hs256("dont-tell-anyone")

# In:  {"signed":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyMTIzIn0.hUl-nngPMY_3h9vveWJUPsCcO5PeL6k9hWLnMYeFbFQ"}
# Out: {"claims":{"sub":"user123"}}
```
---
### **`parse_jwt_hs384`**

Parses a claims object from a JWT string encoded with HS384. This method does not validate JWT claims.

**Parameters**

**`signing_secret`** \<string\> The HMAC secret that was used for signing the token.

**Examples**
```yaml
root.claims = this.signed.parse_jwt_hs384("dont-tell-anyone")

# In:  {"signed":"eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyMTIzIn0.zGYLr83aToon1efUNq-hw7XgT20lPvZb8sYei8x6S6mpHwb433SJdXJXx0Oio8AZ"}
# Out: {"claims":{"sub":"user123"}}
```
---

### **`parse_jwt_hs512`**

Parses a claims object from a JWT string encoded with HS512. This method does not validate JWT claims.

**Parameters**

**`signing_secret`** \<string\> The HMAC secret that was used for signing the token.

**Examples**
```yaml
root.claims = this.signed.parse_jwt_hs512("dont-tell-anyone")

# In:  {"signed":"eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyMTIzIn0.zBNR9o_6EDwXXKkpKLNJhG26j8Dc-mV-YahBwmEdCrmiWt5les8I9rgmNlWIowpq6Yxs4kLNAdFhqoRz3NXT3w"}
# Out: {"claims":{"sub":"user123"}}
```
---

### **`quote`**

Quotes a target string using escape sequences (\t, \n, \xFF, \u0100) for control characters and non-printable characters.

**Examples**
```yaml
root.quoted = this.thing.quote()

# In:  {"thing":"foo\nbar"}
# Out: {"quoted":"\"foo\\nbar\""}
```
---
### **`replace_all`**

Replaces all occurrences of the first argument in a target string with the second argument.

**Parameters**

**`old`** \<string\> A string to match against.

**`new`** \<string\> A string to replace with.

**Examples**
```yaml
root.new_value = this.value.replace_all("foo","dog")

# In:  {"value":"The foo ate my homework"}
# Out: {"new_value":"The dog ate my homework"}
```
---
### **`replace_all_many`**
For each pair of strings in an argument array, replaces all occurrences of the first item of the pair with the second. This is a more compact way of chaining a series of replace_all methods.

**Parameters**
**`values`** \<array\> An array of values, each even value will be replaced with the following odd value.

**Examples**
```yaml
root.new_value = this.value.replace_all_many([
  "<b>", "&lt;b&gt;",
  "</b>", "&lt;/b&gt;",
  "<i>", "&lt;i&gt;",
  "</i>", "&lt;/i&gt;",
])

# In:  {"value":"<i>Hello</i> <b>World</b>"}
# Out: {"new_value":"&lt;i&gt;Hello&lt;/i&gt; &lt;b&gt;World&lt;/b&gt;"}
```
---
### **`reverse`**
Returns the target string in reverse order.

**Examples**
```yaml
root.reversed = this.thing.reverse()

# In:  {"thing":"backwards"}
# Out: {"reversed":"sdrawkcab"}
```
```yaml
root = content().reverse()

# In:  {"thing":"backwards"}
# Out: }"sdrawkcab":"gniht"{
```
---
### **`slice`**

Extract a slice from a string by specifying two indices, a low and high bound, which selects a half-open range that includes the first character, but excludes the last one. If the second index is omitted then it defaults to the length of the input sequence.

**Parameters**

**`low`** \<integer\> The low bound, which is the first element of the selection, or if negative selects from the end.

**`high`** \<(optional) integer\> An optional high bound.

**Examples**
```yaml
root.beginning = this.value.slice(0, 2)
root.end = this.value.slice(4)

# In:  {"value":"foo bar"}
# Out: {"beginning":"fo","end":"bar"}
```

A negative low index can be used, indicating an offset from the end of the sequence. If the low index is greater than the length of the sequence then an empty result is returned.

```yaml
root.last_chunk = this.value.slice(-4)
root.the_rest = this.value.slice(0, -4)

# In:  {"value":"foo bar"}
# Out: {"last_chunk":" bar","the_rest":"foo"}
```
---
### **`slug`**

<aside style="padding:15px; border-radius:5px;">

**BETA**

This method is mostly stable but breaking changes could still be made outside of major version releases if a fundamental problem with it is found.

</aside>

Creates a "slug" from a given string. Wraps the github.com/gosimple/slug package. See its docs for more information.

**Parameters**

**`lang`** \<(optional) string, default "en"\>

**Examples**

Creates a slug from an English string
```yaml
root.slug = this.value.slug()

# In:  {"value":"Gopher & Benthos"}
# Out: {"slug":"gopher-and-benthos"}
```

Creates a slug from a French string

```yaml
root.slug = this.value.slug("fr")

# In:  {"value":"Gaufre & Poisson d'Eau Profonde"}
# Out: {"slug":"gaufre-et-poisson-deau-profonde"}
```
---
### **`split`**

Split a string value into an array of strings by splitting it on a string separator.

**Parameters**

**`delimiter`** \<string\> The delimiter to split with.

**Examples**
```yaml
root.new_value = this.value.split(",")

# In:  {"value":"foo,bar,baz"}
# Out: {"new_value":["foo","bar","baz"]}
```
---
### **`strip_html`**

Attempts to remove all HTML tags from a target string.

**Parameters**

**`preserve`** \<(optional) array\> An optional array of element types to preserve in the output.

**Examples**
```yaml
root.stripped = this.value.strip_html()

# In:  {"value":"<p>the plain <strong>old text</strong></p>"}
# Out: {"stripped":"the plain old text"}
```

It's also possible to provide an explicit list of element types to preserve in the output.
```yaml
root.stripped = this.value.strip_html(["article"])

# In:  {"value":"<article><p>the plain <strong>old text</strong></p></article>"}
# Out: {"stripped":"<article>the plain old text</article>"}
```
---
### **`trim`**
Remove all leading and trailing characters from a string that are contained within an argument cutset. If no arguments are provided then whitespace is removed.

**Parameters**

**`cutset`** \<(optional) string\> An optional string of characters to trim from the target value.

**Examples**
```yaml
root.title = this.title.trim("!?")
root.description = this.description.trim()

# In:  {"description":"  something happened and its amazing! ","title":"!!!watch out!?"}
# Out: {"description":"something happened and its amazing!","title":"watch out"}
```
---
### **`trim_prefix`**

Remove the provided leading prefix substring from a string. If the string does not have the prefix substring, it is returned unchanged.

**`Parameters`**

**`prefix`** \<string\> The leading prefix substring to trim from the string.

**`Examples`**
```yaml
root.name = this.name.trim_prefix("foobar_")
root.description = this.description.trim_prefix("foobar_")

# In:  {"description":"unchanged","name":"foobar_blobton"}
# Out: {"description":"unchanged","name":"blobton"}
```
---
### **`trim_suffix`**

Remove the provided trailing suffix substring from a string. If the string does not have the suffix substring, it is returned unchanged.


**Parameters**

**`suffix`** \<string\> The trailing suffix substring to trim from the string.

**Examples**
```yaml
root.name = this.name.trim_suffix("_foobar")
root.description = this.description.trim_suffix("_foobar")

# In:  {"description":"unchanged","name":"blobton_foobar"}
# Out: {"description":"unchanged","name":"blobton"}
```
---
### **`unescape_html`**

Unescapes a string so that entities like &lt; become <. It unescapes a larger range of entities than escape_html escapes. For example, &aacute; unescapes to á, as does &#225; and &xE1;.

**Examples**
```yaml
root.unescaped = this.value.unescape_html()

# In:  {"value":"foo &amp; bar"}
# Out: {"unescaped":"foo & bar"}
```
---
### **`unescape_url_query`**

Expands escape sequences from a URL query string.

**Examples**
```yaml
root.unescaped = this.value.unescape_url_query()

# In:  {"value":"foo+%26+bar"}
# Out: {"unescaped":"foo & bar"}
```
---
### **`unquote`**

Unquotes a target string, expanding any escape sequences (\t, \n, \xFF, \u0100) for control characters and non-printable characters.

**Examples**
```yaml
root.unquoted = this.thing.unquote()

# In:  {"thing":"\"foo\\nbar\""}
# Out: {"unquoted":"foo\nbar"}
```
---
### **`uppercase`**

Convert a string value into uppercase.

**Examples**
```yaml
root.foo = this.foo.uppercase()

# In:  {"foo":"hello world"}
# Out: {"foo":"HELLO WORLD"}
```

## Regular Expressions

### **`re_find_all`**

Returns an array containing all successive matches of a regular expression in a string.

**Parameters**

**`pattern`** \<string\> The pattern to match against.

**Examples**

```yaml
root.matches = this.value.re_find_all("a.")

# In:  {"value":"paranormal"}
# Out: {"matches":["ar","an","al"]}
```
---

### **`re_find_all_object`**

Returns an array of objects containing all matches of the regular expression and the matches of its subexpressions. The key of each match value is the name of the group when specified, otherwise, it is the index of the matching group, starting with the expression as a whole at 0.

**Parameters**

**`pattern`** \<string\> The pattern to match against.

**Examples**

```yaml
root.matches = this.value.re_find_all_object("a(?P<foo>x*)b")

# In:  {"value":"-axxb-ab-"}
# Out: {"matches":[{"0":"axxb","foo":"xx"},{"0":"ab","foo":""}]}
```

```yaml
root.matches = this.value.re_find_all_object("(?m)(?P<key>\\w+):\\s+(?P<value>\\w+)$")

# In:  {"value":"option1: value1\noption2: value2\noption3: value3"}
# Out: {"matches":[{"0":"option1: value1","key":"option1","value":"value1"},{"0":"option2: value2","key":"option2","value":"value2"},{"0":"option3: value3","key":"option3","value":"value3"}]}
```

---

### **`re_find_all_submatch`**

Returns an array of arrays containing all successive matches of the regular expression in a string and the matches, if any, of its subexpressions.

**Parameters**

**`pattern`** \<string\> The pattern to match against.

**Examples**

```yaml
root.matches = this.value.re_find_all_submatch("a(x*)b")

# In:  {"value":"-axxb-ab-"}
# Out: {"matches":[["axxb","xx"],["ab",""]]}
```

---

### **`re_find_object`**

Returns an object containing the first match of the regular expression and the matches of its subexpressions. The key of each match value is the name of the group when specified; otherwise, it is the index of the matching group, starting with the expression as a whole at 0.

**Parameters**

**`pattern`** \<string\> The pattern to match against.

**Examples**

```yaml
root.matches = this.value.re_find_object("a(?P<foo>x*)b")

# In:  {"value":"-axxb-ab-"}
# Out: {"matches":{"0":"axxb","foo":"xx"}}
```

```yaml
root.matches = this.value.re_find_object("(?P<key>\\w+):\\s+(?P<value>\\w+)")

# In:  {"value":"option1: value1"}
# Out: {"matches":{"0":"option1: value1","key":"option1","value":"value1"}}
```

---

### **`re_match`**

Checks whether a regular expression matches against any part of a string and returns a boolean.

**Parameters**

**`pattern`** \<string\> The pattern to match against.

**Examples**

```yaml
root.matches = this.value.re_match("[0-9]")

# In:  {"value":"there are 10 puppies"}
# Out: {"matches":true}

# In:  {"value":"there are ten puppies"}
# Out: {"matches":false}
```

---

### **`re_replace_all`**

Replaces all occurrences of the argument regular expression in a string with a value. Inside the value, $ signs are interpreted as sub-match expansions, e.g. `$1` represents the text of the first sub match.

**Parameters**

**`pattern`** \<string\> The pattern to match against.

**`value`** \<string\> The value to replace with.

**Examples**

```yaml
root.new_value = this.value.re_replace_all("ADD ([0-9]+)","+($1)")

# In:  {"value":"foo ADD 70"}
# Out: {"new_value":"foo +(70)"}
```

## Number Manipulation

### **`abs`**

Returns the absolute value of a number.

**Examples**

```yaml
root.new_value = this.value.abs()

# In:  {"value":5.3}
# Out: {"new_value":5.3}

# In:  {"value":-5.9}
# Out: {"new_value":5.9}
```

---

### **`ceil`**

Returns the least integer value greater than or equal to a number. If the resulting value fits within a 64-bit integer, then that is returned; otherwise, a new floating-point number is returned.

**Examples**

```yaml
root.new_value = this.value.ceil()

# In:  {"value":5.3}
# Out: {"new_value":6}

# In:  {"value":-5.9}
# Out: {"new_value":-5}
```
---

### **`floor`**

Returns the greatest integer value less than or equal to the target number. If the resulting value fits within a 64-bit integer, then that is returned; otherwise, a new floating-point number is returned.

**Examples**

```yaml
root.new_value = this.value.floor()

# In:  {"value":5.7}
# Out: {"new_value":5}
```
---

### **`int32`**

Converts a numerical type into a 32-bit signed integer, this is for advanced use cases where a specific data type is needed for a given component (such as the ClickHouse SQL driver).

If the value is a string, then an attempt will be made to parse it as a 32-bit integer. If the target value exceeds the capacity of an integer or contains decimal values, then this method will throw an error. In order to convert a floating point number containing decimals, first use `.round()` on the value first. Please refer to the [`strconv.ParseInt` documentation](https://pkg.go.dev/strconv#ParseInt) for details regarding the supported formats.

**Examples**

```yaml
root.a = this.a.int32()
root.b = this.b.round().int32()
root.c = this.c.int32()

# In:  {"a":12,"b":12.34,"c":"12"}
# Out: {"a":12,"b":12,"c":12}
```

```yaml
root = this.int32()

# In:  "0xB70B"
# Out: 46859
```
---

### **`int64`**

Converts a numerical type into a 64-bit signed integer, this is for advanced use cases where a specific data type is needed for a given component (such as the ClickHouse SQL driver).

If the value is a string, then an attempt will be made to parse it as a 64-bit integer. If the target value exceeds the capacity of an integer or contains decimal values, then this method will throw an error. In order to convert a floating point number containing decimals, first use `.round()` on the value first. Please refer to the [`strconv.ParseInt` documentation](https://pkg.go.dev/strconv#ParseInt) for details regarding the supported formats.

**Examples**

```yaml
root.a = this.a.int64()
root.b = this.b.round().int64()
root.c = this.c.int64()

# In:  {"a":12,"b":12.34,"c":"12"}
# Out: {"a":12,"b":12,"c":12}
```

```yaml
root = this.int64()

# In:  "0xDEADBEEF"
# Out: 3735928559
```

---

### **`log`**

Returns the natural logarithm of a number.

**Examples**

```yaml
root.new_value = this.value.log().round()

# In:  {"value":1}
# Out: {"new_value":0}

# In:  {"value":2.7183}
# Out: {"new_value":1}
```

---

### **`log10`**

Returns the decimal logarithm of a number.

**Examples**

```yaml
root.new_value = this.value.log10()

# In:  {"value":100}
# Out: {"new_value":2}

# In:  {"value":1000}
# Out: {"new_value":3}
```

---

### **`max`**

Returns the largest numerical value found within an array. All values must be numerical and the array must not be empty; otherwise, an error is returned.

**Examples**

```yaml
root.biggest = this.values.max()

# In:  {"values":[0,3,2.5,7,5]}
# Out: {"biggest":7}
```

```yaml
root.new_value = [0,this.value].max()

# In:  {"value":-1}
# Out: {"new_value":0}

# In:  {"value":7}
# Out: {"new_value":7}
```
---

### **`min`**

Returns the smallest numerical value found within an array. All values must be numerical and the array must not be empty; otherwise, an error is returned.

**Examples**

```yaml
root.smallest = this.values.min()

# In:  {"values":[0,3,-2.5,7,5]}
# Out: {"smallest":-2.5}
```

```yaml
root.new_value = [10,this.value].min()

# In:  {"value":2}
# Out: {"new_value":2}

# In:  {"value":23}
# Out: {"new_value":10}
```
---

### **`round`**

Rounds numbers to the nearest integer, rounding half away from zero. If the resulting value fits within a 64-bit integer, then that is returned; otherwise, a new floating-point number is returned.

**Examples**

```yaml
root.new_value = this.value.round()

# In:  {"value":5.3}
# Out: {"new_value":5}

# In:  {"value":5.9}
# Out: {"new_value":6}
```
---

### **`uint32`**

Converts a numerical type into a 32-bit unsigned integer, this is for advanced use cases where a specific data type is needed for a given component (such as the ClickHouse SQL driver).

If the value is a string, then an attempt will be made to parse it as a 32-bit unsigned integer. If the target value exceeds the capacity of an integer or contains decimal values, then this method will throw an error. In order to convert a floating point number containing decimals, first use `.round()` on the value first. Please refer to the [`strconv.ParseInt` documentation](https://pkg.go.dev/strconv#ParseInt) for details regarding the supported formats.

**Examples**

```yaml
root.a = this.a.uint32()
root.b = this.b.round().uint32()
root.c = this.c.uint32()
root.d = this.d.uint32().catch(0)

# In:  {"a":12,"b":12.34,"c":"12","d":-12}
# Out: {"a":12,"b":12,"c":12,"d":0}
```

```yaml
root = this.uint32()

# In:  "0xB70B"
# Out: 46859
```
---

### **`uint64`**

Converts a numerical type into a 64-bit unsigned integer, this is for advanced use cases where a specific data type is needed for a given component (such as the ClickHouse SQL driver).

If the value is a string, then an attempt will be made to parse it as a 64-bit unsigned integer. If the target value exceeds the capacity of an integer or contains decimal values, then this method will throw an error. In order to convert a floating point number containing decimals, first use `.round()` on the value first. Please refer to the [`strconv.ParseInt` documentation](https://pkg.go.dev/strconv#ParseInt) for details regarding the supported formats.

**Examples**

```yaml
root.a = this.a.uint64()
root.b = this.b.round().uint64()
root.c = this.c.uint64()
root.d = this.d.uint64().catch(0)

# In:  {"a":12,"b":12.34,"c":"12","d":-12}
# Out: {"a":12,"b":12,"c":12,"d":0}
```

```yaml
root = this.uint64()

# In:  "0xDEADBEEF"
# Out: 3735928559
```

## Timestamp Manipulation

### **`parse_duration`**

Attempts to parse a string as a duration and returns an integer of nanoseconds. A duration string is a possibly signed sequence of decimal numbers, each with an optional fraction and a unit suffix, such as "300ms", "-1.5h" or "2h45m". Valid time units are "ns", "us" (or "µs"), "ms", "s", "m", "h".

**Examples**
```yaml
root.delay_for_ns = this.delay_for.parse_duration()

# In:  {"delay_for":"50us"}
# Out: {"delay_for_ns":50000}
```
```yaml
root.delay_for_s = this.delay_for.parse_duration() / 1000000000

# In:  {"delay_for":"2h"}
# Out: {"delay_for_s":7200}
```

---

### **`parse_duration_iso8601`**

<aside style="padding:15px; border-radius:5px;">

**BETA**

This method is mostly stable but breaking changes could still be made outside of major version releases if a fundamental problem with it is found.

</aside>

Attempts to parse a string using ISO-8601 rules as a duration and returns an integer of nanoseconds. A duration string is represented by the format "P[n]Y[n]M[n]DT[n]H[n]M[n]S" or "P[n]W". In these representations, the "[n]" is replaced by the value for each of the date and time elements that follow the "[n]". For example, "P3Y6M4DT12H30M5S" represents a duration of "three years, six months, four days, twelve hours, thirty minutes, and five seconds". The last field of the format allows fractions with one decimal place, so "P3.5S" will return 3500000000ns. Any additional decimals will be truncated.

**Examples**

Arbitrary ISO-8601 duration string to nanoseconds:
```yaml
root.delay_for_ns = this.delay_for.parse_duration_iso8601()

# In:  {"delay_for":"P3Y6M4DT12H30M5S"}
# Out: {"delay_for_ns":110839937000000000}
```

Two hours ISO-8601 duration string to seconds:

```yaml
root.delay_for_s = this.delay_for.parse_duration_iso8601() / 1000000000

# In:  {"delay_for":"PT2H"}
# Out: {"delay_for_s":7200}
```

Two and a half seconds ISO-8601 duration string to seconds:

```yaml
root.delay_for_s = this.delay_for.parse_duration_iso8601() / 1000000000

# In:  {"delay_for":"PT2.5S"}
# Out: {"delay_for_s":2.5}
```

---

### **`ts_add_iso8601`**

<aside style="padding:15px; border-radius:5px;">

**BETA**

This method is mostly stable but breaking changes could still be made outside of major version releases if a fundamental problem with it is found.

</aside>

Parse parameter string as ISO 8601 period and add it to value with high precision for units larger than an hour.

**Parameters**

**`duration`** \<string\> Duration in ISO 8601 format

---

### **`ts_format`**

<aside style="padding:15px; border-radius:5px;">

**BETA**

This method is mostly stable but breaking changes could still be made outside of major version releases if a fundamental problem with it is found.
</aside>

Attempts to format a timestamp value as a string according to a specified format, or RFC 3339 by default. Timestamp values can either be a numerical unix time in seconds (with up to nanosecond precision via decimals), or a string in RFC 3339 format.

The output format is defined by showing how the reference time, defined to be Mon Jan 2 15:04:05 -0700 MST 2006, would be displayed if it were the value. For an alternative way to specify formats check out the `ts_strftime` method.

**Parameters**

**`format`** \<string, default "2006-01-02T15:04:05.999999999Z07:00"\> The output format to use.

**`tz`** \<(optional) string\> An optional timezone to use, otherwise the timezone of the input string is used, or in the case of unix timestamps the local timezone is used.

**Examples**
```yaml
root.something_at = (this.created_at + 300).ts_format()
```
An optional string argument can be used in order to specify the output format of the timestamp. The format is defined by showing how the reference time, defined to be Mon Jan 2 15:04:05 -0700 MST 2006, would be displayed if it were the value.
```yaml
root.something_at = (this.created_at + 300).ts_format("2006-Jan-02 15:04:05")
```
A second optional string argument can also be used in order to specify a timezone, otherwise the timezone of the input string is used, or in the case of unix timestamps the local timezone is used.
```yaml
root.something_at = this.created_at.ts_format(format: "2006-Jan-02 15:04:05", tz: "UTC")

# In:  {"created_at":1597405526}
# Out: {"something_at":"2020-Aug-14 11:45:26"}

# In:  {"created_at":"2020-08-14T11:50:26.371Z"}
# Out: {"something_at":"2020-Aug-14 11:50:26"}
```
And `ts_format` supports up to nanosecond precision with floating point timestamp values.
```yaml
root.something_at = this.created_at.ts_format("2006-Jan-02 15:04:05.999999", "UTC")

# In:  {"created_at":1597405526.123456}
# Out: {"something_at":"2020-Aug-14 11:45:26.123456"}

# In:  {"created_at":"2020-08-14T11:50:26.371Z"}
# Out: {"something_at":"2020-Aug-14 11:50:26.371"}
```

---

### **`ts_parse`**

<aside style="padding:15px; border-radius:5px;">

**BETA**

This method is mostly stable but breaking changes could still be made outside of major version releases if a fundamental problem with it is found.
</aside>

Attempts to parse a string as a timestamp following a specified format and outputs a timestamp, which can then be fed into methods such as `ts_format`.

The input format is defined by showing how the reference time, defined to be Mon Jan 2 15:04:05 -0700 MST 2006, would be displayed if it were the value. For an alternative way to specify formats check out the ts_strptime method.

**Parameters**

**`format`** \<string\> The format of the target string.

**Examples**
```yaml
root.doc.timestamp = this.doc.timestamp.ts_parse("2006-Jan-02")

# In:  {"doc":{"timestamp":"2020-Aug-14"}}
# Out: {"doc":{"timestamp":"2020-08-14T00:00:00Z"}}
```

---

### **`ts_round`**

<aside style="padding:15px; border-radius:5px;">

**BETA**

This method is mostly stable but breaking changes could still be made outside of major version releases if a fundamental problem with it is found.
</aside>

Returns the result of rounding a timestamp to the nearest multiple of the argument duration (nanoseconds). The rounding behavior for halfway values is to round up. Timestamp values can either be a numerical unix time in seconds (with up to nanosecond precision via decimals), or a string in RFC 3339 format. The ts_parse method can be used in order to parse different timestamp formats.

**Parameters**

**`duration`** \<integer\> A duration measured in nanoseconds to round by.

**Examples**

Use the method parse_duration to convert a duration string into an integer argument.

```yaml
root.created_at_hour = this.created_at.ts_round("1h".parse_duration())

# In:  {"created_at":"2020-08-14T05:54:23Z"}
# Out: {"created_at_hour":"2020-08-14T06:00:00Z"}
```

---

### **`ts_strftime`**

<aside style="padding:15px; border-radius:5px;">

**BETA**

This method is mostly stable but breaking changes could still be made outside of major version releases if a fundamental problem with it is found.
</aside>

Attempts to format a timestamp value as a string according to a specified strftime-compatible format. Timestamp values can either be a numerical unix time in seconds (with up to nanosecond precision via decimals), or a string in RFC 3339 format.

**Parameters**

**format** \<string\> The output format to use.

**tz** \<(optional) string\> An optional timezone to use, otherwise the timezone of the input string is used.

**Examples**

The format consists of zero or more conversion specifiers and ordinary characters (except %). All ordinary characters are copied to the output string without modification. Each conversion specification begins with % character followed by the character that determines the behaviour of the specifier. Please refer to man 3 strftime for the list of format specifiers.

```yaml
root.something_at = (this.created_at + 300).ts_strftime("%Y-%b-%d %H:%M:%S")
```
A second optional string argument can also be used in order to specify a timezone, otherwise the timezone of the input string is used, or in the case of unix timestamps the local timezone is used.

```yaml
root.something_at = this.created_at.ts_strftime("%Y-%b-%d %H:%M:%S", "UTC")

# In:  {"created_at":1597405526}
# Out: {"something_at":"2020-Aug-14 11:45:26"}

# In:  {"created_at":"2020-08-14T11:50:26.371Z"}
# Out: {"something_at":"2020-Aug-14 11:50:26"}
```
As an extension provided by the underlying formatting library, itchyny/timefmt-go, the %f directive is supported for zero-padded microseconds, which originates from Python. Note that E and O modifier characters are not supported.

```yaml
root.something_at = this.created_at.ts_strftime("%Y-%b-%d %H:%M:%S.%f", "UTC")

# In:  {"created_at":1597405526}
# Out: {"something_at":"2020-Aug-14 11:45:26.000000"}

# In:  {"created_at":"2020-08-14T11:50:26.371Z"}
# Out: {"something_at":"2020-Aug-14 11:50:26.371000"}
```

---

### **`ts_strptime`**

<aside style="padding:15px; border-radius:5px;">

**BETA**
This method is mostly stable but breaking changes could still be made outside of major version releases if a fundamental problem with it is found.
</aside>

Attempts to parse a string as a timestamp following a specified strptime-compatible format and outputs a timestamp, which can then be fed into `ts_format`.

**Parameters**

**`format`** \<string\> The format of the target string.

**Examples**

The format consists of zero or more conversion specifiers and ordinary characters (except %). All ordinary characters are copied to the output string without modification. Each conversion specification begins with a % character followed by the character that determines the behaviour of the specifier. Please refer to man 3 strptime for the list of format specifiers.

```yaml
root.doc.timestamp = this.doc.timestamp.ts_strptime("%Y-%b-%d")

# In:  {"doc":{"timestamp":"2020-Aug-14"}}
# Out: {"doc":{"timestamp":"2020-08-14T00:00:00Z"}}
```
As an extension provided by the underlying formatting library, itchyny/timefmt-go, the %f directive is supported for zero-padded microseconds, which originates from Python. Note that E and O modifier characters are not supported.

```yaml
root.doc.timestamp = this.doc.timestamp.ts_strptime("%Y-%b-%d %H:%M:%S.%f")

# In:  {"doc":{"timestamp":"2020-Aug-14 11:50:26.371000"}}
# Out: {"doc":{"timestamp":"2020-08-14T11:50:26.371Z"}}
```

---

### **`ts_sub_iso8601`**

<aside style="padding:15px; border-radius:5px;">

**BETA**

This method is mostly stable but breaking changes could still be made outside of major version releases if a fundamental problem with it is found.
</aside>

Parse parameter string as ISO 8601 period and subtract it from value with high precision for units larger than an hour.

**Parameters**

**`duration`** \<string\> Duration in ISO 8601 format

---

### **`ts_tz`**

<aside style="padding:15px; border-radius:5px;">

**BETA**

This method is mostly stable but breaking changes could still be made outside of major version releases if a fundamental problem with it is found.
</aside>

Returns the result of converting a timestamp to a specified timezone. Timestamp values can either be a numerical unix time in seconds (with up to nanosecond precision via decimals), or a string in RFC 3339 format. The `ts_parse` method can be used in order to parse different timestamp formats.

**Parameters**

**tz** \<string\> The timezone to change to. If set to "UTC" then the timezone will be UTC. If set to "Local" then the local timezone will be used. Otherwise, the argument is taken to be a location name corresponding to a file in the IANA Time Zone database, such as "America/New_York".

**Examples**
```yaml
root.created_at_utc = this.created_at.ts_tz("UTC")

# In:  {"created_at":"2021-02-03T17:05:06+01:00"}
# Out: {"created_at_utc":"2021-02-03T16:05:06Z"}
```
---

### **`ts_unix`**

<aside style="padding:15px; border-radius:5px;">

**BETA**
This method is mostly stable but breaking changes could still be made outside of major version releases if a fundamental problem with it is found.
</aside>

Attempts to format a timestamp value as a unix timestamp. Timestamp values can either be a numerical unix time in seconds (with up to nanosecond precision via decimals), or a string in RFC 3339 format. The `ts_parse` method can be used in order to parse different timestamp formats.

**Examples**
```yaml
root.created_at_unix = this.created_at.ts_unix()

# In:  {"created_at":"2009-11-10T23:00:00Z"}
# Out: {"created_at_unix":1257894000}
```

---

### **`ts_unix_micro`**

<aside style="padding:15px; border-radius:5px;">

**BETA**

This method is mostly stable but breaking changes could still be made outside of major version releases if a fundamental problem with it is found.
</aside>
Attempts to format a timestamp value as a unix timestamp with microsecond precision. Timestamp values can either be a numerical unix time in seconds (with up to nanosecond precision via decimals), or a string in RFC 3339 format. The `ts_parse` method can be used in order to parse different timestamp formats.

**Examples**
```yaml
root.created_at_unix = this.created_at.ts_unix_micro()

# In:  {"created_at":"2009-11-10T23:00:00Z"}
# Out: {"created_at_unix":1257894000000000}
```
---

### **`ts_unix_milli`**

<aside style="padding:15px; border-radius:5px;">

**BETA**

This method is mostly stable but breaking changes could still be made outside of major version releases if a fundamental problem with it is found.
</aside>

Attempts to format a timestamp value as a unix timestamp with millisecond precision. Timestamp values can either be a numerical unix time in seconds (with up to nanosecond precision via decimals), or a string in RFC 3339 format. The `ts_parse` method can be used in order to parse different timestamp formats.

**Examples**

```yaml
root.created_at_unix = this.created_at.ts_unix_milli()

# In:  {"created_at":"2009-11-10T23:00:00Z"}
# Out: {"created_at_unix":1257894000000}
```
---

### **`ts_unix_nano`**

<aside style="padding:15px; border-radius:5px;">

**BETA**
This method is mostly stable but breaking changes could still be made outside of major version releases if a fundamental problem with it is found.
</aside>

Attempts to format a timestamp value as a unix timestamp with nanosecond precision. Timestamp values can either be a numerical unix time in seconds (with up to nanosecond precision via decimals), or a string in RFC 3339 format. The `ts_parse` method can be used in order to parse different timestamp formats.

**Examples**
```yaml
root.created_at_unix = this.created_at.ts_unix_nano()

# In:  {"created_at":"2009-11-10T23:00:00Z"}
# Out: {"created_at_unix":1257894000000000000}
```

## Type Coercion

### **`bool`**

Attempt to parse a value into a boolean. An optional argument can be provided, in which case if the value cannot be parsed the argument will be returned instead. If the value is a number then any non-zero value will resolve to true, if the value is a string then any of the following values are considered valid: 1, t, T, TRUE, true, True, 0, f, F, FALSE.

**Parameters**

**`default`** \<(optional) bool\> An optional value to yield if the target cannot be parsed as a boolean.

**Examples**
```yaml
root.foo = this.thing.bool()
root.bar = this.thing.bool(true)
```

---

### **`bytes`**

Marshal a value into a byte array. If the value is already a byte array it is unchanged.

**Examples**
```yaml
root.first_byte = this.name.bytes().index(0)

# In:  {"name":"foobar bazson"}
# Out: {"first_byte":102}
```

---

### **`not_empty`**
Ensures that the given string, array or object value is not empty, and if so returns it, otherwise an error is returned.

**Examples**
```yaml
root.a = this.a.not_empty()

# In:  {"a":"foo"}
# Out: {"a":"foo"}

# In:  {"a":""}
# Out: Error("failed assignment (line 1): field `this.a`: string value is empty")

# In:  {"a":["foo","bar"]}
# Out: {"a":["foo","bar"]}

# In:  {"a":[]}
# Out: Error("failed assignment (line 1): field `this.a`: array value is empty")

# In:  {"a":{"b":"foo","c":"bar"}}
# Out: {"a":{"b":"foo","c":"bar"}}

# In:  {"a":{}}
# Out: Error("failed assignment (line 1): field `this.a`: object value is empty")
```

---

### **`not_null`**

Ensures that the given value is not null, and if so returns it, otherwise an error is returned.

**Examples**
```yaml
root.a = this.a.not_null()

# In:  {"a":"foobar","b":"barbaz"}
# Out: {"a":"foobar"}

# In:  {"b":"barbaz"}
# Out: Error("failed assignment (line 1): field `this.a`: value is null")
```

---

### **`number`**

Attempt to parse a value into a number. An optional argument can be provided, in which case if the value cannot be parsed into a number the argument will be returned instead.

**Parameters**

**`default`** \<(optional) float\> An optional value to yield if the target cannot be parsed as a number.

**Examples**
```yaml
root.foo = this.thing.number() + 10
root.bar = this.thing.number(5) * 10
```

---

### **`string`**

Marshal a value into a string. If the value is already a string it is unchanged.

**Examples**
```yaml
root.nested_json = this.string()

# In:  {"foo":"bar"}
# Out: {"nested_json":"{\"foo\":\"bar\"}"}
```
```yaml
root.id = this.id.string()

# In:  {"id":228930314431312345}
# Out: {"id":"228930314431312345"}
```

---

### **`type`**

Returns the type of a value as a string, providing one of the following values: string, bytes, number, bool, timestamp, array, object or null.

**Examples**

```yaml
root.bar_type = this.bar.type()
root.foo_type = this.foo.type()

# In:  {"bar":10,"foo":"is a string"}
# Out: {"bar_type":"number","foo_type":"string"}
```
```yaml

root.type = this.type()

# In:  "foobar"
# Out: {"type":"string"}

# In:  666
# Out: {"type":"number"}

# In:  false
# Out: {"type":"bool"}

# In:  ["foo", "bar"]
# Out: {"type":"array"}

# In:  {"foo": "bar"}
# Out: {"type":"object"}

# In:  null
# Out: {"type":"null"}
```
```yaml
root.type = content().type()

# In:  foobar
# Out: {"type":"bytes"}
```
```yaml
root.type = this.ts_parse("2006-01-02").type()

# In:  "2022-06-06"
# Out: {"type":"timestamp"}
```

## Encoding and Encryption

### **`compress`**

Compresses a string or byte array value according to a specified algorithm.

**Parameters**

**`algorithm`** \<string\> One of flate, gzip, pgzip, lz4, snappy, zlib, zstd.

**`level`** \<integer, default -1\> The level of compression to use. May not be applicable to all algorithms.

**Examples**

```yaml
let long_content = range(0, 1000).map_each(content()).join(" ")
root.a_len = $long_content.length()
root.b_len = $long_content.compress("gzip").length()

# In:  hello world this is some content
# Out: {"a_len":32999,"b_len":161}
```

```yaml
root.compressed = content().compress("lz4").encode("base64")

# In:  hello world I love space
# Out: {"compressed":"BCJNGGRwuRgAAIBoZWxsbyB3b3JsZCBJIGxvdmUgc3BhY2UAAAAAGoETLg=="}
```
---

### **`decode`**

Decodes an encoded string target according to a chosen scheme and returns the result as a byte array. When mapping the result to a JSON field the value should be cast to a string using the method string, or encoded using the method encode, otherwise it will be base64 encoded by default.

Available schemes are: base64, base64url (RFC 4648 with padding characters), base64rawurl (RFC 4648 without padding characters), hex, ascii85.

**Parameters**

**`scheme`** \<string\> The decoding scheme to use.

**Examples**

```yaml
root.decoded = this.value.decode("hex").string()

# In:  {"value":"68656c6c6f20776f726c64"}
# Out: {"decoded":"hello world"}
```

```yaml
root = this.encoded.decode("ascii85")

# In:  {"encoded":"FD,B0+DGm>FDl80Ci\"A>F`)8BEckl6F`M&(+Cno&@/"}
# Out: this is totally unstructured data
```
---

### **`decompress`**

Decompresses a string or byte array value according to a specified algorithm. The result of decompression

**Parameters**

**`algorithm`** \<string\> One of gzip, pgzip, zlib, bzip2, flate, snappy, lz4, zstd.

**Examples**
```yaml
root = this.compressed.decode("base64").decompress("lz4")

# In:  {"compressed":"BCJNGGRwuRgAAIBoZWxsbyB3b3JsZCBJIGxvdmUgc3BhY2UAAAAAGoETLg=="}
# Out: hello world I love space
```

Use the .string() method in order to coerce the result into a string, this makes it possible to place the data within a JSON document without automatic base64 encoding.

```yaml
root.result = this.compressed.decode("base64").decompress("lz4").string()

# In:  {"compressed":"BCJNGGRwuRgAAIBoZWxsbyB3b3JsZCBJIGxvdmUgc3BhY2UAAAAAGoETLg=="}
# Out: {"result":"hello world I love space"}
```
---

### **`decrypt_aes`**

Decrypts an encrypted string or byte array target according to a chosen AES encryption method and returns the result as a byte array. The algorithms require a key and an initialization vector / nonce. Available schemes are: ctr, ofb, cbc.

**Parameters**

**`scheme`** \<string\> The scheme to use for decryption, one of ctr, ofb, cbc.

**`key`** \<string\> A key to decrypt with.

**`iv`** \<string\> An initialization vector / nonce.


**Examples**

```yaml
let key = "2b7e151628aed2a6abf7158809cf4f3c".decode("hex")
let vector = "f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff".decode("hex")
root.decrypted = this.value.decode("hex").decrypt_aes("ctr", $key, $vector).string()

# In:  {"value":"84e9b31ff7400bdf80be7254"}
# Out: {"decrypted":"hello world!"}
```
---
### **`encode`**

Encodes a string or byte array target according to a chosen scheme and returns a string result. Available schemes are: base64, base64url (RFC 4648 with padding characters), base64rawurl (RFC 4648 without padding characters), hex, ascii85.

**Parameters**

**`scheme`** \<string\> The encoding scheme to use.

**Examples**

```yaml
root.encoded = this.value.encode("hex")

# In:  {"value":"hello world"}
# Out: {"encoded":"68656c6c6f20776f726c64"}
```
```yaml
root.encoded = content().encode("ascii85")

# In:  this is totally unstructured data
# Out: {"encoded":"FD,B0+DGm>FDl80Ci\"A>F`)8BEckl6F`M&(+Cno&@/"}
```
---
### **`encrypt_aes`**

Encrypts a string or byte array target according to a chosen AES encryption method and returns a string result. The algorithms require a key and an initialization vector / nonce. Available schemes are: ctr, ofb, cbc.

**Parameters**

**`scheme`** \<string\> The scheme to use for encryption, one of ctr, ofb, cbc.

**`key`** \<string\> A key to encrypt with.

**`iv`** \<string\> An initialization vector / nonce.


**Examples**

```yaml
let key = "2b7e151628aed2a6abf7158809cf4f3c".decode("hex")
let vector = "f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff".decode("hex")
root.encrypted = this.value.encrypt_aes("ctr", $key, $vector).encode("hex")

# In:  {"value":"hello world!"}
# Out: {"encrypted":"84e9b31ff7400bdf80be7254"}
```
---
### **`hash`**

Hashes a string or byte array according to a chosen algorithm and returns the result as a byte array. When mapping the result to a JSON field the value should be cast to a string using the method string, or encoded using the method encode, otherwise it will be base64 encoded by default.

Available algorithms are: hmac_sha1, hmac_sha256, hmac_sha512, md5, sha1, sha256, sha512, xxhash64, crc32.

The following algorithms require a key, which is specified as a second argument: hmac_sha1, hmac_sha256, hmac_sha512.

**Parameters**

**`algorithm`** \<string\> The hasing algorithm to use.

**`key`** \<(optional) string\> An optional key to use.

**`polynomial`** \<string, default "IEEE"\> An optional polynomial key to use when selecting the crc32 algorithm, otherwise ignored. Options are IEEE (default), Castagnoli and Koopman

Examples
```yaml
root.h1 = this.value.hash("sha1").encode("hex")
root.h2 = this.value.hash("hmac_sha1","static-key").encode("hex")

# In:  {"value":"hello world"}
# Out: {"h1":"2aae6c35c94fcfb415dbe95f408b9ce91ee846ed","h2":"d87e5f068fa08fe90bb95bc7c8344cb809179d76"}
```

The crc32 algorithm supports options for the polynomial.

```yaml
root.h1 = this.value.hash(algorithm: "crc32", polynomial: "Castagnoli").encode("hex")
root.h2 = this.value.hash(algorithm: "crc32", polynomial: "Koopman").encode("hex")

# In:  {"value":"hello world"}
# Out: {"h1":"c99465aa","h2":"df373d3c"}
```

## GeoIP

### **`geoip_anonymous_ip`**

<aside style="padding:15px; border-radius:5px;">

**EXPERIMENTAL**

This method is experimental and therefore breaking changes could be made to it outside of major version releases.

</aside>

Looks up an IP address against a MaxMind database file and, if found, returns an object describing the anonymous IP associated with it.

**Parameters**

**`path`** <string> A path to an mmdb (maxmind) file.

---

### **`geoip_asn`**

<aside style="padding:15px; border-radius:5px;">

**EXPERIMENTAL**

This method is experimental and therefore breaking changes could be made to it outside of major version releases.
</aside>

Looks up an IP address against a MaxMind database file and, if found, returns an object describing the ASN associated with it.

**Parameters**

**`path`** \<string\> A path to an mmdb (maxmind) file.

---

### **`geoip_city`**

<aside style="padding:15px; border-radius:5px;">

**EXPERIMENTAL**

This method is experimental and therefore breaking changes could be made to it outside of major version releases.

</aside>

Looks up an IP address against a MaxMind database file and, if found, returns an object describing the city associated with it.

**Parameters**

**`path`** \<string\> A path to an mmdb (maxmind) file.

---

### **`geoip_connection_type`**

<aside style="padding:15px; border-radius:5px;">

**EXPERIMENTAL**

This method is experimental and therefore breaking changes could be made to it outside of major version releases.

</aside>

Looks up an IP address against a MaxMind database file and, if found, returns an object describing the connection type associated with it.

**Parameters**

**`path`** \<string\> A path to an mmdb (maxmind) file.

---

### **`geoip_country`**

<aside style="padding:15px; border-radius:5px;">

**EXPERIMENTAL**

This method is experimental and therefore breaking changes could be made to it outside of major version releases.
</aside>

Looks up an IP address against a MaxMind database file and, if found, returns an object describing the country associated with it.

**Parameters**

**`path`** \<string\> A path to an mmdb (maxmind) file.

---

### **`geoip_domain`**

<aside style="padding:15px; border-radius:5px;">

**EXPERIMENTAL**

This method is experimental and therefore breaking changes could be made to it outside of major version releases.
</aside>

Looks up an IP address against a MaxMind database file and, if found, returns an object describing the domain associated with it.

**Parameters**

**`path`** \<string\> A path to an mmdb (maxmind) file.

---

### **`geoip_enterprise`**

<aside style="padding:15px; border-radius:5px;">

**EXPERIMENTAL**

This method is experimental and therefore breaking changes could be made to it outside of major version releases.

</aside>

Looks up an IP address against a MaxMind database file and, if found, returns an object describing the enterprise associated with it.

**Parameters**

**`path`** \<string\> A path to an mmdb (maxmind) file.

---

### **`geoip_isp`**

<aside style="padding:15px; border-radius:5px;">

**EXPERIMENTAL**

This method is experimental and therefore breaking changes could be made to it outside of major version releases.

</aside>

Looks up an IP address against a MaxMind database file and, if found, returns an object describing the ISP associated with it.

**Parameters**

**`path`** \<string\> A path to an mmdb (maxmind) file.

## Deprecated

### **`format_timestamp`**

Attempts to format a timestamp value as a string according to a specified format, or RFC 3339 by default. Timestamp values can either be a numerical unix time in seconds (with up to nanosecond precision via decimals), or a string in RFC 3339 format.

The output format is defined by showing how the reference time, defined to be Mon Jan 2 15:04:05 -0700 MST 2006, would be displayed if it were the value. For an alternative way to specify formats check out the ts_strftime method.

**Parameters**

**`format`** \<string, default "2006-01-02T15:04:05.999999999Z07:00"\> The output format to use.

**`tz`** \<(optional) string\> An optional timezone to use, otherwise the timezone of the input string is used, or in the case of unix timestamps the local timezone is used.

---

### **`format_timestamp_strftime`**

Attempts to format a timestamp value as a string according to a specified strftime-compatible format. Timestamp values can either be a numerical unix time in seconds (with up to nanosecond precision via decimals), or a string in RFC 3339 format.

**Parameters**

**`format`** \<string\> The output format to use.

**`tz`** \<(optional) string\> An optional timezone to use, otherwise the timezone of the input string is used.

---

### **`format_timestamp_unix`**

Attempts to format a timestamp value as a unix timestamp. Timestamp values can either be a numerical unix time in seconds (with up to nanosecond precision via decimals), or a string in RFC 3339 format. The ts_parse method can be used in order to parse different timestamp formats.

---

### **`format_timestamp_unix_micro`**

Attempts to format a timestamp value as a unix timestamp with microsecond precision. Timestamp values can either be a numerical unix time in seconds (with up to nanosecond precision via decimals), or a string in RFC 3339 format. The ts_parse method can be used in order to parse different timestamp formats.

---

### **`format_timestamp_unix_milli`**

Attempts to format a timestamp value as a unix timestamp with millisecond precision. Timestamp values can either be a numerical unix time in seconds (with up to nanosecond precision via decimals), or a string in RFC 3339 format. The ts_parse method can be used in order to parse different timestamp formats.

---

### **`format_timestamp_unix_nano`**

Attempts to format a timestamp value as a unix timestamp with nanosecond precision. Timestamp values can either be a numerical unix time in seconds (with up to nanosecond precision via decimals), or a string in RFC 3339 format. The ts_parse method can be used in order to parse different timestamp formats.

---

### **`parse_timestamp`**

Attempts to parse a string as a timestamp following a specified format and outputs a timestamp, which can then be fed into methods such as ts_format.

The input format is defined by showing how the reference time, defined to be Mon Jan 2 15:04:05 -0700 MST 2006, would be displayed if it were the value. For an alternative way to specify formats check out the ts_strptime method.

**Parameters**

**`format`** \<string\> The format of the target string.

---

### **`parse_timestamp_strptime`**

Attempts to parse a string as a timestamp following a specified strptime-compatible format and outputs a timestamp, which can then be fed into ts_format.

**Parameters**

**`format`** \<string\> The format of the target string.