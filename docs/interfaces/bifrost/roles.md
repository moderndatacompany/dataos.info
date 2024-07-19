
A role in DataOS is a tag present in the tag-namespace called roles, with the glob `roles:**`. It is a way to group two or more subjects that need to share the same level of access to various entities in the ecosystem. The idea of granting same-level access to specific users becomes especially valuable for some particular scenarios.

For instance, when a new project is initiated within your company, involving specific users or team members assigned to work on it, and these individuals or roles require access to the same level of access for project completion, an alternative approach can be adopted. Instead of granting individual access to each person involved in the project, a new role can be created. Subsequently, users can be added to this role. For instance, if the project pertains to the marketing team, the role tag could be defined as `roles:id:marketing:userid`, indicating that this role is specific to the marketing project, granting access to the dataset within a particular database.

The Roles page provides a comprehensive view of system default roles alongside custom roles tailored for specific use cases or as per organizational needs.

<aside class="callout">
🗣 The roles added during the installation process become permanent or default, and cannot be removed thereafter.
</aside>

### Role Detail panel

- **Info:** Displays the Name, ID, Tag, and description of each role.
- **Users:** Presents a list of users associated with selected role.
- **Grants:** This displays the list of use cases possessed by each role. In the subject action, we can observe other roles that were previously assigned a use case in addition to this role.
- **Change Log:** Records all historical changes made to a role, such as ID, subject ID, object ID, action taken ("what"), creation timestamp, object type, and additional details.

## How to create a Role?

To create a custom role follow the below steps:

- Navigate to the Roles. Click on the “Create Role” button in the top right corner.

<center>
  <div style="text-align: center;">
    <img src="/interfaces/bifrost/roles.png" alt="Roles" style="width: 60rem; border: 1px solid black;">
    <figcaption>Roles</figcaption>
  </div>
</center>


- Provide a Name for the role, such as "test role" or “Test Role”s, and add a description if needed. Now, Click on the "Create" button to finalize the creation of the role.

<center>
  <div style="text-align: center;">
    <img src="/interfaces/bifrost/roles2.png" alt="Roles" style="width: 60rem; border: 1px solid black;">
    <figcaption>Roles</figcaption>
  </div>
</center>

- A success message will be displayed confirming that the use case has been successfully added to the role.

!!! Note
    After creating a new role, no users will be displayed initially. You must manually add users by navigating back to the Users tab and repeating the steps to [assign a role to a specific user](/interface/bifrost/users/#how-to-add-a-user-to-a-role).


## How to delete a role?

To delete a specific role follow the below steps:

- Navigate to the roles section
- Click the role you wish to delete 
- Click on “Delete Role” button 

<aside class="callout">
🗣 Deleting a custom role cannot be undone—it results in permanent removal from the system.
</aside>