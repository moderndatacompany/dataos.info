# SQL Functions and Operators
This section provides a comprehensive overview of the SQL functions and operators that are natively supported by Minerva. These built-in functions and operators empower users to perform various data manipulation, aggregation, and computation tasks directly within the Minerva environment, enhancing the efficiency and flexibility of data analysis workflows.


Refer to the following sections for further details:

Alphabetical list of Minerva SQL Funcions
SQL Functions by Topic

## Aggregate

For more details, see {doc}`aggregate`

- `any_value`
- `approx_distinct`
- `approx_most_frequent`
- `approx_percentile`
- `approx_set()`
- `arbitrary`
- `array_agg`
- `avg`
- `bitwise_and_agg`
- `bitwise_or_agg`
- `bool_and`
- `bool_or`
- `checksum`
- `corr`
- `count`
- `count_if`
- `covar_pop`
- `covar_samp`
- `every`
- `geometric_mean`
- `histogram`
- `kurtosis`
- `map_agg`
- `map_union`
- `max`
- `max_by`
- `merge()`
- `min`
- `min_by`
- `multimap_agg`
- `numeric_histogram`
- `qdigest_agg()`
- `regr_intercept`
- `regr_slope`
- `skewness`
- `sum`
- `stddev`
- `stddev_pop`
- `stddev_samp`
- `tdigest_agg()`
- `variance`
- `var_pop`
- `var_samp`

## Array

For more details, see {doc}`array`

- `all_match`
- `any_match`
- `array_distinct`
- `array_except`
- `array_intersect`
- `array_join`
- `array_max`
- `array_min`
- `array_position`
- `array_remove`
- `array_sort`
- `array_union`
- `arrays_overlap`
- `cardinality`
- `combinations`
- `concat()`
- `contains`
- `element_at`
- `filter`
- `flatten`
- `ngrams`
- `none_match`
- `reduce`
- `repeat`
- `reverse()`
- `sequence`
- `shuffle`
- `slice`
- `transform`
- `trim_array`
- `zip`
- `zip_with`

## Binary

For more details, see {doc}`binary`

- `concat()`
- `crc32`
- `from_base32`
- `from_base64`
- `from_base64url`
- `from_big_endian_32`
- `from_big_endian_64`
- `from_hex`
- `from_ieee754_32`
- `from_ieee754_64`
- `hmac_md5`
- `hmac_sha1`
- `hmac_sha256`
- `hmac_sha512`
- `length()`
- `lpad()`
- `md5`
- `murmur3`
- `reverse()`
- `rpad()`
- `sha1`
- `sha256`
- `sha512`
- `spooky_hash_v2_32`
- `spooky_hash_v2_64`
- `substr()`
- `to_base32`
- `to_base64`
- `to_base64url`
- `to_big_endian_32`
- `to_big_endian_64`
- `to_hex`
- `to_ieee754_32`
- `to_ieee754_64`
- `xxhash64`

## Bitwise

For more details, see {doc}`bitwise`

- `bit_count`
- `bitwise_and`
- `bitwise_left_shift`
- `bitwise_not`
- `bitwise_or`
- `bitwise_right_shift`
- `bitwise_right_shift_arithmetic`
- `bitwise_xor`

## Color

For more details, see {doc}`color`

- `bar`
- `color`
- `render`
- `rgb`

## Comparison

For more details, see {doc}`comparison`

- `greatest`
- `least`

## Conditional

For more details, see {doc}`conditional`

- [case](case-expression)
- [coalesce](coalesce-function)
- [if](if-expression)
- [nullif](nullif-function)
- [try](try-function)

## Conversion

For more details, see {doc}`conversion`

- `cast`
- `format`
- `try_cast`
- `typeof`

## Date and time

For more details, see {doc}`datetime`

