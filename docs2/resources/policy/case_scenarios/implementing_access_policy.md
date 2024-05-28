# Implementing Access Policy

## Granting Access to Users Using Pre-defined Tags

### **Sample Ingested Dataset**

Access to ingested datasets on Workbench is denied by default due to the DataOS default policy applied during installation, which restricts all DataOS users from accessing these datasets.

![Sample inaccessible dataset](./implementing_access_policy/access_denied.png)
<center><i>Dataset access denied</i></center>

## Implementation of Access Policy

### **Creating a YAML Configuration**

To enable access to the dataset, a Policy Resource can be used to grant access to pre-existing users or a subset of those users. Below is an example Policy configuration:

```yaml
version: v1
name: test-policy-allowing-access
type: policy
layer: user
description: "Policy allowing all users"
policy:
  access:
    subjects:
      tags:
        - "roles:id:*"                  # Default tag for DataOS users
        - "users:id:*" 
    predicates:
      - "read"
    objects:
      paths:                            # Sample dataset resource
        - "dataos://icebase:sample/test_dataset"
    allow: true                        # Granting access
```
<center><i>Example of an Access Policy</i></center>

## Applying the YAML

To create a Policy Resource in the DataOS environment, open the DataOS CLI and use the apply command with the provided YAML file.

```shell
dataos-ctl apply -f {{file path}}
```

Once the Policy is applied, all users will be able to access this dataset from Workbench.

![Access allowed](./implementing_access_policy/allow_access.png)
<center><i>Dataset accessible after implementing the Policy</i></center>

## Granting Access via Custom Tags

Alternatively, an Access Policy can be created to allow access to the dataset for users with a specific custom tag.

### **Creating a Policy YAML**

Create a new Policy to allow access to the resource (sample dataset in this example) for users possessing a custom tag. Here is an example YAML configuration for such a policy:

```yaml
name: test-policy-allowing-access
version: v1
type: policy
layer: user
description: "Policy implementation to allow users having custom tag 'roles:id:test:user'"
policy:
  access:
    subjects:
      tags:
        - "roles:id:test:user"          # Custom tag
    predicates:
      - "read"
    objects:
      paths:                            # Sample dataset resource
        - "dataos://icebase:sample/test_dataset"
    allow: true
```

### **Applying the YAML**

Open the DataOS CLI and use the apply command to create a Policy Resource in the DataOS environment.

```shell
dataos-ctl apply -f access_policy_allowing.yaml
```

### **Adding Custom Tag to User**

To allow a user to access the sample dataset, add the custom tag using the following CLI command. The custom tag will be listed in the output for the user.

```shell
dataos-ctl user tag add -i 'iamgroot' -t 'roles:id:test:user'

# Expected Output

INFO[0000] 🏷 User tag added.                            
INFO[0000] New tags: roles:id:test:user                 
INFO[0003] 🏷 User tag added successfully.               

        ID       |              TAGS               
----------------|---------------------------------
    iamgroot    | roles:direct:collated,          
                | roles:id:data-dev,              
                | roles:id:depot-manager,         
                | roles:id:depot-reader,          
                | roles:id:operator,              
                | roles:id:system-dev,            
                | roles:id:test:user,             
                | roles:id:user,                  
                | users:id:iamgroot
```

These tags can also be viewed in the user's profile on the DataOS UI.

![Tags on user’s profile page](./implementing_access_policy/ui_new_tag.png)

<center><i>Tags displayed on user's profile page</i></center>

The user with the identifier 'iamgroot' can now access and query the sample dataset due to the access policy implemented with the custom tag.

The following screenshot displays the query result on the DataOS Workbench.

![Access allowed](./implementing_access_policy/allow_access.png)

<center><i>Dataset accessible after adding a custom tag</i></center>