# Column Tagging

In Flare 4.0, a new feature has been introduced to enable users to tag columns in an output table from the Flare Workflow YAMLs. This new functionality provides immediate governance over tagged columns during dataset writing. To facilitate this, a new `columnTags` property has been added to the `outputs` section of the Flare YAML.

Three mutually exclusive ways have been defined to identify a column, which includes specifying either `columnRegex`, `columnName`, or `columnNames` within the `columnTags` property.

The following section provides a comprehensive overview of these three ways:

### `columnRegex`

The `columnRegex` property allows the specification of a regular expression pattern to identify columns that require tagging. The pattern will initiate matching from the beginning of the string. 

```yaml
columnTags:
  - columnRegex: "city_*"
    tags:
      - PII.Sensitive
      - PII.Email
      - Tier.Bronze
      - customer
```

### `columnName`

The `columnName` property is utilized to designate a particular column.

```yaml
 columnTags:
	- columnName: "zip_code"
	  tags:
	    - PII.Gender
	    - PHI.DateOfBirth
	- columnName: "state_name"
	  tags:
	    - PII.Sensitive
	    - PII.Name
	    - PII.Name
```

### `columnNames`

The `columnNames` property is utilized when identical tags need to be applied to columns that match the specified name.

```yaml
 columnTags:                  
	- columnNames: # Column Name
    - "state_code"
    - "zip_code"
    - "county_name"
    - "state_name"
    - "city_id"
    - "city_name"
    - "version"
	  tags: # Tags
	    - PII.None
```

> 🗣️ Few important points to note
> 
> 1. Tags are case-sensitive. This implies that `PII` is not interchangeable with `piI`, `pii`, or `Pii`. So, consistency in the usage of tag names should be maintained between the Metis GUI and YAML.
> 2. If the intention is to attach a tag to a column that is already present on Metis, the correct tag, FQN (Fully Qualified Name), must be used. The FQN is constructed using the format `TagCategory.PrimaryTagName`.
> 3. In the event of applying the incorrect tag to a dataset (through YAML), the following steps should be followed for the tag removal:
> 1. Use the Metis GUI to manually remove the erroneous tag from the corresponding column. However, this step alone is not enough, as the tag may reappear in subsequent workflow runs. 
> 2. Subsequently, delete and rerun the workflow by excluding the undesired tag name. It is crucial to ensure that the workflow and DAG names match.

## Code Snippet

The code snippet to define column identifiers and tags is provided below

```yaml
version: v1 # Version
name: columnlevel-tag-workflow # Name of the Workflow
type: workflow # Type of Resource (Here its workflow)
# tags:
#   - Platinum
#   - PII.Age
#   - Tier.Gold
#   - XYZ.Workflow
title: Column Level Tagging # Title
description: |
  The purpose of this workflow is to provide tags at the column level using Flare. 
workflow: # Workflow Section
  dag: # Directed Acyclic Graph (DAG)
  - name: columnlevel-tag-job # Name of the Job
    title: Column Level Tagging Job # Title of the Job
    description: |
      The purpose of this job is to tag columns at column level.
    spec: # Specifications
      # tags:
      # - System
      # - PII.DateOfBirth
      # - Tier.Bronze
      # - XYZ.Job
      stack: flare:4.0 # Stack Version (Here its 4.0)
      compute: runnable-default # Compute
      flare: # Flare Section
        job: # Job Section
          explain: true # Explain
          logLevel: INFO # Loglevel
          showPreviewLines: 2 # Show Preview Lines
          inputs: # Inputs Section
            - name: a_city_csv # Input Dataset Name
              dataset: dataos://thirdparty01:none/city # UDL of the Dataset
              format: csv # Input Dataset Format
              schemaPath: dataos://thirdparty01:none/schemas/avsc/city.avsc # Schema Path
          outputs: # Outputs Section
            - name: finalDf # Output Dataset Name
              dataset: dataos://icebase:publiccollection/customer_406?acl=rw # Output Dataset UDL
              options: # Options
                iceberg: # Iceberg Specific Properties Section
                  partitionSpec:
                    - column: version
                      type: identity
                  properties:
                    write.format.default: parquet
                    write.metadata.compression-codec: gzip
                sort: # Sort
                  columns:
                    - name: version
                      order: desc
                  mode: partition
              format: iceberg # Format of Output Dataset
              # tags:
              # - Tier.System
              # - Tier.Bronze              
              # - PII.DateOfBirth
              # - XYZ.Dataset
              # - Rubber
              # - Pencil
              title: Column tags
              description: Column tags 

              columnTags: # Column Tag Property
                - columnRegex: "city_*" # Column Regular Expression to specify columns to be tagged.
                  tags: # Tags to be designated
                    - PII.Sensitive
                    - PII.Email
                    - Tier.Bronze
                    - customer
                - columnName: "zip_code" # Name of the column to be tagged
                  tags: # Tags to be applied to the column
                    - PII.Gender
                    - PHI.DateOfBirth
                - columnName: "state_name" # Name of the column to be tagged
                  tags: # Tags to be applied to the column
                    - PII.Sensitive
                    - PII.Name
                    - PII.Name
                - columnNames: # Name of the columns to be tagged (multiple)
                    - "state_name"
                    - "version"
                    - "zip_code"
                    - "zip_code"
                  tags: # Tags to be applied to the column
                    - PII.Name
                    - Tier.Bronze
                    - Rubber
                    - Pencil
                    - PII.*
          steps: # Steps Section
            - sequence: # Sequence Section
                - name: finalDf # Name of the transformation step
                  sql: SELECT *, date_format(now(), 'yyyyMMddHHmm') AS version FROM a_city_csv LIMIT 10 # sql
                  functions: # Flare Function
                    - name: drop
                      columns:
                        - "__metadata_dataos_run_mapper_id"
```