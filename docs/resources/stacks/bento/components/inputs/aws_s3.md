# aws_s3

Downloads objects within an Amazon S3 bucket, optionally filtered by a prefix, either by walking the items in the bucket or by streaming upload notifications in real-time.

## YAML Configurations

### Common Config

```yaml
# Common config fields, showing default values
input:
  label: ""
  aws_s3:
    bucket: ""
    prefix: ""
    codec: all-bytes
    sqs:
      url: ""
      key_path: Records.*.s3.object.key
      bucket_path: Records.*.s3.bucket.name
      envelope_path: ""
```

### Advanced Config

```yaml
# All config fields, showing default values
input:
  label: ""
  aws_s3:
    bucket: ""
    prefix: ""
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
    force_path_style_urls: false
    delete_objects: false
    codec: all-bytes
    max_buffer: 1000000
    sqs:
      url: ""
      endpoint: ""
      key_path: Records.*.s3.object.key
      bucket_path: Records.*.s3.bucket.name
      envelope_path: ""
      delay_period: ""
      max_messages: 10
```

## Streaming Objects on Upload with SQS

A common pattern for consuming S3 objects is to emit upload notification events from the bucket either directly to an SQS queue or to an SNS topic that is consumed by an SQS queue and then have your consumer listen for events that prompt it to download the newly uploaded objects. More information about this pattern and how to set it up can be found [here.](https://docs.aws.amazon.com/AmazonS3/latest/dev/ways-to-add-notification-config-to-bucket.html)

Bento is able to follow this pattern when you configure an `sqs.url`, where it consumes events from SQS and only downloads object keys received within those events. In order for this to work, Bento needs to know where within the event the key and bucket names can be found, specified as [dot paths](../../configurations/fields_paths.md) with the fields `sqs.key_path` and `sqs.bucket_path`. The default values for these fields should already be correct when following the guide above.

If your notification events are being routed to SQS via an SNS topic, then the events will be enveloped by SNS, in which case you also need to specify the field `sqs.envelope_path`, which in the case of SNS to SQS will usually be `Message`.

When using SQS, please make sure you have sensible values for `sqs.max_messages` and also the visibility timeout of the queue itself. When Bento consumes an S3, object, the SQS message that triggered it is not deleted until the S3 object has been sent onwards. This ensures at-least-once crash resiliency but also means that if the S3 object takes longer to process than the visibility timeout of your queue, then the same objects might be processed multiple times.

## Downloading Large Files

When downloading large files, it's often necessary to process it in streamed parts in order to avoid loading the entire file in memory at a given time. In order to do this, a `codec` can be specified that determines how to break the input into smaller individual messages.

## Credentials

By default, Bento will use a shared credentials file when connecting to AWS services. It's also possible to set them explicitly at the component level, allowing you to transfer data across accounts. 

## Metadata

This input adds the following metadata fields to each message:

```
- s3_key
- s3_bucket
- s3_last_modified_unix
- s3_last_modified (RFC3339)
- s3_content_type
- s3_content_encoding
- All user defined metadata
```

You can access these metadata fields using [function interpolation](../../configurations/interpolation.md). Note that user-defined metadata is case insensitive within AWS, and it is likely that the keys will be received in a capitalized form, if you wish to make them consistent, you can map all metadata keys to lower or uppercase using a Bloblang mapping, such as `meta = meta().map_each_key(key -> key.lowercase())`.

## Fields

### `bucket`

The bucket to consume from. If the field `sqs.url` is specified, this field is optional.

Type: `string`

Default: `""`

---

### `prefix`

An optional path prefix, if set, only objects with the prefix are consumed when walking a bucket.

Type: `string`

Default: `""`

---

### `region`

The AWS region to target.

Type: `string`

Default: `""`

---

### `endpoint`

Allows you to specify a custom endpoint for the AWS API.

Type: `string`

Default: `""`

---

### `credentials`

Optional manual configuration of AWS credentials to use. 

Type: `object`

---

### `credentials.profile`

A profile from `~/.aws/credentials` to use.

Type: `string`

Default: `""`

---

### `credentials.id

The ID of credentials to use.

Type: `string`

Default: `""`

---

### `credentials.secret`

The secret for the credentials being used.

Type: `string`

Default: `""`

---

### `credentials.token`

The token for the credentials being used required when using short-term credentials.

Type: `string`

Default: `""`

---

### `credentials.from_ec2_role`

Use the credentials of a host EC2 machine configured to assume an IAM role associated with the instance.

Type: `bool`

Default: `false`

---

### `credentials.role`

A role ARN to assume.

Type: `string`

Default: `""`

---

### `credentials.role_external_id`

An external ID to provide when assuming a role.

Type: `string`

Default: `""`

---

### `force_path_style_urls`

Forces the client API to use path-style URLs for downloading keys, which is often required when connecting to custom endpoints.

Type: `bool`

Default: `false`

---

### `delete_objects`

Whether to delete downloaded objects from the bucket once they are processed.

Type: `bool`

Default: `false`

---

### `codec`

The way in which the bytes of a data source should be converted into discrete messages, codecs are useful for specifying how large files or continuous streams of data might be processed in small chunks rather than loading it all in memory. It's possible to consume lines using a custom delimiter with the `delim:x` codec, where x is the character sequence custom delimiter. Codecs can be chained with `/`, for example, a gzip compressed CSV file can be consumed with the codec `gzip/csv`.

Type: `string`

Default: `"all-bytes"`

| Option | Summary |
| --- | --- |
| auto | EXPERIMENTAL: Attempts to derive a codec for each file based on information such as the extension. For example, a .tar.gz file would be consumed with the gzip/tar codec. Defaults to all-bytes. |
| all-bytes | Consume the entire file as a single binary message. |
| avro-ocf:marshaler=x | EXPERIMENTAL: Consume a stream of Avro OCF datum. The marshaler parameter is optional and has the options: goavro (default), json. Use goavro if OCF contains logical types. |
| chunker:x | Consume the file in chunks of a given number of bytes. |
| csv | Consume structured rows as comma-separated-values, the first row must be a header row. |
| csv:x | Consume structured rows as values separated by a custom delimiter, the first row must be a header row. The custom delimiter must be a single character, e.g. the codec "csv:\t" would consume a tab delimited file. |
| delim:x | Consume the file in segments divided by a custom delimiter. |
| gzip | Decompress a gzip file, this codec should precede another codec, e.g. gzip/all-bytes, gzip/tar, gzip/csv, etc. |
| lines | Consume the file in segments divided by linebreaks. |
| multipart | Consumes the output of another codec and batches messages together. A batch ends when an empty message is consumed. For example, the codec lines/multipart could be used to consume multipart messages where an empty line indicates the end of each batch. |
| regex:(?m)^\d\d:\d\d:\d\d | Consume the file in segments divided by regular expression. |
| tar | Parse the file as a tar archive, and consume each file of the archive as a message. |

```yaml
# Examples

codec: lines

codec: "delim:\t"

codec: delim:foobar

codec: gzip/csv
```

---

### `max_buffer`

The largest token size expected when consuming objects with a tokenized codec such as `lines`.

Type: `int`

Default: `1000000`

---

### `sqs`

Consume SQS messages in order to trigger key downloads.

Type: `object`

---

### `sqs.url`

An optional SQS URL to connect to. When specified, this queue will control which objects are downloaded.

Type: `string`

Default: `""`

---

### `sqs.endpoint`

A custom endpoint to use when connecting to SQS.

Type: `string`

Default: `""`

---

### `sqs.key_path`

A dot path whereby object keys are found in SQS messages.

Type: `string`

Default: `"Records.*.s3.object.key"`

---

### `sqs.bucket_path`

A dot path whereby the bucket name can be found in SQS messages.

Type: `string`

Default: `"Records.*.s3.bucket.name"`

---

### `sqs.envelope_path`

A dot path of a field to extract an enveloped JSON payload for further extracting the key and bucket from SQS messages. This is specifically useful when subscribing an SQS queue to an SNS topic that receives bucket events.

Type: `string`

Default: `""`

```yaml
# Examples

envelope_path: Message
```

---

### `sqs.delay_period`

An optional period of time to wait from when a notification was originally sent to when the target key download is attempted.

Type: `string`

Default: `""`

```yaml
# Examples

delay_period: 10s

delay_period: 5m

```

---

### `sqs.max_messages`

The maximum number of SQS messages to consume from each request.

Type: `int`

Default: `10`