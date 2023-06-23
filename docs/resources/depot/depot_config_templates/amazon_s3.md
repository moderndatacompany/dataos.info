# Amazon S3

DataOS offers the capability to connect to Amazon S3 for accessing objects within buckets using Depots. Depots facilitate access to S3 object metadata. Amazon S3 functions as a key-based object store, where each object is stored and retrieved using a unique key. An account can have multiple buckets for data storage and organization within the Amazon S3 namespace. An object within a bucket is identified by a unique key and a version ID.

## Requirements

To establish a connection with Amazon S3, the following information is required:

- AWS access key ID
- AWS bucket name
- Secret access key
- Scheme
- Relative Path
- Format

## Template

To create a Depot of type ‘S3‘, utilize the following template:

```yaml
version: v1
name: {{depot-name}}
type: depot
tags:
  - {{tag1}}
owner: {{owner-name}}
layer: user
depot:
  type: S3                                          
  description: {{description}}
  external: {{true}}
  connectionSecret:                                
    - acl: rw
      type: key-value-properties
      data:
        accesskeyid: {{AWS_ACCESS_KEY_ID}}
        secretkey: {{AWS_SECRET_ACCESS_KEY}}
        awsaccesskeyid: {{AWS_ACCESS_KEY_ID}}
        awssecretaccesskey: {{AWS_SECRET_ACCESS_KEY}}
    - acl: r
      type: key-value-properties
      data:
        accesskeyid: {{AWS_ACCESS_KEY_ID}}
        secretkey: {{AWS_SECRET_ACCESS_KEY}}
        awsaccesskeyid: {{AWS_ACCESS_KEY_ID}}
        awssecretaccesskey: {{AWS_SECRET_ACCESS_KEY}}
  spec:                                            
    scheme: {{s3a}}
    bucket: {{project-name>}}
    relativePath: {{relative-path}}
    format: {{format}}
```
