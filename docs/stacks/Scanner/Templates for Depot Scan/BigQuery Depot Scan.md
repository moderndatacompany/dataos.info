# **BigQuery Depot Scan**

DataOS allows you to create a Depot of type 'BIGQUERY' to read the data stored in the BigQuery projects. You can create several Depots, each pointing to a different project. You can scan metadata from BigQuery type depot.

# **Requirements**

To scan the BigQuery depot, you need the following:

1. Ensure that the BigQuery project is created.
2. Ensure that the depot is created and you have `read` access for the depot.
3. BigQuery user must have`viewer` privilege on the warehouse. 
4. You should have enough access to fetch the required metadata. The following list describes the minimum required permissions.

|  | GCP Permission | GCP Role | Required For |
| --- | --- | --- | --- |
| 1 | bigquery.datasets.get | BigQuery Data Viewer | Metadata Ingestion |
| 2 | bigquery.tables.get | BigQuery Data Viewer | Metadata Ingestion |
| 3 | bigquery.tables.getData | BigQuery Data Viewer | Metadata Ingestion |
| 4 | bigquery.tables.list | BigQuery Data Viewer | Metadata Ingestion |
| 5 | resourcemanager.projects.get | BigQuery Data Viewer | Metadata Ingestion |
| 6 | bigquery.jobs.create | BigQuery Job User | Metadata Ingestion |
| 7 | bigquery.jobs.listAll | BigQuery Job User | Metadata Ingestion |
| 8 | datacatalog.taxonomies.get | BigQuery Policy Admin | Fetch Policy Tags |
| 9 | datacatalog.taxonomies.list | BigQuery Policy Admin | Fetch Policy Tags |
| 10 | bigquery.readsessions.create | BigQuery Admin | Bigquery Usage Workflow |
| 11 | bigquery.readsessions.getData | BigQuery Admin | Bigquery Usage Workflow |

# **Scanner Workflow**

Here is an example of YAML configuration to connect to the source and reach the Metis server to save the metadata in Metis DB.

1. Create and apply the Scanner YAML. You can apply database, schema and table filter patterns while scanning metadata.
    
    You can run the Scanner workflow with or without a filter pattern. 
    
    ```yaml
    version: v1
    name: wf-bigquery-depot
    type: workflow
    tags:
      - bigquery-depot
    description: The job scans schema tables and register data
    workflow:
      dag:
        - name: bigquery-depot
          description: The job scans schema from bigquery-depot tables and register data to metis2
          spec:
            tags:
              - scanner
            stack: scanner:2.0
            compute: runnable-default
            runAsUser: metis
            scanner:
              depot: demoprepbq
              # sourceConfig:
              #   config:
              #     schemaFilterPattern:
              #       includes:
              #         - Amazon
              #         - CUSTOMER
              #     tableFilterPattern:
              #       includes:
              #         - Customer_Profiles
              #         - user
    ```
    

> **Note:** Remove the commented part mentioned under the filter pattern in the Scanner YAML to apply filters for the required schemas and tables.
> 
> 
> 
1. After the successful workflow run, you can check the metadata of scanned Tables on Metis UI for all schemas present in the database.
    
    
    > 🗣 Filtering for the Scanner workflow works on a hierarchy level; First, it will filter all given schemas and then the table in that schema if present.
    
    