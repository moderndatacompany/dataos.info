# SQL Functions and Operators
This section provides a comprehensive overview of the SQL functions and operators that are natively supported by Minerva. These built-in functions and operators empower users to perform various data manipulation, aggregation, and computation tasks directly within the Minerva environment, enhancing the efficiency and flexibility of data analysis workflows.


Refer to the following sections for further details:

[Minerva SQL Functions and Operators: Alphabetical Reference](functions_and_operators.md)


## Minerva SQL Functions by Topic

### **Aggregate**

For more details, see [aggregate function](./functions_and_operators/aggregate.md)

- [`any_value`](./functions_and_operators/aggregate.md#any_value)
- [`approx_distinct`](./functions_and_operators/aggregate.md#approx_distinct)
- [`approx_most_frequent`](./functions_and_operators/aggregate.md#approx_most_frequent)
- [`approx_percentile`](./functions_and_operators/aggregate.md#approx_percentile)
- [`approx_set`](./functions_and_operators/aggregate.md#approx_set)
- [`arbitrary`](./functions_and_operators/aggregate.md#arbitrary)
- [`array_agg`](./functions_and_operators/aggregate.md#array_agg)
- [`avg`](./functions_and_operators/aggregate.md#avg)
- [`bitwise_and_agg`](./functions_and_operators/aggregate.md#bitwise-aggregate-functions)
- [`bitwise_or_agg`](./functions_and_operators/aggregate.md#bitwise-aggregate-functions)
- [`bool_and`](./functions_and_operators/aggregate.md#bool)
- [`bool_or`](./functions_and_operators/aggregate.md#bool)
- [`checksum`](./functions_and_operators/aggregate.md#checksum)
- [`corr`](./functions_and_operators/aggregate.md#corr)
- [`count`](./functions_and_operators/aggregate.md#count)
- [`count_if`](./functions_and_operators/aggregate.md#count)
- [`covar_pop`](./functions_and_operators/aggregate.md#covar_pop)
- [`covar_samp`](./functions_and_operators/aggregate.md#covar_samp)
- [`every`](./functions_and_operators/aggregate.md#every)
- [`geometric_mean`](./functions_and_operators/aggregate.md#geometric_mean)
- [`histogram`](./functions_and_operators/aggregate.md#histogram)
- [`kurtosis`](./functions_and_operators/aggregate.md#kurtosis)
- ['list_agg](./functions_and_operators/aggregate.md#listagg)
- [`map_agg`](./functions_and_operators/aggregate.md#map_agg)
- [`map_union`](./functions_and_operators/aggregate.md#map_union)
- [`max`](./functions_and_operators/aggregate.md#max)
- [`max_by`](./functions_and_operators/aggregate.md#max_by)
- [`merge`](./functions_and_operators/aggregate.md#merge)
- [`min`](./functions_and_operators/aggregate.md#min)
- [`min_by`](./functions_and_operators/aggregate.md#min_by)
- [`multimap_agg`](./functions_and_operators/aggregate.md#multimap_agg)
- [`numeric_histogram`](./functions_and_operators/aggregate.md#numeric_histogram)
- [`qdigest_agg`](./functions_and_operators/aggregate.md#qdigest_agg)
- [`regr_intercept`](./functions_and_operators/aggregate.md#regr_intercept)
- [`regr_slope`](./functions_and_operators/aggregate.md#regr_slope)
- [`skewness`](./functions_and_operators/aggregate.md#skewness)
- [`sum`](./functions_and_operators/aggregate.md#sum)
- [`stddev`](./functions_and_operators/aggregate.md#stddev)
- [`stddev_pop`](./functions_and_operators/aggregate.md#stddev_pop)
- [`stddev_samp`](./functions_and_operators/aggregate.md#stddev_samp)
- [`tdigest_agg`](./functions_and_operators/aggregate.md#tdigest_agg)
- [`variance`](./functions_and_operators/aggregate.md#variance)
- [`var_pop`](./functions_and_operators/aggregate.md#var_pop)
- [`var_samp`](./functions_and_operators/aggregate.md#var_samp)
- [`reduce_agg`](./functions_and_operators/aggregate.md#reduce_agg)

### **Array**

For more details, see [`array`](./functions_and_operators/array.md)



- [`all_match`](./functions_and_operators/array.md#all_match)
- [`any_match`](./functions_and_operators/array.md#any_match)
- [`array_distinct`](./functions_and_operators/array.md#array_distinct)
- [`array_except`](./functions_and_operators/array.md#array_except)
- [`array_intersect`](./functions_and_operators/array.md#array_intersect)
- [`array_join`](./functions_and_operators/array.md#array_join)
- [`array_max`](./functions_and_operators/array.md#array_max)
- [`array_min`](./functions_and_operators/array.md#array_min)
- [`array_position`](./functions_and_operators/array.md#array_position)
- [`array_remove`](./functions_and_operators/array.md#array_remove)
- [`array_sort`](./functions_and_operators/array.md#array_sort)
- [`array_union`](./functions_and_operators/array.md#array_union)
- [`arrays_overlap`](./functions_and_operators/array.md#arrays_overlap)
- [`cardinality`](./functions_and_operators/array.md#cardinality)
- [`combinations`](./functions_and_operators/array.md#combinations)
- [`concat()`](./functions_and_operators/array.md#concat)
- [`contains`](./functions_and_operators/array.md#contains)
- [`element_at`](./functions_and_operators/array.md#element_at)
- [`filter`](./functions_and_operators/array.md#filter)
- [`flatten`](./functions_and_operators/array.md#flatten)
- [`ngrams`](./functions_and_operators/array.md#ngrams)
- [`none_match`](./functions_and_operators/array.md#none_match)
- [`reduce`](./functions_and_operators/array.md#reduce)
- [`repeat`](./functions_and_operators/array.md#repeat)
- [`reverse()`](./functions_and_operators/array.md#reverse)
- [`sequence`](./functions_and_operators/array.md#sequence)
- [`shuffle`](./functions_and_operators/array.md#shuffle)
- [`slice`](./functions_and_operators/array.md#slice)
- [`transform`](./functions_and_operators/array.md#transform)
- [`trim_array`](./functions_and_operators/array.md#trim_array)
- [`zip`](./functions_and_operators/array.md#zip)
- [`zip_with`](./functions_and_operators/array.md#zip_with)


### **Binary**

For more details, see [`binary`](./functions_and_operators/binary.md)


- [`concat()`](./functions_and_operators/binary.md#binary-operators)
- [`crc32`](./functions_and_operators/binary.md#hashing-function)
- [`from_base32`](./functions_and_operators/binary.md#base64-encoding-functions)
- [`from_base64`](./functions_and_operators/binary.md#base64-encoding-functions)
- [`from_base64url`](./functions_and_operators/binary.md#base64-encoding-functions)
- [`from_big_endian_32`](./functions_and_operators/binary.md#integer-encoding-functions)
- [`from_big_endian_64`](./functions_and_operators/binary.md#integer-encoding-functions)
- [`from_hex`](./functions_and_operators/binary.md#hex-encoding-functions)
- [`from_ieee754_32`](./functions_and_operators/binary.md#floating-point-encoding-functions)
- [`from_ieee754_64`](./functions_and_operators/binary.md#floating-point-encoding-functions)
- [`hmac_md5`](./functions_and_operators/binary.md#hmac-function)
- [`hmac_sha1`](./functions_and_operators/binary.md#hmac-function)
- [`hmac_sha256`](./functions_and_operators/binary.md#hmac-function)
- [`hmac_sha512`](./functions_and_operators/binary.md#hmac-function)
- [`length()`](./functions_and_operators/binary.md#binary-operators)
- [`lpad()`](./functions_and_operators/binary.md#binary-operators)
- [`md5`](./functions_and_operators/binary.md#hashing-function)
- [`murmur3`](./functions_and_operators/binary.md#hashing-function)
- [`reverse()`](./functions_and_operators/binary.md#binary-operators)
- [`rpad()`](./functions_and_operators/binary.md#binary-operators)
- [`sha1`](./functions_and_operators/binary.md#hashing-function)
- [`sha256`](./functions_and_operators/binary.md#hashing-function)
- [`sha512`](./functions_and_operators/binary.md#hashing-function)
- [`spooky_hash_v2_32`](./functions_and_operators/binary.md#hashing-function)
- [`spooky_hash_v2_64`](./functions_and_operators/binary.md#hashing-function)
- [`substr()`](./functions_and_operators/binary.md#binary-operators)
- [`to_base32`](./functions_and_operators/binary.md#hex-encoding-functions)
- [`to_base64`](./functions_and_operators/binary.md#base64-encoding-functions)
- [`to_base64url`](./functions_and_operators/binary.md#base64-encoding-functions)
- [`to_big_endian_32`](./functions_and_operators/binary.md#integer-encoding-functions)
- [`to_big_endian_64`](./functions_and_operators/binary.md#integer-encoding-functions)
- [`to_hex`](./functions_and_operators/binary.md#hex-encoding-functions)
- [`to_ieee754_32`](./functions_and_operators/binary.md#floating-point-encoding-functions)
- [`to_ieee754_64`](./functions_and_operators/binary.md#floating-point-encoding-functions)
- [`xxhash64`](./functions_and_operators/binary.md#hashing-function)


### **Bitwise**

For more details, see [`bitwise`](./functions_and_operators/bitwise.md)

- [`bit_count`](./functions_and_operators/bitwise.md#bit_count)
- [`bitwise_and`](./functions_and_operators/bitwise.md#bitwise_and)
- [`bitwise_left_shift`](./functions_and_operators/bitwise.md#bitwise_left_shift)
- [`bitwise_not`](./functions_and_operators/bitwise.md#bitwise_not)
- [`bitwise_or`](./functions_and_operators/bitwise.md#bitwise_or)
- [`bitwise_right_shift`](./functions_and_operators/bitwise.md#bitwise_right_shift)
- [`bitwise_right_shift_arithmetic`](./functions_and_operators/bitwise.md#bitwise_right_shift_arithmetic)
- [`bitwise_xor`](./functions_and_operators/bitwise.md#bitwise_xor)


### **Color**

For more details, see [`color`](./functions_and_operators/color.md)

- [`bar`](./functions_and_operators/color.md#bar)
- [`color`](./functions_and_operators/color.md#color)
- [`render`](./functions_and_operators/color.md#render)
- [`rgb`](./functions_and_operators/color.md#rgb)

### **Comparison**

For more details, see [`comparison`](./functions_and_operators/comparison.md)

- [`greatest`](./functions_and_operators/comparison.md#greatest)
- [`least`](./functions_and_operators/comparison.md#least)

### **Conditional**

For more details, see [`conditional`](./functions_and_operators/conditional.md)

- [`case`](./functions_and_operators/conditional.md#case)
- [`coalesce`](./functions_and_operators/conditional.md#coalesce)
- [`if`](./functions_and_operators/conditional.md#if)
- [`nullif`](./functions_and_operators/conditional.md#nullif)
- [`try`](./functions_and_operators/conditional.md#try)

### **Conversion**

For more details, see [`conversion`](./functions_and_operators/conversion.md)

- [`cast`](./functions_and_operators/conversion.md#cast)
- [`format`](./functions_and_operators/conversion.md#format)
- [`try_cast`](./functions_and_operators/conversion.md#try_cast)
- [`typeof`](./functions_and_operators/conversion.md#typeof)

### **Date and time**

For more details, see [`date and time`](./functions_and_operators/datetime.md)

- [`AT TIME ZONE`](./functions_and_operators/datetime.md#at-time-zone-operator)
- [`current_date`](./functions_and_operators/datetime.md#current_date)
- [`current_time`](./functions_and_operators/datetime.md#current_time)
- [`current_timestamp`](./functions_and_operators/datetime.md#current_timestamp)
- [`localtime`](./functions_and_operators/datetime.md#localtime)
- [`localtimestamp`](./functions_and_operators/datetime.md#localtimestamp)
- [`current_timezone`](./functions_and_operators/datetime.md#current_timezone)
- [`date`](./functions_and_operators/datetime.md#date)
- [`date_add`](./functions_and_operators/datetime.md#date_add)
- [`date_diff`](./functions_and_operators/datetime.md#date_diff)
- [`date_format`](./functions_and_operators/datetime.md#date_format)
- [`date_parse`](./functions_and_operators/datetime.md#date_parse)
- [`date_trunc`](./functions_and_operators/datetime.md#date_trunc)
- [`format_datetime`](./functions_and_operators/datetime.md#format_datetime(timestamp, format))




### **HyperLogLog**

For more details, see [`hyperloglog`](./functions_and_operators/hyperloglog.md)

- [`approx_set`](./functions_and_operators/aggregate.md#approx_set)
- [`cardinality()`](./functions_and_operators/hyperloglog.md#cardinality)
- [`empty_approx_set`](./functions_and_operators/hyperloglog.md#empty_approx_set)
- [`merge`](./functions_and_operators/aggregate.md#merge)



### **Lambda**

For more details, see [`lambda`](./functions_and_operators/lambda.md)

- [`any_match`](./functions_and_operators/lambda.md#any_match)
- [`reduce_agg`](./functions_and_operators/lambda.md#reduce_agg)
- [`regexp_replace`](./functions_and_operators/lambda.md#regexp_replace)
- [`transform`](./functions_and_operators/lambda.md#transform)

### **Machine Learning**

For more details, see [`machine learning`](./functions_and_operators/machine_learning.md)

- [`classify`](./functions_and_operators/machine_learning.md#classify)
- [`features`](./functions_and_operators/machine_learning.md#features)
- [`learn_classifier`](./functions_and_operators/machine_learning.md#learn_classifier)
- [`learn_libsvm_classifier`](./functions_and_operators/machine_learning.md#learn_libsvm_classifier)
- [`learn_libsvm_regressor`](./functions_and_operators/machine_learning.md#learn_libsvm_regressor)
- [`learn_regressor`](./functions_and_operators/machine_learning.md#learn_regressor)
- [`regress`](./functions_and_operators/machine_learning.md#regress)

### **Map**

For more details,see [`map`](./functions_and_operators/map.md)

- [`cardinality`](./functions_and_operators/map.md#cardinality)
- [`element_at`](./functions_and_operators/map.md#element_at)
- [`map`](./functions_and_operators/map.md#map)
- [`map_concat`](./functions_and_operators/map.md#map_concat)
- [`map_entries`](./functions_and_operators/map.md#map_entries)
- [`map_filter`](./functions_and_operators/map.md#map_filter)
- [`map_from_entries`](./functions_and_operators/map.md#map_from_entries)
- [`map_keys`](./functions_and_operators/map.md#map_keys)
- [`map_values`](./functions_and_operators/map.md#map_values)
- [`map_zip_with`](./functions_and_operators/map.md#map_zip_with)
- [`multimap_from_entries`](./functions_and_operators/map.md#multimap_from_entries)
- [`transform_keys`](./functions_and_operators/map.md#transform_keys)
- [`transform_values`](./functions_and_operators/map.md#transform_values)

### **Math**

For more details, see [`maths`](./functions_and_operators/math.md#abs)

- [`acos`](./functions_and_operators/math.md#acos)
- [`asin`](./functions_and_operators/math.md#asin)
- [`atan`](./functions_and_operators/math.md#atan)
- [`beta_cdf`](./functions_and_operators/math.md#beta_cdf)
- [`cbrt`](./functions_and_operators/math.md#cbrt)
- [`ceil`](./functions_and_operators/math.md#ceil)
- [`cos`](./functions_and_operators/math.md#cos)
- [`cosh`](./functions_and_operators/math.md#cosh)
- [`cosine_similarity`](./functions_and_operators/math.md#cosine_similarity)
- [`degrees`](./functions_and_operators/math.md#degrees)
- [`e`](./functions_and_operators/math.md#e)
- [`exp`](./functions_and_operators/math.md#exp)
- [`floor`](./functions_and_operators/math.md#floor)
- [`from_base`](./functions_and_operators/math.md#from_base)
- [`infinity`](./functions_and_operators/math.md#infinity)
- [`inverse_beta_cdf`](./functions_and_operators/math.md#inverse_beta_cdf)
- [`inverse_normal_cdf`](./functions_and_operators/math.md#inverse_normal_cdf)
- [`is_finite`](./functions_and_operators/math.md#is_finite)
- [`is_nan`](./functions_and_operators/math.md#is_nan)
- [`ln`](./functions_and_operators/math.md#ln)
- [`log`](./functions_and_operators/math.md#log)
- [`log2`](./functions_and_operators/math.md#log2)
- [`log10`](./functions_and_operators/math.md#log10)
- [`mod`](./functions_and_operators/math.md#mod)
- [`nan`](./functions_and_operators/math.md#nan)
- [`normal_cdf`](./functions_and_operators/math.md#normal_cdf)
- [`pi`](./functions_and_operators/math.md#pi)
- [`pow`](./functions_and_operators/math.md#pow)
- [`power`](./functions_and_operators/math.md#power)
- [`radians`](./functions_and_operators/math.md#radians)
- [`rand`](./functions_and_operators/math.md#rand)
- [`random`](./functions_and_operators/math.md#random)
- [`round`](./functions_and_operators/math.md#round)
- [`sign`](./functions_and_operators/math.md#sign)
- [`sin`](./functions_and_operators/math.md#sin)
- [`sinh`](./functions_and_operators/math.md#sinh)
- [`sqrt`](./functions_and_operators/math.md#sqrt)
- [`tan`](./functions_and_operators/math.md#tan)
- [`tanh`](./functions_and_operators/math.md#tanh)
- [`to_base`](./functions_and_operators/math.md#to_base)
- [`truncate`](./functions_and_operators/math.md#truncate)
- [`width_bucket`](./functions_and_operators/math.md#width_bucket)
- [`wilson_interval_lower`](./functions_and_operators/math.md#wilson_interval_lower)
- [`wilson_interval_upper`](./functions_and_operators/math.md#wilson_interval_upper)

### **Quantile Digest**

For more details, see [`quantile digest`](./functions_and_operators/quantile_digest.md)

- [`merge()`](./functions_and_operators/quantile_digest.md#merge)
- [`qdigest_agg`](./functions_and_operators/quantile_digest.md#qdigest_agg)
- [`value_at_quantile`](./functions_and_operators/quantile_digest.md#value_at_quantile)
- [`values_at_quantiles`](./functions_and_operators/quantile_digest.md#values_at_quantiles)


### **Regular Expression**

For more details, see [`regular expression`](./functions_and_operators/regular_expression.md)

- [`regexp_count`](./functions_and_operators/regular_expression.md#regexp_count)
- [`regexp_extract`](./functions_and_operators/regular_expression.md#regexp_extract)
- [`regexp_extract_all`](./functions_and_operators/regular_expression.md#regexp_extract_all)
- [`regexp_like`](./functions_and_operators/regular_expression.md#regexp_like)
- [`regexp_position`](./functions_and_operators/regular_expression.md#regexp_position)
- [`regexp_replace`](./functions_and_operators/regular_expression.md#regexp_replace)
- [`regexp_split`](./functions_and_operators/regular_expression.md#regexp_split)



### **Session**

For more details, see [`session`](./functions_and_operators/session_information.md)

- [`current_catalog`](./functions_and_operators/session_information.md#current_catalog)
- [`current_groups`](./functions_and_operators/session_information.md#current_groups)
- [`current_schema`](./functions_and_operators/session_information.md#current_schema)
- [`current_user`](./functions_and_operators/session_information.md#current_user)


### **Set Digest**

For more details, see [`setdigest`](./functions_and_operators/set_digest.md)

- [`make_set_digest`](./functions_and_operators/set_digest.md#make_set_digest)
- [`merge_set_digest`](./functions_and_operators/set_digest.md#merge_set_digest)
- [`cardinality`](./functions_and_operators/set_digest.md#cardinality)
- [`intersection_cardinality`](./functions_and_operators/set_digest.md#intersection_cardinality)
- [`jaccard_index`](./functions_and_operators/set_digest.md#jaccard_index)
- [`hash_counts`](./functions_and_operators/set_digest.md#hash_counts)


### **String**

For more details, see [`string`](./functions_and_operators/string.md)

- [`chr`](./functions_and_operators/string.md#chr)
- [`codepoint`](./functions_and_operators/string.md#codepoint)
- [`concat`](./functions_and_operators/string.md#concat)
- [`concat_ws`](./functions_and_operators/string.md#concat_ws)
- [`format`](./functions_and_operators/string.md#format)
- [`from_utf8`](./functions_and_operators/string.md#from_utf8)
- [`hamming_distance`](./functions_and_operators/string.md#hamming_distance)
- [`length`](./functions_and_operators/string.md#length)
- [`levenshtein_distance`](./functions_and_operators/string.md#levenshtein_distance)
- [`lower`](./functions_and_operators/string.md#lower)
- [`lpad`](./functions_and_operators/string.md#lpad)
- [`ltrim`](./functions_and_operators/string.md#ltrim)
- [`luhn_check`](./functions_and_operators/string.md#luhn_check)
- [`normalize`](./functions_and_operators/string.md#normalize)
- [`position`](./functions_and_operators/string.md#position)
- [`replace`](./functions_and_operators/string.md#replace)
- [`reverse`](./functions_and_operators/string.md#reverse)
- [`rpad`](./functions_and_operators/string.md#rpad)
- [`rtrim`](./functions_and_operators/string.md#rtrim)
- [`soundex`](./functions_and_operators/string.md#soundex)
- [`split`](./functions_and_operators/string.md#split)
- [`split_part`](./functions_and_operators/string.md#split_part)
- [`split_to_map`](./functions_and_operators/string.md#split_to_map)
- [`split_to_multimap`](./functions_and_operators/string.md#split_to_multimap)
- [`starts_with`](./functions_and_operators/string.md#starts_with)
- [`strpos`](./functions_and_operators/string.md#strpos)
- [`substr`](./functions_and_operators/string.md#substr)
- [`substring`](./functions_and_operators/string.md#substring)
- [`to_utf8`](./functions_and_operators/string.md#to_utf8)
- [`translate`](./functions_and_operators/string.md#translate)
- [`trim`](./functions_and_operators/string.md#trim)
- [`upper`](./functions_and_operators/string.md#upper)
- [`word_stem`](./functions_and_operators/string.md#word_stem)

### **System**

For more details, see [`system`](./functions_and_operators/system.md)

- [`version`](./functions_and_operators/system.md#version)

### **T-Digest**

For more details, see [`tdigest`](./functions_and_operators/t_digest.md)

- [`merge()`](./functions_and_operators/t_digest.md#merge)
- [`tdigest_agg`](./functions_and_operators/t_digest.md#tdigest_agg)
- [`value_at_quantile()`](./functions_and_operators/t_digest.md#value_at_quantile)


### **Teradata**

For more details, see [`teradata`](./functions_and_operators/teradata.md)

- [`char2hexint`](./functions_and_operators/teradata.md#char2hexint)
- [`index`](./functions_and_operators/teradata.md#index)
- [`to_char`](./functions_and_operators/teradata.md#to_char)
- [`to_timestamp`](./functions_and_operators/teradata.md#to_timestamp)
- [`to_date`](./functions_and_operators/teradata.md#to_date)


### **URL**

For more details, see [`url`](./functions_and_operators/url.md)

- [`url_decode`](./functions_and_operators/url.md#url_decode)
- [`url_encode`](./functions_and_operators/url.md#url_encode)
- [`url_extract_fragment`](./functions_and_operators/url.md#url_extract_fragment)
- [`url_extract_host`](./functions_and_operators/url.md#url_extract_host)
- [`url_extract_parameter`](./functions_and_operators/url.md#url_extract_parameter)
- [`url_extract_path`](./functions_and_operators/url.md#url_extract_path)
- [`url_extract_port`](./functions_and_operators/url.md#url_extract_port)
- [`url_extract_protocol`](./functions_and_operators/url.md#url_extract_protocol)
- [`url_extract_query`](./functions_and_operators/url.md#url_extract_query)


### **UUID**

For more details, see [`uuid`](./functions_and_operators/uuid.md)

- [`uuid`](./functions_and_operators/uuid.md#uuid)

### **Window**

For more details, see [`window`](./functions_and_operators/window.md)

- [`cume_dist`](./functions_and_operators/window.md#cume_dist)
- [`dense_rank`](./functions_and_operators/window.md#dense_rank)
- [`first_value`](./functions_and_operators/window.md#first_value)
- [`lag`](./functions_and_operators/window.md#lag)
- [`last_value`](./functions_and_operators/window.md#last_value)
- [`lead`](./functions_and_operators/window.md#lead)
- [`nth_value`](./functions_and_operators/window.md#nth_value)
- [`ntile`](./functions_and_operators/window.md#ntile)
- [`percent_rank`](./functions_and_operators/window.md#percent_rank)
- [`rank`](./functions_and_operators/window.md#rank)
- [`row_number`](./functions_and_operators/window.md#row_number)

