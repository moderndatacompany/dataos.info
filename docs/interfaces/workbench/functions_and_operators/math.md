# Mathematical functions and operators

## Mathematical operators

| Operator | Description                            |
|----------|----------------------------------------|
| +        | Addition                               |
| -        | Subtraction                            |
| *        | Multiplication                         |
| /        | Division (integer division performs truncation) |
| %        | Modulus (remainder)                    |



When performing division operations in SQL queries, it's important to handle division by zero errors. One approach is to use the `NULLIF` function to replace the divisor with NULL when it equals zero. However, if you prefer not to return NULL values, you can use the `COALESCE` function to replace NULL values with a specified default value. Here's an example:

```sql
SELECT value1 / NULLIF(value2, 0) AS ratio
FROM your_table;
```

```sql
SELECT value1 / COALESCE(NULLIF(value2, 0), default_value) AS ratio
FROM your_table;
```


## Mathematical functions
### **`abs()`**
| Function      | Description                         | Return Value   |
| ------------- | ----------------------------------- | -------------- |
| `abs(x)`      | Returns the absolute value of `x`. | [same as input] |

### **`cbrt()`**
| Function      | Description                   | Return Value   |
| ------------- | ----------------------------- | -------------- |
| `cbrt(x)`     | Returns the cube root of `x`. | numeric        |

### **`ceil(x)`**
| Function      | Description                        | Return Value   |
| ------------- | ---------------------------------- | -------------- |
| `ceil(x)`     | Alias for `ceiling()`.             | [same as input] |

### **`ceiling()`**
| Function      | Description                        | Return Value   |
| ------------- | ---------------------------------- | -------------- |
| `ceiling(x)`  | Returns x rounded up to the nearest integer. | [same as input] |

### **`degrees()`**
| Function      | Description                                 | Return Value   |
| ------------- | ------------------------------------------- | -------------- |
| `degrees(x)` | Converts angle x in radians to degrees.     | numeric        |

### **`e()`**
| Function      | Description              | Return Value   |
| ------------- | ------------------------ | -------------- |
| `e()`         | Returns Euler’s number. | numeric        |

### **`exp()`**
| Function      | Description                             | Return Value   |
| ------------- | --------------------------------------- | -------------- |
| `exp(x)`      | Returns Euler’s number raised to the power of x. | numeric         |

### **`floor()`**
| Function      | Description                        | Return Value   |
| ------------- | ---------------------------------- | -------------- |
| `floor(x)`    | Returns x rounded down to the nearest integer. | [same as input] |

### **`ln()`**
| Function      | Description                        | Return Value   |
| ------------- | ---------------------------------- | -------------- |
| `ln(x)`       | Returns the natural logarithm of x. | numeric       |

### **`log()`**
| Function      | Description                        | Return Value   |
| ------------- | ---------------------------------- | -------------- |
| `log(b, x)`   | Returns the base b logarithm of x. | numeric        |

### **`log2()`**
| Function      | Description                        | Return Value   |
| ------------- | ---------------------------------- | -------------- |
| `log2(x)`     | Returns the base 2 logarithm of x. | numeric        |

### **`log10()`**
| Function      | Description                        | Return Value   |
| ------------- | ---------------------------------- | -------------- |
| `log10(x)`    | Returns the base 10 logarithm of x.| numeric        |

### **`mod()`**
| Function      | Description                        | Return Value   |
| ------------- | ---------------------------------- | -------------- |
| `mod(n, m)`   | Returns the modulus (remainder) of n divided by m. | [same as input] |

### **`pi()`**
| Function      | Description                        | Return Value   |
| ------------- | ---------------------------------- | -------------- |
| `pi()`        | Returns the constant Pi.           | numeric        |

### **`pow()`**
| Function      | Description                        | Return Value   |
| ------------- | ---------------------------------- | -------------- |
| `pow(x, p)`   | Alias for `power()`.               | numeric        |

