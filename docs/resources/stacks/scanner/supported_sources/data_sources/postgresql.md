# Scanner for PostgreSQL

PostgreSQL metadata Scanner Workflow can be configured and scheduled through the DataOS CLI. Ensure that all prerequisites are met before initiating the workflow.


## Prerequisites

- The user should have both `CONNECT` and `SELECT` privileges on the database.

- Check whether PostgreSQL Depot is already created. To check the Depot go to the Metis UI of the DataOS or use the following command:

    ```bash
    dataos-ctl get -t depot -a
    ```

    ```bash
    #expected output

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

  - If the PostgreSQL Depot is not created, create a Depot using the PostgreSQL Depot Template given below:

    ```yaml
    name: ${{postgresdb}}
    version: v2alpha
    type: depot
    layer: user
    depot:
      type: JDBC                  
      description: ${{To write data to postgresql database}}
      external: ${{true}}
      secrets:
        - name: ${{sf-instance-secret-name}}-r
          allkeys: true
        - name: ${{sf-instance-secret-name}}-rw
          allkeys: true
      postgresql:                        
        subprotocol: "postgresql"
        host: ${{host}}
        port: ${{port}}
        database: ${{postgres}}
        params: 
          sslmode: ${{disable}}
    ```

- **Access Permissions in DataOS**: To execute a Scanner Workflow in DataOS, verify that at least one of the following role tags is assigned:

    * `roles:id:data-dev`  
    * `roles:id:system-dev`  
    * `roles:id:user`  

    Use the following command to check assigned roles:

    ```bash
    dataos-ctl user get
    ```

    If any required tags are missing, contact a **DataOS Operator** or submit a **Grant Request** for role assignment.

    Alternatively, if access is managed through **use cases**, ensure the following use cases are assigned:

    * **Read Workspace**  
    * **Run as Scanner User**  
    * **Manage All Depot**  
    * **Read All Dataset**  
    * **Read All Secrets from Heimdall**

    To validate assigned use cases, refer to the [**Bifrost Application Use Cases**](/interfaces/bifrost/ "Bifrost is a Graphical User Interface (GUI) that empowers users to effortlessly create and manage access policies for applications, services, people, and datasets. Bifrost leverages the governance engine of DataOS, Heimdall, to ensure secure and compliant data access through ABAC policies, giving users fine-grained control over the data and resources.") section.

## Scanner Workflow for PostgreSQL

DataOS facilitates database connections via a JDBC driver for reading data from tables using Depot. Additionally, metadata can be scanned from a POSTGRES-type depot through Scanner Workflows. The Depot provides access to all schemas that are visible to the specified user within the configured PostGRES database.


```yaml
version: v1
name: demopreppostgres-scanner2
type: workflow
tags:
  - demopreppostgres-scanner2.0
description: The job scans schema tables and register metadata
workflow:
  dag:
    - name: scanner2-demopreppostgres
      description: The job scans schema from demopreppostgres depot tables and register metadata to metis2
      spec:
        stack: scanner:2.0
        compute: runnable-default
        runAsUser: metis
        stackSpec:
          depot: dataos://demopreppostgres          # Postgres depot name or UDL
          # sourceConfig:
          #   config:
          #     schemaFilterPattern:
          #       includes:
          #         - Public
          #     tableFilterPattern:
          #       includes:
          #         - F_delivery
          
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