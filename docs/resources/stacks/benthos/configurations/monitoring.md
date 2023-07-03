# Monitoring

## Health Checks

Benthos serves two HTTP endpoints for health checks:

- `/ping` can be used as a liveness probe as it always returns a 200.
- `/ready` can be used as a readiness probe as it serves a 200 only when both the input and output are connected, otherwise, a 503 is returned.

## Metrics

Benthos exposes lots of metrics either to Statsd, Prometheus, Cloudwatch, or for debugging purposes, an HTTP endpoint that returns a JSON-formatted object.

The target destination of Benthos metrics is configurable from the metrics section, where it's also possible to rename and restrict the metrics that are emitted with mappings.

## Tracing

Benthos also emits opentracing events to a tracer of your choice, which can be used to visualize the processors within a pipeline.