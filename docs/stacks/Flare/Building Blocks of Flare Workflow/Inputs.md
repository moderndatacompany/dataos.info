# Inputs

Within the `inputs` section of a Flare Job, users can specify the input dataset details required for reading data from various supported data sources. It is important to note that a single Flare Job has the ability to read data from multiple data sources.

## Structure of Input Section

```yaml
inputs:
    - name: account_connect #(Mandatory)
      dataset: dataos://gcdexport:none/gcdcore_account #(Mandatory)
			query: select * from icebase.retail.city limit 100 #(Optional)
      format: csv #(Mandatory)
      isStream: true #(Optional)
      schemaType: "avro" #(Optional)
      schemaPath: "dataos://thirdparty:none/somedir/someschema.avsc" #(Optional)
      schemaString: "{avsc_schema_file_content}" #(Optional)
      schemaSubject: custom-topic-value-schema-name, #(Optional)
      schemaId: 2 #(Optional)
      options: #(Optional)
				key1: value1
				key2: value2
      incremental: #(Optional)
				context: incrinput
        sql: select ws_sold_date_sk , ws_sold_time_sk , ws_item_sk, ws_bill_customer_sk , ws_web_page_sk ,ws_ship_mode_sk,
          ws_order_number, ws_quantity,ws_list_price ,ws_sales_price , ws_wholesale_cost  , ws_net_profit from incrinput where ws_sold_date_sk between '$|start_date|' AND '$|end_date|'
        keys:
          - name: start_date
            sql: select 2452641
          - name: end_date
            sql: select 2452642
				state:
					- key: start_date
						value: end_date
```

The below table summarizes the various attributes within the `inputs` section:

| Property | Description | Examples | Default Value | Possible Values | Note/Rule | Field (Mandatory / Optional) |
| --- | --- | --- | --- | --- | --- | --- |
| `name` | Name with which you will refer this input dataset | `name: account_connect` | NA | NA | Rules for name: 37 alphanumeric characters and a special character '-' allowed. `[a-z0-9]([-a-z0-9]*[a-z0-9]`. The maximum permissible length for the name is 47 (Note: It is advised to keep the name length less than 30 characters because the orchestration engine behind the scenes adds a Unique ID which is usually 17 characters. Hence reduce the name length to 30.  | Mandatory |
| `dataset` | Dataset address you wanna read from. You can also load a specific file within a dataset | `dataos://gcdexport:none/gcdcore_account` <br> or (for a specific file path) `dataos://gcdexport:none/gcdcore_account/account_x.csv` | NA | NA | Must be a valid UDL and conform to the form `dataos://[depot]:[collection]/[dataset].`  | Mandatory |
| `query` | Flare does support reading from Minerva. You can specify a Minerva SQL directly to load the result of the specified query. | `query: select * from icebase.retail.city limit 100` | NA | NA | NA | Optional |
| `format` | Format of the `dataset`.  | `format: csv` | `iceberg` | `iceberg`/`text`/`json`/`parquet`/`orc`/`avro`/`csv`/`xml` | Must be one of the available formats. | Mandatory |
| `isStream` | Set this flag as true to read some dataset in a streaming fashion. Only if stream is `true` the Streaming Section attributes can be used | `isStream: true` | Depends on Depot Type | `true` /`false` | If value is not supplied we default it to `true`/`false` based on the depot type e.g. for depots like Kafka and eventhub it is `true` and for gcs/abfss etc it is `false`. | Optional |
| `schemaString` | Spark struct schema | `schemaString: "{avsc_schema_file_content}"` | `json` | `json`/`avro` | NA | Optional |
| `schemaPath` | DataOS address to schema to be applied while loading the dataset. This is very helpful in case of few datasets with format like csv.  | `schemaPath: "dataos://thirdparty:none/somedir/someschema.avsc"` | NA | NA | The schemapath should be valid and should conform to the format `dataos://[depot]:[collection]/[dataset]` <br> OR `dataos://[depot]:[collection]/[dataset]`. | Optional |
| `schemaType` | Type of schema supplied in `schemaPath` or `schemaString` above | `schemaType: "avro"` | `avro` | `avro`/`spark` | NA | Optional |
| `schemaSubject` | Use this to override a subject name to be used to refer schema of a kafka topic in schema registry while loading avro data from the same. | `schemaSubject: custom-topic-value-schema-name` | NA | NA | NA | Optional |
| `schemaId` | In case of utilising a schema with specified schema id in kafka schema registry. | `schemaId: 2` | NA | NA | NA | Optional |
| `options` | All other options supported by the underlying spark connector to load data from the supplied dataset. Flare will just iterate over them and will forward each one of those to spark. | `options:` <br> `key1: value1` <br> `key2: value2` | NA | NA | NA | Optional |
| `incremental` | Loads data from some dataset in an incremental fashion | `incremental:` <br>&nbsp;&nbsp;&nbsp;&nbsp; `context: incrinput` <br>&nbsp;&nbsp;&nbsp;&nbsp; `sql: select table_1, table_2` <br>&nbsp;&nbsp;&nbsp;&nbsp; `keys:` <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `- name: start_date` <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `sql: select 2452641` <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `- name: end_date` <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `sql: select 2452642` <br>&nbsp;&nbsp;&nbsp;&nbsp; `state:` <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `- key: start_date` <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `value: end_date`   | NA | NA | NA | Optional |