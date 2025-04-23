# Scanner for MariaDB

MariaDB metadata Scanner Workflow can be configured and scheduled through the DataOS CLI. Ensure that all prerequisites are met before initiating the workflow.

## Prerequisites

- **Metadata Access Requirements**:  
    - To extract metadata, the MariaDB user must have access to the `INFORMATION_SCHEMA`.  
    - By default, a user can only view rows in `INFORMATION_SCHEMA` that correspond to objects for which they have access privileges.

- **Access Permissions in DataOS**:  
  To execute a Scanner Workflow in DataOS, verify that at least one of the following role tags is assigned:

    - `roles:id:data-dev`
    - `roles:id:system-dev`
    - `roles:id:user`

    Use the following command to check assigned roles:

    ```bash
    dataos-ctl user get
    ```

    If any required tags are missing, contact a **DataOS Operator** or submit a **Grant Request** for role assignment.

    Alternatively, if access is managed through **use cases**, ensure the following use cases are assigned:

    - **Read Workspace**
    - **Run as Scanner User**
    - **Manage All Depot**
    - **Read All Dataset**
    - **Read All Secrets from Heimdall**

    To validate assigned use cases, refer to the [**Bifrost Application Use Cases**](/interfaces/bifrost/ "Bifrost is a Graphical User Interface (GUI) that empowers users to effortlessly create and manage access policies for applications, services, people, and datasets. Bifrost leverages the governance engine of DataOS, Heimdall, to ensure secure and compliant data access through ABAC policies, giving users fine-grained control over the data and resources.") section.

- **Depot Verification**: Ensure a JDBC-type Depot is created via the Metis UI or using the CLI:

    ```bash
    dataos-ctl get -t depot -a
    ```

    ```bash
    # expected output

    INFO[0000] 🔍 get...
    INFO[0000] 🔍 get...complete

    | NAME             | VERSION | TYPE  | WORKSPACE | STATUS | RUNTIME | OWNER      |
    | ---------------- | ------- | ----- | --------- | ------ | ------- | ---------- |
    | mongodepot       | v2alpha | depot |           | active |         | usertest   |
    | snowflakedepot   | v2alpha | depot |           | active |         | gojo       |
    | redshiftdepot    | v2alpha | depot |           | active |         | kira       |
    | mysqldepot       | v2alpha | depot |           | active |         | ryuk       |
    | oracle01         | v2alpha | depot |           | active |         | drdoom     |
    | mariadb01        | v2alpha | depot |           | active |         | tonystark  |
    | demopreppostgres | v2alpha | depot |           | active |         | slimshaddy |
    | demoprepbq       | v2alpha | depot |           | active |         | pengvin    |
    | mssql01          | v2alpha | depot |           | active |         | hulk       |
    | kafka01          | v2alpha | depot |           | active |         | peeter     |
    | icebase          | v2alpha | depot |           | active |         | blackpink  |
    | azuresql         | v2alpha | depot |           | active |         | arnold     |
    | fastbase         | v2alpha | depot |           | active |         | ddevil     |
    ```

    If the desired depot is not present, create it using the following manifest:

    ```yaml
    name: ${{depot-name}} # examples: mariadb01, mariadepot, etc.
    version: v2alpha
    type: depot
    tags:
      - ${{tag1}}
    owner: ${{owner-name}}
    layer: user
    depot:
      type: JDBC
      description: ${{description}}
      external: ${{true}}
      secrets:
        - name: ${{sf-instance-secret-name}}-r
          allkeys: true
        - name: ${{sf-instance-secret-name}}-rw
          allkeys: true
      jdbc:
        subprotocol: ${{subprotocol}}
        host: ${{host}}
        port: ${{port}}
        database: ${{database-name}}
        params:
          ${{"key1": "value1"}}
          ${{"key2": "value2"}}
    ```

## Scanner Workflow for MariaDB

DataOS helps to connect to a database with JDBC driver to read data from tables using Depot. The Depot enables access to all schemas visible to the specified user in the configured database, MariaDB.

```yaml
version: v1
name: mariadb-scanner2
type: workflow
tags: 
  - mariadb-scanner2.0
description: The job scans schema tables and register metadata
workflow: 
  dag: 
    - name: scanner2-mariadb
      description: The job scans schema from mariadb depot tables and register metadata to metis2
      spec: 
        stack: scanner:2.0
        compute: runnable-default
        runAsUser: metis
        stackSpec: 
          depot: mariadb01
          # sourceConfig:
          #   config:
          #     schemaFilterPattern:      # use schemas and table filters to get specefic metadata from the data source
          #       includes:
          #         - mariadb     
```

The above sample manifest file is deployed using the following command:

```bash
dataos-ctl resource apply -f ${{path to the Scanner YAML}}
```

**Updating the Scanner Workflow**:

If the Depot or Scanner configurations are updated, the Scanner must be redeployed after deleting the previous instance. Use the following command to delete the existing Scanner:

```bash 
  dataos-ctl delete -f ${{path-to-Scanner-YAML}}]
```

**OR**

```bash
  dataos-ctl delete -t workflow -n ${{name of Scanner}} -w ${{name of workspace}}
```


!!! info "**Best Practice**"

    As part of best practices, it is recommended to regularly delete Resources that are no longer in use. This practice offers several benefits, including saving time and reducing costs.