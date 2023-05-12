# Timestamp Manipulation

### `parse_duration`

Attempts to parse a string as a duration and returns an integer of nanoseconds. A duration string is a possibly signed sequence of decimal numbers, each with an optional fraction and a unit suffix, such as "300ms", "-1.5h" or "2h45m". Valid time units are "ns", "us" (or "µs"), "ms", "s", "m", "h".

### Examples

```python
root.delay_for_ns = this.delay_for.parse_duration()

# In:  {"delay_for":"50us"}
# Out: {"delay_for_ns":50000}
```

```python
root.delay_for_s = this.delay_for.parse_duration() / 1000000000

# In:  {"delay_for":"2h"}
# Out: {"delay_for_s":7200}
```

---

### `parse_duration_iso8601`


> 🗣 BETA
This method is mostly stable but breaking changes could still be made outside of major version releases if a fundamental problem with it is found.


Attempts to parse a string using ISO-8601 rules as a duration and returns an integer of nanoseconds. A duration string is represented by the format "P[n]Y[n]M[n]DT[n]H[n]M[n]S" or "P[n]W". In these representations, the "[n]" is replaced by the value for each of the date and time elements that follow the "[n]". For example, "P3Y6M4DT12H30M5S" represents a duration of "three years, six months, four days, twelve hours, thirty minutes, and five seconds". The last field of the format allows fractions with one decimal place, so "P3.5S" will return 3500000000ns. Any additional decimals will be truncated.

### Examples

Arbitrary ISO-8601 duration string to nanoseconds:

```python
root.delay_for_ns = this.delay_for.parse_duration_iso8601()

# In:  {"delay_for":"P3Y6M4DT12H30M5S"}
# Out: {"delay_for_ns":110839937000000000}
```

Two hours ISO-8601 duration string to seconds:

```python
root.delay_for_s = this.delay_for.parse_duration_iso8601() / 1000000000

# In:  {"delay_for":"PT2H"}
# Out: {"delay_for_s":7200}
```

Two and a half seconds ISO-8601 duration string to seconds:

```python
root.delay_for_s = this.delay_for.parse_duration_iso8601() / 1000000000

# In:  {"delay_for":"PT2.5S"}
# Out: {"delay_for_s":2.5}
```

---

### `ts_format`

> 🗣 BETA
This method is mostly stable, but breaking changes could still be made outside of major version releases if a fundamental problem with it is found.


Attempts to format a timestamp value as a string according to a specified format, or RFC 3339 by default. Timestamp values can either be a numerical unix time in seconds (with up to nanosecond precision via decimals), or a string in RFC 3339 format.

The output format is defined by showing how the reference time, defined to be Mon Jan 2 15:04:05 -0700 MST 2006, would be displayed if it were the value. For an alternative way to specify formats check out the `ts_strftime` method.

### Parameters

`format` <string, default `"2006-01-02T15:04:05.999999999Z07:00"`> The output format to use.`tz` <(optional) string> An optional timezone to use, otherwise the timezone of the input string is used, or in the case of unix timestamps the local timezone is used.

### Examples

```python
root.something_at = (this.created_at + 300).ts_format()
```

An optional string argument can be used in order to specify the output format of the timestamp. The format is defined by showing how the reference time, defined to be Mon Jan 2 15:04:05 -0700 MST 2006, would be displayed if it were the value.

```python
root.something_at = (this.created_at + 300).ts_format("2006-Jan-02 15:04:05")
```

A second optional string argument can also be used in order to specify a timezone; otherwise, the timezone of the input string is used, or in the case of unix timestamps, the local timezone is used.

```python
root.something_at = this.created_at.ts_format(format: "2006-Jan-02 15:04:05", tz: "UTC")

# In:  {"created_at":1597405526}
# Out: {"something_at":"2020-Aug-14 11:45:26"}

# In:  {"created_at":"2020-08-14T11:50:26.371Z"}
# Out: {"something_at":"2020-Aug-14 11:50:26"}
```

And `ts_format` supports up to nanosecond precision with floating point timestamp values.

```python
root.something_at = this.created_at.ts_format("2006-Jan-02 15:04:05.999999", "UTC")

# In:  {"created_at":1597405526.123456}
# Out: {"something_at":"2020-Aug-14 11:45:26.123456"}

# In:  {"created_at":"2020-08-14T11:50:26.371Z"}
# Out: {"something_at":"2020-Aug-14 11:50:26.371"}
```

