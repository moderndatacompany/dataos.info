# How to configure a Scanner ?

## Manifest file attributes in Scanner Workflows

The manifest file within a Scanner stack includes attributes designed to facilitate metadata extraction. These attributes specify source configurations, apply filtering criteria, and manage metadata control. Key functionalities include:

- **Source configuration**: Defines the connection details and parameters for the data source.

- **Filtering**: Enables metadata extraction to be limited to specific databases, schemas, tables, or topics.

- **Metadata Control**: Manages the extraction process by identifying and flagging deleted tables and topics.

**Syntax for Manifest configuration file:**

```yaml

name: ${{scanner2-snowflake-depot}}
version: v1
type: workflow
tags: 
  - ${{tag1}}
  - ${{tag}}
description: ${{The description of the scanner}}
workflow: 
  dag: 
    - name: ${{scanner2-snowflake-job}}
      description: ${{The job description}}
      tags: 
          - ${{tag}}
      spec: 
        stack: scanner:2.0               
        compute: runnable-default        
        runAsUser: metis                 
        stackSpec: 
          depot: dataos://${{path of the depot}}  #UDL(Uniform Data Link)             
          sourceConfig: 
            config: 
              type: DatabaseMetadata         
              databaseFilterPattern: 
                includes: 
                  - ${{regex}}
                excludes: 
                  - ${{regex}}
              schemaFilterPattern: 
                includes: 
                  - ${{regex}}
                excludes: 
                  - ${{regex}}
              tableFilterPattern: 
                includes: 
                  - ${{regex}}
                excludes: 
                  - ${{regex}}
                markDeletedTables: false   
                includeTags: true
                includeViews: true
```

## Scanner Configuration Attributes details

The Scanner Workflow attributes given below provide further details on their roles in metadata extraction:

### **`schedule`**

**Description**: Scanner Workflows are either single-time run or scheduled to run at a specific cadence.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | --------------- | ----------------- | ------------------ |
| string        | optional        | None              | None               |

**Example Usage:**

```yaml
workflow: 
  title: scheduled Scanner Workflow
  schedule:  
    cron: '*/2 * * * *'  #every 2 minute  [Minute, Hour, day of the month ,month, dayoftheweek]
    concurrencyPolicy: Allow #forbid/replace
    endOn: 2024-11-01T23:40:45Z
    timezone: Asia/Kolkata
```

To schedule a Workflow, user must add the schedule property defining a cron in `workflow` section.

### **`spec`**

**Description**: Specs of the Scanner Workflow

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | --------------- | ----------------- | ------------------ |
| mapping       | Mandatory       |                   |                    |

**Example Usage:**

```yaml
spec:
  stack: scanner:2.0
```

### **`stack`**

**Description:** A Stack is a Resource that serves as a secondary extension point, enhancing the capabilities of a Workflow Resource by introducing additional programming paradigms.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value**          |
| ------------- | --------------- | ----------------- | --------------------------- |
| string        | Mandatory       | None              | flare/toolbox/scanner/alpha |

**Additional Details:** You also need to specify specific versions of the stack. If no version is explicitly specified, the system will automatically select the latest version as the default option

**Example Usage:**

```yaml
stack: scanner:2.0
```

### **`compute`**

**Description:** A Compute resource provides processing power for the job.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value**                                               |
| ------------- | --------------- | ----------------- | ---------------------------------------------------------------- |
| string        | Mandatory       | None              | runnable-default or any other custom compute created by the user |

**Example Usage:**

```yaml
compute: runnable-default
```

### **`runAsUser`**

**Description:** When the "runAsUser" field is configured with the UserID of the use-case assignee, it grants the authority to perform operations on behalf of that user.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value**              |
| ------------- | --------------- | ----------------- | ------------------------------- |
| string        | Mandatory       | None              | UserID of the Use Case Assignee |

**Additional information**: The default value here is `metis`. but 'Run as a Scanner user' use case should be granted to run Scanner Workflow. **Example Usage:**

`runAsUser: metis`

### **`depot`**

**Description**: Name or address of the Depot. Depot provides a reference to the source from which metadata is read/ingested.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value**                               |
| ------------- | --------------- | ----------------- | ------------------------------------------------ |
| string        | Mandatory       | None              | icebase, redshift\_depot, dataos://icebase, etc. |

**Additional information**: The Scanner job will scan all the datasets referred by a Depot. Scanner Workflow will automatically create a source (with the same name as the Depot name) where the scanned metadata is saved within Metastore.

**Example Usage**:

