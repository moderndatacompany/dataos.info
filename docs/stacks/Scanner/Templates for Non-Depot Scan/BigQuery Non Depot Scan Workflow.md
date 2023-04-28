# **BigQuery Non Depot Scan Workflow**

The non-depot Scanner workflow will help you to connect with BigQuery to extract metadata details such as schemas, tables, view details etc.

# **Requirements**

To run the Scanner, you need the following:

1. Ensure that the BigQuery project is created.
2. BigQuery user must have`viewer` privilege on the warehouse. 
3. You should have enough access to fetch the required metadata. The following list describes the minimum required permissions.

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

1. Create and apply the Scanner YAML. You need to provide source connection details and configuration settings such as  metadata type and filter patterns to include/exclude assets for metadata scanning. 
    
    ```yaml
    version: v1
    name: bigquery-scanner2
    type: workflow
    tags:
      - bigquery-non-depot
    description: The job scans schema tables and register metadata
    workflow:
      dag:
        - name: bigquery-scanner2
          description: The job scans schema from bigquery via Non-depot tables and register metadata to metis2
          spec:
            tags:
              - scanner2.0
            stack: scanner:2.0
            compute: runnable-default
    				runAsUser: metis
            scanner:
              type: bigquery
              source: BigQuerySource_ND
              sourceConnection:
                config:
                  type: BigQuery
                  credentials:
                    gcsConfig:
                      type: <account type>
                      projectId: project ID # ["project-id-1", "project-id-2"]
                      privateKeyId: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                      privateKey: |                              # divide every \n to new line  between BEGIN & END PRIVATE KEY
                              -----BEGIN PRIVATE KEY-----
                              xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    													xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                              xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    													xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    													xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    													xxxxxxxxxxxxxxxxxxxx
                              -----END PRIVATE KEY-----
                      clientEmail: client@mail.com
                      clientId: 123456
                      # authUri: https://accounts.google.com/o/oauth2/auth (default)
                      # tokenUri: https://oauth2.googleapis.com/token (default)
                      # authProviderX509CertUrl: https://www.googleapis.com/oauth2/v1/certs (default)
                      clientX509CertUrl: https://cert.url
              sourceConfig:
                config:
                  markDeletedTables: false
                  includeTables: true
                  includeViews: true
                  # databaseFilterPattern:
                  #   includes:
                  #     - database1
                  #     - database2
                  #   excludes:
                  #     - database3
                  #     - database4
                  # schemaFilterPattern:
                  #   includes:
                  #     - schema1
                  #     - schema2
                  #   excludes:
                  #     - schema3
                  #     - schema4
                  # tableFilterPattern:
                  #   includes:
                  #     - table1
                  #     - table2
                  #   excludes:
                  #     - table3
                  #     - table4
    ```
    

    > **Note:** Remove the commented part mentioned under the filter pattern in the Scanner YAML to apply filters for the required schemas and tables.
    
    

1. After the successful workflow run, you can check the metadata of scanned Tables on Metis UI.
    
    
    > 🗣 Filtering for the Scanner workflow works on a hierarchy level; First, it will filter all given schemas and then the table in that schema if present.
    
    