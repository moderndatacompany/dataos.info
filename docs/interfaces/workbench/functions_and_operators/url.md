# URL functions

## Extraction functions

The URL extraction functions extract components from HTTP URLs (or any valid URIs conforming to RFC 2396). The following syntax is supported:
```sql
[protocol:][//host[:port]][path][?query][#fragment]
```
> **Note:** The extracted components do not contain URI syntax separators such as : or ?.

### **`url_extract_fragment()`**

| Function                      | Description                                                                                     | Return Type |
| ----------------------------- | ----------------------------------------------------------------------------------------------- | ----------- |
| `url_extract_fragment(url)`   | Returns the fragment identifier from url.                                                      | `varchar`   |

### **`url_extract_host()`**

| Function                    | Description                                                           | Return Type |
| --------------------------- | --------------------------------------------------------------------- | ----------- |
| `url_extract_host(url)`     | Returns the host from url.                                           | `varchar`   |

### **`url_extract_parameter()`**

| Function                           | Description                                                                                        | Return Type |
| ---------------------------------- | -------------------------------------------------------------------------------------------------- | ----------- |
| `url_extract_parameter(url, name)` | Returns the value of the first query string parameter named name from url.                          | `varchar`   |

### **`url_extract_path()`**

| Function                     | Description                                                              | Return Type |
| ---------------------------- | ------------------------------------------------------------------------ | ----------- |
| `url_extract_path(url)`      | Returns the path from url.                                               | `varchar`   |

### **`url_extract_port()`**

| Function                      | Description                                                      | Return Type |
| ----------------------------- | ---------------------------------------------------------------- | ----------- |
| `url_extract_port(url)`       | Returns the port number from url.                                | `bigint`    |

### **`url_extract_protocol()`**

| Function                         | Description                                                   | Return Type |
| -------------------------------- | ------------------------------------------------------------- | ----------- |
| `url_extract_protocol(url)`      | Returns the protocol from URL.                                 | `varchar`   |

Example:
```sql
SELECT url_extract_protocol('https://127.0.0.1:8080/req_path');
-- https

SELECT url_extract_protocol('ftp://path/file');
-- ftp
```
### **`url_extract_query()`**
| Function                   | Description                                 | Return Type |
| -------------------------- | ------------------------------------------- | ----------- |
| `url_extract_query(url)`   | Returns the query string from URL.          | `varchar`   |


## Encoding funtions

### **`url_encode()`**

| Function                   | Description                                                         | Return Type |
| -------------------------- | ------------------------------------------------------------------- | ----------- |
| `url_encode(value)`        | Escapes value by encoding it for safe inclusion in URL parameters.  | `varchar`   |



| Rule                          | Description                                                                                   |
|-------------------------------|-----------------------------------------------------------------------------------------------|
| Alphanumeric characters      | Not encoded                                                                                   |
| ., -, *, and _               | Not encoded                                                                                   |
| ASCII space character        | Encoded as +                                                                                  |
| All other characters         | Converted to UTF-8 and encoded as %XX, where XX is the uppercase hexadecimal value of byte |



### **`url_decode()`**

| Function                | Description                                                              | Return Type |
| ----------------------- | ------------------------------------------------------------------------ | ----------- |
| `url_decode(value)`     | Unescapes the URL encoded `value`. This function is the inverse of `url_encode()`. | `varchar`   |

