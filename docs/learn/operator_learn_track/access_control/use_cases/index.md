# Use-cases

This guide provides the end-to-end process for creating and assigning use-cases to Roles and users in DataOS, ensuring that each user has access only to the Resources they need to perform their tasks. It covers the creation of use-cases, the assignment process.

## Scenario

After defining the Roles and responsibilities within your organization (such as `data-dev`, `consumer`, `operator`), aligning with the personas in your organization (such as Data Engineer, Data Analyst, Operator, etc.), you will need to assign use cases to those Roles to manage granular access to Resources within DataOS. This ensures that each Role or user can perform only the actions necessary for their job.

## Understand Use-Cases and Permissions

Before assigning use cases, it's important to understand what they are and how they work. 


A Use-case combines predicates (actions) with the objects (entities upon which actions are performed), defining the set of permissions granted to users. By assigning a Use-case to a Role, such as Iamgroot’s data-dev Role, you link that Role to the specific actions it can perform on certain Resources.

Actions in the use case can range from basic operations like reading, updating, or deleting Resources to more coarser actions like managing specific platform features. For example, if a user is granted the `Manage Lens` use case, they should likely also have the ability to Read Lens, as managing includes actions like creating and updating the Lens in addition to reading it.

However, breaking use-cases into more granular permissions is essential. This level of granularity allows for precise control over which actions a user can perform on a resource. By defining smaller, specific permissions, you can ensure users only have access to what’s necessary, reducing the risk of over-granting access. This granular approach enhances security, compliance, and flexibility, as you can tailor permissions to the user's Roles and responsibilities.

To illustrate, let’s take the Lens resource as an example. A Use-case can be defined as the following:

- **Resource (object):** `Lens` – a dataset, collection, data source, or an API path of an application or service.
- **Action (predicate):** The HTTP operations that can be performed on the resource, such as `read`, `create`, `update`, `delete`.

This results in the following authorization atoms:

- `create on Lens` – Grants permission to create a new lens.
- `read on Lens` – Grants permission to read the lens data.
- `update on Lens` – Grants permission to update the lens data.
- `delete on Lens` – Grants permission to delete the lens data.

Each action represents a separate authorization atom, which helps establish fine-grain access to the resource.

**Applying Granular Access**

Now, let’s explore how granular access applies to two Roles working with the Lens resource: a Data Analyst and a Data Engineer. A Data Analyst typically needs to explore and view the data without making any changes. A Data Engineer, however, requires full access to manage the Lens resource. They need the ability to create, modify, and delete lenses. This grants the Data Engineer complete control over the Lens, enabling them to create, read, update, and delete lens data.

| Aspect                | Data Analyst           | Data Engineer        |
|-----------------------|------------------------|----------------------|
| Primary Goal          | Explore and view the Lens data | Create, manage, update, and delete the Lens |
| Use-Case              | Read Lens              | Manage Lens          |
| Authorization Atom(s) | `read on Lens`         | `create on Lens`, `read on Lens`, `update on Lens`, `delete on Lens` |
| Permissions           | View-only access to Lens data | Full access to create, read, update, and delete Lens data |
| Scope of Access       | Restricted to viewing data | Full control over the resource |


## Creating a Use-Case

Once you understand the concept of use-cases, the next step is to create them. This involves defining the permissions that users or Roles need to interact with Resources. Use-cases are created in YAML format, specifying the actions that can be performed on the Resources.

Follow the steps below to create a use case in DataOS. 

1. You go to the Use-case tab in the Bifrost app and click Create Use-case.

    ![image.png](/learn/operator_learn_track/access_control/use_cases/image (12).png)

2. In the YAML artifact, you define the necessary parameters for the use case. For example, to create a Use-case for reading a DataOS workspace, you will enter the following YAML configuration:

    ```bash
    # Enter the Yaml Use-Case Artifact

    id: read-dataos-workspace
    name: 'Read Workspace'
    description: 'Read workspace in dataos'
    category: data
    authorization_atoms:
    - get-path-ingress
    - read-dataos-workspace  #action+object
    values:
    - authorization_atom_id: get-path-ingress  #
    variable_values:
    - path: /poros/api/v1/workspaces**
    
    ```

