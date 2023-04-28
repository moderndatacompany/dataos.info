# **Creating Access Policy**

Access policy definition consists of configuration settings for the subject, predicate, and object. It may include rules for the subject, predicate and object defining AND/OR relationships.

1. Create the YAML file. 
    - Specify the version, resource name (the policy will be referred to by this name), and resource type (policy). 
    -  Provide layer as **‘user’** or **‘system’**. 
        
        `user`: When the resources to be accessed are defined at the DataOS User layer.
        
        `system`: When the resources to be accessed are defined at the DataOS System layer. For example, if you want to read or write from the PostgreSQL database.
        
    -  Provide a description to help understand its purpose.
    -  Specify the policy-related configuration properties under the `access` section.
        
        `subjects` : Subject can be a user or an application identified by a tag. They can be a group of tags defined as an array. See [Rules for AND/OR Logic](Rules%20for%20AND%20OR%20Logic.md).
        
        `predicates`: Predicate defines an action to be allowed/denied for the underlying resource. You provide multiple possible actions in the form of an array here, but only one action at a time will be considered. See [Rules for AND/OR Logic](Rules%20for%20AND%20OR%20Logic.md).
        
        Refer to the following tables for possible actions specified in the `predicate` section.
        
        **DataOS user:**
        
        <center>
        
        | Action | Description |
        | --- | --- |
        | create | Creates a new resource (for example dataset on a given path) |
        | read | Read the data  |
        | update | Update the data |
        | delete | Delete the data  |
        </center>

        **DataOS Applications can perform API operations on resources:**
        
        <center>
        
        | Action | Description |
        | --- | --- |
        | get | Returns the resource(content/data) |
        | post | Creates a new resource |
        | put | Updates resource by replacing the resource information/content/data |
        | patch | Modifies resource content |
        | delete | Removes resource entirely |
        </center>


        `objects`: Object is a target resource on which the subject would like to perform actions. A tag or path identifies the object. You can specify multiple tags/paths here. See [Rules for AND/OR Logic](Rules%20for%20AND%20OR%20Logic.md).
        
    -  Specify whether you are allowing/denying access to the resource.
2. Create the policy resource using the  `apply` command.

# **Access Policy Examples**

Here are examples of how we can create policies to allow the user to perform certain operations on the resources. 

**Example 1**

The users with `roles:id:testuser` tag can have read permissions on the mentioned depots. 

```yaml
version: v1
name: "user-access-demo-depots"
type: policy
layer: user
description: "policy allowing users to read from demo depots."
policy:
  access:
    subjects:
      tags:
        - - "roles:id:testuser"         # DataOS user
    predicates:
      - "read"                          # Allowed action
    objects:
      paths:
        - "dataos://crmbq**"            # resource paths for Depots
        - "dataos://poss3**"
    allow: true
```

**Example 2**

Only users with DataOS operator(admin) tag can perform CRUD operations on the mentioned depots. 

```yaml
version: v1
name: "user-access-demo-syn-depots"
type: policy
layer: user
description: "policy allowing users to crud demo depots"
policy:
  access:
    subjects:                             
      tags:
        - - "roles:id:operator"           # DataOS admin 
    predicates:                           # Allowed actions (one at a time)
      - "create"
      - "read"
      - "update"
      - "delete"
    objects:
      paths:
        - "dataos://syndicationgcs**".    # resource paths for Depots
    allow: true
```