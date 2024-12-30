# Attributes of Volume manifest

## Structure of Volume manifest

```yaml 
## RESOURCE META SECTION
# Attributes commmon across all DataOS Resources
name: ${{resource_name}} # Name of the Resource (e.g., my-first-worker)
version: v1beta # Manifest version of the Resource
type: worker # Type of Resource
tags: # Tags for categorizing the Resource
  - ${{tag_example_1}} # Tags (e.g., dataos:worker)
  - ${{tag_example_2}} # Additional tags (e.g., dataos:workspace:curriculum)
description: ${{resource_description}} # Description of the resource (e.g., Common attributes applicable to all DataOS Resources)
owner: ${{resource_owner}} # Owner of the Resource (e.g., iamgroot)
layer: ${{resource_layer}} # DataOS Layer (e.g., user, system)

# VOLUME-SPECIFIC SECTION
# Attributes specific to Volume resource-type
volume:
   size: ${{1Gi} } #100Gi, 50Mi, 10Ti, 500Mi
   accessMode: ${{accessMode}} #Mode Eg: ReadWriteMany ReadWriteOnce, ReadOnlyMany 
   type: ${{typeofvolume}} #Volume type (e.g. temps)
```


## Configuration

### **Resource meta section configuration**


### **Volume-specific section configuration**


#### **`volume`**

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

#### **`size`**

**Description:** size of storage requested by user. 

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | 100Gi, 50Mi, 1Ti, 500Mi |

**Example Usage:**

```yaml
volume:
  size: 10Gi
```


#### **`accessMode`**

**ReadOnlyMany:** In this mode multiple pods running on different Nodes could connect to the storage and carry out read operation.

**ReadWriteMany:** In this mode multiple pods running on different Nodes could connect to the storage and carry out read and write operation.

**ReadWriteOnce:** the volume can be mounted as read-write by a single node. ReadWriteOnce access mode still can allow multiple pods to access the volume when the pods are running on the same node. For single pod access, please see ReadWriteOncePod.

**Description:** A Volume can be mounted on a host in any way each Volumes access modes are set to the specific modes.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | ReadWriteOnce, ReadOnlyMany, ReadWriteMany |

**Example Usage:**

```yaml
volume:
  accessMode: ReadWriteMany
```

#### **`type`**

**Description:** A temp Volume in Kubernetes is ephemeral storage allocated for a Pod's containers, created upon Pod assignment to a node, allowing read-write access but data is deleted permanently when the Pod is removed from the node.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | temp |

**Example Usage:**

```yaml
volume:
  type: temp
```

