# Creating Data Policy (Masking)

Data policy definition consists of configuration settings for the user, columns of the dataset and masking operator.

It may include rules for the subject, predicate and object defining AND/OR relationships.

Follow the steps given below to create a data policy using masking to replace(mask) the original  data with fictitious data to maintain the privacy of sensitive data.

1. Create the YAML file. 
    -  Specify the version, resource name (the policy will be referred to by this name), and resource type (policy). 
    -  Provide layer as ‘user’ or ‘system’. 
        
        `user`: When the resources to be accessed are defined at the DataOS User layer.
        
        `system`: When the resources to be accessed are defined at the DataOS System layer. For example, if you want to read or write from the PostgreSQL database.
        
    -  Provide a description to help understand its purpose.
    -  Specify the policy-related configuration properties under the `data` section.
        
        `type`: Specify “mask”.
        
        `priority`: The policy with higher priority will override all other policies defined for the same resources.
        
        `depot`: Mention the depot name to connect to the data source.
        
        `collection`: Provide the name of collection.
        
        `dataset`: Provide name of the dataset.
        
    -  Specify user related settings under the `selector` section.
        
        `match`: You can specify two operators here. `any` (must match at least one tag) and `all`(match all tags).
        
        `user` : Specify a user identified by a tag. They can be a group of tags defined as an array. See [Rules for AND/OR Logic](./Rules%20for%20AND%20OR%20Logic.md).
        
    -  Specify the columns of the dataset for which data is to be masked.
        
        `names`: Provide names as array.
        
        `tags`: Alternatively, you can also provides tags for the columns.
        
    -  Specify the logic for performing masking on the original sensitive data.
        
        `operator`: This is to specify masking type such as `hash`, `redact`, `pass_through`, etc.
        
        To understand more about the operators through which you can specify masking definitions, refer to [Masking Strategies](../Policy/Policy.md).
        
        You may also need to provide additional information for these operators.
        
        <center>
        
        | Operator | Additional Properties |
        | --- | --- |
        | hash | algo: sha256 <br>*Currently sha256 algorithm is supported. |
        | redact | No additional configuration needed. <br>*Policy will simply redact values of the column based on its type |
        | pass_through | No additional configuration needed <br>*To allow access to the value of columns tagged with fingerprint PII. |
        | bucket_date | bucket_date: <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;precision : "day" <br>*Precision can be year, quarter, month, day. |
        | bucket_number | bucket_number: <br>&nbsp;&nbsp;&nbsp;&nbsp;buckets: <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 10 <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 20 <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 30 <br>*Provide bucket numbers as per requirement. |
        | regex_replace | regex_replace: <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pattern: < regex pattern> <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;replacement: “#” |
        | rand_pattern | rand_pattern: <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pattern: ”###-####-#####” <br>*Provide pattern as per requirement. |
        | rand_regexify | rand_regexify: <br>&nbsp;&nbsp;&nbsp;&nbsp;pattern : {a\|x}(5,10).com <br>*Provide pattern as per requirement. |
        
        </center>
        
        Supported Column Types
        
        The checklist for support of masking strategy by column types is given below.
        
        <center>

        | Type | Text | Number | Date | Object |
        | --- | --- | --- | --- | --- |
        | Hashing | Y | N | N | N |
        | Bucketing | N | Y | Y | N |
        | Regex replace | Y | N | N | N |
        | Format preservation | Y | N | N | N |
        | Redaction | Y | Y | Y | N |

        </center>
        
2. Create the policy resource using the  `apply` command.

## Masking Policy Examples

### Example 1

The following policy will mask the original sensitive data for the given columns using the `sha256` algorithm.

```yaml
version: v1
name: demo-pii-hash
type: policy
layer: user
description: "data policy to hash pii columns by name"
owner:
policy:
  data:
    type: mask
    priority: 99
    depot: raw01
    collection: public
    dataset: store_01
    selector:
      user:
        match: any
        tags:
          - "roles:id:*"
      column:
        names:
          - "first_name"
          - "last_name"
          - "email_id"
    mask:
      # operator: redact
      operator: hash
      hash:
        algo: sha256
```

### Example 2

You can override the masking strategies by using a special policy type- pass_through. This policy will allow access to the value of columns tagged with fingerprint PII.

```yaml
version: v1
name: demo-reader
type: policy
layer: user
description: "policy to allow users with a demo-reader tag to view"
policy:
  data:
    type: mask
    priority: 90
    depot: raw01
    collection: public
    dataset: store_01
    selector:
      user:
        match: any
        tags:
          - "roles:id:demo-reader"
      column:
        names:
          - "first_name"
          - "last_name"
    mask:
      operator: pass_through
```

### Example 3

This policy will allow DataOS admin (user with roles:id:operator tag) to access to the value of columns tagged with fingerprint PII. Here, all the masking strategies are overriden by using a special policy type pass_through.

```yaml
version: v1
name: pii-pass-through
type: policy
layer: user
description: "data policy to pass-through all finger-prints"
owner:
policy:
  data:
    type: mask
    priority: 95
    depot: raw01
    collection: public
    dataset: store_01
    selector:
      user:
        match: any
        tags:
          - "roles:id:operator"
      column:
        tags:
          - "PII.*"
    mask:
      operator: pass_through
```