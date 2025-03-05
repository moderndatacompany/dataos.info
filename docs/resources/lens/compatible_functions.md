<!-- # Postgres

The following is a list of PostgreSQL functions that have been verified to work when connecting through the Postern service:

| Function                     | Example Syntax                                                      | Description                                         |
|------------------------------|---------------------------------------------------------------------|-----------------------------------------------------|
| `cast`                       | cast(CAST(date as date) AS varchar)                               | Cast a date as varchar                             |
| `date_trunc`                 | DATE_TRUNC('month', abc.start_date)                               | Truncates date to the specified date part (e.g., month) |
| `EXTRACT`                    | EXTRACT(YEAR FROM discover.created_at)                            | Extract a specific part of the date (e.g., year)    |
| `date_part`                  | date_part('week', discover.created_at)                            | Extract a specific part of the date (e.g., week)    |
| `concat (|| works)`          | discover.data_source || discover.column_name                      | Concatenation of two strings works, but text||column doesn't |
| `Mathematical Functions`     | MEASURE(discover.total_discoveries) + MEASURE(discover.unique_columns) | Mathematical operations (e.g., sum)                |
| `char_length`                | char_length(logs.message)                                        | Returns the length of a string (e.g., message length) |
| `substring`                  | substring(logs.message from 2 for 3)                             | Extracts a substring from the string               |
| `left`                       | left(logs.message, 4)                                            | Extracts the left part of a string (e.g., first 4 characters) |
| `length`                     | length(logs.message)                                              | Returns the length of the string                   |
| `right`                      | right(logs.message, 3)                                            | Extracts the right part of a string (e.g., last 3 characters) |
| `Count Distinct`             |                                                                   | Counts the number of distinct values               |


The following is a list of PostgreSQL functions that are not working as expected when connecting through the Postern service:


| Function                          | Example Syntax                                                   | Error Description                                                                                               |
|-----------------------------------|------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| `AGE`                             | `AGE(discover.created_at)`                                       | ERROR:  Error during rewrite: Can't understand the query and it may be not supported yet. Please check logs for additional information. |
| `day add`                         | `discover.created_at+ interval '1' day`                          | ERROR:  External error: Internal error: Data type Timestamp(Nanosecond, None) not supported for scalar operation 'add' on primitive array. |
| `concat`                          | `concat(discover.data_source , '-' ,discover.column_name)`        | ERROR:  Error during rewrite: Can't understand the query and it may be not supported yet. Please check logs for additional information. |
| `lower`                           | `lower(logs.message)`                                            | ERROR:  Error during rewrite: Can't understand the query and it may be not supported yet. Please check logs for additional information. |
| `position`                        | `position('chec' in logs.message)`                               | ERROR:  Error during rewrite: Can't understand the query and it may be not supported yet. Please check logs for additional information. |
| `substring(string from pattern)`  | `substring(logs.message from '..$')`                              | Initial planning error: Error during planning: Coercion from [Utf8, Utf8] to the signature OneOf([Exact([Utf8, Int64]), Exact([LargeUtf8, Int64]), Exact([Utf8, Int64, Int64]), Exact([LargeUtf8, Int64, Int64])]) failed. |
| `substring(string from pattern for escape)` |                                   | ERROR:  Error during rewrite: Can't understand the query and it may be not supported yet. Please check logs for additional information. |
| `trim`                            |                                        | ERROR:  Error during rewrite: Can't understand the query and it may be not supported yet. Please check logs for additional information. |
| `upper`                           | `upper(logs.message)`                                            | ERROR:  Error during rewrite: Can't understand the query and it may be not supported yet. Please check logs for additional information. |
| `concat_ws`                       | `concat_ws(',',logs.message, logs.doc)`                          | ERROR:  Error during rewrite: Can't understand the query and it may be not supported yet. Please check logs for additional information. |
| `initcap`                         | `initcap(logs.message)`                                          | ERROR:  Error during rewrite: Can't understand the query and it may be not supported yet. Please check logs for additional information. |
| `md5`                             | `md5(logs.message)`                                              | ERROR:  Error during rewrite: Can't understand the query and it may be not supported yet. Please check logs for additional information. |
| `regexp_count`                    | `regexp_count(logs.message,'\d',1)`                              | ERROR:  Error during rewrite: Can't understand the query and it may be not supported yet. Please check logs for additional information. |
| `regexp_match`                    | `regexp_match(logs.message,'(check)')`                            | ERROR:  Error during rewrite: Can't understand the query and it may be not supported yet. Please check logs for additional information. |
| `regexp_replace`                  | `regexp_replace(logs.message,'check','abc')`                     | ERROR:  Error during rewrite: Can't understand the query and it may be not supported yet. Please check logs for additional information. |
| `regexp_split_to_array`           | `regexp_split_to_array(logs.message,'\s+')`                      | ERROR:  Error during rewrite: Can't understand the query and it may be not supported yet. Please check logs for additional information. |
| `replace`                         | `replace(logs.message,'check','abc')`                             | ERROR:  Error during rewrite: Can't understand the query and it may be not supported yet. Please check logs for additional information. |
| `reverse`                         | `reverse(logs.message)`                                          | ERROR:  Error during rewrite: Can't understand the query and it may be not supported yet. Please check logs for additional information. |
| `split_part`                      | `split_part(logs.message,'che',1)`                                | ERROR:  Error during rewrite: Can't understand the query and it may be not supported yet. Please check logs for additional information. |
| `starts_with`                     | `starts_with(logs.message,'che')`                                 | ERROR:  Error during rewrite: Can't understand the query and it may be not supported yet. Please check logs for additional information. |
| `substr`                          | `substr(logs.message,2)`                                         | ERROR:  Error during rewrite: Can't understand the query and it may be not supported yet. Please check logs for additional information. |
| `sum`                             |                                        | (Not specified in error description)                                                                   |
| `count`                           |                                        | (Not specified in error description)                                                                   |
| `avg`                             |                                        | (Not specified in error description)                                                                   |
  -->
