# Attribute of Grant manifest 

## Structure of the grants manifest

```yaml
name: test-user-runas-test-dev1
version: v1alpha
type: grant
layer: user
tags:
- governance
grant:
  policy_use_case_id: run-as-user
  subjects:
  - users:id:test-user
  values:
    run-as-dataos-resource: 
    - path : ${valid-path}
  requester: manish
  notes: the user test-user needs to runas the test-developer for data dev purposes
  approve: false
```

### Attributes of Grant Resource

### **`grant`**

**Description:** Describes the permissions granted for the policy use case.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | required | none | Key-value pairs representing granted permissions |

**Example usage:**

```yaml
grant:
  read: true
  write: false
```

#### **`policy-use-case-id`**

**Description:** Identifier for the policy use case.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | required | none | inique identifier for the policy use case |

**Example usage:**

```yaml
policy-use-case-id: my_policy_use_case
```

#### **`subjects`**

**Description:** List of subjects represented as tags associated with the policy.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of strings | optional | none | list of subject identifiers |

**Example usage:**

```yaml
subjects:
  - user1
  - user2
```

#### **`values`**

**Description:** List of values associated with the policy.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of mapping | optional | none | list of key-value pairs representing values |

**Example usage:**

```yaml
values:
  - path: ds/icebase/retail
```
##### **`path`**

**Description:** Specifies the path value associated with the granted permission.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | valid path string indicating the resource location |

**Example usage:**

```yaml
path: ds/icebase/retail
```

#### **`approve`**

**Description:** Indicates whether the policy is approved or not.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| boolean | required | false | true, false |

**Example usage:**

```yaml
approve: true
```

**`requester`**

**Description:** The user responsible for granting approval for access requests

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | unique identifier for the requester |

**Example usage:**

```yaml
requester: user123
```

#### **`notes`**

**Description:** Additional notes or comments for the policy.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | textual notes or comments |

**Example usage:**

```yaml
notes: This policy is for testing purposes.
```

#### **`collection`**

**Description:** Identifier for the collection associated with the policy.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | unique identifier for the collection |

**Example usage:**

```yaml
collection: my_collection
```

#### **`manageAsUser`**

**Description:** When the `manageAsUser` attribute is configured with the UserID of the use-case assignee, it grants the authority to perform operations on behalf of that user.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | userid of the use-case assignee |

**Example usage:**

```yaml
manageAsUser: iamgroot
```