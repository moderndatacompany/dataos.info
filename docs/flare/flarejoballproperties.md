# Flare Job Properties
Here is the skeleton of the Flare job.

YAML is a simple but robust data serialization language. It has just
two data structures: 
sequences (a list) 
mappings (key and value pairs).

**Sequence (lists)**
---
- Linux
- BSD
- Illumos

**Mapping (key value pairs)**
--- 
version: v1beta1
name: product-demo-01
type: workflow

**These structures can be combined and embedded.**
Sequence of mappings (list of pairs) 
---
-
 CPU: AMD
 RAM: ‘16 GB’
-
 CPU: Intel
 RAM: ‘16 GB’

**Mapping sequences (key with many values)**
---
tags:
  - Connect
  - City
functions:
  - name: rename
    column: id
    asColumn: country_id
  - name: rename
    column: name
    asColumn: country_name
  
**Sequence of sequences (a list of lists)** 
- 
  - pineapple
  - coconut
-
  - umbrella
  - raincoat

**Mapping of mappings**
Joey:
  age: 22
  sex: M
Laura:
  age: 24
  sex: F

job:
  explain: true
  logLevel: INFO



```yaml
---
version: v1beta1
name: cnt-city-demo-01
type: workflow
tags:
- Connect
- City
description: The job ingests city data from dropzone into raw zone
#owner: itspiyush
workflow:
  title: Connect City
  dag:
  - name: city-01
    title: City Dimension Ingester
    description: The job ingests city data from dropzone into raw zone
    spec:
      tags:
      - Connect
      - City
      stack: flare:1.0
      # persistentVolume:
      #   name: persistent-v
      #   directory: connectCity
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
            - name: output01
              depot: dataos://icebase:retail?acl=rw
          steps:
          - sink:
              - sequenceName: cities
                datasetName: city
                outputName: output01
                outputType: Iceberg
                description: City data ingested from external csv
                outputOptions:
                  saveMode: overwrite
                  iceberg:
                    properties:
                      write.format.default: parquet
                      write.metadata.compression-codec: gzip
                    partitionSpec:
                    - type: identity
                      column: version
                tags:
                  - Connect
                  - City
                title: City Source Data

            sequence:
              - name: cities
                doc: Pick all columns from cities and add version as yyyyMMddHHmm formatted
                  timestamp.
                sql: SELECT *, date_format(now(), 'yyyyMMddHHmm') as version, now() as
                  ts_city FROM city_connect
          


```
```yaml
version: v1beta1
name: wf-ingest-city-state-countries
type: workflow
tags:
  - ingest-data
  - cities
  - states
  - countries
  - enriched
description: This ingest city state and countries data and enriched data
owner: rakeshvishvakarma21
workflow:
  dag:
    - name: ingest-and-enrich-city-state-country
      title: city state and countries workflow
      description: This ingest city state and countries data and data enrichment
      spec:
        tags:
          - cities
          - states
          - countries
          - enriched
        stack: flare:1.0
        flare:
          job:
            explain: true
            inputs:
             - name: cities
               dataset: dataos://thirdparty01:none/cities
               format: csv
               schema: "{\"type\":\"struct\",\"fields\":[{\"name\":\"country_code\",\"type\":\"string\",\"nullable\":true,\"metadata\":{}},{\"name\":\"country_id\",\"type\":\"long\",\"nullable\":true,\"metadata\":{}},{\"name\":\"id\",\"type\":\"long\",\"nullable\":true,\"metadata\":{}},{\"name\":\"latitude\",\"type\":\"double\",\"nullable\":true,\"metadata\":{}},{\"name\":\"longitude\",\"type\":\"double\",\"nullable\":true,\"metadata\":{}},{\"name\":\"name\",\"type\":\"string\",\"nullable\":true,\"metadata\":{}},{\"name\":\"state_code\",\"type\":\"string\",\"nullable\":true,\"metadata\":{}},{\"name\":\"state_id\",\"type\":\"long\",\"nullable\":true,\"metadata\":{}}]}"
             - name: countries
               dataset: dataos://thirdparty01:none/countries
               format: csv
               schema: "{\"type\":\"struct\",\"fields\":[{\"name\":\"capital\",\"type\":\"string\",\"nullable\":true,\"metadata\":{}},{\"name\":\"currency\",\"type\":\"string\",\"nullable\":true,\"metadata\":{}},{\"name\":\"currency_symbol\",\"type\":\"string\",\"nullable\":true,\"metadata\":{}},{\"name\":\"emoji\",\"type\":\"string\",\"nullable\":true,\"metadata\":{}},{\"name\":\"emojiU\",\"type\":\"string\",\"nullable\":true,\"metadata\":{}},{\"name\":\"id\",\"type\":\"long\",\"nullable\":true,\"metadata\":{}},{\"name\":\"iso2\",\"type\":\"string\",\"nullable\":true,\"metadata\":{}},{\"name\":\"iso3\",\"type\":\"string\",\"nullable\":true,\"metadata\":{}},{\"name\":\"latitude\",\"type\":\"double\",\"nullable\":true,\"metadata\":{}},{\"name\":\"longitude\",\"type\":\"double\",\"nullable\":true,\"metadata\":{}},{\"name\":\"name\",\"type\":\"string\",\"nullable\":true,\"metadata\":{}},{\"name\":\"native\",\"type\":\"string\",\"nullable\":true,\"metadata\":{}},{\"name\":\"numeric_code\",\"type\":\"long\",\"nullable\":true,\"metadata\":{}},{\"name\":\"phone_code\",\"type\":\"string\",\"nullable\":true,\"metadata\":{}},{\"name\":\"region\",\"type\":\"string\",\"nullable\":true,\"metadata\":{}},{\"name\":\"subregion\",\"type\":\"string\",\"nullable\":true,\"metadata\":{}},{\"name\":\"timezones\",\"type\":\"string\",\"nullable\":true,\"metadata\":{}},{\"name\":\"tld\",\"type\":\"string\",\"nullable\":true,\"metadata\":{}}]}"
             - name: states
               dataset: dataos://thirdparty01:none/states
               format: csv
               schema: "{\"type\":\"struct\",\"fields\":[{\"name\":\"country_code\",\"type\":\"string\",\"nullable\":true,\"metadata\":{}},{\"name\":\"country_id\",\"type\":\"long\",\"nullable\":true,\"metadata\":{}},{\"name\":\"id\",\"type\":\"long\",\"nullable\":true,\"metadata\":{}},{\"name\":\"latitude\",\"type\":\"double\",\"nullable\":true,\"metadata\":{}},{\"name\":\"longitude\",\"type\":\"double\",\"nullable\":true,\"metadata\":{}},{\"name\":\"name\",\"type\":\"string\",\"nullable\":true,\"metadata\":{}},{\"name\":\"state_code\",\"type\":\"string\",\"nullable\":true,\"metadata\":{}}]}"

            logLevel: ERROR
            
            outputs:
              - name: output01  # cities
                depot: dataos://icebase:countries_states_cities?acl=rw

              - name: output02  # states
                depot: dataos://icebase:countries_states_cities?acl=rw
 
              - name: output03  # countries
                depot: dataos://icebase:countries_states_cities?acl=rw
 
              - name: output04  # joined-data
                depot: dataos://icebase:countries_states_cities?acl=rw

            steps:
              - sequence:
                  - name: countries_uppdated
                    sql: SELECT * FROM countries
                    functions:
                      - name: rename
                        column: id
                        asColumn: country_id
                      - name: rename
                        column: name
                        asColumn: country_name
                      - name: rename
                        column: latitude
                        asColumn: country_latitude
                      - name: rename
                        column: longitude
                        asColumn: country_longitude

                  - name: states_uppdated
                    sql: SELECT * FROM states
                    functions:
                      - name: rename
                        column: id
                        asColumn: state_id
                      - name: rename
                        column: name
                        asColumn: state_name
                      - name: rename
                        column: latitude
                        asColumn: state_latitude
                      - name: rename
                        column: longitude
                        asColumn: state_longitude
                      - name: rename
                        column: country_id
                        asColumn: country_id_in_states

                  - name: cities_uppdated
                    sql: SELECT * FROM cities
                    functions:
                      - name: rename
                        column: id
                        asColumn: city_id
                      - name: rename
                        column: name
                        asColumn: city_name
                      - name: rename
                        column: latitude
                        asColumn: city_latitude
                      - name: rename
                        column: longitude
                        asColumn: city_longitude
                      - name: rename
                        column: state_id
                        asColumn: state_id_in_cities
                      - name: drop
                        columns:
                          - state_code
                          - country_id
                          - country_code

                  - name: joined_states_cities
                    sql: SELECT * FROM cities_uppdated uc left join states_uppdated us on uc.state_id_in_cities = us.state_id
                    functions:
                      - name: drop
                        columns:
                          - state_id_in_cities

                  - name: joined_states_cities_countries
                    sql: SELECT * FROM joined_states_cities jsc left join countries_uppdated ucon on jsc.country_id_in_states = ucon.country_id
                    functions:
                      - name: drop
                        columns:
                          - country_id_in_states

                sink:
                  - sequenceName: cities
                    datasetName: cities
                    outputName: output01
                    outputType: Iceberg
                    description: Cities Information With State and Country Code
                    outputOptions:
                      saveMode: overwrite
                      iceberg:
                        properties:
                          write.format.default: parquet
                          write.metadata.compression-codec: gzip
                    tags:
                      - city-info
                      - database
                    title: Cities Information

                  - sequenceName: states
                    datasetName: states
                    outputName: output02
                    outputType: Iceberg
                    description: States Information With Country Code
                    outputOptions:
                      saveMode: overwrite
                      iceberg:
                        properties:
                          write.format.default: parquet
                          write.metadata.compression-codec: gzip
                    tags:
                      - state-info
                      - database
                    title: States Information

                  - sequenceName: countries
                    datasetName: countries
                    outputName: output03
                    outputType: Iceberg
                    description: Countries Details
                    outputOptions:
                      saveMode: overwrite
                      iceberg:
                        properties:
                          write.format.default: parquet
                          write.metadata.compression-codec: gzip
                    tags:
                      - country-info
                      - database
                    title: Countries Information

                  - sequenceName: joined_states_cities_countries
                    datasetName: enriched_cities_states_countries
                    outputName: output04
                    outputType: Iceberg
                    description: Enriched data of cities, states and countries details 
                    outputOptions:
                      saveMode: overwrite
                      iceberg:
                        properties:
                          write.format.default: parquet
                          write.metadata.compression-codec: gzip
                        partitionSpec:
                          - type: identity
                            column: country_name 
                            name: country_name
                    tags:
                      - cities
                      - states
                      - countries
                      - enriched
                    title: Enriched Countries With States and Cities Information

```
```yaml
---
version: v1beta1
name: cnt-product-demo-01
type: workflow
tags:
- Connect
- Product
description: The job ingests product data from dropzone into raw zone
# owner: deenkar_rubik
workflow:
  title: Connect Product
  dag:
  - name: product-01
    title: Product Dimension Ingester
    description: The job ingests product data from dropzone into raw zone
    spec:
      tags:
      - Connect
      - Product
      stack: flare:1.0
      flare:
        job:
          explain: true
          inputs:
           - name: product_connect
             dataset: dataos://thirdparty01:none/product
             format: csv
             schemaPath: dataos://thirdparty01:none/schemas/avsc/product.avsc

          logLevel: WARN
          outputs:
            - name: output01
              depot: dataos://icebase:retail?acl=rw

          steps:
          - sink:
              - sequenceName: products
                datasetName: product
                outputName: output01
                outputType: Iceberg
                description: Customer data ingested from external csv
                outputOptions:
                  saveMode: overwrite
                  iceberg:
                    properties:
                      write.format.default: parquet
                      write.metadata.compression-codec: gzip
                  partitionSpec:
                    - type: identity
                      column: version
                tags:
                  - Connect
                  - Product
                title: Product Source Data

            sequence:
              - name: products
                doc: Pick all columns from products and add version as yyyyMMddHHmm formatted
                  timestamp.
                sql: SELECT *, date_format(now(), 'yyyyMMddHHmm') as version, now() as
                  ts_product FROM product_connect



```

