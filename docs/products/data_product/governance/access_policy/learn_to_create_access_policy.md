---
search:
  exclude: true
---

## Learn to create Access Policy 


The policy includes:

-[ Resource-specific section](/resources/manifest_attributes/): Common for all Resources.
- [Access Policy-specific section]():

```yaml
#Resource-specific section
name: ${{my_policy}}
version: v1
type: policy
tags:
  - ${{policy}}
  - ${{access}}
description: ${{policy_manifest}}
owner: ${{iamgroot}}
layer: users

#Access Policy-specific section
policy:
  access:
    subjects:
      tags:
        - - ${{roles:id:**}}
        - - ${{users:id:**}}
    predicates:
      - ${{create}}
      - ${{read}}
      - ${{write}}
      - ${{put}}
      - ${{update}}
      - ${{delete}}
      - ${{post}}
      - ${{access}}
    objects:
      paths:
        - ${{dataos://lakehouse:retail/city}}
    allow: ${{true}}
    collection: default
    name: ${{test_access_policy}}
    description: ${{description_of_policy}}
```

## Access Policy-specific section


### `subjects.tags`

A subject is a user who would like to perform a specific predicate on a specific object. It refers to persons or applications/services that make the request to act. Subject attributes, such as tags or groups of tags, provide the context used to determine which access policies apply to a request.


In DataOS, subjects are identified using **identity `tags`**, which are used to associate policies with users or roles.

**Examples**

- User identity tag: `users:id:iamgroot`
- Role identity tag: `roles:id:data-dev`
- List of users:

```yaml
subjects:
  tags:
    - users:id:iamgroot
    - users:id:ironman
```


```yaml
subjects:
  tags:
    - "roles:id:testuser"
    - "roles:id:sys-dev"
```

### `predicate`

The action or the verb that the subject would like to perform on the specific object.

**Examples:** `read`, `write`, `create`, `update`, `delete`, `execute`, `access`

> 🗣 Predicates are ‘OR’ relationships only, since the PEP is authorizing one action at a time.

### `object`

The target that the subject would like to perform the predicate on. This can be any target, an API path, a column. The object is the resource (data or service) on which the action is to be performed.

The object is identified using `tags` or `paths` both.

#### `object.tags`

```yaml
objects:
  paths:
    - /dataos/system/themis/**
```

or

#### `object.paths`

```yaml
objects:
  tags:
    - dataos:resource:depot
```


### allow

Action to be allowed or denied. Allows if `true`, denies if `false`.

```yaml
allow: true
```

### description

Provide an accurate description of the access policy.

```yaml
description: this is a access policy
```

### Collection

Collection of the access policy always sets to `default`.

```yaml
collection: default
```

## Combining it all!

Create a new Policy to allow access to the resource (sample dataset in this example) for users possessing a custom tag. Here is an example YAML configuration for such a policy:

```yaml
name: test-policy-allowing-access
version: v1
type: policy
layer: user
description: "Policy implementation to allow users having custom tag 'roles:id:test:user'"
policy:
  access:
    subjects:
      tags:
        - "roles:id:test:user"          # Custom tag
    predicates:
      - "read" 
    objects:
      paths:                            # Sample dataset resource
        - "dataos://lakehouse:sample/test_dataset"
    allow: true
```
