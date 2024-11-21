# Use-cases

This guide provides the end-to-end process for creating and assigning use-cases to roles and users in DataOS, ensuring that each user has access only to the resources they need to perform their tasks. It covers the creation of use-cases, the assignment process.

## Scenario

After defining the roles and responsibilities within your organization (such as `data-dev`, `consumer`, `operator`), aligning with the personas in your organization (such as Data Engineer, Data Analyst, Operator, etc.), you will need to assign use cases to those roles to manage granular access to resources within DataOS. This ensures that each role or user can perform only the actions necessary for their job.

### **Step 1: Understand Use-Cases and Permissions**

Before assigning use cases, it's important to understand what they are and how they work. A use case defines a set of permissions that users have on a specific resource in DataOS, such as Lens, Depot, or Datasets. Each use case will specify which actions can be performed on those resources.

A use-case combines predicates (actions) with the objects (entities upon which actions are performed), defining the set of permissions granted to users. By assigning a use-case to a role, such as Iamgroot’s data-dev role, you link that role to the specific actions it can perform on certain resources.

Actions in the use case can range from basic operations like reading, updating, or deleting resources to more coarser actions like managing specific platform features. For example, if a user is granted the `Manage Lens` use case, they should likely also have the ability to Read Lens, as managing includes actions like creating and updating the Lens in addition to reading it.

However, breaking use-cases into more granular permissions is essential. This level of granularity allows for precise control over which actions a user can perform on a resource. By defining smaller, specific permissions, you can ensure users only have access to what’s necessary, reducing the risk of over-granting access. This granular approach enhances security, compliance, and flexibility, as you can tailor permissions to the user's roles and responsibilities.

To illustrate, let’s take the Lens resource as an example. A use-case can be defined as the following:

- **Resource (object):** `Lens` – a dataset, collection, data source, or an API path of an application or service.
- **Action (predicate):** The HTTP operations that can be performed on the resource, such as `read`, `create`, `update`, `delete`.

This results in the following authorization atoms:

- `create on Lens` – Grants permission to create a new lens.
- `read on Lens` – Grants permission to read the lens data.
- `update on Lens` – Grants permission to update the lens data.
- `delete on Lens` – Grants permission to delete the lens data.

Each action represents a separate authorization atom, which helps establish fine-grain access to the resource.

### **Applying Granular Access**

Now, let’s explore how granular access applies to two roles working with the Lens resource: a Data Analyst and a Data Engineer. A Data Analyst typically needs to explore and view the data without making any changes. A Data Engineer, however, requires full access to manage the Lens resource. They need the ability to create, modify, and delete lenses. This grants the Data Engineer complete control over the Lens, enabling them to create, read, update, and delete lens data.

| Aspect                | Data Analyst           | Data Engineer        |
|-----------------------|------------------------|----------------------|
| Primary Goal          | Explore and view the Lens data | Create, manage, update, and delete the Lens |
| Use-Case              | Read Lens              | Manage Lens          |
| Authorization Atom(s) | `read on Lens`         | `create on Lens`, `read on Lens`, `update on Lens`, `delete on Lens` |
| Permissions           | View-only access to Lens data | Full access to create, read, update, and delete Lens data |
| Scope of Access       | Restricted to viewing data | Full control over the resource |


### **Step 2: Create a Use-Case**

Once you understand the concept of use-cases, the next step is to create them. This involves defining the permissions that users or roles need to interact with resources. Use-cases are created in YAML format, specifying the actions that can be performed on the resources.

[How to create a use-case?]()

### **Step 3: Assign a Use-Case to a Role or User**

After creating use-cases, you will assign them to your organization's relevant roles and users. This ensures that users in each role have the correct permissions to interact with the resources necessary for their tasks.

[How to assign a use-case to a role?]()