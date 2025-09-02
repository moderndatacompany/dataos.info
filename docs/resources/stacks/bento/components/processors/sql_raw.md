# `sql_raw`

Bento now supports **Depot UDL** in the `sql_raw` processor as `dataos_sql_raw`, allowing dynamic connections to databases instead of using static DSNs. This makes your services more portable, secure, and easier to configure across environments.

Earlier, database connections required embedding a **static DSN** string directly in configuration. With **Depot UDL**, you can now reference database connections through the DataOS platform, providing consistent access with fine-grained ACL control.


## Querying Postgres with Depot UDL

While building a **data service** that accepts an HTTP request with a `device_id`, looks up corresponding records in a Postgres table (`table_entity`), and returns the results as an enriched JSON response.

## Sample YAML Manifest

Below is a sample YAML configuration for deploying bento service using `dataos_sql_raw` processor:

```yaml
version: v1
name: testservicebento
type: service

service:
  title: 
  replicas: 1
  servicePort: 9876
  metricPort: 8093
  envs:
    LOG_LEVEL: "INFO"
  compute: runnable-default
  ingress: 
    enabled: true
    path: /random-user
    noAuthentication: true  
  resources:
    requests:
      cpu: 100m
      memory: 128Mi
    limits:
      cpu: 2000m
      memory: 1024Mi      
  stack: ${{bento:4.0}}               # dataos stack with version
  logLevel: INFO

  stackSpec:   
    input:
      label: "http_input"
      http_server:
        address: "0.0.0.0:9876"
        path: /random-user
        allowed_verbs:
          - POST
        timeout: 5s
        rate_limit: ""

    pipeline:
      processors:
        - log:
            level: "INFO"
            message: "input json: ${!json()}"
        - branch:
            request_map: root.id = this.device_id
            processors:
              - dataos_sql_raw:
                  address: ${{dataos://metisdb:public/table_entity?acl=rw}}
                  query: "SELECT * FROM table_entity where id = $1"
                  args_mapping: '[this.id]'
            result_map: root.table_result = json()
        - log:
            level: "INFO"
            message: "Final json output event: ${!json()}"

    output:
      sync_response: {}
```

!!! Info

    Please replace the placeholders such as `<Stack Version>` and `<Depot UDL>` with the actual version number of the stack and the specific Depot UDL relevant to your environment.

## Running the Service

When applying the manifest, you must disable variable interpolation to ensure UDL works correctly:

```bash

dataos-ctl resource apply -f {{path of the manifestfile.yaml}} --disable-interpolation

```

## Field

### **`address`**

The address of the Depot or UDL to connect to with the access control level `acl`.

Type: `string`



### **`query`**

The query to execute. The style of placeholder to use depends on the driver, some drivers require question marks (?) whereas others expect incrementing dollar signs ($1, $2, and so on) or colons (:1, :2 and so on). The style to use is outlined in this table:

| **Driver** | **Placeholder Style** |
| ---------- | --------------------- |
| `clickhouse` | Dollar sign           |
| `mysql`      | Question mark         |
| `postgres`   | Dollar sign           |
| `mssql`      | Question mark         |
| `sqlite`     | Question mark         |
| `oracle`     | Colon                 |
| `snowflake`  | Question mark         |
| `spanner`    | Question mark         |
| `trino`      | Question mark         |
| `gocosmos`   | Colon                 |



Type: `string`

**Examples**

```yaml

query: INSERT INTO footable (foo, bar, baz) VALUES (?, ?, ?);
# Or
query: SELECT * FROM footable WHERE user_id = $1;

```

### **`args_mapping`**

An optional Bloblang mapping which should evaluate to an array of values matching in size to the number of placeholder arguments in the field query.

Type: `string`

**Examples**

```yaml

args_mapping: root = [ this.cat.meow, this.doc.woofs[0] ]
# Or
args_mapping: root = [ metadata("user.id").string() ]

```