```yaml
stackSpec:    
  depot: dataos://icebase
```

### **`type`**

**Description**: Type of the dataset to be scanned. This depends on the underlying data source.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value**                  |
| ------------- | --------------- | ----------------- | ----------------------------------- |
| string        | Mandatory       | None              | snowflake, bigquery, redshift, etc. |

**Example Usage**:

```yaml
stackSpec:  
  type: snowflake
```

### **`sourceConnection`**

**Description**: Source connection configuration properties required to connect with the underlying data source to be scanned.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| ------------- | --------------- | ----------------- | ------------------- |
| mapping       | optional        | None              | None                |

### **`type`**

**Description**: Data source type in the sourceConnection section.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values**                 |
| ------------- | --------------- | ----------------- | ----------------------------------- |
| string        | optional        | None              | Redshift, Snowflake, Bigquery, etc. |

**Example Usage**:

```yaml
sourceConnection: 
  config: 
    type: Snowflake
```

### **`sourceConfig`**

**Description**: Source configuration properties required to control the metadata scan.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| ------------- | --------------- | ----------------- | ------------------- |
| mapping       | Mandatory       | None              | None                |

### **`type`**

**Description**: Specify source config type; This is for type of metadata to be scanned.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values**                 |
| ------------- | --------------- | ----------------- | ----------------------------------- |
| string        | optional        | None              | DatabaseMetadata, DashboardMetadata |

**Additional information**: There will be more properties under the 'sourceConfig' section to customize and control metadata scanning.

**Example Usage**:

```yaml
sourceConfig: 
  config: 
    type: DatabaseMetadata
```

### **`databaseFilterPattern`**

**Description**: To determine which databases to include/exclude during metadata ingestion.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| ------------- | --------------- | ----------------- | ------------------- |
| mapping       | Mandatory       | None              |                     |

**Additional information**: Applicable in case of databases/warehouses

**`includes OR excludes`**

- `includes:` Add an array of regular expressions to this property in the YAML. The Scanner Workflow will include any databases whose names match one or more of the provided regular expressions. All other databases will be excluded.

- `excludes:` Add an array of regular expressions to this property in the YAML. The Scanner Workflow will exclude any databases whose names match one or more of the provided regular expressions. All other databases will be included.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values**                                                      |
| ------------- | --------------- | ----------------- | ------------------------------------------------------------------------ |
| string        | Optional        | None              | Exact values (e.g., 'employee'), regular expressions (e.g., '^sales.\*') |

**Example Usage**:

```yaml
sourceConfig:  
  config:  
    type: DatabaseMetadata
    databaseFilterPattern:
      includes: 
        - TMDCSNOWFLAKEDB
```

### **`schemaFilterPattern`**

**Description**: To determine which schemas to include/exclude during metadata ingestion.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| ------------- | --------------- | ----------------- | ------------------- |
| mapping       | Mandatory       | None              |                     |

**Additional information**: Applicable in case of databases/warehouses

**`includes OR excludes`**

- `includes:` Add an array of regular expressions to this property in the YAML. The Scanner Workflow will include any schemas whose names match one or more of the provided regular expressions. All other schemas will be excluded.

- `excludes:` Add an array of regular expressions to this property in the YAML. The Scanner Workflow will exclude any schemas whose names match one or more of the provided regular expressions. All other schemas will be included.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values**                                                      |
| ------------- | --------------- | ----------------- | ------------------------------------------------------------------------ |
| string        | Optional        | None              | Exact values (e.g., 'employee'), regular expressions (e.g., '^sales.\*') |

**Example Usage**:

```yaml
sourceConfig: 
  config: 
    schemaFilterPattern: 
      excludes: 
        - mysql.*
        - information_schema.*
        - ^sys.*
```

**Additional information**: Applicable in case of databases/warehouses

### **`tableFilterPattern`**

**Description**: To determine which tables to include/exclude during metadata ingestion.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values**                                                      |
| ------------- | --------------- | ----------------- | ------------------------------------------------------------------------ |
| mapping       | Mandatory       | None              | Exact values (e.g., 'employee'), regular expressions (e.g., '^sales.\*') |

**Additional information**: Applicable in case of databases/warehouses

**`includes OR excludes`**

- `includes:` Add an array of regular expressions to this property in the YAML to include any tables whose names match one or more of the provided regular expressions. All other tables will be excluded.

