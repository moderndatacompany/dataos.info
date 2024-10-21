# Attributes of Policy manifest

## Structure of a Access Policy manifest

```yaml
name: ${my_policy}
version: v1
type: policy
tags:
  - ${policy}
  - ${access}
description: ${policy manifest}
owner: ${iamgroot}
layer: users
policy:
  access:
    subjects:
      tags:
        - - ${roles:id:**}
        - - ${users:id:**}
    predicates:
      - ${create}
      - ${read}
      - ${write}
      - ${put}
      - ${update}
      - ${delete}
      - ${post}
      - ${access}
    objects:
      paths:
        - ${dataos://icebase:retail/city}
    allow: ${true}
    collection: default
    name: ${test_access_policy}
    description: ${description of policy}
```

### **Configuration Attributes**

#### **`policy`**


**Description:** configuration for the policy.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| mapping        | mandatory      | none                   | none

**Example Usage:**<br>
```yaml
policy:
  data/access:
    {}
```


#### **`access`**

**Description:** mapping for access policy attributes<br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| mapping       | mandatory      | none              | none                |


**Example Usage:**<br>
```yaml
access:
  subjects:
    {}
  predicates:
    {}
  objects:
    {}
  allow: true
```

---

#### **`subjects`**

**Description:** a subject is a user that would like to perform a specific predicate on a specific object. It refers to persons or application/services that make the request to perform an action. Attributes of the subject might include tags or groups of tags.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| mapping       | mandatory      | none              | none                |

**Example Usage:**<br>
```yaml
subjects:
  tags:
    -- "roles:id:testuser"
```

---

#### **`objects`**:

**Description:** the target that the subject would like to perform the predicate on. This can be any target, an API path, a column. The object is the resource (data or service) on which the action is to be performed.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| list of strings       | mandatory      | none              | any target, api path, tags of requested object, column etc.               |

**Additional Information:** Predicates are ‘OR’ relationships only, since the PEP is authorizing one action at a time.

**Example Usage:** 
```yaml
objects:
  paths:
    - /dataos/system/themis/**
```

---

#### **`paths`**

**Description:** object address in the  form of paths 

| **Data Type** | **Requirement** | **Default Value**  | **Possible Value** |
| ------------- | --------------  | -------------------| -------------------|
| list of string| optional        | none               | valid paths        |

**Example Usage:** 
```yaml
paths:
  - /dataos/system/themis/**
```

---


#### **`tags`**

| **Data Type** | **Requirement**| **Default Value**  | **Possible Value**  |
| ------------- | -------------- | -------------------| ------------------- |
|list of strings| mandatory      | none               |         none        |


**Additional Information:**
The manifest tags field in both subjects and objects is an array of string arrays. The [rules](/resources/policy/rules_for_and_or_relationship/) page will help you to define required expressions.

---

#### **`predicates`**


**Description:** the action or the verb that the subject would like to perform on the specific object.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| list of strings       | mandatory      | none              | crud operations like read, write, update, delete or http operations like get, put, post, delete, options.               |

**Additional Information:** Predicates are ‘OR’ relationships only, since the PEP is authorizing one action at a time.

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

#### **`allow`**

**Description:** action to be allowed or denied<br>

| **Data Type** | **Requirement**| **Default Value** | **Possible Value** |
| ------------- | -------------- | -------------------| ------------------|
| boolean       | optional       | false              | true/false        |

**Example Usage:** 

```yaml
allow: true
```

#### **`name`**

**Description:** name of the access policy<br>

| **Data Type** | **Requirement** | **Default Value**  | **Possible Value**  |
| ------------- | --------------  | -------------------| ------------------- |
| string        | optional        | false              | none         |

**Example Usage:** 

```yaml
name: my-first-access-policy
```

---

#### **`description`**

**Description:** description of the access policy<br>

| **Data Type** | **Requirement** | **Default Value**  | **Possible Value**  |
| ------------- | --------------  | -------------------| ------------------- |
| string        | optional        | false              | none       |

**Example Usage:** 
```yaml
description: this is a access policy
```
---

#### **`collection`**

**Description:** description of the access policy<br>

| **Data Type** | **Requirement** | **Default Value**  | **Possible Value**  |
| ------------- | --------------  | -------------------| ------------------- |
| string        | optional        | default            | none                |

