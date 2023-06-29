# cassandra

> 🗣 EXPERIMENTAL
This component is experimental and, therefore, subject to change or removal outside of major version releases.


Executes a find query and creates a message for each row received.

## YAML Configurations

### Common Config

```yaml
# Common config fields, showing default values
input:
  label: ""
  cassandra:
    addresses: []
    query: ""
    timeout: 600ms
```

### Advanced Config

```yaml
# All config fields, showing default values
input:
  label: ""
  cassandra:
    addresses: []
    password_authenticator:
      enabled: false
      username: ""
      password: ""
    disable_initial_host_lookup: false
    query: ""
    max_retries: 0
    backoff:
      initial_interval: ""
      max_interval: ""
    timeout: 600ms
```

## Examples[](https://www.benthos.dev/docs/components/inputs/cassandra/#examples)

### Minimal Select (Cassandra/Scylla)

Let's presume that we have 3 Cassandra nodes, like in this tutorial by Sebastian Sigl from [freeCodeCamp.](https://www.freecodecamp.org/news/the-apache-cassandra-beginner-tutorial/)


Then if we want to select everything from the table users_by_country, we should use the configuration below. If we specify the stdin output, the result will look like:

```json
{"age":23,"country":"UK","first_name":"Bob","last_name":"Sandler","user_email":"[bob@email.com](mailto:bob@email.com)"}
```

This configuration also works for Scylla.

```yaml
input:
  cassandra:
    addresses:
      - 172.17.0.2
    query:
      'SELECT * FROM learn_cassandra.users_by_country'
```

## Fields

### `addresses`

A list of Cassandra nodes to connect to.

Type: `array`

---

### `password_authenticator`

Optional configuration of Cassandra authentication parameters.

Type: `object`

---

### `password_authenticator.enabled`

Whether to use password authentication

Type: `bool`

---

### `password_authenticator.username`

A username

Type: `string`

---

### `password_authenticator.password`

A password

> 🗣 SECRET
This field contains sensitive information that usually shouldn't be added to a config directly, read our secrets page for more info.


Type: `string`

---

### `disable_initial_host_lookup`

If enabled, the driver will not attempt to get host info from the system.peers table. This can speed up queries but will mean that data_centre, rack, and token information will not be available.

Type: `bool`

---

### `query`

A query to execute.

Type: `string`

---

### `max_retries`

The maximum number of retries before giving up on a request.

Type: `int`

---

### `backoff`

Control time intervals between retry attempts.

Type: `object`

---

### `backoff.initial_interval`

The initial period to wait between retry attempts.

Type: `string`

---

### `backoff.max_interval`

The maximum period to wait between retry attempts.

Type: `string`

---

### `timeout`

Sorry! This field is missing documentation.

Type: `string`

Default: `"600ms"`

```yaml
# Examples

timeout: 600ms
```