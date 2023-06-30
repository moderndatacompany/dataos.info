# Steps

In the `steps` section, a series of sequences are defined to execute the necessary actions for performing transformations or applying Flare Functions and SQL queries.

## Structure of Steps Section

```yaml
steps:
  - sequence:
    - name: top_100_accounts
      doc: this step is to document
      sql: select * from account_connect limit 100
      classpath: io.dataos.custom.step.Step.class
      functions:
        - name: set_type
          columns:
            account_id: string
      commands:
        - name: persist
          sequenceName: account_connect
          mode: MEMORY_AND_DISK
```



| Property | Description | Example | Default Value | Possible Values | Note/Rule | Field (Mandatory / Optional) |
| --- | --- | --- | --- | --- | --- | --- |
| sequence | Sequences contain a list of steps to be executed in a sequential manner. One can add multiple such sequences. One can envision each intermediate step in a sequence as an action that results in a view that can be referred to in subsequent steps or outputs. In this section, flare will try to run supplied SQL and associated functions and commands. | sequence:
     - name: transformation-1 # Name of the first transformation step
       sql: select * from account limit 10 # sql transformation
     - name: transformation-2 # Name of the second transformation step
       sql: select * from account limit 30 # sql transformation | NA | NA | NA | Mandatory |
| name | Preferred name for your sequence  | - name: top_100_accounts | NA | NA | NA | Mandatory |
| doc | Description of SQL/transformation | doc: this step is to document | NA | NA | NA | Optional |
| sql | SQL steps to transform your data. | sql: select * from account_connect limit 100 | iceberg | iceberg/text/json/parquet/orc/avro/csv/xml | NA | Mandatory |
| classpath | Custom logic/step implemented by the user and present in the classpath. | classpath: io.dataos.custom.step.Step.class | Depends on Depot Type | true /false | If value is not supplied we default it to true/false based on the depot type e.g. for depots like kafka and eventhub it is true and for gcs/abfss etc it is false. | Optional |
| functions | Flare functions like drop_column, any_date,
change_case, etc. To know more click ../Flare%20Functions%206bab680519a1428da65857910201fb00.md | functions:
     - name: set_type # Name of the Flare Function
       columns:
       account_id: string # Column and data type in column | NA | Check the ../Flare%20Functions%206bab680519a1428da65857910201fb00.md for available functions  | NA | Optional |
| commands | There are two commands available persist and unpersist. | commands:
    - name: persist
      sequenceName: account_connect
      mode: MEMORY_AND_DISK | NA | persist/unpersist | NA | Optional |