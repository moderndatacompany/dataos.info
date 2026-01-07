# Delta Lake

Nilus supports Delta Lake as a batch ingestion source, enabling you to bring structured datasets from Azure Blob Storage, Amazon S3, or Google Cloud Storage (GCS) into the DataOS Lakehouse or other supported destinations.

!!! info
    Delta Lake is only supported via DataOS Depot. Direct connection URIs are **not** supported.


## Prerequisites

The following are the requirements for enabling Batch Data Movement in Delta Lake:

### **Storage Prerequisites**

The following are the storage requirements for different cloud providers:

* **Azure Blob Storage:** Existing container, proper RBAC permissions, optional custom endpoint configuration, storage firewall rules
* **Amazon S3:** Existing bucket, IAM roles/policies, optional VPC endpoint configuration, bucket versioning recommended
* **Google Cloud Storage:** Existing bucket, IAM roles, optional VPC service controls, optional CMEK for encryption

### **Required Parameters**

The following are the parameters needed:

* `container` / `bucket`: Storage container (Azure) or bucket (S3/GCS)
* `path`: Optional relative path inside the container/bucket
* `collection`: Collection name
* `dataset`: Dataset name

### **Authentication**

The following are the authentication methods for each storage type:

* **Azure Blob Storage:** Storage Account Name + Key (optional: endpoint suffix)
* **Amazon S3:** AWS Access Key ID + Secret Key + Region (optional: custom endpoint)
* **Google Cloud Storage:** HMAC credentials (Access Key + Secret Key) or Service Account JSON

### **Pre-created Depot**

A Depot must exist in DataOS with read-write access. To check the Depot, go to the Metis UI of the DataOS or use the following command:

```bash
dataos-ctl resource get -t depot -a

#Expected Output
NFO[0000] 🔍 get...                                     
INFO[0000] 🔍 get...complete 
|     NAME     | VERSION | TYPE  | STATUS | OWNER    |
| ------------ | ------- | ----- | ------ | -------- |
| synapsedepot | v2alpha | depot | active | usertest |
```

If the Depot is not created, use the following manifest configuration template to create the Delta Lake Depot:

??? note "Delta Lake Depot Manifest"

    The following manifest is for Amazon S3 Delta Lake:

    ```yaml
    name: ${{depot-name}}
    version: v2alpha
    type: depot
    description: ${{description}}
    tags:
        - ${{tag1}}
    owner: ${{owner-name}}
    layer: user
    depot:
      type: S3
      external: ${{true}}
      secrets:
        - name: ${{s3-instance-secret-name}}-r
          allkeys: true
        - name: ${{s3-instance-secret-name}}-rw
          allkeys: true
      s3:
        scheme: ${{s3a}}
        bucket: ${{project-name}}
        relativePath: ${{relative-path}}
        format: delta
        region: ${{us-gov-east-1}}
        endpoint: ${{s3.us-gov-east-1.amazonaws.com}}
    ```

    !!! info
        * Update variables such as `name`, `owner`, `compute`, `scheme`,`bucket` `format` `region` etc., and contact the DataOS Administrator or Operator to obtain the appropriate secret name.
        *   DataOS supports the Delta table format on the following object storage Depots:

        [Amazon S3](https://dataos.info/resources/depot/delta_table_format/#amazon-s3), [Azure Blob File System Secure (ABFSS)](https://dataos.info/resources/depot/delta_table_format/#azure-blob-file-system-secure-abfss), [Google Cloud Storage (GCS)](https://dataos.info/resources/depot/delta_table_format/#google-cloud-storage-gcs), [Windows Azure Storage Blob Service (WASBS)](https://dataos.info/resources/depot/delta_table_format/#windows-azure-storage-blob-service-wasbs).




## Sample Workflow Config

```yaml
name: nb-deltalake-test-01
version: v1
type: workflow
tags:
    - workflow
    - nilus-batch
description: Nilus Batch Workflow Sample for Delta Lake (S3) to DataOS Lakehouse
workspace: research
workflow:
  dag:
    - name: nb-job-01
      spec:
        stack: nilus:1.0
        compute: runnable-default
        logLevel: INFO
        resources:
          requests:
            cpu: 500m
            memory: 512Mi
        stackSpec:
          source:
            address: dataos://delta_depot
            options:
              source-table: analytics.events
          sink:
            address: dataos://testawslh
            options:
              dest-table: delta_retail.batch_events
              incremental-strategy: replace
```

!!! info
    Ensure that all placeholder values and required fields (e.g., connection `addresses`, `compute`, and access credentials) are properly updated before applying the configuration to a DataOS workspace.


Deploy the manifest file using the following command:

```bash
dataos-ctl resource apply -f ${{path to the Nilus Workflow YAML}}
```

## Supported Attribute Details

Nilus supports the following source options for Delta Lake:

| Option         | Required | Description                  |
| -------------- | -------- | ---------------------------- |
| `source-table` | Yes      | Format: `collection.dataset` |

!!! info "Core Concepts"

    - **Depot-Only Support**
   
        Delta Lake sources must be configured through Depot. Nilus does not support direct connections.
      
    - **Path Construction**

        Delta Lake datasets are referenced as:

        ```yaml
        <storage>://<container_or_bucket>/<relative_path>/<collection>/<dataset>
        ```

