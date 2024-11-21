# Roles

In this guide, you will learn how to create and manage Roles within DataOS using Bifrost, ensuring users are granted the appropriate permissions based on their job functions or departmental needs. You will also explore how Roles are linked to tags for managing access control and how these Roles map to users' responsibilities.

## Scenario

As a DataOS operator, you have been tasked with creating Roles to manage access for different users, based on their project or team requirements. Specifically, you need to create a new Data Consumer Role for stakeholders who need read-only access to data resources, ensuring they have the appropriate permissions while adhering to the principle of least privilege.

<aside class="callout">
🗣️ Always follow the principle of least privilege.
</aside>

Before creating Roles, let us develop a deep understanding of Roles in DataOS.

## Understanding Roles

In DataOS, Roles manage user access to resources based on job functions or personas within the organization. Each Role defines the user's actions and the resources they can access. For example,

- The Data Consumer Role is for users who need view-only access, such as data analysts or business stakeholders.
- The Data Dev Role is for users like data engineers who must manage data resources, workflows, and services.

Roles are created to align with specific personas, ensuring users have the appropriate permissions for their responsibilities.

### How Roles work with Tags and Tag Namespaces?

Roles are linked to tags that define the permissions for each Role. These tags are associated with predefined IAM (Identity and Access Management) policies to enforce access control within DataOS. Tags specify what actions users can perform and which resources they can access.

For example, the Data Dev Role is identified by the tag `Roles:id:data-dev`. The namespace for all Roles follows the pattern `Roles:id:**`, meaning every Role tag starts with `Roles:id:` followed by the Role identifier (e.g., `data-dev`, `data-consumer`). This consistent naming convention helps to easily identify and organize Role tags under the `Roles:` namespace.

## Role mapping to Access Management Groups

DataOS assigns Roles to users according to their group memberships in AMS. For instance, if you define various groups in AMS such as user, data-dev, and operator and add users to these groups, the same groups will be reflected in DataOS as Roles.

**For example:**

- data-dev group maps to the data-dev Role in DataOS.
- operator group maps to the operator Role in DataOS.
- user group maps to the user Role in DataOS.

Once a user logs into DataOS, the system identifies the group(s) they belong to in AMS. DataOS will then automatically assign them the corresponding Roles.

For example, if Iamgroot is added to both the data-dev and user groups in AMS, when Iamgroot logs into DataOS, the system will automatically assign both the data-dev and user Roles (also identified by tags `Roles:id:data-dev` and `Roles:id:user`) and grant them the relevant permissions based on each Role.

The policies attached to the attached Role also automatically get assigned, ensuring access control.

<aside class="callout">
🗣️ However, you always have the option to create new Roles in Bifrost to meet your organizational needs.
</aside>

## Create and manage Roles

While DataOS provides default Role mappings based on AMS groups, you may occasionally need to create custom Roles to fulfill specific access requirements that don’t align with the existing AMS groups.

To create a custom Role, follow these steps:

### Step 1: Identify job functions or departments

The first step in creating a custom Role is identifying the job functions or departments requiring specific access to DataOS resources. For instance, you might define Roles for:

- Job Functions (e.g., Data Engineers, Consumers)
- Departments (e.g., Marketing, Research, Engineering)

For example, you define a ‘Consumer’ Role for stakeholders who need access to data but do not need permission to modify it.

### Step 2: Define the access requirements

Next, define the access permissions for the Role, ensuring that users have only the permissions they need to perform their tasks. Follow the principle of least privilege, meaning each user should have access to the resources necessary for their job, but not more.

- **Consumer Role:** Grants read-only access to datasets and data resources.
- **Data Dev Role:** Grants full access for data engineers to manage workflows, workers, and services.

For this guide, we’ll focus on creating a Data Consumer Role, assuming the data-dev Role already exists in the AMS Group.

### Step 3: Navigate to the Roles section in Bifrost

1. You navigate to the Roles tab in Bifrost.

2. Click on the Create Role button in the top right corner.

    ![image.png](/learn/operator_learn_track/access_control/roles/image (2).png)

3. A create Role dialog box appears. In this dialog, input the desired Role name (e.g., Consumer) and description of the Role's purpose or responsibilities. Click the ‘Create’ button to finalize the Role's creation. Once the details are entered, click the Create button.

    ![image.png](/learn/operator_learn_track/access_control/roles/image (12).png)

4. Upon successful creation, a confirmation message will appear, indicating that the Role has been successfully created. The newly created Role will now be visible in the Roles tab of the Bifrost interface, as shown in the below image.

    ![image.png](/learn/operator_learn_track/access_control/roles/image (3).png)

<aside class="callout">
🗣️ When you create a new Role, the system automatically assigns it an ID. This ID is usually a lowercase version of the name. For instance, if the Role name is `Consumer`, the automatically generated ID will be `consumer`.
</aside>

## Add a user to the Role

Once a custom Role is created in DataOS, the next step is to assign it to the relevant users. This ensures that users are granted the appropriate access based on their responsibilities. 

Follow the below steps:

1. You begin by accessing the Users section in the Bifrost interface. Use the search bar to find Iamgroot by their username or email.

    ![image.png](/learn/operator_learn_track/access_control/roles/image (4).png)

2. When you click the Add Role button, the Add Role dialog box opens. Select the Consumer Role and click Add.

    ![image.png](/learn/operator_learn_track/access_control/roles/image (5).png)

3. With the consumer Role successfully assigned, Iamgroot is ready to perform his duties and manage the Depot in DataOS. Now you can see Iamgroot has a tag associated with the Consumer Role.

    ![image.png](/learn/operator_learn_track/access_control/roles/image (6).png)

Now, Iamgroot will be granted all the access privileges attached to the Consumer Role (if any).
