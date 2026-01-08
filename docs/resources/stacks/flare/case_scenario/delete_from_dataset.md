# Delete from dataset

The [`delete_from_dataset` action](/resources/stacks/flare/configurations/#delete_from_dataset) removes data from tables upon a specified filter. There could be myriad such filter condition, two such scenarios are provided below.

!!! info  

    `deletefromdataset` only remove data files,metadata files (like snapshots, manifests, etc.) are retained for audit and rollback purposes until they are explicitly cleaned up.
 

## **Delete from single dataset**

The below case scenario depicts data deletion based on a filter. To accomplish this, we make use of Flare Stack's `delete_from_dataset` action upon the input dataset `inputDf` and delete from the dataset upon the filter condition provided in `deleteWhere` property. The YAML for the same is provided below:

```yaml
version: v1                                               # Version
name: delete-from-dataset                                 # Name of the Workflow
type: workflow                                            # Type of Resource (Here its a workflow)
tags:                                                     # Tags for the Workflow
  - Delete
workflow:                                                 # Workflow Specific Section
  title: Delete from Dataset                              # Title of the DAG
  dag:                                                    # DAG (Directed Acyclic Graph)
    - name: delete                                        # Name of the Job
      title: Delete from Dataset                          # Title of the Job
      spec:                                               # Specs
        tags:                                             # Tags
          - Delete
        stack: flare:7.0                                  # Stack Version
        compute: runnable-default                         # Compute 
        stackSpec:                                        # Flare Section
          job:                                            # Job Section
            explain: true                                 # Explain
            logLevel: INFO                                # Loglevel
            inputs:                                       # Inputs Section
              - name: inputDf                             # Name of Input Dataset
                dataset: dataos://lakehouse:actions/random_users_data?acl=rw   # Dataset UDL
                format: Iceberg                           # Dataset Format
            actions:                                      # Action Section
              - name: delete_from_dataset                 # Name of the Action
                input: inputDf                            # Input Dataset Name
                deleteWhere: "target.state_code = 'AL'"   # Delete where the provided condition is true

```

Delete from the dataset with a filter to match rows to delete:

```yaml
actions:                                # Action Section
  - name: delete_from_dataset           # Name of the Action
    input: inputDf                      # Input Dataset Name
    deleteWhere: "date_time <  TIMESTAMP('2026-01-01 00:00:00')" # Delete where Timestamp is less then given
```



## **Delete from multiple dataset**

The below case scenario also depicts data deletion based on a filter.

Here, two input datasets `customer` and `city` are given on which an inner join is performed. The filter condition for the same is provided in the `deleteWhere` property. The YAML for the same is provided below:

```yaml
version: v1                                                  # Version
name: delete-from-customer                                   # Name of the Workflow
type: workflow                                               # Type of Resource (Here its workflow)
workflow:                                                    # Workflow Section
  dag:                                                       # Directed Acyclic Graph (DAG)
    - name: delete-from-city                                 # Name of the Job
      spec:                                                  # Specs
        stack: flare:7.0                                     # Stack is Flare (so its a Flare Job)
        compute: runnable-default                            # Compute
        stackSpec:                                           # Flare Stack Specific Section
          job:                                               # Job Section
            inputs:                                          # Inputs Section
              - name: customer                               # Name of First Input Dataset
                dataset: dataos://lakehouse:test/customer    # Input Dataset UDL
                format: Iceberg                              # Format
              - name: city                                   # Name of Second Input Dataset
                dataset: dataos://lakehouse:test/city        # Input Dataset UDL
                format: Iceberg                              # Format
            steps:                                           # Steps Section
              - sequence:                                    # Sequence
                  - name: finalDf                            # Transformation
                    sql: SELECT customer.city_id FROM customer INNER JOIN city ON customer.city_id = city.city_id   # SQL Snippet
            actions:                                         # Action Section
              - name: delete_from_dataset                    # Name of the Flare Action
                input: customer                              # Input Dataset Name
                deleteWhere: "exists (SELECT city_id FROM finalDf WHERE target.city_id = city_id)"     # Deletes from the specified condition

```


!!! tip

    - To verify you can use Workbench and count the record before and after running the `delete_from_dataset` action job.
    - Multiple input datasets are supported exclusively by the `delete_from_dataset` action.
    - When operating within a Google Cloud Storage (GCS) ecosystem, the dataset address must include the acl=rw query parameter. For example:
      ```yaml
      inputs:
        - name: inputDf
          dataset: dataos://icebase:actions/random_users_data?acl=rw
          format: Iceberg
      ```
    - The inclusion of the `acl=rw` parameter is required due to GCS credential behavior. GCS typically generates two sets of credentials: one with read-only access and another with read and write access. Since Flare `actions` involve writing operations, the write-enabled credentials must be explicitly specified. If the `acl` parameter is omitted, Flare defaults to read-only mode, which restricts the ability to write or update data and metadata files.
    - Expected Error if `acl=rw` is omitted:
    ```json
    [CIRCULAR REFERENCE:com.google.api.client.googleapis.json.GoogleJsonResponseException: 403 Forbidden
    POST https://storage.googleapis.com/upload/storage/v1/b/lake001-shiningtr-dev/o?ifGenerationMatch=0&name=icebase/test/city251/data/version%3D202301250835/00131-8-8ac950a8-6007-4679-90e3-6902966af097-00001.parquet&uploadType=resumable
    {
      "error": {
        "code": 403,
        "message": "ds-sa-r-shiningtr-stw-dev@<account-name>.iam.gserviceaccount.com does not have storage.objects.create access to the Google Cloud Storage object. Permission 'storage.objects.create' denied on resource (or it may not exist).",
        "errors": [
          {
            "message": "ds-sa-r-shiningtr-stw-dev@<account-name>.iam.gserviceaccount.com does not have storage.objects.create access to the Google Cloud Storage object. Permission 'storage.objects.create' denied on resource (or it may not exist).",
            "domain": "global",
            "reason": "forbidden"
          }
        ]
      }
    }
    ]
    ```