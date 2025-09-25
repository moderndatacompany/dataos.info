# BigQuery

**Google BigQuery** is a fully managed, serverless data warehouse on Google Cloud, providing scalable and cost-effective analytics.

Nilus supports BigQuery as both a **batch ingestion source** and a **destination**, enabling efficient data movement between BigQuery and the DataOS Lakehouse or other supported destinations.

## Prerequisites

The following are the requirements for enabling Batch Data Movement in BigQuery:

### **Service Account Permissions**

The service account used for BigQuery connections must have the following roles:

* `roles/bigquery.dataViewer` (BigQuery Data Viewer)
* `roles/bigquery.jobUser` (BigQuery Job User)
* `roles/bigquery.user` (BigQuery User)

### **Required Parameters**

The following are the required parameters:

* `project-name`: Google Cloud project ID
* `credentials_path`: Path to service account JSON file
* `credentials_base64`: Base64-encoded credentials JSON (alternative to path)
* `location`: Dataset location (default: `US`)

### **Pre-created Redshift Depot**

A Depot must exist in DataOS with read-write access. To check the Depot, go to the Metis UI of the DataOS or use the following command:

```bash
dataos-ctl resource get -t depot -a

#Expected Output
NFO[0000] 🔍 get...                                     
INFO[0000] 🔍 get...complete 
| NAME          | VERSION | TYPE  | STATUS | OWNER    |
| ------------- | ------- | ----- | ------ | -------- |
| bigquerydepot | v2alpha | depot | active | usertest |
```

If the Depot is not created, use the following manifest configuration template to create the BigQuery Depot:

??? note "BigQuery Depot Manifest"

    ```yaml
    name: ${{depot-name}}
    version: v2alpha
    type: depot
    description: ${{description}} # optional
    tags:
        - ${{dropzone}}
        - ${{bigquery}}
    owner: ${{owner-name}}
    layer: user
    depot:
      type: BIGQUERY                 
      external: ${{true}}
      secrets:
        - name: ${{instance-secret-name}}-r
          keys: 
            - ${{instance-secret-name}}-r
        - name: ${{instance-secret-name}}-rw
          keys: 
            - ${{instance-secret-name}}-rw
      bigquery:  # optional                         
        project: ${{project-name}} # optional
        params: # optional
          ${{"key1": "value1"}}
          ${{"key2": "value2"}}
    ```

    !!! info
        Update variables such as `name`, `owner`, and `layer`, and contact the DataOS Administrator or Operator to obtain the appropriate instance secret name and parameters.




## Sample Workflow Config

```yaml
name: nb-bq-test-01
version: v1
type: workflow
tags:
    - workflow
    - nilus-batch
description: Nilus Batch Workflow Sample for BigQuery to DataOS Lakehouse
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
            address: dataos://bigquery_depot
            options:
              source-table: analytics.orders
              incremental-key: updated_at
              staging-bucket: gs://my-bucket
          sink:
            address: dataos://testawslh
            options:
              dest-table: bq_retail.batch_orders
              incremental-strategy: append
              aws_region: us-west-2

```

!!! info
    Ensure that all placeholder values and required fields (e.g., connection addresses, slot names, and access credentials) are properly updated before applying the configuration to a DataOS workspace.


Deploy the manifest file using the following command:

```bash
dataos-ctl resource apply -f ${{path to the Nilus Workflow YAML}}
```

## Supported Attribute Details

Nilus supports the following source options for BigQuery:

| Option            | Required | Description                                                                             |
| ----------------- | -------- | --------------------------------------------------------------------------------------- |
| `source-table`    | Yes      | Table name (`dataset.table` or `project.dataset.table`) or query prefixed with `query:` |
| `incremental-key` | No       | Column used for incremental ingestion                                                   |



!!! info
    **Staging with GCS**

    * For large data transfers, BigQuery can use Google Cloud Storage (GCS) as a staging area.
    * Requires additional IAM permissions: `Storage Object Viewer` and `Storage Object Creator`.

    **Incremental Loading**

    * Supported using timestamp or sequential key columns (e.g., `updated_at`).
    * Default incremental key in usage tracking: `start_time`.