**Example Usage:** 
```yaml
collection: default
```
---

## Structure of a Data Policy manifest

```yaml
name: ${my_policy}
version: v1
type: policy
tags:
  - policy
  - data
policy:
  data:
    type: ${filter/mask}
    depot: ${icebase}
    collection: ${data_uber}
    dataset: ${sample_driver}
    priority: ${90}
    selector:
      user:
        match: any
        tags:
          - "roles:id:testuser"
      column:
        tags:
          - "PII.email"
          - "PII.income"
    ${filter/mask}: 
```

### **Configuration Attributes**

#### **`data`**

**Description:** data policy specific section<br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | --------------  | -------------------| ------------------|
| mapping       | mandatory       | none               | none                |


**Example Usage:** 

```yaml
data:
  {}
```

---

#### **`priority`**

**Description:** the Policy with lower value of priority attribute will take precedence over all other policies associated with the same resources. Consequently, a policy assigned a priority of 1 will supersede any conflicting policy assigned a priority of 90.<br>

| **Data Type** | **Requirement** | **Default Value**  | **Possible Value**   |
| ------------- | --------------  | -------------------| -------------------  |
| number        | optional        | none               | 1 to 100 (inclusive) |

**Example Usage:** 

```yaml
priority: 80
```

---

#### **`depot`**

**Description:** name of depot<br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| string        | optional       | none                | **                |

**Example Usage:** 

```yaml
depot: icebase
```

---

#### **`collection`**

**Description:** name of the collection in the glob pattern<br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| string        | optional       | default               | valid collection name , ** (for all collection)              |

**Example Usage:**

```yaml
collection: retail
```

---

#### **`dataset`**

**Description:** name of dataset<br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| string        | optional       | none                | **                |

**Example Usage:** 

```yaml
dataset: city
```

---

#### **`selector`**

**Description:** selector section<br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| mapping       | mandatory      | none                | none                |

**Example Usage:**
```yaml
selector:
  user:
    {}
  column:
    {}
```

---

#### **`user`**

**Description:** section for defining the user<br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | -------------- | ------------------- | ------------------- |
| mapping       | mandatory      | none                | none                |

**Example Usage:** 
```yaml
user:
  match: any
  tags:
    - "roles:id:testuser"
```
---

#### **`match`**
**Description:**  The `match` attribute specifies the match condition.<br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | --------------- | ----------------- | ------------------ |
| string        | mandatory       | none              | any/all            |

**Additional Information:** - `any`- must match at least one tag - `all` - must match all tags

**Example Usage:** 

```yaml
match: any
```

---

#### **`column`**

**Description:** column section<br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | --------------- | ----------------- | ------------------ |
| mapping       | mandatory       | none              | none               |

**Example Usage:** 

```yaml
column:
  
```

---

#### **`names`**

**Description:** list of column names<br>

| **Data Type**     | **Requirement** | **Default Value** | **Possible Value** |
| ----------------- | --------------- | ----------------- | ------------------ |
| list of strings   | mandatory       | none              | valid column name  |

**Example Usage:**

<br>
```yaml
names:
  - "first_name"
  - "last_name"
```
<br>

---

#### **`tags`**

**Description:** list of tags given to columns<br>

| **Data Type**     | **Requirement** | **Default Value** | **Possible Value** |
| ----------------- | --------------- | ----------------- | ------------------ |
| list of strings   | mandatory       | none              | valid column tags defined under some tag group  |

**Example Usage:**

```yaml
tags:
  - "PII.age"
  - "dataos.city"
```
<aside class="callout">
🗣️ The specified tag must be *associated* with a corresponding tag group and follow the format. For additional information on tag groups, please refer to the <a href="/interfaces/metis/navigating_metis_ui_how_to_guide/#adding-tag-categories-tags-and-glossary">Metis documentation</a>.
</aside>

---

#### **`mask`**

**Description:** field for defining the data masking strategy<br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | --------------- | ----------------- | ------------------ |
| mapping       | optional        | none              | depends on the masking strategy utilized |

**Example Usage:** 
```yaml
mask:
  operator: hash
  hash:
    algo: sha256
```

#### **`operator`**

**Description:** operator defines the data masking strategy<br>

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | --------------- | ----------------- | ------------------ |
| string       | mandatory        | none              | depends on the masking strategy utilized |

