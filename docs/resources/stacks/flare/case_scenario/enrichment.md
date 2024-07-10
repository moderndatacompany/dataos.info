# Enrichment


```yaml
version: v1
name: wf-ingest-city-state-countries
type: workflow
tags:
  - ingest-data
  - cities
  - states
  - countries
  - enriched
description: This ingest city state and countries data and enriched data
owner: rakeshvishvakarma
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
        stack: flare:3.0
        compute: runnable-default
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
                    tags:
                      - cities
                      - states
                      - countries
                      - enriched
                    title: Enriched Countries With States and Cities Information
```

# Toolbox Workflow

```yaml
version: v1
name: dataos-tool-connect-all
type: workflow
workflow:
  dag:
  - name: dataos-tool-cities-01
    spec:
      stack: toolbox
      compute: runnable-default
      toolbox:
        dataset: dataos://icebase:countries_states_cities/cities?acl=rw
        action:
          name: set_version
          value: latest

  - name: dataos-tool-states-01
    spec:
      stack: toolbox
      compute: runnable-default
      toolbox:
        dataset: dataos://icebase:countries_states_cities/states?acl=rw
        action:
          name: set_version
          value: latest

  - name: dataos-tool-countries-01
    spec:
      stack: toolbox
      compute: runnable-default
      toolbox:
        dataset: dataos://icebase:countries_states_cities/countries?acl=rw
        action:
          name: set_version
          value: latest

  - name: dataos-tool-enriched-01
    spec:
      stack: toolbox
      compute: runnable-default
      toolbox:
        dataset: dataos://icebase:countries_states_cities/enriched_cities_states_countries?acl=rw
        action:
          name: set_version
          value: latest
```