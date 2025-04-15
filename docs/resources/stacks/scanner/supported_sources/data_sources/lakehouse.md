# Scanner for Lakehouse 


Lakehouse (ABFSS, WASBS, GCS, S3) metadata Scanner Workflow can be configured and scheduled through the DataOS CLI. Ensure that all prerequisites are met before initiating the workflow.


## Prerequisites

- To scan the ⁠Lakehouse (ABFSS, WASBS, GCS, S3) Depot, ensure that the depot is created and  have `read` access for the depot. To check the Depot go to the Metis UI of the DataOS or use the following command:

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

    If the Lakehouse (ABFSS, WASBS, GCS, S3) Depot is not created, create a Depot using the Lakehouse (ABFSS, WASBS, GCS, S3) Depot Template given below:

    ```yaml
    # sample manifest for S3
    version: v2alpha
    name: ${{name of the ⁠Lakehouse (ABFSS, WASBS, GCS, S3)}}
    type: depot
    tags: 
      - S3
    layer: user
    description: "AWS S3 Bucket for Data"
    depot: 
      type: S3
      compute: runnable-default
      s3: 
        bucket: ${{S3_BUCKET}}        
        relativePath: ${{S3_RELATIVE_PATH}}          
        format: ICEBERG
        scheme: s3a       
      external: true
      secrets: 
        - name: ${{icebase-s3-instance-secret-name}}-r
          allkeys: true

        - name: ${{icebase-s3-instance-secret-name}}-rw
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

## Scanner Workflow for Lakehouse (ABFSS, WASBS, GCS, S3)

Here is an example of manifest configuration to connect to the source and reach the Metis server to save the metadata in Metis DB. The Scanner Workflow can run with or without a filter pattern.

```yaml
version: v1
    name: ${{name of the scanner}}
    type: workflow
    tags:
      - ${{tag1}}
      - ${{tag1}}
    description: The workflow scans Icebase Depot
    workflow:
      dag:
        - name: ${{name of the job}}
          description: ${{description of the job}}
          spec:
            tags:
              - ${{tag}}
            stack: scanner:2.0
            compute: runnable-default
            stackSpec:
              depot: dataos://${{path to the depot}}
              sourceConfig: 
                config:
                  type: DatabaseMetadata
                  schemaFilterPattern:      # add appropriate include and exclude filter patterns
                    excludes:
                      - information_schema
                      - sys
                      - performance_schema
                      - innodb
```

After replacing the placeholders, the above sample manifest file is deployed using the following command:

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