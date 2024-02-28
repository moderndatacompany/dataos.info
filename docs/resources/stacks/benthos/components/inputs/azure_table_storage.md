# azure_table_storage

> 🗣 BETA
This component is mostly stable, but breaking changes could still be made outside of major version releases if a fundamental problem with the component is found.


Queries an Azure Storage Account Table, optionally with multiple filters.

## YAML Configurations

### Common Config

```yaml
# Common config fields, showing default values
input:
  label: ""
  azure_table_storage:
    storage_account: ""
    storage_access_key: ""
    storage_connection_string: ""
    table_name: ""
```

### Advanced Config

```yaml
# All config fields, showing default values
input:
  label: ""
  azure_table_storage:
    storage_account: ""
    storage_access_key: ""
    storage_connection_string: ""
    table_name: ""
    filter: ""
    select: ""
    page_size: 1000
```

Queries an Azure Storage Account Table, optionally with multiple filters.

## Metadata

This input adds the following metadata fields to each message:

```yaml
- table_storage_name
- row_num
```

You can access these metadata fields using [function interpolation](../../configurations/interpolation.md).

## Fields

### `storage_account`

The storage account to upload messages to. This field is ignored if  `storage_connection_string` is set.

Type: `string`

Default: `""`

---

### `storage_access_key`

The storage account access key. This field is ignored if `storage_connection_string` is set.

Type: `string`

Default: `""`

---

### `storage_connection_string`

A storage account connection string. This field is required if  `storage_account`  and  `storage_access_key` are not set.

Type: `string`

Default: `""`

---

### `table_name`

The table to read messages from.

Type: `string`

Default: `""`

```yaml
# Examples

table_name: Foo
```

---

### `filter`

OData filter expression. Is not set, all rows are returned. Valid operators are `eq, ne, gt, lt, ge and le`

Type: `string`

Default: `""`

```yaml
# Examples

filter: PartitionKey eq 'foo' and RowKey gt '1000'
```

---

### `select`

Select expression using OData notation. Limits the columns on each record to just those requested.

Type: `string`

Default: `""`

```yaml
# Examples

select: PartitionKey,RowKey,Foo,Bar,Timestamp
```

---

### `page_size`

Maximum number of records to return on each page.

Type: `int`

Default: `1000`

```yaml
# Examples

page_size: "1000"
```