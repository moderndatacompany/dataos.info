# String functions and operators


## String operators

| Function      | Description                                        | Return Value |
| ------------- | -------------------------------------------------- | ------------ |
| &#124; &#124;         | Performs concatenation.                            | String       |
| `LIKE`        | Used for pattern matching. See Pattern comparison: LIKE for details. | Boolean      |

> **Note:**  Minerva functions assume valid UTF-8 encoded Unicode input, lacking explicit checks. They process Unicode code points, not user-visible characters. lower() and upper() functions may not handle locale-specific mappings correctly, leading to inaccuracies in languages like Lithuanian, Turkish, and Azeri.


## String Functions

### **`chr()`**

| Function    | Description                                                | Return Value |
| ----------- | ---------------------------------------------------------- | ------------ |
| `chr(n)`    | Returns the Unicode code point `n` as a single character string. | varchar      |

### **`codepoint()`**

| Function         | Description                                                | Return Value |
| ----------------| ---------------------------------------------------------- | ------------ |
| `codepoint(string)` | Returns the Unicode code point of the only character of `string`. | integer      |

### **`format()`**

| Function                  | Description                                                                                        | Return Value |
| ------------------------- | -------------------------------------------------------------------------------------------------- | ------------ |
| `format(format, args...)` | Returns a formatted string using the specified format string and arguments.                       | varchar      |

### **`distance()`**

| Function                              | Description                                                                                      | Return Value |
| ------------------------------------- | ------------------------------------------------------------------------------------------------ | ------------ |
| `hamming_distance(string1, string2)` | Returns the Hamming distance of `string1` and `string2`, i.e., the number of differing positions. Strings must have the same length. | bigint       |
| `levenshtein_distance(string1, string2)` | Returns the Levenshtein edit distance of `string1` and `string2`, i.e., the minimum number of single-character edits needed to transform one string into the other. | bigint       |

### **`length()`**

| Function            | Description                                 | Return Value |
| ------------------- | ------------------------------------------- | ------------ |
| `length(string)`    | Returns the length of `string` in characters. | bigint       |

### **`lower()`**

| Function          | Description                         | Return Value |
| ----------------- | ----------------------------------- | ------------ |
| `lower(string)`   | Converts `string` to lowercase.     | varchar      |

### **`lpad()`**

| Function                    | Description                                                                                             | Return Value |
| --------------------------- | ------------------------------------------------------------------------------------------------------- | ------------ |
| `lpad(string, size, padstring)` | Left pads `string` to `size` characters with `padstring`. If `size` is less than the length of `string`, the result is truncated to `size` characters. `size` must not be negative and `padstring` must be non-empty. | varchar      |

### **`ltrim()`**

| Function        | Description                                 | Return Value |
| --------------- | ------------------------------------------- | ------------ |
| `ltrim(string)` | Removes leading whitespace from `string`.   | varchar      |

### **`luhn_check()`**

| Function                  | Description                                                                                                                                                         | Return Value |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| `luhn_check(string)`      | Tests whether a string of digits is valid according to the Luhn algorithm. This checksum function, also known as modulo 10 or mod 10, distinguishes valid numbers from mistyped or incorrect ones, often used in credit card numbers. | boolean      |

Example:

Valid identification number:
```sql
select luhn_check('79927398713');
-- true
```
Invalid identification number:
```sql
select luhn_check('79927398714');
-- false
```

### **`position()`**

| Function                            | Description                                                                        | Return Value |
| ----------------------------------- | ---------------------------------------------------------------------------------- | ------------ |
| `position(substring IN string)`    | Returns the starting position of the first instance of `substring` in `string`. Positions start with 1. If not found, 0 is returned. | bigint       |

### **`strpos()`**

| Function                               | Description                                                                                                 | Return Value |
| -------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ------------ |
| `strpos(string, substring)`            | Returns the starting position of the first instance of `substring` in `string`. Positions start with 1. If not found, 0 is returned. | bigint       |
| `strpos(string, substring, instance)` | Returns the position of the N-th instance of `substring` in `string`. When `instance` is negative, the search starts from the end of `string`. Positions start with 1. If not found, 0 is returned. | bigint       |

### **`replace()`**

| Function                             | Description                                                                                        | Return Value |
| ------------------------------------ | -------------------------------------------------------------------------------------------------- | ------------ |
| `replace(string, search)`            | Removes all instances of `search` from `string`.                                                  | varchar      |
| `replace(string, search, replace)`   | Replaces all instances of `search` with `replace` in `string`.                                    | varchar      |


### **`reverse()`**

| Function            | Description                                    | Return Value |
| ------------------- | ---------------------------------------------- | ------------ |
| `reverse(string)`   | Returns `string` with the characters in reverse order. | varchar      |

### **`rpad()`**

| Function                    | Description                                                                                              | Return Value |
| --------------------------- | -------------------------------------------------------------------------------------------------------- | ------------ |
| `rpad(string, size, padstring)` | Right pads `string` to `size` characters with `padstring`. If `size` is less than the length of `string`, the result is truncated to `size` characters. `size` must not be negative and `padstring` must be non-empty. | varchar      |

### **`rtrim()`**

| Function          | Description                                        | Return Value |
| ----------------- | -------------------------------------------------- | ------------ |
| `rtrim(string)`   | Removes trailing whitespace from `string`.        | varchar      |

### **`soundex()`**

| Function            | Description                                                                                                      | Return Value |
| ------------------- | ---------------------------------------------------------------------------------------------------------------- | ------------ |
| `soundex(char)`     | Returns a character string containing the phonetic representation of `char`.                                     | string       |

Example:

