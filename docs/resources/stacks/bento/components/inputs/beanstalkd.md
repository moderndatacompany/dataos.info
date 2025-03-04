# beanstalkd

> 🗣 EXPERIMENTAL
This component is experimental and, therefore, subject to change or removal outside of major version releases.


Reads messages from a Beanstalkd queue.

```yaml
# Config fields, showing default values
input:
  label: ""
  beanstalkd:
    address: ""
```

## Fields

### `address`

An address to connect to.

Type: `string`

```yaml
# Examples

address: 127.0.0.1:11300
```