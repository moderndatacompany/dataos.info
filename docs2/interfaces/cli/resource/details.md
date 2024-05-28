# Role Command Group
You run the following `role` sub commands by appending them to *dataos-ctl role*.

## `apply`
Apply resources in the DataOS®

```shell

Usage:
  dataos-ctl resource apply [flags]

Flags:
  -d, --de-ref                  De-reference the files, do not apply
      --disable-interpolation   Disable interpolation, do not interpolate $ENV|${ENV}
      --disable-resolve-stack   Disable resolve stack
  -h, --help                    help for apply
  -l, --lint                    Lint the files, do not apply
  -f, --manifestFile string     Manifest file location
  -r, --re-run                  Re-run resource after apply
  -R, --recursive               Get manifest files recursively from the provided directory
      --tls-allow-insecure      Allow insecure TLS connections
  -w, --workspace string        Workspace to target resource (default "public")
```

## `create`
Create resources in the DataOS®

```shell

Usage:
  dataos-ctl resource create [flags]

Flags:
      --disable-interpolation   Disable interpolation, do not interpolate $ENV|${ENV}
      --disable-resolve-stack   Disable resolve stack
  -h, --help                    help for create
  -f, --manifestFile string     Manifest file location
  -R, --recursive               Get manifest files recursively from the provided directory
      --tls-allow-insecure      Allow insecure TLS connections
  -w, --workspace string        Workspace to target resource (default "public")
```

## `delete`
Delete resources in the DataOS®

```shell

Usage:
  dataos-ctl resource delete [flags]

Flags:
      --force                 Force delete even though dependencies are not allowing it
  -h, --help                  help for delete
      --id string             Resource ID, like: TYPE:VERSION:NAME:WORKSPACE(optional), depot:v1:icebase or service:v1:ping:sandbox
  -i, --identifier string     Identifier of resource, like: NAME:VERSION:TYPE
  -f, --manifestFile string   Manifest file location
  -n, --name string           Name of resource
      --tls-allow-insecure    Allow Insecure TLS connections
  -t, --type string           The resource type to delete. Workspace resources: workflow,service,worker,secret,database,cluster,volume,resource,monitor,pager,lakehouse. Instance resources: policy,depot,compute,dataplane,stack,operator,bundle,instance-secret,grant.
  -v, --version string        Version of resource (default "v1")
  -w, --workspace string      Workspace to target resource (default "public")
```

## `get`
Get resources in the DataOS®


```shell

Usage:
  dataos-ctl resource get [flags]
  dataos-ctl resource get [command]

Available Commands:
  runtime     Get DataOS® Runtime Details

Flags:
  -a, --all                   Get resources for all owners
  -d, --details               Set to true to include details in the result
  -h, --help                  help for get
      --id string             Resource ID, like: TYPE:VERSION:NAME:WORKSPACE(optional), depot:v1:icebase or service:v1:ping:sandbox
  -i, --identifier string     Identifier of resource, like: NAME:VERSION:TYPE
  -f, --manifestFile string   Manifest File location
  -n, --name string           Name to query
  -o, --owner string          Get resources for a specific owner id, defaults to your id.
  -r, --refresh               Auto refresh the results
      --refreshRate int       Refresh rate in seconds (default 5)
      --tags                  Set to true to include tags in the result
      --tls-allow-insecure    Allow insecure TLS connections
  -t, --type string           The resource type to get. Workspace resources: workflow,service,worker,secret,database,cluster,volume,resource,monitor,pager,lakehouse. Instance resources: policy,depot,compute,dataplane,stack,operator,bundle,instance-secret,grant.
      --unSanitize            Get the resources un-sanitized, this includes sensitive fields.
  -v, --version string        Version to query (default "v1")
  -w, --workspace string      Workspace to query

Use "dataos-ctl resource get [command] --help" for more information about a command.

```

## `log`
Get the logs for a resource in the DataOS®

