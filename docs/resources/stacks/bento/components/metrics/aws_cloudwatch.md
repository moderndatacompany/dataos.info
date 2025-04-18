# aws_cloudwatch

Send metrics to AWS CloudWatch using the PutMetricData endpoint.

## YAML Configurations

### Common Config

```yaml
# Common config fields, showing default values
metrics:
  aws_cloudwatch:
    namespace: Bento
  mapping: ""
```

### Advanced Config

```yaml
# All config fields, showing default values
metrics:
  aws_cloudwatch:
    namespace: Bento
    flush_period: 100ms
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
  mapping: ""
```

### Timing Metrics

The smallest timing unit that CloudWatch supports is microseconds; therefore timing metrics are automatically downgraded to microseconds (by dividing delta values by 1000). This conversion will also apply to custom timing metrics produced with a `metric` processor.

### Billing

AWS bills per metric series exported, it is therefore STRONGLY recommended that you reduce the metrics that are exposed with a `mapping` like this:

```yaml
metrics:
  mapping: |
    if ![
      "input_received",
      "input_latency",
      "output_sent",
    ].contains(this) { deleted() }
  aws_cloudwatch:
    namespace: Foo
```

## Fields

### `namespace`

The namespace used to distinguish metrics from other services.

Type: `string`

Default: `"Bento"`

---

### `flush_period`

The period of time between PutMetricData requests.

Type: `string`

Default: `"100ms"`

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

Type: `string`

Default: `""`

---

### `credentials.token`

The token for the credentials being used, required when using short term credentials.

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