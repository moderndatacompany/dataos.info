# Flare Output Section YAML Configuration Field Reference

The Flare Output Section YAML Configuration provides users with the necessary tools to define the output dataset settings for writing data to different destinations. It enables users to specify the desired format, compression, partitioning, and other options for the output dataset.

## Structure of the Outputs Section

```yaml
outputs:
  - name: {{top_100_accounts}}
    dataset: {{dataos://icebase:bronze/topaccounts?acl=rw}}
    format: {{iceberg}}
    driver: {{org.apache.jdbc.psql.Driver}}
    title: {{Account}}
    description: {{Account data from GCD export}}
    tags:
      - {{Lookup-Tables}}
      - {{Accounts}}
    options:
      saveMode: {{overwrite}}
      extraOptions:
        {{key1: value1}}
      compressionType: {{gzip}}
      sort:
        mode: {{partition}}
        columns:
          - name: {{version}}
            order: {{desc}}
      iceberg:
        merge:
          onClause: {{old.id = new.id}}
          whenClause: {{matched then update set * when not matched then insert *}}
        properties:
          write.format.default: {{parquet}}
          write.metadata.compression-codec: {{gzip}}
        partitionSpec:
          - type: {{identity}}
            column: {{version}}
          - type: {{day}}
            column: {{timestamp}}
            asColumn: {{day_partitioned}}
```

## Configuration Fields

### **`outputs`**
<b>Description:</b> The `outputs` section comprises of configurations for sinking any of the views created during input load or sequence step into a dataset. <br>
<b>Data Type:</b> Object <br>
<b>Requirement:</b> Mandatory <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> None <br>
<b>Example Usage:</b>

```yaml
outputs:
  {} # Properties within the outputs section
```

### **`name`**
<b>Description:</b> Name assigned to one of the views you want to sink as an output dataset. <br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Mandatory <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> None <br>
<b>Example Usage:</b>

```yaml
name: top_100_accounts
```

### **`dataset`**
<b>Description:</b> DataOS UDL address specifying the location where the output dataset will be stored. dataset where you want to write your data referred by view in `name` above. <br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Mandatory <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> Any valid UDL address except the input dataset address<br>
<b>Example Usage:</b>

```yaml
dataset: dataos://icebase:bronze/topaccounts?acl=rw
```

### **`format`**
<b>Description:</b> File format in which the output dataset will be saved.<br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> Based on output depot type <br>
<b>Possible Value:</b> iceberg/parquet/json/kafkaavro/kafkajson/pulsar/bigquery <br>
<b>Example Usage:</b>

```yaml
format: iceberg
```

### **`driver`**
<b>Description:</b> The field can be used to override the default driver class in case of output dataset to be stored in JDBC depot types. <br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> None <br>
<b>Example Usage:</b>

```yaml
driver: org.apache.jdbc.psql.Driver
```

### **`title`**
<b>Description:</b> Title of the output dataset. <br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> Any string <br>
<b>Example Usage:</b>

```yaml
title: Account
```

### **`description`**
<b>Description:</b> Description of the output dataset. <br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> Any string <br>
<b>Example Usage:</b>

```yaml
description: Account data from GCD export
```

### **`tags`**
<b>Description:</b> List of tags or labels associated with the output dataset. <br>
<b>Data Type:</b> List of strings <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> Any string <br>
<b>Example Usage:</b>

```yaml
tags:
  - Lookup-Tables
  - Accounts
```

### **`options`**
<b>Description:</b> Additional options or configurations for the output dataset. They are specified as key-value pairs. These include properties for saveMode, partitioning, etc.<br>
<b>Data Type:</b> Object <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b>Any option supported by the underlying Spark datasource connector<br>
<b>Example Usage:</b>

```yaml
options:
  saveMode: overwrite
  extraOptions:
    key1: value1
  compressionType: gzip
  sort:
    mode: partition
    columns:
      - name: version
        order: desc
```

