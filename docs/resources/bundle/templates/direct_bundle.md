# Inline Resource Specification in Bundle

This YAML template defines a DataOS Bundle Resource that demonstrates **inline Resource specification** using the `spec` attribute. Unlike file-based approaches, this template embeds complete Resource definitions directly within the Bundle manifest, making it ideal for self-contained deployments where all configurations are maintained in a single file.

## Use case

This template is ideal for:

- **Quick deployments** where you want all configurations in one place

- **Testing and prototyping** data pipelines without managing multiple files

- **Simple workflows** with 2-3 Resources that don't require extensive modularization

- **Documentation and examples** where readability and completeness in a single file is important


## Template



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
              spec:
                tags:
                  - Connect
                  - write
                stack: flare:7.0
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
                            sfWarehouse: newone
      dependencies: 
        - snowflakedepot
```


**Resource orchestration flow:**

1. Bundle applies and creates the Snowflake Depot inline
2. DataOS validates connection and marks Depot as `active`
3. Once Depot is active, the dependent Flare workflow is triggered
4. Workflow reads from CSV source and writes to Snowflake Depot

## When to use inline vs. file-based Bundles

**Use inline Bundle (this template) when:**

- You have few Resources (2-5) with simple configurations
- All configurations fit comfortably in one file (<500 lines)
- You want maximum portability with a single file
- Resource definitions are tightly coupled and always deployed together

**Use file-based Bundle when:**

- You have many Resources or complex configurations
- Resources are reused across multiple Bundles
- Different teams manage different Resource definitions
- You need better organization and separation of concerns


