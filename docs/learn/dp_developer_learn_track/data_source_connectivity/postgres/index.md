# Data source connectivity- Postgres

In this topic, you'll learn about data connectivity by establishing a connection from the DataOS platform to a hosted PostgreSQL database.

## Scenario

Imagine you are a data engineer or Data Product Developer and you need to integrate various data sources within DataOS without moving the data. By configuring a Depot, you can establish a secure connection to your PostgreSQL database, making it accessible for querying, building pipelines, and creating data products directly in DataOS. This setup not only enhances data security but also promotes interoperability with a wide range of DataOS Resources.

### **Step 1: Create an Instance Secret manifest file**

The first step is to create an Instance Secret to securely store the credentials needed for connecting to the PostgreSQL database.

#### **Drafting the manifest**

Begin by drafting the manifest file for a read-only Instance Secret:

```yaml
# PostgreSQL Read Instance-secret Manifest

name: postgresdepot-r # Unique identifier for Resource, replace ${DEPOT_NAME} with depot name
version: v1 # Manifest version
type: instance-secret # Type of the Resource
description: Postgres Depot instance secret # Purpose of the Instance-secret
layer: user # DataOS layer
instance-secret:
  type: key-value-properties # Secret type
  acl: ${ACCESS_CONTROL_LIST} # Access control: 'r' for read-only
  data:
    username: $POSTGRES_USERNAME # replace with postgres username
    password: $POSTGRES_PASSWORD # replace with postgres password
```

<aside class="callout">
📖 Best Practice: You can use enviroment variables for attributes like `$POSTGRES_USERNAME` and `$POSTGRES_PASSWORD` to ensure that sensitive data is not hardcoded into the manifest file.

</aside>

#### **Configuring Instance Secret manifest attributes**

Replace the placeholders with actual values specific to your database setup:

| **Attribute** | **Placeholder** | **Description** | **Example Value** |
| --- | --- | --- | --- |
| `name` | `${DEPOT_NAME}-${ACCESS_CONTROL_LIST}` | Unique name for the Instance Secret | `postgresdepot-r` |
| `description` | `${DESCRIPTION}` | Purpose of the Instance Secret | "Postgres read secret" |
| `acl` | `${ACCESS_CONTROL_LIST}` | Access Control List | `r` (for read access) |
| `username` | `$POSTGRES_USERNAME` | Username for the PostgreSQL database | `max_postgres_user` |
| `password` | `$POSTGRES_PASSWORD` | Password for the PostgreSQL database | `securepassword123` |


#### **Deploying the Instance Secret**

Once the manifest file is ready, deploy it using the DataOS CLI. Run the following command to apply the configuration:

```bash
dataos-ctl resource apply -f /path/to/instance_secret.yml
```

This step ensures that the database credentials are securely stored and ready for use in the next step.


### **Step 2: Create a Depot Manifest File**

With the Instance Secret deployed, the next task is to create a Depot that defines the connection configuration for your PostgreSQL database. The Depot acts as a bridge between DataOS and your data source.

#### **Drafting the Depot manifest**

Draft the manifest file for the Depot:

```yaml
# PostgreSQL Depot Manifest

name: postgres-depot # Unique name for the Depot
version: v2alpha # Manifest version
type: depot # Type of the Resource
layer: user # DataOS layer
depot:
  type: postgresql
  description: PostgreSQL data source connection
  external: true
  secrets:
    - name: postgres-depot-r # Reference the Instance Secret for read access
      allkeys: true
  postgresql:
    subprotocol: postgresql
    host: db.postgres.example.com # Replace with the database host URL
    port: 5432 # Replace with the database port number
    database: sales_data # Replace with the database name to connect to
```

### **Step 3: Applying the Depot manifest**

Apply the Depot manifest using the following command:

```bash
dataos-ctl resource apply -f /path/to/depot_manifest.yml
```

### **Step 4: Verify the Connection**

To ensure the connection is successfully established, you can verify the Depot status using the DataOS CLI:

```bash
dataos-ctl get -t depot
```

This command displays the details of the configured Depot, confirming that it is active and properly connected to the PostgreSQL database.

---

### **Step 5: Test data access**

**Extracting metadata**

Finally, run a Scanner Workflow to extracct metadata of the connected data source to validate that the Depot is established successfully. This step completes the process of establishing a secure connection from DataOS to the PostgreSQL database.

```yaml
version: v1
name: postgresdepotscanner
type: workflow
tags:
  - postgres
  - scanner
description: The job scans schema tables and register metadata
workflow:
  dag:
    - name: postgresdepotjob
      description: The job scans schema from postgres depot tables and register metadata to metis
      spec:
        stack: scanner:2.0
        compute: runnable-default
        stackSpec:
          depot: dataos://postgresdepot          # Postgres depot name
```

---

## Additional learning resources

The following resources to deepen your understanding of data source connections:

- [Depot Resource Documentation](https://dataos.info/resources/depot/)
- [Instance Secret Resource Documentation](https://dataos.info/resources/instance_secret)
- [Quick Guide: Depot Creation with DataOS CLI](/quick_guides/depot_creation_cli/)

With this knowledge, you are now equipped to connect DataOS to a wide variety of data sources.

## Next Step

With Depot in place, you are now ready to build data pipelines to deliver reliable data for your data products ensuring seamless data flow.
To learn more, refer to [Building and maintaining data pipelines](/learn/dp_developer_learn_track/build_pipeline/).