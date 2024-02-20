# Decimal 

### **`litreals`**

Specify a decimal literal using the syntax DECIMAL `xxxxxxx.yyyyyyy`.

The precision of the decimal type for a literal is determined by the total number of digits in the literal, considering both the leading and trailing zeros. The scale is determined by the number of digits in the fractional part, including any trailing zeros.

| Example Literal                   | Data Type      |
|-----------------------------------|----------------|
| DECIMAL '0'                       | DECIMAL(1)     |
| DECIMAL '12345'                    | DECIMAL(5)     |
| DECIMAL '0000012345.1234500000'   | DECIMAL(20, 10)|



```sql
-- DECIMAL '0'
SELECT CAST('0' AS DECIMAL(1)) AS result1;

-- DECIMAL '12345'
SELECT CAST('12345' AS DECIMAL(5)) AS result2;

-- DECIMAL '0000012345.1234500000'
SELECT CAST('0000012345.1234500000' AS DECIMAL(20, 10)) AS result3;
```

## Binary arithmetic decimal operators

Mathematical operations adhere to standard mathematical operators. The precision and scale calculation rules for the result are elucidated in the table below. Let `x` denote a variable of type DECIMAL(xp, xs), and `y` denote a variable of type DECIMAL(yp, ys).

| Operation         | Result type precision                                      | Result type scale           |
|-------------------|-------------------------------------------------------------|-----------------------------|
| x + y and x - y   | min(38, 1 + max(xs, ys) + max(xp - xs, yp - ys))           | max(xs, ys)                 |
| x * y             | min(38, xp + yp)                                            | xs + ys                     |
| x / y             | min(38, xp + ys - xs + max(0, ys - xs))                    | max(xs, ys)                 |
| x % y             | min(xp - xs, yp - ys) + max(xs, ys)                         | max(xs, ys)                 |


## Comparison operators

The decimal type supports all standard [comparison functions and operators](./comparison.md) 

## Unary decimal operators:

The `-` operator executes negation, and the resulting type is identical to the type of the argument.
