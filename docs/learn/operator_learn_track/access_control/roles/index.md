This guide outlines the process for creating and managing roles in DataOS, allowing for efficient access control within your organization. It walks you through defining roles, assigning permissions, and ensuring proper access control.

## Scenario

You’ve been tasked with creating and managing roles for different users, especially for those working on specific projects, to group users with similar access needs.

<aside class="callout">
🗣️ Always follow the principle of least privilege.
</aside>

## **What are Roles?**

In DataOS, **Roles** manage user access to resources based on job functions or personas within the organization. Each role defines the user's actions and the resources they can access.

For example:

- The **Data Consumer** role is for users who need **view-only** access, such as **data analysts** or **business stakeholders**.
- The **Data Dev** role is for users like **data engineers** who must **manage** data resources, workflows, and services.

Roles are created to align with specific personas, ensuring users have the appropriate permissions for their responsibilities.

### **What are Tags and Tag Namespaces?**

Tags are central to DataOS’s access control system. A **tag** is an attribute assigned to users or resources that defines what actions can be performed or which resources can be accessed. Tags follow a fixed structure determined by their **Tag-Namespace**.

There are two types of tags:

- **Subject Tags**: Assigned to **users** or **applications** (e.g., `users:id:data-dev`).
- **Object Tags**: Assigned to **resources** or **services** (e.g., `dataos:layer:system`).

A **Tag Namespace** is a container that groups related tags. It helps organize tags logically based on their purpose. For example:

- The `roles:` namespace includes tags like `roles:id:data-dev`, `roles:id:user`, and `roles:id:operator`.
- The `users:` namespace might include tags like `users:id:data-analyst` or `users:id:business-stakeholder`.
- The `dataos:` namespace could include tags like `dataos:layer:system` or `dataos:workflow:execution`.

**Glob Patterns**: Each group uses a glob pattern to define tag structure:

- `roles: roles:**`
- `users: users:**`
- `dataos: dataos:type:**`

**Wildcard Matching**: The `*` in the pattern allows for any specific identifier (e.g., role, user, or data type) to be included under each category, making it flexible for dynamic tag generation.

### **How Roles Work with Tags and Tag Namespaces**

Roles are linked to tags that define the permissions for each role. These tags are associated with predefined **IAM (Identity and Access Management) policies** to enforce access control within DataOS. Tags specify what actions users can perform and which resources they can access.

For example, the **Data Dev** role is identified by the tag `roles:id:data-dev`. The **namespace** for all roles follows the pattern `roles:id:**`, meaning every role tag starts with `roles:id:` followed by the role identifier (e.g., `data-dev`, `data-consumer`). This consistent naming convention helps to easily identify and organize role tags under the `roles:` namespace.

## **Role Mapping to Access Management Groups**

DataOS assigns roles to users according to their group memberships in AMS. For instance, if you define various groups in AMS—such as **user**, **data-dev**, and **operator**—and add users to these groups. The same groups will be reflected in the DataOS as Roles.

For example:

- **data-dev** group maps to the **data-dev** role in DataOS.
- **operator** group maps to the **operator** role.
- **user** group maps to the **user** role.

Once a user logs into DataOS, the system identifies the group(s) they belong to in AMS. DataOS will then automatically assign them the corresponding roles.

For example, if **Iamgroot** is added to both the **data-dev** and **user** groups in AMS, when **Iamgroot** logs into DataOS, the system will automatically assign both the **data-dev** and **user** roles (also identified by tags `roles:id:data-dev` and `roles:id:user`) and grant them the relevant permissions based on each role.

The policies attached to the attached role also automatically get assigned, ensuring access control.

<aside>
🗣

However, you always have the option to create new Roles in Bifrost to meet your organizational needs.

</aside>

## How to create and manage Roles

After creating roles, you must assign users to the appropriate roles,

While DataOS provides default role mappings based on AMS groups, you may occasionally need to create **custom roles** to fulfill specific access requirements that don’t align with the existing AMS groups. 

To create a custom role, follow these steps:

### **Step 1: Identify Job Functions or Departments**

The first step in creating a custom role is identifying the job functions or departments requiring specific access to DataOS resources. For instance, you might define roles for:

- **Job Functions** (e.g., Data Engineers, Consumers)
- **Departments** (e.g., Marketing, Research, Engineering)

For example, you define a ‘Consumer’ role for stakeholders who need access to data but do not need permission to modify it.

### **Step 2: Define the Access Requirements**

Next, define the access permissions for the role, ensuring that users have only the permissions they need to perform their tasks. Follow the principle of **least privilege**, meaning each user should have access to the resources necessary for their job, but not more.

- **Consumer Role**: Grants read-only access to datasets and data resources.
- **Data Dev Role**: Grants full access for data engineers to manage workflows, workers, and services.

For this module, we’ll focus on creating a **Data Consumer** role, assuming the data-dev role already exists in the AMS Group.

### **Step 3: Navigate to the Roles Section in Bifrost**

1. You navigate to the **Roles** tab in **Bifrost.**
2. Click on the **Create Role** button in the top right corner.

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/cd91b24b-d334-4e96-9133-727d354e14f4/image.png)

1. A create role dialog box appears. In this dialog, input the desired **role name** (e.g., **Consumer**) and **description** of the role's purpose or responsibilities. Click the ‘Create’ button to finalize the role's creation. Once the details are entered, click the **Create** button

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/484ddaef-b8fa-4d64-af99-ac0b1a4c671d/bdbba43d-854d-453e-b6c8-e965a29b6d2e.png)

1. Upon successful creation, a confirmation message will appear, indicating that the role has been successfully created. The newly created role will now be visible in the **Roles** tab of the Bifrost interface, as shown in the below image.

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/329290ff-2b61-47c2-8c3a-8e794a9908e4/image.png)

<aside>
🗣️

When you create a new role the system automatically assigns it an **ID**. This ID is usually a lowercase version of the name. For instance, if the role name is `Consumer` the automatically generated ID will be `consumer`.

</aside>

## **How to add users to the created role?**

Once a custom role is created in DataOS, the next step is to assign it to the relevant users. This ensures that users are granted the appropriate access based on their responsibilities.

## Scenario

You have been assigned to add **Iamgroot** to the **Consumer** role. This process involves assigning the correct permissions to **Iamgroot**, ensuring they can access the necessary resources while maintaining the principle of least privilege.

**Navigate to the User Tab in Bifrost**:

You begin by accessing the **Users** section in the Bifrost interface. Use the search bar to find **Iamgroot** by their username or email.

### Steps

You begin by accessing the **Users** section in the Bifrost interface. Use the search bar to find **Iamgroot** by their username or email.

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/e9849ee8-1efa-42ea-a687-93480280b299/image.png)

When you click the Add Role button, the Add Role dialog box opens. Select the Consumer Role and click Add.

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/8c45fdd4-43b7-4da2-8f8d-f232887f17a0/image.png)

With the consumer role successfully assigned, **Iamgroot** is ready to perform his duties and manage the Depot in DataOS.

Now you can see the Iamgroot has a tag associated with the consumer role.

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/4a3a42d1-7163-4c35-a75f-6c153841a153/image.png)

<aside>
🗣

Now, Iamgroot will be granted all the access privileges attached to the Consumer role(if any). 

</aside>