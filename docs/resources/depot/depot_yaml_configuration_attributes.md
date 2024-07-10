# Attributes of Depot YAML Configuration

## Structure of Depot YAML

```yaml
depot:
  type: ${{S3}}                                          
  description: ${{description}}
  external: ${{true}}
  source: ${{metadata}}
  compute: ${{runnable-default}}
  connectionSecret:                                
    - acl: ${{rw}}
      type: key-value-properties
      data:
        ${{data-source-specific-connection-secrets}}
  spec:
    ${{data-source-specifications}}
```
<center><i> Structure of Depot YAML configuration </i></center>

## Attributes Configuration

## **`depot`**
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

### **`connectionSecret`**
<b>Description:</b> Specifies the connection secrets for the data source.<br>

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|-----------|-------------|---------------|----------------|
| mapping    | optional    | none          | varies between data sources |

<b>Example Usage:</b>
```yaml
connectionSecret:
  {} 
```

#### **`acl`**
<b>Description:</b> Declares the access policy for the depot. Multiple connections with different access levels can be created for the same depot. For example, read and write permissions for a specific transformation and read-only permission for another operation using the same depot. <br>

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|-----------|-------------|---------------|----------------|
| string    | optional    | r             | r/rw           |

<b>Example Usage:</b>

```yaml
acl: rw
```

#### **`type`**
<b>Description:</b> Specifies the type of Secret<br>

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|-----------|-------------|-------------------|--------------------|
| string    | optional    | key-value-properties | key-value-properties |

<b>Example Usage:</b>

```yaml
type: key-value-properties 
```

#### **`data`**
<b>Description:</b> Provides the credentials and additional information needed to connect with the data source, such as access key ID, secret key ID, username, and passwords. <br>

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|-----------|-------------|---------------|----------------|
| mapping    | optional    | none          | varies between data sources |

<b>Example Usage:</b>

```yaml
data:
  projectid: project-name
  email: iamgroot@tmdc.io
```

#### **`files`**
<b>Description:</b> Allows storing sensitive information in a separate JSON file. Specify the absolute path to the JSON file containing the credentials.<br>

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|-----------|-------------|---------------|-------------------|
| string    | optional    | none          | valid absolute path |

<b>Example Usage:</b>

```yaml
files:
  json_keyfile: secrets/gcp-demo-sa.json
```

### **`spec`**
<b>Description:</b> Specifies the precise location of the data and provides the hierarchical structure in which the data is stored. <br>

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|-----------|-------------|---------------|----------------|
| mapping    | mandatory   | none          | varies between data sources |

<b>Example Usage:</b>

```yaml
spec:
  host: host
  port: port
```

