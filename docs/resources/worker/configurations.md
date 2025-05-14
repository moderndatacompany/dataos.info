# Attributes of Worker Manifest

## Structure of Worker manifest

```yaml title="worker_manifest_reference.yml"
--8<-- "examples/resources/worker/manifest_reference.yml"
```

## Configuration

### **Resource meta section**

This section serves as the header of the manifest file, defining the overall characteristics of the Worker Resource you wish to create. It includes attributes common to all types of Resources in DataOS. These attributes help DataOS in identifying, categorizing, and managing the Resource within its ecosystem. To learn about the Resources of this section, refer to the following link: [Attributes of Resource meta section]().


### **Worker-specific section**

This section comprises attributes specific to the Worker Resource. The attributes within the section are listed below:


##### **`worker`**

**Description:** The `worker` attribute defines a mapping that contains attributes specific to the Worker resource-type. 

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| mapping | mandatory | none | none |

**Example Usage:**

```yaml
name: bento3-worker-sample
version: v1beta
type: worker
tags:
    - worker
    - dataos:type:resource
    - dataos:resource:worker
    - dataos:layer:user
    - dataos:workspace:public
description: Random User Console
worker:
  tags:
  - worker
  highAvailabilityConfig:
    level: hostname #hostname/region/zone
    mode: preferred #preferred/required
  replicas: 2
  stack: bento-worker:3.0
  logLevel: DEBUG
  compute: runnable-default
  stackSpec:
  input:
      http_client:
      headers:
          Content-Type: application/octet-stream
      url: https://randomuser.me/api/
      verb: GET
  output:
      stdout:
      codec: |
          delim:
            -----------GOOD------------
```

---

#### **`title`**

**Description:** The `title` attribute specifies the title of the Worker. It provides a descriptive title for the Worker.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | optional | none | any valid string |

**Example Usage:**

```yaml
title: bento worker
```

---

#### **`tags`**

**Description:** The `tags` attribute is used to assign tags to the Worker. Tags are labels that can be used for categorization or identification in Metis.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| list of strings | optional | none | list of valid strings |

**Example Usage:**

```yaml
tags:
  - tag1
  - tag2
```

---

#### **`highAvailabilityConfig`**

**Description:** The highAvailabilityConfig section defines how multiple replicas of the worker are distributed across infrastructure boundaries such as hostnames, zones, or regions. This ensures that if one replica becomes unavailable due to an issue in a specific part of the infrastructure, other replicas continue to operate independently.

**Example Usage**

```yaml
highAvailabilityConfig:
  level: hostname         # Options: hostname | zone | region
  mode: preferred         # Options: preferred | required
  tags:
    - worker
  replicas: 3
```
#### **`level`**

**Description:** Specifies the level across which replicas should be distributed. This determines the intended placement separation — at the host, zone, or region level. The actual distribution is dependent on the mode. If the required number of distinct units is not available and mode is preferred, replicas may be placed on the same unit. If mode is required and separation cannot be satisfied, the worker will fail.

| Data Type | Requirement | Default Value | Possible Values |
|-----------|-------------|----------------|------------------|
| string    | optional    |     none       | `hostname`, `zone`, `region` |

**Example Usage**

```yaml
highAvailabilityConfig:
  level: hostname         # Options: hostname | zone | region
  mode: preferred         # Options: preferred | required
  tags:
    - worker
  replicas: 3
```

#### **`mode`**

**Description:** Specifies how strictly the system should apply the separation defined by the level field.

- If set to `preferred`, the system will try to place each replica on a different hostname (machine), zone, or region as specified by level. If not enough distinct options are available, it will still proceed and place replicas together if needed.

- If set to `required`, the system will place replicas only if it can exactly meet the separation defined by level. If not enough hostnames (machines), zones, or regions are available, the worker will fail.


| Data Type | Requirement | Default Value | Possible Values |
|-----------|-------------|---------------|------------------|
| string    |  optional   |    none       | `preferred`, `required` |

**Example Usage**

```yaml
highAvailabilityConfig:
  level: hostname         # Options: hostname | zone | region
  mode: preferred         # Options: preferred | required
  tags:
    - worker
  replicas: 3
```

#### **`replicas`**

**Description:** The `replicas` attribute specifies the number of replicas for the Worker. Replicas are multiple instances of the Worker that run concurrently.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| integer | optional | 1 | any positive integer |

**Example Usage:**

```yaml
replicas: 3
```

---

#### **`autoscaling`**

**Description:** The `autoscaling` attribute is used to configure autoscaling for the Worker. Autoscaling allows the Worker to automatically adjust the number of replicas based on resource utilization.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| mapping | optional | none | none |

**Example Usage:**

```yaml
autoscaling:
  enabled: true
  minReplicas: 1
  maxReplicas: 3
  targetMemoryUtilizationPercentage: 60
  targetCPUUtilizationPercentage: 70
```

---

#### **`stack`**

**Description:** The `stack` attribute specifies the name of the stack that the Worker orchestrates.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | valid stack name |

**Example Usage:**

```yaml
stack: bento
```

---

#### **`logLevel`**

**Description:** The `logLevel` attribute sets the logging level for the Worker. It determines the verbosity of log messages generated by the Worker.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | optional | INFO | valid log levels (e.g., INFO, DEBUG, ERROR) |

