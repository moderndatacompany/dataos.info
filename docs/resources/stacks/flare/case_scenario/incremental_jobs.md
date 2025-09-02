# Incremental jobs


## Case scenario

This case scenario describes a situation where your data source contains a large amount of data that are continuously updated. Reloading the entire data set can be time-consuming. So you want only to read new data, hence we would be using the incremental job or the incremental load method. The incremental load method (incremental job) is more efficient as compared to full data load (batch job) when working with a huge volume of data. 


## Implementation flow

**Define Time Range:** Iceberg supports snapshots with timestamp-based access. You specify start_time and end_time using SQL to define the data window for each job run.

**Identify New Data:** In each run, the job reads only the new records between start_time and end_time. This is crucial for evolving datasets where data changes frequently.

**Configure Workflow:** Create a Flare workflow YAML that defines the data source, incremental SQL logic, and output configuration. For example, you might configure the job to run monthly starting from 2020-01-01 00:00:00.


## Defining Incremental Read Properties

You can define an incremental job generically using the following syntax:


```yaml
incremental:
  context: <context_name>
  sql: >
    SELECT * FROM <source_table>
    WHERE <timestamp_column> BETWEEN '$|start_time|' AND '$|end_time|'

  keys:
    - name: start_time
      sql: SELECT '<start_timestamp>'  # Default or derived

    - name: end_time
      sql: SELECT '<end_timestamp>'  # Usually current timestamp

  state:
    - key: start_time
      value: end_time  # Store progress so next run starts where the last one ended
```

## Flare Workflow for Incremental Ingestion

**1. Manifest Configuration for Incremental Ingestion** 

The below Flare Workflow reads data incrementally based on the commit timestamp.

```yaml
version: v1
name: incremental-ingestion-001
type: workflow
tags:
- Connect
- Incremental
workflow:
  title: Connect Order Incremental Data
  dag:
    - name: order-incremental-001
      title: Order Incremental Data
      spec:
        tags:
        - Connect
        - Incremental
        stack: flare:7.0
        compute: runnable-default
        stackSpec:
          job:
            explain: true
            inputs:
            - name: order_input
              dataset: dataos://lakehouse:retail/orders_enriched
              format: iceberg
  
            logLevel: WARN
            outputs:
              - name: order_input
                dataset: dataos://lakehouse:sample/order_incremental_08?acl=rw
                format: iceberg
                description: Orders Data Incremental From Iceberg
                options:
                  saveMode: overwrite
                  sort:
                    mode: global
                    columns:
                      - name: order_date
                        order: desc
                  iceberg:
                    properties:
                      write.format.default: parquet
                      write.metadata.compression-codec: gzip
                      overwrite-mode: dynamic
                    partitionSpec:
                      - type: day
                        column: order_date
                        name: day_partition       # this should be different from column names in schema in column
                tags:
                  - Connect
                  - Incremental
                title: Order Incremental Data
```


**2. Apply the Workflow using the following command:**

```bash
dataos-ctl resource apply  -f  <file-path>
```


**3. Get the status of the Workflow using:**

=== "Command"

      ```bash
      dataos-ctl resource get -t workflow -w <workspace_name>
      ```

=== "Example"

      For example, if your workflow is applied on sandbox (should be already existing workspace) the command will be:

      ```bash
      dataos-ctl resource get -t workflow -w sandbox
      ```



## Examples

### **Monthly incremental**

This job reads data incrementally from the table incremental_order_15, fetching only the rows where order_date falls within a one-month window, and advances that window automatically after each run.


```yaml
incremental:
  context: incremental_order_15
  sql: select * from incremental_order_15 where order_date > '$|start|' AND order_date <= '$|end|'
  keys:
    - name: start                           # name will always be stored in string
      sql: select to_timestamp('2020-01-01 00:00:00')

    - name: end                             # name will always be stored in string
      sql: select to_timestamp('$|start|') + INTERVAL '1' MONTH

  state:
    - key: start
      value: end
```

### **Real-time Ingestion until Current Timestamp**

```yaml
incremental:
  context: incremental_datas_0001
  sql: >
    select *
    from incremental_datas_0001
    where  event_ts  > to_timestamp('$|start_time|') and event_ts  <= '$|end_time|'
  keys:
    - name: start_time
      sql: SELECT "2022-09-01 00:00:00"
                                                                
    - name: end_time
      sql: select current_timestamp()
  state:
    - key: start_time
      value: end_time
```