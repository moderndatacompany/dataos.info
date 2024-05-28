# Workspace Command Group
You run the following `workspace` sub commands by appending them to *dataos-ctl workspace*.

## `create`

Create workspace.

```shell
Usage:
dataos-ctl workspace create [flags]

Flags:
-d, --description string   workspace description
-h, --help                 help for create
    --labels strings       The workspace labels
-l, --layer string         workspace layer (default "user")
-n, --name string          workspace name
    --tags strings         The workspace tags
-v, --version string       workspace version (default "v1beta1")
```

## `delete`

Delete workspaces.

```shell
Usage:
dataos-ctl workspace delete [flags]

Flags:
-h, --help          help for delete
-n, --name string   workspace name
```

## `get`

Get workspaces.

```shell
Usage:
dataos-ctl workspace get [flags]

Flags:
-h, --help           help for get
-l, --layer string   workspace layer (default "user")
```