```shell

Usage:
  dataos-ctl resource log [flags]

Aliases:
  log, logs

Flags:
  -c, --container string    Container name to filter logs
  -f, --follow              Follow the logs
  -h, --help                help for log
  -i, --identifier string   Identifier of resource, like: NAME:VERSION:TYPE
  -r, --includeRunnable     Include runnable system pods and logs
  -n, --name string         Name to query
      --node string         Node name to filter logs
  -l, --tailLines int       Number of tail lines to retrieve, use -1 to get all logs (default 300)
  -t, --type string         The resource type to get, possible values: service, workflow, cluster, depot
  -v, --version string      Version to query (default "v1")
  -w, --workspace string    Workspace to query (default "public")

Global Flags:
      --tls-allow-insecure   Allow insecure TLS connections
```

## `run`
Create and Run a Resource in the DataOS®

```shell

Usage:
  dataos-ctl resource run [flags]

Flags:
  -c, --configFile string                     Config file location
      --disable-interpolation                 Disable interpolation, do not interpolate $ENV|${ENV}
      --do-not-delete-on-failure              Do not delete the resource on completion with failure (default true)
      --do-not-delete-on-success              Do not delete the resource on completion with success
      --failure-strings strings               Runtime strings that indicates this resource is complete with failure (default [failed])
  -h, --help                                  help for run
  -f, --manifestFile string                   Manifest file location
      --run-start-timeout-duration duration   The runtime start timeout duration (default 2m0s)
      --run-string string                     Runtime string that indicates this resource is running (default "running")
      --run-timeout-duration duration         The runtime timeout duration (default 5m0s)
      --stream-logs                           Stream logs from primary runtime node to stdout
      --success-strings strings               Runtime strings that indicates this resource is complete with success (default [succeeded])
  -w, --workspace string                      Workspace to target resource (default "public")

Global Flags:
      --tls-allow-insecure   Allow insecure TLS connections

```

## `runtime`
DataOS® runtime management commands

```shell

Usage:
  dataos-ctl resource runtime [command]

Available Commands:
  get         Get DataOS® Runnable Resources
  pause       Pause DataOS® Runnable Resources
  re-run      Re-run DataOS® Runnable Resources
  resume      Resume DataOS® Runnable Resources
  stop        Stop DataOS® Runnable Resources

Flags:
  -h, --help   help for runtime

Global Flags:
      --tls-allow-insecure   Allow insecure TLS connections

Use "dataos-ctl resource runtime [command] --help" for more information about a command.
```
### **`get`**
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
### **`pause`**

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

### **`re-run`**
Re-run runnable resources in the DataOS®

```shell

Usage:
  dataos-ctl resource runtime re-run [flags]

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

### **`resume`**
Resume runnable resources in the DataOS®

```shell

Usage:
  dataos-ctl resource runtime resume [flags]

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

### **`stop`**

Stop runnable resources in the DataOS®

```shell

Usage:
  dataos-ctl resource runtime stop [flags]

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

## `tcp-stream`

Open a tcp stream for resources in the DataOS®
```shell


Usage:
  dataos-ctl resource tcp-stream [flags]

Flags:
      --dataplane string       Dataplane name; default=hub (default "hub")
  -h, --help                   help for tcp-stream
  -i, --identifier string      Identifier of resource, like: NAME:VERSION:TYPE
      --listenPort int         Port the local client will listen on to tcp stream (default 14040)
  -n, --name string            Name of resource
      --node string            Node name to open tcp stream in resource runtime
      --servicePort int        Service port to be forwarded (default 4040)
      --serviceSuffix string   Suffix to override default service suffix: ui-svc (default "ui-svc")
      --tls-allow-insecure     Allow Insecure TLS connections
  -t, --type string            The resource type to tcp-stream. Workspace resources: workflow,service,worker,secret,database,cluster,volume,resource,monitor,pager,lakehouse. Instance resources: policy,depot,compute,dataplane,stack,operator,bundle,instance-secret,grant.
  -w, --workspace string       Workspace to target resource (default "public")
```

## `update`

Update resources in the DataOS®
```shell

Usage:
  dataos-ctl resource update [flags]

Flags:
      --disable-interpolation   Disable interpolation, do not interpolate $ENV|${ENV}
      --disable-resolve-stack   Disable resolve stack
  -h, --help                    help for update
  -f, --manifestFile string     Manifest file location
  -R, --recursive               Get manifest files recursively from the provided directory
      --tls-allow-insecure      Allow insecure TLS connections
  -w, --workspace string        Workspace to target resource (default "public")
```