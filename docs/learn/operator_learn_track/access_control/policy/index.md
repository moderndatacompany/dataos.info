# Policy

In this guide, you will learn how to create and configure Policies in DataOS to manage access to resources. Specifically, it will walk you through granting appropriate permissions to a Role, ensuring efficient and secure access for your organization's teams.

## Scenario

Your organization’s data engineering team requires access to a specific Depot for their analytics work. However, data engineers do not have default access to Depots. As an operator, your responsibility is to create a Policy to grant them the appropriate permissions.

We assume you have already created a Role called `data-dev` via Bifrost for this demonstration. This role will only be assigned to your organization's data engineers. To learn how to create roles, [click here]. So, you'll make a Policy to grant access to the `data-dev` role, which is the more efficient approach for broader access.

Before creating a Policy, you will determine the level of access the team needs. In this case, they require permission to read, create, update, and delete data from the Depot, ensuring they cannot modify or delete any resources.


## Policy

Policy are based on Attribute-Based Access Control (ABAC) strategy. These policies specify which subjects (users or applications) can perform certain actions (predicates) on objects (resources), based on the attributes associated with them.

Following are the steps to create and apply the Policy.

### **Step 1: Define the resource metadata**

First, open your code editor (preferably VS Code) and create a new YAML file named `datd_dev_Policy.yml`. Then, start by defining the Policy's basic metadata. This includes the Policy's name, version, type (which should be `Policy`), and a brief description to clarify its purpose.

Here’s an example of the resource metadata:

```yaml
version: v1
name: "user-access-demo-depots"
type: Policy
layer: user
description: "Policy allowing data engineers to read from demo depots."
```

### **Step 2: Define the Policy configuration**

Next, you'll define the specific access control settings for the Policy. This is done by specifying the subjects, predicates, and objects:

- **Subjects**: Define the users or applications to which the Policy applies. Here, you’ll use the `roles:id:data-dev` tag to apply the Policy to data engineers.
- **Predicates**: Define the allowed actions (or operations) for the subject. In this case, the actions are related to data access, such as `read`, `update`, or `delete`.
- **Objects**: Define the resources (such as datasets or API endpoints) the Policy applies to. You can specify resources using paths or tags. Here, the objects are the demo Depots located at `dataos://crmbq` and `dataos://poss3`.

You will also set the `allow` attribute to `true` to grant access.

Here’s how to define the full Policy configuration:

```yaml
version: v1
name: "user-access-demo-depots"
type: Policy
layer: user
description: "Policy allowing data engineers to read from demo depots."
Policy:
  access:
    subjects:
      tags:
        - "roles:id:data-dev"  # Applies to users with the 'data-dev' role
    predicates:
      - "read"  # Allow reading access
      - "update"
      - "delete"
      - "create"  # Allow all relevant actions
    objects:
      paths:
        - "dataos://crmbq**"  # Resources: demo depots
        - "dataos://poss3**"
    allow: true  # Grant access

```

This Policy grants `data-dev` roles, which means all the data engineers have access to manage the Depots located at `dataos://crmbq` and `dataos://poss3`.

## Step 3: Apply Policy manifest file

Use the following command to apply the Policy Resource.

```
dataos-ctl apply -f apply /access_policy.yml
```

## Policy evaluation

After applying the Policy it is time to understand how this Policy will be evaluted.

Policies are evaluated dynamically by the Policy Decision Point (PDP), which uses attributes (tags) associated with the subject, object, and predicate to decide whether to grant or deny access.

- **Policy Decision Point (PDP)**: The PDP evaluates whether the policy allows the requested action. It processes the request, compares the subject’s attributes (e.g., roles or grants), and the object’s attributes (e.g., visibility, access level), and decides whether to permit or deny the request. Heimdall, the governance engine within DataOS, ensures granular access control over datasets, API paths, and applications. Acting as the Policy Decision Point (PDP), it manages authorizations and access across all data products through native governance, ensuring secure interactions at every level.

- **Policy Enforcement Point (PEP)**: Once the PDP makes a decision, the PEP enforces that decision by allowing or blocking the user’s action.