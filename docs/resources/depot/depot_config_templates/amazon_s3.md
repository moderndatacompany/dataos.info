# Depot for Amazon S3

DataOS provides the capability to establish a connection with the Amazon S3 buckets. We have provided the template for the manifest file to establish this connection. Follow these steps to create the depot:
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
name: {{depot-name}}
version: v1
type: depot
tags:
  - {{tag1}}
owner: {{owner-name}}
layer: user
description: {{description}}
depot:
  type: S3                                          
  external: {{true}}
  spec:                                            
    scheme: {{s3a}}
    bucket: {{project-name}}
    relativePath: {{relative-path}}
    format: {{format}}
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
```
