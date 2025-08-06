---
title: Grant
search:
  boost: 4
---

# :material-card-account-details-star-outline: Grant

A Grant [Resource](/resources/) links the Subject-Predicate-Object relationship, generating an access [policy](/resources/policy/). Through grants, administrators assign use cases to subjects either as users or roles, granting them access to specific parts of the system or data. This level of detail in access control enables administrators to regulate user interactions effectively. Grants facilitate the assignment of use cases to multiple roles and users, providing flexibility in access management. Grants can be implemented via [CLI](/interfaces/cli/) or through the [Bifrost](/interfaces/bifrost/) Interface. To learn about how  to create grant through Bifrost click [here](/interfaces/bifrost/grants/#how-to-create-policy-use-case-grant).

## How to create and manage a Grant Resource?

### **Create a Grant manifest file**

Data Developers can create a Grant Resource by applying the manifest file of a Grant from the DataOS CLI. An example of a grant manifest is as follows:

???tip "Example Grant manifest"

    ```yaml
    name: test-user-runas-test-dev1
    version: v1alpha
    type: grant
    layer: user
    tags:
      - governance
      - grant
    grant:
      policy_use_case_id: run-as-user
      subjects:
        - users:id:test-user
      values:
        run-as-dataos-resource: 
         - path: ${valid-path}
      requester: iamgroot
      notes: the user test-user needs to run as the test-developer for data dev purposes
      approve: false
    ```
*The above YAML artifact defines a grant named "test-user-runas-test-dev1" for allowing the user "test-user" to run as a "test-developer" for data development purposes.*

The manifest for creating a Grant has the following two sections:

- [Resource meta section](#resource-meta-section)
- [Grant-specific section](#grant-specific-section)

### **Resource meta section**

In DataOS, a Grant is categorized as a [Resource-type](/resources/types/). The Resource meta section within the manifest file encompasses attributes universally applicable to all Resource-types. The provided manifest file elucidates the requisite attributes for this section:

=== "Syntax"

      ```yaml
      # Resource-meta section
      name: ${resource-name}
      version: v1alpha
      type: grant
      tags:
        - ${tag1}
        - ${tag2}
      description: ${description}
      owner: ${userid-of-owner}
      layer: user
      grant:
        # attributes of grant-specific section
      ```
=== "Example"

      ```yaml
      # Resource-meta section
      name: test-user-runas-test-dev1
      version: v1alpha
      type: grant
      description: ${description}
      tags:
        - governance
      owner: ${iamgroot}
      layer: user
      grant:
        # attributes of grant-specific section
      ```

For more information about the various attributes in Resource meta section, refer to the [Attributes of Resource meta section.](/resources/manifest_attributes/)

### **Grant-specific section**

The Grant-specific section of a Grant manifest comprises attributes-specific to the Grant Resource.

=== "Syntax"

      ```yaml
      grant:
        policy_use_case_id: ${policy-use-case-id}
        subjects:
        - ${users:id:test-user}
        values:
          run-as-dataos-resource: 
          - path: ${valid-path}
        requester: ${iamgroot}
        notes: ${the user test-user needs to run as the test-developer for data dev purposes}
        approve: ${false}
      ```
=== "Example"

      ```yaml
      grant:
        policy_use_case_id: run-as-user
        subjects:
        - users:id:test-user
        values:
          run-as-dataos-resource: 
          - path: ${valid-path}
        requester: iamgroot
        notes: the user test-user needs to run as the test-developer for data dev purposes
        approve: false
      ```
| Attribute          | Data Type        | Default Value | Possible Values                                | Requirement |
|--------------------|------------------|---------------|------------------------------------------------|-------------|
| [`grant`](/resources/grant/configurations/#grant)               | mapping          | none          | valid grant-specific attributes               | mandatory   |
| [`policy_use_case_id`](/resources/grant/configurations/#policy_use_case_id) | string           | none          | Unique identifier for the policy use case      | mandatory   |
| [`subjects`](/resources/grant/configurations/#subjects)            | list of strings  | none          | List of subject identifiers                    | optional    |
| [`values`](/resources/grant/configurations/#values)              | list of mapping  | none          | List of key-value pairs representing values   | mandatory   |
| [`path`](/resources/grant/configurations/#path)                 | string           | none          | valid path string indicating the resource location | optional    |
| [`approve`](/resources/grant/configurations/#approve)             | boolean          | false         | true, false                                    | optional    |
| [`requester`](/resources/grant/configurations/#requester)           | string           | none          | Unique identifier for the requester            | optional    |
| [`notes`](/resources/grant/configurations/#notes)               | string           | none          | Textual notes or comments                      | optional    |
| [`collection`](/resources/grant/configurations/#collection)          | string           | none          | Unique identifier for the collection           | optional    |
| [`manageAsUser`](/resources/grant/configurations/#manageAsUser)       | string           | none          | UserID of the Use Case Assignee                | optional    |


To know more  about the grant attributes click [here](/resources/grant/configurations/)

<aside class="callout">
🗣  By default, the `approve` attribute is set to false. This signifies that grants specified in this YAML file are not automatically approved. Instead, they will appear as requests in the grant request section.
</aside>

Before applying any manifest, it's considered a best practice to lint the manifest file to fix potential issues in manifest.

### **Apply the Grant manifest**

After successfully creating the Grant manifest, it’s time to apply manifest. To apply the Grant manifest, utilize the `apply` command. 

Upon applying the grant, administrators can track and manage grant requests through the Bifrost UI. The applied grant are reflected in the grant request tab, providing administrators with an interface to oversee, approve, reject, or delete grant requests as needed. 

=== "Syntax"

      ```bash
      dataos-ctl resource apply -f ${manifest-file-path} 
      ```

=== "Example"

      ```bash
      dataos-ctl resource apply -f grant.yaml  
      #Expected Output 
      INFO[0000] 🛠 apply...                                   
      INFO[0000] 🔧 applying test-user-runas-test-dev1:v1alpha:grant... 
      INFO[0001] 🔧 applying test-user-runas-test-dev1:v1alpha:grant...updated
      ```

After applying for the Grant via the CLI, the status or log can be viewed in the Grant request section of the Bifrost UI as following. 

<div style="text-align: center;">
  <img src="/resources/grant/grant1.png" alt="grant1" style="border:1px solid black; width: 80%; height: auto;">
  <figcaption><i>*user shraddhaade requested access to read resource system workspaces for user named test-developer to piyushjoshi*</i></figcaption>
</div>

Once the grant request is submitted, the operator views the request and makes a decision. If another operator views the request and finds it appropriate, they can also grant the request. 

<div style="text-align: center;">
  <img src="/resources/grant/grant2.png" alt="grant2" style="border:1px solid black; width: 80%; height: auto;">
</div>

The name of the operator who took the final decision will be recorded

<div style="text-align: center;">
  <img src="/resources/grant/grant3.png" alt="grant3" style="border:1px solid black; width: 80%; height: auto;">
  <figcaption><i>*operator named aayushisolanki granted this permission to test-developer*</i></figcaption>
</div>

## Managing Grant

### **Verify Grant creation**

To check the successful creation of Grant in DataOS Workspace use the following two methods:

- **Check the Grant in a Workspace:** Use the following command to list the grant

```bash
dataos-ctl resource get -t grant 
```

- **Retrieve all Databases in a Workspace:** To retrieve the list of all Grants created, add the `-a` flag to the command:

```bash
dataos-ctl resource get -t grant -a
```

### **Debugging a Grant**

When a Grant creation encounter errors, data developers can employ various tactics to diagnose and resolve issues effectively using command:

```bash
dataos-ctl get -t grant -n test-user-runas-test-dev1 -d
```

## Deleting a Grant

To delete Grant that are no longer in use the following methods:

=== "Method1"

    ```bash
    dataos-ctl delete -t ${grant} -n ${name of grant}
    ```

=== "Method2"

    ```bash
    dataos-ctl delete -i ${name to workspace the in the output table from get status command}
    ```

=== "Method3"

    ```bash
    dataos-ctl delete -f ${file-path}
    ```