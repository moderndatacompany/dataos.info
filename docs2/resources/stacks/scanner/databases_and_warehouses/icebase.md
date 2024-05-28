# Scanner for Icebase

DataOS allows you to create a Depot of type 'ICEBASE' to read the schemas/tables stored in DataOS’s lakehouse called Icebase.  The created Depot enables you to read the stored data in datasets. You can scan metadata from the ICEBASE-type depot with the Scanner workflows.

## Requirements

To scan the ICEBASE depot, you need the following:

- Ensure that the depot is created and you have `read` access for the depot.


## Scanner Workflow

Here is an example of YAML configuration to connect to the source and reach the Metis server to save the metadata in Metis DB.

**Depot Scan Workflow YAML**

Create and apply the Scanner YAML. You can run the Scanner workflow with or without a filter pattern. 
```yaml
version: v1
    name: scanner2-icebase-k
    type: workflow
    tags:
      - scanner
      - icebase
    description: The workflow scans Icebase Depot
    workflow:
      dag:
        - name: scanner2-icebase-job
          description: The job scans schema datasets referred to by Icebase Depot and registers in Metis2
          spec:
            tags:
              - scanner2
            stack: scanner:2.0
            compute: runnable-default
            scanner:
              depot: dataos://icebase
              
                sourceConfig:
                  config:
                    type: DatabaseMetadata
                    schemaFilterPattern:
                      includes:
                        - icebase
                      excludes:
                        - information_schema
                        - sys
                        - performance_schema
                        - innodb
```
> After the successful workflow run, you can check the metadata of scanned Tables on Metis UI.