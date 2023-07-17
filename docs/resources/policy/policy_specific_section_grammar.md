# Policy Section-specific Grammar

## Access Policy YAML Configuration

```yaml
policy:
  access:
    subjects:
      tags:
        - - {{roles:id:**}}
        - - {{users:id:**}}
    predicates:
      - {{create}}
      - {{read}}
      - {{write}}
      - {{put}}
      - {{update}}
      - {{delete}}
      - {{post}}
    objects:
      paths:
        - {{dataos://icebase:spend_analysis/**}}
    allow: {{false}}
```

## Configuration Attributes/Fields

### **`subjects`**

**Description:** a subject is a user that would like to perform a specific predicate on a specific object. It refers to persons or application/services that make the request to perform an action. Attributes of the subject might include tags or groups of tags.<br>
**Data Type:** object<br>
**Requirement:** mandatory<br>
**Default Value:** none<br>
**Possible Value:** none<br>
**Example Usage:**<br>
```yaml
subjects:
  tags:
    -- "roles:id:testuser"
```

---

### **`objects`**

**Description:** the target that the subject would like to perform the predicate on. This can be any target, an API path, a column. The object is the resource (data or service) on which the action is to be performed.<br>
**Data Type:** list of strings<br>
**Requirement:** mandatory<br>
**Default Value:** none<br>
**Possible Value:** any target, api path, tags of requested object, column etc.<br>
**Additional Information:** Predicates are ‘OR’ relationships only, since the PEP is authorizing one action at a time.
**Example Usage:** 
```yaml
objects:
  paths:
    - /dataos/system/themis/**
```

---


### **`tags`**

**Description:** tags are the attributes of the subject or object. A tag field can contain one single tag or a group of tags in the form of a list<br>
**Data Type:** list of strings<br>
**Requirement:** mandatory<br>
**Default Value:** none<br>
**Possible Value:** any valid string<br>
**Additional Information:** 
- **Defining AND/OR Relationships**
    - Defining OR Relationship
        - The syntax given below allows access for either `tag1` OR `tag2`.
            
            ```yaml
            tags: 
            	-- tag1
            	-- tag2
            ```
            
        - The outermost list contains two inner lists, each representing a tag. In this case, it means that both "tag1" and "tag2" are considered separately which is how you define the OR relationships between tags.
        - Example of OR Relationship
            - In this example policy, an object MUST have the resource path of `/metis/api/v2/workspaces/public` **OR** `/metis/api/v2/workspaces/sandbox` to qualify for this policy to apply.
                
                ```yaml
                name: object-example1
                version: v1
                type: policy
                layer: user
                description: example policy
                policy:
                  access:
                    subjects:
                      tags:
                        - - roles:id:developer
                          - roles:id:testuser
                    predicates:
                      - read
                    objects:
                      paths:
                        - /metis/api/v2/workspaces/public
                        - /metis/api/v2/workspaces/sandbox
                    allow: true
                ```
                
            - In this example policy, an object MUST have the `PII.Email` **OR** `PII.Sensitive` tags to qualify for this policy to apply.
                
                ```yaml
                name: object-example2
                version: v1
                type: policy
                layer: user
                description: example policy
                policy:
                  access:
                    subjects:
                      tags:
                        - - roles:id:developer
                          - roles:id:testuser
                    predicates:
                      - read
                    objects:
                      tags:
                        - - PII.Email
                        - - PII.Sensitive
                    allow: true
                ```
                
    - Defining AND relationship
        - To define an AND relationship between tags, the structure would be like this:
            
            ```yaml
            tags: 
            	-- tag1
            	 - tag2
            ```
            
        - The outermost list contains a single inner list with two tags. The indentation implies that "tag2" is a child of "tag1," indicating the requirement for both tags to be present which is how you define the AND relationship between tags.
        - Example of AND Relationship
            
            For example, in this example policy, a subject MUST have both the tags (`roles:id:pii-reader` AND `roles:id:testuser`) to qualify for this policy to apply/or to be applicable. 
            
            ```yaml
            name: subject-example1
            version: v1
            type: policy
            layer: user
            description: example policy
            policy:
              access:
                subjects:
                  tags:
                    - - roles:id:pii-reader
                      - roles:id:user
                predicates:
                  - read
                objects:
                  tags:
                    - - PII.Sensitive
                      - dataos:type:column
                allow: true
            ```
            
    - Defining Complex Relationships Using AND, OR
        - This section represents an expression where either "tag1" or both "tag2" and "tag3" should be true. The outermost list contains three elements. The first and second elements represent "tag1" and "tag2" separately. The third element, "tag3," is indented to indicate that it is a child of "tag2," implying that both "tag2" and "tag3" should be true.
            
            ```yaml
            # tag1 OR (tag2 AND tag3)
            tags: 
            - - tag1
            - - tag2
              - tag3
            ```
            
        - Example of Complex AND, OR Relationship
            
            For example, to qualify for the following example policy, a subject must have either both tags (`roles:id:pii-reader` AND `roles:id:testuser`) OR the tag `roles:id:marketing-manager`.
            
            ```yaml
            name: subject-example2
            version: v1
            type: policy
            layer: user
            description: example policy
            policy:
              access:
                subjects:
                  tags:
                    - - roles:id:pii-reader
                      - roles:id:testuser
                    - - roles:id:marketing-manager
                predicates:
                  - read
                objects:
                  tags:
                    - - PII.Sensitive
                      - dataos:type:column
                allow: true
            ```
            
