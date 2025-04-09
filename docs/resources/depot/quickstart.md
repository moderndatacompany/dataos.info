# Quickstart with Depot

This section focuses on Data Source Connectivity using the Depot, a critical responsibility of a DataOS operator or a data developer that involves configuring Depots, establishing secure access to diverse data sources, and maintaining operational efficiency. By the end, the users will have the tools to ensure workflows remain efficient, data remains protected, and a user team can access data sources securely.


## Scenario

A key project in an organization requires real-time data from multiple systems. Every configuration a user manages will directly impact the team's ability to work with the data efficiently and securely. As a user step into this challenge, the user faced multiple objectives:

- Establishing secure connections to relational databases, cloud object stores, and other critical data sources.

- Configuring Depots to streamline these integrations.

- Ensuring all credentials are encrypted and security best practices are followed.

Follow the steps given below to integrate a growing number of data sources into DataOS for your team. These connections are essential for powering Data Products that fuel decision-making across the organization.

## Quick concepts

The Depot Resource in DataOS provides a standardized way to connect to a variety of enterprise data sources, such as:

- Cloud-based object stores

- Databases

- Data warehouses

- NoSQL data stores

This versatility allows a user to integrate structured, semi-structured, and unstructured data seamlessly. Using Depots, a user can set up data sources to:

- Create high-quality data pipelines for building robust data products.

- Utilize query clusters for efficient data querying.

- Develop comprehensive semantic models.

## Prerequisites

Before diving into configuring data source connections, make sure everything is ready:

1. **Check required Permissions**: Some tasks require specific permissions typically assigned to DataOS Operators. Ensure a user has access to one of the following permission sets either via use-case or via tags:

    | **Access Permission (via use-cases)** | **Access Permissions (via tags)** |
    | ------------------------------------- | --------------------------------- |
    | Read Workspace                        | `roles:id:data-dev `              |
    | Manage All Depot                      | `roles:id:system-dev`             |
    | Read All Dataset                      | `roles:id:user`                   |
    | Read all secrets from Heimdall        |                                   |

2. **Check CLI installation and initialization**: a user needs this text-based interface that allows a user to interact with the DataOS context via command prompts. Click [here](/interfaces/cli/) to learn more.

3. **Manage Credentials Securely**: Use Instance Secrets for storing a user data source credentials, ensuring sensitive information remains protected.

    <aside class="callout">
    🗣️ To prevent credential exposure, contact DataOS administrator and understand the best practices for handling sensitive data.
    </aside>

4. **Organize a user Code Repository**: Place Depot manifests in a private, permission-controlled repository to maintain security and compliance.

## Data source connection - PostgreSQL

For demonstration purposes, we'll use a PostgreSQL database in this example. However, the same process applies to any database that supports the JDBC protocol, such as MySQL, MariaDB, and MSSQL-Server.

With permissions set up, the next step is to establish a connection from DataOS to a user-hosted PostgreSQL database. This connection is vital for seamless data retrieval, enabling a user to access and work with PostgreSQL datasets directly in DataOS. It lays the foundation for building data pipelines, executing queries, and developing valuable data products using a user PostgreSQL data source. 

## Steps to create a Depot

First, we'll create instance secrets containing the credentials required to connect to the data source. Then, we'll reference these instance secrets in the Depot. This approach strengthens security while ensuring seamless compatibility with DataOS Resources.

### **Step 1: Create an Instance Secret manifest file**

The first step is to create an Instance Secret to securely store the credentials needed for connecting to the PostgreSQL database.

**Drafting the manifest**

Begin by drafting the manifest file for a read-only Instance Secret:

```yaml
# PostgreSQL Read Instance-secret Manifest

name: postgres-r # Unique identifier for Resource, replace ${DEPOT_NAME} with depot name
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

**Configuring Instance Secret manifest attributes**

Replace the placeholders with actual values specific to your database setup:

| **Attribute** | **Placeholder** | **Description** | **Example Value** |
| --- | --- | --- | --- |
| `name` | `${DEPOT_NAME}-${ACCESS_CONTROL_LIST}` | Unique name for the Instance Secret | `postgresdepot-r` |
| `description` | `${DESCRIPTION}` | Purpose of the Instance Secret | "Postgres read secret" |
| `acl` | `${ACCESS_CONTROL_LIST}` | Access Control List | `r` (for read access) |
| `username` | `$POSTGRES_USERNAME` | Username for the PostgreSQL database | `max_postgres_user` |
| `password` | `$POSTGRES_PASSWORD` | Password for the PostgreSQL database | `securepassword123` |


**Deploying the Instance Secret**

Once the manifest file is ready, deploy it using the DataOS CLI. Run the following command to apply the configuration:

```bash
dataos-ctl resource apply -f /path/to/instance_secret.yml
```

This step ensures that the database credentials are securely stored and ready for use in the next step.

<aside class="callout">
🗣 If you don’t have the necessary credentials, contact your administrator. They will create the instance secret for you and provide its details, which you can then reference in the Depot.
</aside>

### **Step 2: Create a Depot Manifest File**

With the Instance Secret deployed, the next task is to create a Depot that defines the connection configuration for your PostgreSQL database. The Depot acts as a bridge between DataOS and your data source.

**Drafting the Depot manifest**

Draft the manifest file for the Depot:

```yaml
# PostgreSQL Depot Manifest
name: postgres    # Unique name for the Depot
version: v2alpha  # Manifest version
type: depot       # Type of the Resource
layer: user
depot:
  type: jdbc                 
  description: default postgres depot
  external: true
  secrets:
    - name: postgres-rw   # Reference the Instance Secret for read & write access
      keys: 
        - postgres-rw
      allkeys: true

    - name: postgres-r    # Reference the Instance Secret for read access
      keys: 
        - postgres-r
      allkeys: true
    
  jdbc:
    subprotocol: postgresql
    host: usr-db-dataos-ck-eymm-dataostra-stg.postgres.database.azure.com # Replace with the database host URL
    port: 5432  # Replace with the database port number
    database: postgres  # Replace with the database name to connect to
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

<aside class="callout">
🗣️ Ensure that the name of your Instance secret is ${depot-name}-${acl}. For instance, if your Depot name is postgres and the acl(access control list) is rw, then the instance secret name will be postgres-rw.
</aside>

### **Step 5: Test data access**

**Extracting metadata**

Finally, run a Scanner Workflow to extract metadata of the connected data source to validate that the Depot is established successfully. This step completes the process of establishing a secure connection from DataOS to the PostgreSQL database.

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

To simplify the creation of depots for commonly used data sources, a set of pre-defined manifest [templates](/resources/depot/#templates-of-depot-for-different-source-systems) is available. These templates provide a quick starting point for setting up depots for popular data sources.

To use these templates, you must fill in the key-value properties in the manifest file with the specific details of your data source. The required values will vary depending on the data source. A basic understanding of your organization's data infrastructure, as well as the necessary credentials or connection details, is essential for configuring these templates effectively.



**Check your Depots**

```bash
dataos-ctl get -t depot
```

**View all Depots (with permissions):**

```bash
dataos-ctl get -t depot -a
```

Depot details can also be explored via the Metis UI in DataOS.

## Additional learning resources

Explore the following resources to enhance your understanding of data source connections:

- [Depot Resource Documentation](https://dataos.info/resources/depot/)
- [Instance Secret Resource Documentation](https://dataos.info/resources/instance_secret)
- [Quick Guide: Depot Creation with DataOS CLI](/quick_guides/depot_creation_cli/)

With this knowledge, you are now equipped to connect DataOS to a wide variety of data sources.
