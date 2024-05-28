# Runtime Command Group
You run the following `runtime` sub commands by appending them to *dataos-ctl runtime*.

## `get`
Get runnable resources in the DataOS®

```shell

Usage:
  dataos-ctl resource runtime get [flags]

Flags:
  -d, --details               Print lots of details
  -h, --help                  help for get
      --id string             Resource ID, like: TYPE:VERSION:NAME:WORKSPACE(optional), depot:v1:icebase or service:v1:ping:sandbox
  -i, --identifier string     Identifier of resource, like: NAME:VERSION:TYPE:WORKSPACE
  -f, --manifestFile string   Manifest file location
  -n, --name string           Name to query
      --node string           Node name to get details
  -r, --refresh               Auto refresh the results
      --refreshRate int       Refresh rate in seconds (default 5)
  -t, --type string           The resource type to get. Workspace resources: workflow, service, worker, cluster. Instance resources: depot.
  -v, --version string        Version to query (default "v1")
  -w, --workspace string      Workspace to query
  -y, --yaml                  Print the full node as yaml

Global Flags:
      --tls-allow-insecure   Allow insecure TLS connections
```
## `pause`

Pause runnable resources in the DataOS®
```shell

Usage:
  dataos-ctl resource runtime pause [flags]

Flags:
  -h, --help                  help for pause
      --id string             Resource ID, like: TYPE:VERSION:NAME:WORKSPACE(optional), depot:v1:icebase or service:v1:ping:sandbox
  -i, --identifier string     Identifier of resource, like: NAME:VERSION:TYPE
  -f, --manifestFile string   Manifest File location
  -n, --name string           Name to pause
      --tls-allow-insecure    Allow insecure TLS connections
  -t, --type string           The resource type to pause. Workspace resources: workflow.
  -v, --version string        Version to pause (default "v1")
  -w, --workspace string      Workspace to target
```

## `re-run`
Re-run runnable resources in the DataOS®

```shell

Usage:
  dataos-ctl  runtime re-run [flags]

Flags:
  -h, --help                  help for re-run
      --id string             Resource ID, like: TYPE:VERSION:NAME:WORKSPACE(optional), depot:v1:icebase or service:v1:ping:sandbox
  -i, --identifier string     Identifier of resource, like: NAME:VERSION:TYPE
  -f, --manifestFile string   Manifest File location
  -n, --name string           Name to re-run
      --tls-allow-insecure    Allow insecure TLS connections
  -t, --type string           The resource type to re-run. Workspace resources: workflow.
  -v, --version string        Version to re-run (default "v1")
  -w, --workspace string      Workspace to target
```

## `resume`
Resume runnable resources in the DataOS®

```shell

Usage:
  dataos-ctl runtime resume [flags]

Flags:
  -h, --help                  help for resume
      --id string             Resource ID, like: TYPE:VERSION:NAME:WORKSPACE(optional), depot:v1:icebase or service:v1:ping:sandbox
  -i, --identifier string     Identifier of resource, like: NAME:VERSION:TYPE
  -f, --manifestFile string   Manifest File location
  -n, --name string           Name to resume
      --tls-allow-insecure    Allow insecure TLS connections
  -t, --type string           The resource type to resume. Workspace resources: workflow.
  -v, --version string        Version to resume (default "v1")
  -w, --workspace string      Workspace to target
```

## `stop`

Stop runnable resources in the DataOS®

```shell

Usage:
  dataos-ctl  runtime stop [flags]

Flags:
  -h, --help                  help for stop
      --id string             Resource ID, like: TYPE:VERSION:NAME:WORKSPACE(optional), depot:v1:icebase or service:v1:ping:sandbox
  -i, --identifier string     Identifier of resource, like: NAME:VERSION:TYPE
  -f, --manifestFile string   Manifest File location
  -n, --name string           Name to stop
      --tls-allow-insecure    Allow insecure TLS connections
  -t, --type string           The resource type to stop. Workspace resources: workflow.
  -v, --version string        Version to stop (default "v1")
  -w, --workspace string      Workspace to target
```
