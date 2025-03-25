# How to apply Service and get runtime status of it using CLI Stack?

```yaml
version: v1
name: dataos-ctl-service-lifecycle-01
type: workflow
workflow:
  dag:
  - name: create-service
    spec:
      stack: dataos-ctl
      compute: runnable-default
      dataosSecrets:
      - name: dataos-ctl-user-apikey
        allKeys: true
        consumptionType: envVars
      stackSpec:
        arguments:
        - resource
        - apply
        - -f
        - /etc/dataos/config/manifest.yaml
        - -w
        - ${CURRENT_WORKSPACE}
        manifest:
          version: v1
          name: random-user
          type: service
          tags:
            - service
          description: Random User
          service:
            title: Test  API
            replicas: 1
            servicePort: 9876
            compute: runnable-default
            resources:
              requests:
                cpu: 100m
                memory: 128Mi
              limits:
                cpu: 1000m
                memory: 1024Mi
            ingress:
              enabled: true
              path: /random-user
              noAuthentication: true
            stack: bento:3.0
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
                      Content-Type: application/octet-stream

              pipeline:
                processors:

                  - bloblang: meta status_code = 200

                  - log:
                      level: DEBUG
                      message: "received message: ${!meta()}"

                  - bloblang: |
                      root.id = uuid_v4()
                      root.title = this.results.0.name.title.or("")
                      root.first_name = this.results.0.name.first.or("")
                      root.last_name = this.results.0.name.last.("")
                      root.gender = this.results.0.gender.or("")
                      root.email = this.results.0.email.or("")
                      root.city = this.results.0.location.city.or("")
                      root.state = this.results.0.location.state.or("")
                      root.country = this.results.0.location.country.or("")
                      root.postcode = this.results.0.location.postcode.or("").string()
                      root.age = this.results.0.age.or("").string()
                      root.phone = this.results.0.phone.or("").string()
                  - log:
                      level: INFO
                      message: 'payload: ${! json() }'

              output:
                broker:
                  outputs:
                    - broker:
                        pattern: fan_out
                        outputs:
                          - stdout: {}
                          - type: dataos_depot
                            plugin:
                              address: dataos://fastbase:default/random_users_test_01
                              metadata:
                                auth:
                                  token:
                                    enabled: true
                                description: Audit receiver Service
                                format: AVRO
                                schema: "{\"type\":\"record\",\"name\":\"default\",\"namespace\":\"defaultNamespace\",\"fields\":[{\"name\":\"id\",\"type\":\"string\"},{\"name\":\"title\",\"type\":\"string\"},{\"name\":\"first_name\",\"type\":\"string\"},{\"name\":\"last_name\",\"type\":\"string\"}, {\"name\":\"gender\",\"type\":\"string\"},{\"name\":\"email\",\"type\":\"string\"},{\"name\":\"city\",\"type\":\"string\"},{\"name\":\"state\",\"type\":\"string\"},{\"name\":\"country\",\"type\":\"string\"},{\"name\":\"postcode\",\"type\":\"string\"},{\"name\":\"age\",\"type\":\"string\"},{\"name\":\"phone\",\"type\":\"string\"}]}"
                                schemaLocation: http://registry.url/schemas/ids/11
                                title: Random Uses Info
                                tls:
                                  enabled: true
                                  tls_allow_insecure_connection: true
                                  tls_validate_hostname: false
                                type: STREAM
  - name: get-service-runtime
    spec:
      stack: dataos-ctl
      compute: runnable-default
      dataosSecrets:
      - name: dataos-ctl-user-apikey
        allKeys: true
        consumptionType: envVars
      stackSpec:
        arguments:
        - resource
        - get
        - -t
        - service
        - -n
        - random-user
        - runtime
        - -w
        - ${CURRENT_WORKSPACE}
    dependencies:
    - create-service
```