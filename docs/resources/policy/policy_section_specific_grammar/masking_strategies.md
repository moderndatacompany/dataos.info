# Masking Strategies

Masking strategies are key components in preserving data privacy and ensuring information security. These strategies encompass a set of operators or rules meticulously designed with the capability to be tailored based on user requirements.

Here's a handy table that lists the data masking strategies and the corresponding data types they can be used for:

| Type | Text | Number | Date | Object |
| --- | --- | --- | --- | --- |
| Hashing | Y | N | N | N |
| Bucketing | N | Y | Y | N |
| Regex replace | Y | N | N | N |
| Format preservation (Random Pattern) | Y | N | N | N |
| Redaction | Y | Y | Y | N |
| Pass Through | Y | Y | Y | Y |

In the following section, we delve into comprehensive explanations and syntax examples for each of these data masking strategies.

## Bucketing

The bucketing approach to data masking involves the categorization of distinct data points into predefined 'buckets' or categories. By doing this, we ensure the individual data points are obfuscated while the overall patterns and distributions are maintained. Currently, bucketing is applicable for both numerical and date data types.

### **Numerical Data Bucketing**

**Operator: `bucket_number`**

Using the `bucket_number` operator, numerical data can be categorized into defined range 'buckets.' Each data point is then replaced by the lower boundary of the bucket it falls into.

**Configuration Syntax**

To leverage the `bucket_number` operator, incorporate the following YAML configuration in your data masking definition:

```yaml
mask:
	operator: bucket_number 
	bucket_number:
	  buckets:
			${bucket-list}
```

The `{bucket_list}` is a placeholder for your list of bucket ranges.

**Example**

```yaml
mask:
	operator: bucket_number 
	bucket_number:
	  buckets:
	    - 20
	    - 40
	    - 60
	    - 80
	    - 100
```

In this example, numerical data would be segmented into the indicated ranges. A value of 27, for example, would be bucketed to the 20 range, whereas a value of 77 would fall into the 60 range.

### **Date Data Bucketing**

**Operator: `bucket_date`**

The ‘bucket_date’ operator functions similarly to ‘bucket_number’ but is specifically tailored for date data types. This strategy enables the categorization of dates into various precision levels such as hour, day, week, or month.

**Configuration Syntax** 

To implement the ‘bucket_date’ operator, use the following YAML configuration:

```yaml
mask:
  operator: bucket_date
  bucket_date:
    precision: ${date-precision} # Options: hour, day, week, month
```

**Example**

```yaml
mask:
  operator: bucket_date
  bucket_date:
    precision: month 
```

In this example, the `precision` field designates the granularity of the date bucketing to be at a 'month' level.

## Hashing

The hashing method is a powerful data masking technique wherein a specific input consistently produces an identical fixed-size byte string, commonly referred to as a 'hash code'. A notable feature of hashing is its sensitivity to changes in input; even the slightest modification in input can yield a significantly different hash output.

A unique and crucial characteristic of hashing is its irreversibility — once data is hashed, it cannot be converted back to its original state. This property makes hashing a particularly useful technique for masking sensitive textual data, such as passwords, or personally identifiable information (PII), such as names and email addresses.

**Operator: `hash`**

**Configuration Syntax**

Hashing involves the use of a specific algorithm that performs the conversion from original data to hashed data. To implement hashing, you will need to specify the hashing algorithm you wish to use. The general syntax structure is as follows:

```yaml
mask:
  operator: hash
  hash:
    algo: ${algorithm-name}
```

**Example**

```yaml
mask:
  operator: hash
  hash:
    algo: sha256
```

In this YAML configuration, the operator `hash` is specified along with the SHA-256 algorithm (`algo: sha256`). The SHA-256 algorithm is a popular choice due to its strong security properties, but other algorithms could be used as per your requirements.

Remember, the `hash` operator is only applicable to textual data types. Attempting to use it on non-textual data types may lead to unintended results or errors. Always make sure the data you wish to mask is compatible with the masking operator you choose.

## Redaction

