# Conversion functions



Minerva allows implicit conversion of numeric and character values to the correct type when possible. However, it does not perform automatic conversions between character and numeric types. For instance, a query expecting a varchar will not automatically convert a bigint value to an equivalent varchar.

Explicit casting to a particular type can be done when necessary.

## Conversion functions

| Function                | Description                                              | Return Type |
|-------------------------|----------------------------------------------------------|-------------|
| `cast(value AS type)`   | Explicitly cast a value as a type. Used for varchar to numeric and vice versa conversions. | `type`      |
| `try_cast(value AS type)`| Similar to `cast()`, but returns null if the cast fails.  | `type`      |


### **`Formatting`**

| Function                     | Description                                              | Return Type |
|------------------------------|----------------------------------------------------------|-------------|
| `format(format, args...)`    | Returns a formatted string using the specified `format string` and arguments. | `varchar`   |
| `format_number(number)`| Returns a formatted string using a unit symbol.                    | `varchar`   |


```sql
-- '123%'
SELECT format('%s%%', 123);

-- '3.14159'
SELECT format('%.5f', pi());

-- '008'
SELECT format('%03d', 8);

-- '1,234,567.89'
SELECT format('%,.2f', 1234567.89);

-- 'hello  ,  world'
SELECT format('%-7s,%7s', 'hello', 'world');

-- 'b c a'
SELECT format('%2$s %3$s %1$s', 'a', 'b', 'c');

-- 'Tuesday, July 4, 2006'
SELECT format('%1$tA, %1$tB %1$te, %1$tY', date '2006-07-04');

```



### **Data size**


The `parse_data_size` function supports the following units:

| Unit  | Description   | Value     |
|------ |---------------|-----------|
| `B`   | Bytes         | 1         |
| `kB`  | Kilobytes     | 1024      |
| `MB`  | Megabytes     | 1024²     |
| `GB`  | Gigabytes     | 1024³     |
| `TB`  | Terabytes     | 1024⁴     |
| `PB`  | Petabytes     | 1024⁵     |
| `EB`  | Exabytes      | 1024⁶     |
| `ZB`  | Zettabytes    | 1024⁷     |
| `YB`  | Yottabytes    | 1024⁸     |




### **`parse_data_size`**

| Function          | Description                                                  |
|-------------------|--------------------------------------------------------------|
| `parse_data_size`   | Parses a `string` of format `value unit` into a number.          |


### **Miscellaneous**


 | Function            | Description                                              | Return Type |
|---------------------|----------------------------------------------------------|-------------|
| `typeof(expr)`    | Returns the name of the type of the provided expression. | `varchar`  |