**Example Usage:** 
```yaml
mask:
  operator: hash
  hash:
    algo: sha256
```


**Additional Information:** 

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

##### **`bucket_number`**

Using the `bucket_number` operator, numerical data can be categorized into defined range 'buckets'. Each data point is then replaced by the lower boundary of the bucket it falls into.

=== "Configuration Syntax"

    To leverage the `bucket_number` operator, incorporate the following YAML configuration in your data masking definitio. The`${bucket_list}` is a placeholder for your list of bucket ranges.

    ```yaml
    mask:
      operator: bucket_number 
      bucket_number:
        buckets:
          ${bucket-list}
    ```

=== "Example"

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


##### **`bucket_date`**

The `bucket_date` operator functions similarly to ‘bucket_number’ but is specifically tailored for date data types. This strategy enables the categorization of dates into various precision levels such as hour, day, week, or month.

=== "Configuration Syntax"

    To implement the ‘bucket_date’ operator, use the following YAML configuration:

    ```yaml
    mask:
      operator: bucket_date
      bucket_date:
        precision: ${date-precision} # Options: hour, day, week, month
    ```

=== "Example"

    ```yaml
    mask:
      operator: bucket_date
      bucket_date:
        precision: month 
    ```

In this example, the `precision` field designates the granularity of the date bucketing to be at a 'month' level.


##### **`hash`**

The hashing method is a powerful data masking technique wherein a specific input consistently produces an identical fixed-size byte string, commonly referred to as a 'hash code'. A notable feature of hashing is its sensitivity to changes in input; even the slightest modification in input can yield a significantly different hash output.

A unique and crucial characteristic of hashing is its irreversibility — once data is hashed, it cannot be converted back to its original state. This property makes hashing a particularly useful technique for masking sensitive textual data, such as passwords, or personally identifiable information (PII), such as names and email addresses.

Hashing involves the use of a specific algorithm that performs the conversion from original data to hashed data. To implement hashing, you will need to specify the hashing algorithm you wish to use. The general syntax structure is as follows:

=== "Configuration Syntax"

    ```yaml
    mask:
      operator: hash
      hash:
        algo: ${algorithm-name}
    ```

=== "Example"

    ```yaml
    mask:
      operator: hash
      hash:
        algo: sha256
    ```

In this YAML configuration, the operator `hash` is specified along with the SHA-256 algorithm (`algo: sha256`). The SHA-256 algorithm is a popular choice due to its strong security properties, but other algorithms could be used as per your requirements.

Remember, the `hash` operator is only applicable to textual data types. Attempting to use it on non-textual data types may lead to unintended results or errors. Always make sure the data you wish to mask is compatible with the masking operator you choose.


##### **`redact`**

Redaction is a data masking strategy that aims to obscure or completely erase portions of data. Its real-world analogy can be seen in blacking out sections of a document to prevent sensitive information from being disclosed. When applied to data masking, redaction might involve replacing certain elements in a data field (such as characters in an email address or digits in a Social Security number) with a placeholder string, e.g., "[REDACTED]"

For instance, the gender of every individual could be redacted and substituted with a consistent value, 'REDACTED'. Similarly, an individual's location information (which may include address, zip code, state, or country) could be redacted and replaced with 'REDACTED'.

=== "Configuration Syntax"

    To implement the `redact` operator, the following YAML configuration can be utilized:

    ```yaml
    mask:
      operator: redact
    #   redact:
    #     replacement: ${replacement-string}
    #    hash: 
    #   algo: sha256
    ```

=== "Example"

    ```yaml
    mask:
      operator: redact
      redact:
        replacement: 'REDACTED'
    ```

The `replacement` field determines the string that will replace the redacted portions of data.

##### **`rand_pattern`**

Random Pattern Masking involves the substitution of sensitive data with randomly produced equivalents that maintain the original data's format or structure. The fundamental goal is to ensure that the masked data is statistically representative and retains operational utility while safeguarding critical information. For example, it can be used to replace personal names with random strings or transform real addresses into plausible but entirely fictitious ones.

=== "Configuration Syntax"

    To implement the `rand_pattern` operator, the following YAML configuration can be utilized:

    ```yaml
    mask:
      operator: rand_pattern
      rand_pattern:
        pattern: ${random-pattern}
    ```

