# Dataset Commnad Group
You run the following `dataset` commands by appending them to *dataos-ctl dataset*. 

## `add-field`

Add field.

```bash

Usage:
  dataos-ctl dataset add-field [flags]

Flags:
  -a, --address string     Dataset Address
  -t, --datatype string    Datatype of field
  -h, --help               help for add-field
  -k, --keyType string     Datatype of Map-Key
  -n, --name string        Name of new field
  -p, --precision int8     --precision 10 (only for decimal type)
  -s, --scale int8         --scale 1 (only for decimal type) (default 1)
  -v, --valueType string   Datatype of Map-Value
```

## `add-properties`

Add properties.

```bash
Usage:
  dataos-ctl dataset add-properties [flags]

Flags:
  -a, --address string       The address of Dataset
  -h, --help                 help for add-properties
  -p, --properties strings   --properties <property_name>:<property_value>
```

## `create`

Create dataset.

```bash
Usage:
  dataos-ctl dataset create [flags]

Flags:
  -a, --address string        Dataset Address
  -h, --help                  help for create
  -f, --manifestFile string   Manifest file location
```

## `drop`
Drop dataset.

```shell

Usage:
  dataos-ctl dataset drop [flags]

Flags:
  -a, --address string   Dataset Address
  -h, --help             help for drop
  -p, --purge string     Purge Value: true or false (default "false")
```

## `drop-field`

Drop field.

```bash
Usage:
  dataos-ctl dataset drop-field [flags]

Flags:
  -a, --address string   The dataset address
  -h, --help             help for drop-field
  -n, --name string      Name of field
```

## `get`

Get dataset address.

```bash
Usage:
  dataos-ctl dataset get [flags]

Flags:
  -a, --address string   Dataset Address
  -h, --help             help for get
```

## `metadata`
`
Get dataset metadata.

```bash
Usage:
  dataos-ctl dataset metadata [flags]

Flags:
  -a, --address string   The address of Dataset
  -h, --help             help for metadata
```

## `properties`

Get dataset properties.

```bash
Usage:
  dataos-ctl dataset properties [flags]

Flags:
  -a, --address string   The address of Dataset
  -h, --help             help for properties
```

## `remove-properties`

Remove dataset properties.

```bash
Usage:
  dataos-ctl dataset remove-properties [flags]

Flags:
  -a, --address string           The address of Dataset
  -h, --help                     help for remove-properties
  -p, --properties stringArray   --properties <property_name>
```

## `rename-field`

Rename dataset field.

```bash
Usage:
  dataos-ctl dataset rename-field [flags]

Flags:
  -a, --address string   The address of dataset
  -h, --help             help for rename-field
  -n, --name string      Name of existing field
  -m, --newName string   New name for field
```

## `rollback`
Rollback Snapshot

```shell

Usage:
  dataos-ctl dataset rollback [flags]

Flags:
  -a, --address string   The address of Dataset
  -h, --help             help for rollback
  -i, --id string        The snapshot id
```

## `set-metadata`

Set metadata for the dataset.

```bash
Usage:
  dataos-ctl dataset set-metadata [flags]

Flags:
  -a, --address string   The address for dataset.
  -h, --help             help for set-metadata
  -v, --version string   set metadata of dataset
```

## `set-nullable`

Set nullable.

```bash
Usage:
  dataos-ctl dataset set-nullable [flags]

Flags:
  -a, --address string    The address of Dataset
  -h, --help              help for set-nullable
  -n, --name string       Name of field
  -b, --nullable string   true for nullable field, else false
```

## `set-snapshot
`
Set snapshot.

```bash
Usage:
  dataos-ctl dataset set-snapshot [flags]

Flags:
  -a, --address string   The address of Dataset
  -h, --help             help for set-snapshot
  -i, --id string        The snapshot id
```

## `snapshots`

List dataset snapshots.

```bash
Usage:
  dataos-ctl dataset snapshots [flags]

Flags:
  -a, --address string   The address of Dataset
  -h, --help             help for snapshots
```

## `update-field`

Update dataset field.

```bash
Usage:
  dataos-ctl dataset update-field [flags]

Flags:
  -a, --address string    The address of Dataset
  -t, --datatype string   Datatype of field
  -h, --help              help for update-field
  -n, --name string       Name of field
  -p, --precision int8    --precision 10 (only for decimal type)
  -s, --scale int8        --scale 1 (only for decimal type) (default 1)
```

## `update-partition`

Update partition.

```bash
Usage:
  dataos-ctl dataset update-partition [flags]

Flags:
  -a, --address string       The address of Dataset
  -n, --count int            --count 2
  -h, --help                 help for update-partition
  -p, --partitions strings   --partitions <partition_type>:<column_name>:<partition_name>
```
