# Scanner for Redshift

Redshift metadata Scanner Workflow can be configured and scheduled through the DataOS CLI. Ensure that all prerequisites are met before initiating the workflow.



## Prerequisites

To scan metadata from a Redshift data source, prerequisites are as follows:

1. Credentials to connect to Redshift database.
2. `SVV_TABLE_INFO` View contains summary information for tables in the Redshift database and is visible only to superusers. The permissions to query the view are needed while scanning metadata from Scanner Workflow.
3. Redshift user must grant `SELECT` privilege on table [SVV_TABLE_INFO](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_TABLE_INFO.html) to fetch the metadata of tables and views.
4. Access Permissions in DataOS: To execute a Scanner Workflow in DataOS, verify that at least one of the following role tags is assigned:
    
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
    
    To validate assigned use cases, refer to the **Bifrost Application Use Cases** section.

5. Pre-created Redshift Depot. To check the Depot go to the Metis UI of the DataOS or use the following command:
    
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

- If the Redshift Depot is not created, create a Depot using the following Depot Template:

    ```yaml
    name: ${{redshift-depot-name}}
    version: v2alpha
    type: depot
    tags:
      - ${{redshift}}
    layer: user
    description: ${{Redshift Sample data}}
    depot:
      type: REDSHIFT
      redshift:
        host: ${{hostname}}
        subprotocol: ${{subprotocol}}
        port: ${{5439}}
        database: ${{sample-database}}
        bucket: ${{tmdc-dataos}}
        relativePath: ${{development/redshift/data_02/}}
      external: ${{true}}
      secrets:
        - name: ${{redshift-instance-secret-name}}-r
          allkeys: true
    
        - name: ${{redshift-instance-secret-name}}-rw
          allkeys: true
    ```
  
  The Depot enables access to all schemas visible to the specified user in the configured database, REDSHIFT.

### Scanner Workflow for Redshift

The manifest configuration for the Redshift are as follows: 

```yaml
version: v1
name: redshift-scanner2
type: workflow
tags:
  - redshift-scanner2.0
description: The workflow scans schema tables and register metadata
workflow:
  dag:
    - name: scanner2-redshift
      description: The job scans schema from redshift depot tables and register metadata to metis2
      spec:
        stack: scanner:2.0
        compute: runnable-default
        runAsUser: metis
        stackSpec:
          depot: demoprepredshift
          sourceConfig:
            config:
              markDeletedTables: false
              includeTables: true
              includeViews: false
              schemaFilterPattern:
                includes:
                  - ^Public$
              tableFilterPattern:
                includes:
                  - ^Customer.*
```

Once the credentials of the sample file is given by the user and save with the .yam/.yml extension it can be deployed to extract the meta data by using the following command:

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