# Steps

In the `steps` section, a series of sequences are defined to execute the necessary actions for performing transformations or applying Flare Functions and SQL queries.

## Structure of Steps Section

```yaml
steps:  
  - sequence: 
      - name: top_100_accounts #(Mandatory)
				doc: this step is to document #(Optional)
        sql: select * from account_connect limit 100 #(Mandatory)
				classpath: io.dataos.custom.step.Step.class #(Optional)
        functions: #(Optional)
					# Name of function. You can refer signature of every function in flare function docs.
          - name: set_type
            columns:
              account_id: string
				# (Optional) There are two commands available persist and unpersist.
				commands: #(Optional)
					- name: persist
						sequenceName: account_connect
						mode: MEMORY_AND_DISK
```

| Property | Description | Example | Default Value | Possible Values | Note/Rule | Field (Mandatory / Optional) |
| --- | --- | --- | --- | --- | --- | --- |
| `sequence` | Sequences contain a list of steps to be executed in a sequential manner. One can add multiple such sequences. One can envision each intermediate step in a sequence as an action that results in a view that can be referred to in subsequent steps or outputs. In this section, flare will try to run supplied SQL and associated functions and commands. | `sequence:` <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `- name: transformation-1` <span style="color:green"> # Name of the first transformation step</span> <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `sql: select * from account limit 10` <span style="color:green"> # sql transformation</span> <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `- name: transformation-2` <span style="color:green"> # Name of the second transformation step </span> <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  `sql: select * from account limit 30`<span style="color:green"> # sql transformation</span> | NA | NA | NA | Mandatory |
| `name` | Preferred name for your sequence  | `- name: top_100_accounts` | NA | NA | NA | Mandatory |
| `doc` | Description of SQL/transformation | `doc: this step is to document` | NA | NA | NA | Optional |
| `sql` | SQL steps to transform your data. | `sql: select * from account_connect limit 100` | `iceberg` | `iceberg`/`text`/`json`/`parquet`/`orc`/`avro`/`csv`/`xml` | NA | Mandatory |
| `classpath` | Custom logic/step implemented by the user and present in the classpath. | `classpath: io.dataos.custom.step.Step.class` | Depends on Depot Type | `true` /`false` | If value is not supplied we default it to `true`/`false` based on the depot type e.g. for depots like kafka and eventhub it is true and for gcs/abfss etc it is false. | Optional |
| `functions` | Flare functions like `drop_column`, `any_date`,`change_case`, etc. To know more, refer to [Flare Functions](../Flare%20Functions/Flare%20Functions.md). | `functions:` <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `- name: set_type`<span style="color:green"> # Name of the Flare Function</span>  <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `columns:       account_id: string`<span style="color:green"> # Column and data type in column</span>  | NA | Check the [Flare Functions](../Flare%20Functions/Flare%20Functions.md) for available functions  | NA | Optional |
| `commands` | There are two commands available `persist` and `unpersist`. | `commands:` <br>&nbsp;&nbsp;&nbsp;&nbsp; `- name: persist` <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `sequenceName: account_connect` <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `mode: MEMORY_AND_DISK` | NA | `persist`/`unpersist` | NA | Optional |



/home/abhyudaiverma/Desktop/abc (2nd copy)/mkdocs/Mk Docs/Transformation/Flare/