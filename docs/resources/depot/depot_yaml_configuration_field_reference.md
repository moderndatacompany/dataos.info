# Depot-specific Section YAML Configuration Field Reference

## Syntax of Depot-specific Section

```yaml
depot:
  type: {{S3}}                                          
  description: {{description}}
  external: {{true}}
  source: {{metadata}}
  compute: {{runnable-default}}
  connectionSecret:                                
    name: {{secret-name}}
    - acl: {{rw}}
      type: key-value-properties
      data:
        {{data-source-specific-connection-secrets}}
  spec:
    {{data-source-specifications}}
```
<center><i> Depot YAML Configuration </i></center>

## Configuration Fields

### **`depot`**
<b>Description:</b> Specifies the configuration for the Depot section <br>
<b>Data Type:</b> Object <br>
<b>Requirement:</b> Mandatory <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> None <br>
<b>Example Usage:</b>

```yaml
depot:
  {}
```

### **`type`**
<b>Description:</b> Specifies the type of Depot <br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Mandatory <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> ABFSS, WASBS, REDSHIFT, S3, ELASTICSEARCH, EVENTHUB, PULSAR, BIGQUERY, GCS, JDBC, MSSQL, MYSQL, OPENSEARCH, ORACLE, POSTGRES, SNOWFLAKE <br>
<b>Example Usage:</b>
```yaml
type: ABFSS
```

### **`description`**
<b>Description:</b> Provides a description for the Depot <br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> Any string <br>
<b>Example Usage:</b>
```yaml
description: Azure Blob Storage Depot
```

### **`external`**
<b>Description:</b> Specifies whether the depot is external. Set to true if the depot is external<br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Mandatory <br>
<b>Default Value:</b> false <br>
<b>Possible Value:</b> true/false <br>
<b>Example Usage:</b>
```yaml
external: true
```

### **`source`**
<b>Description:</b> Maps the depot to the metadata source name in Metis. Running a scanner job on this depot will save the metadata in Metis DB under the specified 'source' name. If this key-value property is not mentioned, the metadata will surface under the depot name on Metis UI.<br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> depot name <br>
<b>Possible Value:</b> Any string <br>
<b>Example Usage:</b>

```yaml
source: bigquerymetadata
```

### **`compute`**
<b>Description:</b> Specifies the compute resource for the depot being created.<br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> runnable-default <br>
<b>Possible Value:</b> Any compute resource <br>
<b>Example Usage:</b>

```yaml
compute: runnable-default
```

### **`connectionSecret`**
<b>Description:</b> Specifies the connection secrets for the data source.<br>
<b>Data Type:</b> Object <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> Varies between data sources <br>
<b>Example Usage:</b>
```yaml
connectionSecret:
  {} 
```

### **`acl`**
<b>Description:</b> Declares the access policy for the depot. Multiple connections with different access levels can be created for the same depot. For example, read and write permissions for a specific transformation and read-only permission for another operation using the same depot. <br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> r <br>
<b>Possible Value:</b> r/rw <br>
<b>Example Usage:</b>

```yaml
acl: rw
```

### **`type`**
<b>Description:</b> Specifies the type of Secret<br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> key-value-properties <br>
<b>Possible Value:</b> key-value-properties <br>
<b>Example Usage:</b>

```yaml
type: key-value-properties 
```

### **`data`**
<b>Description:</b> Provides the credentials and additional information needed to connect with the data source, such as access key ID, secret key ID, username, and passwords. <br>
<b>Data Type:</b> Object <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> Varies between data sources <br>
<b>Example Usage:</b>

```yaml
data:
  projectid: project-name
  email: iamgroot@tmdc.io
```

### **`files`**
<b>Description:</b> Allows storing sensitive information in a separate JSON file. Specify the absolute path to the JSON file containing the credentials.<br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> Valid absolute path <br>
<b>Example Usage:</b>

```yaml
files:
  json_keyfile: secrets/gcp-demo-sa.json
```

### **`name`**
<b>Description:</b> Specifies the name of the Secret resource containing the connection credentials.
<br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> Valid Secret resource name <br>
<b>Example Usage:</b>

```yaml
name: "mysql-secret"
```

### **`spec`**
<b>Description:</b> Specifies the precise location of the data and provides the hierarchical structure in which the data is stored. <br>
<b>Data Type:</b> Object <br>
<b>Requirement:</b> Mandatory <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> Varies between data sources <br>
<b>Example Usage:</b>

```yaml
spec:
  host: host
  port: port
```