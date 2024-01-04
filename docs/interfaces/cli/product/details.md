# Product Command Group
You run the following `product` sub commands by appending them to *dataos-ctl product*.

## `apply`
Apply products in the DataOS®

```shell

Usage:
  dataos-ctl product apply [flags]

Flags:
  -d, --de-ref                  De-reference the files, do not apply
      --disable-interpolation   Disable interpolation, do not interpolate $ENV|${ENV}
  -h, --help                    help for apply
  -l, --lint                    Lint the files, do not apply
  -f, --manifestFile string     Manifest file location
  -R, --recursive               Get manifest files recursively from the provided directory
      --tls-allow-insecure      Allow insecure TLS connections

```

## `delete`
Delete products in the DataOS®

```shell

Usage:
  dataos-ctl product delete [flags]

Flags:
  -h, --help                  help for delete
  -i, --identifier string     Identifier of resource, like: TYPE:VERSION:NAME
  -f, --manifestFile string   Manifest file location
  -n, --name string           Name of product
      --tls-allow-insecure    Allow insecure TLS connections
  -t, --type string           Type of product
  -v, --version string        Version of product
```

## `get`
Get products in the DataOS®

```shell

Usage:
  dataos-ctl product get [flags]

Flags:
  -a, --all                   Get products for all owners
  -d, --details               Set to true to include details in the result
  -h, --help                  help for get
  -f, --manifestFile string   Manifest File location
  -n, --name string           Product name to query
  -o, --owner string          Get products for a specific owner id, defaults to your id.
  -i, --productId string      Product ID, like: TYPE:VERSION:NAME
  -r, --refresh               Auto refresh the results
      --refreshRate int       Refresh rate in seconds (default 5)
      --tags                  Set to true to include tags in the result
      --tls-allow-insecure    Allow insecure TLS connections
  -t, --type string           Product type to query
  -v, --version string        Product version to query
```