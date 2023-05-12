# Components

Every Benthos pipeline is a YAML config file, which acts as a recipe book telling what ingredients (sources) to use and how to use them (transformation). Talking structurally, a Benthos YAML config is made up of several components. They are depicted in the YAML below:

```yaml
# PRIMITIVE/RESOURCE COMPONENT

version: v1 # Version
name: benthos-service # Name of the Service (Resource)
type: service # Type of Resource (Here its a Service)
service:
	# ...
	# ...
	# ... 
  stack: benthos   # Stack (Here it's Benthos)
  benthos:

# BENTHOS STACK COMPONENTS

# MAIN COMPONENTS 
	# Input Component 
    input:
				{} 
	# Buffer Component
		buffer:
				{} 
	# Pipeline Component 
    pipeline:
				{} 
	# Output Component
    output: 
				{} 

# OBSERVABILITY COMPONENTS 
	# Http component
		http:
			  {}
	# Logger Component
		logger:
			  {}
	# Metrics Component
		metrics:
			  {}
	# Tracer Component
		tracer:
				{}

# RESOURCE COMPONENTS
	# Rate Limit Resource Component
		rate_limit_resources:
				{}
  # Cache Resource Component
		cache_resources: 
				{}
```

## Primitive/Resource Component

At the core of any Benthos Service lies its Service Primitive/Resource Component, which is responsible for defining a Service Primitive through a set of YAML fields and configurations. The Service component defines a persistent process that either receives or delivers API requests. The Benthos stack is then invoked within the Service to effectuate the requisite transformations. For a deeper understanding of Services and their associated YAML configurations, please refer to the following page:

[Service](https://www.notion.so/Service-7e65eb7e49094f7bbf11fd17b1a35d0a)

## Benthos Stack Components

### Main Components

Benthos has at least one input, an optional buffer, an output, and any number of processors:

```yaml
input:
  kafka:
    addresses: [ TODO ]
    topics: [ foo, bar ]
    consumer_group: foogroup

buffer:
  type: none

pipeline:
  processors:
  - mapping: |
      message = this
      meta.link_count = links.length()

output:
  aws_s3:
    bucket: TODO
    path: '${! meta("kafka_topic") }/${! json("message.id") }.json'
```

These are the main components within Benthos and they provide the majority of useful behavior.

### Observability Components

There are also the observability components http, logger, metrics, and tracing, which allow you to specify how Benthos exposes observability data:

```yaml
http:
  address: 0.0.0.0:4195
  enabled: true
  debug_endpoints: false

logger:
  format: json
  level: WARN

metrics:
  statsd:
    address: localhost:8125
    flush_period: 100ms

tracer:
  jaeger:
    agent_address: localhost:6831
```

### Resource Components

Finally, there are caches and rate limits. These are components that are referenced by core components and can be shared.

```yaml
input:
  http_client: # This is an input
    url: TODO
    rate_limit: foo_ratelimit # This is a reference to a rate limit

pipeline:
  processors:
    - cache: # This is a processor
        resource: baz_cache # This is a reference to a cache
        operator: add
        key: '${! json("id") }'
        value: "x"
    - mapping: root = if errored() { deleted() }

rate_limit_resources:
  - label: foo_ratelimit
    local:
      count: 500
      interval: 1s

cache_resources:
  - label: baz_cache
    memcached:
      addresses: [ localhost:11211 ]
```

It's also possible to configure inputs, outputs, and processors as resources which allows them to be reused throughout a configuration with the `resource` input,  `resource` output,  and `resource` processor, respectively.

For a thorough and comprehensive understanding of these magnificent components, do peruse the pages that lie beyond the links below. You might discover hidden secrets, juicy details, or even a surprise cameo appearance from your favorite celebrity component. Who knows, the possibilities are endless!

[HTTP](./HTTP.md)

[Inputs](./Inputs/Inputs.md)

[Processors](./Processors/Processors.md)

[Output](./Output/Output.md)

[Caches](./Caches/Caches.md)

[Rate Limit](./Rate%20Limit/Rate%20Limit.md)

[Buffers](./Buffers/Buffers.md)

[Metrics](./Metrics/Metrics.md)

[Tracers](./Tracers/Tracers.md)

[Logger](./Logger.md)