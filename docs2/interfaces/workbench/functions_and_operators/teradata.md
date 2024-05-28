# Teradata functions
These functions provide compatibility with Teradata SQL.

## String functions

### **`char2hexint()`**

| Function             | Description                                                                                     | Return Type |
| -------------------- | ----------------------------------------------------------------------------------------------- | ----------- |
| `char2hexint(string)` | Returns the hexadecimal representation of the UTF-16BE encoding of the string.                 | `varchar`   |

### **`index()`**

| Function          | Description                                                                         | Return Type |
| ----------------- | ----------------------------------------------------------------------------------- | ----------- |
| `index(string, substring)` | Alias for the `strpos()` function.                                                   | `bigint`    |

> **Note:** Alias for strpos() function.

## Date functions

| Specifier | Description                        |
|-----------|------------------------------------|
| / , . ; : | Punctuation characters are ignored|
| dd        | Day of month (1-31)                |
| hh        | Hour of day (1-12)                 |
| hh24      | Hour of the day (0-23)             |
| mi        | Minute (0-59)                      |
| mm        | Month (01-12)                      |
| ss        | Second (0-59)                      |
| yyyy      | 4-digit year                       |
| yy        | 2-digit year                       |

> **Warning:**  Case insensitivity is not currently supported. All specifiers must be lowercase.

### **`to_char()`**

| Function                      | Description                                             | Return Type |
| ----------------------------- | ------------------------------------------------------- | ----------- |
| `to_char(timestamp, format)`  | Formats timestamp as a string using format.             | `varchar`   |

### **`to_timestamp()`**

| Function                           | Description                                        | Return Type |
| ---------------------------------- | -------------------------------------------------- | ----------- |
| `to_timestamp(string, format)`     | Parses string into a TIMESTAMP using format.       | `timestamp` |

### **`to_date()`**

| Function                     | Description                                   | Return Type |
| ---------------------------- | --------------------------------------------- | ----------- |
| `to_date(string, format)`    | Parses string into a DATE using format.       | `date`      |

