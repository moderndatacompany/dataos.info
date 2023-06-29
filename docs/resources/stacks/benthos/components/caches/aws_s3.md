# aws_s3

Tags: AWS

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

## Fields[](https://www.benthos.dev/docs/components/caches/aws_s3#fields)

### `bucket`[](https://www.benthos.dev/docs/components/caches/aws_s3#bucket)

The S3 bucket to store items in.

**Type:** `string`


**Type:** `string`

**Default:** `""`

---

### `credentials.token`[](https://www.benthos.dev/docs/components/caches/aws_s3#credentialstoken)

The token for the credentials being used, required when using short-term credentials.

**Type:** `string`

**Default:** `""`

---

### `credentials.from_ec2_role`[](https://www.benthos.dev/docs/components/caches/aws_s3#credentialsfrom_ec2_role)

Use the credentials of a host EC2 machine configured to assume [an IAM role associated with the instance](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html).

**Type:** `bool`

**Default:** `false`

---

### `credentials.role`[](https://www.benthos.dev/docs/components/caches/aws_s3#credentialsrole)

A role ARN to assume.

**Type:** `string`

**Default:** `""`

---

### `credentials.role_external_id`[](https://www.benthos.dev/docs/components/caches/aws_s3#credentialsrole_external_id)

An external ID to provide when assuming a role.

**Type:** `string`

**Default:** `""`