---

### `ts_parse`


> 🗣 BETA
This method is mostly stable, but breaking changes could still be made outside of major version releases if a fundamental problem with it is found.


Attempts to parse a string as a timestamp following a specified format and outputs a timestamp, which can then be fed into methods such as `ts_format`.

The input format is defined by showing how the reference time, defined to be Mon Jan 2 15:04:05 -0700 MST 2006, would be displayed if it were the value. For an alternative way to specify formats check out the `ts_strptime` method.

### Parameters

`format` <string> The format of the target string.

### Examples

```python
root.doc.timestamp = this.doc.timestamp.ts_parse("2006-Jan-02")

# In:  {"doc":{"timestamp":"2020-Aug-14"}}
# Out: {"doc":{"timestamp":"2020-08-14T00:00:00Z"}}
```

---

### `ts_round`

> 🗣 BETA
This method is mostly stable, but breaking changes could still be made outside of major version releases if a fundamental problem with it is found.


Returns the result of rounding a timestamp to the nearest multiple of the argument duration (nanoseconds). The rounding behavior for halfway values is to round up. Timestamp values can either be a numerical unix time in seconds (with up to nanosecond precision via decimals), or a string in RFC 3339 format. The `ts_parse` method can be used in order to parse different timestamp formats.

### Parameters

`duration` <integer> A duration measured in nanoseconds to round by.

### Examples

Use the method `parse_duration` to convert a duration string into an integer argument.

```python
root.created_at_hour = this.created_at.ts_round("1h".parse_duration())

# In:  {"created_at":"2020-08-14T05:54:23Z"}
# Out: {"created_at_hour":"2020-08-14T06:00:00Z"}
```

---

### `ts_strftime`

> 🗣 BETA
This method is mostly stable, but breaking changes could still be made outside of major version releases if a fundamental problem with it is found.


Attempts to format a timestamp value as a string according to a specified strftime-compatible format. Timestamp values can either be a numerical unix time in seconds (with up to nanosecond precision via decimals) or a string in RFC 3339 format.

### Parameters

`format` <string> The output format to use.`tz` <(optional) string> An optional timezone to use, otherwise the timezone of the input string is used.

### Examples

