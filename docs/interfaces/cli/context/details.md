# Context Command Group
You run the following `context` commands by appending them to *dataos-ctl context*. 

## `list`

Get the list of environments you have initialized using the *dataos-ctl init* command. The active context will be shown with a star and you can see its URL in the output.

```bash
Usage:
dataos-ctl context select [flags]

Flags:
-h, --help          help for select
-n, --name string   name of context to select
```

Here is the expected output:

```bash
➜  ~ dataos-ctl context list
INFO[0000] * meerkat                                    
INFO[0000]   squirrel                                   
INFO[0000]   wholly-merry-orca                          
INFO[0000] 🔗...https://cleanly-mutual-meerkat.dataos.io
```

## `delete`

Delete the context which is pointing to your DataOS environment.

```bash
Usage:
dataos-ctl context delete [flags]

Flags:
-h, --help          help for delete
-n, --name string   name of context to select
```
## `product`
Manage products and releases for the current DataOS® context

```shell

Usage:
  dataos-ctl context product [command]

Available Commands:
  create-inputs  Create inputs assets
  create-install Create install assets
  interpolate    Interpolates a file
  list           List entitled products and releases for the current DataOS® context

Flags:
  -h, --help   help for product
```

### **`create-inputs`**
Create inputs assets for the specified product and release and model

```shell

Usage:
  dataos-ctl context product create-inputs [flags]

Flags:
  -h, --help                help for create-inputs
  -l, --licenseKey string   license key
  -m, --model string        model name (default "default")
  -o, --outputDir string    output directory to write the install assets
  -p, --product string      product id
  -r, --release string      release name
```

### **`create-install`**
Create install assets for the specified product and release and model

```shell

Usage:
  dataos-ctl context product create-install [flags]

Flags:
  -h, --help                help for create-install
  -l, --licenseKey string   license key
  -m, --model string        model name (default "default")
  -o, --outputDir string    output directory to write the install assets
  -p, --product string      product id
  -r, --release string      release name
```
### **`interpolate`**

```shell
Interpolates a file

Usage:
  dataos-ctl context product interpolate [flags]

Flags:
  -f, --file string         Input File Location
  -h, --help                help for interpolate
  -o, --outputFile string   Interpolated Output File Location
```

### **`list`**

```shell
List entitled products and releases for the current DataOS® context

Usage:
  dataos-ctl context product list [flags]

Flags:
  -h, --help                help for list
  -l, --licenseKey string   license key

```
## `select`

Select a new context to point to, from the available environments.

```bash
Usage:
    dataos-ctl context select [flags]

Flags:
-h, --help          help for select
-n, --name string   name of context to select
```
