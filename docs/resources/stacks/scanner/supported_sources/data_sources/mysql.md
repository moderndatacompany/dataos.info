# Scanner for MySQL

MySQL metadata Scanner Workflow can be configured and scheduled through the DataOS CLI. Ensure that all prerequisites are met before initiating the workflow.

## Prerequisites

- **Metadata Access Requirements**: The MySQL user must have access to the `INFORMATION_SCHEMA`.

- **Supported Versions**: Metadata Scan is supported only for MySQL version **8.0.0 or greater**.

- **Grant SELECT Privilege**: The MySQL user must be granted `SELECT` privileges to fetch metadata of tables and views.

- **Depot Verification**: Ensure a MySQL Depot is already created. To verify, use the Metis UI in DataOS or run the following command:

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

    If the MySQL Depot is not present, create one using the following template:

    ```yaml
    name: ${{mysqldepot}}
    version: v2alpha
    type: depot
    tags:
      - ${{dropzone}}
      - ${{mysql}}
    layer: user
    depot:
      type: MYSQL
      description: ${{"MYSQL Sample Database"}}
      mysql:
        subprotocol: "mysql"
        host: ${{host}}
        port: ${{port}}
        params:
          tls: ${{skip-verify}}
      external: ${{true}}
      secrets:
        - name: ${{sf-instance-secret-name}}-r
          allkeys: true
        - name: ${{sf-instance-secret-name}}-rw
          allkeys: true
    ```


- **Access Permissions in DataOS**: To execute a Scanner Workflow in DataOS, verify that at least one of the following role tags is assigned:

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


## Scanner Workflow for MySQL

With the use of the following sample manifest file, DataOS allows to  scan metadata from a MySQL-type Depot with the Scanner Workflows.


```yaml
version: v1
name: mysql-scanner
type: workflow
tags:
  - mysql-scanner
description: The workflow scans schema tables and registers metadata
workflow:
  dag:
    - name: mysql-scanner
      description: The job scans schema from MySQL depot tables and registers metadata to metis2
      spec:
        tags:
          - scanner
        stack: scanner:2.0
        compute: runnable-default
                runAsUser: metis
        stackSpec:
          depot: mysqldepot
          sourceConfig:
            config:
              markDeletedTables: false
              includeTables: true
              includeViews: true
              databaseFilterPattern:
                  includes:
                      - database1
                      - database2
                  schemaFilterPattern:
                    includes:
                      - schema1
                      - schema2
                  tableFilterPattern:
                    includes:
                      - table1
                      - table2
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