- **Evaluating List Attributes using Wildcard**
    - The symbol`:` is a delimiter in the tags field and paths field, and predicates field; additional syntax includes:
        
        
        | Wildcard | Wildcard Name | Example | Description |
        | --- | --- | --- | --- |
        | ? | Single Character Wildcard - Matches exactly one occurrence of any character | ?at | Matches cat and bat but not at |
        | * | Glob/Asterisk - Matches any number of characters, including none, within the same level of a hierarchy. Can be used to evaluate all items in a list; if any item in the list matches the condition, then the condition passes. | foo:*:bar | Matches foo:baz:bar and foo:zab:bar but not foo:bar nor foo:baz:baz:bar |
        | ** | Super Glob/Double Asterisk - Matches any number of characters across multiple levels of a hierarchy. Can be used to evaluate all items in a list; if any item in the list matches the condition, then the condition passes. |  foo:**:bar | Matches foo:baz:baz:bar, foo:baz:bar, and foo:bar, but not foobar or foo:baz |
        | [] | Character List - Matches exactly one character that is contained within the brackets.  | [cb]at | matches cat and bat but not mat nor at
        (It’s worthing noting that the order of characters within the brackets doesn’t matter, [cb]at and [bc]at function the same way) |
        | [!] | Negated Character List - Matches any single character that is not listed between the brackets. | [!cb]at | matches tat and mat but not cat nor bat |
        | [-] | Ranged Character List - Match a specific character within a certain range. | [a-c]at | cat and bat but not mat nor at |
        | [!-] | Negated Ranged Character List | [!a-c]at  | matches mat and tat but not cat nor bat |
        | {[]} | Alternatives List | {cat,bat,[mt]at}  | matches cat, bat, mat, tat and nothing else |
        | \ | Backslash (escape) | foo\\bar
        foo\bar 
        foo\*bar | matches foo\bar and nothing else
        matches foobar and nothing else
        matches foo*bar and nothing else |

**Example Usage:**

```yaml
# single tag
tags:
	-- "roles:id:testuser"
# group of tags
tags:
	-- "roles:id:test1"
	-- "roles:id:test2"
```

---

### **`predicates`**

