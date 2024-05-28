# Scanner YAML Fields Reference

## Syntax for Depot Scan YAML File

```yaml
stack: scanner:2.0               
compute: runnable-default        
runAsUser: metis                 
scanner:
depot: {{depot name/adddress}}             
sourceConfig:
config:
    type: DatabaseMetadata         
    databaseFilterPattern:
      includes/excludes:
        - {{regex}}
    schemaFilterPattern:
      includes/excludes:
        - {{regex}}
    tableFilterPattern:
      includes/excludes:
        - {{regex}}
    markDeletedTables: true/false
    includeViews: true/false
```
    
## Syntax for Non-Depot Scan YAML File
        
```yaml
stack: scanner:2.0               
compute: runnable-default        
runAsUser: metis
scanner:
type: {{source type}}                
source: {{source name}}              
sourceConnection:                    
  config:
    type: {{source connection type}}
    username: {{username}}
    password: {{password}}
    account: {{account}}
sourceConfig:                  
  config:
    type: {{metadata type}}         
    databaseFilterPattern:
      includes/excludes:
        - <regex>
    schemaFilterPattern:
      includes/excludes:
        - <regex>
    tableFilterPattern:
    includes/excludes:
        - <regex>
    markDeletedTables: true/false
    includeViews: true/false
```
    
## Configuration Attributes

### **`spec`**

**Description**: Specs of the Scanner workflow

| **Data Type**     | **Requirement** | **Default Value** | **Possible Value**                |
| ----------------- | --------------- | ----------------- | --------------------------------- |
| mapping           | Mandatory       |               |       |

<b>Example Usage:</b>
```yaml
spec:
  stack: scanner:2.0 
```

### **`stack`**
<b>Description:</b> A Stack is a Resource that serves as a secondary extension point, enhancing the capabilities of a Workflow Resource by introducing additional programming paradigms.  <br>

| **Data Type**     | **Requirement** | **Default Value** | **Possible Value**                |
| ----------------- | --------------- | ----------------- | --------------------------------- |
| string            | Mandatory       | None              | flare/toolbox/scanner/alpha      |


<b>Additional Details:</b> You also need to specify specific versions of the stack. If no version is explicitly specified, the system will automatically select the latest version as the default option <br>
<b>Example Usage:</b>
```yaml
stack: scanner:2.0 
```

### **`compute`**
<b>Description:</b> A Compute resource provides processing power for the job.  <br>

| **Data Type**     | **Requirement** | **Default Value**                | **Possible Value**                                    |
| ----------------- | --------------- | -----------------------------    | ----------------------------------------------------- |
| string            | Mandatory       | None                            | runnable-default or any other custom compute created by the user |


<b>Example Usage:</b>
```yaml
compute: runnable-default 
```
    
### **`runAsUser`**

<b>Description:</b> When the "runAsUser" field is configured with the UserID of the use-case assignee, it grants the authority to perform operations on behalf of that user. <br>

| **Data Type**     | **Requirement** | **Default Value**        | **Possible Value**                  |
| ----------------- | --------------- | -----------------------  | ----------------------------------- |
| string            | Mandatory       | None                      | UserID of the Use Case Assignee     |

<br>**Additional information**: The default value here is `metis`. but 'Run as a Scanner user' use case should be granted to run Scanner workflow.
<b>Example Usage:</b>
```yaml
runAsUser: metis 
```  
    
### **`depot`**

**Description**: Name or address of the depot. Depot provides a reference to the source from which metadata is read/ingested. <br>

| **Data Type**     | **Requirement**                                 | **Default Value** | **Possible Value**                                  |
| ----------------- | ----------------------------------------------- | ------------------ | --------------------------------------------------- |
| string            | Mandatory only in depot scan workflow | None               | icebase, redshift_depot, dataos://icebase, etc.     |

**Additional information**: The Scanner job will scan all the datasets referred by a depot. Scanner workflow will automatically create a source (with the same name as the depot name) where the scanned metadata is saved within Metastore. <br>
**Example Usage**:  
```yaml
scanner:   
  depot: dataos://icebase            
```

