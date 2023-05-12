# Fetching Data from Instagram API

This recipe will provide a step-by-step process for fetching data from Instagram using Benthos.

## Step 1: Create an Instagram Account

To access the Instagram API, you will need an Instagram account. If you already have one, skip to the next step.

## Step 2: Switch to Business Account

After creating an Instagram account, switch to a business account. This is important because Instagram only allows businesses to access their API.

## Step 3: Create a Facebook Page

Create a Facebook page that is linked to your Instagram account.

## Step 4: Connect Instagram to Facebook

After creating a Facebook page, connect it to your Instagram account. This is done in the page settings by clicking on Instagram.

## Step 5: Create an App on Meta Developer

Go to the Meta Developer [page](https://developers.facebook.com/) and create an app. This app will be used to access the Instagram API.

## Step 6: Set Up Instagram and Facebook

Once you have created the app, set up both Instagram and Facebook in the app settings.

## Step 7: Generate Access Token

Go to Graph API Explorer [here](https://developers.facebook.com/) to generate an access token. This token will be used to access the Instagram API. Once you have the access token, copy the code for the required output.

## Step 8: Configure Benthos Service

With the access token in hand, configure a Benthos Service to fetch data from Instagram. The following YAML code can be used as a template:

```yaml
version: v1
name: insta
type: service
tags:
  - service
description: insta
service:
  title: Test  API
  replicas: 1
  servicePort: 9846  # DataOS port
  resources:
    requests:
      cpu: 100m
      memory: 128Mi
    limits:
      cpu: 1000m
      memory: 1024Mi
  ingress:
    enabled: true
    path: /test13   # URL for DataOS (topic name)
    noAuthentication: true
    annotations:
      konghq.com/strip-path: "false"
      kubernetes.io/ingress.class: kong
  stack: benthos
  logLevel: DEBUG
  tags:
    - service
  benthos:
    input:
        http_client:
          url: https://graph.facebook.com/v14.0/17841453571657288?fields=business_discovery.username(7000_tmdc)%7Bmedia%7Bcaption%2Ccomments_count%2Clike_count%2C%20username%2C%20id%2C%20media_type%2C%20permalink%2C%20owner%2C%20timestamp%7D%7D&access_token=EAAXXaOWgX9gBAP7ux7LVK0giGxEI8CNPG5tN9oidlZCEX1IXeX2vlukfVIXcF1WVltjXQZArrjQRDAE2RRotDxyuPuZC8b5vG5wxAZA6u6y24UEHPsIibgmhupvej9OSDCQrbZCQSUFAvZArLlfnY5sg55ZBZBMTUSbFGZBugzXaV85yNeeUaPLMGAWcdYZCj2yYD3aeQQ1IueR7OLFs9nzRw7SalB7Xxyk44ZD
          verb: GET
          headers:
            Content-Type: application/JSON
    pipeline:
      processors:
        - label: my_blobl
          bloblang: |
            owner_id = this.id
            username = this.business_discovery.media.data.1.username
            post_id = this.business_discovery.media.data.1.id
            caption = this.business_discovery.media.data.1.caption
            media_type = this.business_discovery.media.data.1.media_type
            link = this.business_discovery.media.data.1.permalink
            timestamp = this.business_discovery.media.data.1.timestamp
            like_count = this.business_discovery.media.data.1.like_count
            comments_count = this.business_discovery.media.data.1.comments_count

    output:
      - broker:
          pattern: fan_out
          outputs:
          - plugin:
              address: dataos://fastbase:default/test13
              metadata:
                auth:
                  token:
                    enabled: true
                    token: <dataos-api-key-token>
                description: Random users data
                format: AVRO
                schema: "{\"name\":\"default\",\"type\":\"record\",\"namespace\":\"defaultNamespace\",\"fields\":[{\"name\":\"caption\",\"type\":\"string\"},{\"name\":\"comments_count\",\"type\":\"int\"},{\"name\":\"like_count\",\"type\":\"int\"},{\"name\":\"link\",\"type\":\"string\"},{\"name\":\"media_type\",\"type\":\"string\"},{\"name\":\"owner_id\",\"type\":\"string\"},{\"name\":\"post_id\",\"type\":\"string\"},{\"name\":\"timestamp\",\"type\":\"int\",\"logicalType\":\"date\"},{\"name\":\"username\",\"type\":\"string\"}]}"
                schemaLocation: http://registry.url/schemas/ids/12 
                title: Random Uses Info
                type: STREAM
            type: dataos_depot
          - stdout: {}
```

## Step 9: Apply the YAML file

You can apply the YAML file, to create a Service resource within the DataOS environment using the command given below:

```bash
dataos-ctl apply -f <path-of-the-config-file> -w <workspace>
```

## Step 10: Check Topic Consume in Fastbase Depot

### Check Run time

```bash
dataos-ctl -t service -w <workspace> -n <service-name>  get runtime -r
# Sample
dataos-ctl -t service -w public -n pulsar-random  get runtime -r
```

### List all tenants

```bash
dataos-ctl fastbase tenant list
```

### List all Namespaces within the Public Tenant

```bash
dataos-ctl fastbase namespace list -t <tenant> 
```

### List all topics in public/default namespace

```bash
dataos-ctl fastbase topic list -n <namespace>
# Sample
dataos-ctl fastbase topic list -n public/default
```

### Check Topic Consume

```bash
dataos-ctl fastbase topic consume -p -s -t persistent://<tenant>/<namespace>/<topic>
# Sample
dataos-ctl fastbase topic consume -p -s -t persistent://public/default/test12
```

## Step 11: Read from Fastbase and write to Icebase

```yaml
version: v1
name: pulsar-insta
type: workflow
tags:
  - json-api
description: This jobs ingest Data from pulsar to icebase
workflow:
  schedule:                # workflow scheduler                                                
    cron: '* * * * *'           # Every Minutes               
    endOn: 2022-12-31T23:59:45Z
    concurrencyPolicy: Forbid
  dag:
    - name: test13
      title: Data from insta 
      description: Picking insta detailes
      spec:
        tags:
          - insta    
        stack: flare:2.0  

        flare:
          driver:
            coreLimit: 2000m
            cores: 1
            memory: 2000m
          executor:
            coreLimit: 2000m
            cores: 1
            instances: 1
            memory: 2000m
          job:
            explain: true
            streaming:
              batchMode: true
              triggerMode: Once
              checkpointLocation: dataos://icebase:sys01/checkpoints/insta/insta?acl=rw 
            inputs:
             - name: randomip
               dataset: dataos://fastbase:default/test13
               options:
                   startingOffsets: earliest
               isStream: true               
            logLevel: INFO
            outputs:
              - name: output01 # http client data
                depot: dataos://icebase:sample?acl=rw
            steps:
              - sink: 
                  - sequenceName: randomip
                    datasetName: test13
                    outputName: output01
                    outputType: Iceberg
                    outputOptions:
                      saveMode: append
                      iceberg:
                        properties:
                          write.format.default: parquet
                          write.metadata.compression-codec: gzip                     
                    
          # sparkConf:
          #   - spark.dynamicAllocation.enabled: true 
          #   - spark.shuffle.service.enabled: true

    - name: dt-test13
      spec:
        stack: toolbox
        toolbox:
          dataset: dataos://icebase:sample/test13?acl=rw
          action:
            name: set_version
            value: latest
      dependencies:
        - test13
```