3. As you click on the Create button, the Use-case will be recorded in the Use-case list as shown in the below image:
    
    ![image.png](/learn/operator_learn_track/access_control/use_cases/image (13).png)

4. As you click on the newly created use case, you see the details that you gave in the YAML artifact, as shown in the below image:

    ![image.png](/learn/operator_learn_track/access_control/use_cases/image (14).png)

The Image describes the following properties:

- **Info:** This section provides the Use-case's name, ID, and category, allowing you to identify its purpose and classification quickly.
- **Authorization Atoms:** Clicking on a predicate reveals additional details, including the action and the object the action is applied to. For example, clicking on a "get" predicate shows the associated API path, giving you insight into the specific Resources and operations the Use-case grants access to.
- **Variables & Grant:** You can view the variables linked to each authorization atom, such as specific API paths or workspace names. In the **Grant** section, you can see who has been granted access to the Use-case and the associated permissions.

Following are the configurations of creating a Use-case:

| **Key Component** | **Description** | **Example** |
| --- | --- | --- |
| **`id`** | A unique identifier for the use case. | `read-dataos-workspace` |
| **`name`** | Describes the name of the use case. | `'Read Workspace'` - The use case focuses on reading the workspace. |
| **`description`** | A brief explanation of what the use case does. | `'Read workspace in dataos'` |
| **`category`** | Specifies the category of the use case (in this case, it's related to data operations). | `data` , `resource management` etc |
| **`authorization_atoms`** | A list of the authorization atoms required to execute the Use-case. These define the actions (predicates) and access controls applied to Resources. This section includes various authorization atoms (actions), such as creating, updating, deleting, and reading Resources in user layer workspaces, as well as interacting with ingress paths.
| `get-path-ingress`: Action to access the API path (ingress). <br> `read-dataos-workspace`: Action to read (access) the workspace object. |
| **`authorization_atom_id`** | Identifies the specific authorization atom used in the use case. | `get-path-ingress`, `read-dataos-workspace` |
| **`values`** | Defines the variable values associated with the authorization atoms. These values specify the specifics of the action and conditions for performing it. | object |
| **`Address/Path`** | Specifies the address (URL) of the resource (object) in the system. | `path: /poros/api/v1/workspaces**` - The API endpoint for accessing the workspace data. |

Similarly, you create a Use-case to read a depot as shown below:

```bash
# Enter the Yaml Use-Case Artifact

id: read-depot
name: 'Read Depot'
description: 'write depot and its datasets using specific dataset elements'
category: data
authorization_atoms:
  - get-path-ingress
  - read-dataos-workspace
  - read-cluster-dataos-resource
values:
  - authorization_atom_id: get-path-ingress
  variable_values:
    - path: /ds/api/v2/depots/**
```

Similarly, you create a coarser access level Use-case to manage the depot, which combines all the predicates on the Depot type object.

```bash
# Enter the Yaml Use-Case Artifact

id: write-depot-dataset
name: 'Write Depot - Dataset'
description: 'write depot and its datasets using specific dataset elements'
category: data
authorization_atoms:
  - get-path-ingress
  - put-path-ingress
values:
  - authorization_atom_id: get-path-ingress
  variable_values:
    - path: /ds/api/v2/depots/**
    - authorization_atom_id: put-path-ingress
  variable_values:
    - path: /ds/api/v2/depots/**
```

**Use-case to manage lens**
    
```bash
# to create lens

id: manage-lens
name: 'Manage Lens'
description: 'Manage lens in DataOS'
category: resource-management
authorization_atoms:
  - create-in-user-layer-workspace
  - create-lens-user-dataos-resource
  - delete-in-user-layer-workspace
  - delete-lens-user-dataos-resource
  - read-compute-cluster-dataos-resource
  - read-log-depot-system-cluster-dataos-resource
  - read-log-depot-user-cluster-dataos-resource
  - update-depot-system-cluster-dataos-resource
  - update-depot-user-cluster-dataos-resource
  - read-dataos-workspace
  - read-in-user-layer-workspace
  - get-path-ingress
  - put-path-ingress
  - post-path-ingress
  - delete-path-ingress

values:
  - authorization_atom_id: create-in-user-layer-workspace
    variable_values:
      - workspace: public
  - authorization_atom_id: create-in-user-layer-workspace
    variable_values:
      - workspace: sandbox
  - authorization_atom_id: create-lens-user-dataos-resource
    variable_values:
      - workspace: public
  - authorization_atom_id: create-lens-user-dataos-resource
    variable_values:
      - workspace: sandbox
  - authorization_atom_id: update-in-user-layer-workspace
    variable_values:
      - workspace: public
  - authorization_atom_id: update-in-user-layer-workspace
    variable_values:
      - workspace: sandbox
  - authorization_atom_id: delete-in-user-layer-workspace
    variable_values:
      - workspace: public
  - authorization_atom_id: delete-in-user-layer-workspace
    variable_values:
      - workspace: sandbox
  - authorization_atom_id: read-in-user-layer-workspace
    variable_values:
      - workspace: public
  - authorization_atom_id: read-in-user-layer-workspace
    variable_values:
      - workspace: sandbox
  - authorization_atom_id: post-path-ingress
    variable_values:
      - path: /poros/api/v1/workspaces/*/Resources/validate
  - authorization_atom_id: post-path-ingress
    variable_values:
      - path: /poros/api/v1/workspaces/*/Resources/lens
  - authorization_atom_id: post-path-ingress
    variable_values:
      - path: /poros/api/v1/workspaces/*/Resources
  - authorization_atom_id: put-path-ingress
    variable_values:
      - path: /poros/api/v1/workspaces/*/Resources/lens**
  - authorization_atom_id: delete-path-ingress
    variable_values:
      - path: /poros/api/v1/workspaces/*/Resources/lens**
  - authorization_atom_id: get-path-ingress
    variable_values:
      - path: /poros/api/v1/workspaces/*/Resources/lens**
  - authorization_atom_id: get-path-ingress
    variable_values:
      - path: /poros/api/v1/workspaces/*/Resources/lens/log
  - authorization_atom_id: get-path-ingress
    variable_values:
      - path: /poros/api/v1/workspaces/*
```
    
<aside class="callout">
🗣️ This example was created to demonstrate the process of generating a Use-case. We have already defined use-cases by identifying the relevant Resources, Interfaces, and the actions that can be performed on them. However, if new Resource or Interfaces are introduced, you can create additional use-cases.
</aside>

### Assign a Use-Case to a Role or User

After creating use-cases, you will assign them to your organization's relevant Roles and users. This ensures that users in each Role have the correct permissions to interact with the Resources necessary for their tasks.

1. Navigate to Roles and select the "Consumer"  Role with the tag `roleid:consumer`. 

    ![image.png](/learn/operator_learn_track/access_control/use_cases/image (4).png)

2. The Consumer Role Dialog Box appears. In this dialog, you navigate to the Grants section and click on the Grant Use-Case button. In the search box, you enter the newly created Use-case `read lens and contracts`, and click the Grant button. This grants all users in the Consumer Role the ability to read the Lens or semantic model as defined in the Use-case.

    ![image.png](/learn/operator_learn_track/access_control/use_cases/image (5).png)

Next, you follow the same process for the `Data-dev` Role by granting the `Manage Lens` Use-case. This ensures that engineers in the `Data-dev` Role have the necessary permissions to manage the Lens. In contrast, users in the `Consumer` Role receive the appropriate level of access based on their persona. This approach ensures that each user group gets the specific access they need to perform their tasks.

## Assigning the Use-case to user

After assigning use-cases to Roles, there may be situations where individual users need permissions that go beyond the default permissions granted by their Role. For example, although users in the Consumer Role typically do not have the ability to manage the Lens, there may be specific situations where a user from the Consumer Role requires this ability for a particular project.

To handle this, you can assign use-cases directly to the individual user. This allows for more granular control rather than being restricted by the Role's default access settings.

Here's how you can assign use-cases to individual users:

- **Navigate to the User List** You navigate to the User List in Bifrost to view all the users.
    
- **Select the User:** You select the specific user by their name from the list.
    
- **Grant the Use-Case:** You click the Grant Use-Case button in the Grants section of the user's profile.
    
- **Search for the Use-Case:** You search for the required Use-case, such as the `Manage Lens` Use-case.
    
- **Apply the Use-Case to the User:** You grant the selected Use-case to the user.
    
The user now has the required permissions (e.g., to manage Lens) regardless of their original Role's permissions.