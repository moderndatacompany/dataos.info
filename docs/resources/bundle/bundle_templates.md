# Bundle Templates


## Template 1

```yaml
name: dataosresourcebundle
version: v1alpha
type: bundle
tags: 
  - bundle resource
  - resource
description: this is a bundle resource
layer: user
bundle:
  schedule: 
    initialState: create
    timezone: Asia/Kolkata
    create:
     - cron: '31 0 * * *'

	workspaces: 
	  - name: bundletesting
      description: this is a workspace for bundle testing
      layer: user

  resources: 
    - id: snowflakedepot
      spec:
        name: snowflakedepotxy
        version: v1
        type: depot
        tags: 
          - snowflake
          - depot
        description: this is a snowflake depot
        layer: user
        depot: 
          type: snowflake
          description: this is not a snowflake depot
          connectionSecret: 
            - acl: rw
              type: key-value-properties
              data: 
                username: iamgroot
                password: iamavenger
          external: true
          spec: 
            warehouse: random_warehouse
            url: https://abcd.west-usa.azure.snowflakecomputing.com
            database: newone

    - id: write-data-to-snowflake12
      workspace: public
      spec:
        version: v1
        name: write-data-to-snowflake1
        type: workflow
        tags:
          - Connect
          - read
          - write
        description: Jobs writes data to snowflake and reads from it
        workflow:
          title: Connect Snowflake
          dag:
            - name: write-snowflake-06
              title: Reading data and writing to snowflake
              description: This job writes data to wnowflake
              spec:
                tags:
                  - Connect
                  - write
                stack: flare:4.0
                compute: runnable-default
                flare:
                  job:
                    explain: true
                    inputs:
                      - name: city_connect
                        dataset: dataos://thirdparty01:none/city
                        format: csv
                        schemaPath: dataos://thirdparty01:none/schemas/avsc/city.avsc
                    logLevel: INFO
                    outputs:
                      - name: city_connect
                        dataset: dataos://snowflakedepot:beta/secondtable?acl=rw
                        format: snowflake
                        description: City data ingested from external csv
                        title: City Source Data
                        options:
                          extraOptions:
                            sfWarehouse: newone
      dependencies: 
        - snowflakedepot
```

## Template 2

```yaml
name: dataosbundleresource01
version: v1alpha
type: bundle
tags: 
  - bundle resource
  - resource
description: this is a bundle resource
layer: user
workspace: bundetesting
bundle:
  resources:
    - id: write-data-to-snowflake12
      workspace: bundletesting
      spec:
        version: v1
        name: write-data-to-snowflake1
        type: workflow
        tags:
          - Connect
          - read
          - write
        description: Jobs writes data to snowflake and reads from it
        workflow:
          title: Connect Snowflake
          dag:
            - name: write-snowflake-06
              title: Reading data and writing to snowflake
              description: This job writes data to wnowflake
              spec:
                tags:
                  - Connect
                  - write
                stack: flare:4.0
                compute: runnable-default
                flare:
                  job:
                    explain: true
                    inputs:
                    - name: city_connect
                      dataset: dataos://thirdparty01:none/city
                      format: csv
                      schemaPath: dataos://thirdparty01:none/schemas/avsc/city.avsc
                    logLevel: INFO
                    outputs:
                      - name: city_connect
                        dataset: dataos://snowflakedepot:beta/secondtable?acl=rw
                        format: snowflake
                        description: City data ingested from external csv
                        title: City Source Data
                        options:
                          extraOptions:
                            sfWarehouse: random_warehouse
```

## Template 3

