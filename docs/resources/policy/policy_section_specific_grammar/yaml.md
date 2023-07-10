# YAML 

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

- Creating Filter Policy
    - version
    - resource name
    - resource type
    - layer
        - user
        - system
    - description
    - data
        - type: filter
        - priority - policy with higher priority will override all other policies defined for the same resources.
        - depot: Mention the depot name to connect to the data source
        - collection: Provide the name of the collection
        - datasets: Provide the name of the dataset
        - selector: Specify user-related settings under the selector section
            - user: Specify a user identified by a tag. They can be a group of tags defined as an array.
                - match: You can specify two operators here.
                    - any - must match at least one tag
                    - all - match all tags
                - tags: Alternatively, you can also provide tags for the columns
        - filters
            - column: Specify the criterion for columns of the dataset for which data is to be filtered.
            - operator: This is to specify filtering conditions
            - value: value to match the criterion