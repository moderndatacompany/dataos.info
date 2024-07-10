# Develop Command Group
You run the following `develop` commands by appending them to *dataos-ctl develop*. 

## `generate`
Generate example manifests


```shell

Usage:
  dataos-ctl develop generate [flags]

Flags:
  -h, --help             help for generate
  -n, --name string      The resource name.
  -t, --type string      The resource type. Workspace resources: workflow,service,worker,secret,database,cluster,volume,resource,monitor,pager,lakehouse. Instance resources: policy,depot,compute,dataplane,stack,operator,bundle,instance-secret,grant.
  -v, --version string   The resource version.
```

## `get`
Get running development containers

```shell

Usage:
  dataos-ctl develop get [flags]

Flags:
  -h, --help   help for get
```

## `schema`
JSON Schema visibility for DataOS® resource types and apis

```shell

Usage:
  dataos-ctl develop schema [command]

Available Commands:
  generate    JSON Schema generation for DataOS® resources
  get         JSON Schema retrieval for DataOS® resources

Flags:
  -h, --help   help for schema
```

### **`generate`**
JSON Schema generation for DataOS® resources

```shell

Usage:
  dataos-ctl develop schema generate [flags]

Flags:
  -h, --help             help for generate
  -t, --type string      The resource type to export: bundle|cluster|compute|database|dataplane|depot|grant|instance-secret|lakehouse|monitor|operator|pager|policy|resource|secret|service|stack|volume|worker|workflow
  -v, --version string   The resource version to export: v1|v1beta|v1alpha|v2alpha
```
### **`get`**
JSON Schema retrieval for DataOS® resources

```shell

Usage:
  dataos-ctl develop schema get [command]

Available Commands:
  api         JSON Schema for DataOS® apis
  resource    JSON Schema for DataOS® resources

Flags:
  -h, --help   help for get
```

#### **`api`**
JSON Schema for DataOS® apis

```shell

Usage:
  dataos-ctl develop schema get api [flags]

Flags:
  -h, --help             help for api
  -t, --type string      The api type to export: instance-scoped|workspace-scoped
  -v, --version string   The api version to export: v1|v1beta|v1alpha|v2alpha
```

#### **`resource`**
JSON Schema retrieval for DataOS® resources

```shell


Usage:
  dataos-ctl develop schema get [command]

Available Commands:
  api         JSON Schema for DataOS® apis
  resource    JSON Schema for DataOS® resources

Flags:
  -h, --help   help for get
```

## `stack`
Stack specific commands
```shell

Usage:
  dataos-ctl develop stack [command]

Available Commands:
  image-pull-secret Get stack image pull secret
  versions          Get stack versions

Flags:
  -h, --help   help for stack

```
### **`image-pull-secret`**
Get stack image pull secret

```shell

Usage:
  dataos-ctl develop stack image-pull-secret [flags]

Flags:
  -h, --help           help for image-pull-secret
  -s, --stack string   Stack Type
```

### **`versions`**
Get stack versions
```shell

Usage:
  dataos-ctl develop stack versions [flags]

Aliases:
  versions, version

Flags:
  -h, --help   help for versions
```

## `start`

```shell

```

## `stop`

```shell

```

## `types`

```shell

```

