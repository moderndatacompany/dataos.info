---
title: Database
search:
  boost: 2
---

# :resources-database: Database

A Database [Resource](/resources/) in DataOS acts as a repository for storing transaction data, utilizing a managed Postgres relational database. It fulfills the transactional data storage needs of custom data applications developed on top of DataOS. Internal applications like [Lens Studio](/interfaces/lens/), [Metis UI](/interfaces/metis/), etc., also leverage the Database Resource for their transactional data storage. Utilizing a [Service](/resources/service/) supported by the [Beacon Stack](/resources/stacks/beacon/) facilitates CRUD operations (Create, Read, Update, Delete) on data assets stored in the Database, ensuring smooth connectivity between the data application and the Database. For analytical operations, users can utilize the [Flare Stack](/resources/stacks/flare/) to move the data from transactional data storage to other [Depots](/resources/depot/) or [Lakehouses](/resources/lakehouse/).

<div style="text-align: center;">
  <img src="/resources/database/database.png" alt="Database Resource" style="border:1px solid black; width: 60%; height: auto;">
  <figcaption><i>Database Resource</i></figcaption>
</div>


<aside class="callout">
🗣️ A Database is a <a href="https://dataos.info/resources/types_of_dataos_resources/"> Workspace-level </a> resource, implying that its scope is limited to a particular Workspace.
</aside>

## Structure of Database manifest

=== "Syntax"

    ```yaml
    #Attribtues for Resource
    name: ${resource-name}                #database_name 
    version: v1                           
    type: database                        
    description: ${description}
      - ${tag1}
      - ${tag2}
    owner: ${iamgroot}
    layer: ${user} 
    database:                            # Specify the resource type
      migrate:
        includes:
          - ${migration-directory}     # Address to all migrations (relative path)
        includesInline:
          migration: |
            ${migration_script}

        command: ${migration-command}   # ("up" or "down")
      compute: ${runnable-default}
    ```


=== "Code"

    ```yaml title="database_manifest_structure.yml"
    --8<-- "examples/resources/database/database.yaml"
    ```

## First Steps

Database Resource in DataOS can be created by applying the manifest file using the DataOS CLI. To learn more about this process, navigate to the link: [First steps](/resources/database/first_steps/).

## Configuration

The Database manifest files serves as the blueprint for defining the structure and behavior of Database Resources within DataOS. By configuring various attributes within the the Database manifest file, data developers can customize it to meet specific requirements. Below is an overview of the key attributes used to configure a the Database-specific section: [Attributes of Database manifest](/resources/database/configurations/).
 
## Recipes


Database Resource is used to store data on the fly. Your next steps depend upon whether you want to learn about what you can do with the database,  here are some how to guides to help you with that process:

- [How to query database data using workbench?](/resources/database/how_to_guide/how_to_query_database_using_workbench/)

- [How to back a streamlit application via database resource](/resources/database/how_to_guide/how_to_create_a_streamlit_application_of_database_on_dataos/)