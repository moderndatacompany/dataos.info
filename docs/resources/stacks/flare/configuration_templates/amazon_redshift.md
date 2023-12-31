# Amazon Redshift Depots


To read/write data on the Redshift data source, you first need to create a depot on top of it. In case you haven’t created a Redshift Depot navigate to the below link

## Read Config

Once you have set up a Redshift Depot, you can start reading data from it. 


**Sample Read configuration YAML**

Let’s take a case scenario where the dataset is stored in Redshift Depot and you have to read data from the source, perform some transformation steps and write it to the Icebase which is a managed depot within the DataOS. The read config YAML will be as follows

Sample Input Section

```yaml
inputs:
  - name: cities
    dataset: dataos://redshift:public/city_01
    format: Redshift
```
Sample Configuration YAML

```yaml
version: v1
name: connect-redshift-read-write
type: workflow
tags:
  - Connect
  - read
  - write
description: Jobs writes data to redshift and reads from it
workflow:
  title: Read redshift
  dag:
    - name: read-redshift-01
      title: Reading data and writing to dataos
      description: This job writes data to dataos
      spec:
        tags:
          - Connect
          - read
        stack: flare:3.0
        compute: runnable-default
        flare:
          job:
            explain: true
            inputs:
              - name: cities
                dataset: dataos://redshift:public/city_01
                format: Redshift
            logLevel: INFO
            outputs:
              - name: output01
                dataset: dataos://icebase:sample/city_read_redshift?acl=rw
                format: iceberg
                options:
                  saveMode: append
            steps:
              - sequence:
                - name: output01
                  sql: SELECT * FROM cities
```

## Write Config

```yaml
version: v1
name: connect-snowflake-read-write-02
type: workflow
tags:
  - Connect
  - read
  - write
description: Jobs writes data to snowflake and reads from it
workflow:
  title: Connect Snowflake
  dag:
    - name: write-snowflake-02
      title: Reading data and writing to snowflake
      description: This job writes data to wnowflake
      spec:
        tags:
          - Connect
          - write
        stack: flare:3.0
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
	           - name: cities
	             dataset: dataos://redshift:public/sanity_redshift_write?acl=rw
	             format: redshift
	             options:
	               saveMode: append
```