# Operator Journey


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
    
    ![Add role](/getting_started/operator/add_role_to_user.png)
    
8. Upon successful assignment, you will see the `roles:id:test-role` role added to the list of the user's existing tags and roles.
    
    ![Role added](/getting_started/operator/role_added.png)


## Secret Management

Operators can create Instance Secret, a DataOS Resource for securely storing sensitive information. This secret can store credentials, keeping them out of codebases and configuration files. It can then be referenced by other DataOS Resources, such as Depots, for secure source system connections.

This can be achieved through the following YAML. 

```yaml
name: depotsecret-rw # Resource name (mandatory)
version: v1 # Manifest version (mandatory)
type: instance-secret # Resource-type (mandatory)
tags: # Tags (optional)
  - just for practice
description: instance secret configuration # Description of Resource (optional)
layer: user
instance-secret: # Instance Secret mapping (mandatory)
  type: key-value-properties # Type of Instance-secret (mandatory)
  acl: rw # Access control list (mandatory)
  data: # Data section mapping (mandatory)
    username: iamgroot
    password: yourpassword

```

Click [here](/resources/instance_secrets/), to access the Resource specific comprehensive documentaion on dataos.info.

## Data Source Connectivity

Operators can create a Depot, a DataOS resource used to connect various data sources to DataOS. Depot enables users to establish connections and retrieve data from various data sources, such as file systems, data lake systems, database systems, and event systems without moving the data. 

```yaml
name: depotsecret
version: v2alpha
type: depot
tags:
  - snowflake
  - depot
layer: user
depot:
  type: SNOWFLAKE
  description: testing instance secrets using snowflake depot
snowflake:
  warehouse: mywarehouse
  url: avengers.central-india.azure.snowflakecomputing.com
  database: mydatabase
  external: true
  dataosSecrets:
    - name: depotsecret-rw
      keys:
        - depotsecret-rw
```

Click [here](/resources/depots/), to access the Resource specific comprehensive documentaion on dataos.info.

## Cluster Management

Gain valuable insights through cluster analysis, enabling operators to understand Cluster usage and optimize available clusters effectively. 

1. Login to DataOS and click on **Superset**. DataOS allows you to integrate external tools seamlessly. 
   
    ![Cluster management](/getting_started/operator/home_superset.png)
   
2. Find Usage Analytics dashboard.

    ![app](/getting_started/operator/cu.png)

3. View the query load distribution along with failed queries for each of the clusters up and running within DataOS instance.

    ![Cluster management](/getting_started/operator/qu.png)

## Monitoring DataOS Resources

Track user, core, and cloud kernel resources, monitoring their utilization and allocation levels directly from the Operations App's interface.

1. Login to DataOS and click on **Operations** app. 
   
    ![app](/getting_started/operator/home_operations.png)

2. You can monitor Core Kernel, Cloud Kernel resources along with resources created by DataOS users,

    ![app](/getting_started/operator/operations_app.png)

3. The "Resources" tab shows the user-created DataOS Resources, such as workflows, services, secrets, depots, clusters, compute, etc. This includes insights into the current running status of these resources, as well as the owner or creator of each resource.

    ![app](/getting_started/operator/operations_workflow.png)

4. Click on the resource to get its details, YAML, and runtime information.

    ![app](/getting_started/operator/resource_runtime.png)

## Monitoring DataOS Infrastructure

Grafana allows you to observe Kubernetes resource (compute & storage) utilization with built-in dashboards. You can leverage Grafana integration to visualize and explore metrics, logs, and traces within the DataOS environment.

1. Login to DataOS and click on **Operations** app. 
   
    ![app](/getting_started/operator/home_grafana.png)

2. On Grafana, you can find a list of various dashboards designed to monitor resources. 

3. Select the dashboard from the list.

    ![app](/getting_started/operator/grafana_dashboard.png)






