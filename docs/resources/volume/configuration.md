# Attributes of Volume manifest

## Structure of Volume manifest

```yaml 
## RESOURCE META SECTION
# Attributes commmon across all DataOS Resources
name: ${{resource_name}} # Name of the Resource (e.g., my-first-volume)
version: v1beta # Manifest version of the Resource
type: volume # Type of Resource
tags: # Tags for categorizing the Resource
  - ${{tag_example_1}} # Tags (e.g., dataos:volume)
  - ${{tag_example_2}} # Additional tags (e.g., dataos:workspace:curriculum)
description: ${{resource_description}} # Description of the resource (e.g., Common attributes applicable to all DataOS Resources)
owner: ${{resource_owner}} # Owner of the Resource (e.g., iamgroot)
layer: ${{resource_layer}} # DataOS Layer (e.g., user, system)

# VOLUME-SPECIFIC SECTION
# Attributes specific to Volume resource-type
volume:
  size: ${{1Gi}} #100Gi, 50Mi, 10Ti, 500Mi
  accessMode: ${{accessMode}} #Mode options ReadWriteMany | ReadWriteOnce | ReadOnlyMany 
  type: ${{typeofvolume}} #Volume type options persistent | temp | CloudTemp | CloudPersistent
```


## Resource meta section configuration

Click [here](/resources/manifest_attributes/) to learn about the Resource meta section configuration.

## Volume-specific section configuration


### **`volume`**

**Description:** The `volume` attribute defines a mapping that contains attributes specific to the Volume resource-type. 

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| mapping | mandatory | none | none |

**Example Usage:**

```yaml
# volumetest:v1beta:volume
version: v1beta
name: volumetest
type: volume
tags:
  - volume
  - dataos:type:resource
  - dataos:resource:volume
  - dataos:layer:user
  - dataos:workspace:public
description: example resource manifest
owner: iamgroot
layer: user
volume:
  size: 1Gi  #100Gi, 50Mi, 10Ti, 500Mi
  accessMode: ReadWriteMany  #ReadWriteOnce, ReadOnlyMany.
  type: temp
```

### **`size`**

**Description:** size of storage requested by user. 

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | 100Gi, 50Mi, 1Ti, 500Mi |

**Example Usage:**

```yaml
volume:
  size: 10Gi
```

### **`accessMode`**

**Description:** A Volume can be mounted on a host in any way each Volumes access modes are set to the specific modes.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | ReadWriteOnce, ReadOnlyMany, ReadWriteMany |

Following is the list of supported accessMode:

- **ReadOnlyMany:** In this mode multiple pods running on different Nodes could connect to the storage and carry out read operation.

- **ReadWriteMany:** The Volume can be mounted by multiple pods concurrently.

- **ReadWriteOnce:** The Volume can be mounted by only one pod at a time.


**Example Usage:**

```yaml
volume:
  accessMode: ReadWriteMany
```

### **`type`**

**Description:** A temp Volume in Kubernetes is ephemeral storage allocated for a Pod's containers, created upon Pod assignment to a node, allowing read-write access but data is deleted permanently when the Pod is removed from the node.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | temp |

Following is the list of all supported types:

**1. Managed by DataOS**

The Volume here can be attached with multiple workloads.

- **`temp`** 
- **`persistent`**  


**2. Managed by Cloud** 

The Volume can only be attached to a single workload.

- **`CloudTemp`**
- **`CloudPersistent`**

!!! info

    The Volume which are managed by cloud i.e. `CloudTemp` and `CloudPersistent` are compatible only with CLI version `2.27.2` or higher.

    You can only use `ReadWriteOnce` accessMode since here the Volume can only be attached with single workload . 


**Difference**

| Feature       | Managed by Cloud                                        | Managed by DataOS                                                    |
|---------------|---------------------------------------------|---------------------------------------------------------------|
| Performance   | High (SSD-backed, high IOPS)                | Moderate          |
| Cost          | Higher                                      | Lower                                                        |
| Expandability | Disk size can be increased, but requires a restart.   | Disk size can be increased while the workflow is running, without interruption.                     |
| Reliability   | SLA 99.99%                                  | Best-effort reliability                                      |
| Use Case      | Single workload requiring high-speed, durable storage | Suitable for shared state, coordination, or services running in parallel.    |

**When to use which??**

- Managed by Cloud: Choose for critical, latency-sensitive operations (e.g., ETL jobs with heavy IO).
- Managed by DataOS: Choose for cost-efficient, scalable data.



**Example Usage:**

```yaml
volume:
  type: temp
```

