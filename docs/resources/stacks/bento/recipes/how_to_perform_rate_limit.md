# Rate Limiting in Bento

[Rate limiting](../components/rate_limit.md) is a crucial feature in Bento that allows you to control the speed at which messages are read, processed, and written. By setting rate limits, you can regulate the flow of messages through your Bento pipelines, preventing overload and ensuring optimal performance.

## Configuration

Rate limiting in Bento is configured using the `rate_limit_resources` field in your configuration file. This field allows you to define resources that are subject to rate limits, along with their specific rate limit settings.

``` yaml
rate_limit_resources:
  - label: my_rate_limit
    type: local
    local:
      count: 1
      interval: 10s
```
In this example:

* `label`: A unique label for the rate limit resource.
* `type`: The type of rate limit. Currently, Bento supports local and redis rate limits.
* `count`: The maximum number of messages allowed within the specified interval.
* `interval`: The time interval (in seconds) over which the message count is measured.

The local rate limit is a simple X every Y type rate limit that can be shared across any number of components within the pipeline but does not support distributed rate limits across multiple running instances of Bento.


## Usage

Once rate limit resources are defined, you can apply them to various components within your DataOS Bento pipeline. For example, you can apply rate limits to inputs, processors, or outputs to control the flow of messages at different stages of processing.

<details><summary>Rate Limiting Manifest</summary>

``` yaml
# Resource-specific section
name: wf-random-user-api 
version: v1
type: service
tags:
  - service
description: The workflow is for the job to ingest random user api data for demo from bento into fastbase
service:
  title: Random User Streaming Dataset
  replicas: 1
  autoScaling:
    enabled: true
    minReplicas: 1
    maxReplicas: 3
    targetMemoryUtilizationPercentage: 80
    targetCPUUtilizationPercentage: 80
  servicePort: 9876
  resources:
    requests:
      cpu: 100m
      memory: 128Mi
    limits:
      cpu: 1000m
      memory: 1024Mi
  ingress:
    enabled: true
    path: /random-user2
    noAuthentication: true
    annotations:
      konghq.com/strip-path: "false"
      kubernetes.io/ingress.class: kong
  stack: bento
  logLevel: DEBUG
  compute: runnable-default
  tags:
    - service
    - random-user
  # Bento-specific section
  stackSpec:
      rate_limit_resources:
        - label: foobar
          type: local
          local:
            count: 1
            interval: 10s
      input:
          http_client:
            url: https://randomuser.me/api/
            verb: GET
            headers:
              Content-Type: application/octet-stream
            rate_limit: foobar

      pipeline:
        processors:
          - bloblang: meta status_code = 200
            rate_limit: foobar

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
              root.phones = this.results.0.phone.or("").string()
              root.timezone = this.results.0.location.timezone.description.string()
              
          - log:
              level: INFO
              message: 'payload: ${! json() }'


      output:
        broker:
          pattern: fan_out
          outputs:
          - plugin:
              address: dataos://fastbase:default/new_random_data_05
              metadata:
                auth:
                  token:
                    enabled: true
                    token: asdfrC5kNTVjMDE5Yy05MThmLTQ4OGMtYTEyMS01ODhjY2IyZDI1MjE=
                description: Random users data
                format: AVRO
                schema: "{\"type\":\"record\",\"name\":\"default\",\"namespace\":\"defaultNamespace\",\"fields\":[{\"name\":\"id\",\"type\":\"string\"},{\"name\":\"title\",\"type\":\"string\"},{\"name\":\"first_name\",\"type\":\"string\"},{\"name\":\"last_name\",\"type\":\"string\"}, {\"name\":\"gender\",\"type\":\"string\"},{\"name\":\"email\",\"type\":\"string\"},{\"name\":\"city\",\"type\":\"string\"},{\"name\":\"state\",\"type\":\"string\"},{\"name\":\"country\",\"type\":\"string\"},{\"name\":\"postcode\",\"type\":\"string\"},{\"name\":\"age\",\"type\":\"string\"},{\"name\":\"phone\",\"type\":\"string\"},{\"name\":\"phones\",\"type\":\"string\"},{\"name\":\"timezone\",\"type\":\"string\"}]}"
                schemaLocation: http://registry.url/schemas/ids/12
                title: Random Uses Info
                type: STREAM
            type: dataos_depot
            rate_limit: foobar
          - stdout: {}
```

</details>

In this example, the rate limit resource my_rate_limit is applied to an input, a processor, and an output component, ensuring that the flow of messages at each stage adheres to the specified rate limit.

## Conclusion

Rate limiting in Bento is a powerful mechanism for controlling message throughput and ensuring the stability and efficiency of your data processing pipelines. By properly configuring and applying rate limits, you can effectively manage the flow of messages and prevent overload in your system.