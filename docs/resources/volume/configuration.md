# Attributes of Volume Manifest

## Structure of Worker manifest

```yaml title=""
--8 "/home/aayushisolanki/V3/dataos.info/docs/examples/resources/volume/manifest_reference.yaml"
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

