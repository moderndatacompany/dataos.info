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

## General[](https://www.benthos.dev/docs/guides/bloblang/functions#general)

### `count`[](https://www.benthos.dev/docs/guides/bloblang/functions#count)

The `count` function is a counter starting at 1 which increments after each time it is called. Count takes an argument which is an identifier for the counter, allowing you to specify multiple unique counters in your configuration.

### Parameters[](https://www.benthos.dev/docs/guides/bloblang/functions#parameters)

**`name`** <string> An identifier for the counter.

### Examples[](https://www.benthos.dev/docs/guides/bloblang/functions#examples)

```python
root = this
root.id = count("bloblang_function_example")

# In:  {"message":"foo"}
# Out: {"id":1,"message":"foo"}

# In:  {"message":"bar"}
# Out: {"id":2,"message":"bar"}
```


Returns the value of a metadata key from the new message being created as a string or `null` if the key does not exist. Changes made to metadata during mapping will be reflected by this function.

### Parameters[](https://www.benthos.dev/docs/guides/bloblang/functions#parameters-8)

**`key`** <string, default `""`> An optional key of a metadata value to obtain.

### Examples[](https://www.benthos.dev/docs/guides/bloblang/functions#examples-16)

```python
root.topic = root_meta("kafka_topic")
```

The key parameter is optional and if omitted the entire metadata contents are returned as an object.

```python
root.all_metadata = root_meta()
```


Provides the message trace id. The returned value will be zeroed if the message does not contain a span.

### Examples[](https://www.benthos.dev/docs/guides/bloblang/functions#examples-17)

```python
meta trace_id = tracing_id()
```


Provides the message tracing span (created via Open Telemetry APIs) as an object serialized via text map formatting. The returned value will be `null` if the message does not have a span.

### Examples[](https://www.benthos.dev/docs/guides/bloblang/functions#examples-18)

```python
root.headers.traceparent = tracing_span().traceparent

# In:  {"some_stuff":"just can't be explained by science"}
# Out: {"headers":{"traceparent":"00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01"}}
```


Takes in a string that maps to a [faker](https://github.com/bxcodec/faker) function and returns the result from that faker function. Returns an error if the given string doesn't match a supported faker function. Supported functions: `latitude`, `longitude`, `unix_time`, `date`, `time_string`, `month_name`, `year_string`, `day_of_week`, `day_of_month`, `timestamp`, `century`, `timezone`, `time_period`, `email`, `mac_address`, `domain_name`, `url`, `username`, `ipv4`, `ipv6`, `password`, `jwt`, `word`, `sentence`, `paragraph`, `cc_type`, `cc_number`, `currency`, `amount_with_currency`, `title_male`, `title_female`, `first_name`, `first_name_male`, `first_name_female`, `last_name`, `name`, `gender`, `chinese_first_name`, `chinese_last_name`, `chinese_name`, `phone_number`, `toll_free_phone_number`, `e164_phone_number`, `uuid_hyphenated`, `uuid_digit`. Refer to the [faker](https://github.com/bxcodec/faker) docs for details on these functions.

### Parameters[](https://www.benthos.dev/docs/guides/bloblang/functions#parameters-11)

**`function`** <string, default `""`> The name of the function to use to generate the value.

### Examples[](https://www.benthos.dev/docs/guides/bloblang/functions#examples-27)

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