### **`type`**

**Description**: Type of the dataset to be scanned. This depends on the underlying data source. <br>

| **Data Type**     | **Requirement**                 | **Default Value** | **Possible Value**                   |
| ----------------- | ------------------------------- | ------------------ | ------------------------------------ |
| string            | Mandatory for non-depot scan workflow | None               | snowflake, bigquery, redshift, etc. |

<br> **Example Usage**: 
```yaml
scanner:
  type: snowflake
```
    
### **`source`**
**Description**: Here you need to explicitly provide the source name where the scanned metadata is saved within Metastore. <br>

| **Data Type**     | **Requirement**                 | **Default Value** | **Possible Value**                   |
| ----------------- | ------------------------------- | ------------------ | ------------------------------------ |
| string            | Mandatory for non-depot scan workflow | None               | snowflake001, samplexyz, etc.       |

**Additional information**: On Metis UI, sources are listed for databases, messaging, dashboards, workflows, ML models, etc. Under the given source name, you can see the information about all the entities scanned for a data source. <br>
**Example Usage**: 
```yaml
scanner:
  source: samplexyz 
```
<aside class="callout"> When the metadata source is not referenced by the depot, you need to provide the source connection details and credentials <b>explicitly</b>. </aside>

### **`sourceConnection`**
**Description**: Source connection configuration properties required to connect with the underlying data source to be scanned. <br>

| **Data Type**   | **Requirement**               | **Default Value** | **Possible Values** |
| ---------- | ----------------------------- | ------------------ | ------------------- |
| mapping    | Mandatory in non-depot scan  | None               | None                |


### **`type`**
**Description**: Data source type in the sourceConnection section. <br>

| **Data Type**   | **Requirement**               | **Default Value** | **Possible Values**                |
| ---------- | ----------------------------- | ------------------ | --------------------------------- |
| string     | Mandatory in non-depot scan  | None               | Redshift, Snowflake, Bigquery, etc.|

**Example Usage**: 
```yaml
sourceConnection:
  config:
    type: Snowflake
```


### **`username`**

**Description**: username to connect with the source <br>

| **Data Type**   | **Requirement**               | **Default Value** | **Possible Values**           |
| ---------- | ----------------------------- | ------------------ | ----------------------------- |
| string     | Mandatory in non-depot scan  | None               | testuser, testuser@bi.io      |

**Additional information**: There will be more properties under the 'sourceConnection' section to be able to connect with the source such as password, hostPort, project, email, etc.    <br>

**Example Usage**:
```yaml
sourceConnection:
  config:
    type: Snowflake   
    username: testuser
    password: ******
    warehouse: WAREHOUSE
    account: NB48718.central-india.azure
```  
<aside class="callout">The properties in the <b>sourceConnection</b> section depend on the underlying metadata source. </aside>   


### **`sourceConfig`**
**Description**: Source configuration properties required to control the metadata scan. <br>

| **Data Type**   | **Requirement**               | **Default Value** | **Possible Values** |
| ---------- | ----------------------------- | ------------------ | ------------------- |
| mapping    | Mandatory in non-depot scan  | None               | None                |


### **`type`**

**Description**: Specify source config type; This is for type of metadata to be scanned. <br>

| **Data Type**   | **Requirement**               | **Default Value** | **Possible Values**           |
| ---------- | ----------------------------- | ------------------ | ----------------------------- |
| string     | Mandatory in non-depot scan  | None               | DatabaseMetadata, DashboardMetadata |

**Additional information**: There will be more properties under the 'sourceConfig' section to customize and control metadata scanning. <br>
**Example Usage**:
```yaml
sourceConfig:
  config:
    type: DatabaseMetadata
```

### **`databaseFilterPattern`** 

**Description**: To determine which databases to include/exclude during metadata ingestion. <br>

| **Data Type**   | **Requirement**               | **Default Value** | **Possible Values**           |
| ---------- | ----------------------------- | ------------------ | ----------------------------- |
| mapping     | Mandatory   | None               |  |

