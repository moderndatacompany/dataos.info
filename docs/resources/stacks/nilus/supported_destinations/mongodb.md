# MongoDB

Nilus supports **MongoDB as a batch destination**, enabling users to load structured or semi-structured data into MongoDB collections. MongoDB is a distributed NoSQL document database known for horizontal scalability, flexible schema design, and high availability.

Currently, MongoDB destinations in Nilus operate **exclusively in full-replace mode**, meaning the target collection is cleared and then fully rewritten during every run.

!!! info
    MongoDB as a batch destination **cannot be used in CDC pipelines**, as incremental sync modes (merge, upsert, append) are not supported.



## Prerequisites

Before configuring MongoDB as a sink, ensure the following:

- **MongoDB Server Access:**
    The MongoDB host must be reachable from the Nilus environment (self-hosted instance or MongoDB Atlas).

- **Authentication:**
    If authentication is enabled, a valid **username** and **password** are required.

- **Permissions:**
    The MongoDB user must have:

    - Read/write privileges on the target database.
    - Permission to create databases/collections, if they do not already exist.

- **Connection URI Requirements:**
    A standard MongoDB URI must be provided **without the database name appended**.

    ```bash
    mongodb://<username>:<password>@<host>:<port>
    ```

    - `port` defaults to **27017** if omitted.
    - Any valid MongoDB connection string parameter may be appended (e.g., `tls=true`, `retryWrites=true`).


!!! info
    Specify the target database and collection using `dest-table` in the format `database.collection`.



## Sink Configuration

=== "Syntax"
    ```yaml
    sink:
      address: mongodb://<username>:<password>@<host>:<port>
      options:
        dest-table: <database.collection>
        incremental-strategy: replace
    ```

=== "Example"
    ```yaml
    name: mongo-dest
    version: v1
    type: workflow
    tags:
      - google-sheet
      - workflow
      - nilus-batch
    description: Nilus Batch Service Sample
    workspace: public
    workflow:
      dag:
        - name: mongo-dest
          spec:
            stack: nilus:1.0
            compute: runnable-default
            resources:
              requests:
                cpu: 100m
                memory: 256Mi
            logLevel: Info
            stackSpec:
              source:
                address: dataos://postgresdepot
                options:
                  source-table: "retail.product" 
              sink:
                address: dataos://mongodepot
                options:
                  dest-table: "retail.product"
                  incremental-strategy: replace
    ```


### **URI & Parameter Details**

| Parameter    | Required              | Description                           | Callouts                                             |
| ------------ | --------------------- | ------------------------------------- | ---------------------------------------------------- |
| `username`   | Yes (if auth enabled) | Username for authentication           | Ensure the user is allowed to write to the target DB |
| `password`   | Yes (if auth enabled) | Password associated with the user     | —                                                    |
| `host`       | Yes                   | MongoDB server hostname               | Must be reachable from Nilus                         |
| `port`       | No                    | Server port (default: `27017`)        | —                                                    |
| Query Params | No                    | Connection options (`tls=true`, etc.) | Useful for Atlas or SSL environments                 |


!!! info
    **Do not append the database name in the URI.** Specify the database + collection using `dest-table` as: `database.collection`.



## Sink Attribute Details

Nilus supports the following MongoDB sink options:

| Option                 | Required | Description                         | Callouts                                   |
| ---------------------- | -------- | ----------------------------------- | ------------------------------------------ |
| `dest-table`           | Yes      | Specifies `<database>.<collection>` | Creates DB/collection if they do not exist |
| `incremental-strategy` | Yes      | Must be `replace`                   | Collection is cleared before each load     |

**Destination Table Format**

```bash
database.collection
```

**Example:**

```bash
analytics.users
```



### **Supported Incremental Strategies**

| Strategy  | Supported | Behavior                                          |
| --------- | --------- | ------------------------------------------------- |
| `replace` | ✅ Yes     | Drops/clears the collection and rewrites all data |
| `append`  | ❌ No      | Not supported                                     |
| `merge`   | ❌ No      | Not supported                                     |
| `upsert`  | ❌ No      | Not supported                                     |

!!! info
    MongoDB as a destinations always run in **full replace mode**.



## Behavior & Capabilities

- Data is written in batches via MongoDB bulk operations.

- If the collection exists:
  
    - It is **fully cleared** under `replace` strategy.

- If the collection does not exist, Nilus automatically creates it.

### **Document ID Behavior**

- If incoming data contains `_id`, it becomes the MongoDB document `_id`.
- If `_id` is not present, MongoDB auto-generates one.

### **Type Mapping**

Nilus maps common types automatically:

| Incoming Type  | MongoDB Representation |
| -------------- | ---------------------- |
| Numbers        | int / long / double    |
| Timestamps     | ISODate                |
| Booleans       | boolean                |
| Strings        | string                 |
| Nested Objects | Embedded documents     |
| Lists          | Arrays                 |

Unsupported or complex types may be stringified.


## Performance Considerations

- Since **replace mode rewrites the entire collection**, it is best suited for:

    - Small to medium datasets
    - Non-real-time workloads

- Not ideal for:
  
    - Collections with millions of documents
    - Use-cases requiring incremental updates or CDC

### **Recommendations for Large Data Volumes**

- Use a Lakehouse (Delta/BigQuery/S3) as the primary destination.
- Sync to MongoDB downstream using a tool that supports incremental merges.



## Troubleshooting

| Issue                      | Possible Cause                                | Resolution                                                      |
| -------------------------- | --------------------------------------------- | --------------------------------------------------------------- |
| Authentication failure     | Wrong credentials or missing roles            | Validate username/password and roles. Verify auth database (default is `admin` unless specified) |
| Database not found         | User lacks permission to create databases     | Grant appropriate privileges                                    |
| Duplicate key `_id` errors | Incoming data contains duplicate `_id` values | Remove or regenerate `_id` upstream                             |
| TLS/SSL errors             | Invalid certificates or missing TLS params    | Add URI params like `tls=true&tlsAllowInvalidCertificates=true` |

