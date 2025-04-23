# How to Govern Talos ?

An **Operator** or **Administrator** can control who can create, read, update, or delete Talos Services by assigning roles or use cases through **Bifrost**.

## Access Permissions for Talos

To create and manage Talos, specific permissions must be assigned. The exact role names and permission levels may vary across organizations based on their governance policies.
 

If granting access through a **use case**, the following use case is required:

- **Manage Talos**
- **Read Talos**

If access is granted using a **role**, the role containing the Talos-related use case must be assigned. For example, the `system-dev` role includes permissions to manage Talos and `data-dev role` includes the premission to read Talos Services.

## How to Grant a Use Case to a User?

### **1. Navigate to DataOS**

- Log in to **DataOS** and select **Bifrost** to launch the interface.

    <div style="text-align: center;">
      <img src="/resources/stacks/talos/recipes/dg_image_0.png" style="border:1px solid black; width: 60%; height: auto;">
    </div>

### **2. Search for the User**

- In **Bifrost**, navigate to the **Users** tab.
- Use the search box to locate the user to whom the use case should be assigned.

    <div style="text-align: center;">
      <img src="/resources/stacks/talos/recipes/dg_image_1.png" style="border:1px solid black; width: 60%; height: auto;">
    </div>

### **3. Select the User**

- Click on the user’s name to view their details.
- Navigate to the **Grants** tab to manage permissions and use cases.
- Click on the **"Grant Use-Case"** button.

    <div style="text-align: center;">
      <img src="/resources/stacks/talos/recipes/dg_image_2.png" style="border:1px solid black; width: 60%; height: auto;">
    </div>

### **4. Search for the Required Use Case**

- A search dialog box will appear.
- Search for **Manage Talos and Read Talos in** User-Specified Workspace.

    <div style="text-align: center;">
      <img src="/resources/stacks/talos/recipes/dg_image_3.png" style="border:1px solid black; width: 60%; height: auto;">
    </div>

After completing, click **"Grant"** to apply the changes. The user’s permissions will be updated, allowing access based on the assigned workspace and role.

This governance model ensures that Talos are securely managed while providing controlled access to authorized users.


## Adding User Groups

Data access in Talos can be governed based on individual users or user groups, allowing control over data visibility and interaction based on each group's role. User groups can be defined in `config.yaml` to control API access.

```yaml
auth:
  userGroups:
    - name: reader
      description: This is a reader group
      includes:
        - roles:id:data-dev
        - roles:id:data-eng
      excludes:
        - users:id:iamgroot
    - name: default
      description: Default group that grants access to all users
      includes: "*"

```

### **User Group Parameters**

- **name**: Defines the name of the user group.
- **description**: Provides a brief description of the user group.
- **includes**: Specifies user roles to be included in the group.
- **excludes**: Specifies user IDs or roles to be excluded from the group.
- `“*”`: Grants access to all users.

<aside class="callout">
🗣 Defining user groups in the `config.yaml` file allows access permissions to be customized, including or excluding specific users or roles as needed.
</aside>

### Case Scenarios

Conside a scenario in which, two users, `user01data` and `user02engg`, have different role assignments. `user01data` holds the `data-dev` role, while `user02engg` has `new-role`, `system-dev`, and `data-dev` roles. Various access control cases are tested based on explicit user inclusion, role-based access, and exclusion rules. 
The table below outlines various authentication test cases with these users:

| **Test Case** | **Included Users** | **Included Roles** | **Excluded Users** | **Excluded Roles** | **Expected Behavior** |
| --- | --- | --- | --- | --- | --- |
| **1. No User or Role Included** | *None* | *None* | *None* | *None* | No access for any user. Error: `[Error [ValidationError]: "auth.userGroups[0].excludes" must be an array]`. |
| **2. User Included Explicitly** | `users:id:user02engg` in `abc` | *None* | *None* | *None* | Only `user02engg` can access `abc`; role-based access is not considered. |
| **3. Both Users Included in Different Groups** | `users:id:user02engg` in `abc` and `users:id:user01data` in `pqr` | *None* | *None* | *None* | Both `user02engg` and `user01data` can access `abc`, as each is explicitly included. |
| **4. Role Included Explicitly** | *None* | `data-dev` in `abc` | *None* | *None* | All users with the `data-dev` role, including `user02engg` and `user01data`, can access `abc`. |
| **5. Both Users and Roles Included** | `users:id:user01data` in `pqr` | `system-dev` in `pqr` | *None* | *None* | `user01data` can access `pqr` due to explicit inclusion, while `user02engg` gains access via the `system-dev` role. |
| **6. User Excluded but Role Included** | *None* | `data-dev` in `abc` | `users:id:user02engg` in `abc` | *None* | `user01data` retains access to `abc` through the `data-dev` role, but `user02engg` is explicitly excluded and cannot access. |
| **7. Role Excluded but User Included** | `users:id:user02engg` in `abc` | `data-dev` in `abc` | *None* | `new-role` in `abc` | `user02engg` has both `new-role` and `data-dev` roles. However, since `new-role` is excluded, only `user01data` can access `abc` via `data-dev`. |
| **8. User in Both Includes and Excludes (Conflict Case)** | `users:id:user01data` in `pqr` | *None* | `users:id:user01data` in `pqr` | *None* | `user01data` is denied access because exclusion overrides inclusion. |
| **9. Role in Both Includes and Excludes (Conflict Case)** | *None* | `data-dev` in `pqr` | *None* | `data-dev` in `pqr` | No user with the `data-dev` role can access `pqr`, as exclusion takes precedence over inclusion. |

