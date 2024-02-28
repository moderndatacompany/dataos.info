# Date and time functions and operators

These functions and operators operate on data type- [date and time](#date-and-time-data-types)

## Date and time operators

| Operator | Example                                             | Result                    |
| -------- | --------------------------------------------------- | ------------------------- |
| `+`      | `date '2012-08-08' + interval '2' day`              | `2012-08-10`              |
| `+`      | `time '01:00' + interval '3' hour`                  | `04:00:00.000`            |
| `+`      | `timestamp '2012-08-08 01:00' + interval '29' hour` | `2012-08-09 06:00:00.000` |
| `+`      | `timestamp '2012-10-31 01:00' + interval '1' month` | `2012-11-30 01:00:00.000` |
| `+`      | `interval '2' day + interval '3' hour`              | `2 03:00:00.000`          |
| `+`      | `interval '3' year + interval '5' month`            | `3-5`                     |
| `-`      | `date '2012-08-08' - interval '2' day`              | `2012-08-06`              |
| `-`      | `time '01:00' - interval '3' hour`                  | `22:00:00.000`            |
| `-`      | `timestamp '2012-08-08 01:00' - interval '29' hour` | `2012-08-06 20:00:00.000` |
| `-`      | `timestamp '2012-10-31 01:00' - interval '1' month` | `2012-09-30 01:00:00.000` |
| `-`      | `interval '2' day - interval '3' hour`              | `1 21:00:00.000`          |
| `-`      | `interval '3' year - interval '5' month`            | `2-7`                     |


## Time zone conversion

The `AT TIME ZONE` operator sets the time zone of a timestamp:

```sql
SELECT timestamp '2012-10-31 01:00 UTC';
-- 2012-10-31 01:00:00.000 UTC

SELECT timestamp '2012-10-31 01:00 UTC' AT TIME ZONE 'America/Los_Angeles';
-- 2012-10-30 18:00:00.000 America/Los_Angeles
```

## Date and time function

| Function               | Description                                                                          |
|------------------------|--------------------------------------------------------------------------------------|
| `current_date`         | Returns the current date as of the start of the query.                               |
| `current_time`         | Returns the current time with time zone as of the start of the query.                |
| `current_timestamp`    | Returns the current timestamp with time zone as of the start of the query.           |
| `current_timestamp(p)` | Returns the current timestamp with time zone as of the start of the query, with p digits of subsecond precision. |
| `current_timezone()`   | Returns the current time zone in the format defined by IANA (e.g., America/Los_Angeles) or as a fixed offset from UTC (e.g., +08:35). |

**Examples:**

- For `current_date`:
  ```sql
  SELECT current_date AS current_date_result;

### **`date`**

| Function | Description                      |
|----------|----------------------------------|
| `date(x)` | Alias for CAST(x AS date).       |

### **`from_iso8601_timestamo_nanos()`**

| Function                                    | Description                                                                                               |
|---------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| `from_iso8601_timestamp_nanos(string)`      | Parses the ISO 8601 formatted date and time string into a timestamp(9) with time zone. The time zone defaults to the session time zone. |

**Examples:**
```sql
SELECT from_iso8601_timestamp_nanos('2020-05-11T11:15:05') AS timestamp_nanos_result;
-- 2020-05-11 11:15:05.000000000 America/Vancouver

SELECT from_iso8601_timestamp_nanos('2020-05-11T11:15:05.123456789+01:00') AS timestamp_nanos_offset_result;
-- 2020-05-11 11:15:05.123456789 +01:00
```

### **`from_iso8601_date()`**

| Function                              | Description                                                                                    |
|---------------------------------------|------------------------------------------------------------------------------------------------|
| `from_iso8601_date(string)`           | Parses the ISO 8601 formatted date string into a date. The date can be a calendar date, a week date using ISO week numbering, or year and day of year combined. |

**Examples:**
```sql
SELECT from_iso8601_date('2020-05-11') AS iso8601_date_result;
-- 2020-05-11

SELECT from_iso8601_date('2020-W10') AS iso8601_week_date_result;
```

### **`at_timezone`**

| Function                            | Description                                                                                                                             |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| `at_timezone(timestamp(p), zone)`   | Returns the timestamp specified in timestamp with the time zone converted from the session time zone to the time zone specified in zone with precision p. In the example below, the session time zone is set to America/New_York, which is three hours ahead of America/Los_Angeles. |

**Examples:**
```sql
-- Retrieve the session time zone
SELECT current_timezone();
-- America/New_York

-- Convert timestamp to a different time zone
SELECT at_timezone(TIMESTAMP '2022-11-01 09:08:07.321', 'America/Los_Angeles');
-- 2022-11-01 06:08:07.321 America/Los_Angeles
```
###  **`with_timezone()`**

| Function                              | Description                                                                                                                   |
|---------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| `with_timezone(timestamp(p), zone)`  | Returns the timestamp specified in timestamp with the time zone specified in zone with precision p. In the example below, the session time zone is set to America/New_York. |

**Examples:**
```sql
-- Retrieve the session time zone
SELECT current_timezone();
-- America/New_York

-- Set timestamp to a different time zone
SELECT with_timezone(TIMESTAMP '2022-11-01 09:08:07.321', 'America/Los_Angeles');
-- 2022-11-01 09:08:07.321 America/Los_Angeles
```
### **`from_unixtime()`**

| Function                                     | Description                                                                                                                                     |
|----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| `from_unixtime(unixtime)`                    | Returns the UNIX timestamp `unixtime` as a timestamp with time zone. `unixtime` is the number of seconds since 1970-01-01 00:00:00 UTC.               |
| `from_unixtime(unixtime, zone)`              | Returns the UNIX timestamp `unixtime` as a timestamp with time zone using `zone` for the time zone. `unixtime` is the number of seconds since 1970-01-01 00:00:00 UTC. |
| `from_unixtime(unixtime, hours, minutes)`    | Returns the UNIX timestamp `unixtime` as a timestamp with time zone using `hours` and `minutes` for the time zone offset. `unixtime` is the number of seconds since 1970-01-01 00:00:00 in double data type. |
| `from_unixtime_nanos(unixtime)`              | Returns the UNIX timestamp `unixtime` as a timestamp with time zone. `unixtime` is the number of nanoseconds since 1970-01-01 00:00:00 UTC.          |


**Examples:**
- For `from_unixtime(unixtime)`:
  ```sql
  SELECT from_unixtime(unixtime) AS result_timestamp;
  -- Result: timestamp(3) with time zone
    ```

### **`localtime`**


| Function   | Description                                      |
|------------|--------------------------------------------------|
| `localtime` | Returns the current time as of the start of the query. |


### **`localtimestamp`**

| Function             | Description                                                                    |
|----------------------|--------------------------------------------------------------------------------|
| `localtimestamp`     | Returns the current timestamp as of the start of the query, with 3 digits of subsecond precision. |
| `localtimestamp(p)`  | Returns the current timestamp as of the start of the query, with p digits of subsecond precision. |


### **`now()`**

| Function | Description                                                |
|----------|------------------------------------------------------------|
| `now()`  | This is an alias for `current_timestamp`.                  |

## **`to_iso8601()`**

| Function      | Description                                                                         |
|---------------|-------------------------------------------------------------------------------------|
| `to_iso8601(x)` | Formats x as an ISO 8601 string. x can be date, timestamp, or timestamp with time zone. |

**Example:**
```sql
-- For date
SELECT to_iso8601(DATE '2022-05-31') AS iso8601_date_result;
-- Result: "2022-05-31"

-- For timestamp
SELECT to_iso8601(TIMESTAMP '2022-05-31 12:30:45') AS iso8601_timestamp_result;
-- Result: "2022-05-31T12:30:45"

-- For timestamp with time zone
SELECT to_iso8601(TIMESTAMP '2022-05-31 12:30:45+03:00') AS iso8601_timestamp_tz_result;
-- Result: "2022-05-31T12:30:45+03:00"
```
### **`to_milliseconds()`**

| Function                        | Description                                      |
|---------------------------------|--------------------------------------------------|
| `to_milliseconds(interval)`     | Returns the day-to-second interval as milliseconds. |

**Example:**
```sql
SELECT to_milliseconds(interval '24000' hour ) AS milliseconds_result;
-- Result: 18393050086400000000
```

### **`to_unixtime()`**

| Function                     | Description                             |
|------------------------------|-----------------------------------------|
| `to_unixtime(timestamp)`      | Returns timestamp as a UNIX timestamp.  |

**Example:**
```sql
SELECT to_unixtime(TIMESTAMP '2022-05-31 12:30:45') AS unix_timestamp_result;
-- Result: 1672487445
```

> **Note:**
>
> The following SQL-standard functions do not use parentheses:
>
> - `current_date`
> - `current_time`
> - `current_timestamp`
> - `localtime`
> - `localtimestamp`

## Truncation function


### **`date_trunc`**

The date_trunc function supports the following units:

| Unit         | Example Truncated Value        |
|--------------|--------------------------------|
| `millisecond`  | 2001-08-22 03:04:05.321        |
| `second`       | 2001-08-22 03:04:05.000        |
| `minute`       | 2001-08-22 03:04:00.000        |
| `hour`         | 2001-08-22 03:00:00.000        |
| `day`          | 2001-08-22 00:00:00.000        |
| `week`         | 2001-08-20 00:00:00.000        |
| `month`        | 2001-08-01 00:00:00.000        |
| `quarter`      | 2001-07-01 00:00:00.000        |
| `year`         | 2001-01-01 00:00:00.000        |


| Function                  | Description                                      |
|---------------------------|--------------------------------------------------|
| `date_trunc(unit, x)  `     | Returns `x` truncated to unit                    |

**Example:**
```sql
SELECT DATE_TRUNC('HOUR', TIMESTAMP '2022-05-17 15:30:45') AS truncated_date;
---2022-05-17 15:00:00.000
```

## Interval functions

The functions in this section support the following interval units:

| Unit          | Description        |
| ------------- | ------------------ |
| `millisecond` | Milliseconds       |
| `second`      | Seconds            |
| `minute`      | Minutes            |
| `hour`        | Hours              |
| `day`         | Days               |
| `week`        | Weeks              |
| `month`       | Months             |
| `quarter`     | Quarters of a year |
| `year`        | Years              |

### **`date_add()`**

| Function                    | Description                                               |
|-----------------------------|-----------------------------------------------------------|
| `date_add(unit, value, timestamp)` | Adds an interval value of type unit to timestamp. Subtraction can be performed by using a negative value. |



```sql
SELECT date_add('second', 86, TIMESTAMP '2020-03-01 00:00:00');
-- 2020-03-01 00:01:26.000

SELECT date_add('hour', 9, TIMESTAMP '2020-03-01 00:00:00');
-- 2020-03-01 09:00:00.000

SELECT date_add('day', -1, TIMESTAMP '2020-03-01 00:00:00 UTC');
-- 2020-02-29 00:00:00.000 UTC
```

### **`date_diff()`**

| Function                    | Description                                               |
|-----------------------------|-----------------------------------------------------------|
| `date_diff(unit, timestamp1, timestamp2)` | Returns timestamp2 - timestamp1 expressed in terms of unit. |


```sql
SELECT date_diff('second', TIMESTAMP '2020-03-01 00:00:00', TIMESTAMP '2020-03-02 00:00:00');
-- 86400

SELECT date_diff('hour', TIMESTAMP '2020-03-01 00:00:00 UTC', TIMESTAMP '2020-03-02 00:00:00 UTC');
-- 24

SELECT date_diff('day', DATE '2020-03-01', DATE '2020-03-02');
-- 1

SELECT date_diff('second', TIMESTAMP '2020-06-01 12:30:45.000000000', TIMESTAMP '2020-06-02 12:30:45.123456789');
-- 86400

SELECT date_diff('millisecond', TIMESTAMP '2020-06-01 12:30:45.000000000', TIMESTAMP '2020-06-02 12:30:45.123456789');
-- 86400123
```

## Duration function

### **`parse_duration()`**

| Function               | Description                                             | Return Type |
|------------------------|---------------------------------------------------------|-------------|
| `parse_duration(string)` | Parses string of format value unit into an interval, where value is a fractional number of unit values. | `interval`    |

```sql
SELECT parse_duration('42.8ms');
-- 0 00:00:00.043

SELECT parse_duration('3.81 d');
-- 3 19:26:24.000

SELECT parse_duration('5m');
-- 0 00:05:00.000
```

### **`human_readable_seconds()`**
| Function                    | Description                                                                      | Return Type |
|-----------------------------|----------------------------------------------------------------------------------|-------------|
| `human_readable_seconds(double)` | Formats the double value of seconds into a human-readable string containing weeks, days, hours, minutes, and seconds. | `varchar`     |

```sql
SELECT human_readable_seconds(96);
-- 1 minute, 36 seconds

SELECT human_readable_seconds(3762);
-- 1 hour, 2 minutes, 42 seconds

SELECT human_readable_seconds(56363463);
-- 93 weeks, 1 day, 8 hours, 31 minutes, 3 seconds
```
## MySQL functions

The functions in this section use a format string that is compatible with the MySQL `date_parse` and `str_to_date` functions. The following table, based on the MySQL manual, describes the format specifiers:

| Specifier | Description                                                        |
|-----------|--------------------------------------------------------------------|
| `%a`      | Abbreviated weekday name (Sun .. Sat)                              |
| `%b`      | Abbreviated month name (Jan .. Dec)                                |
| `%c`      | Month, numeric (1 .. 12), this specifier does not support 0 as a month. |
| `%D`      | Day of the month with English suffix (0th, 1st, 2nd, 3rd, …)       |
| `%d`      | Day of the month, numeric (01 .. 31), this specifier does not support 0 as a month or day. |
| `%e`      | Day of the month, numeric (1 .. 31), this specifier does not support 0 as a day. |
| `%f`      | Fraction of second (6 digits for printing: 000000 .. 999000; 1 - 9 digits for parsing: 0 .. 999999999), timestamp is truncated to milliseconds. |
| `%H`      | Hour (00 .. 23)                                                   |
| `%h`      | Hour (01 .. 12)                                                   |
| `%I`      | Hour (01 .. 12)                                                   |
| `%i`      | Minutes, numeric (00 .. 59)                                       |
| `%j`      | Day of year (001 .. 366)                                          |
| `%k`      | Hour (0 .. 23)                                                    |
| `%l`      | Hour (1 .. 12)                                                    |
| `%M`      | Month name (January .. December)                                   |
| `%m`      | Month, numeric (01 .. 12), this specifier does not support 0 as a month. |
| `%p`      | AM or PM                                                          |
| `%r`      | Time of day, 12-hour (equivalent to %h:%i:%s %p)                  |
| `%S`      | Seconds (00 .. 59)                                                |
| `%s`      | Seconds (00 .. 59)                                                |
| `%T`      | Time of day, 24-hour (equivalent to %H:%i:%s)                     |
| `%U`      | Week (00 .. 53), where Sunday is the first day of the week       |
| `%u`      | Week (00 .. 53), where Monday is the first day of the week       |
| `%V`      | Week (01 .. 53), where Sunday is the first day of the week; used with %X |
| `%v`      | Week (01 .. 53), where Monday is the first day of the week; used with %x |
| `%W`      | Weekday name (Sunday .. Saturday)                                  |
| `%w`      | Day of the week (0 .. 6), where Sunday is the first day of the week, this specifier is not supported, consider using day_of_week() (it uses 1-7 instead of 0-6). |
| `%X`      | Year for the week where Sunday is the first day of the week, numeric, four digits; used with %V |
| `%x`      | Year for the week, where Monday is the first day of the week, numeric, four digits; used with %v |
| `%Y`      | Year, numeric, four digits                                         |
| `%y`      | Year, numeric (two digits), when parsing, two-digit year format assumes range 1970 .. 2069, so “70” will result in year 1970 but “69” will produce 2069. |
| `%%`      | A literal % character                                             |
| `%x`      | x, for any x not listed above                                     |

<aside class="callout">
🗣️ The following specifiers are not currently supported: `%D`, `%U`, `%u`, `%V`, `%w`, `%X` with `` sins on functions.
</aside>

### **`date_format()`**
| Function                 | Description                                                      | Return Type |
|--------------------------|------------------------------------------------------------------|-------------|
| `date_format(timestamp, format) `| Formats timestamp as a string using the specified format.        | `varchar`    |


```sql
SELECT date_format(TIMESTAMP '2022-10-20 05:10:00', '%m-%d-%Y %H');
-- 10-20-2022 05
```
### **`date_parse()`**

| Function                 | Description                                              | Return Type  |
|--------------------------|----------------------------------------------------------|--------------|
| `date_parse(string, format)` | Parses a string into a timestamp using the specified format. | `timestamp(3)` |

```sql
SELECT date_parse('2022/10/20/05', '%Y/%m/%d/%H');
-- 2022-10-20 05:00:00.000
```

## JAVA date function

The functions in this section use a format string that is compatible with JodaTime’s [DateTimeFormat](http://joda-time.sourceforge.net/apidocs/org/joda/time/format/DateTimeFormat.htmlpattern) format.

| Function                       | Description                                                   | Return Type               |
|--------------------------------|---------------------------------------------------------------|---------------------------|
| `format_datetime(timestamp, format)` | Formats timestamp as a string using the specified format.      | `varchar`                  |
| `parse_datetime(string, format)`    | Parses a string into a timestamp with time zone using the specified format. | `timestamp with time zone` |

## Extract function

The `extract()` function supports the following fields:

| `Field`            | Description           |
|--------------------|-----------------------|
| `YEAR`             | year()                |
| `QUARTER`          | quarter()             |
| `MONTH`            | month()               |
| `WEEK`             | week()                |
| `DAY`              | day()                 |
| `DAY_OF_MONTH`     | day()                 |
| `DAY_OF_WEEK`      | day_of_week()         |
| `DOW`              | day_of_week()         |
| `DAY_OF_YEAR`      | day_of_year()         |
| `DOY`              | day_of_year()         |
| `YEAR_OF_WEEK`     | year_of_week()        |
| `YOW`              | year_of_week()        |
| `HOUR`             | hour()                |
| `MINUTE`           | minute()              |
| `SECOND`           | second()              |
| `TIMEZONE_HOUR`    | timezone_hour()       |
| `TIMEZONE_MINUTE`  | timezone_minute()    


The types supported by the `extract` function vary depending on the field to be extracted. Most fields support all date and time types.

| `Function`               | `Description`                        | `Return Type` |
|---------------------------|--------------------------------------|---------------|
| `extract(field FROM x)`   | Returns field from x.                | `bigint`     |

```sql
SELECT extract(YEAR FROM TIMESTAMP '2022-10-20 05:10:00');
-- 2022
```


<aside class="callout"> 🗣️ This SQL-standard function uses special syntax for specifying the arguments.
</aside>


## Convenience extraction functions

| `Function`                  | `Description`                                           | `Return Type` |
|-----------------------------|---------------------------------------------------------|---------------|
| `day(x)`                    | Returns the day of the month from x.                    | `bigint`      |
| `day_of_month(x)`           | Alias for day().                                        | `bigint`      |
| `day_of_week(x)`            | Returns the ISO day of the week from x.                 | `bigint`      |
| `day_of_year(x)`            | Returns the day of the year from x.                     | `bigint`      |
| `dow(x)`                    | Alias for day_of_week().                                | `bigint`      |
| `doy(x)`                    | Alias for day_of_year().                                | `bigint`      |
| `hour(x)`                   | Returns the hour of the day from x.                     | `bigint`      |
| `millisecond(x)`            | Returns the millisecond of the second from x.           | `bigint`      |
| `minute(x)`                 | Returns the minute of the hour from x.                  | `bigint`      |
| `month(x)`                  | Returns the month of the year from x.                   | `bigint`      |
| `quarter(x)`                | Returns the quarter of the year from x.                 | `bigint`      |
| `second(x)`                 | Returns the second of the minute from x.                | `bigint`      |
| `timezone_hour(timestamp)`  | Returns the hour of the time zone offset from timestamp.| `bigint`      |
| `timezone_minute(timestamp)`| Returns the minute of the time zone offset from timestamp.| `bigint`      |
| `week(x)`                   | Returns the ISO week of the year from x.                | `bigint`      |



### Data types - Date and time


| Data Type                  | Format and Precision                                |
|----------------------------|------------------------------------------------------|
| DATE                       | Calendar date (year, month, day)                     |
| TIME(P)                    | Time of day (hour, minute, second) with P precision  |
| TIME WITH TIME ZONE        | Time of day (hour, minute, second, millisecond) with time zone |
| TIMESTAMP(P)               | Calendar date and time of day without time zone, with P precision |
| TIMESTAMP WITH TIME ZONE(P)| Instant in time with date, time, and time zone, with P precision |
| INTERVAL YEAR TO MONTH     | Span of years and months                             |
| INTERVAL DAY TO SECOND     | Span of days, hours, minutes, seconds, and milliseconds |
