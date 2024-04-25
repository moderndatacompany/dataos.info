# Grants

A grant links the Subject-Predicate-Object relationship, generating an access policy. Through grants, administrators assign use cases to subjects either as users or roles, granting them access to specific parts of the system or data. This level of detail in access control enables administrators to regulate user interactions effectively. Grants facilitate the assignment of use cases to multiple roles and users, providing flexibility in access management. Grants can be implemented via [CLI](../interfaces/cli.md) or through the User Interface (UI). To learn about how  to create grant through UI click [here](../interfaces/bifrost_new/grants.md#how-to-create-policy-use-case-grant)

## How to create and manage Grant?

### **Create a Grant manifest file**

When utilizing the CLI, administrators apply the Grant manifest. An example of a grant manifest is as follows:
???tip "Example Grant manifest"

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
*This YAML artifact defines a grant named "test-user-runas-test-dev1" for allowing the user "test-user" to run as a "test-developer" for data development purposes.*

The manifest for creating a Grant has the following two sections:

- Resource meta section
- Grant specific section

### Resource meta section

In DataOS, a Grant is categorized as a [Resource-type](https://dataos.info/resources/types_of_dataos_resources/). The Resource meta section within the manifest file encompasses attributes universally applicable to all Resource-types. The provided manifest file elucidates the requisite attributes for this section:

```yaml
name: test-user-runas-test-dev1
version: v1alpha
type: grant
description: ${description}
tags:
  - governance
owner: ${iamgroot}
layer: user
```

For more information about the various attributes in Resource meta section, refer to the [Attributes of Resource meta section.](../resources/resource_attributes.md)

### **Grant-specific section**

The Grant-specific section of a Grant manifest comprises attributes-specific to the Grant Resource.

```yaml
name: ${grant-name}
version: v1alpha
type: grant
layer: ${user}
tags:
- ${governance}
grant:
  policy_use_case_id: ${policy-use-case-id}
  subjects:
  - ${users:id:test-user}
  values:
    run-as-dataos-resource: 
    - path : ${valid-path}
  requester: ${iamgroot}
  notes: the user test-user needs to runasathe test-developer for data dev purposes
  approve: ${false}
```

| Attribute | Data Type | Default Value | Possible Values | Requirement |
| --- | --- | --- | --- | --- |
| grant | mapping | none | valid grant-specific attributes | mandatory |
| policy_use_case_id | string | none | Unique identifier for the policy use case | mandatory |
| subjects | list of strings | none | List of subject identifiers | optional |
| values | list of mapping | none | List of key-value pairs representing values | mandatory |
| approve | boolean | false | true, false | optional |
| requester | string | none | Unique identifier for the requester | optional |
| notes | string | none | Textual notes or comments | optional |
| collection | string | none | Unique identifier for the collection | optional |
| manageAsUser | string | none | UserID of the Use Case Assignee | optional |

To know more  about the grant attributes click [here](https://www.notion.so/Grants-Attribute-manifest-43172ca953b1493892aabb9a00274e8a?pvs=21)

<aside>
🗣  By default, the **`approve`** attribute is set to false. This signifies that grants specified in this YAML file are not automatically approved. Instead, they will appear as requests in the grant request section.

</aside>

Before applying any manifest, it's considered a best practice to lint the manifest file to fix potential   issues in manifest.

### **Apply the** Grant **manifest**

After successfully creating the Grant manifest, it’s time to apply manifest. To apply the Grant manifest, utilize the `apply` command. 

Upon applying the grant, administrators can track and manage grant requests through the Bifrost UI. The applied grants are reflected in the grant request tab, providing administrators with an interface to oversee, approve, reject, or delete grant requests as needed. 

```yaml
dataos-ctl resource apply -f ${manifest-file-path} 
```

```yaml
dataos-ctl resource apply -f grant.yaml   
INFO[0000] 🛠 apply...                                   
INFO[0000] 🔧 applying test-user-runas-test-dev1:v1alpha:grant... 
INFO[0001] 🔧 applying test-user-runas-test-dev1:v1alpha:grant...updated
```

After applying for the Grant via the CLI, the status or log can be viewed in the Grant request section of the Bifrost UI. 

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/b74fe0cc-bea4-4e10-92c0-4551771d8e1a/Untitled.png)

Once the grant request is submitted, the operator views the request and makes a decision. If another operator views the request and finds it appropriate, they can also grant the request. 

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/6a79bb0e-2952-41aa-929e-d0e7f08db7e0/Untitled.png)

The name of the operator who took the final decision will be recorded

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/9265b9a9-8af7-44d8-b190-7227697032af/Untitled.png)

## **Managing a** Grant

### **Verify** Grant **creation**

To check the successful creation of Grant in DataOS Workspace use the following two methods:

- **Check the Grant in a Workspace:** Use the following command to list the grant

```yaml
dataos-ctl resource get -t grant 
```

- **Retrieve all Databases in a Workspace:** To retrieve the list of all Grants created, add the `-a` flag to the command:

```yaml
dataos-ctl resource get -t grant -a
```

### **Debugging a Grant**

When a Grant creation encounter errors, data developers can employ various tactics to diagnose and resolve issues effectively using command:

```yaml
dataos-ctl get -t grant -n test-user-runas-test-dev1 -d
```

## Deleting a Grant

To delete Grant that are no longer in use the following methods:

Method1:

```yaml
dataos-ctl delete -t ${grant} -n ${name of grant}
```

Method2:

```yaml
dataos-ctl delete -i ${name to workspace the in the output table from get status command}
```

Method3:

```yaml
dataos-ctl delete -f ${file-path}
```

## Possible Errors(WIP)

1. Invalid use case or policy does not exist
2. data type error
3. resource empty error

### End to End Use-case

[End-to-end use -case](https://www.notion.so/End-to-end-use-case-d5fd4432612d440c856be424a34d8c32?pvs=21)

[Grants Attribute manifest ](https://www.notion.so/Grants-Attribute-manifest-43172ca953b1493892aabb9a00274e8a?pvs=21)