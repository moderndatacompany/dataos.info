# Grants

In the Grants section of  Bifrost, administrators can easily track which use cases are assigned to specific roles and users. This level of visibility allows for precise management of user permissions.

To assign a particular use case to multiple roles, create a grant. When administrators create a grant, they define the access policies that govern user interactions with specific resources. Once a grant is created in the Grant section, it can be leveraged as a reusable template for similar access scenarios and employed repeatedly without recreating the entire configuration.

<aside class="callout">
🗣 As part of our best practice, we suggest a cautious approach by setting up restricted access for all users, granting only minimum access privileges. This approach encourages granting access only when necessary and allows flexibility to gradually expand access as visibility and understanding of usage patterns increase over time.
</aside>

## How to create Policy Use-Case Grant?

While it's straightforward to assign use-cases to individual users via the Bifrost UI, there's a rare chance that you may be required to assign a particular use-case to multiple users across different teams, you can accomplish this by following the steps outlined below.

- On Bifrost UI, goto the **Grants** tab, where you can view all the grants (use-cases assigned to users). Click on **Create Grant.**

<center>
  <div style="text-align: center;">
    <img src="/interfaces/bifrost/create_grant.png" alt="Create Grant" style="width: 60rem; border: 1px solid black;">
    <figcaption>Create Grant</figcaption>
  </div>
</center>

-  In the create grant dialog box, define a grant manifest. A sample grant manifest is given

```yaml
policy_use_case_id: manage-pulsar
  subjects:
  - roles:id:operator
```
-  Click on the **Create** button to apply the use-case grant.

Following are some more sample grant manifest

**Sample manifest 1**

**Description:** This use-case authorize actions using a user id assigned to a app-user.

```yaml
policy_use_case_id: authorize-with-userid
subjects:
- roles:id:app-user
```

**Sample manifest 3**

**Description:** This use-case allows certain subejcts identified by tag to read all topics in pulsar.

```yaml
policy_use_case_id: read-topics
subjects:
- roles:id:operator
- roles:id:pulsar-admin
- roles:id:system-dev
- users:id:caretaker
- users:id:pulsar-client-admin
- users:id:usage-collector**
- users:id:poros-recorder**
```

**Sample manifest 4**

**Description:** This use-case allows subjects to create and update governance primitives; roles, providers, atoms, use-cases, grants, policies.

```yaml
policy_use_case_id: create-update-governance-primitives
subjects:
- roles:id:operator
- users:id:dataos-resource-manager
```

**Sample manifest 5**

**Description:** This use-case allows subjects to delete governance-primitives; roles, providers, atoms, use-cases, grants, policies.


```yaml
policy_use_case_id: delete-governance-primitives
subjects:
- roles:id:operator
- users:id:dataos-resource-manager
```

<aside class="callout">
🗣 To remove a specific permission associated with a role, you'll need to delete the corresponding grant.
</aside>