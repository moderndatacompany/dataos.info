# **Creating Data Policy (Filtering)**

Filter policy definition consists of configuration settings for the user, columns of the dataset, and masking operator. It may include rules for the subject, predicate, and object defining AND/OR relationships.

1. Create the YAML file. 
    -  Specify the version, resource name (the policy will be referred to by this name), and resource type (policy). 
    -  Provide layer as **‘user’** or **‘system’**. 
        
        `user`: When the resources to be accessed are defined at the DataOS User layer.
        
        `system`: When the resources to be accessed are defined at the DataOS System layer. For example, if you want to read or write from the PostgreSQL database.
        
    -  Provide a description to help understand its purpose.
    -  Specify the policy-related configuration properties under the `data` section.
        
        `type`: Specify **“filter”**.
        
        `priority`: The policy with higher priority will override all other policies defined for the same resources.
        
        `depot`: Mention the depot name to connect to the data source.
        
        `collection`: Provide the name of the collection.
        
        `dataset`: Provide the name of the dataset.
        
    -  Specify user-related settings under the `selector` section.
        
        `match`: You can specify two operators here. `any` (must match at least one tag) and `all`(match all tags).
        
        `user`: Specify a user identified by a tag. They can be a group of tags defined as an array. See [Rules for AND/OR Logic](Rules%20for%20AND%20OR%20Logic.md).
        
    -  Specify the criterion for columns of the dataset for which data is to be filtered.
        
        `names`: Provide names as an array.
        
        `tags`: Alternatively, you can also provide tags for the columns.
        
        `operator`: This is to specify filtering conditions.
        
        `value`: value to match the criterion.
        
2. Create the policy resource using the `apply` command.

## **Filtering Policy Example**

**Example** 

```yaml
version: v1
name: filter-to-florida
type: policy
layer: user
description: "data policy to filter just FL data"
owner:
policy:
  data:
    type: filter
    priority: 80
    depot: raw01
    collection: public
    dataset: store_01
    selector:
      user:
        match: any
        tags:
          - "roles:id:testuser"
    filters:
      - column: store_state_code
        operator: not_equals
        value: FL
    
```