# Query-details Command Group
You run the following `query-details` sub commands by appending them to *dataos-ctl query-details*.

## `connect`
Connect to the DataOS® Query Gateway

```shell

Usage:
  dataos-ctl query-gateway connect [flags]

Flags:
  -c, --catalog string     The catalog to connect to through the query gateway.
      --cluster string     The cluster to connect to through the query gateway.
  -d, --dataplane string   The dataplane to connect to the query gateway.
  -h, --help               help for connect
  -p, --port string        The port to connect to the query gateway. (default "7432")

Global Flags:
      --tls-allow-insecure   Allow insecure TLS connections
```