**Description:** the action or the verb that the subject would like to perform on the specific object.<br>
**Data Type:** list of strings<br>
**Requirement:** mandatory<br>
**Default Value:** none<br>
**Possible Value:** crud operations like read, write, update, delete or http operations like get, put, post, delete, options.<br>
**Additional Information:** predicates are ‘OR’ relationships only, since the PEP is authorizing one action at a time.<br>
**Example Usage:** in this example policy, a predicate MUST be `read` OR `write` from the PEP to qualify for this policy to apply.

```yaml
predicates:
  - read
  - write
```
<details><summary>Sample Predicates OR Relationship</summary>
    
  ```yaml
  name: predicate-example2
  version: v1
  type: policy
  layer: user
  description: example policy
  policy:
    access:
      subjects:
        tags:
          - - roles:id:pii-reader
            - roles:id:user
          - - roles:id:marketing-manager
      predicates:
        - read
        - write
      objects:
        tags:
          - - PII.Sensitive
            - dataos:type:column
      allow: true
  ```
</details>

---

### **`allow`**

**Description:** action to be allowed or denied<br>
**Data Type:** boolean<br>
**Requirement:** optional<br>
**Default Value:** false<br>
**Possible Value:** true/false<br>
**Example Usage:** 

```yaml
allow: true
```

## Data Policy YAML Configuration

```yaml
policy:
  data:
		dataset: {{sample_driver}}
    collection: {{data_uber}}
    depot: {{icebase}}
    priority: {{90}}
    selector:
      user:
			  match: any
        tags:
					- "roles:id:testuser"
			column:
			  names:
          - "first_name"
          - "last_name"
          - "email_id"
    type: {{filter/mask}}
		{{filter/mask}}: 
```

## Configuration Fields/Attributes

### **`data`**

**Description:** data policy specific section<br>
**Data Type:** object<br>
**Requirement:** mandatory<br>
**Default Value:** none<br>
**Possible Value:** none<br>
**Example Usage:** 

```yaml
data:
  {}
```

---

### **`priority`**

**Description:** the policy with higher priority will override all other policies defined for the same resources.<br>
**Data Type:** number<br>
**Requirement:** optional<br>
**Default Value:** none<br>
**Possible Value:** any number between 0-100. 0 being the lowest priority and 100 being the highest<br>
**Example Usage:** 

```yaml
priority: 80
```

---

### **`depot`**

**Description:** name of depot<br>
**Data Type:** string<br>
**Requirement:** optional<br>
**Default Value:** none<br>
**Possible Value:** valid depot name. Use ** for all possible depot names.<br>
**Example Usage:** 

```yaml
depot: icebase
```

---

### **`collection`**

**Description:** name of the collection<br>
**Data Type:** string<br>
**Requirement:** optional<br>
**Default Value:** none<br>
**Possible Value:** any valid collection name. Use ** for all possible collection names.<br>
**Example Usage:**

```yaml
collection: retail
```

---

### **`dataset`**

**Description:** name of dataset<br>
**Data Type:** string<br>
**Requirement:** optional<br>
**Default Value:** none<br>
**Possible Value:** any valid dataset name. Use ** for all possible dataset names.<br>
**Example Usage:** 

```yaml
dataset: city
```

---

### **`selector`**

**Description:** selector section<br>
**Data Type:** object<br>
**Requirement:** mandatory<br>
**Default Value:** none<br>
**Possible Value:** none<br>
**Example Usage:**

```yaml
selector:
  user:
    {}
  column:
    {}
```

---

### **`user`**

**Description:** section for defining the user<br>
**Data Type:** object<br>
**Requirement:** mandatory<br>
**Default Value:** none<br>
**Possible Value:** none<br>
**Example Usage:** 

```yaml
user:
  match: any
  tags:
    - "roles:id:testuser"
```

---

### **`match`**
**Description:** This attribute<br>
**Data Type:** string<br>
**Requirement:** mandatory<br>
**Default Value:** none<br>
**Possible Value:** any/all<br>
**Example Usage:** 

