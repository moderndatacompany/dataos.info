# Attributes of Flare `stackSpec`

The `stackSpec` configuration within a Flare Job provides a flexible way to define the operational characteristics of a job. The configuration is expressed through a structured mapping in a declarative YAML. Each attribute within the `stackSpec` mapping (or section) precisely controls various aspects of the job's execution environment, allowing for detailed customization and optimization of resource allocation and job behavior. By specifying these attributes, users can finely tune their Flare Jobs to match specific performance and resource requirements.


## Structure of Flare `stackSpec` section

```yaml
stackSpec: # Flare Stack-specific section or mapping (mandatory)

# Driver and Executor resources configuration
  driver: # Driver configuration (optional)
    coreLimit: 1000m # Core limit for the driver (optional)
    cores: 1 # Number of cores for the driver (optional)
    memory: 1024m # Memory allocation for the driver (optional)
  executor: # Executor configuration (optional)
    coreLimit: 1000m # Core limit for each executor (optional)
    cores: 1 # Number of cores for each executor (optional)
    instances: 1 # Number of executor instances (optional)
    memory: 1024m # Memory allocation for each executor (optional)

# Flare Job configuration

  job: # Job configuration (mandatory)
    logLevel: INFO # Application log level (optional)
    explain: true # Flag to print Spark logical/physical plans (optional)

# Input Dataset configurations (mandatory)
    inputs:
      - name: account_connect # Reference name for input dataset (mandatory)
        dataset: dataos://gcdexport:none/gcdcore_account # Dataset address (mandatory)
        query: select * from icebase.retail.city limit 100 # SQL query for data load (mandatory)
        format: csv # Data format of the dataset (optional, default: iceberg)
        isStream: true # Flag for streaming dataset (optional, default: false)
        schemaType: "avro" # Schema type (optional, default: avro)
        schemaPath: "dataos://thirdparty:none/somedir/someschema.avsc" # DataOS address to schema (optional)
        schemaString: "{avsc_schema_file_content}" # Spark struct or Avro schema JSON (optional)
        schemaSubject: custom-topic-value-schema-name # Subject name for schema registry (optional)
        schemaId: 2 # Schema ID in schema registry (optional)
        options: # Additional data load options (optional)
          branch: b1
          key1: value1
          key2: value2
        incremental: # Incremental load configuration (optional)
          context: incrinput
          sql: select ws_sold_date_sk, ws_sold_time_sk, ws_item_sk, ws_bill_customer_sk, ws_web_page_sk, ws_ship_mode_sk, ws_order_number, ws_quantity, ws_list_price,ws_sales_price, ws_wholesale_cost, ws_net_profit from incrinput where ws_sold_date_sk between '$|start_date|' AND '$|end_date|'
          keys:
            - name: start_date # Incremental load start date (mandatory)
              sql: select 2452641 # SQL to obtain start date (mandatory)
            - name: end_date # Incremental load end date (mandatory)
              sql: select 2452642 # SQL to obtain end date (mandatory)
          state:
            - key: start_date # State key for incremental load (mandatory)
              value: end_date # State value for incremental load (mandatory)

# Transformation Steps configurations (optional)
    steps:
      - sequence:
          - name: top_100_accounts # Sequence name (mandatory)
            doc: this step is to document # Step documentation (optional)
            sql: select * from account_connect limit 100 # SQL for data transformation (mandatory)
            classpath: io.dataos.custom.step.Step.class # Custom logic classpath (optional)
            functions: # Data transformation functions (optional)
              - name: set_type
                columns:
                  account_id: string
            commands: # Commands to execute (optional)
              - name: persist
                sequenceName: account_connect
                mode: MEMORY_AND_DISK

# Output Dataset configurations (optional)
    outputs:
      - name: top_100_accounts # Output dataset name (mandatory)
        dataset: dataos://icebase:bronze/topaccounts?acl=rw # Dataset URI for output (mandatory)
        format: iceberg # Output dataset format (optional, default: based on depot type)
        driver: org.apache.jdbc.psql.Driver # JDBC driver class (optional)
        title: Account # Output dataset title (optional)
        description: Account data from GCD export # Dataset description (optional)
        tags: # Dataset tags (optional)
          - Lookup-Tables
          - Accounts
        options: # Output options (optional)
          saveMode: overwrite # Data save mode (optional, default: overwrite)
          extraOptions:
            branch: b2
            key1: value1
          compressionType: gzip # Compression type (optional)
          sort:
            mode: partition # Sort mode (optional)
            columns:
              - name: version
                order: desc
          iceberg: # Iceberg specific options (optional)
            merge:
              onClause: old.id = new.id
              whenClause: matched then update set * when not matched then insert *
            properties:
              write.format.default: parquet
              write.metadata.compression-codec: gzip
            partitionSpec: # Partition specification (optional)
              - type: identity
                column: version
              - type: day
                column: timestamp
                asColumn: day_partitioned

# Streaming configuration (optional)
    streaming:
      triggerMode: ProcessingTime # Streaming trigger mode (mandatory)
      triggerDuration: 10 seconds # Trigger duration (optional)
      outputMode: append # Output mode for streaming (mandatory)
      checkpointLocation: /tmp/checkpoint # Checkpoint location (mandatory)
      forEachBatchMode: true # Flag for forEachBatchMode (optional)
      extraOptions: # Additional streaming options (optional)
        opt: val

# Assertion configuration (optional)
    assertions:
      - column: order_amount # Target column for assertions (mandatory)
        filter: brand_name == 'Urbane' # Filter condition for assertion (optional)
        validFormat: 
          regex: Awkward # Regular expression for validating format (optional)
        tests: # List of tests to apply (mandatory)
          - avg > 1000.00 # Test for average value (mandatory)
          - max < 1000 # Test for maximum value (mandatory)
          - max > 1000 # Additional test for maximum value (mandatory)
      - sql: | # Custom SQL query for assertions (mandatory)
          SELECT
            AVG(order_amount) AS avg_order_amount,
            MAX(order_amount) AS max_order_amount
          FROM source
          WHERE brand_name = 'Awkward Styles'
        tests: # List of tests to apply on SQL query results (mandatory)
          - avg_order_amount > 1000 # Test for average order amount (mandatory)
          - max_order_amount < 1000 # Test for maximum order amount (mandatory)


# Actions configuraiton
    actions:
      {} # depends on action to be performed

```