### **`power()`**
| Function      | Description                        | Return Value   |
| ------------- | ---------------------------------- | -------------- |
| `power(x, p)` | Returns x raised to the power of p.| numeric        |

### **`radians()`**
| Function      | Description                        | Return Value   |
| ------------- | ---------------------------------- | -------------- |
| `radians(x)`  | Converts angle x in degrees to radians. | numeric        |

### **`round()`**
| Function      | Description                                                        | Return Value   |
| ------------- | ------------------------------------------------------------------ | -------------- |
| `round(x)`    | Returns x rounded to the nearest integer.                          | [same as input] |
| `round(x, d)` | Returns x rounded to d decimal places.                             | [same as input] |

### **`sign()`**

| Function      | Description                                                        | Return Value   |
| ------------- | ------------------------------------------------------------------ | -------------- |
| `sign(x)`     | Returns the signum function of x.                                  | [same as input] |

### **`sqrt()`**
| Function      | Description                                   | Return Value   |
| ------------- | --------------------------------------------- | -------------- |
| `sqrt(x)`     | Returns the square root of x.                 | numeric       |

### **`truncate()`**
| Function      | Description                                                        | Return Value   |
| ------------- | ------------------------------------------------------------------ | -------------- |
| `truncate(x)` | Returns x rounded to integer by dropping digits after decimal point.| numeric        |

### **`width_bucket()`**
| Function                | Description                                                                                            | Return Value   |
| ----------------------- | ------------------------------------------------------------------------------------------------------ | -------------- |
| `width_bucket(x, bound1, bound2, n)` | Returns the bin number of x in an equi-width histogram with the specified bounds and number of buckets. | bigint         |
| `width_bucket(x, bins)` | Returns the bin number of x according to the specified bins array.                                     | bigint         |

## Random functions

### **`rand()`**

| Function  | Description                    | Return Value   |
| --------- | ------------------------------ | -------------- |
| `rand()`  | Alias for `random()`.          | numeric        |


### **`random()`**

| Function       | Description                                       | Return Value   |
| -------------- | ------------------------------------------------- | -------------- |
| `random()`     | Returns a pseudo-random value in the range 0.0 <= x < 1.0. | numeric         |
| `random(n)`    | Returns a pseudo-random number between 0 and n (exclusive). | [same as input] |
| `random(m, n)` | Returns a pseudo-random number between m and n (exclusive). | [same as input] |

## Trignometric functions

### **`acos()`**

| Function   | Description                   | Return Value   |
| ---------- | ----------------------------- | -------------- |
| `acos(x)`  | Returns the arc cosine of x. | numeric        |

### **`asin()`**
| Function   | Description                | Return Value   |
| ---------- | -------------------------- | -------------- |
| `asin(x)`  | Returns the arc sine of x. | numeric        |

### **`atan()`**

| Function   | Description                | Return Value   |
| ---------- | -------------------------- | -------------- |
| `atan(x)`  | Returns the arc tangent of x. | numeirc        |

### **`atan2()`**

| Function     | Description                        | Return Value   |
| ------------ | ---------------------------------- | -------------- |
| `atan2(y, x)` | Returns the arc tangent of y / x. | numeric        |

### **`cos()`**
| Function   | Description               | Return Value   |
| ---------- | ------------------------- | -------------- |
| `cos(x)`   | Returns the cosine of x. | numeric        |

### **`cosh()`**
| Function    | Description                         | Return Value   |
| ----------- | ----------------------------------- | -------------- |
| `cosh(x)`   | Returns the hyperbolic cosine of x. | numeric        |

### **`sin()`**

| Function   | Description               | Return Value   |
| ---------- | -------------------------| -------------- |
| `sin(x)`   | Returns the sine of x.   | numeric        |

### **`sinh()`**

| Function   | Description                          | Return Value   |
| ---------- | ------------------------------------ | -------------- |
| `sinh(x)`  | Returns the hyperbolic sine of x.    | numeric        |

### **`tan()`**