**Example Usage:**

```yaml
logLevel: INFO
```

---

#### **`configs`**

**Description:** The `configs` attribute allows you to specify custom configurations for the Worker. It provides a way to customize the behavior of the Worker.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| mapping | optional | none | valid custom configurations in key-value format |

**Example Usage:**

```yaml
configs:
  alpha: beta
  gamma: sigma
```

---

#### **`envs`**

**Description:** The `envs` attribute is used to define environment variables for the Worker. These variables can be used to configure the Worker's runtime environment.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| mapping | optional | none | valid environment variable definitions |

**Example Usage:**

```yaml
envs:
    DATAOS_RESOURCE_LIFECYCLE_EVENT_TOPIC: '************************'
    DATAOS_RESOURCE_LIFECYCLE_EVENT_TOPIC_SUBS_NAME: '********************'
    DATAOS_TOPIC_COLLATED_RESOURCE_OFFSET: '******'
```

---

#### **`secrets`**

> To be deprecated
> 

**Description:** The `secrets` attribute specifies Secrets required by the Worker. Secrets are DataOS Resources that stored sensitive pieces of information securely within the Heimdall vault.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| list of mappings | optional | none | list of secret definitions |

**Example Usage:**

```yaml
secrets:
  - mysecret
```

---

#### **`dataosSecrets`**

**Description:** The `dataosSecrets` attribute is used to define DataOS Secret Resources required by the Worker. DataOS Secret Resources are securely managed secrets used within the Heimdall vault.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| list of mappings | optional | none | list of DataOS secret definitions |

**Example Usage:**

```yaml
dataosSecrets:
  - name: random        # mandatory
    workspace: delta    # mandatory
    key: hola
    keys:
      - list
      - abcd
    allKeys: true
    consumptionType: hola
```

#### **`dataosVolumes`**

**Description:** The `dataosVolumes` attribute specifies volumes required by the Worker. Volumes are used to provide storage for the Worker's data.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| list of mappings | optional | none | list of volume definitions |

**Example Usage:**

```yaml
dataosVolumes:
  - name: devolume
    directory: random
    readOnly: true
    subPath: "dev/hola"
```

---

#### **`tempVolume`**

**Description:** The `tempVolume` attribute specifies a temporary volume associated with the Worker. Temporary volumes are used for temporary storage.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | optional | none | valid volume name |

**Example Usage:**

```yaml
tempVolume: hola
```

---

#### **`persistentVolume`**

**Description:** The `persistentVolume` attribute specifies a persistent volume associated with the Worker. Persistent volumes are used for long-term storage.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| mapping | optional | none | valid persistent volume definition |

**Example Usage:**

```yaml
persistentVolume:
  name: devta
  directory: iamgroot
  readOnly: true/false
  subPath: dev/hola
```

---

#### **`compute`**

**Description:** The `compute` attribute defines the Compute Resource referred by the Worker. 

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | runnable-default or any other valid Compute Resource name |

**Example Usage:**

```yaml
compute: runnable-default
```

---

#### **`resources`**

**Description:** The `resources` attribute specifies the resource requests and limits for the Worker. It defines the computational resources required by the Worker.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| mapping | optional | none | valid resource requests and limits |

**Example Usage:**

```yaml
resources:
  requests:
    cpu: 1000m
    memory: 100Mi
  limits:
    cpu: 1000m
    memory: 100Mi
```

---

#### **`dryRun`**

**Description:** The `dryRun` attribute determines whether the Worker should run in a dry run mode. In dry run mode, the Worker doesn't perform actual execution but simulates the process.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| boolean | optional | false | true or false |

**Example Usage:**

```yaml
dryRun: false
```

---

#### **`runAsApiKey`**

**Description:** The `runAsApiKey` attribute specifies the DataOS API key used for running the Worker. It determines the identity under which the Worker operates.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | optional | none | valid DataOS API key |

**Example Usage:**

```yaml
runAsApiKey: abcdefghijklmnopqrstuvwxyz
```

---

#### **`runAsUser`**

**Description:** The `runAsUser` attribute defines the user identity under which the Worker runs. It specifies the user account associated with the Worker.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | optional | none | valid user-id |

**Example Usage:**

```yaml
runAsUser: iamgroot
```

---

#### **`topology`**

**Description:** The `topology` attribute is used to define the topology of the Worker. It specifies the elements and dependencies within the Worker's topology.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| list of mappings | mandatory | none | list of topology element definitions |

**Example Usage:**

```yaml
topology:
  - name: random            # mandatory
    type: alpha             # mandatory
    doc: new                # Documentation for the element
    properties:
      random: lost          # Custom properties for the element
    dependencies:
      - new1
      - new2
```

### **Stack-specific section**

#### **`stackSpec`**

> Attributes named `flare`/`bento`/`beacon`/`scanner`/`alpha` has been deprecated and will be removed in future releases, please replace with the generic `stackSpec`
> 

**Description:** This attribute allows for specifying stack-specific attributes. These attributes are specific to the stack configuration used by the Worker.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| mapping | optional | none | valid stack-specific attributes |

**Example Usage:**

```yaml
stackSpec/flare/bento/beacon/scanner/alpha:
  ${{Stack-specific Attributes}}
```