# User

## Scenario

As a DataOS Operator, you manage users within Bifrost and ensure they have access to necessary resources by assigning appropriate roles and policies. Recently, your data engineering team requested access to manage Depot within DataOS. You have already created a policy for the `data-dev` role; now, you will assign this role to your organization's data engineers to give them access to the Depot. 

Before assigning a role to each user, you should explore the User tab in the Bifrost.

In Bifrost, the Users tab displays a list of users accessing DataOS. Users can be categorized into two types: person and application. New users can be added by clicking the Create User button, but keep in mind the following:

- **Application users** can only be added directly through Bifrost.
- **Person-type users** require access to your organization’s Active Directory (AD) before being added.

<aside class="callout">
🗣️ If you add a person as a new user through Bifrost without first including them in your organization’s AD, it will create an empty user who cannot perform any actions.
</aside>

### User details panel

Clicking on any user will give you detailed info about the particular user. 

1. **Info**: Displays general information or metadata about the user.
    
    ![image.png](/learn/operator_learn_track/access_control/users/image (2).png)
    
2. **Tags**: This section lists the tags associated with the user, who assigned them, and an option to delete tags if necessary.
    
    ![image.png](/learn/operator_learn_track/access_control/users/image (3).png)
    
3. **Grants**: This section summarizes the use cases granted to the user. Clicking on a use case displays the associated tags. You can also grant a new use case to the user.
    
    ![image.png](/learn/operator_learn_track/access_control/users/image (4).png)
    
4. **Change Logs**: Tracks user profile changes, offering an audit trail.
    
    ![image.png](/learn/operator_learn_track/access_control/users/image (5).png)
    
5. **Advanced**: This field contains the federated User ID and Connection ID for authentication. By default, the system uses the federated user ID, but you can add other properties for user identification.
    
    ![image.png](/learn/operator_learn_track/access_control/users/image (6).png)
    