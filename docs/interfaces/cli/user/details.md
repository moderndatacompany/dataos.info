# User Command Group
You run the following `user` sub commands by appending them to *dataos-ctl user*.

## `apikey`

Manage a DataOS® User apikey

```shell

Usage:
  dataos-ctl user apikey [command]

Available Commands:
  create      Create an apikey for a user
  delete      Delete the apikey for a user
  get         Get the apikey for a user

Flags:
  -h, --help   help for apikey

Global Flags:
      --tls-allow-insecure   Allow insecure TLS connections

Use "dataos-ctl user apikey [command] --help" for more information about a command.
```

### **`create`**
Create an apikey for a user

```shell

Usage:
  dataos-ctl user apikey create [flags]

Flags:
  -d, --duration string   Duration for the apikey to live (default "24h")
  -h, --help              help for create
  -i, --id string         Id of the user
  -n, --name string       Name of the apikey

Global Flags:
      --tls-allow-insecure   Allow insecure TLS connections
```

### **`delete`**
Delete the apikey for a user

```shell

Usage:
  dataos-ctl user apikey delete [flags]

Flags:
  -h, --help          help for delete
  -n, --name string   apikey name

Global Flags:
      --tls-allow-insecure   Allow insecure TLS connections
```

### **`get`**
Get the apikey for a user

```shell

Usage:
  dataos-ctl user apikey get [flags]

Flags:
  -h, --help          help for get
  -i, --id string     Id of the user
  -n, --name string   Name of the apikey

Global Flags:
      --tls-allow-insecure   Allow insecure TLS connections

```

## `changes`
View a DataOS® User changes

```shell

Usage:
  dataos-ctl user changes [command]

Available Commands:
  get         Get the changes for a user

Flags:
  -h, --help   help for changes

Global Flags:
      --tls-allow-insecure   Allow insecure TLS connections

Use "dataos-ctl user changes [command] --help" for more information about a command.

```

### **`get`**
Get the changes for a user

```shell

Usage:
  dataos-ctl user changes get [flags]

Flags:
  -h, --help        help for get
  -i, --id string   Id of the user

Global Flags:
      --tls-allow-insecure   Allow insecure TLS connections
```

## `create`

Create a DataOS® User
```shell

Usage:
  dataos-ctl user create [flags]

Flags:
      --apikeyName string   A specific apikey name to associate with the new user as a token
  -d, --duration string     The duration that the apikey should last before expiring
  -e, --email string        The email
  -h, --help                help for create
  -n, --name string         The user name
      --tags strings        The list of tags to associate with the user
  -t, --type string         The user type: person|application
  -u, --user_id string      The userId

Global Flags:
      --tls-allow-insecure   Allow insecure TLS connections
```

## `delete`
Delete a DataOS® User

```shell

Usage:
  dataos-ctl user delete [flags]

Flags:
  -h, --help        help for delete
  -i, --id string   Id of the user

Global Flags:
      --tls-allow-insecure   Allow insecure TLS connections
```

## `get`
Get DataOS® Users

```shell

Usage:
  dataos-ctl user get [flags]

Flags:
  -a, --all         Get all users
  -h, --help        help for get
  -i, --id string   Id of the user

Global Flags:
      --tls-allow-insecure   Allow insecure TLS connections
```

## `tag`
Manage DataOS® User's tags

```shell

Usage:
  dataos-ctl user tag [command]

Available Commands:
  add         Add tags to a user
  delete      Delete tags from a user

Flags:
  -h, --help   help for tag

Global Flags:
      --tls-allow-insecure   Allow insecure TLS connections

Use "dataos-ctl user tag [command] --help" for more information about a command.
```

### **`add`**
Add tags to a user

```shell

Usage:
  dataos-ctl user tag add [flags]

Flags:
  -h, --help           help for add
  -i, --id string      Id of the user
  -t, --tags strings   The tags to add

Global Flags:
      --tls-allow-insecure   Allow insecure TLS connections
```

### **`delete`**
Delete tags from a user
```shell

Usage:
  dataos-ctl user tag delete [flags]

Flags:
  -h, --help           help for delete
  -i, --id string      Id of the user
  -t, --tags strings   The tags to delete

Global Flags:
      --tls-allow-insecure   Allow insecure TLS connections
```