The format consists of zero or more conversion specifiers and ordinary characters (except `%`). All ordinary characters are copied to the output string without modification. Each conversion specification begins with `%` character followed by the character that determines the behavior of the specifier. Please refer to [man 3 strftime](https://linux.die.net/man/3/strftime) for the list of format specifiers.

```python
root.something_at = (this.created_at + 300).ts_strftime("%Y-%b-%d %H:%M:%S")
```

A second optional string argument can also be used in order to specify a timezone, otherwise, the timezone of the input string is used, or in the case of unix timestamps, the local timezone is used.

```python
root.something_at = this.created_at.ts_strftime("%Y-%b-%d %H:%M:%S", "UTC")

# In:  {"created_at":1597405526}
# Out: {"something_at":"2020-Aug-14 11:45:26"}

# In:  {"created_at":"2020-08-14T11:50:26.371Z"}
# Out: {"something_at":"2020-Aug-14 11:50:26"}
```

As an extension provided by the underlying formatting library, [itchyny/timefmt-go](https://github.com/itchyny/timefmt-go), the `%f` directive is supported for zero-padded microseconds, which originates from Python. Note that E and O modifier characters are not supported.

```python
root.something_at = this.created_at.ts_strftime("%Y-%b-%d %H:%M:%S.%f", "UTC")

# In:  {"created_at":1597405526}
# Out: {"something_at":"2020-Aug-14 11:45:26.000000"}

# In:  {"created_at":"2020-08-14T11:50:26.371Z"}
# Out: {"something_at":"2020-Aug-14 11:50:26.371000"}
```

---

### `ts_strptime`

> 🗣 BETA
This method is mostly stable, but breaking changes could still be made outside of major version releases if a fundamental problem with it is found.

Attempts to parse a string as a timestamp following a specified strptime-compatible format and outputs a timestamp, which can then be fed into `ts_format`.

### Parameters

`format` <string> The format of the target string.

### Examples

The format consists of zero or more conversion specifiers and ordinary characters (except `%`). All ordinary characters are copied to the output string without modification. Each conversion specification begins with a `%` character followed by the character that determines the behavior of the specifier. Please refer to [man 3 strptime](https://linux.die.net/man/3/strptime) for the list of format specifiers.

```python
root.doc.timestamp = this.doc.timestamp.ts_strptime("%Y-%b-%d")

# In:  {"doc":{"timestamp":"2020-Aug-14"}}
# Out: {"doc":{"timestamp":"2020-08-14T00:00:00Z"}}
```

As an extension provided by the underlying formatting library, [itchyny/timefmt-go](https://github.com/itchyny/timefmt-go), the `%f` directive is supported for zero-padded microseconds, which originates from Python. Note that E and O modifier characters are not supported.

```python
root.doc.timestamp = this.doc.timestamp.ts_strptime("%Y-%b-%d %H:%M:%S.%f")

# In:  {"doc":{"timestamp":"2020-Aug-14 11:50:26.371000"}}
# Out: {"doc":{"timestamp":"2020-08-14T11:50:26.371Z"}}
```

---

### `ts_tz`

> 🗣 BETA
This method is mostly stable, but breaking changes could still be made outside of major version releases if a fundamental problem with it is found.

Returns the result of converting a timestamp to a specified timezone. Timestamp values can either be a numerical unix time in seconds (with up to nanosecond precision via decimals) or a string in RFC 3339 format. The `ts_parse` method can be used in order to parse different timestamp formats.

### Parameters

`tz` <string> The timezone to change to. If set to "UTC" then the timezone will be UTC. If set to "Local" then the local timezone will be used. Otherwise, the argument is taken to be a location name corresponding to a file in the IANA Time Zone database, such as "America/New_York".

### Examples

```python
root.created_at_utc = this.created_at.ts_tz("UTC")

# In:  {"created_at":"2021-02-03T17:05:06+01:00"}
# Out: {"created_at_utc":"2021-02-03T16:05:06Z"}
```

---

### `ts_unix`

> 🗣 BETA
This method is mostly stable, but breaking changes could still be made outside of major version releases if a fundamental problem with it is found.


Attempts to format a timestamp value as a unix timestamp. Timestamp values can either be a numerical unix time in seconds (with up to nanosecond precision via decimals) or a string in RFC 3339 format. The `ts_parse` method can be used in order to parse different timestamp formats.

### Examples

```python
root.created_at_unix = this.created_at.ts_unix()

# In:  {"created_at":"2009-11-10T23:00:00Z"}
# Out: {"created_at_unix":1257894000}
```

---

### `ts_unix_micro`

> 🗣 BETA
This method is mostly stable, but breaking changes could still be made outside of major version releases if a fundamental problem with it is found.


Attempts to format a timestamp value as a unix timestamp with microsecond precision. Timestamp values can either be a numerical unix time in seconds (with up to nanosecond precision via decimals) or a string in RFC 3339 format. The `ts_parse` method can be used in order to parse different timestamp formats.

### Examples

```python
root.created_at_unix = this.created_at.ts_unix_micro()

# In:  {"created_at":"2009-11-10T23:00:00Z"}
# Out: {"created_at_unix":1257894000000000}
```

---

### `ts_unix_milli`

> 🗣 BETA
This method is mostly stable, but breaking changes could still be made outside of major version releases if a fundamental problem with it is found.


Attempts to format a timestamp value as a unix timestamp with millisecond precision. Timestamp values can either be a numerical unix time in seconds (with up to nanosecond precision via decimals) or a string in RFC 3339 format. The `ts_parse` method can be used in order to parse different timestamp formats.

### Examples

```python
root.created_at_unix = this.created_at.ts_unix_milli()

# In:  {"created_at":"2009-11-10T23:00:00Z"}
# Out: {"created_at_unix":1257894000000}
```

---

### `ts_unix_nano`

> 🗣 BETA
This method is mostly stable, but breaking changes could still be made outside of major version releases if a fundamental problem with it is found.

Attempts to format a timestamp value as a unix timestamp with nanosecond precision. Timestamp values can either be a numerical unix time in seconds (with up to nanosecond precision via decimals) or a string in RFC 3339 format. The `ts_parse` method can be used in order to parse different timestamp formats.

### Examples

```python
root.created_at_unix = this.created_at.ts_unix_nano()

# In:  {"created_at":"2009-11-10T23:00:00Z"}
# Out: {"created_at_unix":1257894000000000000}
```