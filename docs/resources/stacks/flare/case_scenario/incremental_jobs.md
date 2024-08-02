# Incremental Jobs


## Case Scenario

This case scenario describes a situation where your data source contains a large amount of data that are continuously updated. Reloading the entire data set can be time-consuming. So you want only to read new data, hence we would be using the incremental job or the incremental load method. The incremental load method (incremental job) is more efficient as compared to full data load (batch job) when working with a huge volume of data. 

To know more about an Incremental Job, click [here](/resources/stacks/flare/case_scenario/#incremental-job)

## Implementation Flow

1. The Iceberg file format has a snapshot and timestamp which is explicitly specified by the user to specify the scope of consumption. The ‘start_time’ and ‘end_time’ timestamps are defined and updated using SQL query.
2. To configure your Incremental Job, you need to identify what is new data in an evolving data coming from the data source in Iceberg. This new data needs to be captured and stored at regular intervals.
3. Apply the Command using CLI.

## Implementation Flow (Altered)

1. In this case scenario, we would run an incremental job to incrementally read data for 1 month from the `starting_date` on an interval of 1 month, starting from `start: 2020-01-01 00:00:00`.
2. The Flare Workflow for the Incremental Job is provided in the [Code Snippet](/resources/stacks/flare/case_scenario/incremental_jobs/#code-snippet) below.
3. Once you have the YAML apply it using CLI.

## Outcomes

The Flare Workflow provided below in the code snippet reads data incrementally based on the commit timestamp.

## Code Snippet

```yaml
version: v1
name: incremental-ingestion-08
type: workflow
tags:
- Connect
- Incremental
workflow:
  title: Connect Order Incremental Data
  dag:
  - name: order-incremental-08
    title: Order Incremental Data
    spec:
      tags:
      - Connect
      - Incremental
      stack: flare:3.0
      compute: runnable-default
      envs:
        FLARE_AUDIT_MODE: LOG
        STORE_URL: https://<full-domain>/stores/api/v1
      flare:
        job:
          explain: true
          inputs:
           - name: order_input
             dataset: dataos://icebase:retail/orders_enriched
             format: iceberg
# Incremental Read Properties
             incremental:
               context: incremental_order_8
               sql: select * from incremental_order_8 where order_date > '$|start|' AND order_date <= '$|end|'
               keys:
                - name: start # this will alway be stored in string
                  sql: select to_timestamp('2020-01-01 00:00:00')

                - name: end # this will alway be stored in string
                  sql: select to_timestamp('$|start|') + INTERVAL '1' MONTH

               state:
                  - key: start
                    value: end

          logLevel: WARN
          outputs:
            - name: order_input
              dataset: dataos://icebase:sample/order_incremental_08?acl=rw
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
                      name: day_partition # this should be different from column names in schema in column
              tags:
                - Connect
                - Incremental
              title: Order Incremental Data

  - name: dataos-tool-order
    spec:
      stack: toolbox
      compute: runnable-default
      stackSpec:
        dataset: dataos://icebase:sample/order_incremental_08?acl=rw
        action:
          name: set_version
          value: latest
    dependencies:
      - order-incremental-08
```