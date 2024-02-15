# Bitwise functions

### **`bit_count()`**

| Function                    | Description                                                                                                                | Return Type |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------|-------------|
| `bit_count(x, bits)`        | Count the number of bits set in `x` (treated as `bits`-bit signed integer) in 2’s complement representation.                | `bigint`    |


```sql
SELECT bit_count(9, 64); -- 2
SELECT bit_count(9, 8); -- 2
SELECT bit_count(-7, 64); -- 62
SELECT bit_count(-7, 8); -- 6
```