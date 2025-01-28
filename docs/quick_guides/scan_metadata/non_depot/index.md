# Scan Metadata without Depot

!!! info "Information"
    This guide will demonstrate the steps to perform metadata scanning from external data stored in structured data sources (RDBMS/Data Warehouses) without using Depot. In this case, you must set up a source connection within the Scanner workflow and provide configuration to capture schema details.

## Quick Steps

Follow the below steps:

<center>
<div style="text-align: center;">
<img src="/quick_guides/scan_metadata/non_depot/3_scan_non_depot.png" alt="Steps to create Scanner Workflow" style="border: 1px solid black;">
</div>
</center>

For illustration purposes, we will connect with the **BigQuery** data source.

### **Step 1: Check Required Permissions**

1. You should have enough access to fetch the required metadata from the metadata source. The following list describes the minimum permissions needed for BigQuery.
    
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
    
    <aside class="callout">
    The required permissions and privileges will change according to the data source. For more about data source-specific permissions, refer to the [Scanner](/resources/stacks/scanner/#supported-data-sources) documentation.
    
    </aside>
    
2. To run the scanner workflow, a user must have either Metis admin access or be granted access to the "**Run as Scanner User"** use case.

### **Step 2: Create Scanner Workflow**

Let us create a Scanner workflow with `sourceConnection` and `sourceConfig` sections, where we can provide connection information for the metadata source.

1. Provide the workflow properties, such as version, name, description, tags, etc.
2. Define the Scanner job configuration properties in the dag, such as job name, its description, stack used, etc.
    
    ```yaml
    version: v1
    name: bigquery-scanner-test
    type: workflow
    tags:
      - bigquery-non-depot-scanner
    description: The workflow is for the job to scan schema tables and register metadata
    workflow:
      dag:
        - name: bigquery-scanner2
          description: The job scans schema from bigquery via Non-depot tables and registers metadata to metis2
          spec:
            tags:
              - scanner2.0
            stack: scanner:2.0
            compute: runnable-default
    ```
    
3. Under the ‘**Scanner**’ stack, provide the following:
    
    1. **type**: This depends on the underlying data source. Values for type could be snowflake, bigquery, redshift, etc.

    2. **source**: Here, you need to explicitly provide the source name where the scanned metadata is saved within Metastore (Metis). On Metis UI, sources are listed for databases, messaging, dashboards, workflows, ML models, etc.
        
    
    ```yaml
    workflow:
    ...
    ...
            scanner:
              type: bigquery
              source: BigQueryTestSourcenp
    ```
    
4. **When the metadata source is not referenced by the Depot**, you need to provide the `source connection` details and credentials **explicitly.** These details will depend on the underlying data source to be scanned. Click [here](/resources/stacks/scanner/#supported-data-sources) to learn more about the source specific configuration properties. 

    This requires us to provide the following information for our example, all provided by BigQuery**:** 
    
    **`type`**, **`projected`, `privateKey`, `privateKeyId`, `clientEmail`, `clientId`, `authUri`**,**`tokenUri`**, **`authProviderX509CertUrl`**, **`clientX509CertUrl`**
    
    These details are sent to the metadata source while making the connection.
    
    ```yaml
    sourceConnection:
      config:
        type: BigQuery
        credentials:
          gcsConfig:
            type: service_account
            projectId: ${{project_id}}
            privateKeyId: ${{provate_keyID}}
            privateKey: |
                    |                              # divide every \n to new line  between BEGIN & END PRIVATE KEY
                              -----BEGIN PRIVATE KEY-----
                              xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    						  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                              xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    						  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    						  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    						  xxxxxxxxxxxxxxxxxxxx
                              -----END PRIVATE KEY-----
            clientEmail: ${{client_mail}}
            clientId: ${{clientID}}
            # authUri: https://accounts.google.com/o/oauth2/auth (default)
            # tokenUri: https://oauth2.googleapis.com/token (default)
            # authProviderX509CertUrl: https://www.googleapis.com/oauth2/v1/certs (default)
            clientX509CertUrl: "https://www.googleapi.com/robot/v1/metadata/x509/ds-demo-write%40dataos-ck-res-yak-dev.iam.gserviceaccount.com"
    sourceConfig:
    ```
    
    <aside class="callout">
    🗣 Please note that when entering the private key between the BEGIN and END PRIVATE KEY tags, you need to manually provide a new line for every occurrence of `\n`.
    
    </aside>
    
5. Provide a set of configurations specific to the source type under `source configuration` to customize and control metadata scanning. 
    1. **type**: `DatabaseMetadata`
    2. **filterPattern**: Specify which databases/ schemas/ tables/ charts/ dashboards/ topics are of interest.
    
    `includes:` and `excludes:` are used to specify schema/table names or a regex rule to include/exclude tables while scanning the schema and registering with Metis.
    
    ```yaml
    sourceConfig:
                config:
                  databaseFilterPattern:
                    includes:
                      - dataos-ck-res-yak-dev
                  schemaFilterPattern:
                    excludes:
                      - manufacturing
    ```
    To know more about how to specify filters in different scenarios, refer to [Filter Pattern Examples](/resources/stacks/scanner/creating_scanner_workflows/filter_pattern_examples/).

    <details><summary>Here is the complete YAML code.</summary>
    
    ```yaml
    version: v1
    name: bigquery-scanner-test
    type: workflow
    tags:
      - bigquery-non-depot-scanner
    description: The workflow is to scan schema tables and register metadata
    workflow:
      dag:
        - name: bigquery-scanner2
          description: The job scans schema from bigquery via Non-depot tables and registers metadata to metis2
          spec:
            tags:
              - scanner2.0
            stack: scanner:2.0
            compute: runnable-default
            stackSpec:
              type: bigquery
              source: BigQueryTestSource
              sourceConnection:
                config:
                  type: BigQuery
                  credentials:
                    gcsConfig:
                      type: service_account
                      projectId: dataos-ck-res-yak-dev
                      privateKeyId: ${{project_id}}
                      privateKey: |
                              -----BEGIN PRIVATE KEY-----
                              ${{private_key}}
                              -----END PRIVATE KEY-----
                      clientEmail: ${{client_mail}}
                      clientId: ${{client_id}}
                      authUri: https://accounts.google.com/o/oauth2/auth (default)
                      tokenUri: https://oauth2.googleapis.com/token (default)
                      authProviderX509CertUrl: https://www.googleapis.com/oauth2/v1/certs (default)
                      clientX509CertUrl: "https://www.googleapi.com/robot/v11/metadata/x509/ds-demo-writer%40dataos-ck-res-yak-dev.iam.gserviceaccount.com"
              sourceConfig:
                config:
                  databaseFilterPattern:
                    includes:
                      - dataos-ck-res-yak-dev
                  schemaFilterPattern:
                    excludes:
                      - manufacturing 
                     
    ```
    </details>

### **Step 3: Check Scanned Metadata on Metis**

After the successful workflow run, scanned metadata is registered with Metis. You can check the metadata of scanned databases/schemas/tables on Metis UI. To see it, go to the Metis app -> Settings -> Databases. 

The following metadata source is created (as configured in the Scanner Workflow).

![bigquery scanned source.png](/quick_guides/scan_metadata/non_depot/bigquery_scanned_source.png)

**Scanned Database**

![bigquery schemas.png](/quick_guides/scan_metadata/non_depot/bigquery_database.png)

**Scanned Schemas** 

![bigquery tables.png](/quick_guides/scan_metadata/non_depot/bigquery_schemas.png)

## Scheduling Scanner Workflow Run

Scanner workflows are either single-time run or scheduled to run at a specific cadence. To schedule a workflow, you must add the schedule property defining a cron in `workflow` section.
```yaml
workflow:
  title: scheduled Scanner Workflow
  schedule: 
    cron: '*/2 * * * *'  #every 2 minute  [Minute, Hour, day of the month ,month, dayoftheweek]
    concurrencyPolicy: Allow #forbid/replace
    endOn: 2024-11-01T23:40:45Z
    timezone: Asia/Kolkata
```
To learn more about these properties, refer to [Schedulable workflows](/resources/workflow/how_to_guide/scheduled_workflow/).