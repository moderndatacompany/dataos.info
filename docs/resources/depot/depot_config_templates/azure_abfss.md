# Azure ABFSS (Azure Blob File System Service)

DataOS enables the creation of a Depot of type 'ABFSS' to facilitate the reading of data stored in an Azure Blob Storage account. This Depot provides access to the storage account, which can consist of multiple containers. A container serves as a grouping mechanism for multiple blobs. It is recommended to define a separate Depot for each container.

## Requirements

To establish a connection with Azure ABFSS, the following information is required:

- Storage account name
- Storage account key
- Container
- Relative path
- Data format stored in the container

## Template

To create a Depot of type ‘ABFSS‘, utilize the following template:

=== "v1"

    ```yaml
    name: {{depot-name}}
    version: v1
    type: depot
    tags:
      - {{tag1}}
      - {{tag2}}
    owner: {{owner-name}}
    layer: user
    depot:
      type: ABFSS                                       
      description: {{description}}
      external: {{true}}
      compute: {{runnable-default}}
      connectionSecret:                                 
        - acl: rw
          type: key-value-properties
          data:
            azurestorageaccountname: {{account-name}}
            azurestorageaccountkey: {{account-key}}
        - acl: r
          type: key-value-properties
          data:
            azurestorageaccountname: {{account-name}}
            azurestorageaccountkey: {{account-key}}
      spec:                                             
        account: {{account-name}}
        container: {{container-name}}
        relativePath: {{relative-path}}
        format: {{format}}
    ```
=== "v2alpha"

    ```yaml
    name: {{depot-name}}
    version: v1
    type: depot
    tags:
      - {{tag1}}
      - {{tag2}}
    owner: {{owner-name}}
    layer: user
    depot:
      type: ABFSS                                       
      description: {{description}}
      external: {{true}}
      compute: {{runnable-default}}
      connectionSecret:                                 
        - acl: rw
          type: key-value-properties
          data:
            azurestorageaccountname: {{account-name}}
            azurestorageaccountkey: {{account-key}}
        - acl: r
          type: key-value-properties
          data:
            azurestorageaccountname: {{account-name}}
            azurestorageaccountkey: {{account-key}}
      spec:                                             
        account: {{account-name}}
        container: {{container-name}}
        relativePath: {{relative-path}}
        format: {{format}}
    ```