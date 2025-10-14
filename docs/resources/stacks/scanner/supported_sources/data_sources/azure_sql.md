# Scanner for AzureSQL


AzureSQL metadata Scanner Workflow can be configured and scheduled through the DataOS CLI. Ensure that all prerequisites are met before initiating the workflow.

## Prerequisites

1. **Whitelist IP address**: Ensure that the IP is whitelisted in AzureSQL firewall rules. Refer to the [Azure Portal documentation](https://learn.microsoft.com/en-us/azure/azure-sql/database/firewall-configure) for instructions on how to whitelist IP addresses.

2. **Grant SELECT Privilege**: The AzureSQL database user must be granted SELECT privileges to retrieve metadata from tables and views. Execute the following SQL commands to create a user and assign the required permissions:
  
    ```sql
    -- Create a login for the user (server-level)
    CREATE LOGIN Mary WITH PASSWORD = 'StrongPasswordHere';

    -- Create a user in the current database mapped to the login
    CREATE USER Mary FOR LOGIN Mary;

    -- Grant SELECT permission on a specific table
    GRANT SELECT ON dbo.YourTableName TO Mary;
    ```

3. **Pre-created AzureSQL Depot**: Ensure that an AzureSQL Depot is already created with valid read access and the necessary permissions to extract metadata.  
    To verify the existence of an AzureSQL Depot, use the Metis UI → Resources section in DataOS or execute the following command on DataOS CLI:

    ```bash
    dataos-ctl get -t depot -a
  
    # Expected output:
  
    INFO[0000] 🔍 get...
    INFO[0000] 🔍 get...complete

    | NAME             | VERSION | TYPE  | WORKSPACE | STATUS | RUNTIME | OWNER      |
    | ---------------- | ------- | ----- | --------- | ------ | ------- | ---------- |
    | azuresql       | v2alpha | depot |           | active |         | usertest   |

    ```

    If the AzureSQL Depot is not present in the list, create a new Depot using the template below:

    ```yaml
    name: ${{depot-name}}
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

    Ensure that all placeholders are replaced with appropriate values before deploying the configuration.

4. **Access Permissions in DataOS**

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

    To validate assigned use cases Contact DataOS Operator, and to know more refer to the [**Bifrost Application Use Cases**](/interfaces/bifrost/ "Bifrost is a Graphical User Interface (GUI) that empowers users to effortlessly create and manage access policies for applications, services, people, and datasets. Bifrost leverages the governance engine of DataOS, Heimdall, to ensure secure and compliant data access through ABAC policies, giving users fine-grained control over the data and resources.") section.

## Scanner Workflow for AzureSQL

DataOS enables connections to AzureSQL databases through Depot. The Depot provides access to all schemas visible to the specified user within the configured database. The Scanner Workflow scans schema tables and registers metadata in Metis DB. Below is a sample Scanner manifest file:

```yaml
version: v1
name: azuresql-scanner2
type: workflow
tags: 
  - azuresql-scanner2.0
description: Scanner workflow to scan schema tables and register metadata in Metis DB
workflow: 
  dag: 
    - name: scanner2-azuresql
      description: The job scans schema from azuresql depot tables and register metadata to metis2
      spec: 
        stack: scanner:2.0
        compute: runnable-default
        runAsUser: metis
        stackSpec: 
          depot: dataos://azuresql        #UDL
          sourceConfig:                  # Apply filter as per requirement
            config: 
              databaseFilterPattern: 
                includes: 
                  - <databasename>      # Provide proper database and table name
                excludes: 
                  - <databasename> 
              schemaFilterPattern: 
                includes: 
                  - <schemaname>
                excludes: 
                  - <schemaname>
              tableFilterPattern: 
                includes: 
                  - <tablename>
                excludes: 
                  - <tablename>
```

The above sample manifest file is deployed using the following command:

```bash
dataos-ctl resource apply -f ${{path to the Scanner YAML}}
```

**Updating the Scanner Workflow**:

If the Depot or Scanner configurations are updated, the Scanner must be redeployed after deleting the previous instance. Use the following command to delete the existing Scanner:


  ```bash 
  dataos-ctl delete -f ${{path-to-Scanner-YAML}}
  ```
**OR**
  ```bash
  dataos-ctl delete -t workflow -n ${{name of Scanner}} -w ${{name of workspace}}
  ```


!!! info "**Best Practice**"

    As part of best practices, it is recommended to regularly delete Resources that are no longer in use. This practice offers several benefits, including saving time and reducing costs.
