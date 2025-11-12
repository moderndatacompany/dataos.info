# Configurations

This section provides details of each attribute configured in the Python Service manifest file.

```yaml
name: ${{service_name}}                  # e.g., python-service
version: v1
type: service
tags:
  - service
  - python-stack
  - dataos:type:resource
  - dataos:resource:service
  - dataos:layer:user
  - dataos:workspace:${{workspace_name}} # e.g., public
description: ${{service_description}}    # e.g., Python Service Sample
owner: ${{owner_name}}                   # e.g., iamgroot
workspace: ${{workspace_name}}           # e.g., public

service:
  servicePort: ${{service_port}}         # e.g., 8050
  ingress:
    enabled: true
    path: ${{ingress_path}}              # e.g., /test_sample
    noAuthentication: ${{no_auth}}       # e.g., true/false
  replicas: ${{replica_count}}           # e.g., 1
  stack: python3:1.0
  logLevel: ${{log_level}}               # e.g., INFO
  dataosSecrets:
    - name: ${{secret_name}}             # e.g., bitbucket-cred
      allKeys: true
      consumptionType: envVars
  compute: ${{compute_profile}}          # e.g., runnable-default
  resources:
    requests:
      cpu: ${{cpu_request}}              # e.g., 1000m
      memory: ${{memory_request}}        # e.g., 1536Mi
  stackSpec:
    repo:
      baseDir: ${{repo_base_dir}}        # e.g., queries/app
      syncFlags:
        - '--ref=${{repo_branch}}'       # e.g., main
      url: ${{repo_url}}                 # e.g., https://bitbucket.org/queries/

```

## name

**Description:** Unique name for the Resource. Must be unique within a workspace.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | Alphanumeric values with regex `[a-z0-9]([-a-z0-9]*[a-z0-9])` (max 48 chars) |

**Example usage:**

```yaml
name: python-service
```

---

## version

**Description:** Defines the version of the Resource.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | v1 |

**Example usage:**

```yaml
version: v1
```

---

## type

**Description:** Specifies the Resource type.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | cluster, compute, depot, policy, secret, service, stack, workflow |

**Example usage:**

```yaml
type: service
```

---

## tags

**Description:** Assign tags for classification and searchability.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list | mandatory | none | Any string |

**Example usage:**

```yaml
tags:
  - service
  - python-stack
  - dataos:type:resource
  - dataos:resource:service
  - dataos:layer:user
  - dataos:workspace:${{workspace_name}}
```

---

## description

**Description:** A human-readable explanation of the Service Resource.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | Any string |

**Example usage:**

```yaml
description: Python Service Sample
```

---

## owner

**Description:** The owner responsible for the Service Resource.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | Any string |

**Example usage:**

```yaml
owner: iamgroot
```

---

## workspace

**Description:** Defines the workspace where the Resource belongs.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | Any valid workspace name |

**Example usage:**

```yaml
workspace: public
```

---

## service

**Description:** Encapsulates Service configuration such as ports, ingress, replicas, runtime, secrets, compute, resources, and repo.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | mandatory | none | Contains attributes like servicePort, ingress, replicas, logLevel, compute, etc. |

**Example usage:**

```yaml
service:
  servicePort: 8050
  ingress:
    enabled: true
    path: /test_sample
    noAuthentication: true
  replicas: 1
  stack: python3:1.0
  logLevel: INFO
```

---

## servicePort

**Description:** Defines the port on which the Service runs.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| integer | mandatory | none | any valid port |

**Example usage:**

```yaml
servicePort: 8050
```

---

## ingress

**Description:** Configures external network access for the Service.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| object | optional | none | enabled, path, noAuthentication |

**Example usage:**

```yaml
ingress:
  enabled: true
  path: /test_sample
  noAuthentication: true
```

---

## replicas

**Description:** Number of Service instances to run.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| integer | optional | 1 | Any positive integer |

**Example usage:**

```yaml
replicas: 1
```

---

## stack

**Description:** Defines the runtime Stack and version.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | `<stack-name>:<version>` |

**Example usage:**

```yaml
stack: python3:1.0
```

---

## logLevel

**Description:** Logging level for debugging/monitoring.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | INFO | DEBUG, INFO, WARN, ERROR |

**Example usage:**

```yaml
logLevel: INFO
```

---

## dataosSecrets

**Description:** Secrets referenced into the Service.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list | optional | none | Secret names registered in DataOS |

**Example usage:**

```yaml
dataosSecrets:
  - name: bitbucket-cred
    allKeys: true
    consumptionType: envVars
```

---

## compute

**Description:** Defines the compute type where the Service runs.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | runnable-default | runnable-default, custom types |

**Example usage:**

```yaml
compute: runnable-default
```

---

## resources

**Description:** Specifies Compute Resource requests.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| object | optional | none | CPU and memory allocation |

**Example usage:**

```yaml
resources:
  requests:
    cpu: 1000m
    memory: 1536Mi
```

---

## stackSpec.repo

**Description:** Declares the repository containing the Service code.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| object | mandatory | none | Contains baseDir, syncFlags, url |

**Example usage:**

```yaml
stackSpec:
  repo:
    baseDir: queries/app
    syncFlags:
      - '--ref=main'
    url: https://bitbucket.org/queries
```

## repo.baseDir

**Description:** Directory inside the repo where `main.py` and `requirements.txt` are located.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | Valid relative path |

---

## repo.syncFlags

**Description:** Flags for git-sync, a branch reference.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list | optional | none | e.g., `--ref=main` |

---

## repo.url

**Description:** URL of the Git repository.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | HTTPS URL |