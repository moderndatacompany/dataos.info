# Scanner for BigQuery

Bigquery metadata Scanner Workflow can be configured and scheduled through the DataOS CLI. Ensure that all prerequisites are met before initiating the workflow.


## Prerequisites

To scan the metadata from BigQuery, User need the following:

1) Ensure that the BigQuery project is created.

2) **Access Permissions in GCP**: To successfully execute the Metadata Extraction Scanner Workflow in GCP, the user or service account needs specific permissions to access and retrieve the required data. Here's a summary of the minimum required permissions:

   - **Ingestion Permissions:**
     - `bigquery.datasets.get` – To retrieve metadata about datasets.
     - `bigquery.tables.get` – To access table metadata.
     - `bigquery.tables.getData` – To get metadata about table data.
     - `bigquery.tables.list` – To list metadata for tables.
     - `resourcemanager.projects.get` – To get metadata about the project.
     - `bigquery.jobs.create` – To create jobs related to metadata extraction.
     - `bigquery.jobs.listAll` – To list all jobs for monitoring and management.

   - **Stored Procedure Permissions:**
     - `bigquery.routines.get` – To access stored procedure metadata.
     - `bigquery.routines.list` – To list stored procedures.

   - **Fetch Policy Tags Permissions:**
     - `datacatalog.taxonomies.get` – To get metadata about policy tags.
     - `datacatalog.taxonomies.list` – To list policy tags.

   - **BigQuery Usage & Lineage Workflow Permissions:**
     - `bigquery.readsessions.create` – To create read sessions for usage and lineage analysis.
     - `bigquery.readsessions.getData` – To access data from read sessions for usage and lineage tracking.

   If the user has External Tables, please attach relevant permissions needed for external tables, along with the above list of permissions.

3) **Access Permissions in DataOS**: To execute a Scanner Workflow in DataOS, verify that at least one of the following role tags is assigned:

   - `roles:id:data-dev`
   - `roles:id:system-dev`
   - `roles:id:user`

   Use the following command to check assigned roles:

   ```bash
   dataos-ctl user get
   ```

   If any required tags are missing, contact a **DataOS Operator** or submit a **Grant Request** for role assignment.

   Alternatively, if access is managed through **use cases**, ensure the following use cases are assigned:

   - **Read Workspace**
   - **Run as Scanner User**
   - **Manage All Depot**
   - **Read All Dataset**
   - **Read All Secrets from Heimdall**

   To validate assigned use cases, refer to the [**Bifrost Application Use Cases**](/interfaces/bifrost/ "Bifrost is a Graphical User Interface (GUI) that empowers users to effortlessly create and manage access policies for applications, services, people, and datasets. Bifrost leverages the governance engine of DataOS, Heimdall, to ensure secure and compliant data access through ABAC policies, giving users fine-grained control over the data and resources.") section.

4) **Pre-created Bigquery Depot**: Ensure that a Bigquery Depot is already created with valid read access and the necessary permissions to extract metadata. To check the Depot go to the Metis UI of the DataOS or use the following command:

   ```bash
   dataos-ctl get -t depot -a

   #expected output

   INFO[0000] 🔍 get...
   INFO[0000] 🔍 get...complete

   | NAME             | VERSION | TYPE  | WORKSPACE | STATUS | RUNTIME | OWNER      |
   | ---------------- | ------- | ----- | --------- | ------ | ------- | ---------- |
   | mongodepot       | v2alpha | depot |           | active |         | usertest   |
   | snowflakedepot   | v2alpha | depot |           | active |         | gojo       |
   | redshiftdepot    | v2alpha | depot |           | active |         | kira       |
   | mysqldepot       | v2alpha | depot |           | active |         | ryuk       |
   | oracle01         | v2alpha | depot |           | active |         | drdoom     |
   | mariadb01        | v2alpha | depot |           | active |         | tonystark  |
   | demopreppostgres | v2alpha | depot |           | active |         | slimshaddy |
   | demoprepbq       | v2alpha | depot |           | active |         | pengvin    |
   | mssql01          | v2alpha | depot |           | active |         | hulk       |
   | kafka01          | v2alpha | depot |           | active |         | peeter     |
   | icebase          | v2alpha | depot |           | active |         | blackpink  |
   | azuresql         | v2alpha | depot |           | active |         | arnold     |
   | fastbase         | v2alpha | depot |           | active |         | ddevil     |
   ```

   Template for creating BIGQUERY Depot is shown below:

   ```yaml
   name: ${{depot-name}}
   version: v2alpha
   type: depot
   tags:
     - ${{dropzone}}
     - ${{bigquery}}
   owner: ${{owner-name}}
   layer: user
   depot:
     type: BIGQUERY                 
     description: ${{description}} # optional
     external: ${{true}}
     secrets:
       - name: ${{bq-instance-secret-name}}-r
         allkeys: true

       - name: ${{bq-instance-secret-name}}-rw
         allkeys: true
     bigquery:  # optional                         
       project: ${{project-name}} # optional
       params: # optional
         ${{"key1": "value1"}}
         ${{"key2": "value2"}}
   ```

## Scanner Workflow for BigQuery

DataOS enables the creation of a Depot of type 'BIGQUERY' for accessing data stored in BigQuery projects. Multiple Depots can be established, each directed towards a different project. The following manifest scans metadata from a BigQuery-type Depot.


```yaml

version: v1
name: wf-bigquery-depot
type: workflow
tags:
  - bigquery-depot
description: The workflow scans schema tables and register data
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
        stackSpec:
          depot: dataos://demoprepbq           
          sourceConfig:           
            config:
              markDeletedTables: false
              includeTables: true
              includeViews: true
              databaseFilterPattern:       # provide required regex/name for the filters
                includes:
                  - <databasename> 
                excludes:
                  - <databasename> 
              schemaFilterPattern:
                includes:
                  - <schemaname>
                excludes:
                  - <schemaname>
              tableFilterPattern:
                includes:
                  - <schemaname>
                excludes:
                  - <schemaname>
```

The above sample manifest file is deployed using the following command:

```bash
dataos-ctl resource apply -f ${{path to the Scanner YAML}}
```

**Updating the Scanner Workflow**:

If the Depot or Scanner configurations are updated, the Scanner must be redeployed after deleting the previous instance. Use the following command to delete the existing Scanner:

```bash 
  dataos-ctl delete -f ${{path-to-Scanner-YAML}}]
```

**OR**

```bash
  dataos-ctl delete -t workflow -n ${{name of Scanner}} -w ${{name of workspace}}
```


!!! info "**Best Practice**"

    As part of best practices, it is recommended to regularly delete Resources that are no longer in use. This practice offers several benefits, including saving time and reducing costs.