```yaml
---
version: v1beta1
name: cust-bq-demo-01
type: workflow
tags:
- Connect
- Customer
description: The job ingests customer data from bigquery into raw zone
#owner: itspiyush
workflow:
  title: Connect Customer
  dag:
  - name: customer
    title: Customer Dimension Ingester
    description: The job ingests customer data from bigquery into raw zone
    spec:
      tags:
      - Connect
      - Customer
      stack: flare:1.0
      flare:
        job:
          explain: true
          inputs:
           - name: customer_connect
             dataset: dataos://crmbq:demo/customer_profiles
          logLevel: WARN
          outputs:
            - name: output01
              depot: dataos://icebase:retail?acl=rw
          steps:
          - sink:
              - sequenceName: customers
                datasetName: customer
                outputName: output01
                outputType: Iceberg
                description: Customer data ingested from bigquery
                outputOptions:
                  saveMode: overwrite
                  iceberg:
                    properties:
                      write.format.default: parquet
                      write.metadata.compression-codec: gzip
                  partitionSpec:
                    - type: identity
                      column: version
                tags:
                  - Connect
                  - Customer
                title: Customer Source Data

            sequence:
              - name: customers
                doc: Pick all columns from customers and add version as yyyyMMddHHmm formatted
                  timestamp.
                sql: SELECT *, date_format(now(), 'yyyyMMddHHmm') as version, now() as
                  ts_customer FROM customer_connect
                functions:
                  - name: rename
                    column: Id
                    asColumn: id


```

