# Azure WASBS (Windows Azure Storage Blob Service)

DataOS enables the creation of a Depot of type 'WASBS' to facilitate the reading of data stored in Azure Data Lake Storage. This Depot enables access to the storage account, which can contain multiple containers. A container serves as a grouping of multiple blobs. It is recommended to define a separate Depot for each container.

## Requirements

To establish a connection with Azure WASBS, the following information is required:

- Storage account name
- Storage account key
- Container
- Relative path
- Format

## Template

To create a Depot of type ‘WASBS‘, utilize the following template:

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
  type: WASBS                                      
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
