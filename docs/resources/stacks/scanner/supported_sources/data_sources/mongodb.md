# Scanner for MongoDB

MongoDB metadata Scanner Workflow can be configured and scheduled through the DataOS CLI. Ensure that all prerequisites are met before initiating the workflow.

## Prerequisites

- **Database Access Requirements**: The MongoDB user must have appropriate read privileges to access collections and metadata information.

- **Grant Read Privileges**: The MongoDB user must be granted read privileges to fetch metadata from collections and views.

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

    To validate assigned use cases Contact DataOS Operator, and to know more refer to the [**Bifrost Application Use Cases**](/interfaces/bifrost/ "Bifrost is a Graphical User Interface (GUI) that empowers users to effortlessly create and manage access policies for applications, services, people, and datasets. Bifrost leverages the governance engine of DataOS, Heimdall, to ensure secure and compliant data access through ABAC policies, giving users fine-grained control over the data and resources.") section.

- **Depot Verification**:  
    Ensure a MongoDB-type Depot is created using the Resources section in Metis UI or via CLI:

    ```bash
    dataos-ctl get -t depot -a

    # expected output

    INFO[0000] 🔍 get...
    INFO[0000] 🔍 get...complete

    | NAME             | VERSION | TYPE  | WORKSPACE | STATUS | RUNTIME | OWNER      |
    | ---------------- | ------- | ----- | --------- | ------ | ------- | ---------- |
    | mongodepot       | v2alpha | depot |           | active |         | usertest   |
    ```

    If the desired MongoDB depot is not present, create it using the following manifest:

    ```yaml
    name: ${{depot-name}}   # examples: mongodbdepot, mongodepot, mongodb01 etc.
    version: v2alpha
    type: depot
    tags:
      - ${{tag1}}
    owner: ${{owner-name}}
    layer: user
    depot:
      type: MONGODB
      description: ${{description}}
      external: ${{true}}
      secrets:
        - name: ${{mongodb-instance-secret-name}}-r
          allkeys: true
        - name: ${{mongodb-instance-secret-name}}-rw
          allkeys: true
      mongodb:
        subprotocol: ${{subprotocol}}   # mongodb or mongodb+srv
        nodes: ${{["host:port"]}}       # MongoDB cluster nodes
        params:                         # optional
          tls: ${{false}}               # set to true for TLS connections
    ```

## Scanner Workflow for MongoDB

DataOS allows to connect and scan metadata from a MongoDB-type Depot with Scanner workflows. The Depot enables access to all databases and collections visible to the specified user in the configured MongoDB instance.

```yaml
version: v1
name: ${{mongodb-scanner-name}}
type: workflow
tags:
  - depot
description: The workflow scans schema tables and register data
workflow:
  dag:
    - name: ${{dag-name}}
      description: The job scans schema from depot tables and register data to metis2
      spec:
        tags:
          - scanner
        stack: scanner:2.0
        compute: runnable-default
        runAsUser: metis
        stackSpec:
          depot: ${{mongodb-depot-name}}   # provide depot name or UDL
          sourceConfig:
            config:
              markDeletedTables: false
              includeCollections: true
              includeViews: true
              databaseFilterPattern:         # use valid name and regex to filter the data
                                             # Use Either include or exclude
                includes:
                  - database1
                  - database2
                excludes:
                  - database3
                  - database4
              collectionFilterPattern:
                includes:
                  - collection1
                  - collection2
                excludes:
                  - collection3
                  - collection4
```

After the successful Workflow run, user can check the metadata of scanned collections on Metis UI for all databases present in the MongoDB instance. The above sample manifest file is deployed using the following command:

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