Below is the documentation for each attribute in the provided Flare `stackSpec` YAML manifest:


## **`driver`**

**Description:** The `driver` section configures the driver pod in Flare, specifying resource limits such as CPU cores and memory.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | optional | none | driver node resource configuration settings |

**Example Usage:**

```yaml
stackSpec:
  driver:
    coreLimit: 1000m
    cores: 1
    memory: 1024m
```

---

### **`coreLimit`**

**Description:** The `coreLimit` attribute under [`driver`](#driver) sets the maximum CPU resources the driver is allowed to use.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | cpu resource limit (e.g., '1000m') |

**Additional Details:** m stands for "milli," which is a thousandth of a unit. So, 1000m means 1000 milli-units of CPU, which is equivalent to one full CPU core. Here are some possible values and their meanings:

- 500m: Half (0.5) of a CPU core.
- 100m: One-tenth (0.1) of a CPU core.
- 2000m or 2: Two CPU cores.
- 250m: A quarter (0.25) of a CPU core.

**Example Usage:**

```yaml
stackSpec:
  driver:
    coreLimit: 1000m
```

---

### **`cores`**

**Description:** The `cores` attribute defines the number of CPU cores allocated to the driver.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| integer | optional | none | number of CPU cores |

**Example Usage:**

```yaml
stackSpec:
  driver:
    cores: 1
```

---

### **`memory`**

**Description:** The `memory` attribute specifies the amount of memory allocated to the driver.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | memory allocation (e.g., '1024m') |

**Additional details:** m stands for "megabytes." Therefore, 1024m means 1024 megabytes of memory, which is equivalent to 1 gigabyte (GB). Here are some common memory units used in such configurations:

- 1024m or 1Gi: 1 gigabyte (GB) of memory.
- 512m: 512 megabytes of memory.
- 2048m or 2Gi: 2 gigabytes of memory.
- 256m: 256 megabytes of memory.

**Example Usage:**

```yaml
stackSpec:
  driver:
    memory: 1024m
```

---

## **`executor`**

**Description:** The `executor` section configures the executor pods, specifying resources like the number of instances, CPU cores, and memory.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | mandatory | none | executor node resource configuration settings |

**Example Usage:**

```yaml
stackSpec:
  executor:
    coreLimit: 1000m
    cores: 1
    instances: 1
    memory: 1024m
```

---

### **`coreLimit`**

**Description:** Similar to the driver, `coreLimit` in [`executor`](#executor) sets the maximum CPU resources for each executor pod.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | cpu resource limit (e.g., '1000m') |

**Additional Details:** m stands for "milli," which is a thousandth of a unit. So, 1000m means 1000 milli-units of CPU, which is equivalent to one full CPU core. Here are some possible values and their meanings:

- 500m: Half (0.5) of a CPU core.
- 100m: One-tenth (0.1) of a CPU core.
- 2000m or 2: Two CPU cores.
- 250m: A quarter (0.25) of a CPU core.

**Example Usage:**

```yaml
stackSpec:
  executor:
    coreLimit: 1000m
```

---

### **`cores`**

**Description:** The `cores` attribute in [`executor`](#executor) defines the number of CPU cores for each executor pod.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| integer | optional | none | number of CPU cores |

**Example Usage:**

```yaml
stackSpec:
  executor:
    cores: 1
```

---

### **`instances`**

**Description:** The `instances` attribute specifies the number of executor instances to be launched for the job.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| integer | optional | none | number of executor instances |

**Example Usage:**

```yaml
stackSpec:
  executor:
    instances: 1
```

---

### **`memory`**

**Description:** The `memory` attribute in `executor` sets the memory allocation for each executor pod.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | memory allocation (e.g., '1024m') |


**Additional details:** m stands for "megabytes." Therefore, 1024m means 1024 megabytes of memory, which is equivalent to 1 gigabyte (GB). Here are some common memory units used in such configurations:

- 1024m or 1Gi: 1 gigabyte (GB) of memory.
- 512m: 512 megabytes of memory.
- 2048m or 2Gi: 2 gigabytes of memory.
- 256m: 256 megabytes of memory.

**Example Usage:**

```yaml
stackSpec:
  executor:
    memory: 1024m
```

---

## **`job`**

**Description:** Job can be defined as the entities that make up the [Workflow](/resources/workflow/). The `job` section includes various configurations related to job execution, such as logging, explanation mode, and subsections for specific job components.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | none |

**Example Usage:**

```yaml
stackSpec:
  job:
    explain: true
    logLevel: INFO
    streaming: {}
    inputs: {}
    outputs: {}
    steps: {}
    assertions: {}
    actions: {}
```

---


### **`explain`**

**Description:** The `explain` attribute within `job` enables or disables the explanation mode for the job. When set to `true`, it provides detailed insights into the job execution plan.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| boolean | optional | none | true/false |

**Example Usage:**

```yaml
stackSpec:
  job:
    explain: true
```

---

### **`logLevel`**

**Description:** The `logLevel` attribute sets the verbosity level of the logging for the job. Common levels include `INFO`, `DEBUG`, `WARN`, etc.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | INFO / DEBUG / WARN / ERROR |

**Example Usage:**

```yaml
stackSpec:
  job:
    logLevel: INFO
```

---

### **`inputs`**

**Description:** The `inputs` attribute comprises of input dataset configurations for reading data from various depots and data sources. 

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | mandatory | none | input dataset configuration settings |

**Example Usage:**

```yaml
stackSpec:
  job:
    inputs: 
      - name: account_connect
        dataset: dataos://icebase:retail/city
        format: iceberg
        # ...other input configurations
```

---



#### **`name`**

**Description:** The `name` attribute specifies the unique assigned name to the input dataset. It serves as a reference for the input and can be used for querying the input using Spark SQL. Consider this attribute similar to view name in Spark, allowing you to interact with the input data. 

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | any valid identifier string |

**Example Usage:**

```yaml
stackSpec:
  job:
    inputs: 
      - name: account_connect
        # ...other input configurations
```

---

#### **`dataset`**

**Description:** The `dataset` attribute defines the location from which you want to read the data for the input. It is specified using a Uniform Data Link (UDL) address of the dataset.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | any valid dataset UDL, in the following format `dataos://[depot]:[collection]/[dataset]`|

**Additional Details**: For depots created atop, object storages or file storages, you can also load a specific file within the dataset in the following manner, `dataos://gcdexport:none/gcdcore_account/account_x.csv`. 

**Example Usage:**

```yaml
stackSpec:
  job:
    inputs: 
      - dataset: dataos://gcdexport:alpha/gcdcore_account
        # ...other input configurations
```

---

#### **`query`**

**Description:** Flare offers functionality to read data directly from Minerva result sets. Utilizing the `query` attribute, users can import the results of SQL queries executed within the Minerva query engine and make it available as a view in the Flare session. 

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | any valid TrinoSQL query |

**Example Usage:**

```yaml
stackSpec:
  job:
    inputs: 
      - query: SELECT * FROM icebase.retail.city LIMIT 100
        # ...other input configurations
```


---

#### **`format`**

**Description:** The `format` attribute defines the data format of the input, such as CSV, JSON, etc. It determines how the data should be parsed and processed.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | iceberg | iceberg/text/json/parquet/orc/avro/csv/hudi/xml/db/xlsx |

**Example Usage:**

```yaml
stackSpec:
  job:
    inputs: 
      - format: csv
        # ...other input configurations
```

---

#### **`isStream`**

**Description:** The `isStream` attribute indicates whether the input dataset should be read as a stream. A value of `true` signifies that the data will be read as a stream.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| boolean | optional | If not supplied, the default value will be determined based on the depot type. For depot-types based on streaming data source like Kafka, Pulsar and EventHub, the default value is `true`, while for non streaming data source depot-types like GCS and ABFSS, the default value is `false`. | true/false |

**Example Usage:**

```yaml
stackSpec:
  job:
    inputs: 
      - isStream: true
        # ...other input configurations
```

---

#### **`schemaType`**

**Description:** The `schemaType` attribute specifies the type of schema provied in the `schemaPath` or `schemaString` attribute. It defines the structure of the input dataset. 

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | avro | avro / spark |

**Example Usage:**

```yaml
stackSpec:
  job:
    inputs: 
      - schemaType: avro
        # ...other input configurations
```

---

#### **`schemaPath`**

**Description:** The `schemaPath` attribute defines the path of the schema file where the data schema is located. This schema is interpolated within the [`schemaString`](#schemastring attribute when the YAML manifest is applied using the DataOS CLI.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | any valid DataOS UDL file path |

**Example Usage:**

```yaml
stackSpec:
  job:
    inputs: 
      - schemaPath: dataos://thirdparty:none/somedir/someschema.avsc
        # ...other input configurations
```

---

#### **`schemaString`**

**Description:** The `schemaString` attribute contains the actual content of the data schema, typically provided as a string. It's an alternative to `schemaPath` for directly specifying the schema within the YAML manifest.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | valid avro/spark schema in string format |

**Example Usage:**

```yaml
stackSpec:
  job:
    inputs: 
      - schemaString: "schema"
        # ...other input configurations
```

---

#### **`schemaSubject`**

**Description:** The `schemaSubject` attribute defines a subject or topic associated with the schema, often used in systems that manage schemas centrally, like Schema Registry in Kafka.  It can be used to override a subject name to refer to the schema of a Kafka topic in the schema registry when loading Avro data from it.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | any valid subject name |

**Example Usage:**

```yaml
stackSpec:
  job:
    inputs: 
      - schemaSubject: custom-topic-value-schema-name
        # ...other input configurations
```

---

#### **`schemaId`**

**Description:** The `schemaId` attribute specifies the identifier of the schema. This is usually a numeric ID that uniquely identifies the schema version in a schema management system like Kafka schema registry.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| integer | optional | none | any valid integral schema ID |

**Example Usage:**

```yaml
stackSpec:
  job:
    inputs: 
      - schemaId: 2
        # ...other input configurations
```

---

#### **`options`**

**Description:** The `options` attribute provides additional key-value pairs for configuration. These options can be specific to the data source or processing requirements. Flare will iterate over these options and forward each one of them to Spark Operator.

| Data Type | Requirement | Default Value| Possible Value |
| --- | --- | --- | --- |
| mapping | optional | none | any options supported by the underlying Spark connector to load data from the supplied dataset |

**Example Usage:**

```yaml
stackSpec:
  job:
    inputs:
      - options:
          key1: value1
          key2: value2
        # ...other input configurations

```

---

##### **`branch`**

**Description:** The `branch` attribute specifies the particular branch of an Iceberg-format dataset on which operations are to be conducted. It allows for precise targeting of dataset branches for input operations. If omitted, the default behavior is to operate on the `main` branch of the dataset. This attribute is crucial for ensuring that the operations are performed on the correct version of the data.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | main | any valid branch name |

**Example Usage:**

For input datasets:
```yaml
inputs:
  - name: sanity_city_input
    dataset: dataos://icebase:retail/city
    format: Iceberg
    options:
      branch: b1
  # ...other input attributes
```

---

#### **`incremental`**

**Description:** The `incremental` attribute contains configurations for reading data incrementally (or incremental job). This includes the context, SQL for incremental extraction, keys for incremental processing, and state management. This is particularly useful when dealing with large datasets and performing incremental updates.


| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | optional, mandatory (for incremental processing) | none | valid incremental read configuraiton |

**Example Usage:**

```yaml
stackSpec:
  job:
    inputs:
      - incremental:
          context: incrinput
          sql: SELECT ws_sold_date_sk , ws_sold_time_sk , ws_item_sk, ws_bill_customer_sk , ws_web_page_sk ,ws_ship_mode_sk, ws_order_number, ws_quantity,ws_list_price ,ws_sales_price , ws_wholesale_cost  , ws_net_profit from incrinput where ws_sold_date_sk between '$|start_date|' AND '$|end_date|'
          keys:
            - name: start_date
              sql: select 2452641
            - name: end_date
              sql: select 2452642
          state:
            - key: start_date
              value: end_date
        # ...other input configurations
```

##### **`context`**

**Description:** The `context` attribute specifies the context or environment used for incremental data processing. It typically refers to a specific dataset or a database view.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory (for incremental processing) | none | any valid context identifier in string format |

**Example Usage:**

```yaml
stackSpec:
  job:
    inputs:
      - incremental:
          context: incrinput
          # ...other incremental configurations
```

---

##### **`sql`**

**Description:** The `sql` attribute contains the SQL query used for incremental data retrieval. This query defines how data should be fetched based on incremental changes.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory (for incremental processing) | none | any valid SQL query |

**Example Usage:**

```yaml
stackSpec:
  job:
    inputs:
      - incremental:
          sql: SELECT ws_sold_date_sk, ws_sold_time_sk, ws_item_sk, ws_bill_customer_sk, ws_web_page_sk, ws_ship_mode_sk, ws_order_number, ws_quantity, ws_list_price,ws_sales_price, ws_wholesale_cost, ws_net_profit FROM incrinput WHERE ws_sold_date_sk BETWEEN '$|start_date|' AND '$|end_date|'
          # ...other incremental configurations
```

---

##### **`keys`**

**Description:** The `keys` attribute defines a list of key configurations used in incremental processing. Each key includes a name and an associated SQL query for determining its value.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of mappings | mandatory (for incremental processing) | none | valid key configurations |

**Example Usage:**

```yaml
stackSpec:
  job:
    inputs:
      - incremental:
          keys:
            - name: start_date
              sql: select 2452641
            - name: end_date
              sql: select 2452642
          # ...other incremental configurations
```

---

###### **`name`**

**Description:** The `name` attribute within `keys` specifies the identifier for the key used in incremental processing.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory (for incremental processing) | none | any valid key name |

**Example Usage:**

```yaml
stackSpec:
  job:
    inputs:
      - incremental:
          keys:
            - name: start_date
          # ...other incremental configurations
```

---

###### **`sql`**

**Description:** The `sql` attribute within `keys` provides the SQL query used to determine the value of the corresponding incremental key.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory (for incremental processing) | none | any valid SQL query |

**Example Usage:**

```yaml
stackSpec:
  job:
    inputs:
      - incremental:
          keys:
            - sql: select 2452641
          # ...other incremental configurations
```

---

##### **`state`**

**Description:** The `state` attribute contains key-value pairs for managing the state in incremental processing. Each state entry includes a key and its corresponding value, which are used to track and manage the state of incremental data retrieval.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of mappings | mandatory (for incremental processing) | none | valid state management configuraiton |

**Example Usage:**

```yaml
stackSpec:
  job:
    inputs:
      - incremental:
          state:
            - key: start_date
              value: end_date
          # ...other incremental configurations
```

---

###### **`key`**

**Description:** The `key` attribute within `state` specifies the key for the state used in incremental processing.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory (for incremental processing) | none | any valid key name |

**Example Usage:**

```yaml
stackSpec:
  job:
    inputs:
      - incremental:
          state:
            - key: start_date
          # ...other incremental configurations
```

---

###### **`value`**

**Description:** The `value` attribute within `state` provides the value to determine the value of the corresponding incremental key.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory (for incremental processing) | none | any valid SQL query |

**Example Usage:**

```yaml
stackSpec:
  job:
    inputs:
      - incremental:
          state:
            - value: end_date
          # ...other incremental configurations
```



---

### **`outputs`**


**Description:** The `outputs` attribute comprises of output dataset configurations for writing data from various depots and data sources. 

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | opitional | none | input dataset configuration settings |

**Example Usage:**

```yaml
stackSpec:
  job:
    inputs: 
      - name: account_connect
        dataset: dataos://icebase:retail/city
        format: iceberg
        # ...other input configurations
```


#### **`name`**

**Description:** The `name` attribute specifies the unique identifier for the output dataset you want to sink as an output dataset. If only inputs are provided and no steps are defined, the output `name` should coincide with the input `name`. However, if steps are included in the configuration, the name of the output should be the same as the step `name` to be sinked. 

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | any valid identifier string |

**Example Usage:**

```yaml
stackSpec:
  job:
    outputs:
      - name: top_100_accounts
```

---

#### **`dataset`**

**Description:** The `dataset` attribute defines the destination for the output dataset, referred by output `name`. It is specified as a DataOS Uniform Data Link (UDL) address that points to the dataset location. To prevent conflicts and maintain the directed acyclic nature of Flare, the output dataset address must differ from the input `dataset` address, avoiding any cyclic dependencies.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | any valid UDL address except the input dataset address |

**Example Usage:**

```yaml
stackSpec:
  job:
    outputs:
      - dataset: dataos://icebase:bronze/topaccounts?acl=rw
```

---

#### **`format`**

**Description:** The `format` attribute defines the data format of the output, such as Iceberg, JSON, etc. It determines how the data should be structured and stored.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | based on output depot-type | iceberg/parquet/json/kafkaavro/kafkajson/pulsar/bigquery |

**Example Usage:**

```yaml
stackSpec:
  job:
    outputs:
      - format: iceberg
```

---

#### **`driver`**

**Description:** The `driver` attribute specifies the JDBC driver used to interact with the database. It is essential for connecting to and executing commands on the database. It can be used to override the default driver class. 

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | org.apache.jdbc.psql.Driver | any valid JDBC driver class name |

**Example Usage:**

```yaml
stackSpec:
  job:
    outputs:
      - driver: org.apache.jdbc.psql.Driver
```

---

#### **`title`**

**Description:** The `title` attribute provides a human-readable title for the output dataset. It is used for identification and description purposes in graphical user interfaces.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | any descriptive title in string format |

**Example Usage:**

```yaml
stackSpec:
  job:
    outputs:
      - title: Account
```

---

#### **`description`**

**Description:** The `description` attribute gives a detailed explanation of the output dataset. It helps in understanding the context and contents of the dataset.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | any descriptive text in string format |

**Example Usage:**

```yaml
stackSpec:
  job:
    outputs:
      - description: Account data from GCD export
```

---

#### **`tags`**

**Description:** The `tags` attribute is used for adding metadata tags to the output dataset. These tags assist in categorization, searching, and organization within DataOS.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of strings | optional | none | any valid tags |

**Example Usage:**

```yaml
stackSpec:
  job:
    outputs:
      - tags:
        - Lookup-Tables
        - Accounts
      # ...additional output configurations
```

---

#### **`options`**

**Description:** The `options` attribute includes additional configuration settings specific to the output. This can include save modes, compression types, and other relevant options.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | optional | none | any option supported by the underlying Spark data source connector |

**Example Usage:**

```yaml
stackSpec:
  job:
    outputs:
      - options:
          saveMode: overwrite
          # Additional options...
```

---

##### **`saveMode`**

**Description:** The `saveMode` option under `options` determines how the output data is saved, such as 'overwrite', 'append', etc.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | overwrite | overwrite, append |

**Example Usage:**

```yaml
stackSpec:
  job:
    outputs:
      - options:
          saveMode: overwrite
```

---

##### **`extraOptions`**

**Description:** The `extraOptions` under `options` provide a way to specify additional, more detailed configuration settings. These might include custom parameters relevant to the data output process.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | optional | none | key-value pairs for extra options |

**Example Usage:**

```yaml
stackSpec:
  job:
    outputs:
      - options:
          extraOptions:
            key1: value1
            # Additional extra options...
```

---

###### **`branch`**

**Description:** The `branch` attribute specifies the particular branch of an Iceberg-format dataset on which operations are to be conducted. It allows for precise targeting of dataset branches for output operations. If omitted, the default behavior is to operate on the `main` branch of the dataset. This attribute is crucial for ensuring that the operations are performed on the correct version of the data.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | main | any valid branch name |

**Example Usage:**

For output datasets:
```yaml
outputs:
  - name: cities
    dataset: dataos://icebase:retail/city_01
    format: ICEBERG
    options:
      extraOptions:
        branch: b2
      saveMode: append
  # ...other output attributes
```

---

##### **`compressionType`**

**Description:** The `compressionType` option specifies the type of compression to be applied to the output data, like 'gzip', 'snappy', etc.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | gzip | gzip/snappy |

**Example Usage:**

```yaml
stackSpec:
  job:
    outputs:
      - options:
          compressionType: gzip
```

---

##### **`sort`**

**Description:** The `sort` option provides configurations related to sorting the output data. This includes the sorting mode and the columns to sort by.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | optional | none | sorting configuration attributes |

**Example Usage:**

```yaml
stackSpec:
  job:
    outputs:
      - options:
          sort:
            mode: partition
            # Additional sorting configurations...
```

---

###### **`mode`**

**Description:** The `mode` attribute under `sort` defines how the sorting should be executed, such as 'partition' etc. 

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | partition / global |

**Additional Details:** In `partition` mode, chunk of data or logical division of data are stored on a node in the cluster in Iceberg kind of dataset.

**Example Usage:**

```yaml
stackSpec:
  job:
    outputs:
      - options:
          sort:
            mode: partition
```

---

###### **`columns`**

**Description:** The `columns` attribute under `sort` specifies the columns to be used for sorting and their respective sort order.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of mappings | mandatory | none | column names and order settings |

**Example Usage:**

```yaml
stackSpec:
  job:
    outputs:
      - options:
          sort:
            columns:
              - name: version
                order: desc
```

---


#### **`iceberg`**

**Description:** The `iceberg` attribute contains configurations specific to Apache Iceberg, a table format for large analytic datasets. This section includes settings for merge operations, properties, and partition specifications. These configurations are crucial when the output format is set to `iceberg` and determine how the data is stored, partitioned, and managed within an Iceberg table.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | optional | none | iceberg-specific configuration settings |

**Example Usage:**

```yaml
stackSpec:
  job:
    outputs:
      - iceberg:
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

---

##### **`merge`**

**Description:** The `merge` attribute within `iceberg` defines the merge strategy for handling data updates and inserts. It includes an `onClause` for matching records and a `whenClause` to specify actions for matched and unmatched records. This setting is essential for defining how existing data is updated or new data is appended in Iceberg tables.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | optional | none | merge strategy settings |

**Example Usage:**

```yaml
stackSpec:
  job:
    outputs:
      - iceberg:
          merge:
            onClause: old.id = new.id
            whenClause: matched then update set * when not matched then insert *
```

---


###### **`onClause`**

**Description:** The `onClause` attribute within the `merge` section of `iceberg` defines the condition used to match records in the merge operation. It's typically a SQL-like expression used to identify matching records between the source and target tables.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | sql-like matching condition |

**Example Usage:**

```yaml
stackSpec:
  job:
    outputs:
      - iceberg:
          merge:
            onClause: old.id = new.id
```

---

###### **`whenClause`**

**Description:** The `whenClause` attribute within the `merge` section of `iceberg` specifies the actions to be taken when records match or do not match the condition specified in `onClause`. It determines how matched and unmatched records are handled during the merge operation.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | sql-like action definitions |

**Example Usage:**

```yaml
stackSpec:
  job:
    outputs:
      - iceberg:
          merge:
            whenClause: matched then update set * when not matched then insert *
```

---


##### **`properties`**

**Description:** The `properties` attribute within `iceberg` specifies various Iceberg table settings, like default write format and metadata compression codec. These properties optimize how the data is stored and accessed in the Iceberg table.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | optional | none | iceberg table property settings |

**Example Usage:**

```yaml
stackSpec:
  job:
    outputs:
      - iceberg:
          properties:
            write.format.default: parquet
            write.metadata.compression-codec: gzip
```

---

###### **`write.format.default`**

**Description:** This attribute sets the default format for writing data in the Iceberg table, such as 'parquet' or 'avro'. It affects how data is serialized and stored.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | pqrquet | parquet, avro, etc. |

**Example Usage:**

```yaml
stackSpec:
  job:
    outputs:
      - iceberg:
          properties:
            write.format.default: parquet
```

---

###### **`write.metadata.compression-codec`**

**Description:** This attribute specifies the compression codec to be used for the metadata files in the Iceberg table, like 'gzip' or 'snappy'.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | gzip | gzip/snappy |

**Example Usage:**

```yaml
stackSpec:
  job:
    outputs:
      - iceberg:
          properties:
            write.metadata.compression-codec: gzip
```

---

##### **`partitionSpec`**

**Description:** The `partitionSpec` attribute within `iceberg` configures how data in the Iceberg table is partitioned. It includes a list of partition fields, each with a `type` and `column`, and potentially an alias (`asColumn`). Partitioning is crucial for optimizing data retrieval and storage efficiency.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of mappings | optional | none | partition specification settings |

**Example Usage:**

```yaml
stackSpec:
  job:
    outputs:
      - iceberg:
          partitionSpec:
            - type: identity
              column: version
            - type: day
              column: timestamp
              asColumn: day_partitioned
```

###### **`type`**

**Description:** The `type` attribute within each entry of `partitionSpec` specifies the partitioning method to be applied to the column, such as 'identity', 'day', etc.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | identity, day, etc. |

**Example Usage:**

```yaml
stackSpec:
  job:
    outputs:
      - iceberg:
          partitionSpec:
            - type: identity
```

---

###### **`column`**

**Description:** The `column` attribute within `partitionSpec` identifies the column in the Iceberg table that will be used for partitioning.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | any valid column name in the table |

**Example Usage:**

```yaml
stackSpec:
  job:
    outputs:
      - iceberg:
          partitionSpec:
            - column: version
```

---

###### **`asColumn`**

**Description:** The `asColumn` attribute in `partitionSpec` provides an alias for the partitioned column, allowing for renaming or redefining the partition column in the output dataset.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | any valid column name |

**Example Usage:**

```yaml
stackSpec:
  job:
    outputs:
      - iceberg:
          partitionSpec:
            - asColumn: day_partitioned
```

---


### **`steps`**

**Description:** specifies Flare transformation attributes. This may include one or more sequences to execute the steps defined for performing any transformation or applying any Flare function or command.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of mappings | mandatory | none | transformation step configurations |

**Example Usage:**

```yaml
stackSpec:
  job:
    steps:
      - sequence:
        # Additional steps configurations...
```

---


#### **`sequence`**

**Description:** The `sequence` attribute within `steps` defines an ordered list of operations or transformations to be performed on the dataset. Each item in the sequence represents a distinct step with its specific configuration. One can add multiple such sequences. Each intermediate step in a sequence can be envisioned as an action that results in a view that can be referred to in subsequent steps or outputs. 

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of mappings | mandatory | none | sequence configurations |

**Example Usage:**

```yaml
stackSpec:
  job:
    steps:
      - sequence:
          - name: top_100_accounts
            # Additional step configurations...
```

---

##### **`name`**

**Description:** The `name` attribute within each step of `sequence` provides a unique identifier for the step. It is used to reference and describe a view created as a result of a specific set of transformation being applied. The value of the step `name` attribute can be supplied to the output `name` to sink it.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | any valid step name |

**Example Usage:**

```yaml
stackSpec:
  job:
    steps:
      - sequence:
          - name: top_100_accounts
```

---

##### **`doc`**

**Description:** The `doc` attribute offers a brief description of the step, explaining its purpose or the operation it performs. It serves as documentation to clarify the role of this step in the sequence.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | descriptive text about the step |

**Example Usage:**

```yaml
stackSpec:
  job:
    steps:
      - sequence:
          - doc: this step is to document
```

---

##### **`sql`**

**Description:** The `sql` attribute contains the SQL query executed in the step. This query defines the data processing or transformation logic for that specific step.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | any valid SQL query |

**Example Usage:**

```yaml
stackSpec:
  job:
    steps:
      - sequence:
          - sql: select * from account_connect limit 100
```

---

##### **`sqlFile`**

**Description:** The sqlFile attribute specifies the path to an SQL file containing transformation queries.The sql snippets are interpolated within the `sql` attribute when the YAML manifest is applied using the DataOS CLI. This feature enables clean code separation and efficient management of complex SQL transformations.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | any valid SQL file path |

**Example Usage:**

```yaml
stackSpec:
  job:
    steps:
      - sequence:
          - sqlFile: transformation/data-product/mycode.sql
```

---

##### **`classpath`**

**Description:** The `classpath` attribute specifies the classpath of the Java or Scala class that implements the step's logic. It is essential for steps that involve custom processing logic.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | fully-qualified class name |

**Example Usage:**

```yaml
stackSpec:
  job:
    steps:
      - sequence:
          - classpath: io.dataos.custom.step.Step.class
```

---

##### **`functions`**

**Description:** The `functions` attribute within a step defines a list of functions to be applied to the data. Each function has a name and specific settings like column types.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of mappings | optional | none | any custom or valid Flare functions provided in the document: [Flare Functions](/resources/stacks/flare/functions/). |

**Example Usage:**

```yaml
stackSpec:
  job:
    steps:
      - sequence:
          - functions:
              - name: set_type
                columns:
                  account_id: string
```

---


###### **`name`**

**Description:** The `name` attribute within [`functions`](#functions) specifies the name of the function to be applied. This name identifies the particular transformation or operation function being invoked.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | any valid function name from amongst the following [Flare Functions](/resources/stacks/flare/functions/).|

**Example Usage:**

```yaml
stackSpec:
  job:
    steps:
      - sequence:
          - functions:
              - name: set_type
```

---

###### **`columns`**

**Description:** The `columns` attribute within [`functions`](#functions) defines the columns to which the function will be applied, along with their expected data types. It maps each column name to its respective data type.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | optional | none | column name and data type pairs |

**Example Usage:**

```yaml
stackSpec:
  job:
    steps:
      - sequence:
          - functions:
              - columns:
                  account_id: string
```

---

##### **`commands`**

**Description:** The `commands` attribute specifies a series of commands or actions to be executed as part of the step. Each command has its name, associated sequence name, and other relevant settings.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of mappings | optional | none | command configurations |

**Example Usage:**

```yaml
stackSpec:
  job:
    steps:
      - sequence:
          - commands:
              - name: persist
                sequenceName: account_connect
                mode: MEMORY_AND_DISK
```


---

###### **`name`**

**Description:** The `name` attribute within [`commands`](#commands) identifies the specific command or action to be executed in the step. This name reflects the purpose or effect of the command.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | persist / unpersist |

**Example Usage:**

```yaml
stackSpec:
  job:
    steps:
      - sequence:
          - commands:
              - name: persist
```

---

###### **`sequenceName`**

**Description:** The `sequenceName` attribute in `commands` refers to the name of the sequence (or step) to which the command applies. It links the command to a specific part of the step sequence.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | name of an existing sequence or step |

**Example Usage:**

```yaml
stackSpec:
  job:
    steps:
      - sequence:
          - commands:
              - sequenceName: account_connect
```

---

###### **`mode`**

**Description:** The `mode` attribute within `commands` specifies how data should be persisted or handled during execution, such as 'MEMORY_AND_DISK', 'DISK_ONLY', etc. This setting impacts the performance and reliability of the data processing.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | MEMORY_AND_DISK, DISK_ONLY, etc. |

**Example Usage:**

```yaml
stackSpec:
  job:
    steps:
      - sequence:
          - commands:
              - mode: MEMORY_AND_DISK
```

---


### **`streaming`**


**Description:** The `streaming` attribute contains configurations specific to streaming data processing. This section includes settings for trigger mode and duration, output mode, checkpoint location, batch processing, and other extra options related to streaming.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | optional | none | Streaming configuration settings |

**Example Usage:**

```yaml
stackSpec:
  job:
    streaming:
      triggerMode: ProcessingTime
      triggerDuration: 10 seconds
      outputMode: append
      checkpointLocation: /tmp/checkpoint
      forEachBatchMode: true
      extraOptions:
        opt: val
```

---

#### **`triggerMode`**

**Description:** The `triggerMode` attribute specifies the mode of triggering in streaming processing. Common modes include 'ProcessingTime', 'OneTime', etc.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | ProcessingTime, OneTime, etc. |

**Example Usage:**

```yaml
stackSpec:
  job:
    streaming:
      triggerMode: ProcessingTime
```

---

#### **`triggerDuration`**

**Description:** The `triggerDuration` attribute sets the interval at which streaming data will be processed. It is often specified in time units like seconds, minutes, etc.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | Time duration (e.g., '10 seconds', '5 minutes') |

**Example Usage:**

```yaml
stackSpec:
  job:
    streaming:
      triggerDuration: 10 seconds
```

---

#### **`outputMode`**

**Description:** The `outputMode` attribute defines how the results of a streaming query are written to the output sink. Common modes include 'append', 'complete', 'update', etc.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | append, complete, update |

**Example Usage:**

```yaml
stackSpec:
  job:
    streaming:
      outputMode: append
```

---

#### **`checkpointLocation`**

**Description:** The `checkpointLocation` attribute specifies the path where the streaming process will save checkpoints. Checkpoints are used for fault tolerance and recovery in streaming processing.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | any valid file system path |

**Example Usage:**

```yaml
stackSpec:
  job:
    streaming:
      checkpointLocation: /tmp/checkpoint
```

---

#### **`forEachBatchMode`**

**Description:** The `forEachBatchMode` attribute indicates whether to process each batch of streaming data separately. When set to `true`, it enables individual handling of each data batch.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| boolean | optional | none | true/false |

**Example Usage:**

```yaml
stackSpec:
  job:
    streaming:
      forEachBatchMode: true
```

---

#### **`extraOptions`**

**Description:** The `extraOptions` attribute provides a way to specify additional, custom configuration settings relevant to the streaming process.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | optional | none | key-value pairs for extra options |

**Example Usage:**

```yaml
stackSpec:
  job:
    streaming:
      extraOptions:
        opt: val
```

---


### **`assertions`**

**Description:** Assertions refer to validation rules that are tailored to a particular business domain and serve to determine the fitness-for-purpose of datasets. The application of assertions enables the execution of additional validation checks on top of existing datasets, thereby enhancing their overall quality. The `assertions` attribute contains a list of checks or tests to be applied to data columns or SQL queries. 

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of mappings | optional | none | assertion configurations |

**Example Usage:**

```yaml
stackSpec:
  job:
    assertions:
      - column: order_amount
        filter: brand_name == 'Urbane'
        validFormat:
          regex: Awkward
        tests:
          - avg > 1000.00
          - max < 1000
          - max > 1000
      - sql: |
          SELECT
            AVG(order_amount) AS avg_order_amount,
            MAX(order_amount) AS max_order_amount
          FROM source
          WHERE brand_name = 'Awkward Styles'
        tests:
          - avg_order_amount > 1000
          - max_order_amount < 1000
```

---

#### **`column`**

**Description:** The `column` attribute specifies the column name on which the assertions will be applied. It is used when assertions are column-based.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | Any valid column name |

**Example Usage:**

```yaml
stackSpec:
  job:
    assertions:
      - column: order_amount
```

---

##### **`filter`**

**Description:** The `filter` attribute is used to apply a conditional filter to the column specified in `column`. It filters data based on the provided condition.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | SQL-like conditional filter |

**Example Usage:**

```yaml
stackSpec:
  job:
    assertions:
      - column: order_amount
        filter: brand_name == 'Urbane'
```

---

#### **`validFormat`**

**Description:** The `validFormat` attribute defines the format or pattern that the data in the specified column should adhere to. It's often used to ensure data consistency and format correctness.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | optional | none | Format validation settings |

**Example Usage:**

```yaml
stackSpec:
  job:
    assertions:
      - column: order_amount
        validFormat:
          regex: Awkward
```

---

##### **`regex`**

**Description:** The `regex` attribute within `validFormat` specifies a regular expression that the data in the specified column should match. This is used to validate that the data follows a particular pattern or format.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | Any valid regular expression |

**Example Usage:**

```yaml
stackSpec:
  job:
    assertions:
      - column: order_amount
        validFormat:
          regex: Awkward
```

---

#### **`tests`**

**Description:** The `tests` attribute under assertions lists the conditions or tests that data must pass. These are specified as expressions and are used to validate various aspects of the data.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of strings | mandatory | none | Test expressions |

**Additional details:**

| Function | Description | Example |
| --- | --- | --- |
| `avg` | The avg function returns the average of a column. | `avg > 1000.00` |
| `avg_length` | The avg_length function returns the average length of the column value. | `avg_length < 12` |
| `distinct_count` | The distinct_count function returns the count of the distinct values of a column. | `distinct_count > 10` |
| `duplicate_count` | The duplicate_count function returns the count of duplicate values in the column. | `duplicate_count < 11` |
| `min` | The min function returns the minimum value of a column. | `min > 100` |
| `max` | The max function returns the maximum value of a column. | `max < 1000` |
| `max_length` | The max_length function returns the maximum length of the column value. | `max_length < 20` |
| `min_length` | The min_length function returns the minimum length of the column value. | `min_length > 30` |
| `missing_count` | The missing_count function returns the count of missing values in the column. | `missing_count < 5` |
| `missing_percentage` | The missing_percentage function returns the rate of missing values in the column. | `missing_percentage < 0.1` |
| `sum` | The sum function returns the total sum of the column value. | `sum > 500` |

**Example Usage:**

```yaml
stackSpec:
  job:
    assertions:
      - column: order_amount
        tests:
          - avg > 1000.00
          - max < 1000
```

---

#### **`sql`**

**Description:** The `sql` attribute allows defining a SQL query for complex data checks. The results of this query are then used in the `tests`.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | Any valid SQL query |

**Example Usage:**

```yaml
stackSpec:
  job:
    assertions:
      - sql: |
          SELECT
            AVG(order_amount) AS avg_order_amount,
            MAX(order_amount) AS max_order_amount
          FROM source
          WHERE brand_name = 'Awkward Styles'
```

---



### **`actions`**

**Description:** Maintenance of any Iceberg table is challenging; therefore, DataOS internal depot Icebase gives users in-built capabilities to manage and maintain metadata files and data. In DataOS, these operations can be performed using Flare stack. This service in Flare is offered through `actions` attribute. 

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of mappings | optional | none | action configuration settings |

**Additional details:** The Data Maintenance Actions are only supported in depots with Iceberg datasets. For e.g. Icebase. Following are the different actions that can be accomplished using Flare in DataOS:

- [`rewrite_dataset`](#rewrite_dataset)
- [`rewrite_manifest`](#rewrite_manifest)
- [`expire_snapshots`](#expire_snapshots)
- [`remove_orphans`](#remove_orphans)
- [`delete_from_dataset`](#delete_from_dataset)

**Example Usage:**

```yaml
stackSpec:
  job:
    actions:
      # ... attribute specific to Flare Action
```


The configurations for the different actions and their definitions are provided in the below section:

#### **`rewrite_dataset`**

> Supported in Flare Stack Version `flare:4.0`.
> 

Iceberg format within Icebase depots tracks each data file in a table. More data files lead to more metadata stored in manifest files, and small data files cause an unnecessary amount of metadata and less efficient queries from file open costs. 

The data files can be compacted in parallel within Icebase depots using Flare’s `rewrite_dataset` action. This will combine small files into larger files to reduce metadata overhead and runtime file open costs. The `rewrite_dataset` action definition for `flare:4.0` is given below:

```yaml
actions:
  - name: rewrite_dataset # Name of the Action
    input: <input-dataset-name> # Input dataset name
    options: # Options
      properties: # Properties
        "target-file-size-bytes": "<target-file-size>" # Target File Size in Bytes
```

The `rewrite_dataset` action is beneficial in the case of streaming, where small data files can be compacted into larger files to improve query performance. To explore a case scenario on how to compact files using the `rewrite_dataset` action, click [here.](/resources/stacks/flare/case_scenario/rewrite_dataset/)

---

#### **`rewrite_manifest`**

> Supported in Flare Stack Version `flare:4.0`.
> 

DataOS internal depot, Icebase uses metadata in its manifest list and manifest files to speed up query planning and to prune unnecessary data files. Some tables can benefit from rewriting manifest files to make locating data for queries much faster. The metadata tree functions as an index over a table’s data. Manifests in the metadata tree are automatically compacted in the order they are added, which makes queries faster when the write pattern aligns with read filters. For example, writing hourly-partitioned data as it arrives is aligned with time-range query filters. The `rewrite_manifest` action definition for `flare:4.0` is given below:

```yaml
actions:
  - name: rewrite_manifest # Name of the Action
    input: <input-dataset-name> # Input Dataset Name
```

A case scenario illustrating the implementation of the `rewrite_manifest` action is given [here.](/resources/stacks/flare/case_scenario/rewrite_manifest_files/)

---

#### **`expire_snapshots`**

> Supported in Flare Stack Version `flare:4.0`
> 

Each write to an Iceberg table within Icebase depots creates a new snapshot, or version, of a table. Snapshots can be used for time-travel queries, or the table can be rolled back to any valid snapshot. Snapshots accumulate until they are expired by Flare’s `expire_snapshots` action. The `expire_snapshots` action definition for `flare:4.0` is as follows:

```yaml
actions:
  - name: expire_snapshots # Name of the Action
    input: <input-dataset-name> # Input Dataset Name
    options: # Options
      expireOlderThan: "<date-in-unix-format-as-a-string>" # Timestamp in Unix Format (All Snapshots older than timestamp are expired)
```

Regularly expiring snapshots is recommended to delete data files that are no longer needed, and to keep the size of table metadata small. To view a case scenario for `expire_snapshots` action, click [here.](/resources/stacks/flare/case_scenario/expire_snapshots/)

---

#### **`remove_orphans`**

> Supported in Flare Stack Version `flare:4.0`.
> 

While executing Flare Jobs upon Icebase depots, job failures can leave files that are not referenced by table metadata, and in some cases, normal snapshot expiration may not be able to determine if a file is no longer needed and delete it.

To clean up these ‘orphan’ files under a table location older than a specified timestamp, we can use Flare’s `remove_orphans` action. The below code block shows the definition for `remove_orphans` action for `flare:4.0`:

```yaml
actions:
  - name: remove_orphans # Name of Action
    input: <input-dataset-name> # Name of Input Dataset
    options: # Options
      olderThan: "<timestamp>" # Time to be provided in Unix Format
```

Click [here](/resources/stacks/flare/case_scenario/remove_orphans/) to view a case scenario depicting the use of `remove_orphans` action.

---

#### **`delete_from_dataset`**

> Supported in Flare Stack Version `flare:4.0`only.
> 

The `delete_from_dataset` action removes data from tables. The action accepts a filter provided in the `deleteWhere` property to match rows to delete. If the delete filter matches entire partitions of the table, Iceberg format within the Icebase depot will perform a metadata-only delete. If the filter matches individual rows of a table, then only the affected data files will be rewritten. The syntax of the `delete_from_dataset` action is provided below:

```yaml
actions:
  - name: delete_from_dataset # Name of the Action
    input: <input-dataset-name> # Input Dataset Name
    deleteWhere: "<condition>" # Delete where the provided condition is true
```

The `delete_from_dataset` can be used in multiple configurations, which have been showcased in the case scenarios [here.](/resources/stacks/flare/case_scenario/delete_from_dataset/)

<aside class="callout">

🗣️ When using a GCS-based environment, use the dataset address with the <code>acl=rw</code> query parameter (e.g. <code>dataos://icebase:actions/random_users_data?acl=rw</code>). This is because GCS generates two credentials with different permissions: one with only read access and one with both read and write access. Flare actions need write access to create files, so if you don't specify <code>acl=rw</code>, Flare will default to read-only access and prevent you from updating or creating files.

```yaml
inputs:
  - name: inputDf
    dataset: dataos://icebase:actions/random_users_data?acl=rw
    format: Iceberg
```

</aside>