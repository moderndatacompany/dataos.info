# Collation Command Group
You run the following `collation` commands by appending them to *dataos-ctl collation*.

## `content`
Interact with content items in the DataOS® Collation Service

```bash
Usage:
  dataos-ctl collation content [command]

Available Commands:
  get         Get the content item in the DataOS® Collation Service

Flags:
  -h, --help   help for content

Global Flags:
      --tls-allow-insecure   Allow insecure TLS connections

Use "dataos-ctl collation content [command] --help" for more information about a command.
```
### **`get`**
Get the content item in the DataOS® Collation Service

```bash
Usage:
  dataos-ctl collation content get [flags]

Flags:
  -h, --help        help for get
      --id string   Id of the content item

Global Flags:
      --tls-allow-insecure   Allow insecure TLS connections

```

## `metadata`
Interact with metadata in the DataOS® Collation Service

```bash
Usage:
  dataos-ctl collation metadata [command]

Available Commands:
  message     Interact with metadata messages in the DataOS® Collation Service
  node        Interact with metadata nodes in the DataOS® Collation Service
  pod         Interact with metadata pods in the DataOS® Collation Service
  resource    Interact with metadata resources in the DataOS® Collation Service
  workspace   Interact with metadata workspaces in the DataOS® Collation Service

Flags:
  -h, --help   help for metadata

Global Flags:
      --tls-allow-insecure   Allow insecure TLS connections

Use "dataos-ctl collation metadata [command] --help" for more information about a command.
```

### **`message`**
Interact with metadata messages in the DataOS® Collation Service

```bash
Usage:
  dataos-ctl collation metadata message [command]

Available Commands:
  read        Read the most recent metadata messages in the DataOS® Collation Service

Flags:
  -h, --help   help for message

Global Flags:
      --tls-allow-insecure   Allow insecure TLS connections

Use "dataos-ctl collation metadata message [command] --help" for more information about a command.
```
#### **`read`**
Read the most recent metadata messages in the DataOS® Collation Service

```bash

Usage:
  dataos-ctl collation metadata message read [flags]

Flags:
  -d, --duration string    FastBase duration to seek in the past
  -h, --help               help for read
  -m, --messageId string   FastBase message id to start reading from
```
### **`node`**
Interact with metadata nodes in the DataOS® Collation Service

```bash

Usage:
  dataos-ctl collation metadata node [command]

Available Commands:
  list        List the metadata nodes in the DataOS® Collation Service

Flags:
  -h, --help   help for node


```

#### **`list`**
List the metadata nodes in the DataOS® Collation Service

```bash

Usage:
  dataos-ctl collation metadata node list [flags]

Flags:
      --filter string   Filter fields and values, only status=STATUS is supported for filtering
  -h, --help            help for list
      --page string     Page number
      --size string     Size of a page
      --sort string     Sort field, add a '-' at the beginning to sort descending
```
### **`pod`**
Interact with metadata pods in the DataOS® Collation Service

```bash

Usage:
  dataos-ctl collation metadata pod [command]

Available Commands:
  list        List the metadata pods in the DataOS® Collation Service

Flags:
  -h, --help   help for pod

```

##### **List**
List the metadata pods in the DataOS® Collation Service

```bash

Usage:
  dataos-ctl collation metadata pod list [flags]

Flags:
      --filter string   Filter fields and values, only status=STATUS is supported for filtering
  -h, --help            help for list
      --page string     Page number
      --size string     Size of a page
      --sort string     Sort field, add a '-' at the beginning to sort descending
```

### **`resource`**

Interact with metadata resources in the DataOS® Collation Service

```bash

Usage:
  dataos-ctl collation metadata resource [command]

Available Commands:
  list        List the metadata resources in the DataOS® Collation Service

Flags:
  -h, --help   help for resource
```

#### **`list`**
List the metadata resources in the DataOS® Collation Service

```bash

Usage:
  dataos-ctl collation metadata resource list [flags]

Flags:
      --filter string   Filter fields and values, only type=TYPE&version=VERSION&workspace=WORKSPACE | status=STATUS is supported for filtering
  -h, --help            help for list
      --page string     Page number
      --size string     Size of a page
      --sort string     Sort field, add a '-' at the beginning to sort descending


```

### **`workspace`**
Interact with metadata workspaces in the DataOS® Collation Service


```bash

Usage:
  dataos-ctl collation metadata workspace [command]

Available Commands:
  list        List the metadata workspaces in the DataOS® Collation Service

Flags:
  -h, --help   help for workspace

```

#### **`list`**
List the metadata workspaces in the DataOS® Collation Service

```bash

Usage:
  dataos-ctl collation metadata workspace list [flags]

Flags:
      --filter string   Filter fields and values, only status=STATUS is supported for filtering
  -h, --help            help for list
      --page string     Page number
      --size string     Size of a page
      --sort string     Sort field, add a '-' at the beginning to sort descending


```
## resource
Interact with resources in the DataOS® Collation Service

```shell

Usage:
  dataos-ctl collation resource [command]

Available Commands:
  get         Get the resource in the DataOS® Collation Service

Flags:
  -h, --help   help for resource

```
### **get**
Get the resource in the DataOS® Collation Service
```shell

Usage:
  dataos-ctl collation resource get [flags]

Flags:
  -h, --help        help for get
      --id string   Id of the collated resource
```
