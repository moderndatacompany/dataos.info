# Bundle Templates


## Template 1

The YAML template defines a DataOS Bundle Resource that automates the deployment of interconnected resources. The first resource defines a Snowflake Depot, which is configured with connection details such as warehouse, URL, and database. Once the Snowflake Depot is created, a data ingestion workflow is triggered. It reads data from an external source (CSV) and writes it into the Snowflake Depot. The data ingestion is dependent on the successful creation of the Snowflake Depot, ensuring the operations are performed in the correct order. Modify this template to manage your own resources and workflows in Bundle Resource.

```yaml title="bundle_template.yml"
--8<-- "examples/resources/bundle/bundle_template_1.yml"
```

<!-- ## Template 2

```yaml title="bundle_template_2.yml"
--8<-- "examples/resources/bundle/bundle_template_2.yml"
``` -->

## Template 2

This YAML template defines a DataOS Bundle Resource. It demonstrates how to reference resources either directly within the bundle or by using external manifest files with the file attribute (e.g., depot.yaml, read_icebase_write_snowflake.yaml). This approach allows you to modularize resource definitions and keep your bundle manifest clean and manageable.

```yaml title="bundle_template_3.yml"
--8<-- "examples/resources/bundle/bundle_template_3.yml"
```
<!-- 
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
          description: this is a snowflake depot
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
                stack: flare:6.0
                compute: runnable-default
                stackSpec:
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
``` -->

