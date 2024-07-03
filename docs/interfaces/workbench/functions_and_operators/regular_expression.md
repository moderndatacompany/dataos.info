# Regular expression functions

All of the regular expression functions use the Java pattern syntax, with a few notable exceptions:

| Feature                                         | Description                                                                                                                                                                        |
|-------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Multi-line mode                                 | Only `\n` is recognized as a line terminator when using multi-line mode (`(?m)` flag). The `(?d)` flag is not supported and should not be used.                                   |
| Case-insensitive matching                      | Case-insensitive matching (`(?i)` flag) is always performed in a Unicode-aware manner. Context-sensitive and local-sensitive matching is not supported. The `(?u)` flag is not supported. |
| Surrogate pairs                                 | Surrogate pairs are not supported. For example, `\uD800\uDC00` must be specified as `\x{10000}`.                                                                                   |
| Boundaries                                      | Boundaries (`\b`) are incorrectly handled for a non-spacing mark without a base character.                                                                                        |
| `\Q` and `\E` in character classes             | `\Q` and `\E` are treated as literals and not supported in character classes (such as `[A-Z123]`).                                                                                  |
| Unicode character classes                      | - Underscores in names must be removed. Example: `OldItalic` instead of `Old_Italic`. <br> - Scripts must be specified directly without prefixes. Example: `Hiragana`.           |
| Blocks                                          | Blocks must be specified with the `In` prefix. Example: `\p{Mongolian}`. The `block=` and `blk=` prefixes are not supported.                                                        |
| Categories                                      | Categories must be specified directly without prefixes. Example: `\p{L}`.                                                                                                         |
| Binary properties                              | Binary properties must be specified directly without prefixes. Example: `\p{NoncharacterCodePoint}`.                                                                              |

### **`regex_count()`**

| Function                   | Description                                                             | Return Value |
| -------------------------- | ----------------------------------------------------------------------- | ------------ |
| `regexp_count(string, pattern) → bigint` | Returns the number of occurrences of `pattern` in `string`.               | bigint       |
Example:
```sql
SELECT regexp_count('1a 2b 14m', '\s*[a-z]+\s*'); -- 3
```

### **`regexp_extract_all`**

| Function                                   | Description                                                                                            | Return Value      |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ----------------- |
| `regexp_extract_all(string, pattern)`      | Returns the substring(s) matched by the regular expression `pattern` in `string`.                       | Array of substrings |
| `regexp_extract_all(string, pattern, group)` | Finds all occurrences of the regular expression `pattern` in `string` and returns the capturing group number. | Array of substrings (group) |

Example:

```sql
SELECT regexp_extract_all('1a 2b 14m', '\d+');
-- [1, 2, 14]

SELECT regexp_extract_all('1a 2b 14m', '(\d+)([a-z]+)', 2); 
-- ['a', 'b', 'm']
```

### **`regexp_extract()`**

| Function                                         | Description                                                                                                   | Return Value      |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------- | ----------------- |
| `regexp_extract(string, pattern)`                | Returns the first substring matched by the regular expression `pattern` in `string`.                         | varchar           |
| `regexp_extract(string, pattern, group)`         | Finds the first occurrence of the regular expression `pattern` in `string` and returns the capturing group number `group`. | varchar           |

Example:
```sql
SELECT regexp_extract('1a 2b 14m', '\d+'); 
-- 1
SELECT regexp_extract('1a 2b 14m', '(\d+)([a-z]+)', 2); 
-- 'a'
```
### **`regexp_like()`**

| Function                            | Description                                                                                              | Return Value |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------- | ------------ |
| `regexp_like(string, pattern)`     | Evaluates the regular expression `pattern` and determines if it is contained within `string`.            | boolean      |

Example:

```sql
SELECT regexp_like('1a 2b 14m', '\d+b'); -- true
```

### **`regexp_position()`**

| Function                                    | Description                                                                                                   | Return Value |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------ |
| `regexp_position(string, pattern)`          | Returns the index of the first occurrence (counting from 1) of `pattern` in `string`. Returns -1 if not found. | integer      |
| `regexp_position(string, pattern, start)`   | Returns the index of the first occurrence of `pattern` in `string`, starting from `start` (inclusive). Returns -1 if not found. | integer      |
| `regexp_position(string, pattern, start, occurrence)` | Returns the index of the nth occurrence of `pattern` in `string`, starting from `start` (inclusive). Returns -1 if not found. | integer      |

Example:

```sql
SELECT regexp_position('I have 23 apples, 5 pears and 13 oranges', '\b\d+\b'); 
-- 8
SELECT regexp_position('I have 23 apples, 5 pears and 13 oranges', '\b\d+\b', 12); 
-- 19
```
### **`regexp_replace()`**

| Function                                       | Description                                                                                                           | Return Value |
| ---------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ------------ |
| `regexp_replace(string, pattern)`              | Removes every instance of the substring matched by the regular expression `pattern` from `string`.                    | varchar      |
| `regexp_replace(string, pattern, replacement)` | Replaces every instance of the substring matched by the regular expression `pattern` in `string` with `replacement`.   | varchar      |
| `regexp_replace(string, pattern, function)`    | Replaces every instance of the substring matched by the regular expression `pattern` in `string` using `function`.    | varchar      |

Example:

```sql
SELECT regexp_replace('1a 2b 14m', '\d+[ab] '); 
-- '14m'
SELECT regexp_replace('1a 2b 14m', '(\d+)([ab]) ', '3c$2 '); 
-- '3ca 3cb 14m'
SELECT regexp_replace('new york', '(\w)(\w*)', x -> upper(x[1]) || lower(x[2])); 
--'New York'
```

### **`regexp_split()`**

| Function                                | Description                                                                                               | Return Value |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------- | ------------ |
| `regexp_split(string, pattern)`         | Splits `string` using the regular expression `pattern` and returns an array. Trailing empty strings are preserved. | Array        |
Example:
```sql
SELECT regexp_split('1a 2b 14m', '\s*[a-z]+\s*'); 
-- [1, 2, 14, ]
```








