# Users

The user tab on Bifrost lists all the applications which have, & the people who have access to DataOS. In addition to this, you can add new users by clicking on the ‘Create User’ button. Currently, Bifrost only allows you to add an application as a new user. You should go to your organisation’s Active Directory to add new people.

<aside>
🗣️ If you add a person as a new user through Bifrost without first including this person in your organisation’s AD, it will create an empty user who cannot perform any actions.

</aside>

To get the details of any user, such as their contact details, tags and access permissions, click on the user's name or anywhere on the row. The pop-up window appearing from the right will give you all the details. You can check their DataOS id, email and type (human or machine) here.

It will also show you all the roles this user has been assigned. You can delete a role-tag if it is no longer required for the user to have access corresponding to that particular role.

Scrolling down, you can check all the use-cases granted to this user. This lets you pinpoint precisely what action the user can perform on which part of the system.

## Manage User

The key feature here is that you can control the access that a user has via the following options -

- Add Role: Click on Add Role to assign the user new roles and corresponding permissions.
- Grant Use-Case: Instead of assigning all the permissions associated with a role, you can choose to grant only a specific use-case to the user, thus limiting their access to precisely what is necessary & sufficient in the given situation.
- Add Tag: You can add new tags to the list of attributes that the user has. Note that only those tags that have already been included in one of the Tag-Namespaces can be added.

There’s a difference between what happens when you assign a Role to a user versus when you Grant a Use-case. Let’s take the example of the use-case to create depots. 

- To provide this permission to the user, you can assign that person the following roles:
    
    `roles:id:data-dev`
    `roles:id:system-dev`
    
    The user can now create and manage depots through the DataOS interface and perform other actions unrelated to the depot creation.
    
- The other way to authorize the user to create Depots is to grant the use-case ‘Write Depot - DataOS Address’ to the user. This will allow the user to create Depot but not perform any other action. Also, while creating the Depot, the user now has to include a new key-value property in the config file of Depot. They must declare the operator's id who authorized them to create Depot. This is how it is done:
    
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
    
    The reason for this is that the user is able to create the Depot via the Operator and not as a result of the attributes associated to their own profile.
    

Another aspect is that of associating new key-value property to a user. We have explained it below.