# Role Command Group
You run the following `role` sub commands by appending them to *dataos-ctl role*.

## `changes`
View a DataOS® Role changes

```shell

Usage:
  dataos-ctl role changes [command]

Available Commands:
  get         Get the changes for a role

Flags:
  -h, --help   help for changes

Global Flags:
      --tls-allow-insecure   Allow insecure TLS connections

Use "dataos-ctl role changes [command] --help" for more information about a command.
```

### **'get'**


```shell
Get the changes for a role

Usage:
  dataos-ctl role changes get [flags]

Flags:
  -h, --help        help for get
  -i, --id string   Id of the role

Global Flags:
      --tls-allow-insecure   Allow insecure TLS connections

```

## `get`
Get DataOS® Roles

```shell

Usage:
  dataos-ctl role get [flags]

Flags:
  -h, --help   help for get

Global Flags:
      --tls-allow-insecure   Allow insecure TLS connections
```