```sql
SELECT name
FROM nation
WHERE SOUNDEX(name)  = SOUNDEX('CHYNA');

 name  |
-------+----
 CHINA |
(1 row)
```

### **`split()`**

| Function                            | Description                                                                                                        | Return Value |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ------------ |
| `split(string, delimiter, limit)`  | Splits `string` on `delimiter` and returns an array of size at most `limit`. The last element contains everything left in the string. `limit` must be a positive number. | array        |
| `split_part(string, delimiter, index)` | Splits `string` on `delimiter` and returns the field at `index`. Field indexes start with 1. If the index is larger than the number of fields, then null is returned. | varchar      |
| `split_to_map(string, entryDelimiter, keyValueDelimiter)` | Splits `string` by `entryDelimiter` and `keyValueDelimiter` and returns a map. `entryDelimiter` splits string into key-value pairs. `keyValueDelimiter` splits each pair into key and value. | map<varchar, varchar> |
| `split_to_multimap(string, entryDelimiter, keyValueDelimiter)` | Splits `string` by `entryDelimiter` and `keyValueDelimiter` and returns a map containing an array of values for each unique key. `entryDelimiter` splits string into key-value pairs. `keyValueDelimiter` splits each pair into key and value. The values for each key will be in the same order as they appeared in string. | map<varchar, array<varchar>> |

### **`starts_with()`**

| Function                            | Description                                              | Return Value |
| ----------------------------------- | -------------------------------------------------------- | ------------ |
| `starts_with(string, substring)`   | Tests whether `substring` is a prefix of `string`.       | boolean      |

### **`substring()`**

| Function                                   | Description                                                                                     | Return Value |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------- | ------------ |
| `substr(string, start)`                    | This is an alias for `substring()`.                                                             | varchar      |
| `substring(string, start)`                 | Returns the rest of `string` from the starting position `start`. Positions start with 1. A negative starting position is interpreted as being relative to the end of the string. | varchar      |
| `substr(string, start, length)`            | This is an alias for `substring()`.                                                             | varchar      |
| `substring(string, start, length)`         | Returns a substring from `string` of length `length` from the starting position `start`. Positions start with 1. A negative starting position is interpreted as being relative to the end of the string. | varchar      |
        
### **`translate()`**

| Function                             | Description                                                                                                        | Return Value |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------ |
| `translate(source, from, to)`       | Returns the `source` string translated by replacing characters found in the `from` string with the corresponding characters in the `to` string. If the `from` string contains duplicates, only the first is used. If the source character does not exist in the `from` string, the source character will be copied without translation. If the index of the matching character in the `from` string is beyond the length of the `to` string, the source character will be omitted from the resulting string. | varchar      |

Example:

```sql
SELECT translate('Palhoça', 'ç','c'); -- 'Palhoca'
SELECT translate('abcd', 'b', U&'\+01F600'); -- a😀cd
SELECT translate('abcd', 'a', ''); -- 'bcd'
```
### **`trim()`**

| Function                              | Description                                                                                             | Return Value |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------ |
| `trim(string)`                        | Removes leading and trailing whitespace from `string`.                                                   | varchar      |
| `trim([ [ specification ] [ string ] FROM ] source)` | Removes any leading and/or trailing characters as specified up to and including `string` from `source`. | varchar      |

Example:

``` sql
SELECT trim('!' FROM '!foo!'); -- 'foo'
SELECT trim(LEADING FROM '  abcd');  -- 'abcd'
SELECT trim(BOTH '$' FROM '$var$'); -- 'var'
SELECT trim(TRAILING 'ER' FROM upper('worker')); -- 'WORK'
```
### **`upper()`**

| Function          | Description                            | Return Value |
| ----------------- | -------------------------------------- | ------------ |
| `upper(string)`   | Converts `string` to uppercase.        | varchar      |

### **`word_stem()`**

| Function                      | Description                                                             | Return Value |
| ----------------------------- | ----------------------------------------------------------------------- | ------------ |
| `word_stem(word)`             | Returns the stem of `word` in the English language.                     | varchar      |
| `word_stem(word, lang)`       | Returns the stem of `word` in the specified language (`lang`).          | varchar      |


## Unicode functions

### **`normalize()`**

| Function                      | Description                                                             | Return Value |
| ----------------------------- | ----------------------------------------------------------------------- | ------------ |
| `normalize(string)`           | Transforms `string` with NFC normalization form.                        | varchar      |
| `normalize(string, form)`     | Transforms `string` with the specified normalization form. `form` must be one of the following keywords: | varchar      |

`form` must be one of the following keywords:

| Form  | Description                              |
| ----- | ---------------------------------------- |
| `NFD`  | Canonical Decomposition                   |
| `NFC` | Canonical Decomposition, followed by Canonical Composition |
| `NFKD` | Compatibility Decomposition              |
| `NFKC` | Compatibility Decomposition, followed by Canonical Composition |


> **Note:** This SQL-standard function has special syntax and requires specifying `form` as a keyword, not as a string.

### **`utf8()`**

| Function                        | Description                                                                                     | Return Type |
| ------------------------------- | ----------------------------------------------------------------------------------------------- | ----------- |
| `to_utf8(string) → varbinary`   | Encodes `string` into a UTF-8 varbinary representation.                                         | varbinary   |
| `from_utf8(binary) → varchar`   | Decodes a UTF-8 encoded string from binary. Invalid UTF-8 sequences are replaced with the Unicode replacement character U+FFFD. | varchar     |
| `from_utf8(binary, replace) → varchar` | Decodes a UTF-8 encoded string from binary. Invalid UTF-8 sequences are replaced with `replace`. The replacement string `replace` must either be a single character or empty (in which case invalid characters are removed). | varchar     |









