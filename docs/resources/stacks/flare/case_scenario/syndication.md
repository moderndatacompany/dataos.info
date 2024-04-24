# Syndication


## Case Scenario

In this case scenario, we syndicate the data from the DataOS internal managed depot icebase to an external depot. This involves reading the data from Icebase, doing certain transformations, and writing it to the external depot.

## Implementation Flow

1. Save the YAML and adjust the depots accordingly.
2. Apply the YAML using DataOS CLI.

## Code Snippet

```yaml
version: v1
name: syndct-fusd-of-tx
type: workflow
tags:
- Offline
- Syndicate
description: This job is Syndicating offline transactions data
workflow:
  dag:
  - name: syndct-fusd-off-tx-01-step
    title: Syndicate Fused Offline transactions
    description: Syndicate fused data between Offline Txn, Store, Product and Customer in CSV format
    spec:
      tags:
      - Offline
      - Syndicate
      stack: flare:3.0
      compute: runnable-default
      flare:
        configs: {}
        driver:
          coreLimit: 2400m
          cores: 2
          memory: 3072m
        executor:
          coreLimit: 2400m
          cores: 2
          instances: 2
          memory: 4096m
        job:
          explain: true
          inputs:
            - name: processed_transactions
              format: iceberg
              dataset: dataos://icebase:set01/pos_store_product_cust_01
          logLevel: INFO
          outputs:
            - name: syndicatePos
              dataset: dataos://syndicationgcs:syndicate/fused_offline_01_csv?acl=rw
              description: Fused offline transactions into csv
              options:
                file:
                  saveMode: Overwrite
                  outputType: CSV
              tags:
                - Fused
                - Offline
                - Syndicate
              title: Fused Offline Transactions
          steps:
          - sequence:
              - name: transactions
                sql: SELECT customer_index, transaction_header.store_id, explode(transaction_line_item)
                  as line_item, store FROM processed_transactions
              - name: syndicatePos
                sql: SELECT customer_index, store_id, line_item.*, store.store_name, store.store_city,
                  store.store_state FROM transactions
          variables:
            keepSystemColumns: "false"
```