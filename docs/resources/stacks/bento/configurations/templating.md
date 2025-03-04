# Templating

> 🗣 EXPERIMENTAL: Templates are an experimental feature and, therefore, subject to change outside of major version releases.


Templates are a way to define new Bento components (similar to plugins) that are implemented by generating a Bento config snippet from pre-defined parameter fields. This is useful when a common pattern of Bento configuration is used but with varying parameters each time.

A template is defined in a YAML file that can be imported when Bento runs using the flag `-t`:

```bash
bento -t "./templates/*.yaml" -c ./config.yaml
```

The template describes the type of component and configuration fields that can be used to customize it, followed by a [Bloblang mapping](../bloblang.md) that translates an object containing those fields into a bento config structure. This allows you to use logic to generate more complex configurations:

## Template

```yaml
name: aws_sqs_list
type: input

fields:
  - name: urls
    type: string
    kind: list
  - name: region
    type: string
    default: us-east-1

mapping: |
  root.broker.inputs = this.urls.map_each(url -> {
    "aws_sqs": {
      "url": url,
      "region": this.region,
    }
  })
```

## Config

```yaml
input:
  aws_sqs_list:
    urls:
      - https://sqs.us-east-2.amazonaws.com/123456789012/MyQueue1
      - https://sqs.us-east-2.amazonaws.com/123456789012/MyQueue2

pipeline:
  processors:
    - mapping: |
        root.id = uuid_v4()
        root.foo = this.inner.foo
        root.body = this.outer
```

## Result

```yaml
input:
  broker:
    inputs:
      - aws_sqs:
          url: https://sqs.us-east-2.amazonaws.com/123456789012/MyQueue1
          region: us-east-1
      - aws_sqs:
          url: https://sqs.us-east-2.amazonaws.com/123456789012/MyQueue2
          region: us-east-1

pipeline:
  processors:
    - mapping: |
        root.id = uuid_v4()
        root.foo = this.inner.foo
        root.body = this.outer
```

## Fields

The schema of a template file is as follows:

### `name`

The name of the component this template will create.

Type: `string`

---

### `type`

The type of the component this template will create.

Type: `string`

Options: `cache`, `input`, `output`, `processor`, `rate_limit`.

---

### `status`

The stability of the template describing the likelihood that the configuration spec of the template, or its behavior, will change.

Type: `string`

Default: `"stable"`

| Option | Summary |
| --- | --- |
| stable | This template is stable and will therefore not change in a breaking way outside of major version releases. |
| beta | This template is beta and will therefore not change in a breaking way unless a major problem is found. |
| experimental | This template is experimental and therefore subject to breaking changes outside of major version releases. |

### `categories`

An optional list of tags, which are used for arbitrarily grouping components in the documentation.

Type: list of `string`

Default: `[]`

---

### `summary`

A short summary of the component.

Type: `string`

Default: `""`

---

### `description`

A longer form description of the component and how to use it.

Type: `string`

Default: `""`

---

### `fields`

The configuration fields of the template, fields specified here, will be parsed from a Bento config and will be accessible from the template mapping.

Type: list of `object`

---

### `fields[].name`

The name of the field.

Type: `string`

---

### `fields[].description`

A description of the field.

Type: `string`

Default: `""`

---

### `fields[].type`

The scalar type of the field.

Type: `string`

| Option | Summary |
| --- | --- |
| string | standard string type |
| int | standard integer type |
| float | standard float type |
| bool | a boolean true/false |
| unknown | allows for nesting arbitrary configuration inside of a field |

---

### `fields[].kind`

The kind of the field.

Type: `string`

Default: `"scalar"`

Options: `scalar`, `map`, `list`.

---

### `fields[].default`

An optional default value for the field. If a default value is not specified, then a configuration without the field is considered incorrect.

Type: `unknown`

---

### `fields[].advanced`

Whether this field is considered advanced.

Type: `bool`

Default: `false`

---

### `mapping`

A [Bloblang](../bloblang.md) mapping that translates the fields of the template into a valid Bento configuration for the target component type.

Type: `string`

---

### `metrics_mapping`

An optional [Bloblang mapping](../bloblang.md) that allows you to rename or prevent certain metrics paths from being exported. For more information, check out the [metrics documentation](../components/metrics.md). When metric paths are created, renamed, and dropped, a trace log is written, enabling TRACE level logging is, therefore, a good way to diagnose path mappings.

Invocations of this mapping are able to reference a variable $label in order to obtain the value of the label provided to the template config. This allows you to match labels with the root of the config.

Type: `string`

Default: `""`

```yaml
# Examples

metrics_mapping: this.replace("input", "source").replace("output", "sink")

metrics_mapping: |-
  root = if ![
    "input_received",
    "input_latency",
    "output_sent"
  ].contains(this) { deleted() }
```

---

### `tests`

Optional unit test definitions for the template that verify certain configurations produce valid configs. These tests are executed with the command `bento template lint`.

Type: list of `object`

Default: `[]`

---

### `tests[].name`

A name to identify the test.

Type: `string`

---

### `tests[].config`

A configuration to run this test with, the config resulting from applying the template with this config, will be linted.

Type: `object`

---

### `tests[].expected`

An optional configuration describing the expected result of applying the template, when specified the result will be diffed and any mismatching fields will be reported as a test error.

Type: `object`