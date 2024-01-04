# Fastbase Command Group
You run the following `fastbase` sub commands by appending them to *dataos-ctl fastbase*.

## `namespace`
Interact with namespaces in the DataOS® FastBase

```shell

Usage:
  dataos-ctl fastbase namespace [command]

Aliases:
  namespace, namespaces

Available Commands:
  list        List namespaces in the DataOS® FastBase

Flags:
  -h, --help   help for namespace
```
### **`list`**
List namespaces in the DataOS® FastBase

```shell

Usage:
  dataos-ctl fastbase namespace list [flags]

Flags:
  -h, --help            help for list
  -t, --tenant string   FastBase tenant
```
## `tenant`
Interact with tenants in the DataOS® FastBase

```shell

Usage:
  dataos-ctl fastbase tenant [command]

Aliases:
  tenant, tenants

Available Commands:
  list        List tenants in the DataOS® FastBase

Flags:
  -h, --help   help for tenant
```
### **`list`**
List tenants in the DataOS® FastBase

```shell

Usage:
  dataos-ctl fastbase tenant list [flags]

Flags:
  -h, --help   help for list
```

## `topic`
Interact with topics in the DataOS® FastBase

```shell

Usage:
  dataos-ctl fastbase topic [command]

Aliases:
  topic, topics

Available Commands:
  consume     Consume Messages from a Topic
  list        List topics in the DataOS® FastBase
  permissions List Permissions of a Topic
  read        Read Message from a Topic

Flags:
  -h, --help   help for topic
```

### **`consume`**
Consume Messages from a Topic in the DataOS® FastBase
```shell

Usage:
  dataos-ctl fastbase topic consume [flags]

Flags:
  -h, --help                  help for consume
  -l, --logMessage            Log message (default true)
  -p, --logPayload            Log payload with message
  -s, --startAtFirstMessage   Start at the first message in the topic
  -t, --topic string          FastBase topic to consume messages from
```

### **`list`**
List topics in the DataOS® FastBase
```shell

Usage:
  dataos-ctl fastbase topic list [flags]

Flags:
  -h, --help               help for list
  -n, --namespace string   FastBase namespace
```

### **`permissions`**
List Permissions of a Topic in the DataOS® FastBase
```shell

Usage:
  dataos-ctl fastbase topic permissions [flags]

Flags:
  -h, --help           help for permissions
  -t, --topic string   FastBase topic to read message from
```

### **`read`**
Read Message from a Topic in the DataOS® FastBase

```shell

Usage:
  dataos-ctl fastbase topic read [flags]

Flags:
  -d, --duration string    FastBase duration to seek in the past
  -h, --help               help for read
  -l, --logMessage         Log message (default true)
  -p, --logPayload         Log payload with message
  -m, --messageId string   FastBase message id to start reading from
  -t, --topic string       FastBase topic to read message from
```