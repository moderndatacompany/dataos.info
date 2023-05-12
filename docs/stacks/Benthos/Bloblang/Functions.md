# Functions

Functions can be placed anywhere and allow you to extract information from your environment, generate values, or access data from the underlying message being mapped:

```python
root.doc.id = uuid_v4()
root.doc.received_at = now()
root.doc.host = hostname()
```

Functions support both named and nameless style arguments:

```python
root.values_one = range(start: 0, stop: this.max, step: 2)
root.values_two = range(0, this.max, 2)
```

## General

### `count`

The `count` function is a counter starting at 1 which increments after each time it is called. Count takes an argument which is an identifier for the counter, allowing you to specify multiple unique counters in your configuration.

### Parameters

`name` <string> An identifier for the counter.

### Examples

```python
root = this
root.id = count("bloblang_function_example")

# In:  {"message":"foo"}
# Out: {"id":1,"message":"foo"}

# In:  {"message":"bar"}
# Out: {"id":2,"message":"bar"}
```

---

### `deleted`

A function that returns a result indicating that the mapping target should be deleted. Deleting, also known as dropping, messages will result in them being acknowledged as successfully processed to inputs in a Benthos pipeline. For more information about error handling patterns, read here.

### Examples

```python
root = this
root.bar = deleted()

# In:  {"bar":"bar_value","baz":"baz_value","foo":"foo value"}
# Out: {"baz":"baz_value","foo":"foo value"}
```

Since the result is a value, it can be used to do things like remove elements of an array within `map_each`.

```python
root.new_nums = this.nums.map_each(num -> if num < 10 { deleted() } else { num - 10 })

# In:  {"nums":[3,11,4,17]}
# Out: {"new_nums":[1,7]}
```

---

### `ksuid`

Generates a new ksuid each time it is invoked and prints a string representation.

### Examples

```python
root.id = ksuid()
```

---

### `nanoid`

Generates a new nanoid each time it is invoked and prints a string representation.

### Parameters

`length` <(optional) integer> An optional length.`alphabet` <(optional) string> An optional custom alphabet to use for generating IDs. When specified the field `length` must also be present.

### Examples

```python
root.id = nanoid()
```

It is possible to specify an optional length parameter.

```python
root.id = nanoid(54)
```

It is also possible to specify an optional custom alphabet after the length parameter.

```python
root.id = nanoid(54, "abcde")
```

---

### `random_int`

Generates a non-negative pseudo-random 64-bit integer. An optional integer argument can be provided in order to seed the random number generator. Optional `min` and `max` arguments can be provided to make the generated numbers within a range.

### Parameters

`seed` <query expression, default `{"Value":0}`> A seed to use, if a query is provided it will only be resolved once during the lifetime of the mapping.`min` <integer, default `0`> The minimum value the random generated number will have. The default value is 0.`max` <integer, default `9223372036854775806`> The maximum value the random generated number will have. The default value is 9223372036854775806 (math.MaxInt64 - 1).

### Examples

```python
root.first = random_int()
root.second = random_int(1)
root.third = random_int(max:20)
root.fourth = random_int(min:10, max:20)
root.fifth = random_int(timestamp_unix_nano(), 5, 20)
root.sixth = random_int(seed:timestamp_unix_nano(), max:20)
```

It is possible to specify a dynamic seed argument, in which case the argument will only be resolved once during the lifetime of the mapping.

```python
root.first = random_int(timestamp_unix_nano())
```

---

### `range`

The `range` function creates an array of integers following a range between a start, stop, and optional step integer argument. If the step argument is omitted, then it defaults to 1. A negative step can be provided as long as stop < start.

### Parameters

`start` <integer> The start value.`stop` <integer> The stop value.`step` <integer, default `1`> The step value.

### Examples

```python
root.a = range(0, 10)
root.b = range(start: 0, stop: this.max, step: 2) # Using named params
root.c = range(0, -this.max, -2)

# In:  {"max":10}
# Out: {"a":[0,1,2,3,4,5,6,7,8,9],"b":[0,2,4,6,8],"c":[0,-2,-4,-6,-8]}
```

---

### `snowflake_id`

