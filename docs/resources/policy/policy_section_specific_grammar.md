# Policy Section-specific Grammar

## Access Policy

### **`subjects`**

**Description:** a subject is a user that would like to perform a specific predicate on a specific object. It refers to persons or application/services that make the request to perform an action. Attributes of the subject might include tags or groups of tags.

**Data Type:** object

**Requirement:** mandatory

**Default Value:** none

**Possible Value:** none

**Example Usage:**

```yaml
subjects:
  tags:
    -- "roles:id:testuser"
```

---

### **`objects`**

**Description:** the target that the subject would like to perform the predicate on. This can be any target, an API path, a column. The object is the resource (data or service) on which the action is to be performed.

**Data Type:** list of strings

**Requirement:** mandatory

**Default Value:** none

**Possible Value:** any target, api path, tags of requested object, column etc.

**Additional Information:** Predicates are ‘OR’ relationships only, since the PEP is authorizing one action at a time.

**Example Usage:** 

```yaml
objects:
  paths:
    - /dataos/system/themis/**
```

---

### **`tags`**

**Description:** Tags are the attributes of the subject or object. A tag field can contain one single tag or a group of tags in the form of a list. 

**Data Type:** list of strings

**Requirement:** mandatory

**Default Value:** none

**Possible Value:** any valid string

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

**Description:** the action or the verb that the subject would like to perform on the specific object. 

**Data Type:** list of strings

**Requirement:** mandatory

**Default Value:** none

**Possible Value:** crud operations like read, write, update, delete or http operations like get, put, post, delete, options.

**Additional Information:** predicates are ‘OR’ relationships only, since the PEP is authorizing one action at a time.

**Example Usage:** in this example policy, a predicate MUST be `read` OR `write` from the PEP to qualify for this policy to apply.

```yaml
predicates:
  - read
  - write
```

- **Sample Predicates OR Relationship**
    
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
    

---

### **`allow`**

**Description:** action to be allowed or denied

**Data Type:** boolean

**Requirement:** optional

**Default Value:** false

**Possible Value:** true/false

**Example Usage:** 

```yaml
allow: true
```

## Data Policy

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

### **`data`**

**Description:** data policy specific section 

**Data Type:** object

**Requirement:** mandatory

**Default Value:** none

**Possible Value:** none

**Example Usage:** 

```yaml
data:
  {}
```

---

### **`priority`**

**Description:** the policy with higher priority will override all other policies defined for the same resources.

**Data Type:** number

**Requirement:** optional

**Default Value:** none

**Possible Value:** any number between 0-100. 0 being the lowest priority and 100 being the highest

**Example Usage:** 

```yaml
priority: 80
```

---

### **`depot`**

**Description:** name of depot

**Data Type:** string

**Requirement:** optional

**Default Value:** none

**Possible Value:** valid depot name. Use ** for all possible depot names. 

**Example Usage:** 

```yaml
depot: icebase
```

---

### **`collection`**

**Description:** name of the collection

**Data Type:** string

**Requirement:** optional

**Default Value:** none

**Possible Value:** any valid collection name. Use ** for all possible collection names. 

**Example Usage:** 

```yaml
collection: retail
```

---

### **`dataset`**

**Description:** name of dataset

**Data Type:** string

**Requirement:** optional

**Default Value:** none

**Possible Value:** any valid dataset name. Use ** for all possible dataset names. 

**Example Usage:** 

```yaml
predicates:
  - read
  - write
```

---

### **`selector`**

**Description:** selector section

**Data Type:** object

**Requirement:** mandatory

**Default Value:** none

**Possible Value:** none

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

**Description:** section for defining the user 

**Data Type:** object

**Requirement:** mandatory

**Default Value:** none

**Possible Value:** none

**Example Usage:** 

```yaml
user:
  match: any
  tags:
    - "roles:id:testuser"
```

---

### **`match`**
**Description:** This attribute 

**Data Type:** string

**Requirement:** mandatory

**Default Value:** none

**Possible Value:** any/all

**Example Usage:** 

