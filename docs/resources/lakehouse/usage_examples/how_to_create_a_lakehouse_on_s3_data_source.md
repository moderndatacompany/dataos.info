# How to create a Lakehouse on Amazon Simple Storage Service (S3) data source?

This guide outlines the steps to create a Lakehouse resource on Amazon Simple Storage Service (S3) data source.

## Procedure

### **Step 1: Create Instance Secret manifest**

The first step involves creating Instance Secret manifest files for both read and read-write access. These Instance Secrets will store sensitive information like storage account keys and endpoint details.

**Read Secret manifest:** This manifest file is designed for read-only access. It contains the storage account name, key, and endpoint suffix.

```yaml
name: ${s3-depot-name}-r
version: v1
type: instance-secret
description: "read secrets"
layer: user
instance-secret:
  type: key-value-properties
  acl: r
  data:
    accesskeyid: ${access-key-id}
    awsaccesskeyid: ${aws-access-key-id}
    awssecretaccesskey: ${aws secret access key}
    secretkey: ${secret-key}
```

**Read-Write Secrets manifest:** This manifest file allows read-write access. Similar to the read-only secret but with 'rw' access control (acl).

```yaml
name: ${s3-depot-name}-rw
version: v1
type: instance-secret
description: "read write secrets"
layer: user
instance-secret:
  type: key-value-properties
  acl: rw
  data:
    accesskeyid: ${access-key-id}
    awsaccesskeyid: ${aws-access-key-id}
    awssecretaccesskey: ${aws-secret-access-key}
    secretkey: ${secret-key}
```

### **Step 2: Apply the manifest**

Depending on your requirement (read-only or read-write), apply the corresponding secret manifest. Use the DataOS CLI interface to apply these manifest files.

```bash
dataos-ctl apply -f ${file path}
```

### **Step 3: Create a Lakehouse manifest**

After setting up the Instance Secrets, the next step is to create a Lakehouse manifest file. This file defines the configuration of your Lakehouse, including its type, associated compute resource, storage configuration, and query engine.

```yaml
name: ${s3-depot-name}
version: v1alpha
layer: user
type: lakehouse
tags:
  - Iceberg
  - Azure
description: "Icebase depot of storage-type S3"
lakehouse:
  type: iceberg
  compute: runnable-default
  iceberg:
    storage:
      type: s3
      s3:
        bucket: ${s3 bucket name}        # "tmdc-dataos-testing"
        relativePath: ${relative path}
      secrets:
        - name: ${s3-depot-name}-rw
          keys:
            - ${s3-depot-name}-rw
          allkeys: true    
        - name: ${s3-depot-name}-r
          keys:
            - ${s3-depot-name}-r
          allkeys: true 
    metastore:
      type: "iceberg-rest-catalog"
    queryEngine:
      type: ${query engine}
```

### **Step 4: Apply the Lakehouse manifest**

Finally, apply the Lakehouse manifest to instantiate your Lakehouse resource. Ensure all the placeholders `${}` in the YAML are replaced with actual values before applying.

```bash
dataos-ctl apply -f ${lakehouse-manifest-path} -w ${workspace-name}
```