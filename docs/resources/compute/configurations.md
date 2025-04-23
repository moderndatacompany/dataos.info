# Attributes of Compute-specific Section

This documentation provides a comprehensive overview of the configuration attributes available for the Compute-specifc Section within a Compute Resource YAML.

## Structure of Compute-specific Section

The YAML syntax below demonstrates the structure of the Compute-specfic section:

```yaml
compute:
  dataplane: ${{hub}}
  purpose: ${{runnable}}
  nodePool:
    nodeSelector:
      ${{"dataos.io/purpose": "runnable"}}
    tolerations:
      - key: ${{"dedicated"}}
        operator: ${{"Equal"}}
        value: ${{"runnable"}}
        effect: ${{"NoSchedule"}}
```
<center><i> Compute-specific section YAML configuration </i></center>

## Configuration Attributes

## `compute

<b>Description:</b> compute-specific attributes are declared within the Compute section specifed by the <code>compute</code> key<br>

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|------------------|-----------------|-------------------|-------------------|
| mapping          | mandatory       | none              | none              |

<b>Example Usage:</b>
```yaml
compute: 
    {}
```
---

### **`dataplane`**

<b>Description:</b> the dataplane attribute specifies the name of the Dataplane Resource for which the Compute Resource is being created <br>

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|------------------|-----------------|-------------------|-------------------|
| string          | mandatory       | none              | hub              |

<b>Example Usage:</b>
```yaml
dataplane: hub 
```
---

### **`purpose`**

<b>Description:</b> the purpose attribute indicates the purpose of the Compute Resource <br>

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|------------------|-----------------|-------------------|-------------------|
| string          | mandatory       | none              | runnable/query/gpu         |

<b>Example Usage:</b>
```yaml
purpose: gpu 
```
---

### **`nodePool`**

<b>Description:</b> the nodePool attribute represents node pool specific key-value properties declared in the nodePool mapping<br>

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|------------------|-----------------|-------------------|-------------------|
| mapping          | mandatory       | none              | none              |

<b>Example Usage:</b>
```yaml
nodePool:
  {}
```
---

#### **`nodeSelector`**

<b>Description:</b> the nodeSelector section allows the specification of key-value properties for node selection. By using the nodeSelector property in the compute specification, desired node labels for the target node can be defined. Kubernetes will only schedule the Pod onto nodes that have all the specified labels. <br>

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|------------------|-----------------|-------------------|-------------------|
| mapping          | mandatory       | none              | dataos.io/purpose: runnable/query/gpu |

<b>Additional Details:</b>For the other custom Compute Resource the key-value pair depends on the cloud providers.<br>
<b>Example Usage:</b>
```yaml
nodeSelector: 
  dataos.io/purpose: runnable 
```
---

#### **`tolerations`**

<b>Description:</b> the tolerations section/mapping allows control over the scheduling of pods on nodes with specific taints. Taints are properties assigned to nodes that repel pods from being scheduled on them. By adding tolerations to pods, the key, operator, value, and effect attributes can be specified to allow certain pods to be scheduled on tainted nodes. <br>

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|------------------|-----------------|-------------------|-------------------|
| mapping          | mandatory       | none              | none |

<b>Example Usage:</b>
```yaml
tolerations:
  - key: "dedicated" 
    operator: "Equal" 
    value: "runnable" 
    effect: "NoSchedule" 
```
---

##### **`key`**
<b>Description:</b> the key attribute represents a string of up to 253 characters. It must start with a letter or a number and can contain letters, numbers, hyphens, dots, and underscores<br>

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|------------------|-----------------|-------------------|-------------------|
| string          | mandatory       | none              | any string starting with<br>a letter or a number, and<br>could contain letters, numbers,<br> hyphens, dots, and underscores.<br>Its length must be less than 253<br>characters |

<b>Example Usage:</b>
```yaml
key: dedicated 
```
---

##### **`operator`**
<b>Description:</b> the operator specifies the operator for the toleration. There are two possible values: "Equal" and "Exists". <br>

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|------------------|-----------------|-------------------|-------------------|
| string          | mandatory       | Equal              | Equal/Exists |

<b>Additional Details:</b><br>
<ul><li><i>Equal: </i>The key/value/effect parameters must match for the toleration to be effective.<br></li>
<li><i>Exists:</i>The key/effect parameters must match. You can leave the value parameter blank to match any value.<br></li></ul>

<b>Example Usage:</b>
```yaml
operator: Equal 
```
---

##### **`value`**
<b>Description:</b> the value represents a string of up to 63 characters. It must start with a letter or a number and can contain letters, numbers, hyphens, dots, and underscores. <br>

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|------------------|-----------------|-------------------|-------------------|
| string          | mandatory       | none              | any string up to 63 characters.<br>It must start with a letter or<br>a number and can contain letters,<br>numbers, hyphens, dots, and underscores. |

<b>Example Usage:</b>
```yaml
value: runnable 
```
---

##### **`effect`**
<b>Description:</b> the effect specifies the action that should be taken when a pod does not tolerate the taint. It can have one of the following values: "NoSchedule", "PreferNoSchedule", or "NoExecute". <br>

| **Data Type**    | **Requirement** | **Default Value** | **Possible Value** |
|------------------|-----------------|-------------------|-------------------|
| string          | mandatory       | none              | NoSchedule/PreferNoSchedule/NoExecute |


<b>Additional Details:</b><br>
<ul><li><i>NoSchedule: </i>New pods that do not match the taint are not scheduled on the node, while existing pods on the node remain unaffected.<br></li>
<li><i>PreferNoSchedule: </i>New pods that do not match the taint might be scheduled onto the node, but the scheduler tries to avoid it. Existing pods on the node remain unaffected.<br></li>
<li><i>NoExecute: </i>New pods that do not match the taint cannot be scheduled onto the node, and existing pods on the node that do not have a matching toleration are removed.<br></li></ul>

<b>Example Usage:</b>
```yaml
effect: NoSchedule 
```