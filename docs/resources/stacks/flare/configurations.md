# Attributes of Flare Configuration

Flare Stack can be configured using attributes in a declarative YAML format.

## Structure of Flare Stack-specific Section

```yaml
flare:
  driver:
    coreLimit: {{1000m}} 
    cores: {{1}}
    memory: {{1024m}}
  executor: 
    coreLimit: {{1000m}}
    cores: {{1}}
    instances: {{1}}
    memory: {{1024m}}
  job:
    explain: {{true}}
    logLevel: {{INFO}}
    streaming: # Streaming Section
      {}
    inputs: #Inputs Section
      {}
    outputs: #Outputs Section
      {}
    steps: # Steps Section
      {}
    assertions: # Assertions Section
      {}
    actions: # Actions Section
      {}
```

The below table summarizes the various attributes within the Flare Stack-specific Section:

<center>

| Attributes | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| [`flare`](./configurations/flare_stack_specific_grammar.md#flare) | object | none | none | mandatory |
| [driver](./configurations/flare_stack_specific_grammar.md#driver) | object | none | none | optional |
| [`executor`](./configurations/flare_stack_specific_grammar.md#executor) | object | none | none | optional |
| [`job`](./configurations/flare_stack_specific_grammar.md#job) | object | none | none | mandatory |
| [`explain`](./configurations/flare_stack_specific_grammar.md#explain) | boolean | false | true/false | optional |
| [`logLevel`](./configurations/flare_stack_specific_grammar.md#loglevel) | string | INFO | INFO / WARN /<br>DEBUG/ ERROR | optional |
| [`streaming`](./configurations/streaming.md) | object | none | none | optional |
| [`inputs`](./configurations/inputs.md) | object | none | none | mandatory |
| [`steps`](./configurations/steps.md) | object | none | none | optional |
| [`outputs`](./configurations/outputs.md) | object | none | none | mandatory |
| [`assertions`](./configurations/assertions.md) | object | none | none | optional |
| [`actions`](./configurations/actions.md) | object | none | none | optional |

</center>

Refer to the link here for more information regarding the Flare Stack-specific Section attributes, click [here.](./configurations/flare_stack_specific_grammar.md)


A Flare Job can be further split into 5 sections:

#### **Inputs**

The `inputs` section encompasses crucial configuration settings necessary for extracting data from diverse sources, such as name, format, dataset address, etc. To facilitate reading data from multiple sources, an array of data source definitions are required. To obtain more detailed information, kindly refer to the link below.


# Flare Input Section Grammar

Within the Flare Job's `inputs` section, users can define the configuration details for input datasets. This allows the Flare Job to read data from different supported data sources. It is worth mentioning that a single Flare Job can handle multiple data sources simultaneously.

## Structure of the `inputs` Section

### **Common Configuration**

```yaml
inputs:
  - name: {{account_connect}}
    dataset: {{dataos://gcdexport:none/gcdcore_account}}
    format: {{csv}}
```
<center><i> Flare Input Section Common YAML Configuration </i></center>

### **Advanced Configuration**

```yaml
inputs:
  - name: {{account_connect}}
    dataset: {{dataos://gcdexport:none/gcdcore_account}}
    query: {{select * from icebase.retail.city limit 100}}
    format: {{csv}}
    isStream: {{true}}
    schemaType: {{avro}}
    schemaPath: {{dataos://thirdparty:none/somedir/someschema.avsc}}
    schemaString: {{"{avsc_schema_file_content}"}}
    schemaSubject: {{custom-topic-value-schema-name}}
    schemaId: {{2}}
    options:
      {{key1: value1}}
      {{key2: value2}}
    incremental:
      context: {{incrinput}}
      sql: {{select ws_sold_date_sk, ws_sold_time_sk, ws_item_sk, ws_bill_customer_sk, ws_web_page_sk, ws_ship_mode_sk, ws_order_number, ws_quantity, ws_list_price,ws_sales_price, ws_wholesale_cost, ws_net_profit from incrinput where ws_sold_date_sk between '$|start_date|' AND '$|end_date|'}}
      keys:
        - name: {{start_date}}
          sql: {{select 2452641}}
        - name: {{end_date}}
          sql: {{select 2452642}}
      state:
        - key: {{start_date}}
          value: {{end_date}}
```

<center><i> Flare Input Section Advanced YAML Configuration </i></center>

## Configuration Fields

### **`inputs`**
<b>Description:</b> All input datasets and their specific properties are declared within this section<br>
<b>Data Type:</b> Object <br>
<b>Requirement:</b> Mandatory <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> None <br>
<b>Example Usage:</b>

```yaml
inputs:
  {}
```

---

### **`name`**
<b>Description:</b> This field represents the assigned name to the input. It serves as a reference for the input and can be used for querying the input using Spark SQL. Consider this field as a view in Spark, allowing you to interact with the input data.<br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Mandatory <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> None <br>
<b>Example Usage:</b>

```yaml
name: account_connect
```

---

### **`dataset`**
<b>Description:</b> Represents the UDL address of the dataset from which you want to read data. You can also load a specific file within the dataset. For example, `dataos://gcdexport:none/gcdcore_account/account_x.csv`. <br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Mandatory <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> Any valid UDL address <br>
<b>Example Usage:</b>

```yaml
dataset: dataos://gcdexport:none/gcdcore_account
```

---

### **`query`**
<b>Description:</b> Flare supports reading from Minerva. The field allows you to specify a Minerva SQL directly. This enables you to load the result of the specified query and make it available as a view in the Spark session. <br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Mandatory <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> Any valid Minerva SQL query <br>
<b>Example Usage:</b>

```yaml
query: select * from icebase.retail.city limit 100
```

---

### **`format`**
<b>Description:</b> Format of the `dataset` <br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> iceberg <br>
<b>Possible Value:</b> iceberg/text/json/parquet/orc/avro/csv/hudi/xml/db/xlsx <br>
<b>Example Usage:</b>

```yaml
format: csv
```

---

### **`isStream`**
<b>Description:</b>  The `isStream` field is used to determine whether to read a dataset in a streaming fashion. Set this flag to `true` if you want to read the dataset as a stream. <br>
<b>Data Type:</b> Boolean <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> If not supplied, the default value will be determined based on the depot type. For depots like Kafka and EventHub, the default value is true, while for depots like GCS and ABFSS, the default value is false. <br>
<b>Possible Value: true/false</b><br>
<b>Example Usage:</b>

```yaml
isStream: true
```

---

### **`schemaType`**
<b>Description:</b> The `schemaType` field specifies the type of schema provided in the `schemaPath` or `schemaString` field above. <br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> avro <br>
<b>Possible Value:</b> avro/spark <br>
<b>Example Usage:</b>

```yaml
schemaType: avro
```

---

### **`schemaPath`**
<b>Description:</b> Represents the DataOS address to the schema that will be applied when loading the dataset. This field is particularly useful for datasets with formats like CSV. <br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> None <br>
<b>Example Usage:</b>

```yaml
schemaPath: dataos://thirdparty:none/somedir/someschema.avsc
```

---

### **`schemaString`**
<b>Description:</b> The `schemaString` field represents the Spark struct schema JSON string or Avro schema JSON.  <br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> None <br>
<b>Example Usage:</b>

```yaml
schemaString: "{avsc_schema_file_content}"
```

---

### **`schemaSubject`**
<b>Description:</b> The `schemaSubject` field represents the subject name of the schema associated with the input data. It can be used to override a subject name to refer to the schema of a Kafka topic in the schema registry when loading Avro data from it.<br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> None <br>
<b>Example Usage:</b>

```yaml
schemaSubject: custom-topic-value-schema-name
```

---

### **`schemaId`**
<b>Description:</b> The `schemaId` field represents the ID of the schema associated with the input data. It is used when utilizing a schema with a specified schema ID in the Kafka schema registry. <br>
<b>Data Type:</b> Integer <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> None <br>
<b>Example Usage:</b>

```yaml
schemaId: 2
```

---

### **`options`**
<b>Description:</b> The `options` field allows you to specify additional options or configurations for the input. These options are provided as key-value pairs. You can use any other options supported by the underlying Spark connector to load data from the supplied dataset. Flare will iterate over these options and forward each one of them to Spark.<br>
<b>Data Type:</b> Map (String, String)<br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> None <br>
<b>Example Usage:</b>

```yaml
options:
  key1: value1
  key2: value2
```

---

### **`incremental`**
<b>Description:</b> The `incremental` field allows you to load data from a dataset in an incremental fashion, you can use this configuration. This feature is particularly useful when dealing with large datasets and performing incremental updates.<br>
<b>Data Type:</b> Object <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> None <br>
<b>Example Usage:</b>

```yaml
incremental:
  context: incrinput
  sql: select ws_sold_date_sk , ws_sold_time_sk , ws_item_sk, ws_bill_customer_sk , ws_web_page_sk ,ws_ship_mode_sk, ws_order_number, ws_quantity,ws_list_price ,ws_sales_price , ws_wholesale_cost  , ws_net_profit from incrinput where ws_sold_date_sk between '$|start_date|' AND '$|end_date|'
  keys:
    - name: start_date
      sql: select 2452641
    - name: end_date
      sql: select 2452642
  state:
    - key: start_date
      value: end_date
```

---

### **`context`**

<b>Description:</b> The context or name of the incremental input. <br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Mandatory for incremental processing<br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> Any string <br>
<b>Example Usage:</b>

```yaml
context: incrinput
```

---

### **`sql`**

<b>Description:</b> The SQL query used to retrieve the incremental data from the input. It should specify the columns and conditions for the incremental processing. <br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Mandatory <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> None <br>
<b>Example Usage:</b>

```yaml
sql: select ws_sold_date_sk, ws_sold_time_sk, ws_item_sk, ws_bill_customer_sk, ws_web_page_sk, ws_ship_mode_sk, ws_order_number, ws_quantity, ws_list_price,ws_sales_price, ws_wholesale_cost, ws_net_profit from incrinput where ws_sold_date_sk between '$|start_date|' AND '$|end_date|'
```

---

### **`keys`**

<b>Description:</b> The keys used for incremental processing. Each key contains a name and an SQL query that retrieves the corresponding value for the key. <br>
<b>Data Type:</b> List of Objects <br>
<b>Requirement:</b> Mandatory for incremental processing <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> None <br>
<b>Example Usage:</b>

```yaml
keys:
  - name: start_date
    sql: select 2452641
  - name: end_date
    sql: select 2452642
```

---

### **`state`**

<b>Description:</b> The state or key-value pairs used to store the incremental processing state. Each state entry consists of a key and its corresponding value. <br>
<b>Data Type:</b> List of Objects <br>
<b>Requirement:</b> Optional <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> None <br>
<b>Example Usage:</b>

```yaml
state:
  - key: start_date
    value: end_date
```

[Inputs](./configurations/inputs.md)

#### **Outputs**

The `outputs` section provides comprehensive information regarding the storage location and naming convention for the output dataset. To access additional details, please refer to the link provided below.

[Outputs](./configurations/outputs.md)

#### **Steps**

The `steps` section outlines the prescribed sequence of tasks for data enrichment and processing, including but not limited to the addition of calculated columns, aggregations, and filtering via SQL. These are defined in `sequence` under `steps`. For further information, please consult the linked page.

[Steps](./configurations/steps.md)

#### **Streaming**

The `streaming` section encompasses properties that pertain to the execution of stream jobs. For further details, please refer to the page provided below.

[Streaming](./configurations/streaming.md)

#### **Assertions**

In the context of data quality, assertions refer to validation rules that are tailored to a particular business domain and serve to determine the fitness-for-purpose of datasets. The application of assertions enables the execution of additional validation checks on top of existing datasets, thereby enhancing their overall quality. Assertions are defined within the dedicated `assertions` section. To gain further insights, please refer to the following page.

[Assertions](./configurations/assertions.md)

To perform validation checks on datasets that are to be written, click [here.](./case_scenario/data_quality_jobs.md#pre-sink-assertions)

#### **Actions**

The DataOS platform provides comprehensive support for executing maintenance actions within the Icebase depot. These are specified within the `actions` section. For further information, please refer to the following page.

[Actions](./configurations/actions.md)