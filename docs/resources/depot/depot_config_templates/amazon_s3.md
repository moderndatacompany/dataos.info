# Amazon S3

DataOS allows you to connect to Amazon S3 to read objects within buckets using Depots. The Depot enables access to S3 object metadata. Amazon S3 is a key-based object store. Each object is stored and retrieved using a unique key. Each account contains one or more buckets to store data and to organize the Amazon S3 namespace. An object is uniquely identified within a bucket by a key (unique identifier) and a version ID.

## Requirements

To connect to Amazon S3, you need:

- AWS access key id
- AWS bucket name
- Secret access key
- Scheme
- Relative Path
- Format

## Template

To create a Depot of type ‘S3‘, use the following template:

```yaml
version: v1
name: <depot-name>
type: depot
tags:
  - <tag1>
owner: <owner-name>
layer: user
depot:
  type: S3                                          **# Depot type**
  description: <description>
  external: true
  connectionSecret:                                 **# Data source specific configurations**
    - acl: rw
      type: key-value-properties
      data:
        accesskeyid: ${AWS_ACCESS_KEY_ID}
        secretkey: ${AWS_SECRET_ACCESS_KEY}
        awsaccesskeyid: ${AWS_ACCESS_KEY_ID}
        awssecretaccesskey: ${AWS_SECRET_ACCESS_KEY}
    - acl: r
      type: key-value-properties
      data:
        accesskeyid: ${AWS_ACCESS_KEY_ID}
        secretkey: ${AWS_SECRET_ACCESS_KEY}
        awsaccesskeyid: ${AWS_ACCESS_KEY_ID}
        awssecretaccesskey: ${AWS_SECRET_ACCESS_KEY}
  spec:                                             **# Data source specific configurations**
    # default scheme "s3a"
    scheme: <s3a>
    bucket: <project-name>
    relativePath: <relative-path>
    format: <format>
```
