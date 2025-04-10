# Scanning metadata

After creating the Depot, a user can run a Scanner Workflow for Depot to extract the metadata which later can be accessed on Metis UI. To know more about Scanner, please refer to this.

**For example:**
A user have created a Depot now he wants to add the meta data related to the data present in that Depot to Metis UI so that anyone can understand what the data have what kind of use cases we can solve with that, for which he created a Scanner workflow targetting the Depot which extracts all the meta data and register it to the Metis UI.

The below manifest file defines the `wf-postgres-depot` Workflow, designed to scan schema tables from a `PostgreSQL`-based Depot and register the extracted data into `Metis2`. It operates under the `scanner:2.0` Stack with Compute Resources managed by `runnable-default` and runs as the `metis` user. The Workflow is tagged as `postgres-depot` and `scanner`, indicating its role in schema discovery. The configuration includes a `depot` specification (`postgresdepot`) and placeholders for source configurations that allow filtering of databases, schemas, and tables based on inclusion and exclusion patterns.

```yaml
version: v1
name: wf-postgres-depot
type: workflow
tags:
    - postgres-depot
description: The workflow scans schema tables and register data
workflow:
    dag:
    - name: postgres-depot
        description: The job scans schema from depot tables and register data to metis2
        spec:
        tags:
            - scanner
        stack: scanner:2.0
        compute: runnable-default
        runAsUser: metis
        stackSpec:
            depot: postgresdepot           
            # sourceConfig:           
            #   config:
            #     markDeletedTables: false
            #     includeTables: true
            #     includeViews: true
            #     databaseFilterPattern:
            #       includes:
            #         - <databasename> 
            #       excludes:
            #         - <databasename> 
            #     schemaFilterPattern:
            #       includes:
            #         - <schemaname>
            #       excludes:
            #         - <schemaname>
            #     tableFilterPattern:
            #       includes:
            #         - <schemaname>
            #       excludes:
            #         - <schemaname>
```

After successfully executing the Scanner Workflow, a user can find the metadata on Metis UI as shown below.