```yaml
---
version: v1beta1
name: cust-360-01
type: workflow
tags:
- Customer 360
- Offline Sales
description: This job is preparing customer 360 data
#owner: deenkar_rubik
workflow:
  title: Customer 360
  dag:
  - name: cust-360-step-01
    title: Customer 360
    description: This job is preparing customer 360 data
    spec:
      tags:
      - Customer 360
      - Offline Sales
      stack: flare:1.0
      tier: rio
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
            - name: input_customers
              format: iceberg
              dataset: dataos://icebase:retail/customer
            - name: input_pos_transactions
              format: iceberg
              dataset: dataos://icebase:retail/pos_txn_enric
          logLevel: INFO
          outputs:
            - name: output01
              depot: dataos://icebase:retail?acl=rw
          steps:
          - flare/customer-360/steps.yaml



```

```yaml
---
version: v1beta1
name: cnt-store-demo-01
type: workflow
tags:
- Connect
- Store
description: The job ingests store data from thirdparty storage into raw
#owner: itspiyush
workflow:
  title: Connect Store
  dag:
  - name: store
    title: Store Dimension Ingester
    description: The job ingests store data from thirdparty storage into raw zone
    spec:
      tags:
      - Connect
      - Store
      stack: flare:1.0
      # persistentVolume:
      #   name: job-persistence
      #   directory: connectCity
      # tempVolume: 2Gi
      flare:
        job:
          explain: true
          inputs:
           - name: store_connect
             dataset: dataos://thirdparty01:none/store
             format: csv
             schemaPath: dataos://thirdparty01:none/schemas/avsc/store.avsc

          logLevel: WARN
          outputs:
            - name: output01
              depot: dataos://icebase:retail?acl=rw

          steps:
          - sink:
              - sequenceName: store
                datasetName: store
                outputName: output01
                outputType: Iceberg
                description: Store information ingested from external csv
                outputOptions:
                  saveMode: overwrite
                  iceberg:
                    properties:
                      write.format.default: parquet
                      write.metadata.compression-codec: gzip
                  partitionSpec:
                    - type: identity
                      column: version
                tags:
                  - Connect
                  - Store
                title: POS Store Source Data
            sequence:
              - name: store
                doc: Pick all columns from store and add version as yyyyMMddHHmm formatted
                  timestamp.
                sql: SELECT *, date_format(now(), 'yyyyMMddHHmm') as version, now() as
                  ts_store FROM store_connect


```
```yaml
---
version: v1beta1
name: cust-snow-demo-01
type: workflow
tags:
- Connect
- Supplier
description: The job ingests supplier data from snowflake into raw zone
#owner: itspiyush
workflow:
  title: Connect
  dag:
  - name: supplier
    title: Supplier Data Ingester
    description: The job ingests supplier data from snowflake into raw zone
    spec:
      tags:
      - Connect
      - Customer
      stack: flare:1.0
      flare:
        job:
          explain: true
          inputs:
           - name: supplier_connect
             dataset: dataos://snowflake:tpch_sf10/supplier
          logLevel: WARN
          outputs:
            - name: output01
              depot: dataos://icebase:raw01?acl=rw
          steps:
          - sink:
              - sequenceName: suppliers
                datasetName: supplier
                outputName: output01
                outputType: Iceberg
                description: Supplier data ingested from snowflake
                outputOptions:
                  saveMode: overwrite
                  iceberg:
                    properties:
                      write.format.default: parquet
                      write.metadata.compression-codec: gzip
                  partitionSpec:
                    - type: identity
                      column: version
                tags:
                  - Connect
                  - Supplier
                title: Supplier Source Data

            sequence:
              - name: suppliers
                doc: Pick all columns from suppliers and add version as yyyyMMddHHmm formatted
                  timestamp.
                sql: SELECT *, date_format(now(), 'yyyyMMddHHmm') as version, now() as
                  ts_customer FROM supplier_connect



```
```yaml
---
version: v1beta1
name: write-pulsar-avro
type: workflow
tags:
  - pulsar
  - read
description: this jobs reads data from thirdparty and writes to pulsar
workflow:
  dag:
    - name: pulsar-write-avro
      title: write avro data to pulsar
      description: write avro data to pulsar
      spec:
        tags:
          - Connect
        stack: flare:1.0
        envs:
          ENABLE_TOPIC_CREATION: "true"
        # persistentVolume:
        #   name: persistent-v
        #   directory: connectCity
        flare:
          job:
            explain: true
            inputs:
              - name: connect_city
                dataset: dataos://thirdparty01:none/city
                format: csv
                isStream: false
            logLevel: INFO
            outputs:
              - name: output01
                depot: dataos://pulsar:default?acl=rw
                checkpointLocation: dataos://icebase:sys01/checkpoints/connect-city/cl01/city03?acl=rw
                schemaRegistryUrl: http://schema-registry.caretaker:8081
            steps:
              - sink:
                  - sequenceName: connect_city
                    datasetName: city_avro_pulsar
                    outputName:  output01
                    outputType: PulsarAvro
                    outputOptions:
                      extraOptions:
                        pulsar.client.useKeyStoreTls: true
                        pulsar.client.tlsTrustStorePassword: 3e128220-2b96-4e5d-b4fa-a0ce6ce77d1c
                        pulsar.client.tlsTrustStoreType: JKS
                        pulsar.client.tlsTrustStorePath: /etc/dataos/certs/truststore.jks
                        pulsar.client.allowTlsInsecureConnection: false
                        pulsar.client.enableTlsHostnameVerification : false

                        #pulsar.client.useTls: true
                        #pulsar.client.tlsAllowInsecureConnection: false
                        #pulsar.client.tlsTrustCertsFilePath: /etc/dataos/certs/ca.cert.pem
                        #pulsar.client.tlsEnableHostnameVerification: false
                    tags:
                      - Connect
                    title: City Data AVRO Pulasr
```