```yaml
match: any
```

---

### [**`tags`**](#tags)

---

### **`column`**

**Description:** column section<br>
**Data Type:** object<br>
**Requirement:** mandatory<br>
**Default Value:** none<br>
**Possible Value:** any valid column name<br>
**Example Usage:** 

```yaml
column:
  names:
    - "first_name"
```

---

### **`names`**

**Description:** list of column name<br>
**Data Type:** list of strings<br>
**Requirement:** mandatory<br>
**Default Value:** none<br>
**Possible Value:** valid column names<br>
**Example Usage:**

```yaml
names:
  - "first_name"
  - "last_name"
```

---

### **`mask`**

**Description:** field for defining the data masking strategy<br>
**Data Type:** object<br>
**Requirement:** optional<br>
**Default Value:** none<br>
**Possible Value:** depends on the masking strategy utilized<br>
**Example Usage:** in this example policy, a predicate MUST be `read` OR `write` from the PEP to qualify for this policy to apply.

```yaml
mask:
  operator: hash
  hash:
    algo: sha256
```

**Additional Information:** for more information regarding the various masking strategies within DataOS refer to the link below

Masking strategies are key components in preserving data privacy and ensuring information security. These strategies encompass a set of operators or rules meticulously designed with the capability to be tailored based on user requirements.

Here's a handy table that lists the data masking strategies and the corresponding data types they can be used for:

| Masking Type | Operator | Text | Number | Date | Object |
| --- | --- | --- | --- | --- | --- |
| Hashing | `hash` | Y | N | N | N |
| Bucketing | `bucket_name`, `bucket_date` |N | Y | Y | N |
| Regex replace | `regex_replace` | Y | N | N | N |
| Format preservation (Random Pattern) | `rand_pattern` | Y | N | N | N |
| Redaction | `redact` | Y | Y | Y | N |
| Pass Through | `pass_through` | Y | Y | Y | Y |

In the following section, we delve into comprehensive explanations and syntax examples for each of these data masking strategies.

#### **`bucket_number`**

Using the `bucket_number` operator, numerical data can be categorized into defined range 'buckets.' Each data point is then replaced by the lower boundary of the bucket it falls into.

**Configuration Syntax**

To leverage the `bucket_number` operator, incorporate the following YAML configuration in your data masking definition:

```yaml
mask:
	operator: bucket_number 
	bucket_number:
	  buckets:
			{{bucket-list}}
```

The `{{bucket_list}}` is a placeholder for your list of bucket ranges.

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


#### **`bucket_date`**

The `bucket_date` operator functions similarly to ‘bucket_number’ but is specifically tailored for date data types. This strategy enables the categorization of dates into various precision levels such as hour, day, week, or month.

**Configuration Syntax** 

To implement the ‘bucket_date’ operator, use the following YAML configuration:

```yaml
mask:
  operator: bucket_date
  bucket_date:
    precision: {{date-precision}} # Options: hour, day, week, month
```

**Example**

```yaml
mask:
  operator: bucket_date
  bucket_date:
    precision: month 
```

In this example, the `precision` field designates the granularity of the date bucketing to be at a 'month' level.


#### **`hash`**

The hashing method is a powerful data masking technique wherein a specific input consistently produces an identical fixed-size byte string, commonly referred to as a 'hash code'. A notable feature of hashing is its sensitivity to changes in input; even the slightest modification in input can yield a significantly different hash output.

A unique and crucial characteristic of hashing is its irreversibility — once data is hashed, it cannot be converted back to its original state. This property makes hashing a particularly useful technique for masking sensitive textual data, such as passwords, or personally identifiable information (PII), such as names and email addresses.


**Configuration Syntax**

Hashing involves the use of a specific algorithm that performs the conversion from original data to hashed data. To implement hashing, you will need to specify the hashing algorithm you wish to use. The general syntax structure is as follows:

