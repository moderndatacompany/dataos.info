# Fastbase Depot

```yaml
    output:
      - broker:
          pattern: fan_out
          outputs:
          - plugin:
              address: dataos://fastbase:default/test08
              metadata:
                auth:
                  token:
                    enabled: true
                    token: YXRsYXNfODBhNjhjYzMzN2JhZTY0OGJkYjJhNzE4MGM2NGQzN2YuZDBkNWFlMjQtMGUyNS00ZmQ1LWExODctNjE0YjhlMjdmMzhi
                description: Random users data
                format: AVRO
                schema: "{\"name\":\"default\",\"type\":\"record\",\"namespace\":\"defaultNamespace\",\"fields\":[{\"name\":\"age\",\"type\":\"int\"},{\"name\":\"city\",\"type\":\"string\"},{\"name\":\"dob\",\"type\":\"string\"},{\"name\":\"email\",\"type\":\"string\"},{\"name\":\"gender\",\"type\":\"string\"},{\"name\":\"name\",\"type\":\"string\"},{\"name\":\"page\",\"type\":\"int\"},{\"name\":\"seed\",\"type\":\"string\"}]}"
                schemaLocation: http://registry.url/schemas/ids/12 
                title: Random Uses Info
                type: STREAM
            type: dataos_depot
          - stdout: {}
```