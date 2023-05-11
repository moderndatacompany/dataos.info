# Policy Implementation Use Case

Data is an asset. You need to carefully craft the governance policies to safeguard the data. Designing and implementing Access and Data control policies are high-level requirements that specify how access is managed and who may access information under what circumstances.

## Policy Creation Guidelines

Follow the below steps to implement DataOS Governance policies for a new project and add users to the project:

1. Identify and prioritize existing data based on client requirements and needs.
2. Identify the users who should have access to project-specific data.
3. After getting complete clarity, <span style="color:blue">create tags</span> for different types of users within the organization.
4. Define and apply <span style="color:blue">access policies</span> based on the tags created.
5. Identify data that need to be masked or filtered to protect the privacy of the data.
6. Create and apply <span style="color:blue">data policies</span> on these identified data by using the best suitable masking strategy and filter policies.

## Design and Implement Policies

Suppose your team is analyzing customer data from a large retail chain. For security and privacy concerns, you have to make this dataset available to a few authorized users and also hide PII information for regulatory compliance.  It's your job to find out how to accomplish this.

This tutorial takes you through the entire process of developing and implementing various policies in DataOS.

As you work through this tutorial, you will learn to design and implement multiple policies for authorized access and data protection for the sample dataset. You will also observe the behavior after implementing the policies.

## Prerequisites

To begin with this tutorial, you should have:

- CLI installed.
- Operator tag to add custom tags and apply policies.
- DataOS Governance and Policies understanding (Basic).
- The sample dataset is ingested.

## Sample Dataset

This is the sample customer data used for applying various access and data policies (dataset name: test_dataset).

Customer Data from the sample dataset on DataOS Workbench:
 
<center>

![Picture](./Policy%20Implementation%20Use%20Case/default_accessible_wb.png)

</center>

<figcaption align = "center">Sample dataset</figcaption>
<br>

> 🗣 You are able to query it on Workbench because the  DataOS default policy applied at the time of installation allows all dataOS users to access the ingested datasets.

## Access Policy Implementation

1. For demonstration purposes, we will create a policy to deny access to all users to this dataset.
    
    ```yaml
    version: v1
    name: test-policy-usecase-denying-access
    type: policy
    layer: user
    description: "policy denying users"
    policy:
      access:
        subjects:
          tags:
            - "roles:id:*"                  # default tag for DataOS users
            
        predicates:
          - "read"
        objects:
          paths:                            # resource, a sample dataset
            - "dataos://icebase:sample/test_dataset"
        allow: false                        # to restrict access
    ```
    

1. Open the DataOS CLI. Use the `apply` command to create this policy in the DataOS environment.
    
    ```yaml
    $ dataos-ctl apply -f access_policy_denying.yml 
    INFO[0000] 🛠 apply...                                   
    INFO[0000] 🔧 applying test-policy-usecase-denying-access:v1:policy... 
    INFO[0001] 🔧 applying test-policy-usecase-denying-access:v1:policy...created 
    INFO[0001] 🛠 apply...complete
    ```
    

1. As a result of this policy implementation, you can not access the sample dataset anymore. 
    
    
  
     
    <center>

    ![Picture](./Policy%20Implementation%20Use%20Case/Access_Denied.png)

    </center>
    
    <figcaption align = "center">Dataset not accessible</figcaption>
    <br>
    

1. Create a new policy to allow access to the resource(sample dataset in the example) for all the users having this custom tag. Here is the policy YAML to allow access for the user having a custom tag - `roles:id:test:user` 
    
    ```yaml
        
        version: v1
        name: test-policy-usecase-allowing-access
        type: policy
        layer: user
        description: "policy implementation to allow users having custom tag 'roles:id:test:user'"
        policy:
          access:
            subjects:
              tags:
                - "roles:id:test:user"          # Custom tag
            predicates:
              - "read"
            objects:
              paths:                            # resource, a sample dataset
                - "dataos://icebase:sample/test_dataset"
            allow: true
    ```
    