```yaml
version: v1alpha
name: "dataosbundlejobsv14"
type: bundle
tags:
  - sampletest
description: This is bundle, dag of resources
layer: "user"
bundle:
  schedule:
    initialState: create
    timezone: Asia/Kolkata
    create:
     cron: '*/12 * * * *'
#    delete:
#      cron: '*/17 * * * *'
  workspaces:
    - name: testbundle14
      description: "This workspace runs dataos bundle based resources"
      tags:
        - bundleJob
        - bundleResource
      labels:
        "name" : "dataosBundleJobsv14"
      layer: "user"
  resources:
    - id: create-icebase-depot
      file: depot.yaml
    - id: write-into-icebase
      dependencies:
        - create-icebase-depot
      workspace: testbundle14
      file: read_icebase_write_snowflake.yaml
    - id: read-from-icebase
      dependencies:
        - write-into-icebase
      workspace: testbundle14
      spec:
        version: v1
        name: sanity-read-workflow-v14
        type: workflow
        tags:
          - Sanity
          - Icebase
        title: Sanity read from icebase
        description: |
          The purpose of this workflow is to verify if we are able to read different
          file formats Icebase.
        workflow:
          dag:
            - name: sanity-read-job-v14
              title: Sanity read files from icebase
              description: |
                The purpose of this job is to verify if we are able to read different
                file formats from icebase.
              spec:
                tags:
                  - Sanity
                  - icebase
                stack: flare:4.0
                compute: runnable-default
                stackSpec:
                  job:
                    explain: true
                    logLevel: INFO
                    showPreviewLines: 2
                    inputs:
                      - name: a_city_csv
                        dataset: dataos://bundleicebergv14:retail14/city1
                        format: Iceberg
                      - name: a_city_json
                        dataset: dataos://bundleicebergv14:retail14/city2
                        format: Iceberg
                      - name: a_city_parquet
                        dataset: dataos://bundleicebergv14:retail14/city3
                        format: Iceberg

                    outputs:
                      # csv
                      - name: finalDf_csv
                        dataset: dataos://bundleicebergv14:temp14/temp?acl=rw
                        format: Iceberg
                        options:
                          saveMode: overwrite
                          partitionBy:
                            - version
                        tags:
                          - Sanity
                          - Icebase
                          - CSV
                        title:  Csv read sanity
                        description: Csv read sanity
                      # json
                      - name: finalDf_json
                        dataset: dataos://bundleicebergv14:temp14/temp2?acl=rw
                        format: Iceberg
                        options:
                          saveMode: overwrite
                          partitionBy:
                            - version
                        tags:
                          - Sanity
                          - Icebase
                          - JSON
                        title: Json read sanity
                        description: Json read sanity
                      # parquet
                      - name: finalDf_parquet
                        dataset: dataos://bundleicebergv14:temp14/temp3?acl=rw
                        format: Iceberg
                        options:
                          saveMode: overwrite
                          partitionBy:
                            - version
                        tags:
                          - Sanity
                          - Icebase
                          - Parquet
                        title: Parquet read sanity
                        description: Parquet read sanity
                    steps:
                      - sequence:
                          - name: finalDf_csv
                            sql: SELECT * FROM a_city_csv LIMIT 10
                            functions:
                              - name: drop
                                columns:
                                  - "__metadata_dataos_run_mapper_id"
                          - name: finalDf_json
                            sql: SELECT * FROM a_city_json LIMIT 10
                            functions:
                              - name: drop
                                columns:
                                  - "__metadata_dataos_run_mapper_id"
                          - name: finalDf_parquet
                            sql: SELECT * FROM a_city_parquet LIMIT 10
                            functions:
                              - name: drop
                                columns:
                                  - "__metadata_dataos_run_mapper_id"
```

## Template 4

```yaml
version: v1alpha
name: true
type: bundle
tags: 
  - bundle resource
  - resource
description: this is a bundle resource
layer: user
bundle:
  schedule: 
    initialState: create
    timezone: Asia/Kolkata
    create:
      cron: '31 0 * * *'
    delete:
      cron: '33 0 * * *'

  workspaces: 
    - name: bundletesting
      description: this is a workspace for bundle testing
      layer: user

  resources: 
    - id: snowflakedepot
      spec:
        name: snowflakedepotxy
        version: v1
        type: depot
        tags: 
          - snowflake
          - depot
        description: this is a snowflake depot
        layer: user
        depot: 
          type: snowflake
          description: this is not a snowflake depot
          connectionSecret: 
            - acl: rw
              type: key-value-properties
              data: 
                username: iamgroot
                password: iamironman
          external: true
          spec: 
            warehouse: newone
            url: https://abcd.west-usa.azure.snowflakecomputing.com
            database: newdatabase

    - id: write-data-to-snowflake12
      workspace: public
      spec:
        version: v1
        name: write-data-to-snowflake1
        type: workflow
        tags:
          - Connect
          - read
          - write
        description: Jobs writes data to snowflake and reads from it
        workflow:
          title: Connect Snowflake
          dag:
            - name: write-snowflake-06
              title: Reading data and writing to snowflake
              description: This job writes data to wnowflake
              spec:
                tags:
                  - Connect
                  - write
                stack: flare:4.0
                compute: runnable-default
                flare:
                  job:
                    explain: true
                    inputs:
                      - name: city_connect
                        dataset: dataos://thirdparty01:none/city
                        format: csv
                        schemaPath: dataos://thirdparty01:none/schemas/avsc/city.avsc
                    logLevel: INFO
                    outputs:
                      - name: city_connect
                        dataset: dataos://snowflakedepot:beta/secondtable?acl=rw
                        format: snowflake
                        description: City data ingested from external csv
                        title: City Source Data
                        options:
                          extraOptions:
                            sfWarehouse: random_warehouse
      dependencies: 
        - snowflakedepot
    - id: secondbundle
      spec: 
        name: dataosbundleresource02
        version: v1alpha
        type: bundle
        tags: 
          - bundle resource
          - resource
        description: this is a bundle resource
        layer: user
        bundle:
          resources:

            - id: snowflakedepoty
              spec:
                name: snowflakedepoty
                version: v1
                type: depot
                tags: 
                  - snowflake
                  - depot
                description: this is a snowflake depot
                layer: user
                depot: 
                  type: snowflake
                  description: this is not a snowflake depot
                  connectionSecret: 
                    - acl: rw
                      type: key-value-properties
                      data: 
                        username: iamgroot
                        password: iamironman
                  external: true
                  spec: 
                    warehouse: newone
                    url: https://yv65571.central-india.azure.snowflakecomputing.com
                    database: newdatabase
      dependencies: 
        - snowflakedepot
```