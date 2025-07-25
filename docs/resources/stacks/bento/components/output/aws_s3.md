# aws_s3

Sends message parts as objects to an Amazon S3 bucket. Each object is uploaded with the path specified with the path field. This processor was introduced in version 1.0.0.

## YAML Configuration

### **Common Config**
```yaml
# Common config fields, showing default values

output:
  label: ""
  aws_s3:
    bucket: "" # No default (required)
    path: ${!count("files")}-${!timestamp_unix_nano()}.txt
    tags: {}
    content_type: application/octet-stream
    metadata:
      exclude_prefixes: []
    max_in_flight: 64
    batching:
      count: 0
      byte_size: 0
      period: ""
      jitter: 0
      check: ""
```


### **Full Config**

```yaml

# All config fields, showing default values
output:
  label: ""
  aws_s3:
    bucket: "" # No default (required)
    path: ${!count("files")}-${!timestamp_unix_nano()}.txt
    tags: {}
    content_type: application/octet-stream
    content_encoding: ""
    cache_control: ""
    content_disposition: ""
    content_language: ""
    website_redirect_location: ""
    metadata:
      exclude_prefixes: []
    storage_class: STANDARD
    kms_key_id: ""
    server_side_encryption: ""
    force_path_style_urls: false
    max_in_flight: 64
    timeout: 5s
    batching:
      count: 0
      byte_size: 0
      period: ""
      jitter: 0
      check: ""
      processors: [] # No default (optional)
    region: ""
    endpoint: ""
    credentials:
      profile: ""
      id: ""
      secret: ""
      token: ""
      from_ec2_role: false
      role: ""
      role_external_id: ""
```

In order to have a different path for each object you should use function interpolations described [here](/resources/stacks/bento/configurations/interpolation/), which are calculated per message of a batch.

## Metadata

Metadata fields on messages will be sent as headers, in order to mutate these values (or remove them) check out the [metadata docs](/resources/stacks/bento/configurations/metadata/).

## Tags