=== "Example"

    Below is an example illustrating the usage of the `rand_pattern` operator:

    ```yaml
    mask:
      operator: rand_pattern
      rand_pattern:
        pattern: '####-####-####'
    ```

In this instance, the specified pattern '####-####-####' will generate random numbers in a format similar to a credit card number, preserving the structure of the original data but replacing it with randomly generated information.

**Format Preserving Encryption (FPE)**: As the name suggests, this method encrypts data in a way that the output has the same format as the input. For example, if a 16-digit credit card number is encrypted using FPE, the result is another 16-digit number. This maintains functional realism, allowing systems to operate normally with masked data.


##### **`regex_replace`**

The Regular Expression (Regex) Replacement strategy utilizes regular expressions to discern and mask identifiable patterns within the data. The identified patterns can be substituted with a predetermined value or random character(s). This strategy is particularly advantageous for masking data that follows a predictable pattern, such as email addresses, phone numbers, or credit card information.


The `regex_replace` operator requires a `pattern` and a `replacement` field in its configuration. The general syntax structure is as follows. The `pattern` field expects a regular expression pattern as its value, while the `replacement` field expects the desired replacement string.:

=== "Configuration Syntax"

    ```yaml
    mask:
      operator: regex_replace
      regex_replace:
        pattern: ${regex-pattern}
        replacement: ${replacement-pattern}
    ```

=== "Example"

    ```yaml
    mask:
      operator: regex_replace
      regex_replace:
        pattern: .{5}$
        replacement: xxxxx
    ```

In the above example, the regular expression`.{5}$` represents any five characters at the end of a string. These characters will be replaced by 'xxxxx'. Here, the regular expression `[0-9]` denotes any single digit which will be replaced with '#'.


=== "Configuration Syntax"

    ```yaml hl_lines="4-5"
    mask:
      operator: regex_replace
      regex_replace:
        pattern: '[0-9]'
        replacement: '#'
    ```


=== "Example"

    ```yaml hl_lines="4-5"
    mask:
      operator: regex_replace
      regex_replace:
        pattern: '[0-9](?=.*.{4})'
        replacement: '#'
    ```

In this case, the regex pattern `[0-9](?=.*.{4})` identifies a digit followed by at least four characters. This digit will be replaced by '#'.


##### **`pass_through`**

The "Pass Through" strategy is used when certain data elements should not be masked or altered. With this technique, data developers can specify that certain data fields remain unchanged during the masking process. This approach is suitable for data that doesn't contain sensitive information or data that is already anonymized.

To implement the `pass_through` operator, the following YAML configuration can be utilized:

```yaml
mask:
  operator: pass_through
```

---

#### **`filters`**

The data visibility for end users is limited due to the filtering policy. You can build a policy to eliminate results from a query's result set depending on comparison operators specified on a column, for example, some users won't be able to see data from the 'Florida' area.

| **Data Type**     | **Requirement** | **Default Value** | **Possible Value** |
| ----------------- | --------------- | ----------------- | ------------------ |
| list of mappings  | optional        | none              | depends on the filter pattern utilized |


**Example Usage:** 

```yaml
filters: 
  - column: ${store_state_code}
    operator: ${not_equals}
    value: ${TN}
```
##### **`column`**

**Description:** column name<br>

| **Data Type**     | **Requirement** | **Default Value** | **Possible Value** |
| ----------------- | --------------- | ----------------- | ------------------ |
| string            | mandatory       | none              | valid column name  |

**Example Usage:** 

```yaml
column: store_state_code
```

##### **`operator`**

**Description:** filter operator name<br>

| **Data Type**     | **Requirement** | **Default Value** | **Possible Value** |
| ----------------- | --------------- | ----------------- | ------------------ |
| string            | mandatory       | none              | equals/not_equals  |


**Example Usage:** 

```yaml
operator: not_equals
```

##### **`value`**

**Description:** value on which filter is to be applied<br>

| **Data Type**                   | **Requirement** | **Default Value** | **Possible Value**              |
| ------------------------------- | --------------- | ----------------- | --------------------------------|
| depends on `column` data type   | mandatory       | none              | any value within the column      |


**Example Usage:** 

```yaml
value: TX
```