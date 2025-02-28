
# Components

Every Bento pipeline is a YAML config file, which acts as a recipe book telling what ingredients (sources) to use and how to use them (transformation). Talking structurally, a Bento YAML config is made up of several components. They are depicted in the YAML below:

```yaml
# Service-Resrouce Section

version: v1 # Version
name: bento-service # Name of the Service (Resource)
type: service # Type of Resource (Here its a Service)
service:
	# ...
	# ...
	# ... 
  stack: bento:1.0   # Stack (Here it's Bento)
  stackSpec:

# Bento Stack-specific Section

# Main Components
	# Input Component 
    input:
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
```

## Service Resource Section

At the core of any Bento Service lies the Service section, which is responsible for defining a Service resource through a set of YAML fields and configurations. A Service is a persistent process that either receives or delivers API requests. The Bento stack is then invoked within the Service to effectuate the requisite transformations. For a deeper understanding of Service and its associated YAML configurations, please refer to the following page:

[Service](/resources/service/)

## Bento Stack Section

The Bento Stack Section comprises of several components which are detailed below.

### **Main Components**

Bento has at least one input, an optional buffer, an output, and any number of processors:

```yaml
input:
  kafka:
    addresses: [ TODO ]
    topics: [ foo, bar ]
    consumer_group: foogroup

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

These are the main components within Bento and they provide the majority of useful behavior.

### **Observability Components**

There are also the observability components [http](/resources/stacks/bento/components/http/), [logger](/resources/stacks/bento/components/logger/), [metrics](/resources/stacks/bento/components/metrics/), and [tracing](/resources/stacks/bento/components/tracers/), which allow you to specify how Bento exposes observability data:

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
```

### **Resource Components**

Finally, there are [caches](/resources/stacks/bento/components/caches/) and [rate limits](/resources/stacks/bento/components/rate_limit/). These are components that are referenced by core components and can be shared.

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
```

It's also possible to configure inputs, outputs, and processors as resources which allows them to be reused throughout a configuration with the [`resource` input](/resources/stacks/bento/components/inputs/),  [`resource` output](/resources/stacks/bento/components/output/),  and [`resource` processor](/resources/stacks/bento/components/processors/), respectively.

For a thorough and comprehensive understanding of these magnificent components, do peruse the pages that lie beyond the links below. You might discover hidden secrets, juicy details, or even a surprise cameo appearance from your favorite celebrity component. Who knows, the possibilities are endless!

[HTTP](/resources/stacks/bento/components/http/)

[Inputs](/resources/stacks/bento/components/inputs/)

[Processors](/resources/stacks/bento/components/processors/)

[Output](/resources/stacks/bento/components/output/)

[Buffers](/resources/stacks/bento/components/buffers/)

[Metrics](/resources/stacks/bento/components/metrics/)

[Logger](/resources/stacks/bento/components/logger/)