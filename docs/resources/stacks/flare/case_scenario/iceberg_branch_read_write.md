# How to read and write data to a specific branch in an Iceberg dataset?

## Read configuration

When you need to access data from a specific branch in an Iceberg dataset, your workflow configuration should reflect the precise branch details to ensure data integrity and accuracy. Below is an example configuration that demonstrates how to read from a branch.

```yaml
version: v1
name: read-from-branch
type: workflow
workflow:
  dag:
    - name: write-data
      spec:
        stack: flare:6.0
        compute: runnable-default
        stackSpec:
          job:
            explain: true
            logLevel: INFO
            showPreviewLines: 2
            inputs:
              - name: sanity_city_input
                dataset: dataos://icebase:retail/city
                format: Iceberg
                options:
                  branch: b1

            steps:
              - sequence:
                  - name: cities
                    sql: select * from city_connect where state_code = 'AZ'

            outputs:
              - dataset: dataos://icebase:retail/city?acl=rw
                format: iceberg
                name: cities
```

## Write configuration

Configuring a workflow to write data to a specific branch requires careful specification of the branch details in the output section. This ensures that all writes are correctly directed to the intended branch of the dataset. Below is the configuration for writing to a branch.

```yaml
version: v1
name: write-in-branch
type: workflow
workflow:
  dag:
    - name: write-data
      spec:
        stack: flare:6.0
        compute: runnable-default
        stackSpec:
          job:
            explain: true
            logLevel: INFO
            showPreviewLines: 2
            inputs:
              - dataset: dataos://icebase:retail/city
                format: iceberg
                name: city_connect

            steps:
              - sequence:
                  - name: cities
                    sql: select * from city_connect where state_code = 'AZ'

            outputs:
              - dataset: dataos://icebase:retail/city?acl=rw
                format: iceberg
                name: cities
                options:
                  extraOptions:
                    branch: b1
```