| Function   | Description               | Return Value   |
| ---------- | -------------------------| -------------- |
| `tan(x)`   | Returns the tangent of x. | numeric       |

### **`tanh()`**

| Function   | Description                          | Return Value   |
| ---------- | ------------------------------------ | -------------- |
| `tanh(x)`  | Returns the hyperbolic tangent of x. | numeric        |

## Floating point functions

### **`infinity()`**

| Function        | Description                                | Return Value   |
| --------------- | ------------------------------------------ | -------------- |
| `infinity()`   | Returns the constant representing positive infinity. | numeric       |

### **`is_finite()`**
| Function        | Description                                | Return Value   |
| --------------- | ------------------------------------------ | -------------- |
| `is_finite(x)` | Determine if x is finite.                  | boolean        |

### **`is_infinite()`**

| Function           | Description                             | Return Value   |
| ------------------ | --------------------------------------- | -------------- |
| `is_infinite(x)`  | Determine if x is infinite.             | boolean        |

### **`is_nan()`**

| Function      | Description                         | Return Value   |
| ------------- | ----------------------------------- | -------------- |
| `is_nan(x)`  | Determine if x is not-a-number.     | boolean        |

### **`nan()`**

| Function   | Description                                     | Return Value   |
| ---------- | ----------------------------------------------- | -------------- |
| `nan()`    | Returns the constant representing not-a-number. | numeric        |

## Base conversion functions

### **`from_base()`**

| Function             | Description                                             | Return Value   |
| -------------------- | ------------------------------------------------------- | -------------- |
| `from_base(string, radix)` | Returns the value of string interpreted as a base-radix number. | bigint         |

### **`to_base()`**

| Function          | Description                                                  | Return Value   |
| ----------------- | ------------------------------------------------------------ | -------------- |
| `to_base(x, radix)` | Returns the base-radix representation of x. | varchar        |

## Statistical functions

### **`cosine_similarity()`**

| Function                    | Description                                                                                      | Return Value   |
| --------------------------- | ------------------------------------------------------------------------------------------------ | -------------- |
| `cosine_similarity(x, y)`   | Returns the cosine similarity between the sparse vectors x and y.                                | FLOAT        |

### **`wilson_interval_lower()`**

| Function                                      | Description                                                                                                           | Return Value   |
| --------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | -------------- |
| `wilson_interval_lower(successes, trials, z)` | Returns the lower bound of the Wilson score interval of a Bernoulli trial process at a confidence specified by z.    | FLOAT        |

### **`wilson_interval_upper()`**
| Function                                      | Description                                                                                                           | Return Value   |
| --------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | -------------- |
| `wilson_interval_upper(successes, trials, z)` | Returns the upper bound of the Wilson score interval of a Bernoulli trial process at a confidence specified by z.    | FLOAT          |



## Cumulative distribution functions

### **`beta_cdf()`**

| Function             | Description                                                                                     | Return Value |
| -------------------- | ----------------------------------------------------------------------------------------------- | ------------ |
| `beta_cdf(a, b, v)` | Compute the Beta cumulative distribution function with given parameters a, b: P(N < v; a, b). | double     |

### **`inverse_beta_cdf()`**

| Function                        | Description                                                                                                     | Return Value |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------- | ------------ |
| `inverse_beta_cdf(a, b, p)`    | Compute the inverse of the Beta cumulative distribution function with given parameters a, b for the probability p: P(N < n). | double     |

### **`inverse_normal_cdf()`**

| Function                            | Description                                                                                                   | Return Value |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------ |
| `inverse_normal_cdf(mean, sd, p)`  | Compute the inverse of the Normal cumulative distribution function with given mean and standard deviation (sd) for the probability p: P(N < n). | double     |

### **`normal_cdf()`**

| Function                     | Description                                                                                                       | Return Value |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------- | ------------ |
| `normal_cdf(mean, sd, v)`   | Compute the Normal cumulative distribution function with given mean and standard deviation (sd): P(N < v; mean, sd). | double     |

