### Scenario

Your organization’s data engineering team requires access to a specific Depot for their analytics work. However, data engineers do not have default access to Depots. As an operator, your responsibility is to create a Policy to grant them the appropriate permissions.

We assume you have already created a Role called `data-dev` via Bifrost for this demonstration. This role will only be assigned to your organization's data engineers. To learn how to create roles, [click here]. So, you'll make a Policy to grant access to the `data-dev` role, which is the more efficient approach for broader access.

Before creating a Policy, you will determine the level of access the team needs. In this case, they require permission to read, create, update, and delete data from the Depot, ensuring they cannot modify or delete any resources.

Following are the steps to create and apply the Policy.

### Step 1: Define the resource metadata

First, open your code editor (preferably VS Code) and create a new YAML file named `datd_dev_Policy.yml`. Then, start by defining the Policy's basic metadata. This includes the Policy's name, version, type (which should be `Policy`), and a brief description to clarify its purpose.

Here’s an example of the resource metadata:

```yaml
version: v1
name: "user-access-demo-depots"
type: Policy
layer: user
description: "Policy allowing data engineers to read from demo depots."
```

### Step 2: Define the Policy configuration

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

## Next step

Ater applying the Policy it is time to understand how this Policy will be evaluted.

