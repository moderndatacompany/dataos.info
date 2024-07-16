# Begin Your DataOS Journey


A DataOS Operator is typically responsible for the following activites to ensure smooth operations:

## Access Management

Bifrost ensures flexible and secure access management tailored to diverse use cases. Operator can harness Bifrost's graphical interface to create and manage policies for fine-grained access control across applications, users, services, and stacks.

1. Login to DataOS and click on **Bifrost** app.
   ![Bifrost](/getting_started/operator/home_bifrost.png)

2. Recognize the different roles or job functions that need access to different resources. These roles might include administrators, managers, analysts, or other custom roles based on the organization's needs.

3. On Bifrost, navigate to the **Roles**. 
   You can see some default/predefined roles. Click on the “Create Role” button in the top right corner.
    
    ![roles](/getting_started/operator/roles.png)
    
4. Provide a Name for the role, such as "test role" or “Test Role”s, and add a description if needed. Now, Click on the "Create" button to finalize the creation of the role.
    
    ![Create roles](/getting_started/operator/create_roles.png)
    
5. Now, users within the organization are then assigned to the appropriate roles based on their job functions or responsibilities. Navigate to the users and select the desired user.
    
    ![MicrosoftTeams-image(4).png](/getting_started/operator/users.png)
    
6. Click anywhere on the user's row to access their details. Now, proceed to the "tags" section and click on the "Add Role" button.
    
    ![MicrosoftTeams-image.png](/getting_started/operator/create_roles.png)
    

7. Search for "Test Role" and select it from the options provided. and click on "Add" to assign the role.
    
    ![Screenshot 2024-03-29 at 12.19.51 AM.png](/getting_started/operator/add_role_to_user.png)
    
8. Upon successful assignment, you will see the `roles:id:test-role` role added to the list of the user's existing tags and roles.
    
    ![MicrosoftTeams-image(6).png](/getting_started/operator/role_added.png)


## Monitor Resources

Track user, core, and cloud kernel resources, monitoring their utilization and allocation levels directly from the Operations App's interface.

## Cluster Insights

Gain valuable analytics through cluster analysis, enabling operators to understand and optimize available clusters effectively.


## Query Management

Access comprehensive insights into query status (completed, failed, running) across clusters and users. Debug and manage queries efficiently from within the app's UI.



## Integrate with Grafana

Leverage Grafana integration to visualize and explore metrics, logs, and traces within the DataOS environment. This integration enhances cluster assessment and supports detailed data analysis.

## Create Resources

Utilize the Operations App to create new resources such as Minerva clusters, streamlining the process through its intuitive UI.

These capabilities empower operators to oversee and manage the DataOS platform comprehensively, enhancing observability, resource management, and operational efficiency.