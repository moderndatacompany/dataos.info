# Pulsar Depots

## Read Config

```yaml
version: v1
name: read-pulsar
type: workflow
tags:
  - pulsar
  - read
description: this jobs reads data from thirdparty and writes to pulsar
workflow:
  dag:
    - name: read-pulsar
      title: write avro data to pulsar
      description: write avro data to pulsar
      spec:
        tags:
          - Connect
        stack: flare:3.0
        compute: runnable-default
        flare:
          job:
            explain: true
            inputs:
              - name: input
                dataset: dataos://sanitypulsaralok01:default/city_pulsar_01
                isStream: false
                options:
                  startingOffsets: earliest
            logLevel: INFO
            outputs:
              - name: input
                dataset: dataos://icebase:sanity/sanity_pulsar?acl=rw
                format: Iceberg
                options:
                  saveMode: overwrite
```

## Write Config

```yaml
# pulsar admin tag required
version: v1
name: read-write-pulsar
type: workflow
tags:
  - pulsar
  - read
description: this jobs reads data from thirdparty and writes to pulsar
workflow:
  dag:
    - name: write-pulsar
      title: write avro data to pulsar
      description: write avro data to pulsar
      spec:
        tags:
          - Connect
        stack: flare:3.0
        compute: runnable-default
        flare:
          job:
            explain: true
            inputs:
              - name: input
                dataset: dataos://thirdparty01:none/city
                format: csv
                isStream: false
            logLevel: INFO
            outputs:
              - name: input
                dataset: dataos://sanitypulsaralok01:default/city_pulsar_01?acl=rw
                format: pulsar
                tags:
                  - Connect
                title: City Data Pulsar
```