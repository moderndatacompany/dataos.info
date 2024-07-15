# Tracers

A tracer type represents a destination for Benthos to send tracing events to, such as [Jaeger](https://www.jaegertracing.io/).

When a tracer is configured, all messages will be allocated a root span during ingestion that represents their journey through a Benthos pipeline. Many Benthos processors create spans, and so tracing is a great way to analyze the pathways of individual messages as they progress through a Benthos instance.

Some inputs, such as `http_server` and `http_client`, are capable of extracting a root span from the source of the message (HTTP headers). This is a work in progress and should eventually expand so that all inputs have a way of doing so.

Other inputs, such as `kafka` can be configured to extract a root span by using the `extract_tracing_map` field.

A tracer config section looks like this:

```yaml
tracer:
  jaeger:
    agent_address: localhost:6831
    sampler_type: const
    sampler_param: 1
```

WARNING: Although the configuration spec of this component is stable the format of spans, tags, and logs created by Benthos is subject to change as it is tuned for improvement.

|Name|Tags|
|---|---|
|[gcp_cloudtrace](/resources/stacks/benthos/components/tracers/gcp_cloudtrace/)|GCP|
|[jaeger](/resources/stacks/benthos/components/tracers/jaeger/)|Jaeger|
|[none](/resources/stacks/benthos/components/tracers/none/)|None|
|[open_telemetry_collector](/resources/stacks/benthos/components/tracers/open_telemetry_collector/)|Open Telemetry Collector|