```yaml
---
version: v1beta1
name: syn-off-tx
type: workflow
tags:
- Offline
- Syndicate
description: This job is Syndicating offline transactions data
#owner: itspiyush
workflow:
  dag:
  - name: syn-off-tx-01-step
    title: Syndicate Offline transactions
    description: This job is Syndicating offline transactions data out into csv.
    spec:
      tags:
      - Offline
      - Syndicate
      stack: flare:1.0
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
              dataset: dataos://icebase:set01/pos_txn_enric_01
          logLevel: INFO
          outputs:
            - name: output01
              depot: dataos://syndicationgcs:syndicate?acl=rw
          steps:
          - sink:
              - sequenceName: syndicatePos
                datasetName: offline_01_csv
                description: Offline transactions into csv.
                outputName: output01
                outputOptions:
                  file:
                    saveMode: Overwrite
                    outputType: CSV
                tags:
                  - Offline
                  - Syndicate
                title: Offline Transactions
            sequence:
              - name: transactions
                sql: SELECT transaction_header.store_id, explode(transaction_line_item)
                  as line_item, store FROM processed_transactions
              - name: syndicatePos
                sql: SELECT store_id, line_item.*, store.store_name, store.store_city,
                  store.store_state FROM transactions
          variables:
            keepSystemColumns: "false"


```


