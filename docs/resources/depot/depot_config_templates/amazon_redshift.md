# Amazon Redshift


DataOS allows you to connect to the Amazon Redshift database to read data from tables using Depots. Amazon Redshift is a fully managed and scalable data warehouse service in the cloud. You can perform analysis queries on your dataset using Workbench.

## Requirements

To connect to Redshift, you need:

- Hostname
- Port
- Database name
- User name and password

In case of accessing the Redshift Database in Flare workflows, you also need to have the following:

- Bucket name where your data belongs
- Relative path
- AWS access key
- AWS secret key

## Template

To create a Depot of type ‘REDSHIFT‘, use the following template:

```yaml
version: v1
name: <choose a depot name of your choice>
type: depot
tags:
  - redshift
layer: user
depot:
  type: REDSHIFT
  description: "Redshift Sample data"
  spec:
    host: <hostname>
    port: 5439
    database: "sample database"
    bucket: "tmdc-dataos-rubik"      
    relativePath: "development/redshift/data_02/"
  external: true
  connectionSecret:
    - acl: rw
      type: key-value-properties
      data:
        username: <username>
        password: <password>
        awsaccesskeyid: <access key>
        awssecretaccesskey: <secret key>
```