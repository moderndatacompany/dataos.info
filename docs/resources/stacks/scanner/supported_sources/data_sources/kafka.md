# Scanner for Kafka

Kafka metadata Scanner Workflow can be configured and scheduled through the DataOS CLI. Ensure that all prerequisites are met before initiating the workflow.

## Prerequisites

To scan the KAFKA depot, ensure the following prerequisites need the following:

- Ensure that the depot is created and user have `read` access for the depot. Check the depot using Metis UI or use the following commands:

    ```bash
    dataos-ctl get -t depot -a

    # Expected output

    INFO[0000] 🔍 get...
    INFO[0000] 🔍 get...complete

    | NAME             | VERSION | TYPE  | WORKSPACE | STATUS | RUNTIME | OWNER      |
    | ---------------- | ------- | ----- | --------- | ------ | ------- | ---------- |
    | kafkadepot       | v2alpha | depot |           | active |         | usertest   |

    ```

    If the KAFKA Depot is not created, create it using the below manifest sample:

    ```yaml
    name: ${{depot-name}}
    version: v1
    type: depot
    tags:
      - ${{tag1}}
    owner: ${{owner-name}}
    layer: user
    depot:
      type: KAFKA                     
      description: ${{description}}
      external: ${{true}}
      spec:                           
        brokers:
          - ${{broker1}}
          - ${{broker2}}
        schemaRegistryUrl: ${{http://20.9.63.231:8081/}}
    ```

    To connect to Kafka, user needs a KAFKA broker list. Once the user provides the broker list, the Depot enables fetching all the topics in the KAFKA cluster.

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


## Scanner Workflow for Kafka

Here is an example of manifest configuration to connect to the source and reach the Metis server to save the metadata in Metis DB

```yaml
version: v1
name: kafka-scanner2
type: workflow
tags: 
  - kafka-scanner2.0
description: The job scans schema tables and register metadata
workflow: 
  dag: 
    - name: scanner2-kafka
      description: The job scans schema from kafka depot tables and register metadata to metis2
      spec:
        stack: scanner:2.0
        compute: runnable-default
        runAsUser: metis
        stackSpec: 
          depot: kafka01
          # sourceConfig:
          #   config:
          #     topicFilterPattern:
          #       includes:
          #         - Sanity
          #         - sampel_Json_Kafka
          #         - consumer_offsets
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