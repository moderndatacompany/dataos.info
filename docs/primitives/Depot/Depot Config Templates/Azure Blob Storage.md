# Azure Blob Storage

DataOS allows you to create a Depot of type 'ABFSS' to support reading data stored in an Azure Blob Storage account. This Depot enables all access through a storage account. This storage account may have multiple containers. A container is a grouping of multiple blobs. Define separate Depot for each container.

## Requirements

To connect to Azure Blob storage, you need:

- Storage account name
- Storage account key
- Container
- Relative path
- Format of data stored in the container.

## Template

To create a Depot of type ‘ABFSS‘, use the following template:

```yaml
version: v1
name: <depot-name>
type: depot
tags:
  - <tag1>
  - <tag2>
owner: <owner-name>
layer: user
depot:
  type: ABFSS                                       # Depot type
  description: <description>
  external: true
  connectionSecret:                                 # Data source specific configurations
    - acl: rw
      type: key-value-properties
      data:
        azurestorageaccountname: <account-name>
        azurestorageaccountkey: <account-key>
    - acl: r
      type: key-value-properties
      data:
        azurestorageaccountname: <account-name>
        azurestorageaccountkey: <account-key>
  spec:                                             # Data source specific configurations
    account: <account-name>
    container: <container-name>
    relativePath: <relative-path>
    format: <format>
```