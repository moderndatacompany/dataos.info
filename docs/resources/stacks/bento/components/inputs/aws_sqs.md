# aws_sqs

Consume messages from an AWS SQS URL.

## YAML Configurations

### Common Config

```yaml
# Common config fields, showing default values
input:
  label: ""
  aws_sqs:
    url: ""
```

### Advanced Config

```yaml
# All config fields, showing default values
input:
  label: ""
  aws_sqs:
    url: ""
    delete_message: true
    reset_visibility: true
    max_number_of_messages: 10
    wait_time_seconds: 0
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

### Credentials

By default, Bento will use a shared credentials file when connecting to AWS services. It's also possible to set them explicitly at the component level, allowing you to transfer data across accounts. You can find out more in this document.

### Metadata

This input adds the following metadata fields to each message:

```yaml
- sqs_message_id
- sqs_receipt_handle
- sqs_approximate_receive_count
- All message attributes
```

You can access these metadata fields using [function interpolation](../../configurations/interpolation.md).

## Fields

### `url`

The SQS URL to consume from.

Type: `string`

Default: `""`

---

### `delete_message`

Whether to delete the consumed message once it is acked. Disabling allows you to handle the deletion using a different mechanism.

Type: `bool`

Default: `true`

---

### `reset_visibility`

Whether to set the visibility timeout of the consumed message to zero once it is nacked. Disabling honors the preset visibility timeout specified for the queue.

Type: `bool`

Default: `true`

---

### `max_number_of_messages`

The maximum number of messages to return on one poll. Valid values: 1 to 10.

Type: `int`

Default: `10`

---

### `wait_time_seconds`

Whether to set the wait time. Enabling this activates long-polling. Valid values: 0 to 20.

Type: `int`

Default: `0`

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

### `credentials.id`

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