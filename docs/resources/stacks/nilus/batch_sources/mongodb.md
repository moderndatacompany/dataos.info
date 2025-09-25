# MongoDB

MongoDB is a popular open-source NoSQL database known for its flexibility and scalability. Nilus supports MongoDB as a **batch ingestion source**, allowing users to efficiently move data into the DataOS Lakehouse or other supported destinations.

Nilus connects to MongoDB through **DataOS Depot**, which provides a managed, secure way to store and reuse connection configurations. In Depot:

* The configuration uses the `dataos://` URI scheme
* Authentication and SSL/TLS are handled by the Depot service
* Secrets and connection details are centrally managed

## Prerequisites

The following are the requirements for enabling Batch Data Movement in MongoDB:

### **Database User Permissions**

The connection user must have at least **read** privileges on the source collection:

```jsx
{
  "role": "read",
  "db": "<database_name>",
  "collection": "<collection_name>"
}
```

### **Pre-created MongoDB Depot**

A Depot must exist in DataOS with read-write access. To check the Depot, go to the Metis UI of the DataOS or use the following command:

```bash
dataos-ctl resource get -t depot -a

#Expected Output
NFO[0000] 🔍 get...                                     
INFO[0000] 🔍 get...complete 
|    NAME      | VERSION | TYPE  | STATUS | OWNER    |
| ------------ | ------- | ----- | ------ | -------- |
| mongodbdepot | v2alpha | depot | active | usertest |
```

If the Depot is not created, use the following manifest configuration template to create the MongoDB Depot:

??? note "MongoDB Depot Manifest"

    ```yaml
    name: ${{depot-name}}
    version: v2alpha
    type: depot
    tags:
        - ${{tag1}}
        - ${{tag2}}
    layer: user
    depot:
      type: mongodb                                 
      description: ${{description}}
      compute: ${{runnable-default}}
      mongodb:                                          
        subprotocol: ${{"mongodb+srv"}}
        nodes: ${{["clusterabc.ezlggfy.mongodb.net"]}}
      external: ${{true}}
      secrets:
        - name: ${{instance-secret-name}}-r
          allkeys: ${{true}}

        - name: ${{instance-secret-name}}-rw
          allkeys: ${{true}}
    ```

    !!! info
        Update variables such as `name`, `owner`, `compute`, `layer`, etc., and contact the DataOS Administrator or Operator to obtain the appropriate secret name.






## Sample Workflow Config

```yaml
name: nb-mdb-test-01
version: v1
type: workflow
tags:
    - workflow
    - nilus-batch
description: Nilus Batch Workflow Sample for MongoDB to S3 Lakehouse
workspace: research
workflow:
  dag:
    - name: nb-job-01
      spec:
        stack: nilus:1.0
        compute: runnable-default
        resources:
          requests:
            cpu: 100m
            memory: 128Mi
        logLevel: INFO
        stackSpec:
          source:
            address: dataos://mongodbdepot
            options:
              source-table: "retail.customer"
          sink:
            address: dataos://testinglh
            options:
              dest-table: mdb_retail.batch_customer_1
              incremental-strategy: replace
              aws_region: us-west-2
```

!!! info
    Ensure that all placeholder values and required fields (e.g., connection addresses, slot names, and access credentials) are properly updated before applying the configuration to a DataOS workspace.


Deploy the manifest file using the following command:

```bash
dataos-ctl resource apply -f ${{path to the Nilus Workflow YAML}}
```


## Supported Attribute Details

Nilus supports the following source options for MongoDB:

| Option             | Required | Description                                                                   |
| ------------------ | -------- | ----------------------------------------------------------------------------- |
| `source-table`     | Yes      | Format: `database.collection` or `database.collection:[aggregation_pipeline]` |
| `filter_`          | No       | MongoDB filter document to apply                                              |
| `projection`       | No       | Fields to include/exclude in the result                                       |
| `chunk_size`       | No       | Number of documents to load in each batch (default: 10000)                    |
| `parallel`         | No       | Enable parallel loading (default: false)                                      |
| `data_item_format` | No       | Format for loaded data (`object` or `arrow`)                                  |
| `incremental-key`  | No       | Field used for incremental batch ingestion                                    |
| `interval-start`   | No       | Optional lower bound timestamp for incremental ingestion                      |
| `interval-end`     | No       | Optional upper bound timestamp for incremental ingestion                      |

!!! info
    Nilus supports incremental batch ingestion by using a field (e.g., `updated_at`) to identify new or updated documents.

    * Field must be indexed for performance
    * Field must be consistently present in documents

    Batch ingestion can be driven by MongoDB aggregation pipelines, enabling complex transformations before loading.

