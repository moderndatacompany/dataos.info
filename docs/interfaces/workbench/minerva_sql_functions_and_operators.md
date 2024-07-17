# SQL Functions and Operators
This section provides a comprehensive overview of the SQL functions and operators that are natively supported by Minerva. These built-in functions and operators empower users to perform various data manipulation, aggregation, and computation tasks directly within the Minerva environment, enhancing the efficiency and flexibility of data analysis workflows.


Refer to the following sections for further details:

[Minerva SQL Functions and Operators: Alphabetical Reference](/interfaces/workbench/functions_and_operators)


## Minerva SQL Functions by Topic

### **Aggregate**

For more details, see [aggregate function](/interfaces/workbench/functions_and_operators/aggregate)

- [`any_value`](/interfaces/workbench/functions_and_operators/aggregate#any_value)
- [`approx_distinct`](/interfaces/workbench/functions_and_operators/aggregate#approx_distinct)
- [`approx_most_frequent`](/interfaces/workbench/functions_and_operators/aggregate#approx_most_frequent)
- [`approx_percentile`](/interfaces/workbench/functions_and_operators/aggregate#approx_percentile)
- [`approx_set`](/interfaces/workbench/functions_and_operators/aggregate#approx_set)
- [`arbitrary`](/interfaces/workbench/functions_and_operators/aggregate#arbitrary)
- [`array_agg`](/interfaces/workbench/functions_and_operators/aggregate#array_agg)
- [`avg`](/interfaces/workbench/functions_and_operators/aggregate#avg)
- [`bitwise_and_agg`](/interfaces/workbench/functions_and_operators/aggregate#bitwise-aggregate-functions)
- [`bitwise_or_agg`](/interfaces/workbench/functions_and_operators/aggregate#bitwise-aggregate-functions)
- [`bool_and`](/interfaces/workbench/functions_and_operators/aggregate#bool)
- [`bool_or`](/interfaces/workbench/functions_and_operators/aggregate#bool)
- [`checksum`](/interfaces/workbench/functions_and_operators/aggregate#checksum)
- [`corr`](/interfaces/workbench/functions_and_operators/aggregate#corr)
- [`count`](/interfaces/workbench/functions_and_operators/aggregate#count)
- [`count_if`](/interfaces/workbench/functions_and_operators/aggregate#count)
- [`covar_pop`](/interfaces/workbench/functions_and_operators/aggregate#covar_pop)
- [`covar_samp`](/interfaces/workbench/functions_and_operators/aggregate#covar_samp)
- [`every`](/interfaces/workbench/functions_and_operators/aggregate#every)
- [`geometric_mean`](/interfaces/workbench/functions_and_operators/aggregate#geometric_mean)
- [`histogram`](/interfaces/workbench/functions_and_operators/aggregate#histogram)
- [`kurtosis`](/interfaces/workbench/functions_and_operators/aggregate#kurtosis)
- ['list_agg](/interfaces/workbench/functions_and_operators/aggregate#listagg)
- [`map_agg`](/interfaces/workbench/functions_and_operators/aggregate#map_agg)
- [`map_union`](/interfaces/workbench/functions_and_operators/aggregate#map_union)
- [`max`](/interfaces/workbench/functions_and_operators/aggregate#max)
- [`max_by`](/interfaces/workbench/functions_and_operators/aggregate#max_by)
- [`merge`](/interfaces/workbench/functions_and_operators/aggregate#merge)
- [`min`](/interfaces/workbench/functions_and_operators/aggregate#min)
- [`min_by`](/interfaces/workbench/functions_and_operators/aggregate#min_by)
- [`multimap_agg`](/interfaces/workbench/functions_and_operators/aggregate#multimap_agg)
- [`numeric_histogram`](/interfaces/workbench/functions_and_operators/aggregate#numeric_histogram)
- [`qdigest_agg`](/interfaces/workbench/functions_and_operators/aggregate#qdigest_agg)
- [`regr_intercept`](/interfaces/workbench/functions_and_operators/aggregate#regr_intercept)
- [`regr_slope`](/interfaces/workbench/functions_and_operators/aggregate#regr_slope)
- [`skewness`](/interfaces/workbench/functions_and_operators/aggregate#skewness)
- [`sum`](/interfaces/workbench/functions_and_operators/aggregate#sum)
- [`stddev`](/interfaces/workbench/functions_and_operators/aggregate#stddev)
- [`stddev_pop`](/interfaces/workbench/functions_and_operators/aggregate#stddev_pop)
- [`stddev_samp`](/interfaces/workbench/functions_and_operators/aggregate#stddev_samp)
- [`tdigest_agg`](/interfaces/workbench/functions_and_operators/aggregate#tdigest_agg)
- [`variance`](/interfaces/workbench/functions_and_operators/aggregate#variance)
- [`var_pop`](/interfaces/workbench/functions_and_operators/aggregate#var_pop)
- [`var_samp`](/interfaces/workbench/functions_and_operators/aggregate#var_samp)
- [`reduce_agg`](/interfaces/workbench/functions_and_operators/aggregate#reduce_agg)

### **Array**

For more details, see [`array`](/interfaces/workbench/functions_and_operators/array)



- [`all_match`](/interfaces/workbench/functions_and_operators/array#all_match)
- [`any_match`](/interfaces/workbench/functions_and_operators/array#any_match)
- [`array_distinct`](/interfaces/workbench/functions_and_operators/array#array_distinct)
- [`array_except`](/interfaces/workbench/functions_and_operators/array#array_except)
- [`array_intersect`](/interfaces/workbench/functions_and_operators/array#array_intersect)
- [`array_join`](/interfaces/workbench/functions_and_operators/array#array_join)
- [`array_max`](/interfaces/workbench/functions_and_operators/array#array_max)
- [`array_min`](/interfaces/workbench/functions_and_operators/array#array_min)
- [`array_position`](/interfaces/workbench/functions_and_operators/array#array_position)
- [`array_remove`](/interfaces/workbench/functions_and_operators/array#array_remove)
- [`array_sort`](/interfaces/workbench/functions_and_operators/array#array_sort)
- [`array_union`](/interfaces/workbench/functions_and_operators/array#array_union)
- [`arrays_overlap`](/interfaces/workbench/functions_and_operators/array#arrays_overlap)
- [`cardinality`](/interfaces/workbench/functions_and_operators/array#cardinality)
- [`combinations`](/interfaces/workbench/functions_and_operators/array#combinations)
- [`concat()`](/interfaces/workbench/functions_and_operators/array#concat)
- [`contains`](/interfaces/workbench/functions_and_operators/array#contains)
- [`element_at`](/interfaces/workbench/functions_and_operators/array#element_at)
- [`filter`](/interfaces/workbench/functions_and_operators/array#filter)
- [`flatten`](/interfaces/workbench/functions_and_operators/array#flatten)
- [`ngrams`](/interfaces/workbench/functions_and_operators/array#ngrams)
- [`none_match`](/interfaces/workbench/functions_and_operators/array#none_match)
- [`reduce`](/interfaces/workbench/functions_and_operators/array#reduce)
- [`repeat`](/interfaces/workbench/functions_and_operators/array#repeat)
- [`reverse()`](/interfaces/workbench/functions_and_operators/array#reverse)
- [`sequence`](/interfaces/workbench/functions_and_operators/array#sequence)
- [`shuffle`](/interfaces/workbench/functions_and_operators/array#shuffle)
- [`slice`](/interfaces/workbench/functions_and_operators/array#slice)
- [`transform`](/interfaces/workbench/functions_and_operators/array#transform)
- [`trim_array`](/interfaces/workbench/functions_and_operators/array#trim_array)
- [`zip`](/interfaces/workbench/functions_and_operators/array#zip)
- [`zip_with`](/interfaces/workbench/functions_and_operators/array#zip_with)


### **Binary**

For more details, see [`binary`](/interfaces/workbench/functions_and_operators/binary)


- [`concat()`](/interfaces/workbench/functions_and_operators/binary#binary-operators)
- [`crc32`](/interfaces/workbench/functions_and_operators/binary#hashing-function)
- [`from_base32`](/interfaces/workbench/functions_and_operators/binary#base64-encoding-functions)
- [`from_base64`](/interfaces/workbench/functions_and_operators/binary#base64-encoding-functions)
- [`from_base64url`](/interfaces/workbench/functions_and_operators/binary#base64-encoding-functions)
- [`from_big_endian_32`](/interfaces/workbench/functions_and_operators/binary#integer-encoding-functions)
- [`from_big_endian_64`](/interfaces/workbench/functions_and_operators/binary#integer-encoding-functions)
- [`from_hex`](/interfaces/workbench/functions_and_operators/binary#hex-encoding-functions)
- [`from_ieee754_32`](/interfaces/workbench/functions_and_operators/binary#floating-point-encoding-functions)
- [`from_ieee754_64`](/interfaces/workbench/functions_and_operators/binary#floating-point-encoding-functions)
- [`hmac_md5`](/interfaces/workbench/functions_and_operators/binary#hmac-function)
- [`hmac_sha1`](/interfaces/workbench/functions_and_operators/binary#hmac-function)
- [`hmac_sha256`](/interfaces/workbench/functions_and_operators/binary#hmac-function)
- [`hmac_sha512`](/interfaces/workbench/functions_and_operators/binary#hmac-function)
- [`length()`](/interfaces/workbench/functions_and_operators/binary#binary-operators)
- [`lpad()`](/interfaces/workbench/functions_and_operators/binary#binary-operators)
- [`md5`](/interfaces/workbench/functions_and_operators/binary#hashing-function)
- [`murmur3`](/interfaces/workbench/functions_and_operators/binary#hashing-function)
- [`reverse()`](/interfaces/workbench/functions_and_operators/binary#binary-operators)
- [`rpad()`](/interfaces/workbench/functions_and_operators/binary#binary-operators)
- [`sha1`](/interfaces/workbench/functions_and_operators/binary#hashing-function)
- [`sha256`](/interfaces/workbench/functions_and_operators/binary#hashing-function)
- [`sha512`](/interfaces/workbench/functions_and_operators/binary#hashing-function)
- [`spooky_hash_v2_32`](/interfaces/workbench/functions_and_operators/binary#hashing-function)
- [`spooky_hash_v2_64`](/interfaces/workbench/functions_and_operators/binary#hashing-function)
- [`substr()`](/interfaces/workbench/functions_and_operators/binary#binary-operators)
- [`to_base32`](/interfaces/workbench/functions_and_operators/binary#hex-encoding-functions)
- [`to_base64`](/interfaces/workbench/functions_and_operators/binary#base64-encoding-functions)
- [`to_base64url`](/interfaces/workbench/functions_and_operators/binary#base64-encoding-functions)
- [`to_big_endian_32`](/interfaces/workbench/functions_and_operators/binary#integer-encoding-functions)
- [`to_big_endian_64`](/interfaces/workbench/functions_and_operators/binary#integer-encoding-functions)
- [`to_hex`](/interfaces/workbench/functions_and_operators/binary#hex-encoding-functions)
- [`to_ieee754_32`](/interfaces/workbench/functions_and_operators/binary#floating-point-encoding-functions)
- [`to_ieee754_64`](/interfaces/workbench/functions_and_operators/binary#floating-point-encoding-functions)
- [`xxhash64`](/interfaces/workbench/functions_and_operators/binary#hashing-function)


### **Bitwise**

For more details, see [`bitwise`](/interfaces/workbench/functions_and_operators/bitwise)

- [`bit_count`](/interfaces/workbench/functions_and_operators/bitwise#bit_count)
- [`bitwise_and`](/interfaces/workbench/functions_and_operators/bitwise#bitwise_and)
- [`bitwise_left_shift`](/interfaces/workbench/functions_and_operators/bitwise#bitwise_left_shift)
- [`bitwise_not`](/interfaces/workbench/functions_and_operators/bitwise#bitwise_not)
- [`bitwise_or`](/interfaces/workbench/functions_and_operators/bitwise#bitwise_or)
- [`bitwise_right_shift`](/interfaces/workbench/functions_and_operators/bitwise#bitwise_right_shift)
- [`bitwise_right_shift_arithmetic`](/interfaces/workbench/functions_and_operators/bitwise#bitwise_right_shift_arithmetic)
- [`bitwise_xor`](/interfaces/workbench/functions_and_operators/bitwise#bitwise_xor)


### **Color**

For more details, see [`color`](/interfaces/workbench/functions_and_operators/color)

- [`bar`](/interfaces/workbench/functions_and_operators/color#bar)
- [`color`](/interfaces/workbench/functions_and_operators/color#color)
- [`render`](/interfaces/workbench/functions_and_operators/color#render)
- [`rgb`](/interfaces/workbench/functions_and_operators/color#rgb)

### **Comparison**

For more details, see [`comparison`](/interfaces/workbench/functions_and_operators/comparison)

- [`greatest`](/interfaces/workbench/functions_and_operators/comparison#greatest)
- [`least`](/interfaces/workbench/functions_and_operators/comparison#least)

### **Conditional**

For more details, see [`conditional`](/interfaces/workbench/functions_and_operators/conditional)

- [`case`](/interfaces/workbench/functions_and_operators/conditional#case)
- [`coalesce`](/interfaces/workbench/functions_and_operators/conditional#coalesce)
- [`if`](/interfaces/workbench/functions_and_operators/conditional#if)
- [`nullif`](/interfaces/workbench/functions_and_operators/conditional#nullif)
- [`try`](/interfaces/workbench/functions_and_operators/conditional#try)

### **Conversion**

For more details, see [`conversion`](/interfaces/workbench/functions_and_operators/conversion)

- [`cast`](/interfaces/workbench/functions_and_operators/conversion#cast)
- [`format`](/interfaces/workbench/functions_and_operators/conversion#format)
- [`try_cast`](/interfaces/workbench/functions_and_operators/conversion#try_cast)
- [`typeof`](/interfaces/workbench/functions_and_operators/conversion#typeof)

### **Date and time**

For more details, see [`date and time`](/interfaces/workbench/functions_and_operators/datetime)

- [`AT TIME ZONE`](/interfaces/workbench/functions_and_operators/datetime#at-time-zone-operator)
- [`current_date`](/interfaces/workbench/functions_and_operators/datetime#current_date)
- [`current_time`](/interfaces/workbench/functions_and_operators/datetime#current_time)
- [`current_timestamp`](/interfaces/workbench/functions_and_operators/datetime#current_timestamp)
- [`localtime`](/interfaces/workbench/functions_and_operators/datetime#localtime)
- [`localtimestamp`](/interfaces/workbench/functions_and_operators/datetime#localtimestamp)
- [`current_timezone`](/interfaces/workbench/functions_and_operators/datetime#current_timezone)
- [`date`](/interfaces/workbench/functions_and_operators/datetime#date)
- [`date_add`](/interfaces/workbench/functions_and_operators/datetime#date_add)
- [`date_diff`](/interfaces/workbench/functions_and_operators/datetime#date_diff)
- [`date_format`](/interfaces/workbench/functions_and_operators/datetime#date_format)
- [`date_parse`](/interfaces/workbench/functions_and_operators/datetime#date_parse)
- [`date_trunc`](/interfaces/workbench/functions_and_operators/datetime#date_trunc)
- [`format_datetime`](/interfaces/workbench/functions_and_operators/datetime#format_datetime(timestamp, format))




### **HyperLogLog**

For more details, see [`hyperloglog`](/interfaces/workbench/functions_and_operators/hyperloglog)

- [`approx_set`](/interfaces/workbench/functions_and_operators/aggregate#approx_set)
- [`cardinality()`](/interfaces/workbench/functions_and_operators/hyperloglog#cardinality)
- [`empty_approx_set`](/interfaces/workbench/functions_and_operators/hyperloglog#empty_approx_set)
- [`merge`](/interfaces/workbench/functions_and_operators/aggregate#merge)



### **Lambda**

For more details, see [`lambda`](/interfaces/workbench/functions_and_operators/lambda)

- [`any_match`](/interfaces/workbench/functions_and_operators/lambda#any_match)
- [`reduce_agg`](/interfaces/workbench/functions_and_operators/lambda#reduce_agg)
- [`regexp_replace`](/interfaces/workbench/functions_and_operators/lambda#regexp_replace)
- [`transform`](/interfaces/workbench/functions_and_operators/lambda#transform)

### **Machine Learning**

For more details, see [`machine learning`](/interfaces/workbench/functions_and_operators/machine_learning)

- [`classify`](/interfaces/workbench/functions_and_operators/machine_learning#classify)
- [`features`](/interfaces/workbench/functions_and_operators/machine_learning#features)
- [`learn_classifier`](/interfaces/workbench/functions_and_operators/machine_learning#learn_classifier)
- [`learn_libsvm_classifier`](/interfaces/workbench/functions_and_operators/machine_learning#learn_libsvm_classifier)
- [`learn_libsvm_regressor`](/interfaces/workbench/functions_and_operators/machine_learning#learn_libsvm_regressor)
- [`learn_regressor`](/interfaces/workbench/functions_and_operators/machine_learning#learn_regressor)
- [`regress`](/interfaces/workbench/functions_and_operators/machine_learning#regress)

### **Map**

For more details,see [`map`](/interfaces/workbench/functions_and_operators/map)

- [`cardinality`](/interfaces/workbench/functions_and_operators/map#cardinality)
- [`element_at`](/interfaces/workbench/functions_and_operators/map#element_at)
- [`map`](/interfaces/workbench/functions_and_operators/map#map)
- [`map_concat`](/interfaces/workbench/functions_and_operators/map#map_concat)
- [`map_entries`](/interfaces/workbench/functions_and_operators/map#map_entries)
- [`map_filter`](/interfaces/workbench/functions_and_operators/map#map_filter)
- [`map_from_entries`](/interfaces/workbench/functions_and_operators/map#map_from_entries)
- [`map_keys`](/interfaces/workbench/functions_and_operators/map#map_keys)
- [`map_values`](/interfaces/workbench/functions_and_operators/map#map_values)
- [`map_zip_with`](/interfaces/workbench/functions_and_operators/map#map_zip_with)
- [`multimap_from_entries`](/interfaces/workbench/functions_and_operators/map#multimap_from_entries)
- [`transform_keys`](/interfaces/workbench/functions_and_operators/map#transform_keys)
- [`transform_values`](/interfaces/workbench/functions_and_operators/map#transform_values)

### **Math**

For more details, see [`maths`](/interfaces/workbench/functions_and_operators/math#abs)

- [`acos`](/interfaces/workbench/functions_and_operators/math#acos)
- [`asin`](/interfaces/workbench/functions_and_operators/math#asin)
- [`atan`](/interfaces/workbench/functions_and_operators/math#atan)
- [`beta_cdf`](/interfaces/workbench/functions_and_operators/math#beta_cdf)
- [`cbrt`](/interfaces/workbench/functions_and_operators/math#cbrt)
- [`ceil`](/interfaces/workbench/functions_and_operators/math#ceil)
- [`cos`](/interfaces/workbench/functions_and_operators/math#cos)
- [`cosh`](/interfaces/workbench/functions_and_operators/math#cosh)
- [`cosine_similarity`](/interfaces/workbench/functions_and_operators/math#cosine_similarity)
- [`degrees`](/interfaces/workbench/functions_and_operators/math#degrees)
- [`e`](/interfaces/workbench/functions_and_operators/math#e)
- [`exp`](/interfaces/workbench/functions_and_operators/math#exp)
- [`floor`](/interfaces/workbench/functions_and_operators/math#floor)
- [`from_base`](/interfaces/workbench/functions_and_operators/math#from_base)
- [`infinity`](/interfaces/workbench/functions_and_operators/math#infinity)
- [`inverse_beta_cdf`](/interfaces/workbench/functions_and_operators/math#inverse_beta_cdf)
- [`inverse_normal_cdf`](/interfaces/workbench/functions_and_operators/math#inverse_normal_cdf)
- [`is_finite`](/interfaces/workbench/functions_and_operators/math#is_finite)
- [`is_nan`](/interfaces/workbench/functions_and_operators/math#is_nan)
- [`ln`](/interfaces/workbench/functions_and_operators/math#ln)
- [`log`](/interfaces/workbench/functions_and_operators/math#log)
- [`log2`](/interfaces/workbench/functions_and_operators/math#log2)
- [`log10`](/interfaces/workbench/functions_and_operators/math#log10)
- [`mod`](/interfaces/workbench/functions_and_operators/math#mod)
- [`nan`](/interfaces/workbench/functions_and_operators/math#nan)
- [`normal_cdf`](/interfaces/workbench/functions_and_operators/math#normal_cdf)
- [`pi`](/interfaces/workbench/functions_and_operators/math#pi)
- [`pow`](/interfaces/workbench/functions_and_operators/math#pow)
- [`power`](/interfaces/workbench/functions_and_operators/math#power)
- [`radians`](/interfaces/workbench/functions_and_operators/math#radians)
- [`rand`](/interfaces/workbench/functions_and_operators/math#rand)
- [`random`](/interfaces/workbench/functions_and_operators/math#random)
- [`round`](/interfaces/workbench/functions_and_operators/math#round)
- [`sign`](/interfaces/workbench/functions_and_operators/math#sign)
- [`sin`](/interfaces/workbench/functions_and_operators/math#sin)
- [`sinh`](/interfaces/workbench/functions_and_operators/math#sinh)
- [`sqrt`](/interfaces/workbench/functions_and_operators/math#sqrt)
- [`tan`](/interfaces/workbench/functions_and_operators/math#tan)
- [`tanh`](/interfaces/workbench/functions_and_operators/math#tanh)
- [`to_base`](/interfaces/workbench/functions_and_operators/math#to_base)
- [`truncate`](/interfaces/workbench/functions_and_operators/math#truncate)
- [`width_bucket`](/interfaces/workbench/functions_and_operators/math#width_bucket)
- [`wilson_interval_lower`](/interfaces/workbench/functions_and_operators/math#wilson_interval_lower)
- [`wilson_interval_upper`](/interfaces/workbench/functions_and_operators/math#wilson_interval_upper)

### **Quantile Digest**

For more details, see [`quantile digest`](/interfaces/workbench/functions_and_operators/quantile_digest)

- [`merge()`](/interfaces/workbench/functions_and_operators/quantile_digest#merge)
- [`qdigest_agg`](/interfaces/workbench/functions_and_operators/quantile_digest#qdigest_agg)
- [`value_at_quantile`](/interfaces/workbench/functions_and_operators/quantile_digest#value_at_quantile)
- [`values_at_quantiles`](/interfaces/workbench/functions_and_operators/quantile_digest#values_at_quantiles)


### **Regular Expression**

For more details, see [`regular expression`](/interfaces/workbench/functions_and_operators/regular_expression)

- [`regexp_count`](/interfaces/workbench/functions_and_operators/regular_expression#regexp_count)
- [`regexp_extract`](/interfaces/workbench/functions_and_operators/regular_expression#regexp_extract)
- [`regexp_extract_all`](/interfaces/workbench/functions_and_operators/regular_expression#regexp_extract_all)
- [`regexp_like`](/interfaces/workbench/functions_and_operators/regular_expression#regexp_like)
- [`regexp_position`](/interfaces/workbench/functions_and_operators/regular_expression#regexp_position)
- [`regexp_replace`](/interfaces/workbench/functions_and_operators/regular_expression#regexp_replace)
- [`regexp_split`](/interfaces/workbench/functions_and_operators/regular_expression#regexp_split)



### **Session**

For more details, see [`session`](/interfaces/workbench/functions_and_operators/session_information)

- [`current_catalog`](/interfaces/workbench/functions_and_operators/session_information#current_catalog)
- [`current_groups`](/interfaces/workbench/functions_and_operators/session_information#current_groups)
- [`current_schema`](/interfaces/workbench/functions_and_operators/session_information#current_schema)
- [`current_user`](/interfaces/workbench/functions_and_operators/session_information#current_user)


### **Set Digest**

For more details, see [`setdigest`](/interfaces/workbench/functions_and_operators/set_digest)

- [`make_set_digest`](/interfaces/workbench/functions_and_operators/set_digest#make_set_digest)
- [`merge_set_digest`](/interfaces/workbench/functions_and_operators/set_digest#merge_set_digest)
- [`cardinality`](/interfaces/workbench/functions_and_operators/set_digest#cardinality)
- [`intersection_cardinality`](/interfaces/workbench/functions_and_operators/set_digest#intersection_cardinality)
- [`jaccard_index`](/interfaces/workbench/functions_and_operators/set_digest#jaccard_index)
- [`hash_counts`](/interfaces/workbench/functions_and_operators/set_digest#hash_counts)


### **String**

For more details, see [`string`](/interfaces/workbench/functions_and_operators/string)

- [`chr`](/interfaces/workbench/functions_and_operators/string#chr)
- [`codepoint`](/interfaces/workbench/functions_and_operators/string#codepoint)
- [`concat`](/interfaces/workbench/functions_and_operators/string#concat)
- [`concat_ws`](/interfaces/workbench/functions_and_operators/string#concat_ws)
- [`format`](/interfaces/workbench/functions_and_operators/string#format)
- [`from_utf8`](/interfaces/workbench/functions_and_operators/string#from_utf8)
- [`hamming_distance`](/interfaces/workbench/functions_and_operators/string#hamming_distance)
- [`length`](/interfaces/workbench/functions_and_operators/string#length)
- [`levenshtein_distance`](/interfaces/workbench/functions_and_operators/string#levenshtein_distance)
- [`lower`](/interfaces/workbench/functions_and_operators/string#lower)
- [`lpad`](/interfaces/workbench/functions_and_operators/string#lpad)
- [`ltrim`](/interfaces/workbench/functions_and_operators/string#ltrim)
- [`luhn_check`](/interfaces/workbench/functions_and_operators/string#luhn_check)
- [`normalize`](/interfaces/workbench/functions_and_operators/string#normalize)
- [`position`](/interfaces/workbench/functions_and_operators/string#position)
- [`replace`](/interfaces/workbench/functions_and_operators/string#replace)
- [`reverse`](/interfaces/workbench/functions_and_operators/string#reverse)
- [`rpad`](/interfaces/workbench/functions_and_operators/string#rpad)
- [`rtrim`](/interfaces/workbench/functions_and_operators/string#rtrim)
- [`soundex`](/interfaces/workbench/functions_and_operators/string#soundex)
- [`split`](/interfaces/workbench/functions_and_operators/string#split)
- [`split_part`](/interfaces/workbench/functions_and_operators/string#split_part)
- [`split_to_map`](/interfaces/workbench/functions_and_operators/string#split_to_map)
- [`split_to_multimap`](/interfaces/workbench/functions_and_operators/string#split_to_multimap)
- [`starts_with`](/interfaces/workbench/functions_and_operators/string#starts_with)
- [`strpos`](/interfaces/workbench/functions_and_operators/string#strpos)
- [`substr`](/interfaces/workbench/functions_and_operators/string#substr)
- [`substring`](/interfaces/workbench/functions_and_operators/string#substring)
- [`to_utf8`](/interfaces/workbench/functions_and_operators/string#to_utf8)
- [`translate`](/interfaces/workbench/functions_and_operators/string#translate)
- [`trim`](/interfaces/workbench/functions_and_operators/string#trim)
- [`upper`](/interfaces/workbench/functions_and_operators/string#upper)
- [`word_stem`](/interfaces/workbench/functions_and_operators/string#word_stem)

### **System**

For more details, see [`system`](/interfaces/workbench/functions_and_operators/system)

- [`version`](/interfaces/workbench/functions_and_operators/system#version)

### **T-Digest**

For more details, see [`tdigest`](/interfaces/workbench/functions_and_operators/t_digest)

- [`merge()`](/interfaces/workbench/functions_and_operators/t_digest#merge)
- [`tdigest_agg`](/interfaces/workbench/functions_and_operators/t_digest#tdigest_agg)
- [`value_at_quantile()`](/interfaces/workbench/functions_and_operators/t_digest#value_at_quantile)


### **Teradata**

For more details, see [`teradata`](/interfaces/workbench/functions_and_operators/teradata)

- [`char2hexint`](/interfaces/workbench/functions_and_operators/teradata#char2hexint)
- [`index`](/interfaces/workbench/functions_and_operators/teradata#index)
- [`to_char`](/interfaces/workbench/functions_and_operators/teradata#to_char)
- [`to_timestamp`](/interfaces/workbench/functions_and_operators/teradata#to_timestamp)
- [`to_date`](/interfaces/workbench/functions_and_operators/teradata#to_date)


### **URL**

For more details, see [`url`](/interfaces/workbench/functions_and_operators/url)

- [`url_decode`](/interfaces/workbench/functions_and_operators/url#url_decode)
- [`url_encode`](/interfaces/workbench/functions_and_operators/url#url_encode)
- [`url_extract_fragment`](/interfaces/workbench/functions_and_operators/url#url_extract_fragment)
- [`url_extract_host`](/interfaces/workbench/functions_and_operators/url#url_extract_host)
- [`url_extract_parameter`](/interfaces/workbench/functions_and_operators/url#url_extract_parameter)
- [`url_extract_path`](/interfaces/workbench/functions_and_operators/url#url_extract_path)
- [`url_extract_port`](/interfaces/workbench/functions_and_operators/url#url_extract_port)
- [`url_extract_protocol`](/interfaces/workbench/functions_and_operators/url#url_extract_protocol)
- [`url_extract_query`](/interfaces/workbench/functions_and_operators/url#url_extract_query)


### **UUID**

For more details, see [`uuid`](/interfaces/workbench/functions_and_operators/uuid)

- [`uuid`](/interfaces/workbench/functions_and_operators/uuid#uuid)

### **Window**

For more details, see [`window`](/interfaces/workbench/functions_and_operators/window)

- [`cume_dist`](/interfaces/workbench/functions_and_operators/window#cume_dist)
- [`dense_rank`](/interfaces/workbench/functions_and_operators/window#dense_rank)
- [`first_value`](/interfaces/workbench/functions_and_operators/window#first_value)
- [`lag`](/interfaces/workbench/functions_and_operators/window#lag)
- [`last_value`](/interfaces/workbench/functions_and_operators/window#last_value)
- [`lead`](/interfaces/workbench/functions_and_operators/window#lead)
- [`nth_value`](/interfaces/workbench/functions_and_operators/window#nth_value)
- [`ntile`](/interfaces/workbench/functions_and_operators/window#ntile)
- [`percent_rank`](/interfaces/workbench/functions_and_operators/window#percent_rank)
- [`rank`](/interfaces/workbench/functions_and_operators/window#rank)
- [`row_number`](/interfaces/workbench/functions_and_operators/window#row_number)

