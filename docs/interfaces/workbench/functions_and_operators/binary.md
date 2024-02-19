# Binary functions and operators
    
## Binary operators


| Function                       | Description                                                                                                          | Return Type |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| `concat(binary1, ..., binaryN)` | Returns the concatenation of `binary1`, `binary2`, ..., `binaryN`. This function provides the same functionality as the SQL-standard concatenation operator!!(). |              `varbinary`  |
| `length(binary)`               | Returns the length of `binary` in bytes.                                                                             | `bigint`     |
| `lpad(binary, size, padbinary)`| Left pads `binary` to `size` bytes with `padbinary`. If `size` is less than the length of `binary`, the result is truncated to `size` characters. `size` must not be negative, and `padbinary` must be non-empty. | `varbinary`  |
| `rpad(binary, size, padbinary)`| Right pads `binary` to `size` bytes with `padbinary`. If `size` is less than the length of `binary`, the result is truncated to `size` characters. `size` must not be negative, and `padbinary` must be non-empty. | `varbinary`  |
| `substr(binary, start)`        | Returns the rest of `binary` from the starting position `start`, measured in bytes. Positions start with 1. A negative starting position is interpreted as being relative to the end of the string. | `varbinary`  |
| `substr(binary, start, length)`| Returns a substring from `binary` of length `length` from the starting position `start`, measured in bytes. Positions start with 1. A negative starting position is interpreted as being relative to the end of the string. | `varbinary`  |
| `reverse(binary)`              | Returns `binary` with the bytes in reverse order.                                                                   | `varbinary`  |


## Base64 encoding functions

| Function                         | Description                                                                                                          | Return Type |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| `from_base64(string)`            | Decodes binary data from the base64 encoded `string`.                                                                 | `varbinary`  |
| `to_base64(binary)`              | Encodes `binary` into a base64 string representation.                                                                 | `varchar`    |
| `from_base64url(string)`         | Decodes binary data from the base64 encoded `string` using the URL safe alphabet.                                   | `varbinary`  |
| `to_base64url(binary)`           | Encodes `binary` into a base64 string representation using the URL safe alphabet.                                   | `varchar`    |
| `from_base32(string)`            | Decodes binary data from the base32 encoded `string`.                                                                 | `varbinary`  |
| `to_base32(binary)`              | Encodes `binary` into a base32 string representation.                                                                 | `varchar`    |

## Hex encoding functions

| Function                      | Description                                                                                       | Return Type |
| ----------------------------- | ------------------------------------------------------------------------------------------------- | ----------- |
| `from_hex(string)`            | Decodes binary data from the hex encoded `string`.                                                 | `varbinary`  |
| `to_hex(binary)`              | Encodes `binary` into a hex string representation.                                                  | `varchar`    |

## Integer encoding functions 

| Function                       | Description                                                                             | Return Type  |
| ------------------------------ | --------------------------------------------------------------------------------------- | ------------ |
| `from_big_endian_32(binary)`   | Decodes the 32-bit two’s complement big-endian binary. The input must be exactly 4 bytes. | `integer`    |
| `to_big_endian_32(integer)`   | Encodes `integer` into a 32-bit two’s complement big-endian format.                      | `varbinary`  |
| `from_big_endian_64(binary)`   | Decodes the 64-bit two’s complement big-endian binary. The input must be exactly 8 bytes. | `bigint`     |
| `to_big_endian_64(bigint)`    | Encodes `bigint` into a 64-bit two’s complement big-endian format.                       | `varbinary`  |

## Floating-point encoding functions

| Function                | Description                                                                                                 | Return Type   |
|-------------------------|-------------------------------------------------------------------------------------------------------------|---------------|
| `from_ieee754_32(binary)` | Decodes the 32-bit big-endian binary in IEEE 754 single-precision floating-point format.                   | `real`        |
| `to_ieee754_32(real)`     | Encodes real into a 32-bit big-endian binary according to IEEE 754 single-precision floating-point format. | `varbinary`   |
| `from_ieee754_64(binary)` | Decodes the 64-bit big-endian binary in IEEE 754 double-precision floating-point format.                    | `double`      |
| `to_ieee754_64(double)`  | Encodes double into a 64-bit big-endian binary according to IEEE 754 double-precision floating-point format.| `varbinary`   |


## Hashing function

| Function                  | Description                                                                         | Return Type   |
|---------------------------|-------------------------------------------------------------------------------------|---------------|
| `crc32(binary)`           | Computes the CRC-32 of binary. For general-purpose hashing, use `xxhash64()`.        | `bigint`      |
| `md5(binary)`             | Computes the MD5 hash of binary.                                                    | `varbinary`   |
| `sha1(binary)`            | Computes the SHA1 hash of binary.                                                   | `varbinary`   |
| `sha256(binary)`          | Computes the SHA256 hash of binary.                                                 | `varbinary`   |
| `sha512(binary)`          | Computes the SHA512 hash of binary.                                                 | `varbinary`   |
| `spooky_hash_v2_32(binary)`| Computes the 32-bit SpookyHashV2 hash of binary.                                   | `varbinary`   |
| `spooky_hash_v2_64(binary)`| Computes the 64-bit SpookyHashV2 hash of binary.                                   | `varbinary`   |
| `xxhash64(binary)`        | Computes the xxHash64 hash of binary.                                              | `varbinary`   |
| `murmur3(binary)`         | Computes the 128-bit MurmurHash3 hash of binary.                                  | `varbinary`   |


## HMAC function

| Function                        | Description                                                             | Return Type  |
|---------------------------------|-------------------------------------------------------------------------|--------------|
| `hmac_md5(binary, key)`         | Computes HMAC with MD5 of binary with the given key.                    | `varbinary`  |
| `hmac_sha1(binary, key)`        | Computes HMAC with SHA1 of binary with the given key.                   | `varbinary`  |
| `hmac_sha256(binary, key)`      | Computes HMAC with SHA256 of binary with the given key.                 | `varbinary`  |
| `hmac_sha512(binary, key)`      | Computes HMAC with SHA512 of binary with the given key.                 | `varbinary`  |