Redaction is a data masking strategy that aims to obscure or completely erase portions of data. Its real-world analogy can be seen in blacking out sections of a document to prevent sensitive information from being disclosed. When applied to data masking, redaction might involve replacing certain elements in a data field (such as characters in an email address or digits in a Social Security number) with a placeholder string, e.g., "[REDACTED]"

For instance, the gender of every individual could be redacted and substituted with a consistent value, 'REDACTED'. Similarly, an individual's location information (which may include address, zip code, state, or country) could be redacted and replaced with 'REDACTED'.

**Operator: `redact`**

**Configuration Syntax**

To implement the `redact` operator, the following YAML configuration can be utilized:

```yaml
mask:
  operator: redact
  redact:
    replacement: ${replacement-string}
# 	hash: # Why is the redact hash here?
#   algo: sha256
```

**Example**

```yaml
mask:
  operator: redact
  redact:
    replacement: 'REDACTED'
#	hash: # Why is the redact hash here?
#  algo: sha256
```

The `replacement` field determines the string that will replace the redacted portions of data.

## Random Pattern

Random Pattern Masking involves the substitution of sensitive data with randomly produced equivalents that maintain the original data's format or structure. The fundamental goal is to ensure that the masked data is statistically representative and retains operational utility while safeguarding critical information. For example, it can be used to replace personal names with random strings or transform real addresses into plausible but entirely fictitious ones.

**Operator: `rand_pattern`**

**Configuration Syntax**

To implement the `rand_pattern` operator, the following YAML configuration can be utilized:

```yaml
mask:
  operator: rand_pattern
  rand_pattern:
    pattern: ${random-pattern}
```

Here, `${random-pattern}` is a placeholder for the random pattern you wish to apply.

**Example**

Below is an example illustrating the usage of the `rand_pattern` operator:

```yaml
mask:
  operator: rand_pattern
  rand_pattern:
    pattern: '####-####-####'
```

In this instance, the specified pattern '####-####-####' will generate random numbers in a format similar to a credit card number, preserving the structure of the original data but replacing it with randomly generated information.

**Format Preserving Encryption (FPE)**: As the name suggests, this method encrypts data in a way that the output has the same format as the input. For example, if a 16-digit credit card number is encrypted using FPE, the result is another 16-digit number. This maintains functional realism, allowing systems to operate normally with masked data.

## Regular Expression (Regex) Replacement

The Regular Expression (Regex) Replacement strategy utilizes regular expressions to discern and mask identifiable patterns within the data. The identified patterns can be substituted with a predetermined value or random character(s). This strategy is particularly advantageous for masking data that follows a predictable pattern, such as email addresses, phone numbers, or credit card information.

**Operator: `regex_replace`**

**Configuration Syntax**

The `regex_replace` operator requires a `pattern` and a `replacement` field in its configuration. The general syntax structure is as follows:

```yaml
mask:
  operator: regex_replace
  regex_replace:
    pattern: ${regex-pattern}
    replacement: ${replacement-pattern}
```

The `pattern` field expects a regular expression pattern as its value, while the `replacement` field expects the desired replacement string.

**Examples**

```yaml
mask:
  operator: regex_replace
  regex_replace:
    pattern: .{5}$
    replacement: xxxxx
```

In the above example, the regular expression`.{5}$` represents any five characters at the end of a string. These characters will be replaced by 'xxxxx'.

```yaml
mask:
  operator: regex_replace
  regex_replace:
    pattern: '[0-9]'
    replacement: '#'
```

Here, the regular expression `[0-9]` denotes any single digit which will be replaced with '#'.

```yaml
mask:
  operator: regex_replace
  regex_replace:
    pattern: '[0-9](?=.*.{4})'
    replacement: '#'
```

In this case, the regex pattern `[0-9](?=.*.{4})` identifies a digit followed by at least four characters. This digit will be replaced by '#'.

## Pass Through

The "Pass Through" strategy is used when certain data elements should not be masked or altered. With this technique, data developers can specify that certain data fields remain unchanged during the masking process. This approach is suitable for data that doesn't contain sensitive information or data that is already anonymized.

**Operator: `pass_through`**

**Configuration Syntax**

To implement the `pass_through` operator, the following YAML configuration can be utilized:

```yaml
mask:
  operator: pass_through
```