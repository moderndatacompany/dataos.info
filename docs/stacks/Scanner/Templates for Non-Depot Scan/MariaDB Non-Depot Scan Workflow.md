# **MariaDB Non-Depot Scan Workflow**

The non-depot Scanner workflow will help you to connect with MariaDB to extract metadata details such as schemas, tables, view details etc.

# **Requirements**

- Credentials to connect to MariaDB database.

# **Scanner Workflow**

Here is an example of YAML configuration to connect to the source and reach the Metis server to save the metadata in Metis DB.

1. Create and apply the Scanner YAML. You need to provide source connection details and configuration settings such as  metadata type and filter patterns to include/exclude assets for metadata scanning.

```yaml
version: v1
name: scanner2-mariadb                           # Scanner workflow name
type: workflow
tags:
  - scanner
  - mariadb
description: The job scans schema tables and register metadata
workflow:
  dag:
    - name: scanner2-mariadb                           # name of the job
      description: The job scans schema from mariadb tables and registers their metadata to metis2
      spec:
        tags:
          - scanner2
        stack: scanner:2.0                            # name and version of the stack used
        compute: runnable-default                     # default compute for running workflows
        runAsUser: metis
        scanner:
          type: mariadb
          source: MariaDBSource
          sourceConnection:
            config:
              type: MariaDB
              username: xxxxxx
              password: xxxxxxxxxxxxxxxxxxxxx
              hostPort: mariadbdev.cb98qlrtcmrz.us-east-1.rds.amazonaws.com:3306
              # databaseSchema: schema
          sourceConfig:
            config:
              markDeletedTables: false
              includeTables: true
              includeViews: true
              # includeTags: true
              # databaseFilterPattern:
              #   includes:
              #     - database1
              #     - database2
				      #   excludes:
				      #     - database3
				      #     - database4
				      # schemaFilterPattern:
				      #   includes:
				      #     - schema1
				      #     - schema2
				      #   excludes:
				      #     - schema3
				      #     - schema4
				      # tableFilterPattern:
				      #   includes:
				      #     - table1
				      #     - table2
				      #   excludes:
				      #     - table3
				      #     - table4
```

> **Note:** Remove the commented part mentioned under the filter pattern in the Scanner YAML to apply filters for the required schemas and tables.