1. Now we will add this custom tag to allow a user to access the sample dataset using the following CLI command. You can see the custom tag listed in the output for the user. 
    
    ```yaml
    $ dataos-ctl user tag add -i 'darshanajmera' -t 'roles:id:test:user'
    INFO[0000] 🏷 user tag add...                            
    INFO[0000] new tags: roles:id:test:user                 
    INFO[0003] 🏷 user tag add...complete                    
    
           ID       |              TAGS               
    ----------------|---------------------------------
      darshanajmera | roles:direct:collated,          
                    | roles:id:data-dev,              
                    | roles:id:depot-manager,         
                    | roles:id:depot-reader,          
                    | roles:id:operator,              
                    | roles:id:system-dev,            
                    | roles:id:test:user,             
                    | roles:id:user,                  
                    | users:id:darshanajmera
    ```
    

    These tags can also be seen in the user’s profile on DataOS UI.
 
    <center>

    ![Picture](./Policy%20Implementation%20Use%20Case/UI_new_tag_-_Copy.png)

    </center>

    <figcaption align = "center">Tags on user’s profile page</figcaption>  

    <br>

    The user, `darshanajmera` is able to access and query the sample dataset due to the access policy implemented with a custom tag. The following screenshot displays the query result on DataOS Workbench.
    
    <center>

    ![Picture](./Policy%20Implementation%20Use%20Case/allow_access_-_Copy.png)

    </center>

    <figcaption align = "center">Dataset accessible after adding custom tag</figcaption>
    <br>

## Data Policy Implementation

### Mask Policy - Hash

A data [masking policy](../Policy.md) defines the logic that replaces (masks) the original sensitive data with fictitious data to maintain the privacy of sensitive data.

1. Create a data policy to mask the content of the column `email_id` in sample dataset using hashing technique for the users having custom tag `roles:id:test:user`. 
    
    ```yaml
        version: v1
        name: test-policy-usecase-pii-hash
        type: policy
        layer: user
        description: "data policy to hash pii column - email_id"
        owner:
        policy:
          data:
            type: mask
            priority: 90
            depot: icebase
            collection: sample
            dataset: test_dataset    
            selector:
              user:
                match: any
                tags:
                  - "roles:id:test:user"
              column:
                names:
                  - "email_id"
            mask:
              operator: hash
              hash:
                algo: sha256
    ```
    
2. Apply the policy using the following command on DataOS CLI.
    
    ```yaml
    $ dataos-ctl apply -f email_id_mask_hash.yml
    INFO[0000] 🛠 apply...                                   
    INFO[0000] 🔧 applying test-policy-usecase-pii-hash:v1:policy... 
    INFO[0001] 🔧 applying test-policy-usecase-pii-hash:v1:policy...created 
    INFO[0001] 🛠 apply...complete
    ```
    

1. Run the query on the DataOS Workbench to see the email_id column values hashed.
 
    <center>

    ![Picture](./Policy%20Implementation%20Use%20Case/masking_hash_email_-_Copy.png)

    </center>
            
    <figcaption align = "center">Column values hashed after the data policy implemented</figcaption>
    <br>

### Filter Policy

You can restrict the data in the query output by [filter policies](../Policy/Policy.md). 

1. Create a filter policy to exclude the records from the dataset for the filter criterion specified, as shown in the example below. This policy will be applicable to all the users with the specified tag `dataos:u:test:policy`.
    
    ```yaml
    version: v1
    name: test-policy-usecase-filter-to-city
    type: policy
    layer: user
    description: "data policy to filter just CITY3317 data"
    owner:
    policy:
      data:
        type: filter
        priority: 80
        selector:
          user:
            match: any
            tags:
              - "roles:id:test:user"
        filters:
          - column: city_id
            operator: not_equals
            value: CITY3317
        depot: icebase
        collection: sample
        dataset: test_dataset
    ```
    

1. Apply the policy using the following command on DataOS CLI.
    
    ```yaml
    $ dataos-ctl apply -f filter-to-city.yaml 
    INFO[0000] 🛠 apply...                                   
    INFO[0000] 🔧 applying test-policy-usecase-filter-to-city:v1beta1:policy... 
    INFO[0001] 🔧 applying test-policy-usecase-filter-to-city:v1:policy...created 
    INFO[0001] 🛠 apply...complete
    ```
    

    Query output Before policy implementation on city_id = ‘CITY3317’ 

    
    <center>

    ![Picture](./Policy%20Implementation%20Use%20Case/before_filter_city_-_Copy.png)

    </center>

    <figcaption align = "center">Data visible for the specific city_id</figcaption>
    <br>

    Query output after policy implementation on city_id = ‘CITY3317’ 
    
    <center>

    ![Picture](./Policy%20Implementation%20Use%20Case/after_filter_city_-_Copy.png)

    </center>

    <figcaption align = "center">Data not visible for the specific city_id after the filter policy implemented</figcaption>
    <br>

## Viewing Applied Policy Information

On Workbench, run the query to show the records from the dataset. When a policy is already applied, you will see the red information icon with the query just above the query result, as shown below. Click on it to see the information about all the policies applied to the dataset.
 
<center>

![Picture](./Policy%20Implementation%20Use%20Case/governance_wb_-_Copy.png)

</center>

<figcaption align = "center">Policies applied to the dataset</figcaption>
<br>