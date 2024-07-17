# Delete from Dataset

> Supported in Flare Stack Version `flare:4.0` only.
> 

The `delete_from_dataset` [action](/resources/stacks/flare/configurations/#delete_from_dataset) removes data from tables upon a specified filter. There could be myriad such filter condition, two such scenarios are provided below.

## Code Snippet

### **Delete from Single Dataset**

The below case scenario depicts data deletion based on a filter. To accomplish this, we make use of Flare Stack's `delete_from_dataset` action upon the input dataset `inputDf` and delete from the dataset upon the filter condition provided in `deleteWhere` property. The YAML for the same is provided below:

```yaml
version: v1 # Version
name: delete-from-dataset # Name of the Workflow
type: workflow # Type of Resource (Here its a workflow)
tags: # Tags for the Workflow
  - Delete
workflow: # Workflow Specific Section
  title: Delete from Dataset # Title of the DAG
  dag: # DAG (Directed Acyclic Graph)
    - name: delete # Name of the Job
      title: Delete from Dataset # Title of the Job
      spec: # Specs
        tags: # Tags
          - Delete
        stack: flare:4.0 # Stack Version (Here its Flare stack)
        compute: runnable-default # Compute 
        flare: # Flare Section
          job: # Job Section
            explain: true # Explain
            logLevel: INFO # Loglevel
            inputs: # Inputs Section
              - name: inputDf # Name of Input Dataset
                dataset: dataos://icebase:actions/random_users_data?acl=rw # Dataset UDL
                format: Iceberg # Dataset Format
            actions: # Action Section
              - name: delete_from_dataset # Name of the Action
                input: inputDf # Input Dataset Name
                deleteWhere: "target.state_code = 'AL'" # Delete where the provided condition is true
```

### **Delete from Multiple Dataset**

The below case scenario also depicts data deletion based on a filter. However, here there are two input datasets `customer` and `city` on which an inner join is performed. The filter condition for the same is provided in the `deleteWhere` property. The YAML for the same is provided below:

```yaml
version: v1 # Version
name: delete-from-customer # Name of the Workflow
type: workflow # Type of Resource (Here its workflow)
workflow: # Workflow Section
  dag: # Directed Acyclic Graph (DAG)
    - name: delete-from-city # Name of the Job
      spec: # Specs
        stack: flare:4.0 # Stack is Flare (so its a Flare Job)
        compute: runnable-default # Compute
        flare: # Flare Stack Specific Section
          job: # Job Section
            inputs: # Inputs Section
              - name: customer # Name of First Input Dataset
                dataset: dataos://icebase:test/customer # Input Dataset UDL
                format: Iceberg # Format
              - name: city # Name of Second Input Dataset
                dataset: dataos://icebase:test/city # Input Dataset UDL
                format: Iceberg # Format
            steps: # Steps Section
              - sequence: # Sequence
                  - name: finalDf # Transformation
                    sql: SELECT customer.city_id FROM customer INNER JOIN city ON customer.city_id = city.city_id # SQL Snippet
            actions: # Action Section
              - name: delete_from_dataset # Name of the Flare Action
                input: customer # Input Dataset Name
                deleteWhere: "exists (SELECT city_id FROM finalDf WHERE target.city_id = city_id)" # Deletes from the specified condition
```