- {ref}`AT TIME ZONE <at-time-zone-operator>`
- {data}`current_date`
- {data}`current_time`
- {data}`current_timestamp`
- {data}`localtime`
- {data}`localtimestamp`
- `current_timezone`
- `date`
- `date_add`
- `date_diff`
- `date_format`
- `date_parse`
- `date_trunc`
- `format_datetime`
- `from_iso8601_date`
- `from_iso8601_timestamp`
- `from_unixtime`
- `from_unixtime_nanos`
- `human_readable_seconds`
- `last_day_of_month`
- `now`
- `parse_duration`
- `to_iso8601`
- `to_milliseconds`
- `to_unixtime`
- `with_timezone`

## Geospatial

For more details, see {doc}`geospatial`

- `bing_tile`
- `bing_tile_at`
- `bing_tile_coordinates`
- `bing_tile_polygon`
- `bing_tile_quadkey`
- `bing_tile_zoom_level`
- `bing_tiles_around`
- `convex_hull_agg`
- `from_encoded_polyline`
- `from_geojson_geometry`
- `geometry_from_hadoop_shape`
- `geometry_invalid_reason`
- `geometry_nearest_points`
- `geometry_to_bing_tiles`
- `geometry_union`
- `geometry_union_agg`
- `great_circle_distance`
- `line_interpolate_point`
- `line_locate_point`
- `simplify_geometry`
- `ST_Area`
- `ST_AsBinary`
- `ST_AsText`
- `ST_Boundary`
- `ST_Buffer`
- `ST_Centroid`
- `ST_Contains`
- `ST_ConvexHull`
- `ST_CoordDim`
- `ST_Crosses`
- `ST_Difference`
- `ST_Dimension`
- `ST_Disjoint`
- `ST_Distance`
- `ST_EndPoint`
- `ST_Envelope`
- `ST_Equals`
- `ST_ExteriorRing`
- `ST_Geometries`
- `ST_GeometryFromText`
- `ST_GeometryN`
- `ST_GeometryType`
- `ST_GeomFromBinary`
- `ST_InteriorRings`
- `ST_InteriorRingN`
- `ST_Intersects`
- `ST_Intersection`
- `ST_IsClosed`
- `ST_IsEmpty`
- `ST_IsSimple`
- `ST_IsRing`
- `ST_IsValid`
- `ST_Length`
- `ST_LineFromText`
- `ST_LineString`
- `ST_MultiPoint`
- `ST_NumGeometries`
- `ST_NumInteriorRing`
- `ST_NumPoints`
- `ST_Overlaps`
- `ST_Point`
- `ST_PointN`
- `ST_Points`
- `ST_Polygon`
- `ST_Relate`
- `ST_StartPoint`
- `ST_SymDifference`
- `ST_Touches`
- `ST_Union`
- `ST_Within`
- `ST_X`
- `ST_XMax`
- `ST_XMin`
- `ST_Y`
- `ST_YMax`
- `ST_YMin`
- `to_encoded_polyline`
- `to_geojson_geometry`
- `to_geometry`
- `to_spherical_geography`

## HyperLogLog

For more details, see {doc}`hyperloglog`

- `approx_set`
- `cardinality()`
- `empty_approx_set`
- `merge`

## JSON

For more details, see {doc}`json`

- `is_json_scalar`
- {ref}`json_array() <json-array>`
- `json_array_contains`
- `json_array_get`
- `json_array_length`
- {ref}`json_exists() <json-exists>`
- `json_extract`
- `json_extract_scalar`
- `json_format`
- `json_parse`
- {ref}`json_object() <json-object>`
- {ref}`json_query() <json-query>`
- `json_size`
- {ref}`json_value() <json-value>`

## Lambda

For more details, see {doc}`lambda`

- `any_match`
- `reduce_agg`
- `regexp_replace`
- `transform`

## Machine learning

For more details, see {doc}`ml`

- `classify`
- `features`
- `learn_classifier`
- `learn_libsvm_classifier`
- `learn_libsvm_regressor`
- `learn_regressor`
- `regress`

