# Components

Every Benthos pipeline is a YAML config file, which acts as a recipe book telling what ingredients (sources) to use and how to use them (transformation). Talking structurally, a Benthos YAML config is made up of several components. They are depicted in the YAML below:

```yaml
# Service-Resrouce Section

version: v1 # Version
name: benthos-service # Name of the Service (Resource)
type: service # Type of Resource (Here its a Service)
service:
	# ...
	# ...
	# ... 
  stack: benthos   # Stack (Here it's Benthos)
  benthos:

# Benthos Stack-specific Section

# Main Components
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

# Observability Components
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

# Resource Components
	# Rate Limit Resource Component
		rate_limit_resources:
				{}
  # Cache Resource Component
		cache_resources: 
				{}
```

## Service Resource Section

At the core of any Benthos Service lies the Service section, which is responsible for defining a Service resource through a set of YAML fields and configurations. A Service is a persistent process that either receives or delivers API requests. The Benthos stack is then invoked within the Service to effectuate the requisite transformations. For a deeper understanding of Service and its associated YAML configurations, please refer to the following page:

[Service](/resources/service/)

## Benthos Stack Section

The Benthos Stack Section comprises of several components which are detailed below.

### **Main Components**

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

### **Observability Components**

There are also the observability components [http](/resources/stacks/benthos/components/http/), [logger](/resources/stacks/benthos/components/logger/), [metrics](/resources/stacks/benthos/components/metrics/), and [tracing](/resources/stacks/benthos/components/tracers/), which allow you to specify how Benthos exposes observability data:

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

### **Resource Components**

Finally, there are [caches](/resources/stacks/benthos/components/caches/) and [rate limits](/resources/stacks/benthos/components/rate_limit/). These are components that are referenced by core components and can be shared.

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

It's also possible to configure inputs, outputs, and processors as resources which allows them to be reused throughout a configuration with the [`resource` input](/resources/stacks/benthos/components/inputs/),  [`resource` output](/resources/stacks/benthos/components/output/),  and [`resource` processor](/resources/stacks/benthos/components/processors/), respectively.

For a thorough and comprehensive understanding of these magnificent components, do peruse the pages that lie beyond the links below. You might discover hidden secrets, juicy details, or even a surprise cameo appearance from your favorite celebrity component. Who knows, the possibilities are endless!

[HTTP](/resources/stacks/benthos/components/http/)

[Inputs](/resources/stacks/benthos/components/inputs/)

[Processors](/resources/stacks/benthos/components/processors/)

[Output](/resources/stacks/benthos/components/output/)

[Caches](/resources/stacks/benthos/components/caches/)

[Rate Limit](/resources/stacks/benthos/components/rate_limit/)

[Buffers](/resources/stacks/benthos/components/buffers/)

[Metrics](/resources/stacks/benthos/components/metrics/)

[Tracers](/resources/stacks/benthos/components/tracers/)

[Logger](/resources/stacks/benthos/components/logger/)