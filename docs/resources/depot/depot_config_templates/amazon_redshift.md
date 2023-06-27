# Amazon Redshift

DataOS provides the capability to establish a connection with the Amazon Redshift database for the purpose of reading data from tables using Depots. Amazon Redshift is a cloud-based, fully managed, and scalable data warehouse service. Analysis queries on your dataset can be performed using Workbench.

## Requirements

To establish a connection with Redshift, the following information is required:

- Hostname
- Port
- Database name
- User name and password

Additionally, when accessing the Redshift Database in Flare workflows, the following details are also necessary:

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
depot:
  type: REDSHIFT
  description: {{Redshift Sample data}}
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