## Map

For more details, see {doc}`map`

- `cardinality`
- `element_at`
- `map`
- `map_concat`
- `map_entries`
- `map_filter`
- `map_from_entries`
- `map_keys`
- `map_values`
- `map_zip_with`
- `multimap_from_entries`
- `transform_keys`
- `transform_values`

## Math

For more details, see {doc}`math`

- `abs`
- `acos`
- `asin`
- `atan`
- `beta_cdf`
- `cbrt`
- `ceil`
- `cos`
- `cosh`
- `cosine_similarity`
- `degrees`
- `e`
- `exp`
- `floor`
- `from_base`
- `infinity`
- `inverse_beta_cdf`
- `inverse_normal_cdf`
- `is_finite`
- `is_nan`
- `ln`
- `log`
- `log2`
- `log10`
- `mod`
- `nan`
- `normal_cdf`
- `pi`
- `pow`
- `power`
- `radians`
- `rand`
- `random`
- `round`
- `sign`
- `sin`
- `sinh`
- `sqrt`
- `tan`
- `tanh`
- `to_base`
- `truncate`
- `width_bucket`
- `wilson_interval_lower`
- `wilson_interval_upper`

## Quantile digest

For more details, see {doc}`qdigest`

- `merge()`
- `qdigest_agg`
- `value_at_quantile`
- `values_at_quantiles`

## Regular expression

For more details, see {doc}`regexp`

- `regexp_count`
- `regexp_extract`
- `regexp_extract_all`
- `regexp_like`
- `regexp_position`
- `regexp_replace`
- `regexp_split`

## Row pattern recognition expressions

- {ref}`classifier <classifier-function>`
- {ref}`first <logical-navigation-functions>`
- {ref}`last <logical-navigation-functions>`
- {ref}`match_number <match-number-function>`
- {ref}`next <physical-navigation-functions>`
- {ref}`permute <permute-function>`
- {ref}`prev <physical-navigation-functions>`

## Session

For more details, see {doc}`session`

- {data}`current_catalog`
- `current_groups`
- {data}`current_schema`
- {data}`current_user`

## Set Digest

For more details, see {doc}`setdigest`

- `make_set_digest`
- `merge_set_digest`
- {ref}`cardinality() <setdigest-cardinality>`
- `intersection_cardinality`
- `jaccard_index`
- `hash_counts`

## String

For more details, see {doc}`string`

- `chr`
- `codepoint`
- `concat`
- `concat_ws`
- `format`
- `from_utf8`
- `hamming_distance`
- `length`
- `levenshtein_distance`
- `lower`
- `lpad`
- `ltrim`
- `luhn_check`
- `normalize`
- `position`
- `replace`
- `reverse`
- `rpad`
- `rtrim`
- `soundex`
- `split`
- `split_part`
- `split_to_map`
- `split_to_multimap`
- `starts_with`
- `strpos`
- `substr`
- `substring`
- `to_utf8`
- `translate`
- `trim`
- `upper`
- `word_stem`

## System

For more details, see {doc}`system`

- `version`

## T-Digest

For more details, see {doc}`tdigest`

- `merge()`
- `tdigest_agg`
- `value_at_quantile()`

## Teradata

For more details, see {doc}`teradata`

- `char2hexint`
- `index`
- `to_char`
- `to_timestamp`
- `to_date`

## URL

For more details, see {doc}`url`

- `url_decode`
- `url_encode`
- `url_extract_fragment`
- `url_extract_host`
- `url_extract_parameter`
- `url_extract_path`
- `url_extract_port`
- `url_extract_protocol`
- `url_extract_query`

## UUID

For more details, see {doc}`uuid`

- `uuid`

## Window

For more details, see {doc}`window`

- `cume_dist`
- `dense_rank`
- `first_value`
- `lag`
- `last_value`
- `lead`
- `nth_value`
- `ntile`
- `percent_rank`
- `rank`
- `row_number`
