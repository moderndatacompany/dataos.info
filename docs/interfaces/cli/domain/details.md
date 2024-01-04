# Domain Command Group
You run the following `domain` commands by appending them to *dataos-ctl domain*.

## `apply`
Apply domains in the DataOS®

```shell

Usage:
  dataos-ctl domain apply [flags]

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
Delete domains in the DataOS®


```shell

Usage:
  dataos-ctl domain delete [flags]

Flags:
  -h, --help                  help for delete
  -i, --identifier string     Identifier of resource, like: TYPE:VERSION:NAME
  -f, --manifestFile string   Manifest file location
  -n, --name string           Name of domain
      --tls-allow-insecure    Allow insecure TLS connections
  -t, --type string           Type of domain
  -v, --version string        Version of domain
```

## `get`
Get domains in the DataOS®

```shell

Usage:
  dataos-ctl domain get [flags]

Flags:
  -a, --all                   Get domains for all owners
  -d, --details               Set to true to include details in the result
  -i, --domainId string       Domain ID, like: TYPE:VERSION:NAME
  -h, --help                  help for get
  -f, --manifestFile string   Manifest File location
  -n, --name string           Domain name to query
  -o, --owner string          Get domains for a specific owner id, defaults to your id.
  -r, --refresh               Auto refresh the results
      --refreshRate int       Refresh rate in seconds (default 5)
      --tags                  Set to true to include tags in the result
      --tls-allow-insecure    Allow insecure TLS connections
  -t, --type string           Domain type to query
  -v, --version string        Domain version to query

```