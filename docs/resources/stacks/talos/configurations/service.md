# Talos Service Configuration

This section describes each attribute of the Talos Service manifest file in detail.

```yaml
name: ${{talos-test}} # service name
version: ${{v1}} # version
type: service # resource type
tags: # tags
  - ${{service}}
  - ${{dataos:type:resource}}
  - ${{dataos:resource:service}}
  - ${{dataos:layer:user}}
description: ${{Talos Service}}
workspace: ${{public}}
service: # service specific section
  servicePort: 3000
  ingress:
    enabled: true
    stripPath: true
    path: /talos/${{workspace}}:${{talos-test}} # service name
    noAuthentication: true
  replicas: ${{1}}
  logLevel: ${{DEBUG}}
  compute: runnable-default
  envs:
    TALOS_SCHEMA_PATH: ${{talos/setup}}
    TALOS_BASE_PATH: /talos/public:${{talos-test}}
  resources:
    requests:
      cpu: ${{100m}}
      memory: ${{128Mi}}
    limits:
      cpu: ${{500m}}
      memory: ${{512Mi}}
  stack: talos:2.0
  dataosSecrets:
    - name: ${{bitrepo-r}}
      allKeys: true
  stackSpec:
    repo:
      url: ${{https://bitbucket.org/mywork15/talos/}}
      projectDirectory: ${{talos/setup}}
      syncFlags:
        - '--ref=main'
```

### `name`

**Description:** Unique identifier for the Talos service.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | Alphanumeric values with the RegEx [a-z0-9]([-a-z0-9]*[a-z0-9]). A hyphen/dash is allowed as a special character. The total length should be ≤ 48 characters. |

**Example Usage:**

```yaml
name: talos-test
```

### `version`

**Description:** The version of the Talos service.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | Alphanumeric values with the RegEx [a-z0-9]([-a-z0-9]*[a-z0-9]). A hyphen/dash is allowed as a special character. The total length should be ≤ 48 characters. |

**Example Usage:**

```yaml
version: v1
```

### `type`

**Description:** The type of resource this configuration represents.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | Descriptive string for the resource type (e.g., service). |

**Example Usage:**

```yaml
type: service
```

### `tags`

**Description:** Tags associated with the Talos service.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| list of strings | optional | none | List of tag strings for categorization and identification. |

**Example Usage:**

```yaml
tags:
  - service
  - dataos:type:resource
  - dataos:resource:service
  - dataos:layer:user
```

### `description`

**Description:** A brief description of the Talos service.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | Any descriptive text providing information about the service. |

**Example Usage:**

```yaml
description: Talos Service
```

### `workspace`

**Description:** The workspace environment where the Talos service is deployed.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | Descriptive string for the workspace environment (e.g., public). |

**Example Usage:**

```yaml
workspace: public
```

### `service`

**Description:** Configuration specific to the Talos service.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |

### `servicePort`

**Description:** Port on which the service will run.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| integer | mandatory | none | Port number for the service (e.g., 3000). |

**Example Usage:**

```yaml
servicePort: 3000
```

### `ingress`

**Description:** Ingress settings for routing traffic to the service.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |

### `enabled`

**Description:** Whether ingress is enabled.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| boolean | mandatory | false | true or false |

**Example Usage:**

```yaml
enabled: true
```

### `stripPath`

**Description:** Whether to strip the path from the incoming requests.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| boolean | mandatory | false | true or false |

**Example Usage:**

```yaml
stripPath: true
```

### `path`

**Description:** Path pattern for ingress routing.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | Path pattern including variables (e.g., /talos/${{workspace}}:${{talos-test}}). |

**Example Usage:**

```yaml
path: /talos/${{workspace}}:${{service-name}}
```

### `noAuthentication`

**Description:** Whether authentication is required.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| boolean | mandatory | false | true or false |

**Example Usage:**

```yaml
noAuthentication: true
```

### `replicas`

**Description:** Number of replicas for the service.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| integer | mandatory | 1 | Number of replicas (e.g., 1). |

**Example Usage:**

```yaml
replicas: 1
```

### `logLevel`

**Description:** Logging level for the service.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | INFO | Logging levels such as DEBUG, INFO, WARN, ERROR. |

**Example Usage:**

```yaml
logLevel: DEBUG
```

### `compute`

**Description:** Compute resource configuration.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | Descriptive string for compute resource (e.g., runnable-default). |

**Example Usage:**

```yaml
compute: runnable-default
```

### `envs`

**Description:** Environment variables for the service.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |

### `TALOS_SCHEMA_PATH`

**Description:** Path to the Talos schema.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | Path to the schema (e.g., talos/setup). |

**Example Usage:**

```yaml
TALOS_SCHEMA_PATH: ${{talos/setup}}
```

### `TALOS_BASE_PATH`

**Description:** Base path for Talos service.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | Base path for the service (e.g., /talos/public:${{talos-test}}). |

**Example Usage:**

```yaml
TALOS_BASE_PATH: /talos/public:${{talos-test}}
```

### `resources`

**Description:** Resource requests and limits for the service.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |

### `requests`

**Description:** Minimum resources requested by the service.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |

### `cpu`

**Description:** Minimum CPU resources.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | CPU requests (e.g., 100m). |

**Example Usage:**

```yaml
cpu: ${{100m}}
```

### `memory`

**Description:** Minimum memory resources.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | Memory requests (e.g., 128Mi). |

**Example Usage:**

```yaml
memory: ${{128Mi}}
```

### `limits`

**Description:** Maximum resources allowed for the service.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |

### `cpu`

**Description:** Maximum CPU resources.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | CPU limits (e.g., 500m). |

**Example Usage:**

```yaml
cpu: ${{500m}
```

### `memory`

**Description:** Maximum memory resources.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | Memory limits (e.g., 512Mi). |

**Example Usage:**

```yaml
memory: ${{512Mi}}
```

### `stack`

**Description:** Version of the Talos stack being used.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | Stack version (e.g., talos:2.0). |

**Example Usage:**

```yaml
stack: talos:2.0
```

### `dataosSecrets`

**Description:** Secrets used by the Talos service.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |

### `name`

**Description:** Name of the secret.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | Name of the secret (e.g., bitrepo-r). |

**Example Usage:**

```yaml
name: ${{bitrepo-r}}
```

### `allKeys`

**Description:** Whether all keys in the secret are to be used.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| boolean | mandatory | false | true or false. |

**Example Usage:**

```yaml
allKeys: true
```

### `stackSpec`

**Description:** Specification for the stack configuration.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |

### `repo`

**Description:** Repository configuration for the stack.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |

### `url`

**Description:** URL of the repository.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | URL of the repository (e.g., https://bitbucket.org/mywork15/talos/). |

**Example Usage:**

```yaml
url: ${{https://bitbucket.org/mywork15/talos/}
```

### `projectDirectory`

**Description:** Directory within the repository.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | Directory for the project (e.g., talos/setup). |

**Example Usage:**

```yaml
projectDirectory: ${{talos/setup}}
```

### `syncFlags`

**Description:** Flags for repository synchronization.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| list of strings | optional | none | List of flags for synchronization (e.g., --ref=main). |

**Example Usage:**

```yaml
syncFlags:
  - '--ref=main'
```