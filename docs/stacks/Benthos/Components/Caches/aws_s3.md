# aws_s3

Stores each item in an S3 bucket as a file, where an item ID is the path of the item within the bucket.

## YAML Configurations

### Common Config

```yaml
# Common config fields, showing default values
label: ""
aws_s3:
  bucket: ""
  content_type: application/octet-stream
```

It is not possible to atomically upload S3 objects exclusively when the target does not already exist; therefore, this cache is not suitable for deduplication.

## Fields

### `bucket`

The S3 bucket to store items in.

Type: `string`

---

### `content_type`

The content type to set for each item.

Type: `string`

Default: `"application/octet-stream"`

---

### `force_path_style_urls`

Forces the client API to use path-style URLs, which helps when connecting to custom endpoints.

Type: `bool`

Default: `false`

---

### `retries`

Determine time intervals and cut-offs for retry attempts.

Type: `object`

---

### `retries.initial_interval`

The initial period to wait between retry attempts.

Type: `string`

Default: `"1s"`

```yaml
# Examples

initial_interval: 50ms

initial_interval: 1s
```

---

### `retries.max_interval`

The maximum period to wait between retry attempts

Type: `string`

Default: `"5s"`

```yaml
# Examples

max_interval: 5s

max_interval: 1m
```

---

### `retries.max_elapsed_time`

The maximum overall period of time to spend on retry attempts before the request is aborted.

Type: `string`

Default: `"30s"`

```yaml
# Examples

max_elapsed_time: 1m

max_elapsed_time: 1h
```

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

Optional manual configuration of AWS credentials to use. More information can be found in this document.

Type: `object`

---

### `credentials.profile`

A profile from `~/.aws/credentials` to use.

Type: `string`

Default: `""`

---

### `credentials.id`

The ID of credentials to use.

Type: `string`

Default: `""`

---

### `credentials.secret`

The secret for the credentials being used.

> 🗣 SECRET
This field contains sensitive information that usually shouldn't be added to a config directly, read our secrets page for more info.


Type: `string`

Default: `""`

---

### `credentials.token`

The token for the credentials being used, required when using short-term credentials.

Type: `string`

Default: `""`

---

### `credentials.from_ec2_role`

Use the credentials of a host EC2 machine configured to assume [an IAM role associated with the instance](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html).

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