The tags field allows you to specify key/value pairs to attach to objects as tags, where the values support [interpolation functions](/resources/stacks/bento/configurations/interpolation/#bloblang-queries):

```yaml
output:
  aws_s3:
    bucket: TODO
    path: ${!count("files")}-${!timestamp_unix_nano()}.tar.gz
    tags:
      Key1: Value1
      Timestamp: ${!metadata("Timestamp").string()}
```

## Credentials

By default Bento will use a shared credentials file when connecting to AWS services. It's also possible to set them explicitly at the component level, allowing you to transfer data across accounts. You can find out more in [this document](/resources/stacks/bento/guids/aws/).

## Batching

It's common to want to upload messages to S3 as batched archives, the easiest way to do this is to batch your messages at the output level and join the batch of messages with an archive and/or compress processor.

For example, if we wished to upload messages as a .tar.gz archive of documents we could achieve that with the following config:

```yaml
output:
  aws_s3:
    bucket: TODO
    path: ${!count("files")}-${!timestamp_unix_nano()}.tar.gz
    batching:
      count: 100
      period: 10s
      processors:
        - archive:
            format: tar
        - compress:
            algorithm: gzip
```


Alternatively, if we wished to upload JSON documents as a single large document containing an array of objects we can do that with:


```yaml
output:
  aws_s3:
    bucket: TODO
    path: ${!count("files")}-${!timestamp_unix_nano()}.json
    batching:
      count: 100
      processors:
        - archive:
            format: json_array
```


## Performance

This output benefits from sending multiple messages in flight in parallel for improved performance. You can tune the max number of in flight messages (or message batches) with the field max_in_flight.

## Fields


### **`bucket`**

The bucket to upload messages to.

Type: `string`

path
The path of each message to upload. This field supports [interpolation functions](/resources/stacks/bento/configurations/interpolation/#bloblang-queries).

Type: `string`

Default: `"${!count(\"files\")}-${!timestamp_unix_nano()}.txt"`

```yaml
# Examples

path: ${!count("files")}-${!timestamp_unix_nano()}.txt

path: ${!metadata("kafka_key")}.json

path: ${!json("doc.namespace")}/${!json("doc.id")}.json
```


### **`tags`**

Key/value pairs to store with the object as tags. This field supports [interpolation functions](/resources/stacks/bento/configurations/interpolation/#bloblang-queries).

Type: `object`

Default: `{}`

```yaml
# Examples

tags:
  Key1: Value1
  Timestamp: ${!metadata("Timestamp")}
```


### **`content_type`**

The content type to set for each object. This field supports [interpolation functions](/resources/stacks/bento/configurations/interpolation/#bloblang-queries).

Type: `string`

Default: `"application/octet-stream"`

### **`content_encoding`**

An optional content encoding to set for each object. This field supports [interpolation functions](/resources/stacks/bento/configurations/interpolation/#bloblang-queries).

Type: `string`

Default: `""`



### **`cache_control`**

The cache control to set for each object. This field supports [interpolation functions](/resources/stacks/bento/configurations/interpolation/#bloblang-queries).

Type: `string`

Default: `""`


### **`content_disposition`**

The content disposition to set for each object. This field supports [interpolation functions](/resources/stacks/bento/configurations/interpolation/#bloblang-queries).

Type: `string`

Default: `""`


### **`content_language`**

The content language to set for each object. This field supports [interpolation functions](/resources/stacks/bento/configurations/interpolation/#bloblang-queries).

Type: `string`

Default: `""`


### **`website_redirect_location`**

The website redirect location to set for each object. This field supports [interpolation functions](/resources/stacks/bento/configurations/interpolation/#bloblang-queries).

Type: `string`

Default: `""`


### **`metadata`**

Specify criteria for which metadata values are attached to objects as headers.

Type: `object`


### **`metadata.exclude_prefixes`**

Provide a list of explicit metadata key prefixes to be excluded when adding metadata to sent messages.

Type: `array`

Default: `[]`


### **`storage_class`**

The storage class to set for each object. This field supports [interpolation functions](/resources/stacks/bento/configurations/interpolation/#bloblang-queries).

Type: `string`

Default: `"STANDARD"`

Options: `STANDARD`, `REDUCED_REDUNDANCY`, `GLACIER`, `STANDARD_IA`, `ONEZONE_IA`, `INTELLIGENT_TIERING`, `DEEP_ARCHIVE`


### **`kms_key_id`**

An optional server side encryption key.

Type: `string`

Default: `""`


### **`server_side_encryption`**

An optional server side encryption algorithm.

Type: `string`

Default: `""`
Requires version 1.0.0 or newer


### **`force_path_style_urls`**

Forces the client API to use path style URLs, which helps when connecting to custom endpoints.

Type: `bool`

Default: `false`


### **`max_in_flight`**

The maximum number of messages to have in flight at a given time. Increase this to improve throughput.

Type: `int`

Default: `64`


### **`timeout`**

The maximum period to wait on an upload before abandoning it and reattempting.

Type: `string`

Default: `"5s"`


### **`batching`**

Allows you to configure a batching policy.

Type: `object`

```yaml
# Examples

batching:
  byte_size: 5000
  count: 0
  period: 1s

batching:
  count: 10
  period: 1s

batching:
  check: this.contains("END BATCH")
  count: 0
  period: 1m

batching:
  count: 10
  jitter: 0.1
  period: 10s
```


### **`batching.count`**

A number of messages at which the batch should be flushed. If 0 disables count based batching.

Type: `int`

Default: `0`


### **`batching.byte_size`**

An amount of bytes at which the batch should be flushed. If 0 disables size based batching.

Type: `int`

Default: `0`


### **`batching.period`**

A period in which an incomplete batch should be flushed regardless of its size.

Type: `string`

Default: `""`

```yaml
# Examples

period: 1s

period: 1m

period: 500ms
```


### **`batching.jitter`**

A non-negative factor that adds random delay to batch flush intervals, where delay is determined uniformly at random between 0 and jitter \* period. For example, with `period: 100ms` and `jitter: 0.1`, each flush will be delayed by a random duration between 0-10ms.

Type: `float`

Default: `0`

```yaml
# Examples

jitter: 0.01

jitter: 0.1

jitter: 1
```


### **`batching.check`**

A Bloblang query that should return a boolean value indicating whether a message should end a batch.

Type: `string`

Default: `""`

```yaml
# Examples

check: this.type == "end_of_transaction"
```


### **`batching.processors`**

A list of processors to apply to a batch as it is flushed. This allows you to aggregate and archive the batch however you see fit. Please note that all resulting messages are flushed as a single batch, therefore splitting the batch into smaller batches using these processors is a no-op.

Type: `array`

```yaml
# Examples

processors:
  - archive:
      format: concatenate

processors:
  - archive:
      format: lines

processors:
  - archive:
      format: json_array
```


### **`region`**

The AWS region to target.

Type: `string`

Default: `""`


### **`endpoint`**

Allows you to specify a custom endpoint for the AWS API.

Type: `string`

Default: `""`


### **`credentials`**

Optional manual configuration of AWS credentials to use. More information can be found in [this document](/resources/stacks/bento/guids/aws/).

Type: `object`


### **`credentials.profile`**

A profile from `~/.aws/credentials` to use.

Type: `string`

Default: `""`


### **`credentials.id`**

The ID of credentials to use.

Type: `string`

Default: `""`


### **`credentials.secret`**

The secret for the credentials being used.

!!! warning "Secret"

      This field contains sensitive information that usually shouldn't be added to a config directly, read [Secret](/resources/stacks/bento/configurations/secrets/) page for more info.

Type: `string`

Default: `""`


### **`credentials.token`**

The token for the credentials being used, required when using short term credentials.

Type: `string`

Default: `""`


### **`credentials.from_ec2_role`**

Use the credentials of a host EC2 machine configured to assume an [IAM role associated with the instance](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html).

Type: `bool`

Default: `false`

Requires version 1.0.0 or newer


### **`credentials.role`**

A role ARN to assume.

Type: `string`

Default: `""`


### **`credentials.role_external_id`**

An external ID to provide when assuming a role.

Type: `string`

Default: `""`

