# Fastbase Depot

The Fastbase Depot output writes messages to a DataOS Depot endpoint and waits for acknowledgment before returning control to the input. It is designed to be used through a broker, enabling fan-out to multiple outputs, including a Fastbase Depot and optional debugging sinks such as stdout.

## Output configuration
```yaml

output:
  - broker:
      pattern: fan_out
      outputs:

        # Output to DataOS Depot
        - plugin:
            type: dataos_depot
            address: dataos://fastbase:default/test08
            metadata:
              auth:
                token:
                  enabled: true
                  token: ${AUTH_TOKEN}
              description: Random users data
              format: AVRO
              schema: |
                {
                  "name": "default",
                  "type": "record",
                  "namespace": "defaultNamespace",
                  "fields": [
                    { "name": "age", "type": "int" },
                    { "name": "city", "type": "string" },
                    { "name": "dob", "type": "string" },
                    { "name": "email", "type": "string" },
                    { "name": "gender", "type": "string" },
                    { "name": "name", "type": "string" },
                    { "name": "page", "type": "int" },
                    { "name": "seed", "type": "string" }
                  ]
                }
              schemaLocation: http://registry.url/schemas/ids/12
              title: Random Users Info
              type: STREAM

        # Output to stdout
        - stdout: {}

```

## Fields

### **`output`**

Root list of one or more outputs. A broker can be used to fan messages out to multiple sinks.

Type: `array`

---

### **`broker`**

Container for multiple outputs executed according to a pattern.

Type: `object`

---

### **`broker.pattern`**

Execution pattern for child outputs. The `fan_out` pattern writes each message to all listed outputs.

Type: `string`
Default: `fan_out`

---

### **`broker.outputs`**

Child outputs to execute under the broker.

Type: `array`

---

### **`plugin`**

Arbitrary output plugin block. When `type` is `dataos_depot`, messages are written to a DataOS Depot endpoint.

Type: `object`

---

### **`plugin.type`**

The plugin implementation to invoke.

Type: `string`
Default: `dataos_depot`

---

### **`plugin.address`**

Target Depot address in DataOS URI form.

Type: `string`

```yaml
# Example
address: dataos://fastbase:default/test08
```

---

### **`plugin.metadata`**

Metadata for the Depot write operation, including authentication and schema controls.

Type: `object`

---

### **`plugin.metadata.auth`**

Authentication configuration.

Type: `object`

---

### **`plugin.metadata.auth.token.enabled`**

Whether token-based authentication is enabled.

Type: `boolean`
Default: `false`

---

### **`plugin.metadata.auth.token.token`**

Bearer token used for Depot authentication. It must be provided securely (for example, through a secret or environment variable).

Type: `string`

```yaml
# Example
auth:
  token:
    enabled: true
    token: ${DEPOT_TOKEN}
```

---

### **`plugin.metadata.description`**

Human-readable description of the data written.

Type: `string`

---

### **`plugin.metadata.format`**

Serialization format of the payload sent to the Depot.

Type: `string`
Default: `AVRO`

---

### **`plugin.metadata.schema`**

Avro schema as a JSON string. It must match the payload structure.

Type: `string`

```yaml
# Example
schema: >
  {"name":"default","type":"record","namespace":"defaultNamespace",
   "fields":[{"name":"age","type":"int"}]}
```

---

### **`plugin.metadata.schemaLocation`**

URI of the schema in a registry or repository. When provided, it can be used to resolve the schema externally.

Type: `string` (URI)

---

### **`plugin.metadata.title`**

Title associated with the stream or dataset.

Type: `string`

---

### **`plugin.metadata.type`**

Depot output mode.

Type: `string`
Default: `STREAM`

---

### **`stdout`**

Optional debugging output that prints messages to standard output. It is intended for validation during development and should be removed or disabled in production configurations.

Type: `object`

```yaml
# Example
stdout: {}
```
