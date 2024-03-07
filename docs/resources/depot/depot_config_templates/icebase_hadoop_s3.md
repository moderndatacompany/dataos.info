# Depot for Icebase

DataOS provides the capability to establish a connection with the Icebase Lakehouse over Amazon S3 or other object storages. We have provided the template for the manifest file to establish this connection. Follow these steps to create the depot:
**Step 1**: Copy the template from below and paste it in a code editor.
**Step 2**: Fill the values for the atttributes/fields declared in the YAML-based manifest file.
**Step 3**: Apply the file through DataOS CLI

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
name: "s3hadoopiceberg"
type: depot
tags:
  - S3
layer: user
description: "AWS S3 Bucket for Data"
depot:
  type: S3
  compute: runnable-default
  spec:
    bucket: $S3_BUCKET        # "tmdc-dataos-testing"
    relativePath: $S3_RELATIVE_PATH           # "/sanity"
    format: ICEBERG
    scheme: s3a       
  external: true
  connectionSecret:
    - acl: rw
      type: key-value-properties
      data:
        accesskeyid: $S3_ACCESS_KEY_ID
        secretkey: $S3_SECRET_KEY
        awsaccesskeyid: $S3_ACCESS_KEY_ID
        awssecretaccesskey: $S3_SECRET_KEY
        awsendpoint: $S3_ENDPOINT    
```
