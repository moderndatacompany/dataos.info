# Scanner for Oracle


Oracle metadata Scanner Workflow can be configured and scheduled through the DataOS CLI. Ensure that all prerequisites are met before initiating the workflow. 

## Prerequisites

- **Metadata Access Requirements**: The Oracle user must have `CREATE SESSION` privilege.

- **Supported Versions**: Metadata Scan is supported for Oracle versions **12c, 18c, 19c, and 21c**.

- **Depot Verification**: Ensure an Oracle Depot is already created. To verify, use the Metis UI in DataOS or run the following command:

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

    If the Oracle Depot is not present, create one using the template below:

    ```yaml
    name: ${{depot-name}}
    version: v1
    type: depot
    tags:
      - ${{dropzone}}
      - ${{oracle}}
    layer: user
    depot:
      type: ORACLE                                    
      description: ${{"Oracle Sample data"}}
      spec:
        subprotocol: ${{subprotocol}}  # e.g., "oracle:thin"                                    
        host: ${{host}}
        port: ${{port}}
        service: ${{service}}
      external: ${{true}}
      secrets:
        - acl: r
          type: key-value-properties
          data:
            username: ${{username}}
            password: ${{password}}  
        - acl: rw
          type: key-value-properties
          data:
            username: ${{username}}
            password: ${{password}}
    ```

- **Access Permissions in DataOS**: To execute a Scanner Workflow in DataOS, ensure that at least one of the following role tags is assigned:

    * `roles:id:data-dev`  
    * `roles:id:system-dev`  
    * `roles:id:user`

    Run the following command to check assigned roles:

    ```bash
    dataos-ctl user get
    ```

    If required roles are missing, contact a **DataOS Operator** or submit a **Grant Request** for assignment.

    If access is managed via **use cases**, verify that the following use cases are assigned:

    * **Read Workspace**  
    * **Run as Scanner User**  
    * **Manage All Depot**  
    * **Read All Dataset**  
    * **Read All Secrets from Heimdall**

    Refer to the [**Bifrost Application Use Cases**](/interfaces/bifrost/ "Bifrost is a Graphical User Interface (GUI) that empowers users to effortlessly create and manage access policies for applications, services, people, and datasets. Bifrost leverages the governance engine of DataOS, Heimdall, to ensure secure and compliant data access through ABAC policies, giving users fine-grained control over the data and resources.") section to validate assigned use cases.

## Scanner Workflow for Oracle

An Oracle-type Depot enables access to all schemas visible to the specified user in the configured database.



```yaml
version: v1
name: oracle-scanner
type: workflow
tags:
  - oracle-scanner
description: The job scans schema tables and register metadata
workflow:
  dag:
    - name: oracle-scanner
      description: The job scans schema from oracle-scanner tables and register metadata to metis2
      spec:
        tags:
          - scanner
        stack: scanner:2.0
        compute: runnable-default
                runAsUser: metis
        stackSpec:
          depot: oracle01          #depo name/address
          sourceConfig:
            config:
              markDeletedTables: false
              includeTables: true
              includeViews: true
              databaseFilterPattern:
                  includes:
                      - database1
                      - database2
                    excludes:
                      - database3
                      - database4
                  schemaFilterPattern:
                    includes:
                      - schema1
                      - schema2
                    excludes:
                      - schema3
                      - schema4
                  tableFilterPattern:
                    includes:
                      - table1
                      - table2
                    excludes:
                      - table3
                      - table4
```

After the successful workflow run, user can check the metadata of scanned Tables on Metis UI for all schemas present in the database. The above sample manifest file is deployed using the following command:

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