<b>Additional information</b>: Applicable in case of databases/warehouses 

#### **`includes OR excludes`** 
- `includes:` Add an array of regular expressions to this property in the YAML. The Scanner workflow will include any databases whose names match one or more of the provided regular expressions. All other databases will be excluded.<br>
- `excludes`: Add an array of regular expressions to this property in the YAML. The Scanner workflow will exclude any databases whose names match one or more of the provided regular expressions. All other databases will be included. <br>

| **Data Type**   | **Requirement** | **Default Value** | **Possible Values**                               |
| ---------- | --------------- | ------------------ | ------------------------------------------------- |
| string     | Optional        | None               | Exact values (e.g., 'employee'), regular expressions (e.g., '^sales.*') |

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

**Description**: To determine which schemas to include/exclude during metadata ingestion. <br>

| **Data Type**   | **Requirement**               | **Default Value** | **Possible Values**           |
| ---------- | ----------------------------- | ------------------ | ----------------------------- |
| mapping     | Mandatory   | None               |  |

<b>Additional information</b>: Applicable in case of databases/warehouses 


#### **`includes OR excludes`** 

- `includes:` Add an array of regular expressions to this property in the YAML. The Scanner workflow will include any schemas whose names match one or more of the provided regular expressions. All other schemas will be excluded.<br>
- `excludes`: Add an array of regular expressions to this property in the YAML. The Scanner workflow will exclude any schemas whose names match one or more of the provided regular expressions. All other schemas will be included. <br>

| **Data Type**   | **Requirement** | **Default Value** | **Possible Values**                               |
| ---------- | --------------- | ------------------ | ------------------------------------------------- |
| string     | Optional        | None               | Exact values (e.g., 'employee'), regular expressions (e.g., '^sales.*') |


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

<b>Additional information</b>: Applicable in case of databases/warehouses <br>

### **`tableFilterPattern`** 

**Description**: To determine which tables to include/exclude during metadata ingestion.<br>

| **Data Type**   | **Requirement** | **Default Value** | **Possible Values**                               |
| ---------- | --------------- | ------------------ | ------------------------------------------------- |
| mapping     |    Mandatory    | None               | Exact values (e.g., 'employee'), regular expressions (e.g., '^sales.*') |

<b>Additional information</b>: Applicable in case of databases/warehouses<br>

#### **`includes OR excludes`**

- `includes:` Add an array of regular expressions to this property in the YAML to include any tables whose names match one or more of the provided regular expressions. All other tables will be excluded.<br>
- `excludes`: Add an array of regular expressions to this property in the YAML. The Scanner workflow will exclude any tables whose names match one or more of the provided regular expressions. All other tables will be included.<br>

| **Data Type**   | **Requirement** | **Default Value** | **Possible Values**                               |
| ---------- | --------------- | ------------------ | ------------------------------------------------- |
| string     | Optional        | None               | Exact values (e.g., 'employee'), regular expressions (e.g., '^sales.*') |

**Example Usage**:
```yaml
sourceConfig:
  config:
    tableFilterPattern:
      includes:
        - ^cust.*

```
<b>Additional information</b>: Applicable in case of databases/warehouses.

### **`topicFilterPattern`** 

**Description**: To determine which topics to include/exclude during metadata ingestion.<br>

| **Data Type**   | **Requirement** | **Default Value**  | **Possible Values**                               |
| ---------- | --------------- | ------------------ | ------------------------------------------------- |
| mapping     |    Mandatory    | none             |                                                   |

<b>Additional information</b>: Applicable in case of stream data.

#### **`includes OR excludes`**

- `includes:` Add an array of regular expressions to this property in the YAML to include any topics whose names match one or more of the provided regular expressions. All other topics will be excluded.
- `excludes`: Add an array of regular expressions to this property in the YAML to exclude any topics whose names match one or more of the provided regular expressions. All other topics will be included.<br>

| **Data Type**   | **Requirement** | **Default Value** | **Possible Values**                               |
| ---------- | --------------- | ------------------ | ------------------------------------------------- |
| string     | Optional        | None               | Exact values (e.g., 'employee'), regular expressions (e.g., '^sales.*') |

