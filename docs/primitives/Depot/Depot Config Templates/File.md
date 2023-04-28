# **File**

DataOS allows you to create a Depot of type 'FILE' to read the CSV/ plain text data stored in the local file storage.

## **Requirements**

To connect, you need:

- Path

## **Template**

To create a Depot of type ‘FILE‘, use the following template:

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
  type: FILE                                # Depot type
  description: <description>              
  external: true
  spec:
      path: "tmp/dataos"                    # Data source specific configuration
```