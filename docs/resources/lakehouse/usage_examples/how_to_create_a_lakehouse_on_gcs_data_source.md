# How to create a Lakehouse on Google Cloud Storage (GCS) data source?

This guide outlines the steps to create a Lakehouse resource on Google Cloud Storage (GCS) data source, focusing on the creation and application of essential YAML files.

## Procedure

### **Step 1: Create Instance Secret YAMLs**

The first step involves creating Instance Secret YAML files for both read and read-write access. These Instance Secrets will store sensitive information like storage account keys and endpoint details.

#### **Read Secrets YAML:**

This YAML file is designed for read-only access. It contains the storage account name, key, and endpoint suffix.

```yaml
name: {{gcs depot name}}-r
version: v1
type: instance-secret
description: "read secret"
layer: user
instance-secret:
  type: key-value-properties
  acl: r
  data:
    projectid: {{project id}}
    email: {{email}}
  files:
    gcskey_json: {{json file path}}
```

#### **Read-Write Secrets YAML:**

This YAML file allows read-write access. Similar to the read-only secret but with 'rw' access control (acl).

```yaml
name: {{gcs depot name}}-rw
version: v1
type: instance-secret
description: "read/write secrets"
layer: user
instance-secret:
  type: key-value-properties
  acl: rw
  data:
    projectid: {{project id}}
    email: {{email}}
  files:
    gcskey_json: {{json file path}}
```

### **Step 2: Apply the YAMLs**

Depending on your requirement (read-only or read-write), apply the corresponding secret YAML. Use the DataOS CLI interface to apply these YAML files.

```bash
dataos-ctl apply -f {{file path}}
```

#### Step 3: Create a Lakehouse YAML

After setting up the Instance Secrets, the next step is to create a Lakehouse YAML. This file defines the configuration of your Lakehouse, including its type, associated compute resource, storage configuration, and query engine.

```yaml
version: v1alpha
name: {{gcs depot name}}
layer: user
type: lakehouse
tags:
  - Iceberg
  - Azure
description: "Icebase depot of storage-type GCS"
lakehouse:
  type: iceberg
  compute: {{compute name}}
  iceberg:
    storage:
      type: "gcs"
      gcs:
        bucket: {{bucket name}}
        relativePath: {{relative path}}
        format: "ICEBERG"        
      secrets:
        - name: {{depot name}}-rw
          keys:
            - {{depot name}}-rw
          allkeys: true    
        - name: {{depot name}}-r
          keys:
            - {{depot name}}-r
          allkeys: true 
    metastore:
      type: "iceberg-rest-catalog"
    queryEngine:
      type: {{query engine}}
```

#### **Step 4: Apply the Lakehouse YAML**

Finally, apply the Lakehouse YAML to instantiate your Lakehouse resource. Ensure all the placeholders ({{ }}) in the YAML are replaced with actual values before applying. 

```bash
dataos-ctl apply -f {{lakehouse yaml path}} -w {{workspace name}}
```