- `excludes:` Add an array of regular expressions to this property in the YAML. The Scanner Workflow will exclude any tables whose names match one or more of the provided regular expressions. All other tables will be included.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values**                                                      |
| ------------- | --------------- | ----------------- | ------------------------------------------------------------------------ |
| string        | Optional        | None              | Exact values (e.g., 'employee'), regular expressions (e.g., '^sales.\*') |

**Example Usage**:

```yaml
sourceConfig: 
  config: 
    tableFilterPattern: 
      includes: 
        - ^cust.*
```

**Additional information**: Applicable in case of databases/warehouses.

### **`topicFilterPattern`**

**Description**: To determine which topics to include/exclude during metadata ingestion.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| ------------- | --------------- | ----------------- | ------------------- |
| mapping       | Mandatory       | none              |                     |

**Additional information**: Applicable in case of stream data.

**`includes OR excludes`**

- `includes:` Add an array of regular expressions to this property in the YAML to include any topics whose names match one or more of the provided regular expressions. All other topics will be excluded.

- `excludes:` Add an array of regular expressions to this property in the YAML to exclude any topics whose names match one or more of the provided regular expressions. All other topics will be included.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values**                                                      |
| ------------- | --------------- | ----------------- | ------------------------------------------------------------------------ |
| string        | Optional        | None              | Exact values (e.g., 'employee'), regular expressions (e.g., '^sales.\*') |

**Example Usage**:

```yaml
sourceConfig: 
  config: 
    topicFilterPattern: 
      includes: 
        - ^topic00.*
```

!!! info

    Filter patterns support Regex in includes and excludes expressions.


### **`markDeletedTables`**

**Description**: Set the Mark Deleted Tables property to true to flag tables as soft-deleted if they are not present anymore in the source system.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| ------------- | --------------- | ----------------- | ------------------- |
| boolean       | Optional        | false             | true, false         |

**Additional information**: If a dataset is deleted from the source and hasn't been ingested in Metis during a previous Scanner run, there will be no visible change in the scanned metadata on the Metis UI. However, if the deleted dataset has already been ingested in MetisDB from previous Scanner runs, users can run a Scanner Workflow for the specific Depot they want to scan with the **`markDeletedTables: true`** option in the Workflow configuration. After a successful run, users can check the Metis UI to see the tables that have been marked as deleted.

**Example Usage**:

```yaml
sourceConfig: 
  config: 
    markDeletedTables: false
```

### **`markDeletedTablesfromFilterOnly`**

**Description**: Set the Mark Deleted Tables property to true to flag tables as soft-deleted if they are not present anymore in the source system.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| ------------- | --------------- | ----------------- | ------------------- |
| boolean       | Optional        | false             | true, false         |

**Additional information**: Set this property to true to flag tables as soft-deleted if they are not present anymore within the filtered schema or database only. This flag is useful when you have more than one ingestion pipelines.

**Example Usage**:

```yaml
sourceConfig: 
  config: 
    markDeletedTablesfromFilterOnly: false
```

### **`ingestSampleData`**

**Description**: Set this property to true to ingest sample data from the topics.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| ------------- | --------------- | ----------------- | ------------------- |
| boolean       | Optional        | false             | true, false         |

**Additional information**: Set this property to true to flag tables as soft-deleted if they are not present anymore within the filtered schema or database only. This flag is useful when you have more than one ingestion pipelines.

**Example Usage**:

```yaml
sourceConfig: 
  config: 
    ingestSampleData: false
```

### **`markDeletedTopics`**

**Description**: Set this property to true to flag topics as soft-deleted if they are not present anymore in the source system.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| ------------- | --------------- | ----------------- | ------------------- |
| boolean       | Optional        | false             | true, false         |

**Additional information**: Set this property to true to flag tables as soft-deleted if they are not present anymore within the filtered schema or database only. This flag is useful when you have more than one ingestion pipelines.

**Example Usage**:

```yaml
sourceConfig: 
  config: 
    markDeletedTables: false
```

### **`includeViews`**

**Description**: Set this property to include views for metadata scanning.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| ------------- | --------------- | ----------------- | ------------------- |
| boolean       | Optional        | false             | true, false         |

**Additional information**: Set this property to true to flag tables as soft-deleted if they are not present anymore within the filtered schema or database only. This flag is useful when you have more than one ingestion pipelines.

**Example Usage**:

```yaml
sourceConfig: 
  config: 
    includeViews: true
```

### **`enableDebugLog`**

**Description**: To set the default log level to debug.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| ------------- | --------------- | ----------------- | ------------------- |
| boolean       | Optional        | false             | true, false         |

**Example Usage**:

```yaml
sourceConfig: 
  config: 
    enableDebugLog: true
```