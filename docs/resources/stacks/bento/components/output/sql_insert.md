# sql_insert
Inserts a row into an SQL database for each message. This processor was introduced in version 1.0.0.


## YAML Configuration

### **Common Config**
```yaml
# Common config fields, showing default values

output:
  label: ""
  sql_insert:
    driver: "" # No default (required)
    dsn: clickhouse://username:password@host1:9000,host2:9000/database?dial_timeout=200ms&max_execution_time=60 # No default (required)
    table: foo # No default (required)
    columns: [] # No default (required)
    args_mapping: root = [ this.cat.meow, this.doc.woofs[0] ] # No default (required)
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
  sql_insert:
    driver: "" # No default (required)
    dsn: clickhouse://username:password@host1:9000,host2:9000/database?dial_timeout=200ms&max_execution_time=60 # No default (required)
    table: foo # No default (required)
    columns: [] # No default (required)
    args_mapping: root = [ this.cat.meow, this.doc.woofs[0] ] # No default (required)
    prefix: "" # No default (optional)
    suffix: ON CONFLICT (name) DO NOTHING # No default (optional)
    max_in_flight: 64
    init_files: [] # No default (optional)
    init_statement: | # No default (optional)
      CREATE TABLE IF NOT EXISTS some_table (
        foo varchar(50) not null,
        bar integer,
        baz varchar(50),
        primary key (foo)
      ) WITHOUT ROWID;
    init_verify_conn: false
    conn_max_idle_time: "" # No default (optional)
    conn_max_life_time: "" # No default (optional)
    conn_max_idle: 2
    conn_max_open: 0 # No default (optional)
    secret_name: "" # No default (optional)
    iam_enabled: false
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
    batching:
      count: 0
      byte_size: 0
      period: ""
      jitter: 0
      check: ""
      processors: [] # No default (optional)
```

## Examples

**Table Insert (MySQL)**

Rows can be inserted into a MySQL database by assigning values to by populating the columns id, name and topic with values extracted from messages and metadata:

```yaml
output:
  sql_insert:
    driver: mysql
    dsn: foouser:foopassword@tcp(localhost:3306)/foodb
    table: footable
    columns: [ id, name, topic ]
    args_mapping: |
      root = [
        this.user.id,
        this.user.name,
        metadata("kafka_topic"),
      ]
```

## Fields



### **`driver`**

A database **driver** to use.

Type: `string`
Options: `mysql`, `postgres`, `clickhouse`, `mssql`, `sqlite`, `oracle`, `snowflake`, `trino`, `gocosmos`, `spanner`.

### **`dsn`**

A Data Source Name to identify the target database.

### **Drivers**

The following is a list of supported drivers, their placeholder style, and their respective DSN formats:

<div style="text-align: center;" markdown="1">

| Driver     | Data Source Name Format                                                                                                                                     |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| clickhouse | `clickhouse://[username[:password]@][netloc][:port]/dbname[?param1=value1&...&paramN=valueN]`                                                               |
| mysql      | `[username[:password]@][protocol[(address)]]/dbname[?param1=value1&...&paramN=valueN]`                                                                      |
| postgres   | `postgres://[user[:password]@][netloc][:port][/dbname][?param1=value1&...]`                                                                                 |
| mssql      | `sqlserver://[user[:password]@][netloc][:port][?database=dbname&param1=value1&...]`                                                                         |
| sqlite     | `file:/path/to/filename.db[?param&=value1&...]`                                                                                                             |
| oracle     | `oracle://[username[:password]@][netloc][:port]/service_name?server=server2&server=server3`                                                                 |
| snowflake  | `username[:password]@account_identifier/dbname/schemaname[?param1=value&...&paramN=valueN]`                                                                |
| spanner    | `projects/[project]/instances/[instance]/databases/dbname`                                                                                                  |
| trino      | `http[s]://user[:pass]@host[:port][?parameters]`                                                                                                            |
| gocosmos   | `AccountEndpoint=<cosmosdb-endpoint>;AccountKey=<cosmosdb-account-key>[;TimeoutMs=<timeout-in-ms>][;Version=<cosmosdb-api-version>][;DefaultDb/Db=<db-name>][;AutoId=<true/false>][;InsecureSkipVerify=<true/false>]` |

</div>

!!! info
        Please note that the postgres driver enforces SSL by default, user can override this with the parameter `sslmode=disable` if required.

