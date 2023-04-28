# **Outputs**

In order to facilitate the task of writing to multiple output locations, it is necessary to furnish an array of data definitions. The `outputs` section within the YAML encompasses the requisite configuration settings for generating output in various data formats that are compatible with Flare. This allows us to sink any of the views that were created during the input load or sequence step into a dataset.

## **Structure of the Outputs Section**

```yaml
outputs:
  - name: top_100_accounts #(Mandatory)
    dataset: dataos://icebase:bronze/topaccounts?acl=rw #(Mandatory)
    format: iceberg #(Optional)
    driver: org.apache.jdbc.psql.Driver #(Optional)
    title: Account #(Optional)
    description: Account data from GCD export #(Optional)
    tags: #(Optional)
      - Lookup-Tables
      - Accounts
    options: #(Optional)
      saveMode: overwrite
			extraOptions:
				key1: value1
	    compressionType: gzip
      sort:
        mode: partition
        columns:
          - name: version 
            order: desc 
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

The below table summarizes the various attributes within the `outputs` section:

| Property | Function | Examples | Default Value | Possible Values | Note/Rule | Field (Mandatory / Optional) |
| --- | --- | --- | --- | --- | --- | --- |
| `name` | One of the views you wanna sink into some dataset. | `- name: top_100_accounts` | NA | NA | Rules for name: 37 alphanumeric characters and a special character '-' allowed. `[a-z0-9]([-a-z0-9]*[a-z0-9]`. The maximum permissible length for the name is 47 (Note: It is advised to keep the name length less than 30 characters because the orchestration engine behind the scenes adds a Unique ID which is usually 17 characters. Hence reduce the name length to 30.  | Mandatory |
| `dataset` | Dataset where you want to write your data referred by view in `name` above.   | `dataset: dataos://icebase:bronze/topaccounts?acl=rw` | NA | NA | Must be a valid UDL and conform to the form `dataos://[depot]:[collection]/[dataset]`. | Mandatory |
| `format` | Output dataset format in which you want the output. | `format: iceberg` | Depends on the depot type | `iceberg`/`parquet`/`json`/`kafkaavro`/`kafkjson`/`pulsar`/`bigquery`  | Must be a supported format. | Optional |
| `driver` | Driver Class. | `driver: org.apache.jdbc.psql.Driver` | NA | NA | In the case of JDBC depot types, one can override the default driver class.  | Optional |
| `title` | Title of the output. | `title: Account` | NA | NA | NA | Optional |
| `description` | Description of the output. Gives details about the dataset. | `description: Account data from GCD export` | NA | NA | NA | Optional |
| `tags` | Tags provide details about data or describe the data in very short.  | `tags:` <br>&nbsp;&nbsp;&nbsp;&nbsp; `- Lookup-Tables` <br>&nbsp;&nbsp;&nbsp;&nbsp; `- Accounts` | NA | NA | NA | Optional |
| `options` | Options for the output like `saveMode`, `properties` of output file format, `partitioning`, etc. | `options:` <br>&nbsp;&nbsp;&nbsp;&nbsp; `saveMode: overwrite` <br> &nbsp;&nbsp;&nbsp;&nbsp; `compressionType: gzip` | `avro` | `avro`/`spark` | Any option supported by the underlying spark data source connector can be used | Optional |

**Additional attributes within the options**

The available output `options` include various attributes such as save mode, file format properties, partitioning, and more. It is important to note that any option supported by the underlying Spark data source connector can be utilized.

A set of option properties for Iceberg output can be specified using YAML, as exemplified in the YAML at the top. The table presented thereafter provides a description of these attributes.

| Property | Description | Examples | Default Value | Possible Values | Note/Rule | Field (Mandatory / Optional) |
| --- | --- | --- | --- | --- | --- | --- |
| `saveMode` | saveMode is used to specify the expected behavior of saving a DataFrame to a data source  | `- name: top_100_accounts` | NA | `overwrite`/`append` | NA | Optional |
| `extraOptions` | Some extra options that can be defined as key value pairs | `extraOptions:` <br>&nbsp;&nbsp;&nbsp;&nbsp; `key1: value1` | NA | NA | NA | Optional |
| `compressionType` | Compression type  | `compressionType: gzip` | Depends on depot type | `gzip`/`snappy` | NA | Optional |
| `sort` | Sort partition chunks of data or logical divisions of data are stored on a node in the cluster. You need to define the column name and order which could be ascending or descending | `sort:` <br>&nbsp;&nbsp;&nbsp;&nbsp; `mode: partition` <br>&nbsp;&nbsp;&nbsp;&nbsp; `columns:` <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `- name: version` <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `order: desc`  | NA | order : `desc`/`asc` | NA | Optional |
| `iceberg` | In case someone wanna supply additional props or partitioning scheme for iceberg format output | `title: Account` | NA | NA | This is specific for the Iceberg kind of dataset | Optional |
| `merge` | Merge on id | `iceberg:` <br>&nbsp;&nbsp;&nbsp;&nbsp; `merge:` <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `onClause: old.id = new.id` <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `whenClause: matched then update set * when not matched then insert *` | NA | NA | NA | Optional |
| `properties` | Properties of output file format | `properties:` <br>&nbsp;&nbsp;&nbsp;&nbsp; `write.format.default: parquet` <br>&nbsp;&nbsp;&nbsp;&nbsp; `write.metadata.compression-codec: gzip` | NA | NA | NA | Optional |
| `partitionSpec` | If you use sort then only partitionSpec is used. It is the specification of the partition  | `partitionSpec:` <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `- type: identity # type of column` <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `column: version # column name` <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `- type: day` <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `column: timestamp` <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `asColumn: day_partitioned` | NA | NA | NA | Optional |