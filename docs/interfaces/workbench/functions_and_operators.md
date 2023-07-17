# Functions and Operators - DataOS

| Function | Return Type | Argument Types | Function Type | Deterministic | Description | Date |
| --- | --- | --- | --- | --- | --- | --- |
| A |  |  |  | 0 |  |  |
| abs | bigint | bigint | scalar | 1 | Absolute value |  |
| abs | decimal(p,s) | decimal(p,s) | scalar | 1 | Absolute value |  |
| abs | double | double | scalar | 1 | Absolute value |  |
| abs | integer | integer | scalar | 1 | Absolute value |  |
| abs | real | real | scalar | 1 | Absolute value |  |
| abs | smallint | smallint | scalar | 1 | Absolute value |  |
| abs | tinyint | tinyint | scalar | 1 | Absolute value |  |
| acos | double | double | scalar | 1 | Arc cosine |  |
| all_match | boolean | array(t), function(t,boolean) | scalar | 1 | Returns true if all elements of the array match the given predicate |  |
| any_match | boolean | array(t), function(t,boolean) | scalar | 1 | Returns true if the array contains one or more elements that match the given predicate |  |
| approx_distinct | bigint | boolean | aggregate | 1 |  |  |
| approx_distinct | bigint | boolean, double | aggregate | 1 |  |  |
| approx_distinct | bigint | t | aggregate | 1 |  |  |
| approx_distinct | bigint | t, double | aggregate | 1 |  |  |
| approx_distinct | bigint | unknown | aggregate | 1 |  |  |
| approx_distinct | bigint | unknown, double | aggregate | 1 |  |  |
| approx_most_frequent | map(bigint,bigint) | bigint, bigint, bigint | aggregate | 1 |  |  |
| approx_most_frequent | map(varchar,bigint) | bigint, varchar, bigint | aggregate | 1 |  |  |
| approx_percentile | array(bigint) | bigint, array(double) | aggregate | 1 |  |  |
| approx_percentile | array(bigint) | bigint, double, array(double) | aggregate | 1 |  |  |
| approx_percentile | array(double) | double, array(double) | aggregate | 1 |  |  |
| approx_percentile | array(double) | double, double, array(double) | aggregate | 1 |  |  |
| approx_percentile | array(real) | real, array(double) | aggregate | 1 |  |  |
| approx_percentile | array(real) | real, double, array(double) | aggregate | 1 |  |  |
| approx_percentile | bigint | bigint, double | aggregate | 1 |  |  |
| approx_percentile | bigint | bigint, double, double | aggregate | 1 |  |  |
| approx_percentile | bigint | bigint, double, double, double | aggregate | 1 |  |  |
| approx_percentile | double | double, double | aggregate | 1 |  |  |
| approx_percentile | double | double, double, double | aggregate | 1 |  |  |
| approx_percentile | double | double, double, double, double | aggregate | 1 |  |  |
| approx_percentile | real | real, double | aggregate | 1 |  |  |
| approx_percentile | real | real, double, double | aggregate | 1 |  |  |
| approx_percentile | real | real, double, double, double | aggregate | 1 |  |  |
| approx_set | hyperloglog | bigint | aggregate | 1 |  |  |
| approx_set | hyperloglog | double | aggregate | 1 |  |  |
| approx_set | hyperloglog | varchar(x) | aggregate | 1 |  |  |
| arbitrary | T | T | aggregate | 1 | Return an arbitrary non-null input value |  |
| array_agg | array(T) | T | aggregate | 1 | return an array of values |  |
| array_distinct | array(e) | array(e) | scalar | 1 | Remove duplicate values from the given array |  |
| array_except | array(e) | array(e), array(e) | scalar | 1 | Returns an array of elements that are in the first array but not the second, without duplicates. |  |
| array_intersect | array(e) | array(e), array(e) | scalar | 1 | Intersects elements of the two given arrays |  |
| array_join | varchar | array(T), varchar | scalar | 1 | Concatenates the elements of the given array using a delimiter and an optional string to replace nulls |  |
| array_join | varchar | array(T), varchar, varchar | scalar | 1 | Concatenates the elements of the given array using a delimiter and an optional string to replace nulls |  |
| array_max | t | array(t) | scalar | 1 | Get maximum value of array |  |
| array_min | t | array(t) | scalar | 1 | Get minimum value of array |  |
| array_position | bigint | array(t), t | scalar | 1 | Returns the position of the first occurrence of the given value in array (or 0 if not found) |  |
| array_remove | array(e) | array(e), e | scalar | 1 | Remove specified values from the given array |  |
| array_sort | array(e) | array(e) | scalar | 1 | Sorts the given array in ascending order according to the natural ordering of its elements. |  |
| array_sort | array(t) | array(t), function(t,t,integer) | scalar | 1 | Sorts the given array with a lambda comparator. |  |
| array_union | array(e) | array(e), array(e) | scalar | 1 | Union elements of the two given arrays |  |
| arrays_overlap | boolean | array(e), array(e) | scalar | 1 | Returns true if arrays have common elements |  |
| asin | double | double | scalar | 1 | Arc sine |  |
| at_timezone | timestamp(p) with time zone | timestamp(p) with time zone, varchar(x) | scalar | 1 |  |  |
| atan | double | double | scalar | 1 | Arc tangent |  |
| atan2 | double | double, double | scalar | 1 | Arc tangent of given fraction |  |
| avg | decimal(p,s) | decimal(p,s) | aggregate | 1 | Calculates the average value |  |
| avg | double | bigint | aggregate | 1 |  |  |
| avg | double | double | aggregate | 1 |  |  |
| avg | interval day to second | interval day to second | aggregate | 1 |  |  |
| avg | interval year to month | interval year to month | aggregate | 1 |  |  |
| avg | real | real | aggregate | 1 | Returns the average value of the argument |  |
| B |  |  |  | 0 |  |  |
| bar | varchar | double, bigint | scalar | 1 |  |  |
| bar | varchar | double, bigint, color, color | scalar | 1 |  |  |
| beta_cdf | double | double, double, double | scalar | 1 | Beta cdf given the a, b parameters and value |  |
| bin | varchar | bigint | scalar | 1 | Converts decimal number to binary |  |
| bing_tile | bingtile | integer, integer, integer | scalar | 1 | Creates a Bing tile from XY coordinates and zoom level |  |
| bing_tile | bingtile | varchar | scalar | 1 | Creates a Bing tile from a QuadKey |  |
| bing_tile_at | bingtile | double, double, integer | scalar | 1 | Given a (latitude, longitude) point, returns the containing Bing tile at the specified zoom level |  |
| bing_tile_coordinates | row(“x” integer,“y” integer) | bingtile | scalar | 1 | Given a Bing tile, returns XY coordinates of the tile |  |
| bing_tile_polygon | geometry | bingtile | scalar | 1 | Given a Bing tile, returns the polygon representation of the tile |  |
| bing_tile_quadkey | varchar | bingtile | scalar | 1 | Given a Bing tile, returns its QuadKey |  |
| bing_tile_zoom_level | tinyint | bingtile | scalar | 1 | Given a Bing tile, returns zoom level of the tile |  |
| bing_tiles_around | array(bingtile) | double, double, integer | scalar | 1 | Given a (longitude, latitude) point, returns the surrounding Bing tiles at the specified zoom level |  |
| bing_tiles_around | array(bingtile) | double, double, integer, double | scalar | 1 | Given a (latitude, longitude) point, a radius in kilometers and a zoom level, returns a minimum set of Bing tiles at specified zoom level that cover a circle of specified radius around the specified point. |  |
| bit_count | bigint | bigint, bigint | scalar | 1 | Count number of set bits in 2’s complement representation |  |
| bitwise_and | bigint | bigint, bigint | scalar | 1 | Bitwise AND in 2’s complement arithmetic |  |
| bitwise_and_agg | bigint | bigint | aggregate | 1 |  |  |
| bitwise_left_shift | bigint | bigint, integer | scalar | 1 | bitwise left shift |  |
| bitwise_left_shift | integer | integer, integer | scalar | 1 | bitwise left shift |  |
| bitwise_left_shift | smallint | smallint, integer | scalar | 1 | bitwise left shift |  |
| bitwise_left_shift | tinyint | tinyint, integer | scalar | 1 | bitwise left shift |  |
| bitwise_not | bigint | bigint | scalar | 1 | Bitwise NOT in 2’s complement arithmetic |  |
| bitwise_or | bigint | bigint, bigint | scalar | 1 | Bitwise OR in 2’s complement arithmetic |  |
| bitwise_or_agg | bigint | bigint | aggregate | 1 |  |  |
| bitwise_right_shift | bigint | bigint, integer | scalar | 1 | bitwise logical right shift |  |
| bitwise_right_shift | integer | integer, integer | scalar | 1 | bitwise logical right shift |  |
| bitwise_right_shift | smallint | smallint, integer | scalar | 1 | bitwise logical right shift |  |
| bitwise_right_shift | tinyint | tinyint, integer | scalar | 1 | bitwise logical right shift |  |
| bitwise_right_shift_arithmetic | bigint | bigint, integer | scalar | 1 | bitwise arithmetic right shift |  |
| bitwise_right_shift_arithmetic | integer | integer, integer | scalar | 1 | bitwise arithmetic right shift |  |
| bitwise_right_shift_arithmetic | smallint | smallint, integer | scalar | 1 | bitwise arithmetic right shift |  |
| bitwise_right_shift_arithmetic | tinyint | tinyint, integer | scalar | 1 | bitwise arithmetic right shift |  |
| bitwise_xor | bigint | bigint, bigint | scalar | 1 | Bitwise XOR in 2’s complement arithmetic |  |
| bool_and | boolean | boolean | aggregate | 1 |  |  |
| bool_or | boolean | boolean | aggregate | 1 |  |  |
| C |  |  |  | 0 |  |  |
| cardinality | bigint | array(e) | scalar | 1 | Returns the cardinality (length) of the array |  |
| cardinality | bigint | hyperloglog | scalar | 1 | Compute the cardinality of a HyperLogLog instance |  |
| cardinality | bigint | map(k,v) | scalar | 1 | Returns the cardinality (the number of key-value pairs) of the map |  |
| cardinality | bigint | setdigest | scalar | 1 |  |  |
| cbrt | double | double | scalar | 1 | Cube root |  |
| ceil | bigint | bigint | scalar | 1 | Round up to nearest integer |  |
| ceil | decimal(rp,0) | decimal(p,s) | scalar | 1 | Round up to nearest integer |  |
| ceil | double | double | scalar | 1 | Round up to nearest integer |  |
| ceil | integer | integer | scalar | 1 | Round up to nearest integer |  |
| ceil | real | real | scalar | 1 | Round up to nearest integer |  |
| ceil | smallint | smallint | scalar | 1 | Round up to nearest integer |  |
| ceil | tinyint | tinyint | scalar | 1 | Round up to nearest integer |  |
| ceiling | bigint | bigint | scalar | 1 | Round up to nearest integer |  |
| ceiling | decimal(rp,0) | decimal(p,s) | scalar | 1 | Round up to nearest integer |  |
| ceiling | double | double | scalar | 1 | Round up to nearest integer |  |
| ceiling | integer | integer | scalar | 1 | Round up to nearest integer |  |
| ceiling | real | real | scalar | 1 | Round up to nearest integer |  |
| ceiling | smallint | smallint | scalar | 1 | Round up to nearest integer |  |
| ceiling | tinyint | tinyint | scalar | 1 | Round up to nearest integer |  |
| char2hexint | varchar | varchar | scalar | 1 | Returns the hexadecimal representation of the UTF-16BE encoding of the argument |  |
| checksum | varbinary | T | aggregate | 1 | Checksum of the given values |  |
| chr | varchar(1) | bigint | scalar | 1 | Convert Unicode code point to a string |  |
| classify | bigint | map(bigint,double), classifier(bigint) | scalar | 1 |  |  |
| classify | varchar | map(bigint,double), classifier(varchar) | scalar | 1 |  |  |
| codepoint | integer | varchar(1) | scalar | 1 | Returns Unicode code point of a single character string |  |
| color | color | double, color, color | scalar | 1 |  |  |
| color | color | double, double, double, color, color | scalar | 1 |  |  |
| color | color | varchar(x) | scalar | 1 |  |  |
| combinations | array(array(t)) | array(t), integer | scalar | 1 | Return n-element subsets from array |  |
| concat | array(E) | E, array(E) | scalar | 1 | Concatenates an element to an array |  |
| concat | array(E) | array(E) | scalar | 1 | Concatenates given arrays |  |
| concat | array(E) | array(E), E | scalar | 1 | Concatenates an array to an element |  |
| concat | char(u) | char(x), char(y) | scalar | 1 | Concatenates given character strings |  |
| concat | varbinary | varbinary | scalar | 1 | concatenates given varbinary values |  |
| concat | varchar | varchar | scalar | 1 | Concatenates given strings |  |
| concat_ws | varchar | varchar, array(varchar) | scalar | 1 |  |  |
| concat_ws | varchar | varchar, varchar | scalar | 1 | Concatenates elements using separator |  |
| contains | boolean | array(t), t | scalar | 1 | Determines whether given value exists in the array |  |
| contains | boolean | varchar, ipaddress | scalar | 1 | Determines whether given IP address exists in the CIDR |  |
| contains_sequence | boolean | array(t), array(t) | scalar | 1 | Determines whether an array contains a sequence, with the values in the exact order |  |
| convex_hull_agg | geometry | geometry | aggregate | 1 | Returns a geometry that is the convex hull of all the geometries in the set. |  |
| corr | double | double, double | aggregate | 1 |  |  |
| corr | real | real, real | aggregate | 1 |  |  |
| cos | double | double | scalar | 1 | Cosine |  |
| cosh | double | double | scalar | 1 | Hyperbolic cosine |  |
| cosine_similarity | double | map(varchar,double), map(varchar,double) | scalar | 1 | Cosine similarity between the given sparse vectors |  |
| count | bigint |  | aggregate | 1 |  |  |
| count | bigint | T | aggregate | 1 | Counts the non-null values |  |
| count_if | bigint | boolean | aggregate | 1 |  |  |
| covar_pop | double | double, double | aggregate | 1 |  |  |
| covar_pop | real | real, real | aggregate | 1 |  |  |
| covar_samp | double | double, double | aggregate | 1 |  |  |
| covar_samp | real | real, real | aggregate | 1 |  |  |
| crc32 | bigint | varbinary | scalar | 1 | Compute CRC-32 |  |
| cume_dist | double |  | window | 1 |  |  |
| current_date | date |  | scalar | 1 | Current date |  |
| current_groups | array(varchar) |  | scalar | 1 | Current groups of current user |  |
| current_timezone | varchar |  | scalar | 1 | Current time zone |  |
| D |  |  |  | 0 |  |  |
| date | date | timestamp(p) | scalar | 1 |  |  |
| date | date | timestamp(p) with time zone | scalar | 1 |  |  |
| date | date | varchar(x) | scalar | 1 |  |  |
| date_add | date | varchar(x), bigint, date | scalar | 1 | Add the specified amount of date to the given date |  |
| date_add | time(p) | varchar(x), bigint, time(p) | scalar | 1 | Add the specified amount of time to the given time |  |
| date_add | time(p) with time zone | varchar(x), bigint, time(p) with time zone | scalar | 1 | Add the specified amount of time to the given time |  |
| date_add | timestamp(p) | varchar(x), bigint, timestamp(p) | scalar | 1 | Add the specified amount of time to the given timestamp |  |
| date_add | timestamp(p) with time zone | varchar(x), bigint, timestamp(p) with time zone | scalar | 1 | Add the specified amount of time to the given timestamp |  |
| date_add | varchar | date, bigint | scalar | 1 | Add number of days to the given date |  |
| date_add | varchar | varchar, bigint | scalar | 1 | Add number of days to the given string date |  |
| date_diff | bigint | varchar(x), date, date | scalar | 1 | Difference of the given dates in the given unit |  |
| date_diff | bigint | varchar(x), time(p) with time zone, time(p) with time zone | scalar | 1 | Difference of the given times in the given unit |  |
| date_diff | bigint | varchar(x), time(p), time(p) | scalar | 1 | Difference of the given times in the given unit |  |
| date_diff | bigint | varchar(x), timestamp(p) with time zone, timestamp(p) with time zone | scalar | 1 | Difference of the given times in the given unit |  |
| date_diff | bigint | varchar(x), timestamp(p), timestamp(p) | scalar | 1 | Difference of the given times in the given unit |  |
| date_format | varchar | timestamp(p) with time zone, varchar(x) | scalar | 1 | Formats the given timestamp by the given format |  |
| date_format | varchar | timestamp(p), varchar(x) | scalar | 1 | Formats the given timestamp by the given format |  |
| date_parse | timestamp(3) | varchar(x), varchar(y) | scalar | 1 |  |  |
| date_sub | varchar | date, bigint | scalar | 1 | Subtract number of days to the given date |  |
| date_sub | varchar | varchar, bigint | scalar | 1 | Subtract number of days to the given string date |  |
| date_trunc | date | varchar(x), date | scalar | 1 | Truncate to the specified precision in the session timezone |  |
| date_trunc | time(p) | varchar(x), time(p) | scalar | 1 | Truncate to the specified precision |  |
| date_trunc | time(p) with time zone | varchar(x), time(p) with time zone | scalar | 1 | Truncate to the specified precision |  |
| date_trunc | timestamp(p) | varchar(x), timestamp(p) | scalar | 1 | Truncate to the specified precision in the session timezone |  |
| date_trunc | timestamp(p) with time zone | varchar(x), timestamp(p) with time zone | scalar | 1 | Truncate to the specified precision |  |
| datediff | bigint | date, date | scalar | 1 | difference of the given dates in days |  |
| datediff | bigint | timestamp with time zone, timestamp with time zone | scalar | 1 | difference of the given dates (Timestamps) in days |  |
| datediff | bigint | timestamp, timestamp | scalar | 1 | difference of the given dates (Timestamps) in days |  |
| datediff | bigint | varchar, varchar | scalar | 1 | difference of the given dates (String) in days |  |
| day | bigint | date | scalar | 1 | Day of the month of the given date |  |
| day | bigint | interval day to second | scalar | 1 | Day of the month of the given interval |  |
| day | bigint | timestamp(p) | scalar | 1 | Day of the month of the given timestamp |  |
| day | bigint | timestamp(p) with time zone | scalar | 1 | Day of the month of the given timestamp |  |
| day | bigint | varchar | scalar | 1 | day of the year of the given string timestamp |  |
| day_of_month | bigint | date | scalar | 1 | Day of the month of the given date |  |
| day_of_month | bigint | interval day to second | scalar | 1 | Day of the month of the given interval |  |
| day_of_month | bigint | timestamp(p) | scalar | 1 | Day of the month of the given timestamp |  |
| day_of_month | bigint | timestamp(p) with time zone | scalar | 1 | Day of the month of the given timestamp |  |
| day_of_week | bigint | date | scalar | 1 | Day of the week of the given date |  |
| day_of_week | bigint | timestamp(p) | scalar | 1 | Day of the week of the given timestamp |  |
| day_of_week | bigint | timestamp(p) with time zone | scalar | 1 | Day of the week of the given timestamp |  |
| day_of_year | bigint | date | scalar | 1 | Day of the year of the given date |  |
| day_of_year | bigint | timestamp(p) | scalar | 1 | Day of the year of the given timestamp |  |
| day_of_year | bigint | timestamp(p) with time zone | scalar | 1 | Day of the year of the given timestamp |  |
| dayofmonth | bigint | varchar | scalar | 1 | day of the year of the given string timestamp |  |
| degrees | double | double | scalar | 1 | Converts an angle in radians to degrees |  |
| dense_rank | bigint |  | window | 1 |  |  |
| dow | bigint | date | scalar | 1 | Day of the week of the given date |  |
| dow | bigint | timestamp(p) | scalar | 1 | Day of the week of the given timestamp |  |
| dow | bigint | timestamp(p) with time zone | scalar | 1 | Day of the week of the given timestamp |  |
| doy | bigint | date | scalar | 1 | Day of the year of the given date |  |
| doy | bigint | timestamp(p) | scalar | 1 | Day of the year of the given timestamp |  |
| doy | bigint | timestamp(p) with time zone | scalar | 1 | Day of the year of the given timestamp |  |
| E |  |  |  | 0 |  |  |
| e | double |  | scalar | 1 | Euler’s number |  |
| element_at | V | map(K,V), K | scalar | 1 | Get value for the given key, or null if it does not exist |  |
| element_at | e | array(e), bigint | scalar | 1 | Get element of array at given index |  |
| empty_approx_set | hyperloglog |  | scalar | 1 | An empty HyperLogLog instance |  |
| evaluate_classifier_predictions | varchar | bigint, bigint | aggregate | 1 |  |  |
| evaluate_classifier_predictions | varchar | varchar(x), varchar(y) | aggregate | 1 |  |  |
| every | boolean | boolean | aggregate | 1 |  |  |
| exp | double | double | scalar | 1 | Euler’s number raised to the given power |  |
| F |  |  |  | 0 |  |  |
| features | map(bigint,double) | double | scalar | 1 |  |  |
| features | map(bigint,double) | double, double | scalar | 1 |  |  |
| features | map(bigint,double) | double, double, double | scalar | 1 |  |  |
| features | map(bigint,double) | double, double, double, double | scalar | 1 |  |  |
| features | map(bigint,double) | double, double, double, double, double | scalar | 1 |  |  |
| features | map(bigint,double) | double, double, double, double, double, double | scalar | 1 |  |  |
| features | map(bigint,double) | double, double, double, double, double, double, double | scalar | 1 |  |  |
| features | map(bigint,double) | double, double, double, double, double, double, double, double | scalar | 1 |  |  |
| features | map(bigint,double) | double, double, double, double, double, double, double, double, double | scalar | 1 |  |  |
| features | map(bigint,double) | double, double, double, double, double, double, double, double, double, double | scalar | 1 |  |  |
| filter | array(t) | array(t), function(t,boolean) | scalar | 0 | Return array containing elements that match the given predicate |  |
| find_in_set | bigint | varchar, varchar | scalar | 1 | Returns the first occurance of string in string list (inputStrList) where string list (inputStrList) is a comma-delimited string. |  |
| first_value | t | t | window | 1 |  |  |
| flatten | array(E) | array(array(E)) | scalar | 1 | Flattens the given array |  |
| floor | bigint | bigint | scalar | 1 | Round down to nearest integer |  |
| floor | decimal(rp,0) | decimal(p,s) | scalar | 1 | Round down to nearest integer |  |
| floor | double | double | scalar | 1 | Round down to nearest integer |  |
| floor | integer | integer | scalar | 1 | Round down to nearest integer |  |
| floor | real | real | scalar | 1 | Round down to nearest integer |  |
| floor | smallint | smallint | scalar | 1 | Round down to nearest integer |  |
| floor | tinyint | tinyint | scalar | 1 | Round down to nearest integer |  |
| format_datetime | varchar | timestamp(p) with time zone, varchar(x) | scalar | 1 | Formats the given time by the given format |  |
| format_datetime | varchar | timestamp(p), varchar(x) | scalar | 1 | Formats the given time by the given format |  |
| format_number | varchar | bigint | scalar | 1 | Formats large number using a unit symbol |  |
| format_number | varchar | double | scalar | 1 | Formats large number using a unit symbol |  |
| format_unixtimestamp | varchar | bigint | scalar | 1 | Converts the number of seconds from unix epoch to a string representing the timestamp |  |
| format_unixtimestamp | varchar | bigint, varchar | scalar | 1 | Converts the number of seconds from unix epoch to a string representing the timestamp according to the given format |  |
| from_base | bigint | varchar(x), bigint | scalar | 1 | Convert a string in the given base to a number |  |
| from_base64 | varbinary | varbinary | scalar | 1 | Decode base64 encoded binary data |  |
| from_base64 | varbinary | varchar(x) | scalar | 1 | Decode base64 encoded binary data |  |
| from_base64url | varbinary | varbinary | scalar | 1 | Decode URL safe base64 encoded binary data |  |
| from_base64url | varbinary | varchar(x) | scalar | 1 | Decode URL safe base64 encoded binary data |  |
| from_big_endian_32 | integer | varbinary | scalar | 1 | Decode bigint value from a 32-bit 2’s complement big endian varbinary |  |
| from_big_endian_64 | bigint | varbinary | scalar | 1 | Decode bigint value from a 64-bit 2’s complement big endian varbinary |  |
| from_datasize | double | varchar, varchar | scalar | 1 | Converts a string representing data size in airlift’s DataSize format to a double representing size in the specified size unit |  |
| from_duration | double | varchar, varchar | scalar | 1 | Converts a string representing time duration in airlift’s Duration format to a double representing time in the specified time unit |  |
| from_encoded_polyline | geometry | varchar | scalar | 1 | Decodes a polyline to a linestring |  |
| from_geojson_geometry | sphericalgeography | varchar | scalar | 1 | Returns a spherical geography from a GeoJSON string |  |
| from_hex | varbinary | varbinary | scalar | 1 | Decode hex encoded binary data |  |
| from_hex | varbinary | varchar(x) | scalar | 1 | Decode hex encoded binary data |  |
| from_ieee754_32 | real | varbinary | scalar | 1 | Decode the 32-bit big-endian binary in IEEE 754 single-precision floating-point format |  |
| from_ieee754_64 | double | varbinary | scalar | 1 | Decode the 64-bit big-endian binary in IEEE 754 double-precision floating-point format |  |
| from_iso8601_date | date | varchar(x) | scalar | 1 |  |  |
| from_iso8601_timestamp | timestamp(3) with time zone | varchar(x) | scalar | 1 |  |  |
| from_iso8601_timestamp_nanos | timestamp(9) with time zone | varchar(x) | scalar | 1 |  |  |
| from_unixtime | timestamp(3) with time zone | double | scalar | 1 |  |  |
| from_unixtime | timestamp(3) with time zone | double, bigint, bigint | scalar | 1 |  |  |
| from_unixtime | timestamp(3) with time zone | double, varchar(x) | scalar | 1 |  |  |
| from_unixtime_nanos | timestamp(9) with time zone | bigint | scalar | 1 |  |  |
| from_unixtime_nanos | timestamp(9) with time zone | decimal(p,s) | scalar | 1 |  |  |
| from_utc_timestamp | timestamp | timestamp, varchar | scalar | 1 | given timestamp in UTC and converts to given timezone |  |
| from_utc_timestamp | timestamp | varchar, varchar | scalar | 1 | given timestamp (in varchar) in UTC and converts to given timezone |  |
| from_utf8 | varchar | varbinary | scalar | 1 | Decodes the UTF-8 encoded string |  |
| from_utf8 | varchar | varbinary, bigint | scalar | 1 | Decodes the UTF-8 encoded string |  |
| from_utf8 | varchar | varbinary, varchar(x) | scalar | 1 | Decodes the UTF-8 encoded string |  |
| G |  |  |  | 0 |  |  |
| geometric_mean | double | bigint | aggregate | 1 |  |  |
| geometric_mean | double | double | aggregate | 1 |  |  |
| geometric_mean | real | real | aggregate | 1 |  |  |
| geometry_from_hadoop_shape | geometry | varbinary | scalar | 1 | Returns a Geometry type object from Spatial Framework for Hadoop representation |  |
| geometry_invalid_reason | varchar | geometry | scalar | 1 | Returns the reason for why the input geometry is not valid. Returns null if the input is valid. |  |
| geometry_nearest_points | row(geometry,geometry) | geometry, geometry | scalar | 1 | Return the closest points on the two geometries |  |
| geometry_to_bing_tiles | array(bingtile) | geometry, integer | scalar | 1 | Given a geometry and a zoom level, returns the minimum set of Bing tiles that fully covers that geometry |  |
| geometry_union | geometry | array(geometry) | scalar | 1 | Returns a geometry that represents the point set union of the input geometries. |  |
| geometry_union_agg | geometry | geometry | aggregate | 1 | Returns a geometry that represents the point set union of the input geometries. |  |
| great_circle_distance | double | double, double, double, double | scalar | 1 | Calculates the great-circle distance between two points on the Earth’s surface in kilometers |  |
| greatest | E | E | scalar | 1 | Get the largest of the given values |  |
| H |  |  |  | 0 |  |  |
| hamming_distance | bigint | varchar(x), varchar(y) | scalar | 1 | Computes Hamming distance between two strings |  |
| hash_counts | map(bigint,smallint) | setdigest | scalar | 1 |  |  |
| hex | varchar | bigint | scalar | 1 | Converts integer number to hex value |  |
| hex | varchar | varbinary | scalar | 1 | Converts binary to hex value |  |
| hex | varchar | varchar | scalar | 1 | Converts string number to hex value |  |
| histogram | map(K,bigint) | K | aggregate | 1 | Count the number of times each value occurs |  |
| hmac_md5 | varbinary | varbinary, varbinary | scalar | 1 | Compute HMAC with MD5 |  |
| hmac_sha1 | varbinary | varbinary, varbinary | scalar | 1 | Compute HMAC with SHA1 |  |
| hmac_sha256 | varbinary | varbinary, varbinary | scalar | 1 | Compute HMAC with SHA256 |  |
| hmac_sha512 | varbinary | varbinary, varbinary | scalar | 1 | Compute HMAC with SHA512 |  |
| hour | bigint | interval day to second | scalar | 1 | Hour of the day of the given interval |  |
| hour | bigint | time(p) | scalar | 1 | Hour of the day of the given time |  |
| hour | bigint | time(p) with time zone | scalar | 1 | Hour of the day of the given time |  |
| hour | bigint | timestamp(p) | scalar | 1 | Hour of the day of the given timestamp |  |
| hour | bigint | timestamp(p) with time zone | scalar | 1 | Hour of the day of the given timestamp |  |
| hour | bigint | varchar | scalar | 1 | day of the year of the given string timestamp |  |
| human_readable_seconds | varchar | double | scalar | 1 |  |  |
| I |  |  |  | 0 |  |  |
| index | bigint | varchar, varchar | scalar | 1 | Returns index of first occurrence of a substring (or 0 if not found) |  |
| infinity | double |  | scalar | 1 | Infinity |  |
| instr | bigint | varchar, varchar | scalar | 1 | returns index of first occurrence of a substring (or 0 if not found) in string |  |
| intersection_cardinality | bigint | setdigest, setdigest | scalar | 1 |  |  |
| inverse_beta_cdf | double | double, double, double | scalar | 1 | Inverse of Beta cdf given a, b parameters and probability |  |
| inverse_normal_cdf | double | double, double, double | scalar | 1 | Inverse of normal cdf given a mean, std, and probability |  |
| is_finite | boolean | double | scalar | 1 | Test if value is finite |  |
| is_infinite | boolean | double | scalar | 1 | Test if value is infinite |  |
| is_json_scalar | boolean | json | scalar | 1 |  |  |
| is_json_scalar | boolean | varchar(x) | scalar | 1 |  |  |
| is_nan | boolean | double | scalar | 1 | Test if value is not-a-number |  |
| J |  |  |  | 0 |  |  |
| jaccard_index | double | setdigest, setdigest | scalar | 1 |  |  |
| json_array_contains | boolean | json, bigint | scalar | 1 |  |  |
| json_array_contains | boolean | json, boolean | scalar | 1 |  |  |
| json_array_contains | boolean | json, double | scalar | 1 |  |  |
| json_array_contains | boolean | json, varchar(x) | scalar | 1 |  |  |
| json_array_contains | boolean | varchar(x), bigint | scalar | 1 |  |  |
| json_array_contains | boolean | varchar(x), boolean | scalar | 1 |  |  |
| json_array_contains | boolean | varchar(x), double | scalar | 1 |  |  |
| json_array_contains | boolean | varchar(x), varchar(y) | scalar | 1 |  |  |
| json_array_get | json | json, bigint | scalar | 1 |  |  |
| json_array_get | json | varchar(x), bigint | scalar | 1 |  |  |
| json_array_length | bigint | json | scalar | 1 |  |  |
| json_array_length | bigint | varchar(x) | scalar | 1 |  |  |
| json_extract | json | json, jsonpath | scalar | 1 |  |  |
| json_extract | json | varchar(x), jsonpath | scalar | 1 |  |  |
| json_extract_scalar | varchar | json, jsonpath | scalar | 1 |  |  |
| json_extract_scalar | varchar(x) | varchar(x), jsonpath | scalar | 1 |  |  |
| json_format | varchar | json | scalar | 1 |  |  |
| json_parse | json | varchar(x) | scalar | 1 |  |  |
| json_size | bigint | json, jsonpath | scalar | 1 |  |  |
| json_size | bigint | varchar(x), jsonpath | scalar | 1 |  |  |
| K |  |  |  | 0 |  |  |
| kurtosis | double | bigint | aggregate | 1 | Returns the (excess) kurtosis of the argument |  |
| kurtosis | double | double | aggregate | 1 | Returns the (excess) kurtosis of the argument |  |
| L |  |  |  | 0 |  |  |
| lag | t | t | window | 1 |  |  |
| lag | t | t, bigint | window | 1 |  |  |
| lag | t | t, bigint, t | window | 1 |  |  |
| last_day_of_month | date | date | scalar | 1 | Last day of the month of the given date |  |
| last_day_of_month | date | timestamp(p) | scalar | 1 | Last day of the month of the given timestamp |  |
| last_day_of_month | date | timestamp(p) with time zone | scalar | 1 | Last day of the month of the given timestamp |  |
| last_value | t | t | window | 1 |  |  |
| lead | t | t | window | 1 |  |  |
| lead | t | t, bigint | window | 1 |  |  |
| lead | t | t, bigint, t | window | 1 |  |  |
| learn_classifier | classifier(bigint) | bigint, map(bigint,double) | aggregate | 1 |  |  |
| learn_classifier | classifier(bigint) | double, map(bigint,double) | aggregate | 1 |  |  |
| learn_classifier | classifier(varchar) | varchar, map(bigint,double) | aggregate | 1 |  |  |
| learn_libsvm_classifier | classifier(bigint) | bigint, map(bigint,double), varchar(x) | aggregate | 1 |  |  |
| learn_libsvm_classifier | classifier(bigint) | double, map(bigint,double), varchar | aggregate | 1 |  |  |
| learn_libsvm_classifier | classifier(varchar) | varchar, map(bigint,double), varchar | aggregate | 1 |  |  |
| learn_libsvm_regressor | regressor | bigint, map(bigint,double), varchar | aggregate | 1 |  |  |
| learn_libsvm_regressor | regressor | double, map(bigint,double), varchar | aggregate | 1 |  |  |
| learn_regressor | regressor | bigint, map(bigint,double) | aggregate | 1 |  |  |
| learn_regressor | regressor | double, map(bigint,double) | aggregate | 1 |  |  |
| least | E | E | scalar | 1 | Get the smallest of the given values |  |
| length | bigint | char(x) | scalar | 1 | Count of code points of the given string |  |
| length | bigint | varbinary | scalar | 1 | Length of the given binary |  |
| length | bigint | varchar(x) | scalar | 1 | Count of code points of the given string |  |
| levenshtein_distance | bigint | varchar(x), varchar(y) | scalar | 1 | Computes Levenshtein distance between two strings |  |
| line_interpolate_point | geometry | geometry, double | scalar | 1 | Returns a Point interpolated along a LineString at the fraction given. |  |
| line_interpolate_points | array(geometry) | geometry, double | scalar | 1 | Returns an array of Points interpolated along a LineString. |  |
| line_locate_point | double | geometry, geometry | scalar | 1 | Returns a float between 0 and 1 representing the location of the closest point on the LineString to the given Point, as a fraction of total 2d line length. |  |
| listagg | varchar | varchar(v), varchar(d), boolean, varchar(f), boolean | aggregate | 1 | concatenates the input values with the specified separator |  |
| ln | double | double | scalar | 1 | Natural logarithm |  |
| locate | bigint | varchar, varchar | scalar | 1 | returns index of first occurrence of a substring (or 0 if not found) |  |
| locate | bigint | varchar, varchar, bigint | scalar | 1 | Returns the position of the first occurrence of substring in str after position pos |  |
| log | double | double, double | scalar | 1 | Logarithm to given base |  |
| log10 | double | double | scalar | 1 | Logarithm to base 10 |  |
| log2 | double | double | scalar | 1 | Logarithm to base 2 |  |
| lower | char(x) | char(x) | scalar | 1 | Converts the string to lower case |  |
| lower | varchar(x) | varchar(x) | scalar | 1 | Converts the string to lower case |  |
| lpad | varbinary | varbinary, bigint, varbinary | scalar | 1 | Pads a varbinary on the left |  |
| lpad | varchar | varchar(x), bigint, varchar(y) | scalar | 1 | Pads a string on the left |  |
| ltrim | char(x) | char(x) | scalar | 1 | Removes whitespace from the beginning of a string |  |
| ltrim | char(x) | char(x), codepoints | scalar | 1 | Remove the longest string containing only given characters from the beginning of a string |  |
| ltrim | varchar(x) | varchar(x) | scalar | 1 | Removes whitespace from the beginning of a string |  |
| ltrim | varchar(x) | varchar(x), codepoints | scalar | 1 | Remove the longest string containing only given characters from the beginning of a string |  |
| luhn_check | boolean | varchar | scalar | 1 | Checks that a string of digits is valid according to the Luhn algorithm |  |
| M |  |  |  | 0 |  |  |
| make_set_digest | setdigest | t | aggregate | 1 |  |  |
| map | map(K,V) | array(K), array(V) | scalar | 1 | Constructs a map from the given key/value arrays |  |
| map | map(unknown,unknown) |  | scalar | 1 | Creates an empty map |  |
| map_agg | map(K,V) | K, V | aggregate | 1 | Aggregates all the rows (key/value pairs) into a single map |  |
| map_concat | map(K,V) | map(K,V) | scalar | 1 | Concatenates given maps |  |
| map_entries | array(row(k,v)) | map(k,v) | scalar | 1 | Construct an array of entries from a given map |  |
| map_filter | map(K,V) | map(K,V), function(K,V,boolean) | scalar | 0 | return map containing entries that match the given predicate |  |
| map_from_entries | map(k,v) | array(row(k,v)) | scalar | 1 | Construct a map from an array of entries |  |
| map_keys | array(k) | map(k,v) | scalar | 1 | Returns the keys of the given map(K,V) as an array |  |
| map_union | map(K,V) | map(K,V) | aggregate | 1 | Aggregate all the maps into a single map |  |
| map_values | array(v) | map(k,v) | scalar | 1 | Returns the values of the given map(K,V) as an array |  |
| map_zip_with | map(K,V3) | map(K,V1), map(K,V2), function(K,V1,V2,V3) | scalar | 0 | Merge two maps into a single map by applying the lambda function to the pair of values with the same key |  |
| max | E | E | aggregate | 1 | Returns the maximum value of the argument |  |
| max | array(E) | E, bigint | aggregate | 1 | Returns the maximum values of the argument |  |
| max_by | V | V, K | aggregate | 1 | Returns the value of the first argument, associated with the maximum value of the second argument |  |
| max_by | array(V) | V, K, bigint | aggregate | 1 | Returns the values of the first argument associated with the maximum values of the second argument |  |
| md5 | varbinary | varbinary | scalar | 1 | Compute md5 hash |  |
| md5 | varchar | varchar | scalar | 1 | md5 hash |  |
| merge | hyperloglog | hyperloglog | aggregate | 1 |  |  |
| merge | qdigest(T) | qdigest(T) | aggregate | 1 | Merges the input quantile digests into a single quantile digest |  |
| merge | tdigest | tdigest | aggregate | 1 |  |  |
| merge_set_digest | setdigest | setdigest | aggregate | 1 |  |  |
| millisecond | bigint | interval day to second | scalar | 1 | Millisecond of the second of the given interval |  |
| millisecond | bigint | time(p) | scalar | 1 | Millisecond of the second of the given time |  |
| millisecond | bigint | time(p) with time zone | scalar | 1 | Millisecond of the second of the given time |  |
| millisecond | bigint | timestamp(p) | scalar | 1 | Millisecond of the second of the given timestamp |  |
| millisecond | bigint | timestamp(p) with time zone | scalar | 1 | Millisecond of the second of the given timestamp |  |
| min | E | E | aggregate | 1 | Returns the minimum value of the argument |  |
| min | array(E) | E, bigint | aggregate | 1 | Returns the minimum values of the argument |  |
| min_by | V | V, K | aggregate | 1 | Returns the value of the first argument, associated with the minimum value of the second argument |  |
| min_by | array(V) | V, K, bigint | aggregate | 1 | Returns the values of the first argument associated with the minimum values of the second argument |  |
| minute | bigint | interval day to second | scalar | 1 | Minute of the hour of the given interval |  |
| minute | bigint | time(p) | scalar | 1 | Minute of the hour of the given time |  |
| minute | bigint | time(p) with time zone | scalar | 1 | Minute of the hour of the given time |  |
| minute | bigint | timestamp(p) | scalar | 1 | Minute of the hour of the given timestamp |  |
| minute | bigint | timestamp(p) with time zone | scalar | 1 | Minute of the hour of the given timestamp |  |
| minute | bigint | varchar | scalar | 1 | day of the year of the given string timestamp |  |
| mod | bigint | bigint, bigint | scalar | 1 | Remainder of given quotient |  |
| mod | decimal(r_precision,r_scale) | decimal(a_precision,a_scale), decimal(b_precision,b_scale) | scalar | 1 |  |  |
| mod | double | double, double | scalar | 1 | Remainder of given quotient |  |
| mod | integer | integer, integer | scalar | 1 | Remainder of given quotient |  |
| mod | real | real, real | scalar | 1 | Remainder of given quotient |  |
| mod | smallint | smallint, smallint | scalar | 1 | Remainder of given quotient |  |
| mod | tinyint | tinyint, tinyint | scalar | 1 | Remainder of given quotient |  |
| month | bigint | date | scalar | 1 | Month of the year of the given date |  |
| month | bigint | interval year to month | scalar | 1 | Month of the year of the given interval |  |
| month | bigint | timestamp(p) | scalar | 1 | Month of the year of the given timestamp |  |
| month | bigint | timestamp(p) with time zone | scalar | 1 | Month of the year of the given timestamp |  |
| month | bigint | varchar | scalar | 1 | month of the year of the given string timestamp |  |
| multimap_agg | map(K,array(V)) | K, V | aggregate | 1 | Aggregates all the rows (key/value pairs) into a single multimap |  |
| multimap_from_entries | map(k,array(v)) | array(row(k,v)) | scalar | 1 | Construct a multimap from an array of entries |  |
| murmur3 | varbinary | varbinary | scalar | 1 | Compute murmur3 hash |  |
| N |  |  |  | 0 |  |  |
| nan | double |  | scalar | 1 | Constant representing not-a-number |  |
| ngrams | array(array(t)) | array(t), integer | scalar | 1 | Return N-grams for the input |  |
| none_match | boolean | array(t), function(t,boolean) | scalar | 1 | Returns true if all elements of the array don’t match the given predicate |  |
| normal_cdf | double | double, double, double | scalar | 1 | Normal cdf given a mean, standard deviation, and value |  |
| normalize | varchar | varchar(x), varchar(y) | scalar | 1 | Transforms the string to normalized form |  |
| now | timestamp(3) with time zone |  | scalar | 1 | Current timestamp with time zone |  |
| nth_value | t | t, bigint | window | 1 |  |  |
| ntile | bigint | bigint | window | 1 |  |  |
| numeric_histogram | map(double,double) | bigint, double | aggregate | 1 |  |  |
| numeric_histogram | map(double,double) | bigint, double, double | aggregate | 1 |  |  |
| numeric_histogram | map(real,real) | bigint, real | aggregate | 1 |  |  |
| numeric_histogram | map(real,real) | bigint, real, double | aggregate | 1 |  |  |
| nvl | t | t, t | scalar | 1 | Return default value if the value is NULL else return value |  |
| O |  |  |  | 0 |  |  |
| objectid | objectid |  | scalar | 1 | Mongodb ObjectId |  |
| objectid | objectid | varchar | scalar | 1 | Mongodb ObjectId from the given string |  |
| objectid_timestamp | timestamp(3) with time zone | objectid | scalar | 1 | Timestamp from the given Mongodb ObjectId |  |
| P |  |  |  | 0 |  |  |
| parse_data_size | decimal(38,0) | varchar(x) | scalar | 1 | Converts data size string to bytes |  |
| parse_datetime | timestamp(3) with time zone | varchar(x), varchar(y) | scalar | 1 | Parses the specified date/time by the given format |  |
| parse_duration | interval day to second | varchar(x) | scalar | 1 | Convert duration string to an interval |  |
| parse_presto_data_size | decimal(38,0) | varchar(x) | scalar | 1 | Converts data size string to bytes |  |
| percent_rank | double |  | window | 1 |  |  |
| pi | double |  | scalar | 1 | The constant Pi |  |
| pmod | bigint | bigint, bigint | scalar | 1 | Returns the positive value of a mod b. |  |
| pmod | double | double, double | scalar | 1 | Returns the positive value of a mod b |  |
| pow | double | double, double | scalar | 1 | Value raised to the power of exponent |  |
| power | double | double, double | scalar | 1 | Value raised to the power of exponent |  |
| Q |  |  |  | 0 |  |  |
| qdigest_agg | qdigest(V) | V | aggregate | 1 | Returns a qdigest from the set of reals, bigints or doubles |  |
| qdigest_agg | qdigest(V) | V, bigint | aggregate | 1 | Returns a qdigest from the set of reals, bigints or doubles |  |
| qdigest_agg | qdigest(V) | V, bigint, double | aggregate | 1 | Returns a qdigest from the set of reals, bigints or doubles |  |
| quarter | bigint | date | scalar | 1 | Quarter of the year of the given date |  |
| quarter | bigint | timestamp(p) | scalar | 1 | Quarter of the year of the given timestamp |  |
| quarter | bigint | timestamp(p) with time zone | scalar | 1 | Quarter of the year of the given timestamp |  |
| R |  |  |  | 0 |  |  |
| radians | double | double | scalar | 1 | Converts an angle in degrees to radians |  |
| rand | bigint | bigint | scalar | 0 | A pseudo-random number between 0 and value (exclusive) |  |
| rand | bigint | bigint, bigint | scalar | 0 | A pseudo-random number between start and stop (exclusive) |  |
| rand | double |  | scalar | 0 | A pseudo-random value |  |
| rand | integer | integer | scalar | 0 | A pseudo-random number between 0 and value (exclusive) |  |
| rand | integer | integer, integer | scalar | 0 | A pseudo-random number between start and stop (exclusive) |  |
| rand | smallint | smallint | scalar | 0 | A pseudo-random number between 0 and value (exclusive) |  |
| rand | smallint | smallint, smallint | scalar | 0 | A pseudo-random number between start and stop (exclusive) |  |
| rand | tinyint | tinyint | scalar | 0 | A pseudo-random number between 0 and value (exclusive) |  |
| rand | tinyint | tinyint, tinyint | scalar | 0 | A pseudo-random number between start and stop (exclusive) |  |
| rand_cellphone | varchar |  | scalar | 0 | Random cell phone |  |
| rand_email | varchar |  | scalar | 0 | Random email address |  |
| rand_pattern | varchar | varchar | scalar | 0 | Random string matching pattern (# for number and ? for letter) |  |
| rand_phone | varchar |  | scalar | 0 | Random phone |  |
| rand_regexify | varchar | varchar | scalar | 0 | Random string matching regex pattern |  |
| rand_ssn | varchar |  | scalar | 0 | Random ssn |  |
| rand_timestamp | timestamp(3) |  | scalar | 1 |  |  |
| rand_timestamp_with_timezone | timestamp(3) with time zone |  | scalar | 1 |  |  |
| random | bigint | bigint | scalar | 0 | A pseudo-random number between 0 and value (exclusive) |  |
| random | bigint | bigint, bigint | scalar | 0 | A pseudo-random number between start and stop (exclusive) |  |
| random | double |  | scalar | 0 | A pseudo-random value |  |
| random | integer | integer | scalar | 0 | A pseudo-random number between 0 and value (exclusive) |  |
| random | integer | integer, integer | scalar | 0 | A pseudo-random number between start and stop (exclusive) |  |
| random | smallint | smallint | scalar | 0 | A pseudo-random number between 0 and value (exclusive) |  |
| random | smallint | smallint, smallint | scalar | 0 | A pseudo-random number between start and stop (exclusive) |  |
| random | tinyint | tinyint | scalar | 0 | A pseudo-random number between 0 and value (exclusive) |  |
| random | tinyint | tinyint, tinyint | scalar | 0 | A pseudo-random number between start and stop (exclusive) |  |
| random_cellphone | varchar |  | scalar | 0 | Random cell phone |  |
| random_email | varchar |  | scalar | 0 | Random email address |  |
| random_pattern | varchar | varchar | scalar | 0 | Random string matching pattern (# for number and ? for letter) |  |
| random_phone | varchar |  | scalar | 0 | Random phone |  |
| random_regexify | varchar | varchar | scalar | 0 | Random string matching regex pattern |  |
| random_ssn | varchar |  | scalar | 0 | Random ssn |  |
| rands | double | bigint | scalar | 1 | a seed pseudo-random value |  |
| rank | bigint |  | window | 1 |  |  |
| redact | t | t | scalar | 1 | Return redacted value |  |
| reduce | R | array(T), S, function(S,T,S), function(S,R) | scalar | 0 | Reduce elements of the array into a single value |  |
| reduce_agg | S | T, S, function(S,T,S), function(S,S,S) | aggregate | 1 | Reduce input elements into a single value |  |
| regexp_count | bigint | varchar(x), joniregexp | scalar | 1 | Returns the number of times that a pattern occurs in a string |  |
| regexp_extract | varchar(x) | varchar(x), joniregexp | scalar | 1 | String extracted using the given pattern |  |
| regexp_extract | varchar(x) | varchar(x), joniregexp, bigint | scalar | 1 | Returns regex group of extracted string with a pattern |  |
| regexp_extract_all | array(varchar(x)) | varchar(x), joniregexp | scalar | 1 | String(s) extracted using the given pattern |  |
| regexp_extract_all | array(varchar(x)) | varchar(x), joniregexp, bigint | scalar | 1 | Group(s) extracted using the given pattern |  |
| regexp_like | boolean | varchar(x), joniregexp | scalar | 1 | Returns whether the pattern is contained within the string |  |
| regexp_position | integer | varchar(x), joniregexp | scalar | 1 | Returns the index of the matched substring |  |
| regexp_position | integer | varchar(x), joniregexp, integer | scalar | 1 | Returns the index of the matched substring starting from the specified position |  |
| regexp_position | integer | varchar(x), joniregexp, integer, integer | scalar | 1 | Returns the index of the n-th matched substring starting from the specified position |  |
| regexp_replace | varchar | varchar, joniregexp, function(array(varchar),varchar(x)) | scalar | 1 | Replaces substrings matching a regular expression using a lambda function |  |
| regexp_replace | varchar(x) | varchar(x), joniregexp | scalar | 1 | Removes substrings matching a regular expression |  |
| regexp_replace | varchar(z) | varchar(x), joniregexp, varchar(y) | scalar | 1 | Replaces substrings matching a regular expression by given string |  |
| regexp_split | array(varchar(x)) | varchar(x), joniregexp | scalar | 1 | Returns array of strings split by pattern |  |
| regr_intercept | double | double, double | aggregate | 1 |  |  |
| regr_intercept | real | real, real | aggregate | 1 |  |  |
| regr_slope | double | double, double | aggregate | 1 |  |  |
| regr_slope | real | real, real | aggregate | 1 |  |  |
| regress | double | map(bigint,double), regressor | scalar | 1 |  |  |
| render | varchar(16) | boolean | scalar | 1 |  |  |
| render | varchar(35) | bigint, color | scalar | 1 |  |  |
| render | varchar(41) | double, color | scalar | 1 |  |  |
| render | varchar(y) | varchar(x), color | scalar | 1 |  |  |
| repeat | array(t) | t, integer | scalar | 1 | Repeat an element for a given number of times |  |
| replace | varchar(u) | varchar(x), varchar(y), varchar(z) | scalar | 1 | Greedily replaces occurrences of a pattern with a string |  |
| replace | varchar(x) | varchar(x), varchar(y) | scalar | 1 | Greedily removes occurrences of a pattern in a string |  |
| reverse | array(e) | array(e) | scalar | 1 | Returns an array which has the reversed order of the given array. |  |
| reverse | varbinary | varbinary | scalar | 1 | Reverse a given varbinary |  |
| reverse | varchar(x) | varchar(x) | scalar | 1 | Reverse all code points in a given string |  |
| rgb | color | bigint, bigint, bigint | scalar | 1 |  |  |
| round | bigint | bigint | scalar | 1 | Round to nearest integer |  |
| round | bigint | bigint, integer | scalar | 1 | Round to nearest integer |  |
| round | decimal(rp,rs) | decimal(p,s) | scalar | 1 | Round to nearest integer |  |
| round | decimal(rp,s) | decimal(p,s), integer | scalar | 1 | Round to given number of decimal places |  |
| round | double | double | scalar | 1 | Round to nearest integer |  |
| round | double | double, integer | scalar | 1 | Round to given number of decimal places |  |
| round | integer | integer | scalar | 1 | Round to nearest integer |  |
| round | integer | integer, integer | scalar | 1 | Round to nearest integer |  |
| round | real | real | scalar | 1 | Round to given number of decimal places |  |
| round | real | real, integer | scalar | 1 | Round to given number of decimal places |  |
| round | smallint | smallint | scalar | 1 | Round to nearest integer |  |
| round | smallint | smallint, integer | scalar | 1 | Round to nearest integer |  |
| round | tinyint | tinyint | scalar | 1 | Round to nearest integer |  |
| round | tinyint | tinyint, integer | scalar | 1 | Round to nearest integer |  |
| round_off | double | double | scalar | 1 | whatever |  |
| row_number | bigint |  | window | 1 |  |  |
| rpad | varbinary | varbinary, bigint, varbinary | scalar | 1 | Pads a varbinary on the right |  |
| rpad | varchar | varchar(x), bigint, varchar(y) | scalar | 1 | Pads a string on the right |  |
| rtrim | char(x) | char(x) | scalar | 1 | Removes whitespace from the end of a string |  |
| rtrim | char(x) | char(x), codepoints | scalar | 1 | Remove the longest string containing only given characters from the end of a string |  |
| rtrim | varchar(x) | varchar(x) | scalar | 1 | Removes whitespace from the end of a string |  |
| rtrim | varchar(x) | varchar(x), codepoints | scalar | 1 | Remove the longest string containing only given characters from the end of a string |  |
| S |  |  |  | 0 |  |  |
| second | bigint | interval day to second | scalar | 1 | Second of the minute of the given interval |  |
| second | bigint | time(p) | scalar | 1 | Second of the minute of the given time |  |
| second | bigint | time(p) with time zone | scalar | 1 | Second of the minute of the given time |  |
| second | bigint | timestamp(p) | scalar | 1 | Second of the minute of the given timestamp |  |
| second | bigint | timestamp(p) with time zone | scalar | 1 | Second of the minute of the given timestamp |  |
| second | bigint | varchar | scalar | 1 | day of the year of the given string timestamp |  |
| sequence | array(bigint) | bigint, bigint | scalar | 1 |  |  |
| sequence | array(bigint) | bigint, bigint, bigint | scalar | 1 | Sequence function to generate synthetic arrays |  |
| sequence | array(date) | date, date | scalar | 1 |  |  |
| sequence | array(date) | date, date, interval day to second | scalar | 1 |  |  |
| sequence | array(date) | date, date, interval year to month | scalar | 1 |  |  |
| sequence | array(timestamp(p)) | timestamp(p), timestamp(p), interval day to second | scalar | 1 |  |  |
| sequence | array(timestamp(p)) | timestamp(p), timestamp(p), interval year to month | scalar | 1 |  |  |
| sha1 | varbinary | varbinary | scalar | 1 | Compute sha1 hash |  |
| sha256 | varbinary | varbinary | scalar | 1 | Compute sha256 hash |  |
| sha256 | varchar | varchar | scalar | 1 | sha256 hash |  |
| sha512 | varbinary | varbinary | scalar | 1 | Compute sha512 hash |  |
| shuffle | array(e) | array(e) | scalar | 0 | Generates a random permutation of the given array. |  |
| sign | bigint | bigint | scalar | 1 |  |  |
| sign | decimal(1,0) | decimal(p,s) | scalar | 1 | Signum |  |
| sign | double | double | scalar | 1 | Signum |  |
| sign | integer | integer | scalar | 1 | Signum |  |
| sign | real | real | scalar | 1 | Signum |  |
| sign | smallint | smallint | scalar | 1 | Signum |  |
| sign | tinyint | tinyint | scalar | 1 | Signum |  |
| simplify_geometry | geometry | geometry, double | scalar | 1 | Returns a “simplified” version of the given geometry |  |
| sin | double | double | scalar | 1 | Sine |  |
| skewness | double | bigint | aggregate | 1 | Returns the skewness of the argument |  |
| skewness | double | double | aggregate | 1 | Returns the skewness of the argument |  |
| slice | array(e) | array(e), bigint, bigint | scalar | 1 | Subsets an array given an offset (1-indexed) and length |  |
| soundex | varchar(4) | varchar | scalar | 1 | Encodes a string into a Soundex value |  |
| spatial_partitioning | varchar | geometry | aggregate | 1 |  |  |
| spatial_partitions | array(integer) | kdbtree, geometry | scalar | 1 | Returns an array of spatial partition IDs for a given geometry |  |
| spatial_partitions | array(integer) | kdbtree, geometry, double | scalar | 1 | Returns an array of spatial partition IDs for a geometry representing a set of points within specified distance from the input geometry |  |
| split | array(varchar(x)) | varchar(x), varchar(y) | scalar | 1 |  |  |
| split | array(varchar(x)) | varchar(x), varchar(y), bigint | scalar | 1 |  |  |
| split_part | varchar(x) | varchar(x), varchar(y), bigint | scalar | 1 | Splits a string by a delimiter and returns the specified field (counting from one) |  |
| split_to_map | map(varchar,varchar) | varchar, varchar, varchar | scalar | 1 | Creates a map using entryDelimiter and keyValueDelimiter |  |
| split_to_multimap | map(varchar,array(varchar)) | varchar, varchar, varchar | scalar | 1 | Creates a multimap by splitting a string into key/value pairs |  |
| spooky_hash_v2_32 | varbinary | varbinary | scalar | 1 | Compute SpookyHashV2 32-bit hash |  |
| spooky_hash_v2_64 | varbinary | varbinary | scalar | 1 | Compute SpookyHashV2 64-bit hash |  |
| sqrt | double | double | scalar | 1 | Square root |  |
| ST_Area | double | geometry | scalar | 1 | Returns the 2D Euclidean area of a geometry |  |
| ST_Area | double | sphericalgeography | scalar | 1 | Returns the area of a geometry on the Earth’s surface using spherical model |  |
| ST_AsBinary | varbinary | geometry | scalar | 1 | Returns the Well-Known Binary (WKB) representation of the geometry |  |
| ST_AsText | varchar | geometry | scalar | 1 | Returns the Well-Known Text (WKT) representation of the geometry |  |
| ST_Boundary | geometry | geometry | scalar | 1 | Returns the closure of the combinatorial boundary of this Geometry |  |
| ST_Buffer | geometry | geometry, double | scalar | 1 | Returns the geometry that represents all points whose distance from the specified geometry is less than or equal to the specified distance |  |
| ST_Centroid | geometry | geometry | scalar | 1 | Returns the Point value that is the mathematical centroid of a Geometry |  |
| ST_Contains | boolean | geometry, geometry | scalar | 1 | Returns TRUE if and only if no points of right lie in the exterior of left, and at least one point of the interior of left lies in the interior of right |  |
| ST_ConvexHull | geometry | geometry | scalar | 1 | Returns the minimum convex geometry that encloses all input geometries |  |
| ST_CoordDim | tinyint | geometry | scalar | 1 | Return the coordinate dimension of the Geometry |  |
| ST_Crosses | boolean | geometry, geometry | scalar | 1 | Returns TRUE if the supplied geometries have some, but not all, interior points in common |  |
| ST_Difference | geometry | geometry, geometry | scalar | 1 | Returns the Geometry value that represents the point set difference of two geometries |  |
| ST_Dimension | tinyint | geometry | scalar | 1 | Returns the inherent dimension of this Geometry object, which must be less than or equal to the coordinate dimension |  |
| ST_Disjoint | boolean | geometry, geometry | scalar | 1 | Returns TRUE if the Geometries do not spatially intersect - if they do not share any space together |  |
| ST_Distance | double | geometry, geometry | scalar | 1 | Returns the 2-dimensional cartesian minimum distance (based on spatial ref) between two geometries in projected units |  |
| ST_Distance | double | sphericalgeography, sphericalgeography | scalar | 1 | Returns the great-circle distance in meters between two SphericalGeography points. |  |
| ST_EndPoint | geometry | geometry | scalar | 1 | Returns the last point of a LINESTRING geometry as a Point |  |
| ST_Envelope | geometry | geometry | scalar | 1 | Returns the bounding rectangular polygon of a Geometry |  |
| ST_EnvelopeAsPts | array(geometry) | geometry | scalar | 1 | Returns the lower left and upper right corners of bounding rectangular polygon of a Geometry |  |
| ST_Equals | boolean | geometry, geometry | scalar | 1 | Returns TRUE if the given geometries represent the same geometry |  |
| ST_ExteriorRing | geometry | geometry | scalar | 1 | Returns a line string representing the exterior ring of the POLYGON |  |
| ST_Geometries | array(geometry) | geometry | scalar | 1 | Returns an array of geometries in the specified collection |  |
| ST_GeometryFromText | geometry | varchar | scalar | 1 | Returns a Geometry type object from Well-Known Text representation (WKT) |  |
| ST_GeometryN | geometry | geometry, integer | scalar | 1 | Returns the geometry element at the specified index (indices started with 1) |  |
| ST_GeometryType | varchar | geometry | scalar | 1 | Returns the type of the geometry |  |
| ST_GeomFromBinary | geometry | varbinary | scalar | 1 | Returns a Geometry type object from Well-Known Binary representation (WKB) |  |
| ST_InteriorRingN | geometry | geometry, integer | scalar | 1 | Returns the interior ring element at the specified index (indices start at 1) |  |
| ST_InteriorRings | array(geometry) | geometry | scalar | 1 | Returns an array of interior rings of a polygon |  |
| ST_Intersection | geometry | geometry, geometry | scalar | 1 | Returns the Geometry value that represents the point set intersection of two Geometries |  |
| ST_Intersects | boolean | geometry, geometry | scalar | 1 | Returns TRUE if the Geometries spatially intersect in 2D - (share any portion of space) and FALSE if they don’t (they are Disjoint) |  |
| ST_IsClosed | boolean | geometry | scalar | 1 | Returns TRUE if the LineString or Multi-LineString’s start and end points are coincident |  |
| ST_IsEmpty | boolean | geometry | scalar | 1 | Returns TRUE if this Geometry is an empty geometrycollection, polygon, point etc |  |
| ST_IsRing | boolean | geometry | scalar | 1 | Returns TRUE if and only if the line is closed and simple |  |
| ST_IsSimple | boolean | geometry | scalar | 1 | Returns TRUE if this Geometry has no anomalous geometric points, such as self intersection or self tangency |  |
| ST_IsValid | boolean | geometry | scalar | 1 | Returns true if the input geometry is well formed |  |
| ST_Length | double | geometry | scalar | 1 | Returns the length of a LineString or Multi-LineString using Euclidean measurement on a 2D plane (based on spatial ref) in projected units |  |
| ST_Length | double | sphericalgeography | scalar | 1 | Returns the great-circle length in meters of a linestring or multi-linestring on Earth’s surface |  |
| ST_LineFromText | geometry | varchar | scalar | 1 | Returns a Geometry type LineString object from Well-Known Text representation (WKT) |  |
| ST_LineString | geometry | array(geometry) | scalar | 1 | Returns a LineString from an array of points |  |
| ST_MultiPoint | geometry | array(geometry) | scalar | 1 | Returns a multi-point geometry formed from input points |  |
| ST_NumGeometries | integer | geometry | scalar | 1 | Returns the cardinality of the geometry collection |  |
| ST_NumInteriorRing | bigint | geometry | scalar | 1 | Returns the cardinality of the collection of interior rings of a polygon |  |
| ST_NumPoints | bigint | geometry | scalar | 1 | Returns the number of points in a Geometry |  |
| ST_Overlaps | boolean | geometry, geometry | scalar | 1 | Returns TRUE if the Geometries share space, are of the same dimension, but are not completely contained by each other |  |
| ST_Point | geometry | double, double | scalar | 1 | Returns a Geometry type Point object with the given coordinate values |  |
| ST_PointN | geometry | geometry, integer | scalar | 1 | Returns the vertex of a linestring at the specified index (indices started with 1) |  |
| ST_Points | array(geometry) | geometry | scalar | 1 | Returns an array of points in a geometry |  |
| ST_Polygon | geometry | varchar | scalar | 1 | Returns a Geometry type Polygon object from Well-Known Text representation (WKT) |  |
| ST_Relate | boolean | geometry, geometry, varchar | scalar | 1 | Returns TRUE if this Geometry is spatially related to another Geometry |  |
| ST_StartPoint | geometry | geometry | scalar | 1 | Returns the first point of a LINESTRING geometry as a Point |  |
| ST_SymDifference | geometry | geometry, geometry | scalar | 1 | Returns the Geometry value that represents the point set symmetric difference of two Geometries |  |
| ST_Touches | boolean | geometry, geometry | scalar | 1 | Returns TRUE if the geometries have at least one point in common, but their interiors do not intersect |  |
| ST_Union | geometry | geometry, geometry | scalar | 1 | Returns a geometry that represents the point set union of the input geometries. |  |
| ST_Within | boolean | geometry, geometry | scalar | 1 | Returns TRUE if the geometry A is completely inside geometry B |  |
| ST_X | double | geometry | scalar | 1 | Return the X coordinate of the point |  |
| ST_XMax | double | geometry | scalar | 1 | Returns X maxima of a bounding box of a Geometry |  |
| ST_XMin | double | geometry | scalar | 1 | Returns X minima of a bounding box of a Geometry |  |
| ST_Y | double | geometry | scalar | 1 | Return the Y coordinate of the point |  |
| ST_YMax | double | geometry | scalar | 1 | Returns Y maxima of a bounding box of a Geometry |  |
| ST_YMin | double | geometry | scalar | 1 | Returns Y minima of a bounding box of a Geometry |  |
| starts_with | boolean | varchar(x), varchar(y) | scalar | 1 | Determine whether source starts with prefix or not |  |
| stddev | double | bigint | aggregate | 1 | Returns the sample standard deviation of the argument |  |
| stddev | double | double | aggregate | 1 | Returns the sample standard deviation of the argument |  |
| stddev_pop | double | bigint | aggregate | 1 | Returns the population standard deviation of the argument |  |
| stddev_pop | double | double | aggregate | 1 | Returns the population standard deviation of the argument |  |
| stddev_samp | double | bigint | aggregate | 1 | Returns the sample standard deviation of the argument |  |
| stddev_samp | double | double | aggregate | 1 | Returns the sample standard deviation of the argument |  |
| strpos | bigint | varchar(x), varchar(y) | scalar | 1 | Returns index of first occurrence of a substring (or 0 if not found) |  |
| strpos | bigint | varchar(x), varchar(y), bigint | scalar | 1 | Returns index of n-th occurrence of a substring (or 0 if not found) |  |
| substr | varbinary | varbinary, bigint | scalar | 1 | Suffix starting at given index |  |
| substr | varbinary | varbinary, bigint, bigint | scalar | 1 | Substring of given length starting at an index |  |
| substr | varchar(x) | char(x), bigint | scalar | 1 | Suffix starting at given index |  |
| substr | varchar(x) | char(x), bigint, bigint | scalar | 1 | Substring of given length starting at an index |  |
| substr | varchar(x) | varchar(x), bigint | scalar | 1 | Suffix starting at given index |  |
| substr | varchar(x) | varchar(x), bigint, bigint | scalar | 1 | Substring of given length starting at an index |  |
| substring | varchar(x) | char(x), bigint | scalar | 1 | Suffix starting at given index |  |
| substring | varchar(x) | char(x), bigint, bigint | scalar | 1 | Substring of given length starting at an index |  |
| substring | varchar(x) | varchar(x), bigint | scalar | 1 | Suffix starting at given index |  |
| substring | varchar(x) | varchar(x), bigint, bigint | scalar | 1 | Substring of given length starting at an index |  |
| sum | bigint | bigint | aggregate | 1 |  |  |
| sum | decimal(38,s) | decimal(p,s) | aggregate | 1 | Calculates the sum over the input values |  |
| sum | double | double | aggregate | 1 |  |  |
| sum | interval day to second | interval day to second | aggregate | 1 |  |  |
| sum | interval year to month | interval year to month | aggregate | 1 |  |  |
| sum | real | real | aggregate | 1 |  |  |
| T |  |  |  | 0 |  |  |
| tan | double | double | scalar | 1 | Tangent |  |
| tanh | double | double | scalar | 1 | Hyperbolic tangent |  |
| tdigest_agg | tdigest | double | aggregate | 1 |  |  |
| tdigest_agg | tdigest | double, double | aggregate | 1 |  |  |
| timestamp_objectid | objectid | timestamp(0) with time zone | scalar | 1 | Mongodb ObjectId from the given timestamp |  |
| timezone_hour | bigint | time(p) with time zone | scalar | 1 | Time zone hour of the given time |  |
| timezone_hour | bigint | timestamp(p) with time zone | scalar | 1 | Time zone hour of the given timestamp |  |
| timezone_minute | bigint | time(p) with time zone | scalar | 1 | Time zone minute of the given time |  |
| timezone_minute | bigint | timestamp(p) with time zone | scalar | 1 | Time zone minute of the given timestamp |  |
| to_base | varchar(64) | bigint, bigint | scalar | 1 | Convert a number to a string in the given base |  |
| to_base64 | varchar | varbinary | scalar | 1 | Encode binary data as base64 |  |
| to_base64url | varchar | varbinary | scalar | 1 | Encode binary data as base64 using the URL safe alphabet |  |
| to_big_endian_32 | varbinary | integer | scalar | 1 | Encode value as a 32-bit 2’s complement big endian varbinary |  |
| to_big_endian_64 | varbinary | bigint | scalar | 1 | Encode value as a 64-bit 2’s complement big endian varbinary |  |
| to_char | varchar | timestamp(p) with time zone, varchar | scalar | 1 | Formats a timestamp |  |
| to_date | date | varchar, varchar | scalar | 1 | Converts a string to a DATE data type |  |
| to_date | varchar | timestamp | scalar | 1 | Returns the date part of the timestamp |  |
| to_date | varchar | timestamp with time zone | scalar | 1 | Returns the date part of the timestamp with time zone |  |
| to_date | varchar | varchar | scalar | 1 | Returns the date part of the timestamp string |  |
| to_encoded_polyline | varchar | geometry | scalar | 1 | Encodes a linestring or multipoint geometry to a polyline |  |
| to_geojson_geometry | varchar | sphericalgeography | scalar | 1 | Returns GeoJSON string based on the input spherical geography |  |
| to_geometry | geometry | sphericalgeography | scalar | 1 | Converts a SphericalGeography object to a Geometry object. |  |
| to_hex | varchar | varbinary | scalar | 1 | Encode binary data as hex |  |
| to_ieee754_32 | varbinary | real | scalar | 1 | Encode value as a big endian varbinary according to IEEE 754 single-precision floating-point format |  |
| to_ieee754_64 | varbinary | double | scalar | 1 | Encode value as a big endian varbinary according to IEEE 754 double-precision floating-point format |  |
| to_iso8601 | varchar(16) | date | scalar | 1 |  |  |
| to_iso8601 | varchar(n) | timestamp(p) | scalar | 1 |  |  |
| to_iso8601 | varchar(n) | timestamp(p) with time zone | scalar | 1 |  |  |
| to_milliseconds | bigint | interval day to second | scalar | 1 |  |  |
| to_spherical_geography | sphericalgeography | geometry | scalar | 1 | Converts a Geometry object to a SphericalGeography object |  |
| to_timestamp | timestamp(3) | varchar, varchar | scalar | 1 | Converts a string to a TIMESTAMP data type |  |
| to_unixtime | double | timestamp(p) with time zone | scalar | 1 |  |  |
| to_utc_timestamp | timestamp | timestamp, varchar | scalar | 1 | given timestamp in a timezone convert it to UTC |  |
| to_utc_timestamp | timestamp | varchar, varchar | scalar | 1 | given timestamp (in varchar) in a timezone convert it to UTC |  |
| to_utf8 | varbinary | varchar(x) | scalar | 1 | Encodes the string to UTF-8 |  |
| transform | array(U) | array(T), function(T,U) | scalar | 0 | Apply lambda to each element of the array |  |
| transform_keys | map(K2,V) | map(K1,V), function(K1,V,K2) | scalar | 0 | Apply lambda to each entry of the map and transform the key |  |
| transform_values | map(K,V2) | map(K,V1), function(K,V1,V2) | scalar | 0 | Apply lambda to each entry of the map and transform the value |  |
| translate | varchar | varchar(x), varchar(y), varchar(z) | scalar | 1 | Translate characters from the source string based on original and translations strings |  |
| trim | char(x) | char(x) | scalar | 1 | Removes whitespace from the beginning and end of a string |  |
| trim | char(x) | char(x), codepoints | scalar | 1 | Remove the longest string containing only given characters from the beginning and end of a string |  |
| trim | varchar(x) | varchar(x) | scalar | 1 | Removes whitespace from the beginning and end of a string |  |
| trim | varchar(x) | varchar(x), codepoints | scalar | 1 | Remove the longest string containing only given characters from the beginning and end of a string |  |
| truncate | decimal(p,s) | decimal(p,s), integer | scalar | 1 | Round to integer by dropping given number of digits after decimal point |  |
| truncate | decimal(rp,0) | decimal(p,s) | scalar | 1 | Round to integer by dropping digits after decimal point |  |
| truncate | double | double | scalar | 1 | Round to integer by dropping digits after decimal point |  |
| truncate | real | real | scalar | 1 | Round to integer by dropping digits after decimal point |  |
| typeof | varchar | t | scalar | 1 | Textual representation of expression type |  |
| U |  |  |  | 0 |  |  |
| unhex | varbinary | varchar | scalar | 1 | Converts Hexadecimal number to binary value |  |
| unix_timestamp | bigint |  | scalar | 1 | Gets current UNIX timestamp in seconds |  |
| upper | char(x) | char(x) | scalar | 1 | Converts the string to upper case |  |
| upper | varchar(x) | varchar(x) | scalar | 1 | Converts the string to upper case |  |
| url_decode | varchar(x) | varchar(x) | scalar | 1 | Unescape a URL-encoded string |  |
| url_encode | varchar(y) | varchar(x) | scalar | 1 | Escape a string for use in URL query parameter names and values |  |
| url_extract_fragment | varchar(x) | varchar(x) | scalar | 1 | Extract fragment from url |  |
| url_extract_host | varchar(x) | varchar(x) | scalar | 1 | Extract host from url |  |
| url_extract_parameter | varchar(x) | varchar(x), varchar(y) | scalar | 1 | Extract query parameter from url |  |
| url_extract_path | varchar(x) | varchar(x) | scalar | 1 | Extract part from url |  |
| url_extract_port | bigint | varchar(x) | scalar | 1 | Extract port from url |  |
| url_extract_protocol | varchar(x) | varchar(x) | scalar | 1 | Extract protocol from url |  |
| url_extract_query | varchar(x) | varchar(x) | scalar | 1 | Extract query from url |  |
| uuid | uuid |  | scalar | 0 | Generates a random UUID |  |
| V |  |  |  | 0 |  |  |
| value_at_quantile | bigint | qdigest(bigint), double | scalar | 1 | Given an input q between [0, 1], find the value whose rank in the sorted sequence of the n values represented by the qdigest is qn. |  |
| value_at_quantile | double | qdigest(double), double | scalar | 1 | Given an input q between [0, 1], find the value whose rank in the sorted sequence of the n values represented by the qdigest is qn. |  |
| value_at_quantile | double | tdigest, double | scalar | 1 | Given an input q between [0, 1], find the value whose rank in the sorted sequence of the n values represented by the tdigest is qn. |  |
| value_at_quantile | real | qdigest(real), double | scalar | 1 | Given an input q between [0, 1], find the value whose rank in the sorted sequence of the n values represented by the qdigest is qn. |  |
| values_at_quantiles | array(bigint) | qdigest(bigint), array(double) | scalar | 1 | For each input q between [0, 1], find the value whose rank in the sorted sequence of the n values represented by the qdigest is qn. |  |
| values_at_quantiles | array(double) | qdigest(double), array(double) | scalar | 1 | For each input q between [0, 1], find the value whose rank in the sorted sequence of the n values represented by the qdigest is qn. |  |
| values_at_quantiles | array(double) | tdigest, array(double) | scalar | 1 | For each input q between [0, 1], find the value whose rank in the sorted sequence of the n values represented by the tdigest is qn. |  |
| values_at_quantiles | array(real) | qdigest(real), array(double) | scalar | 1 | For each input q between [0, 1], find the value whose rank in the sorted sequence of the n values represented by the qdigest is qn. |  |
| var_pop | double | bigint | aggregate | 1 | Returns the population variance of the argument |  |
| var_pop | double | double | aggregate | 1 | Returns the population variance of the argument |  |
| var_samp | double | bigint | aggregate | 1 | Returns the sample variance of the argument |  |
| var_samp | double | double | aggregate | 1 | Returns the sample variance of the argument |  |
| variance | double | bigint | aggregate | 1 | Returns the sample variance of the argument |  |
| variance | double | double | aggregate | 1 | Returns the sample variance of the argument |  |
| W |  |  |  | 0 |  |  |
| week | bigint | date | scalar | 1 | Week of the year of the given date |  |
| week | bigint | timestamp(p) | scalar | 1 | Week of the year of the given timestamp |  |
| week | bigint | timestamp(p) with time zone | scalar | 1 | Week of the year of the given timestamp |  |
| week_of_year | bigint | date | scalar | 1 | Week of the year of the given date |  |
| week_of_year | bigint | timestamp(p) | scalar | 1 | Week of the year of the given timestamp |  |
| week_of_year | bigint | timestamp(p) with time zone | scalar | 1 | Week of the year of the given timestamp |  |
| weekofyear | bigint | timestamp | scalar | 1 | week of the year of the given string timestamp |  |
| weekofyear | bigint | timestamp with time zone | scalar | 1 | week of the year of the given string timestamp |  |
| weekofyear | bigint | varchar | scalar | 1 | week of the year of the given string timestamp |  |
| width_bucket | bigint | double, array(double) | scalar | 1 | The bucket number of a value given an array of bins |  |
| width_bucket | bigint | double, double, double, bigint | scalar | 1 | The bucket number of a value given a lower and upper bound and the number of buckets |  |
| wilson_interval_lower | double | bigint, bigint, double | scalar | 1 | Binomial confidence interval lower bound using Wilson score |  |
| wilson_interval_upper | double | bigint, bigint, double | scalar | 1 | Binomial confidence interval upper bound using Wilson score |  |
| with_timezone | timestamp(p) with time zone | timestamp(p), varchar(x) | scalar | 1 |  |  |
| word_stem | varchar(x) | varchar(x) | scalar | 1 | Returns the stem of a word in the English language |  |
| word_stem | varchar(x) | varchar(x), varchar(2) | scalar | 1 | Returns the stem of a word in the given language |  |
| X |  |  |  | 0 |  |  |
| xxhash64 | varbinary | varbinary | scalar | 1 | Compute xxhash64 hash |  |
| Y |  |  |  | 0 |  |  |
| year | bigint | date | scalar | 1 | Year of the given date |  |
| year | bigint | interval year to month | scalar | 1 | Year of the given interval |  |
| year | bigint | timestamp(p) | scalar | 1 | Year of the given timestamp |  |
| year | bigint | timestamp(p) with time zone | scalar | 1 | Year of the given timestamp |  |
| year | bigint | varchar | scalar | 1 | year of the given string timestamp |  |
| year_of_week | bigint | date | scalar | 1 | Year of the ISO week of the given date |  |
| year_of_week | bigint | timestamp(p) | scalar | 1 | Year of the ISO week of the given timestamp |  |
| year_of_week | bigint | timestamp(p) with time zone | scalar | 1 | Year of the ISO week of the given timestamp |  |
| yow | bigint | date | scalar | 1 | Year of the ISO week of the given date |  |
| yow | bigint | timestamp(p) | scalar | 1 | Year of the ISO week of the given timestamp |  |
| yow | bigint | timestamp(p) with time zone | scalar | 1 | Year of the ISO week of the given timestamp |  |
| Z |  |  |  | 0 |  |  |
| zip | array(row(T1,T2)) | array(T1), array(T2) | scalar | 1 | Merges the given arrays, element-wise, into a single array of rows. |  |
| zip | array(row(T1,T2,T3)) | array(T1), array(T2), array(T3) | scalar | 1 | Merges the given arrays, element-wise, into a single array of rows. |  |
| zip | array(row(T1,T2,T3,T4)) | array(T1), array(T2), array(T3), array(T4) | scalar | 1 | Merges the given arrays, element-wise, into a single array of rows. |  |
| zip | array(row(T1,T2,T3,T4,T5)) | array(T1), array(T2), array(T3), array(T4), array(T5) | scalar | 1 | Merges the given arrays, element-wise, into a single array of rows. |  |
| zip_with | array(R) | array(T), array(U), function(T,U,R) | scalar | 0 | Merge two arrays, element-wise, into a single array using the lambda function |  |