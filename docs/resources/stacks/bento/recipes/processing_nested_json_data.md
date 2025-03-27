# Processing Nested JSON Data

```yaml
version: v1beta1
name: simple-test-av
type: service
tags:
  - service
description: Random User
service:
  title: Test  API
  replicas: 1
  servicePort: 9889  # DataOS port
  resources:
    requests:
      cpu: 100m
      memory: 128Mi
    limits:
      cpu: 1000m
      memory: 1024Mi
  ingress:
    enabled: true
    path: /test08   # URL for DataOS (topic name)
    noAuthentication: true
  stack: "bento:3.0"   # dataos stack
  logLevel: DEBUG
  tags:
    - service
    - random-user
  stackSpec:
    input:
        http_client:
          url: https://randomuser.me/api/
          verb: GET
          headers:
            Content-Type: application/JSON
    pipeline:
      processors:
        - label: my_blobl
          bloblang: |
            page = this.info.page
            age = this.results.0.dob.age
            dob = this.results.0.dob.date
            page = this.info.page
            seed = this.info.seed
            email = this.results.0.email
            gender = this.results.0.gender
            name = this.results.0.id.name
            city = this.results.0.location.city
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
                    token: <token>
                description: Random users data
                format: AVRO
                schema: "{\"name\":\"default\",\"type\":\"record\",\"namespace\":\"defaultNamespace\",\"fields\":[{\"name\":\"age\",\"type\":\"int\"},{\"name\":\"city\",\"type\":\"string\"},{\"name\":\"dob\",\"type\":\"string\"},{\"name\":\"email\",\"type\":\"string\"},{\"name\":\"gender\",\"type\":\"string\"},{\"name\":\"name\",\"type\":\"string\"},{\"name\":\"page\",\"type\":\"int\"},{\"name\":\"seed\",\"type\":\"string\"}]}"
                schemaLocation: http://registry.url/schemas/ids/12 
                title: Random Uses Info
                type: STREAM
            type: dataos_depot
          - stdout: {}
```