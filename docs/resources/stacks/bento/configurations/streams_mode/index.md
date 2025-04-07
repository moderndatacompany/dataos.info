# Streams Mode

A Bento stream consists of four components; an input, an optional buffer, processor pipelines, and an output. Under normal use, a Bento instance is a single stream, and these components are configured within the service config file.

Alternatively, Bento can be run in `streams` mode, where a single running Bento instance is able to run multiple entirely isolated streams. Adding streams in this mode can be done in two ways:

1. [Static configuration files](/resources/stacks/bento/configurations/streams_mode/streams_via_config_files) allows to maintain a directory of static stream configuration files that will be traversed by Bento.
2. An [HTTP REST API](/resources/stacks/bento/configurations/streams_mode/streams_via_rest_api) allows to dynamically create, read the status of, update, and delete streams at runtime.

These two methods can be used in combination, i.e. it's possible to update and delete streams that were created with static files.

When running Bento in streams mode, it is still necessary to provide a general service-wide configuration with the `-c`/`--config` flag that specifies observability configuration such as the `metrics`, `logger`, and `tracing` sections, as well the `http` section for configuring how the HTTP server should behave.

Resources can be imported either through the general configuration or by using the `-r` / `--resources` flag, consistent with the method used when running Bento in standard mode.

```bash
bento -r "./prod/*.yaml" -c ./config.yaml streams
```

## HTTP Endpoints

A Bento config can contain components such as an `http_server` input that register endpoints to the service-wide HTTP server. When these components are created from within a named stream in streams mode, the endpoint will be prefixed with the streams identifier by default. For example, a stream with the identifier `foo` and the config:

```yaml
input:
  http_server:
    path: /meow
pipeline:
  processors:
    - mapping: 'root = "meow " + content()'
output:
  sync_response: {}
```

Will register an endpoint `/meow`, which will be prefixed with the name `foo` to become `/foo/meow`. This behavior is intended to make a clearer distinction between endpoints registered by different streams and prevent collisions of those endpoints. However, this behavior can be disabled by setting the flag `--prefix-stream-endpoints` to `false` (`bento streams --prefix-stream-endpoints=false ./streams/*.yaml`).

## Resources

When running Bento in streams mode, [resource components](/resources/stacks/bento/configurations/resources) are shared across all streams. The streams mode HTTP API also provides an endpoint for modifying and adding resource configurations dynamically.

## Metrics

Metrics from all streams are aggregated and exposed via the method specified in [the config](/resources/stacks/bento/components/metrics) of the Bento instance running in `streams` mode, with their metrics enriched with the tag `stream` containing the stream name.

For example, a Bento instance running in streams mode running a stream named `foo` would have metrics from `foo` registered with the label `stream` with the value of `foo`.

Issues may arise when streams are short-lived and uniquely named, as the number of registered metrics may increase without bound. To mitigate this, the `mapping` field can be used to filter metric names.

```yaml
# Only register metrics for the stream `foo`. Others will be ignored.
metrics:
  mapping: if meta("stream") != "foo" { deleted() }
  prometheus: {}
```

[Streams Via Config Files](/resources/stacks/bento/configurations/streams_mode/streams_via_config_files)

[Streams Via REST API](/resources/stacks/bento/configurations/streams_mode/streams_via_rest_api)

[Streams API](/resources/stacks/bento/configurations/streams_mode/streams_api)