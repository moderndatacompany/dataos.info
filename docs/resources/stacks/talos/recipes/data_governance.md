## Data Governance by UI

An **Operator** or **Administrator** can control who can create, read, update, or delete Talos Services by assigning roles or use cases through **Bifrost**.

### **Access Permissions for Talos**

> To create and manage Talos, specific permissions must be assigned. The exact role names and permission levels may vary across organizations based on their governance policies.
 

If granting access through a **use case**, the following use case is required:

- **Manage Talos**
- **Read Talos**

If access is granted using a **role**, the role containing the Talos-related use case must be assigned. For example, the `system-dev` role includes permissions to manage Talos and `data-dev role` includes the premission to read Talos Services.

## **How to Grant a Use Case to a User?**

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

## Data Governance by `config.yml`

Data access can be governed based on individual users or user groups, allowing control over data visibility and interaction based on each group's role. The following sections outline the process of creating user groups in Talos.

## **Adding User Groups**

User groups can be defined in `config.yaml` to control API access.

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