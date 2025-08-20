---
search:
  exclude: true
---

# azure_cosmosdb

!!! warning "EXPERIMENTAL"
        
    This component is experimental and therefore subject to change or removal outside of major version releases.

Creates or updates messages as JSON documents in [Azure CosmosDB](https://learn.microsoft.com/en-us/azure/cosmos-db/introduction).

Introduced in version v4.25.0.


## YAML Configuration

### **Common Config**
```yaml
# Common config fields, showing default values

output:
  label: ""
  azure_cosmosdb:
    endpoint: https://localhost:8081 # No default (optional)
    account_key: '!!!SECRET_SCRUBBED!!!' # No default (optional)
    connection_string: '!!!SECRET_SCRUBBED!!!' # No default (optional)
    database: testdb # No default (required)
    container: testcontainer # No default (required)
    partition_keys_map: root = "blobfish" # No default (required)
    operation: Create
    item_id: ${! json("id") } # No default (optional)
    batching:
      count: 0
      byte_size: 0
      period: ""
      jitter: 0
      check: ""
    max_in_flight: 64
```



### **Full Config**

```yaml

# All config fields, showing default values
output:
  label: ""
  azure_cosmosdb:
    endpoint: https://localhost:8081 # No default (optional)
    account_key: '!!!SECRET_SCRUBBED!!!' # No default (optional)
    connection_string: '!!!SECRET_SCRUBBED!!!' # No default (optional)
    database: testdb # No default (required)
    container: testcontainer # No default (required)
    partition_keys_map: root = "blobfish" # No default (required)
    operation: Create
    patch_operations: [] # No default (optional)
    patch_condition: from c where not is_defined(c.blobfish) # No default (optional)
    auto_id: true
    item_id: ${! json("id") } # No default (optional)
    batching:
      count: 0
      byte_size: 0
      period: ""
      jitter: 0
      check: ""
      processors: [] # No default (optional)
    max_in_flight: 64
```

When creating documents, each message must have the id property (case-sensitive) set (or use auto_id: true). It is the unique name that identifies the document, that is, no two documents share the same id within a logical partition. The id field must not exceed 255 characters. More details can be found [here](https://learn.microsoft.com/en-us/rest/api/cosmos-db/documents).

The `partition_keys` field must resolve to the same value(s) across the entire message batch.

## Credentials
User can use one of the following authentication mechanisms:

- Set the `endpoint` field and the `account_key` field
- Set only the `endpoint` field to use [DefaultAzureCredential](https://pkg.go.dev/github.com/Azure/azure-sdk-for-go/sdk/azidentity#DefaultAzureCredential)
- Set the `connection_string` field

## Batching

CosmosDB limits the maximum batch size to 100 messages and the payload must not exceed 2MB (details [here](https://learn.microsoft.com/en-us/azure/cosmos-db/concepts-limits#per-request-limits)).

## Performance

This output benefits from sending multiple messages in flight in parallel for improved performance. You can tune the max number of in flight messages (or message batches) with the field max_in_flight.

This output benefits from sending messages as a batch for improved performance. Batches can be formed at both the input and output level. You can find out more [in this doc](/resources/stacks/bento/configurations/message_batching/).

## Examples
### **Create documents**

Create new documents in the `blobfish` container with partition key `/habitat`.

```yaml
output:
  azure_cosmosdb:
    endpoint: http://localhost:8080
    account_key: C2y6yDjf5/R+ob0N8A7Cgv30VRDJIWEHLM+4QDU5DE2nQ9nDuVTqobD4b8mGGyPMbIZnqyMsEcaGQy67XIw/Jw==
    database: blobbase
    container: blobfish
    partition_keys_map: root = json("habitat")
    operation: Create
```

### **Patch documents**

Execute the Patch operation on documents from the `blobfish` container.

```yaml
output:
  azure_cosmosdb:
    endpoint: http://localhost:8080
    account_key: C2y6yDjf5/R+ob0N8A7Cgv30VRDJIWEHLM+4QDU5DE2nQ9nDuVTqobD4b8mGGyPMbIZnqyMsEcaGQy67XIw/Jw==
    database: testdb
    container: blobfish
    partition_keys_map: root = json("habitat")
    item_id: ${! json("id") }
    operation: Patch
    patch_operations:
      # Add a new /diet field
      - operation: Add
        path: /diet
        value_map: root = json("diet")
      # Remove the first location from the /locations array field
      - operation: Remove
        path: /locations/0
      # Add new location at the end of the /locations array field
      - operation: Add
        path: /locations/-
        value_map: root = "Challenger Deep"

```


## Fields


### **`endpoint`**
CosmosDB endpoint.

Type: `string`


```yaml
# Examples

endpoint: https://localhost:8081
```

### **`account_key`**

Account key.

!!! warning "Secret"

      This field contains sensitive information that usually shouldn't be added to a config directly, read [Secret](/resources/stacks/bento/configurations/secrets/) page for more info.


Type: `string`


```yaml
# Examples

account_key: C2y6yDjf5/R+ob0N8A7Cgv30VRDJIWEHLM+4QDU5DE2nQ9nDuVTqobD4b8mGGyPMbIZnqyMsEcaGQy67XIw/Jw==

```

### **`connection_string`**
Connection string.

!!! warning "Secret"

      This field contains sensitive information that usually shouldn't be added to a config directly, read [Secret](/resources/stacks/bento/configurations/secrets/) page for more info.

Type: `string`


```yaml
# Examples

connection_string: AccountEndpoint=https://localhost:8081/;AccountKey=C2y6yDjf5/R+ob0N8A7Cgv30VRDJIWEHLM+4QDU5DE2nQ9nDuVTqobD4b8mGGyPMbIZnqyMsEcaGQy67XIw/Jw==;

```

### **`database`**
Database.

Type: `string`


```yaml
# Examples

database: testdb
```


### **`container`**

Container.

Type: `string`


```yaml
# Examples

container: testcontainer
```


### **`partition_keys_map`**

A Bloblang mapping which should evaluate to a single partition key value or an array of partition key values of type string, integer or boolean. Currently, hierarchical partition keys are not supported so only one value may be provided.

Type: `string`


```yaml
# Examples

partition_keys_map: root = "blobfish"

partition_keys_map: root = 41

partition_keys_map: root = true

partition_keys_map: root = null

partition_keys_map: root = json("blobfish").depth
```


### **`operation`**

Operation.

Type: `string`

Default: `"Create"`

|Option |	Summary|
|------- | --------- |
|`Create` |	Create operation.|
|`Delete` |	Delete operation.|
|`Patch` |	Patch operation.|
|`Replace` |	Replace operation.|
|`Upsert` |	Upsert operation.|


### **`patch_operations`**

Patch operations to be performed when operation: Patch .

Type: `array`

### **`patch_operations[].operation`**

Operation.

Type: `string`

Default: `"Add"`

|Option |	Summary|
|------- | --------- |
|`Add` |	Add patch operation.|
|`Increment` |	Increment patch operation.|
|`Remove` |	Remove patch operation.|
|`Replace` |	Replace patch operation.|
|`Set` |	Set patch operation.|


### **`patch_operations[].path`**

Patch operation Path.


Type: `string`


```yaml
# Examples

path: /foo/bar/baz
```


### **`patch_operations[].value_map`**

A Bloblang mapping which should evaluate to a value of any type that is supported by CosmosDB.

Type: `string`


```yaml
# Examples

value_map: root = "blobfish"

value_map: root = 41

value_map: root = true

value_map: root = json("blobfish").depth

value_map: root = [1, 2, 3]
```


### **`patch_condition`**

Patch operation condition. This field supports interpolation functions.

Type: `string`

```yaml
# Examples

patch_condition: from c where not is_defined(c.blobfish)
```

### **`auto_id`**
Automatically set the item id field to a random UUID v4. If the id field is already set, then it will not be overwritten. Setting this to false can improve performance, since the messages will not have to be parsed.

Type: `bool`

Default: `true`

### **`item_id`**
ID of item to replace or delete. Only used by the Replace and Delete operations This field supports interpolation functions.

Type: `string`

```yaml 

# Examples

item_id: ${! json("id") }
```

### **`batching`**

Allows you to configure a batching policy.

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

A number of messages at which the batch should be flushed. If `0` disables count based batching.

Type: `int`

Default: `0`

### **`batching.byte_size`**

An amount of bytes at which the batch should be flushed. If `0` disables size based batching.

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

A non-negative factor that adds random delay to batch flush intervals, where delay is determined uniformly at random between 0 and jitter * period. For example, with period: 100ms and jitter: 0.1, each flush will be delayed by a random duration between 0-10ms.

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
A list of processors to apply to a batch as it is flushed. This allows you to aggregate and archive the batch however you see fit. Please note that all resulting messages are flushed as a single batch, therefore splitting the batch into smaller batches using these processors is a no-op.

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


### **`max_in_flight`**

The maximum number of messages to have in flight at a given time. Increase this to improve throughput.

Type: `int`

Default: `64`

## CosmosDB Emulator

If you wish to run the CosmosDB emulator that is referenced in the documentation here, the following Docker command should do the trick:


```bash
> docker run --rm -it -p 8081:8081 --name=cosmosdb -e AZURE_COSMOS_EMULATOR_PARTITION_COUNT=10 -e AZURE_COSMOS_EMULATOR_ENABLE_DATA_PERSISTENCE=false mcr.microsoft.com/cosmosdb/linux/azure-cosmos-emulator
```

!!! info "Note"

         `AZURE_COSMOS_EMULATOR_PARTITION_COUNT` controls the number of partitions that will be supported by the emulator. The bigger the value, the longer it takes for the container to start up.

Additionally, instead of installing the container self-signed certificate which is exposed via `https://localhost:8081/_explorer/emulator.pem`, user can run mitmproxy like so:

```bash
> mitmproxy -k --mode "reverse:https://localhost:8081"
```

Then user can access the CosmosDB UI via `http://localhost:8080/_explorer/index.html` and use `http://localhost:8080` as the CosmosDB endpoint.