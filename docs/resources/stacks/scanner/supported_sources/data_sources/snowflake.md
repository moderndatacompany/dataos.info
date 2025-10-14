# Scanner for Snowflake

Snowflake metadata Scanner Workflow can be configured and scheduled through the DataOS CLI. Ensure that all prerequisites are met before initiating the workflow.



## Prerequisites

1. To ingest basic metadata, Snowflake user must have at least `USAGE` privileges on required schemas.
2. While running the usage Workflow, Metis fetches the query logs by querying `snowflake.account_usage.query_history` table. For this, the Snowflake user should be granted the `ACCOUNTADMIN` role (or a role granted IMPORTED PRIVILEGES on the database).
3. If ingesting tags, the user should also have permissions to query `snowflake.account_usage.tag_references`. For this, the Snowflake user should be granted the `ACCOUNTADMIN` role (or a role granted IMPORTED PRIVILEGES on the database).
4. If during the ingestion the user wants to set the session tags, then the user should have `ALTER SESSION` permissions.
5. Ensure that a Snowflake Depot is already created with valid read access and the necessary permissions to extract metadata. To check the Depot, go to the Metis UI of the DataOS or use the following command:

    ```bash
    dataos-ctl get -t depot -a
    ```

    ```bash
    #expected output
    
    INFO[0000] 🔍 get...
    INFO[0000] 🔍 get...complete
    
    | NAME             | VERSION | TYPE  | WORKSPACE | STATUS | RUNTIME | OWNER      |
    | ---------------- | ------- | ----- | --------- | ------ | ------- | ---------- |
    | snowfdepot       | v2alpha | depot |           | active |         | usertest   |

    ```

- If the Snowflake Depot is not created, create a Depot using the Snowflake Depot Template:

    ```yaml
    name: ${{snowflake-depot}}
    version: v2alpha
    type: depot
    tags:
      - ${{tag1}}
      - ${{tag2}}
    layer: user
    depot:
      type: snowflake
      description: ${{snowflake-depot-description}}
      snowflake:
        warehouse: ${{warehouse-name}}
        url: ${{snowflake-url}}
        database: ${{database-name}}
      external: true
      secrets:
        - name: ${{redshift-instance-secret-name}}-r
          allkeys: true
    
        - name: ${{redshift-instance-secret-name}}-rw
          allkeys: true
    ```

6. **Access Permissions in DataOS**:  
    To execute a Scanner Workflow in DataOS, verify that at least one of the following role tags is assigned:

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
    
    To validate assigned use cases Contact DataOS Operator, and to know more refer to the [**Bifrost Application Use Cases**](/interfaces/bifrost/ "Bifrost is a Graphical User Interface (GUI) that empowers users to effortlessly create and manage access policies for applications, services, people, and datasets. Bifrost leverages the governance engine of DataOS, Heimdall, to ensure secure and compliant data access through ABAC policies, giving users fine-grained control over the data and resources.") section.

## Scanner Workflow for Snowflake

Sample manifest configuration file for the Snowflake are as follows: 

```yaml
version: v1                                            
name: snowflake03-scanner2                              
type: workflow
tags:
  - snowflake03-scanner2.0
description: The job scans schema of tables and register their metadata
workflow:
  dag:
    - name: scanner2-snowflake03                        
      description: The job scans schema from snowflake03 depot tables and register their metadata on metis2
      spec:
        stack: scanner:2.0                              
        compute: runnable-default 
        runAsUser: metis                      
        stackSpec:
          depot: dataos://snowfdepot       # Depot name or address UDL
          sourceConfig:
            config:
          #     schemaFilterPattern:
          #       includes:
          #         - Public
          #     tableFilterPattern: 
          #       includes:
          #         - department
          #         - ^EMPLOYEE
              markDeletedTables: false
              includeTables: true
              includeViews: true
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