Generate a new snowflake ID each time it is invoked and prints a string representation. I.e.: 1559229974454472704

### Parameters

`node_id` <integer, default `1`> It is possible to specify the node_id.

### Examples

```python
root.id = snowflake_id()
```

It is possible to specify the node_id.

```python
root.id = snowflake_id(2)
```

---

### `throw`

Throws an error similar to a regular mapping error. This is useful for abandoning a mapping entirely given certain conditions.

### Parameters

`why` <string> A string explanation for why an error was thrown, this will be added to the resulting error message.

### Examples

```python
root.doc.type = match {
  this.exists("header.id") => "foo"
  this.exists("body.data") => "bar"
  _ => throw("unknown type")
}
root.doc.contents = (this.body.content | this.thing.body)

# In:  {"header":{"id":"first"},"thing":{"body":"hello world"}}
# Out: {"doc":{"contents":"hello world","type":"foo"}}

# In:  {"nothing":"matches"}
# Out: Error("failed assignment (line 1): unknown type")
```

---

### `uuid_v4`

Generates a new RFC-4122 UUID each time it is invoked and prints a string representation.

### Examples

```python
root.id = uuid_v4()
```

---

## Message Info

### `batch_index`

Returns the index of the mapped message within a batch. This is useful for applying maps only on certain messages of a batch.

### Examples

```python
root = if batch_index() > 0 { deleted() }
```

---

### `batch_size`

Returns the size of the message batch.

### Examples

```python
root.foo = batch_size()
```

---

### `content`

