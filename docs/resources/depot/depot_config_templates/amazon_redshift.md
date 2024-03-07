# Depot for Amazon Redshift

DataOS provides the capability to establish a connection with the Amazon Redshift database. We have provided the template for the manifest file to establish this connection. Follow these steps to create the depot:
**Step 1**: Copy the template from below and paste it in a code editor.
**Step 2**: Fill the values for the atttributes/fields declared in the YAML-based manifest file.
**Step 3**: Apply the file through DataOS CLI

## Requirements

To establish a connection with Redshift, the following information is required:

- Hostname
- Port
- Database name
- User name and password

Additionally, when accessing the Redshift Database in Workflows or other DataOS Resources, the following details are also necessary:

- Bucket name where the data resides
- Relative path
- AWS access key
- AWS secret key

## Template

To create a Depot of type ‘REDSHIFT‘, utilize the following template:

```yaml
name: {{redshift-depot-name}}
version: v1
type: depot
tags:
  - {{redshift}}
layer: user
description: {{Redshift Sample data}}
depot:
  type: REDSHIFT
  spec:
    host: {{hostname}}
    subprotocol: {{subprotocol}}
    port: {{5439}}
    database: {{sample-database}}
    bucket: {{tmdc-dataos}}
    relativePath: {{development/redshift/data_02/}}
  external: {{true}}
  connectionSecret:
    - acl: {{rw}}
      type: key-value-properties
      data:
        username: {{username}}
        password: {{password}}
        awsaccesskeyid: {{access key}}
        awssecretaccesskey: {{secret key}}
```