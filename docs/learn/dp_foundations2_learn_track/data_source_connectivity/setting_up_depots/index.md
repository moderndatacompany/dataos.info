# Setting Up Depots

In this topic, you’ll learn how to establish secure connections from DataOS to your external data sources using Depots—without moving any data. 

## Scenario

Imagine you are a DataOS Operator or Data Product Developer and you need to integrate various data sources within DataOS. For this example, the data for your use case is stored in PostgreSQL and Azure BLOB Storage.

By setting up Depots, you can securely connect to these systems and enable data access for exploration, workflows, and data product creation—right within DataOS.

  > We'll walk through a PostgreSQL example, but the process applies to any JDBC-compatible system like MySQL, MariaDB, or MSSQL Server.

## Steps to create a Depot for PostgreSQL

To keep credentials secure and decoupled from Depot configuration, we’ll first create Instance Secrets, then reference them in a Depot manifest.

### **Step 1: Create an Instance Secret manifest file**

The Instance Secret securely stores your database credentials.

#### **Drafting the manifest**

Create separate secrets for access level ‘r’ and ‘rw’. We will begin by drafting the manifest file for a read-only Instance Secret:

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

<aside class="callout">
🗣 If you don’t have the necessary credentials, contact your administrator. They will create the instance secret for you and provide its details, which you can then reference in the Depot.
</aside>

### **Step 2: Create a Depot manifest file**

Now link your secret to a Depot that defines the database connection.

**Depot manifest**

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
---

### **Step 3: Applying the Depot manifest**

Apply the Depot manifest using the following command:

```bash
dataos-ctl resource apply -f <filename with path>
```
---

### **Step 4: Verify the Connection**

Run this to confirm the Depot is live and connected:

```bash
dataos-ctl get -t depot
```

This command displays the details of the configured Depot, confirming that it is active and properly connected to the PostgreSQL database.

---

<aside>
Ensure that the name of your Instance secret is ${depot-name}-${acl}. For instance, if your Depot name is postgres and the acl(access control list) is rw, then the instance secret name will be postgres-rw.
</aside>

To simplify the creation of depots for commonly used data sources, a set of pre-defined manifest [templates](/resources/depot/#templates-of-depot-for-different-source-systems) is available. These templates provide a quick starting point for setting up depots for popular data sources.

To use these templates, you must fill in the key-value properties in the manifest file with the specific details of your data source. The required values will vary depending on the data source. A basic understanding of your organization's data infrastructure, as well as the necessary credentials or connection details, is essential for configuring these templates effectively.

Similarly you can create a Depot for Azure using Instance-secret:
??? "Click to see Azure Depot manifest"

    ```yaml
    name: thirdparty
    version: v1
    type: depot
    tags:
      - dataos:type:resource
      - dataos:type:cluster-resource
      - dataos:resource:depot
      - dataos:layer:user
    description: Default Third Party Depot for new
    owner: {{owner}}
    layer: user
    depot:
      name: thirdparty
      type: ABFSS
      owner: 
      description: Default Third Party Depot for new
      secrets:
            - name: thirdparty-rw
              keys:
              - thirdparty-rw
            - name: thirdparty-r
              keys:
              - thirdparty-r
      external: true
      compute: query-default
      resources:
        requests:
          cpu: 100m
          memory: 550Mi
        limits:
          cpu: 1000m
          memory: 1500Mi
      spec:
        account: mockdataos
        container: dropzone001
        relativePath: large_dataset_20200511
      source: thirdparty
    ```

---

## FAQs

**Q1: What are the naming conventions for Instance-secrets and Depots?**

**In Instance-secret names:**

- Only lowercase letters (`a-z`), digits (`0-9`), and hyphens/dashes () are allowed.
- Hyphens/dashes cannot be at the start or end of the string.
- No uppercase letters or additional special characters are allowed.

**In Depot names:**

- Only lowercase letters (`a-z`) and digits (`0-9`) are allowed.
- Hyphens/dashes and other special characters are not allowed.

**Q2: Are usernames/passwords visible in Depot files?**

No, usernames and passwords can be securely stored using instance secrets or referenced through a JSON file path in the Depot manifest, keeping credentials hidden.

Alternatively, you can use environment variables like SNOWFLAKE_USERNAME and SNOWFLAKE_PASSWORD. Define these variables in the shell using export and reference them in the manifest file as $VARIABLE_NAME.

DataOS securely interpolates these values during execution, ensuring sensitive information remains secure and isn’t exposed in code or repositories.

**Q3: Can users see everyone’s Depots or only their own?** 

By default, users with **data-dev** or **operator** roles can view all depots. Access can be restricted by removing the **Manage All Depot** use-case or applying policies to block the depot listing endpoint.  

**Check your Depots:**

```bash
dataos-ctl get -t depot
```

**View all Depots (with permissions):**

```bash
dataos-ctl get -t depot -a
```

Depot details can also be explored via the Metis UI in DataOS.

---

## Additional learning resources

Explore the following resources to enhance your understanding of data source connections:

- [Depot Resource Documentation](https://dataos.info/resources/depot/)
- [Instance Secret Resource Documentation](https://dataos.info/resources/instance_secret)
- [Quick Guide: Depot Creation with DataOS CLI](/quick_guides/depot_creation_cli/)

With this knowledge, you are now equipped to connect DataOS to a wide variety of data sources.

---

## Next step

Now that your depot is connected, the next step is to scan metadata from the data source using a Scanner Workflow.

👉 Refer to the next topic: [Create a Scanner Workflow](/learn/dp_foundations1_learn_track/create_scanner/)