Returns the full raw contents of the mapping target message as a byte array. When mapping to a JSON field, the value should be encoded using the method [encode](https://www.benthos.dev/docs/guides/bloblang/methods#encode), or cast to a string directly using the method [string](https://www.benthos.dev/docs/guides/bloblang/methods#string); otherwise it will be base64 encoded by default.

### Examples

```python
root.doc = content().string()

# In:  {"foo":"bar"}
# Out: {"doc":"{\"foo\":\"bar\"}"}
```

---

### `error`

If an error has occurred during the processing of a message, this function returns the reported cause of the error as a string, otherwise `null`. For more information about error handling patterns, read here.

### Examples

```python
root.doc.error = error()
```

---

### `errored`

Returns a boolean value indicating whether an error has occurred during the processing of a message. For more information about error handling patterns, read here.

### Examples

```python
root.doc.status = if errored() { 400 } else { 200 }
```

---

### `json`

Returns the value of a field within a JSON message located by a dot path argument. This function always targets the entire source JSON document regardless of the mapping context.

### Parameters

`path` <string, default `""`> An optional dot path identifying a field to obtain.

### Examples

```python
root.mapped = json("foo.bar")

# In:  {"foo":{"bar":"hello world"}}
# Out: {"mapped":"hello world"}
```

The path argument is optional, and if omitted, the entire JSON payload is returned.

```python
root.doc = json()

# In:  {"foo":{"bar":"hello world"}}
# Out: {"doc":{"foo":{"bar":"hello world"}}}
```

---

### `meta`

Returns the value of a metadata key from the input message as a string or `null` if the key does not exist. Since values are extracted from the read-only input message, they do NOT reflect changes made from within the map. In order to query metadata mutations made within a mapping, use the `root_meta` function. This function supports extracting metadata from other messages of a batch with the `from` method.

### Parameters

`key` <string, default `""`> An optional key of a metadata value to obtain.

### Examples

```python
root.topic = meta("kafka_topic")
```

The key parameter is optional, and if omitted, the entire metadata contents are returned as an object.

```python
root.all_metadata = meta()
```

---

### `root_meta`

> 🗣 BETA
This function is mostly stable but breaking changes could still be made outside of major version releases if a fundamental problem with it is found.


Returns the value of a metadata key from the new message being created as a string or `null` if the key does not exist. Changes made to metadata during mapping will be reflected by this function.

### Parameters

`key` <string, default `""`> An optional key of a metadata value to obtain.

### Examples

```python
root.topic = root_meta("kafka_topic")
```

The key parameter is optional and if omitted the entire metadata contents are returned as an object.

```python
root.all_metadata = root_meta()
```

---

### `tracing_id`

> 🗣 EXPERIMENTAL
This function is experimental, and therefore breaking changes could be made to it outside of major version releases.

Provides the message trace id. The returned value will be zeroed if the message does not contain a span.

### Examples

```python
meta trace_id = tracing_id()
```

---

### `tracing_span`

> 🗣 EXPERIMENTAL
This function is experimental, and therefore breaking changes could be made to it outside of major version releases.

Provides the message tracing span (created via Open Telemetry APIs) as an object serialized via text map formatting. The returned value will be `null` if the message does not have a span.

### Examples

```python
root.headers.traceparent = tracing_span().traceparent

# In:  {"some_stuff":"just can't be explained by science"}
# Out: {"headers":{"traceparent":"00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01"}}
```

---

## Environment

### `env`

Returns the value of an environment variable, or `null` if the environment variable does not exist.

### Parameters

`name` <string> The name of an environment variable.

### Examples

```python
root.thing.key = env("key").or("default value")
```

---

### `file`

Reads a file and returns its contents. Relative paths are resolved from the directory of the process executing the mapping.

### Parameters

`path` <string> The path of the target file.

### Examples

```python
root.doc = file(env("BENTHOS_TEST_BLOBLANG_FILE")).parse_json()

# In:  {}
# Out: {"doc":{"foo":"bar"}}
```

---

### `hostname`

Returns a string matching the hostname of the machine running Benthos.

### Examples

```python
root.thing.host = hostname()
```

---

### `now`

Returns the current timestamp as a string in RFC 3339 format with the local timezone. Use the method `ts_format` in order to change the format and timezone.

### Examples

```python
root.received_at = now()
```

```python
root.received_at = now().ts_format("Mon Jan 2 15:04:05 -0700 MST 2006", "UTC")
```

---

### `timestamp_unix`

Returns the current unix timestamp in seconds.

### Examples

```python
root.received_at = timestamp_unix()
```

---

### `timestamp_unix_micro`

Returns the current unix timestamp in microseconds.

### Examples

```python
root.received_at = timestamp_unix_micro()
```

---

### `timestamp_unix_milli`

Returns the current unix timestamp in milliseconds.

### Examples

```python
root.received_at = timestamp_unix_milli()
```

---

### `timestamp_unix_nano`

Returns the current unix timestamp in nanoseconds.

### Examples

```python
root.received_at = timestamp_unix_nano()
```

---

## Fake Data Generation

### `fake`

> 🗣 BETA
This function is mostly stable, but breaking changes could still be made outside of major version releases if a fundamental problem with it is found.


Takes in a string that maps to a [faker](https://github.com/bxcodec/faker) function and returns the result from that faker function. Returns an error if the given string doesn't match a supported faker function. Supported functions: `latitude`, `longitude`, `unix_time`, `date`, `time_string`, `month_name`, `year_string`, `day_of_week`, `day_of_month`, `timestamp`, `century`, `timezone`, `time_period`, `email`, `mac_address`, `domain_name`, `url`, `username`, `ipv4`, `ipv6`, `password`, `jwt`, `word`, `sentence`, `paragraph`, `cc_type`, `cc_number`, `currency`, `amount_with_currency`, `title_male`, `title_female`, `first_name`, `first_name_male`, `first_name_female`, `last_name`, `name`, `gender`, `chinese_first_name`, `chinese_last_name`, `chinese_name`, `phone_number`, `toll_free_phone_number`, `e164_phone_number`, `uuid_hyphenated`, `uuid_digit`. Refer to the [faker](https://github.com/bxcodec/faker) docs for details on these functions.

### Parameters

`function` <string, default `""`> The name of the function to use to generate the value.

### Examples

Use `time_string` to generate a time in the format `00:00:00`:

```python
root.time = fake("time_string")
```

Use `email` to generate a string in email address format:

```python
root.email = fake("email")
```

Use `jwt` to generate a JWT token:

```python
root.jwt = fake("jwt")
```

Use `uuid_hyphenated` to generate a hypenated UUID:

```python
root.uuid = fake("uuid_hyphenated")
```