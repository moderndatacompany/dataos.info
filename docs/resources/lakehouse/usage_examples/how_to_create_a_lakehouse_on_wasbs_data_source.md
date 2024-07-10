# How to create a Lakehouse on Windows Azure Storage Blob Secure (WASBS) data source?

This guide outlines the steps to create a Lakehouse Resource on Windows Azure Storage Blob Secure (WASBS) data source.

## **Procedure**

### **Step 1: Create Instance Secret manifests**

The first step involves creating Instance Secret manifest files for both read and read-write access. These Instance Secrets will store sensitive information like storage account keys and endpoint details within the Heimdall vault.

**Read Secrets Instance-secret manifest:** This manifest file is designed for read-only access. It contains the storage account name, key, and endpoint suffix.

```yaml
name: ${depot-name}-r
version: v1
type: instance-secret
description: "read secret"
layer: user
instance-secret:
	type: key-value
  acl: r
  data:
    azureendpointsuffix: ${azure-end-point-suffix}
    azurestorageaccountkey: ${azure-storage-account-key}
    azurestorageaccountname: ${azure-storage-account-name}
```

**Read-Write Instance-secret manifest:** This manifest file allows read-write access. Similar to the read-only secret but with 'rw' access control (acl).

```yaml
name: ${depot-name}-rw
version: v1
type: instance-secret
description: "read-write secret"
layer: user
instance-secret:
  type: key-value
  acl: rw
  data:
	  azureendpointsuffix: ${azure-end-point-suffix}
	  azurestorageaccountkey: ${azure-storage-account-key}
	  azurestorageaccountname: ${azure-storage-account-name}
```

### **Step 2: Apply the Instance-secret manifests**

Apply both the Instance-secret manifest by using the below command.

```shell
dataos-ctl resource apply -f ${file-path}
# or
dataos-ctl apply -f ${instance-secret-manifest-file-path}
```

### **Step 3: Create a Lakehouse manifest**

After setting up the Instance Secrets, the next step is to create a Lakehouse manifest. This file defines the configuration of your Lakehouse, including its type, associated compute resource, storage configuration, and query engine.

```yaml
version: v1alpha
name: ${depot-name}
layer: user
type: lakehouse
tags:
- Iceberg
- Azure
description: "Icebase depot of storage-type ABFSS"
lakehouse:
	type: iceberg
	compute: ${compute-name}
	iceberg:
    storage:
	    type: "wasbs"
	    wasbs:
	      account: ${abfss-account}
	      container: ${container}
	      relativePath: ${relative-path}
	      format: ICEBERG
	      endpointSuffix: ${end-point-suffix}
	    secrets:
	      - name: ${depot-name}-rw
		      keys:
		          - ${depot-name}-rw
		      allkeys: true    
	      - name: ${depot-name}-r
		      keys:
		          - ${depot-name}-r
		      allkeys: true 
	  metastore:
	    type: "iceberg-rest-catalog"
    queryEngine:
	    type: ${query-engine}
```

### **Step 4: Apply the Lakehouse manifest**

Finally, apply the Lakehouse manifest to instantiate your Lakehouse Resource. Ensure all the placeholders `${}` in the manifest are replaced with actual values before applying.

```shell
dataos-ctl apply -f ${lakehouse-manifest-file-path} -w ${workspace-name}
```