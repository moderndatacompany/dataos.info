# Users

The Users tab in Bifrost presents a list of users who have access to DataOS. Users can be categorized into two types **person** & **application**. Additionally, new users can be added by clicking the ‘Create User’ button. However, it's important to note that new users of type applications, can only be added directly through Bifrost. Adding new user of person type requires access to your organization’s Active Directory.

<aside class="callout">
🗣 If you add a person as a new user through Bifrost without first including this person in your organization’s AD, it will create an empty user who cannot perform any actions.
</aside>

### **User Details Panel:**

Clicking on a user in the list opens a detailed view, showcasing additional information about the user.It contains further additional sections:

1. **Info:** Provides additional information or metadata about the user.
2. **Tags:** Contains the list of tags the user possesses, who assigned it, and an action button to delete the certain tag
3. **Grants:** Displays a summary of use-cases granted to the user. Furthermore, clicking on a use-case will display the list of tags have previously been assigned to this use-case. You can grant a use-case to the user by following these steps(link how to grant use case here).
4. **Change Logs:** Logs any changes to the user's profile, providing an audit trail.
5. **Advanced:** Contains federated user ID and Connection ID. The system assigns a unique identifier known as the federated user ID to each user for identification purposes. By default, the system uses the federated user ID to identify users. Alternatively, you can add other properties for user identification using “Add Property”.

### **How to create a user?**

1. In the top-right corner, the "Create User" button allows administrators to add new users to the system.
2. Upon clicking, a form is presented for entering user details, including Name, ID, and Type of user

Bifrost allows to manage a user's access through the following options:

- **Adding Role:** Users can be assigned new roles and their corresponding permissions by clicking the "Add Role" option.
- **Granting Use-Case:** Instead of assigning all permissions linked with a role, the user is granted specific use-cases, restricting their access to precisely what is required in the given scenario.
- **Adding Tag:** New tags can be added to the list of attributes associated with the user. It's important to note that only tags already included in one of the Tag-Namespaces can be added.

There's a difference between assigning a Role and granting a Use-case to a user. For the sake of illustrating, let's consider allowing the creation of depots needs to have the data-dev and system-dev roles

1. Assign the following roles:
    - `roles:id:data-dev`
    - `roles:id:system-dev`
    
    With these roles, the user can create and manage depots through the DataOS interface and perform other actions unrelated to depot creation.
    
2. Another method to authorize the user to create Depots is by granting the use-case `Write Depot - DataOS Address`. This specific use case allows the user to create depots but doesn't enable other actions. However, the user must include a new key-value property in the Depot's config file. They must declare the ID of the operator who authorized them to create the Depot. This ensures proper authorization. The reason being the user can create the Depot via the Operator and not because of the attributes associated with their profile.

```yaml
version: 
name: 
type: depot
tags:
layer: user
depot:
  type:
  description: 
  external:
  runAsUser: #id of the person who assigned you the use case
  connectionSecret:
  spec:
```

### How to add a user to a role?

To add a user to a role follow the below steps:

1. Navigate to the users and select the desired user.

![user1.png](../bifrost_new/users1.png)

2. Click anywhere on the user's row to access their details. Now, proceed to the "tags" section and click on the "Add Role" button.

![user2.png](../bifrost_new/users2.png)

3. Search for "role pulsar admin" and select it from the options provided. and click on "Add" to assign the role.

![user3.png](../bifrost_new/users3.png)

4. Upon successful assignment, you will see the `roles:id:pulsar-admin` role added to the list of the user's existing tags and roles.

![user4.png](../bifrost_new/users4.png)

As seen, when assigning a role, a corresponding tag is assigned to the user. Alternatively, you can also add the tag directly by following the below steps

## How to add a tag to the user?

1. Navigate to the 'Tags' section in the user's profile.
2. Click on the Add Tag button
3. Type in  the tag Click “Add”

You can observe a newly added tag in the list of existing tags for the user.

For instance, if you wish to assign the user a role called "Pulsar Admin," you must add the tag `roles:id:pulsar-admin`. Similarly, when deleting a specific role assigned to a user, you must remove the associated tag. Follow the below steps to achieve the same

## How to delete a role or tag of a user?

To delete the role or tag of a particular user, follow these steps:

1. Select the user whose role you wish to delete.
2. Navigate to the 'Tags' section in the user's profile.
3. Locate the desired tag to delete.
4. Click on the delete button located in front of the desired role.
5. Confirm the deletion if prompted.

Following these steps will result in the selected role or tag being removed from the user's profile, revoking the associated access permissions.

## How to grant a use case to a user?

1. Navigate to the Grants section of the Users tab on Bifrost and select the particular user.

<center>![grant_usecase_minerva1.png](../bifrost_new/grant_usecase_minerva1.png)</center>
<center>All use-cases assigned to the user are displayed</center>

1. Click on **Grant-Use-case**.
2. In the search-box, type in minerva and select **“Minerva Cluster Access”**.
    
<center>![grant_usecase_minerva2.png](../bifrost_new/grant_usecase_minerva2.png)</center>
<center>Minerva Cluster Access use-case displayed</center>

3. Provide values for the following fields:
    
    | Authorization Atom ID | Variable name | Value |
    | --- | --- | --- |
    | minerva-cluster-access | cluster | miniature |
    | minerva-table-read | catalog | icebase |
    | minerva-table-read | schema | retail |
    | minerva-table-read | table | city |
    | ds-read | depot | icebase |
    | ds-read | collection | city |
    | ds-read | dataset | city |

4. Click on **Grant** 
    
<aside class="callout">
🗣 To grant a use-case to a role follow the same steps just instead of going to user now you will go to roles and select any existing role
</aside>

In addition to granting existing use cases, you can also create a new use-case by generating a YAML use-case artifact. This is particularly useful if you identify a combination of predicate and object that isn't already present but may be relevant to your organization. To initiate the creation of a new use case manifest file, click here(link how to crate new use case here).