```yaml
match: any
```

---

### [**`tags`**](./policy_section_specific_grammar.md#tags)

---

### **`column`**

**Description:** column section

**Data Type:** object

**Requirement:** mandatory

**Default Value:** none

**Possible Value:** any valid column name

**Example Usage:** 

```yaml
column:
  names:
    - "first_name"
```

---

### **`names`**

**Description:** list of column name

**Data Type:** list of strings

**Requirement:** mandatory

**Default Value:** none

**Possible Value:** valid column names 

**Example Usage:**

```yaml
names:
  - "first_name"
  - "last_name"
```

---

### **`mask`**

**Description:** field for defining the data masking strategy 

**Data Type:** object

**Requirement:** optional

**Default Value:** none

**Possible Value:** depends on the masking strategy utilized

**Additional Information:** for more information regarding the various masking strategies within DataOS refer to the link below

[Masking Strategies](./policy_section_specific_grammar/masking_strategies.md)

**Example Usage:** in this example policy, a predicate MUST be `read` OR `write` from the PEP to qualify for this policy to apply.

```yaml
mask:
  operator: hash
  hash:
    algo: sha256
```

---

### **`filter`**

**Description:** section for defining data filter pattern

**Data Type:** object

**Requirement:** optional

**Default Value:** none

**Possible Value:** depends on the filter pattern utilized

**Additional Information:** 

**Example Usage:** in this example policy, a predicate MUST be `read` OR `write` from the PEP to qualify for this policy to apply.

```yaml
filters: # Filters Section
  - column: store_state_code
    operator: not_equals
    value: TN
```

---

The configurations are summarized in the table given below.

- description - Provide a description to help understand its purpose
- policy - Specify the policy-related configuration properties under the data section
- type: Specify ‘mask’
- priority:
- depot: Mention the depot name to connect to the data source
- collection: Provide the name of collection
- dataset: Provide name of the dataset
- selector: Specify user-related settings under the selector section

| Field | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| filters | object | None | None | Mandatory |
| column | string | None | Any column within the data | Mandatory |
| operator | string | None | not_equals,
 | Mandatory |
| value | string | None | Any value within the column | Mandatory |

## **Masking Strategies**

The strategy chosen for data masking greatly impacts the effectiveness of a data policy. Various strategies such as hashing, bucketing, regular expression replace, format-preserving encryption, and redaction can be employed based on the specific requirements of your data environment. To understand these strategies in depth and to determine the most suitable one for your use case, refer to the resource provided in the following link:

The data visibility for end users is limited due to the filtering policy. You can build a policy to eliminate results from a query's result set depending on comparison operators specified on a column, for example, some users won't be able to see data from the 'Florida' area.

- The filtering policy constraints data visibility for end users.
- You can define a policy to remove rows from the query’s result set based on comparison operators set on a column
- Such as some users cannot see ‘Florida’ region data.
- Filter policy can be defined in the YAML file and applied at the time of the query
- Filter Policy definition consists of configuration settings for the user, columns of the dataset, and masking operator.
- It may include rules for the subject, predicate, and object defining AND/OR relationships.

## Syntax of a Data Filtering Policy

The YAML given below provides a definition of the Data Policy.

```yaml
policy: # Policy Section
	data: # Data Policy Section
	  type: <type> # Type of Data Policy
	  priority: 80 # Priority
	  selector: # Selector
	    user: # User 
	      match: any # Match
	      tags: # Tags
	        - "users:id:iamgroot"
			column: # Column 
	      names: # Name of the Column
	        - "store_state_code"
	  depot: icebase # Depot
	  collection: retail # Collection
	  dataset: store # Dataset
	  filters: # Filters Section
	    - column: store_state_code
	      operator: not_equals
	      value: TN
```

To dive deep into these configuration fields, click on the link below.

[Filter Policy YAML Configuration Field Reference](./policy_section_specific_grammar/filter_policy_yaml_configuration_field_reference.md)

**Filter YAML Configuration**

[YAML](./policy_section_specific_grammar/yaml.md)