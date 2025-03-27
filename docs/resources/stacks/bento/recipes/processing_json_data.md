# Processing JSON Data using Bento



```yaml
version: v1beta1
name: ll-av-test
type: service
tags:
  - service
description: Linkedin Learning Activity Reports
service:
  title: Linkedin Learning Activity Reports  API
  replicas: 1
  servicePort: 9807  # DataOS port
  resources:
    requests:
      cpu: 100m
      memory: 128Mi
    limits:
      cpu: 1000m
      memory: 1024Mi
  ingress:
    enabled: true
    path: /test42   # URL for DataOS (topic name)
    noAuthentication: true
  stack: "bento:3.0"
  logLevel: DEBUG
  tags:
    - service
  stackSpec:
    input:
      http_client:
        url: https://mocki.io/v1/3b55ac5a-c342-4d6e-b7e9-8459a064bf9d
        verb: GET
        headers:
          Content-Type: application/JSON

    pipeline:
      processors:
        - label: my_blobl
          bloblang: |
            engagement_type = this.elements.0.explode("activities").map_each(this.activities.engagementType.string()).or([])
            engagement_value = this.elements.0.explode("activities").map_each(this.activities.engagementValue.number()).or([])
            asset_type = this.elements.0.explode("activities").map_each(this.activities.assetType.string()).or([])
            engagementmetric_qualifier = this.elements.0.explode("activities").map_each(this.activities.engagementMetricQualifier.string()).or([])
            customAttributes = this.elements.0.explode("activities").map_each(this.learnerDetails.customAttributes.string()).or([])
            email = this.elements.0.explode("activities").map_each(this.learnerDetails.email.string()).or([])
            enterpriseGroups = this.elements.0.explode("activities").map_each(this.learnerDetails.enterpriseGroups.0.string()).or([])
            profileUrn = this.elements.0.explode("activities").map_each(this.learnerDetails.entity.profileUrn.string()).or([])
            name = this.elements.0.explode("activities").map_each(this.learnerDetails.name.string()).or([])
            uniqueUserId = this.elements.0.explode("activities").map_each(this.learnerDetails.uniqueUserId.string()).or([])
            count = this.paging.count
            href = this.paging.explode("links").map_each(this.links.href.string()).or([])
            rel = this.paging.explode("links").map_each(this.links.rel.string()).or([])
            type = this.paging.explode("links").map_each(this.links.type.string()).or([])
            start = this.paging.start
            total = this.paging.total

    output:
      - broker:
          pattern: fan_out
          outputs:
          - plugin:
              address: dataos://fastbase:default/test42
              metadata:
                auth:
                  token:
                    enabled: true
                    token: <token>
                description: Linkedin Learning Activity Reports data
                format: AVRO
                schema: "{\"name\":\"default\",\"type\":\"record\",\"namespace\":\"defaultNamespace\",\"fields\":[{\"name\":\"asset_type\",\"type\":{\"type\":\"array\",\"items\":\"string\"}},{\"name\":\"count\",\"type\":\"int\"},{\"name\":\"customAttributes\",\"type\":{\"type\":\"array\",\"items\":\"string\"}},{\"name\":\"email\",\"type\":{\"type\":\"array\",\"items\":\"string\"}},{\"name\":\"engagementmetric_qualifier\",\"type\":{\"type\":\"array\",\"items\":\"string\"}},{\"name\":\"engagement_type\",\"type\":{\"type\":\"array\",\"items\":\"string\"}},{\"name\":\"engagement_value\",\"type\":{\"type\":\"array\",\"items\":\"int\"}},{\"name\":\"enterpriseGroups\",\"type\":{\"type\":\"array\",\"items\":\"string\"}},{\"name\":\"href\",\"type\":{\"type\":\"array\",\"items\":\"string\"}},{\"name\":\"name\",\"type\":{\"type\":\"array\",\"items\":\"string\"}},{\"name\":\"profileUrn\",\"type\":{\"type\":\"array\",\"items\":\"string\"}},{\"name\":\"rel\",\"type\":{\"type\":\"array\",\"items\":\"string\"}},{\"name\":\"start\",\"type\":\"int\"},{\"name\":\"total\",\"type\":\"int\"},{\"name\":\"type\",\"type\":{\"type\":\"array\",\"items\":\"string\"}},{\"name\":\"uniqueUserId\",\"type\":{\"type\":\"array\",\"items\":\"string\"}}]}"
                schemaLocation: http://registry.url/schemas/ids/12 
                title: Linkedin Learning Activity Reports
                type: STREAM
            type: dataos_depot
          - stdout: {}
```