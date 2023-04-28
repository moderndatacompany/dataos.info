# **Rules for AND/OR Logic**

DataOS policies determine which person or application (subject)can access which DataOS resources(objects) to perform allowed action(predicate) and are defined in the `policy.yaml`
file.

The YAML tags field in both subjects and objects is an array of string arrays.
The string array is how you define the AND relationships between tags, or it can be thought of as a group of tags. The structure is an array of arrays which is how you define the OR relationships between tags.

> 🗣️ **Rule 1.** Subjects are defined using one or more tags with AND/OR relationships.

```yaml
# tag1 OR tag2
- - tag1
- - tag2

# tag1 AND tag2
- - tag1
  - tag2

# tag1 OR (tag2 AND tag3)
- - tag1
- - tag2
  - tag3
```

**Example 1**
In this example policy, a subject MUST have the (`roles:id:pii-reader` **AND** `roles:id:testuser`) tags attributed to qualifying for this policy to apply.

```yaml
version: v1
name: subject-example1
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

**Example 2**

In this example policy, a subject MUST have the (`roles:id:pii-reader` AND `roles:id:testuser`) **OR** `roles:id:marketing-manager` tags attributed to qualifying for this policy to apply.

```yaml
version: v1
name: subject-example2
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

> 🗣 **Rule 2:** Predicates are the string array of actions that the policy will apply to. Predicates are ‘OR’ relationships only since the PEP is authorizing one action at a time.

**Example** 

In this example policy, a predicate MUST be `read` **OR** `write` from the PEP to qualify for this policy to apply.

```yaml
version: v1
name: predicate-example2
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

> 🗣 **Rule 3:** Objects are defined on resource paths or using one or more tags that must be an attribute of the requested object.

**Example 1**

In this example policy, an object MUST have the resource path of `/metis/api/v2/workspaces/public` **OR** `/metis/api/v2/workspaces/sandbox`to qualify for this policy to apply.

```yaml
version: v1
name: object-example1
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

**Example 2**

In this example policy, an object MUST have the `PII.Email` **OR** `PII.Sensitive` tags attributed to qualifying for this policy to apply.

```yaml
version: v1
name: object-example2
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
<br>

### **Evaluating List Attributes using Wildcard**

You may use a wildcard (`*`) or (`**`) to evaluate all items within a list.  If *any* item in the list matches the condition, then the condition passes.

The symbol (`:`) is a delimiter in the tags field and paths field, and predicates field; additional syntax includes:

<center>

| Symbol | Example | Description |
| --- | --- | --- |
| single symbol wildcard: `?` | ?at | matches cat and bat but not at |
| wildcard: `*` | foo:*:bar | matches foo:baz:bar and foo:zab:bar but not foo:bar nor foo:baz:baz:bar |
| super wildcard: `**` |  foo:**:bar | matches foo:baz:baz:bar, foo:baz:bar, and foo:bar, but not foobar or foo:baz |
| character list: [] | [cb]at | matches cat and bat but not mat nor at |
| negated character list: [!] | [!cb]at | matches tat and mat but not cat nor bat |
| ranged character list:[-] | [a-c]at | cat and bat but not mat nor at |
| negated ranged character list: [!-] | [!a-c]at  | matches mat and tat but not cat nor bat |
| alternatives list: {[]} | {cat,bat,[mt]at}  | matches cat, bat, mat, tat and nothing else |
| backslash (escape):\ | foo\\bar | matches foo\bar and nothing else |
|  | foo\bar  | matches foobar and nothing else |
|  | foo\*bar | matches foo*bar and nothing else |

<center>