The `snowflake` driver supports multiple DSN formats. Please consult [the docs](https://pkg.go.dev/github.com/snowflakedb/gosnowflake#hdr-Connection_String) for more details. 
For key pair authentication, the DSN has the following format: `<snowflake_user>@<snowflake_account>/<db_name>/<schema_name>?warehouse=<warehouse>&role=<role>&authenticator=snowflake_jwt&privateKey=<base64_url_encoded_private_key>`, where the value for the privateKey parameter can be constructed from an unencrypted RSA private key `file rsa_key.p8` using `openssl enc -d -base64 -in rsa_key.p8 | basenc --base64url -w0` (user can use `gbasenc` insted of `basenc` on OSX if user install `coreutils` via Homebrew). 
If user have a password-encrypted private key, user can decrypt it using `openssl pkcs8 -in rsa_key_encrypted.p8 -out rsa_key.p8`. Also, make sure fields such as the username are URL-encoded.

The [`gocosmos`](https://pkg.go.dev/github.com/microsoft/gocosmos) driver is still experimental, but it has support for hierarchical partition keys as well as cross-partition queries. Please refer to the SQL notes for details.

Type: `string`


```bash
# Examples

dsn: clickhouse://username:password@host1:9000,host2:9000/database?dial_timeout=200ms&max_execution_time=60

dsn: foouser:foopassword@tcp(localhost:3306)/foodb

dsn: postgres://foouser:foopass@localhost:5432/foodb?sslmode=disable

dsn: oracle://foouser:foopass@localhost:1521/service_name
```

### **`table`**

The table to insert to.

Type: `string`

```yaml
# Examples

table: foo
```

### **`columns`**
A list of columns to insert.

Type: `array`

```yaml
# Examples

columns:
  - foo
  - bar
  - baz
```

### **`args_mapping`**

A Bloblang mapping which should evaluate to an array of values matching in size to the number of columns specified.

Type: `string`

```go
# Examples

args_mapping: root = [ this.cat.meow, this.doc.woofs[0] ]

args_mapping: root = [ metadata("user.id").string() ]
```

### **`prefix`**

An optional prefix to prepend to the insert query (before INSERT).

Type: `string`

### **`suffix`**

An optional suffix to append to the insert query.

Type: `string`


```yaml
# Examples

suffix: ON CONFLICT (name) DO NOTHING
```

### **`max_in_flight`**

The maximum number of inserts to run in parallel.

Type: `int`

Default: `64`

### **`init_files`**

An optional list of file paths containing SQL statements to execute immediately upon the first connection to the target database. This is a useful way to initialize tables before processing data. Glob patterns are supported, including super globs (double star).

Care should be taken to ensure that the statements are idempotent, and therefore would not cause issues when run multiple times after service restarts. If both `init_statement` and `init_files` are specified the `init_statement` is executed after the `init_files`.

If a statement fails for any reason a warning log will be emitted but the operation of this component will not be stopped.

Type: `array`. It requires version 1.0.0 or newer.

```yaml
# Examples

init_files:
  - ./init/*.sql

init_files:
  - ./foo.sql
  - ./bar.sql
```

### **`init_statement`**

An optional SQL statement to execute immediately upon the first connection to the target database. This is a useful way to initialise tables before processing data. Care should be taken to ensure that the statement is idempotent, and therefore would not cause issues when run multiple times after service restarts.

If both `init_statement` and `init_files` are specified the `init_statement` is executed after the `init_files`.

If the statement fails for any reason a warning log will be emitted but the operation of this component will not be stopped.

Type: `string`

Requires version 1.0.0 or newer

```yaml
# Examples

init_statement: |2
  CREATE TABLE IF NOT EXISTS some_table (
    foo varchar(50) not null,
    bar integer,
    baz varchar(50),
    primary key (foo)
  ) WITHOUT ROWID;
```

### **`init_verify_conn`**

Whether to verify the database connection on startup by performing a simple ping, by default this is disabled.

Type: `bool`

Default: `false`

Requires version 1.2.0 or newer

### **`conn_max_idle_time`**

An optional maximum amount of time a connection may be idle. Expired connections may be closed lazily before reuse. If value <= 0, connections are not closed due to a connections idle time.

Type: `string`

### **`conn_max_life_time`**

An optional maximum amount of time a connection may be reused. Expired connections may be closed lazily before reuse. If value <= 0, connections are not closed due to a connections age.

Type: `string`

### **`conn_max_idle`**

An optional maximum number of connections in the idle connection pool. If conn_max_open is greater than 0 but less than the new `conn_max_idle`, then the new `conn_max_idle` will be reduced to match the conn_max_open limit. If value <= 0, no idle connections are retained. The default max idle connections is currently 2. This may change in a future release.

Type: `int`

Default: 2

### **`conn_max_open`**

An optional maximum number of open connections to the database. If `conn_max_idle` is greater than 0 and the new conn_max_open is less than `conn_max_idle`, then `conn_max_idle` will be reduced to match the new conn_max_open limit. If value <= 0, then there is no limit on the number of open connections. The default is 0 (unlimited).

Type: `int`



### **`secret_name`**

An optional field that can be used to get the Username + Password from AWS Secrets Manager. This will overwrite the Username + Password in the DSN with the values from the Secret only if the driver is set to postgres.

Type: `string`

Requires version 1.3.0 or newer



### **`iam_enabled`**

An optional field used to generate an IAM authentication token to connect to an Amazon Relational Database (RDS) DB instance. This will overwrite the Password in the DSN with the generated token only if the drivers are mysql or postgres.

Type: `bool`

Default: `false`

Requires version 1.8.0 or newer



### **`region`**

The AWS region to target.

Type: `string`

Default: `""`



### **`endpoint`**

Allows user to specify a custom endpoint for the AWS API.

Type: `string`

Default: `""`



### **`credentials`**

Optional manual configuration of AWS credentials to use. More information can be found in this document.

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

Use the credentials of a host EC2 machine configured to assume an IAM role associated with the instance.

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



### **`batching`**

Allows user to configure a batching policy.

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

A list of processors to apply to a batch as it is flushed. This allows user to aggregate and archive the batch however user sees fit. Please note that all resulting messages are flushed as a single batch, therefore splitting the batch into smaller batches using these processors is a no-op.

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