### **`saveMode`**
<b>Description:</b> `saveMode` is used to specify the expected behavior of saving a Dataframe to a data source<br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> overwrite <br>
<b>Possible Value:</b>overwrite/append<br>
<b>Example Usage:</b>

```yaml
saveMode: overwrite
```

### **`extraOptions`**
<b>Description:</b> `extraOptions` is used to specify some additional key-value properties<br>
<b>Data Type:</b> Map(String,String) <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b>None<br>
<b>Example Usage:</b>

```yaml
extraOptions:
  key1: value1
```

### **`compressionType`**
<b>Description:</b> Type of Compression<br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> gzip <br>
<b>Possible Value:</b>gzip/snappy<br>
<b>Example Usage:</b>

```yaml
compressionType: gzip
```

### **`sort`**
<b>Description:</b> This field comprises of properties for sorting column values in ascending or descending order.<br>
<b>Data Type:</b> Object <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b>None<br>
<b>Additional Details:</b> In `partition` mode, chunk of data or logical division of data are stored on a node in the cluster in Iceberg kind of dataset.<br>
<b>Example Usage:</b>

```yaml
sort:
  mode: partition
  columns:
    - name: version # column name
      order: desc # order (asc, desc)
```

### **`iceberg`**
<b>Description:</b> Configuration specific to the Iceberg format. This section allows you to specify additional Iceberg-specific options and properties for the output dataset. <br>
<b>Data Type:</b> Object <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> None <br>
<b>Example Usage:</b>

```yaml
iceberg:
  merge:
    onClause: old.id = new.id
    whenClause: matched then update set * when not matched then insert *
  properties:
    write.format.default: parquet
    write.metadata.compression-codec: gzip
  partitionSpec:
    - type: identity
      column: version
    - type: day
      column: timestamp
      asColumn: day_partitioned
```

### **`merge`**
<b>Description:</b> Configuration for merge operation in Iceberg. Specifies the merge behavior for updates and inserts. <br>
<b>Data Type:</b> Object <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> None <br>
<b>Example Usage:</b>

```yaml
merge:
  onClause: old.id = new.id
  whenClause: matched then update set * when not matched then insert *
```


### **`onClause`**
<b>Description:</b> The ON clause to define the merge condition. Specifies the condition to match rows for update or insert operations. <br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> None
<b>Example Usage:</b>

```yaml
onClause: old.id = new.id
```

### **`whenClause`**
<b>Description:</b> The WHEN clause to define the merge behavior. Specifies the action to be performed for matched and unmatched rows. <br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> None <br>
<b>Example Usage:</b>

```yaml
whenClause: matched then update set * when not matched then insert *
```

### **`properties`**
<b>Description:</b> Additional properties to be set for the Iceberg writer. Allows you to specify custom properties or override default properties. <br>
<b>Data Type:</b> Map (String, String) <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> None <br>
<b>Example Usage:</b>

```yaml
properties:
  write.format.default: parquet
  write.metadata.compression-codec: gzip
```

### **`partitionSpec`**
<b>Description:</b> Partitioning configuration for the output dataset. Specifies how the data should be partitioned in the Iceberg format. <br>
<b>Data Type:</b> List of Objects <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> None <br>
<b>Example Usage:</b>

```yaml
partitionSpec:
  - type: identity 
    column: version 
  - type: day
    column: timestamp
    asColumn: day_partitioned
```

### **`type`**
<b>Description:</b> The type of partitioning to be applied. Specifies the partitioning strategy. <br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Mandatory <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> identity/year/month/day/hour <br>
<b>Example Usage:</b>

```yaml
type: identity
```

### **`column`**
<b>Description:</b> The column to be used for partitioning. Specifies the column name on which the partitioning should be based. <br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> None <br>
<b>Example Usage:</b>

```yaml
column: timestamp
```

### **`asColumn`**
<b>Description:</b> Specifies the column name after paritioning. <br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> None <br>
<b>Example Usage:</b>

```yaml
asColumn: day_partitioned
```