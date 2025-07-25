# azure_blob_storage

!!! Warning "BETA"

        This component is mostly stable but breaking changes could still be made outside of major version releases if a fundamental problem with the component is found.

Sends message parts as objects to an Azure Blob Storage Account container. Each object is uploaded with the filename specified with the container field. This processor was introduced in version 1.0.0.

## YAML Configuration

### **Common Config**
```yaml
# Common config fields, showing default values

output:
  label: ""
  azure_blob_storage:
    storage_account: ""
    storage_access_key: ""
    storage_connection_string: ""
    storage_sas_token: ""
    container: messages-${!timestamp("2006")} # No default (required)
    path: ${!count("files")}-${!timestamp_unix_nano()}.txt
    max_in_flight: 64
```

### **Full Config**

```yaml

# All config fields, showing default values
output:
  label: ""
  azure_blob_storage:
    storage_account: ""
    storage_access_key: ""
    storage_connection_string: ""
    storage_sas_token: ""
    container: messages-${!timestamp("2006")} # No default (required)
    path: ${!count("files")}-${!timestamp_unix_nano()}.txt
    blob_type: BLOCK
    public_access_level: PRIVATE
    max_in_flight: 64


```

In order to have a different path for each object you should use function interpolations described [here](/resources/stacks/bento/configurations/interpolation/), which are calculated per message of a batch.

Supports multiple authentication methods but only one of the following is required:

- `storage_connection_string`
- `storage_account` and `storage_access_key`
- `storage_account` and `storage_sas_token`
- `storage_account` to access via [DefaultAzureCredential](https://pkg.go.dev/github.com/Azure/azure-sdk-for-go/sdk/azidentity#DefaultAzureCredential)

If multiple are set then the `storage_connection_string` is given priority.

If the `storage_connection_string` does not contain the `AccountName` parameter, please specify it in the `storage_account` field.

## Performance

This output benefits from sending multiple messages in flight in parallel for improved performance. You can tune the max number of in flight messages (or message batches) with the field max_in_flight.

## Fields

### **`storage_account`**

The storage account to access. This field is ignored if storage_connection_string is set.

Type: `string`
Default: `""`

### **`storage_access_key`**

The storage account access key. This field is ignored if storage_connection_string is set.

Type: `string`
Default: `""`

### **`storage_connection_string`**

A storage account connection string. This field is required if storage_account and storage_access_key / storage_sas_token are not set.

Type: `string`
Default: `""`

### **`storage_sas_token`**

The storage account SAS token. This field is ignored if storage_connection_string or storage_access_key are set.

Type: `string`
Default: `""`

### **`container`**
The container for uploading the messages to. This field supports [interpolation functions](/resources/stacks/bento/configurations/interpolation/#bloblang-queries).

Type: `string`

```yaml
# Examples

container: messages-${!timestamp("2006")}
```

### **`path`**

The path of each message to upload. This field supports [interpolation functions](/resources/stacks/bento/configurations/interpolation/#bloblang-queries).

Type: `string`
Default: `"${!count(\"files\")}-${!timestamp_unix_nano()}.txt"`

```yaml
# Examples

path: ${!count("files")}-${!timestamp_unix_nano()}.json

path: ${!metadata("kafka_key")}.json

path: ${!json("doc.namespace")}/${!json("doc.id")}.json
```


### **`blob_type`**

Block and Append blobs are comprised of blocks, and each blob can support up to 50,000 blocks. The default value is +"BLOCK"+.` This field supports [interpolation functions](/resources/stacks/bento/configurations/interpolation/#bloblang-queries).

Type: `string`

Default: `"BLOCK"`

Options: `BLOCK`, `APPEND`.

### **`public_access_level`**

The container's public access level. The default value is PRIVATE. This field supports [interpolation functions](/resources/stacks/bento/configurations/interpolation/#bloblang-queries).

Type: `string`

Default: `"PRIVATE"`

Options: `PRIVATE`, `BLOB`, `CONTAINER`.

### **`max_in_flight`**

The maximum number of messages to have in flight at a given time. Increase this to improve throughput.

Type: `int`

Default: `64`