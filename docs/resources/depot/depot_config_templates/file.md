# File

DataOS provides the capability to create a Depot of type 'FILE' for reading CSV/plain text data stored in the local file storage.

## Requirements

To establish a connection, the following information is required:

- Path: The location of the file in the local file storage.

## Template

To create a Depot of type ‘FILE‘, utilize the following template:

```yaml
version: v1
name: {{depot-name}}
type: depot
tags:
  - {{tag1}}
  - {{tag2}}
owner: {{owner-name}}
layer: user
depot:
  type: FILE                            
  description: {{description}}            
  external: {{true}}
  spec:
      path: {{"tmp/dataos"}}
```