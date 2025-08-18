# Attributes of Depot YAML Configuration

## Structure of Depot YAML

=== "Manifest file"
    ```yaml
    name: ${{depot-name}}
    version: v2alpha
    type: depot
    description: ${{description}}
    tags:
      - ${{tag1}}
      - ${{tag2}}
    owner: ${{owner-name}}
    layer: user
    depot:
      type: ${{source-type}}                                       
      external: ${{true}}
      compute: ${{runnable-default}}
      secrets:
        - name: ${{abfss-instance-secret-name}}-r
          allkeys: true
        - name: ${{abfss-instance-secret-name}}-rw
          allkeys: true
      ${{source-type}}:                                             
    ```

=== "Example"    
    ```yaml
    name: mydepot
    version: v2alpha
    type: depot
    description: abfss connection
    tags:
      - abfss
    owner: iamgroot
    layer: user
    depot:
      type: ABFSS                                       
      external: true
      compute: runnable-default
      secrets:
        - name: abfss-instance-secret-r
          allkeys: true
        - name: abfss-instance-secret-rw
          allkeys: true
      abfss:                                             
        account: ${{account-name}}
        container: ${{container-name}}
        relativePath: ${{relative-path}}
        format: DELTA # ICEBERG or DELTA
    ```

<center><i> Structure of Depot YAML configuration </i></center>

## Attributes Configuration

### **`name`**

**Description:** Declare a name for the Depot.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value**                                                                                                                                                                                                                                                                                                                   |
| ------------- | --------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| string        | mandatory       | none              | alpha numeric values with the RegEx  `[a-z0-9]([-a-z0-9]*[a-z0-9])`; a hyphen/dash is allowed as a special character      total length of the string should be less than or equal to 48 characters      names of cluster & depot have a different RegEx  `[a-z]([a-z0-9]*)`; a hyphen/dash is **not** allowed as a special character |


**Example usage:**

```yaml
name: resourcename
```

### **`version`**

**Description:** The version of the Resource

| **Data Type** | **Requirement** | **Default Value** | **Possible Value**           |
| ------------- | --------------- | ----------------- | ---------------------------- |
| string        | mandatory       | none              | v1, v2alpha                  |

**Example usage:**

```bash
version: v2alpha
```

### **`type`**

**Description:** Provide the value for the Resource type.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value**                                                   |
| ------------- | --------------- | ----------------- | -------------------------------------------------------------------- |
| string        | mandatory       | none              | cluster, compute, depot, policy,  secret, service, stack or workflow |

**Example usage:**

```yaml
type: depot
```

### **`tags`**

**Description:** Assign tags to the Resource-instance

| **Data Type** | **Requirement** | **Default Value** | **Possible Value**                         |
| ------------- | --------------- | ----------------- | ------------------------------------------ |
| mapping       | mandatory       | none              | any string; special characters are allowed |

**Example usage:**

```javascript
tags: 
  - data connection
  - snowflake depot
```

### **`description`**

**Description:** Assign description to Resource

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | --------------- | ----------------- | ------------------ |
| string        | optional        | none              | any string         |

**Additional information:** the description can be within quotes or without.

<aside class="callout">
🗣️ YAML supports 'scalars' such as strings, numbers, booleans, and null. A scalar value can be unquoted, within single quotes (') or double quotes ("). When the scalar contains a special character, the value must be declared within quotes.
</aside>

**Example usage:**

```yaml
description: "This is a sample description of a Resource"  
```

### **`owner`**

**Description:** Identification of the user

| **Data Type** | **Requirement** | **Default Value**                    | **Possible Value**       |
| ------------- | --------------- | ------------------------------------ | ------------------------ |
| string        | optional        | id of the user applying the Resource | any valid dataos user id |

**Additional information:** when no ID**** is provided, or an incorrect ID is provided, the system automatically corrects it to the ID of the user who applied the Resource on DataOS CLI

**Example usage:**

```yaml
owner: iamgroot
```

### **`layer`**

**Description:** Declare the name of the layer in which the Resource is going to be deployed

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| ------------- | --------------- | ----------------- | ------------------ |
| string        | optional        | user              | user/system        |

**Additional information:**
From a user's perspective, the operating system can be envisaged as working at two levels - user layer & system layer. This is only a logical separation to understand the workings of the system.

**Example usage:**

```yaml
layer: user
```

## `depot`
<b>Description:</b> specifies the configuration for the Depot section <br>

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|--------------|-------------|---------------|----------------|
| mapping       | mandatory   | none          | none           |

<b>Example Usage:</b>

```yaml
depot:
  {}
```

### **`type`**
<b>Description:</b> Specifies the type of Depot <br>

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|-----------|-------------|---------------|---------------------------------------------------------|
| string    | mandatory   | none          | ABFSS, WASBS, REDSHIFT, S3, ELASTICSEARCH, EVENTHUB, PULSAR, BIGQUERY, GCS, JDBC, MSSQL, MYSQL, OPENSEARCH, ORACLE, POSTGRES, SNOWFLAKE |

<b>Example Usage:</b>
```yaml
type: ABFSS
```

### **`description`**
<b>Description:</b> Provides a description for the Depot <br>

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|-----------|-------------|---------------|----------------|
| string    | optional    | none          | any string     |

<b>Example Usage:</b>
```yaml
description: Azure Blob Storage Depot
```

### **`external`**
<b>Description:</b> Specifies whether the depot is external. Set to true if the depot is external<br>

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|-----------|-------------|---------------|----------------|
| string    | mandatory   | false         | true/false     |

<b>Example Usage:</b>
```yaml
external: true
```

### **`source`**
<b>Description:</b> Maps the depot to the metadata source name in Metis. Running a scanner job on this depot will save the metadata in Metis DB under the specified 'source' name. If this key-value property is not mentioned, the metadata will surface under the depot name on Metis UI.<br>

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|-----------|-------------|---------------|----------------|
| string    | optional    | depot name    | any string     |

<b>Example Usage:</b>

```yaml
source: bigquerymetadata
```

### **`compute`**
<b>Description:</b> Specifies the compute resource for the depot being created.<br>

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|-----------|-------------|---------------|----------------|
| string    | optional    | runnable-default | any Compute Resource |

<b>Example Usage:</b>

```yaml
compute: runnable-default
```

### **`secrets`**
<b>Description:</b> Specifies the cInstance Secret reference of the data source.<br>

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|-----------|-------------|---------------|----------------|
| mapping    | optional    | none          | varies between data sources |

<b>Example Usage:</b>

```yaml
secrets:
  - name: ${{abfss-instance-secret-name}}-r    # Name of the read-only Instance Secret
    allkeys: true                              # Use all keys from this secret
  - name: ${{abfss-instance-secret-name}}-rw   # Name of the read-write Instance Secret
    allkeys: true                              # Use all keys from this secret
```

### **`secrets.name`**

The 'name' attribute specifies the name of the Instance Secret to be used for authentication.

### **`secrets.allkeys`**

The 'allkeys' attribute, when set to true, indicates that all keys within the referenced Instance Secret are available for use.

### **`${{depot-type}}`**

<b>Description:</b> Specifies the precise location of the data and provides the hierarchical structure in which the data is stored. <br>

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|-----------|-------------|---------------|----------------|
| mapping    | mandatory   | none          | varies between data sources |

<b>Example Usage:</b>

```yaml
  abfss:                                             
    account: ${{account-name}}
    container: ${{container-name}}
    relativePath: ${{relative-path}}
    format: ${{format}} # ICEBERG or DELTA
```
<aside class="callout">
🗣️ More information about the attributes specific to each source type is provided in their respective prerequisites section.
</aside>