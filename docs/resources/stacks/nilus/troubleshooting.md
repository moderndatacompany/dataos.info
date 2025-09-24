# Troubleshooting Nilus Stack

## Issue 1: Missing Table Schema Format in `dest-table`

**Workflow YAML:**

```yaml
name: abcd-batch-pg-test
version: v1
type: workflow
tags:
    - workflow
    - nilus-batch
description: Nilus Batch Service Sample
workspace: public
workflow:
  dag:
    - name: batch-job-01
      spec:
        stack: nilus:1.0
        compute: runnable-default
        resources:
          requests:
            cpu: 100m
            memory: 128Mi
        logLevel: INFO
        stackSpec:
          source:
            address: dataos://ncdcpostgres
            options:
              source-table: ecom.sales
          sink:
            address: dataos://testinglh
            options:
              dest-table: b_007_batch
              incremental-strategy: append
              aws_region: us-west-2
```

**Error Message:**

```bash
ValueError: Table name must be in the format <schema>.<table>
```

**Root Cause:**

The value of `dest-table` is not in the expected format. It lacks the required `<schema>.<table>` structure.

**Resolution:**

Update the `dest-table` value to include both schema and table names.

**Example:**

```yaml
name: abcd-batch-pg-test
version: v1
type: workflow
tags:
    - workflow
    - nilus-batch
description: Nilus Batch Service Sample
workspace: public
workflow:
  dag:
    - name: batch-job-01
      spec:
        stack: nilus:1.0
        compute: runnable-default
        resources:
          requests:
            cpu: 100m
            memory: 128Mi
        logLevel: INFO
        stackSpec:
          source:
            address: dataos://ncdcpostgres
            options:
              source-table: ecom.sales
          sink:
            address: dataos://testinglh
            options:
              dest-table: b_007_batch.big_table_test       #mandatory
              incremental-strategy: append                #mandatory
```