```yaml
mask:
  operator: hash
  hash:
    algo: {{algorithm-name}}
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


#### **`redact`**

Redaction is a data masking strategy that aims to obscure or completely erase portions of data. Its real-world analogy can be seen in blacking out sections of a document to prevent sensitive information from being disclosed. When applied to data masking, redaction might involve replacing certain elements in a data field (such as characters in an email address or digits in a Social Security number) with a placeholder string, e.g., "[REDACTED]"

For instance, the gender of every individual could be redacted and substituted with a consistent value, 'REDACTED'. Similarly, an individual's location information (which may include address, zip code, state, or country) could be redacted and replaced with 'REDACTED'.

**Configuration Syntax**

To implement the `redact` operator, the following YAML configuration can be utilized:

```yaml
mask:
  operator: redact
#   redact:
#     replacement: {{replacement-string}}
#    hash: 
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

#### **`rand_pattern`**

Random Pattern Masking involves the substitution of sensitive data with randomly produced equivalents that maintain the original data's format or structure. The fundamental goal is to ensure that the masked data is statistically representative and retains operational utility while safeguarding critical information. For example, it can be used to replace personal names with random strings or transform real addresses into plausible but entirely fictitious ones.

**Configuration Syntax**

To implement the `rand_pattern` operator, the following YAML configuration can be utilized:

```yaml
mask:
  operator: rand_pattern
  rand_pattern:
    pattern: {{random-pattern}}
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


#### **`regex_replace`**

The Regular Expression (Regex) Replacement strategy utilizes regular expressions to discern and mask identifiable patterns within the data. The identified patterns can be substituted with a predetermined value or random character(s). This strategy is particularly advantageous for masking data that follows a predictable pattern, such as email addresses, phone numbers, or credit card information.

**Configuration Syntax**

The `regex_replace` operator requires a `pattern` and a `replacement` field in its configuration. The general syntax structure is as follows:

```yaml
mask:
  operator: regex_replace
  regex_replace:
    pattern: {{regex-pattern}}
    replacement: {{replacement-pattern}}
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


#### **`pass_through`**

The "Pass Through" strategy is used when certain data elements should not be masked or altered. With this technique, data developers can specify that certain data fields remain unchanged during the masking process. This approach is suitable for data that doesn't contain sensitive information or data that is already anonymized.

**Configuration Syntax**

To implement the `pass_through` operator, the following YAML configuration can be utilized:

```yaml
mask:
  operator: pass_through
```

---

### **`filters`**

The data visibility for end users is limited due to the filtering policy. You can build a policy to eliminate results from a query's result set depending on comparison operators specified on a column, for example, some users won't be able to see data from the 'Florida' area.

**Description:** section for defining data filter pattern<br>
**Data Type:** list of objects<br>
**Requirement:** optional<br>
**Default Value:** none<br>
**Possible Value:** depends on the filter pattern utilized<br>
**Additional Information:** 
**Example Usage:** 

```yaml
filters: 
  - column: {{store_state_code}}
    operator: {{not_equals}}
    value: {{TN}}
```

#### **`column`**

**Description:** column name<br>
**Data Type:** string<br>
**Requirement:** mandatory<br>
**Default Value:** none<br>
**Possible Value:** valid column name<br>
**Example Usage:** 

```yaml
column: store_state_code
```

#### **`operator`**

**Description:** filter operator name<br>
**Data Type:** string<br>
**Requirement:** mandatory<br>
**Default Value:** none<br>
**Possible Value:** equals/not_equals<br>
**Example Usage:** 

```yaml
operator: not_equals
```

#### **`value`**

**Description:** value on which filter is to be applied<br>
**Data Type:** depends on `coloumn` data type<br>
**Requirement:** mandatory<br>
**Default Value:** none<br>
**Possible Value:** any value within the column<br>
**Example Usage:** 

```yaml
value: TX
```