# Compute Resource Grammar

The Compute Resource Grammar provides a comprehensive overview of the configuration fields available for the Compute Resource (or the Compute-specifc Section).

## Syntax
The syntax below demonstrates the structure of the Compute YAML configuration:

```yaml
compute:
  dataplane: {{hub}}
  purpose: {{runnable}}
  nodePool:
    nodeSelector:
      {{"dataos.io/purpose": "runnable"}}
    tolerations:
      - key: {{"dedicated"}}
        operator: {{"Equal"}}
        value: {{"runnable"}}
        effect: {{"NoSchedule"}}
```
<center><i> Compute YAML configuration </i></center>

## Configuration Attribute/Fields

### **`compute`**
<b>Description:</b> compute-specific key-value properties are declared within the Compute section specifed by the compute field <br>
<b>Data Type:</b> object <br>
<b>Requirement:</b> mandatory <br>
<b>Default Value:</b> none <br>
<b>Possible Value:</b> none <br>
<b>Example Usage:</b>
```yaml
compute: 
    {}
```
---

### **`dataplane`**
<b>Description:</b> the dataplane field specifies the name of the Dataplane Resource for which the Compute Resource is being created <br>
<b>Data Type:</b> string <br>
<b>Requirement:</b> mandatory <br>
<b>Default Value:</b> none <br>
<b>Possible Value:</b> hub <br>
<b>Example Usage:</b>
```yaml
dataplane: hub 
```
---

### **`purpose`**
<b>Description:</b> the purpose field indicates the purpose of the Compute Resource <br>
<b>Data Type:</b> string <br>
<b>Requirement:</b> mandatory <br>
<b>Default Value:</b> none <br>
<b>Possible Value:</b> runnable/query/gpu <br>
<b>Example Usage:</b>
```yaml
purpose: gpu 
```
---

### **`nodePool`**
<b>Description:</b> the nodePool field represents node pool specific key-value properties declared in the nodePool section<br>
<b>Data Type:</b> object <br>
<b>Requirement:</b> mandatory <br>
<b>Default Value:</b> none <br>
<b>Possible Value:</b> none <br>
<b>Example Usage:</b>
```yaml
nodePool: 
    {}
```
---

### **`nodeSelector`**
<b>Description:</b> the nodeSelector section allows the specification of key-value properties for node selection. By using the nodeSelector property in the compute specification, desired node labels for the target node can be defined. Kubernetes will only schedule the Pod onto nodes that have all the specified labels. <br>
<b>Data Type:</b> object <br>
<b>Requirement:</b> mandatory <br>
<b>Default Value:</b> none <br>
<b>Possible Value:</b> <br>
  - key - `dataos.io/purpose` 
  - value - runnable/query/gpu. 
  
  For the other custom compute resource the key-value pair depends on the cloud providers. <br>
<b>Example Usage:</b>
```yaml
nodeSelector: 
    dataos.io/purpose: runnable 
```
---

### **`tolerations`**
<b>Description:</b> the `tolerations` section allows control over the scheduling of pods on nodes with specific taints. Taints are properties assigned to nodes that repel pods from being scheduled on them. By adding tolerations to pods, the key, operator, value, and effect attributes can be specified to allow certain pods to be scheduled on tainted nodes. <br>
<b>Data Type:</b> object <br>
<b>Requirement:</b> mandatory <br>
<b>Default Value:</b> none <br>
<b>Possible Value:</b> none <br>
<b>Example Usage:</b>
```yaml
tolerations:
  - key: "dedicated" 
    operator: "Equal" 
    value: "runnable" 
    effect: "NoSchedule" 
```
---

### **`key`**
<b>Description:</b> the `key` field represents a string of up to 253 characters. It must start with a letter or a number and can contain letters, numbers, hyphens, dots, and underscores<br>
<b>Data Type:</b> string <br>
<b>Requirement:</b> mandatory <br>
<b>Default Value:</b> none <br>
<b>Possible Value:</b> any string starting with a letter or a number, and could contain letters, numbers, hyphens, dots, and underscores. Its length must be less than 253 characters<br>
<b>Example Usage:</b>
```yaml
key: dedicated 
```
---

### **`operator`**
<b>Description:</b> the operator specifies the operator for the toleration. There are two possible values: "Equal" and "Exists". <br>
<b>Data Type:</b> string <br>
<b>Requirement:</b> mandatory <br>
<b>Default Value:</b> Equal <br>
<b>Possible Value:</b> Equal/Exists <br>
<b>Additional Details:</b><br>
- <i>Equal:</i>The key/value/effect parameters must match for the toleration to be effective.<br>
- <i>Exists:</i>The key/effect parameters must match. You can leave the value parameter blank to match any value.<br>

<b>Example Usage:</b>
```yaml
operator: Equal 
```
---

### **`value`**
<b>Description:</b> the value represents a string of up to 63 characters. It must start with a letter or a number and can contain letters, numbers, hyphens, dots, and underscores. <br>
<b>Data Type:</b> string <br>
<b>Requirement:</b> mandatory <br>
<b>Default Value:</b> none <br>
<b>Possible Value:</b> any string up to 63 characters. It must start with a letter or a number and can contain letters, numbers, hyphens, dots, and underscores. <br>
<b>Example Usage:</b>
```yaml
value: runnable 
```
---

### **`effect`**
<b>Description:</b> the effect specifies the action that should be taken when a pod does not tolerate the taint. It can have one of the following values: "NoSchedule", "PreferNoSchedule", or "NoExecute". <br>
<b>Data Type:</b> string <br>
<b>Requirement:</b> mandatory <br>
<b>Default Value:</b> none <br>
<b>Possible Value:</b> NoSchedule/PreferNoSchedule/NoExecute <br>
<b>Additional Details:</b><br>
- <i>NoSchedule:</i>New pods that do not match the taint are not scheduled on the node, while existing pods on the node remain unaffected.<br>
- <i>PreferNoSchedule:</i>New pods that do not match the taint might be scheduled onto the node, but the scheduler tries to avoid it. Existing pods on the node remain unaffected.<br>
- <i>NoExecute:</i>New pods that do not match the taint cannot be scheduled onto the node, and existing pods on the node that do not have a matching toleration are removed.<br>

<b>Example Usage:</b>
```yaml
effect: NoSchedule 
```