**Example Usage**:
```yaml
    sourceConfig:
      config:
        topicFilterPattern:
          includes:
            - ^topic00.*


```     
        
> Filter patterns support Regex in `includes` and `excludes` expressions. Refer to [Filter Pattern Examples](creating_scanner_workflows/filter_pattern_examples.md)  page for the example scenarios.

### **`markDeletedTables`**
**Description**: Set the Mark Deleted Tables property to true to flag tables as soft-deleted if they are not present anymore in the source system.<br>

| **Data Type**   | **Requirement** | **Default Value** | **Possible Values** |
| ---------- | --------------- | ------------------ | ------------------- |
| boolean    | Optional        | false              | true, false         |

**Additional information**: If a dataset is deleted from the source and hasn't been ingested in Metis during a previous scanner run, there will be no visible change in the scanned metadata on the Metis UI. However, if the deleted dataset has already been ingested in MetisDB from previous scanner runs, users can run a scanner workflow for the specific depot they want to scan with the **`markDeletedTables: true`** option in the workflow configuration. After a successful run, users can check the Metis UI to see the tables that have been marked as deleted.<br>
**Example Usage**:
```yaml
sourceConfig:
  config:
    markDeletedTables: false
```
    
### **`markDeletedTablesfromFilterOnly`**

**Description**: Set the Mark Deleted Tables property to true to flag tables as soft-deleted if they are not present anymore in the source system.<br>

| **Data Type**   | **Requirement** | **Default Value** | **Possible Values** |
| ---------- | --------------- | ------------------ | ------------------- |
| boolean    | Optional        | false              | true, false         |

**Additional information**: Set this property to true to flag tables as soft-deleted if they are not present anymore within the filtered schema or database only. This flag is useful when you have more than one ingestion pipelines.<br>
**Example Usage**:
```yaml
sourceConfig:
  config:
    markDeletedTablesfromFilterOnly: false
```

### **`ingestSampleData`**

**Description**: Set this property to true to ingest sample data from the topics.<br>

| **Data Type**   | **Requirement** | **Default Value** | **Possible Values** |
| ---------- | --------------- | ------------------ | ------------------- |
| boolean    | Optional        | false              | true, false         |

**Additional information**: Set this property to true to flag tables as soft-deleted if they are not present anymore within the filtered schema or database only. This flag is useful when you have more than one ingestion pipelines.<br>
**Example Usage**:
```yaml
sourceConfig:
  config:
    ingestSampleData: false
```

### **`markDeletedTopics`**
**Description**: Set this property to true to flag topics as soft-deleted if they are not present anymore in the source system.<br>

| **Data Type**   | **Requirement** | **Default Value** | **Possible Values** |
| ---------- | --------------- | ------------------ | ------------------- |
| boolean    | Optional        | false              | true, false         |

**Additional information**: Set this property to true to flag tables as soft-deleted if they are not present anymore within the filtered schema or database only. This flag is useful when you have more than one ingestion pipelines.<br>
**Example Usage**:
```yaml
sourceConfig:
  config:
    markDeletedTables: false
```
### **`includeViews`**
**Description**: Set this property to include views for metadata scanning.<br>

| **Data Type**   | **Requirement** | **Default Value** | **Possible Values** |
| ---------- | --------------- | ------------------ | ------------------- |
| boolean    | Optional        | false              | true, false         |

**Additional information**: Set this property to true to flag tables as soft-deleted if they are not present anymore within the filtered schema or database only. This flag is useful when you have more than one ingestion pipelines.<br>
**Example Usage**:
```yaml
sourceConfig:
  config:
    includeViews: true
```

### **`enableDebugLog`**

**Description**: To set the default log level to debug. <br>

| **Data Type**   | **Requirement** | **Default Value** | **Possible Values** |
| ---------- | --------------- | ------------------ | ------------------- |
| boolean    | Optional        | false              | true, false         |

**Example Usage**:
```yaml
sourceConfig:
  config:
    enableDebugLog: true
```    
    

