# Compute YAML Configuration Field Reference

The Compute YAML Field Reference provides a comprehensive overview of the configuration fields available for the Compute resource.

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
<center><i> Compute YAML Configuration </i></center>

## Configuration Fields

### **`compute`**
<b>Description:</b> Compute-specific key-value properties are declared within the Compute section <br>
<b>Data Type:</b> Object <br>
<b>Requirement:</b> Mandatory <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> None <br>
<b>Example Usage:</b>
```yaml
compute:
  dataplane: ${hub} # Dataplane resource
  purpose: ${runnable} # Purpose
  nodePool: # Nodepool section
    {}
```

### **`dataplane`**
<b>Description:</b> Dataplane resource <br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Mandatory <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> hub <br>
<b>Example Usage:</b>
```yaml
dataplane: hub # Dataplane resource
```

### **`purpose`**
<b>Description:</b> Purpose of the Compute <br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Mandatory <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> runnable/query/gpu <br>
<b>Example Usage:</b>
```yaml
purpose: gpu # Compute Purpose
```

### **`nodePool`**
<b>Description:</b> Node Pool specific key-value properties are declared in the nodePool section<br>
<b>Data Type:</b> Object <br>
<b>Requirement:</b> Mandatory <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> None <br>
<b>Example Usage:</b>
```yaml
nodePool: # Nodepool Section
    {}
```

### **`nodeSelector`**
<b>Description:</b> The nodeSelector section allows you to specify key-value properties for node selection. By using the nodeSelector property in the compute specification, you can define the desired node labels for the target node. Kubernetes will only schedule the Pod onto nodes that have all the specified labels. <br>
<b>Data Type:</b> Object <br>
<b>Requirement:</b> Mandatory <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> None <br>
<b>Example Usage:</b>
```yaml
nodeSelector: # Node Selector Section
    dataos.io/purpose: runnable # Purpose could be either runnable/gpu/query
```

### **`tolerations`**
<b>Description:</b> The tolerations section allows you to control the scheduling of pods on nodes with specific taints. Taints are properties assigned to nodes that repel pods from being scheduled on them. By adding tolerations to your pods, you can specify the key, operator, value, and effect properties to allow certain pods to be scheduled on tainted nodes. Applying one or more taints to a node is similar to assigning labels. Nodes will reject pods that do not tolerate all the specified taints. <br>
<b>Data Type:</b> Object <br>
<b>Requirement:</b> Mandatory <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> None <br>
<b>Example Usage:</b>
```yaml
tolerations:
  - key: "dedicated" # Key
    operator: "Equal" # Operator
    value: "runnable" # Value
    effect: "NoSchedule" # Effect
```

### **`key`**
<b>Description:</b> The key represents a string of up to 253 characters. It must start with a letter or a number and can contain letters, numbers, hyphens, dots, and underscores. <br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Mandatory <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> Any string starting with a letter or a number, and could contain letters, numbers, hyphens, dots, and underscores. Its length must be less than 253 characters<br>
<b>Example Usage:</b>
```yaml
key: dedicated # Key
```

### **`operator`**
<b>Description:</b> The operator specifies the operator for the toleration. There are two possible values: "Equal" and "Exists". <br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Mandatory <br>
<b>Default Value:</b> Equal <br>
<b>Possible Value:</b> Equal/Exists <br>
<b>Additional Details:</b><br>
- <i>Equal:</i>The key/value/effect parameters must match for the toleration to be effective.<br>
- <i>Exists:</i>The key/effect parameters must match. You can leave the value parameter blank to match any value.<br>

<b>Example Usage:</b>
```yaml
operator: Equal # Operator
```

### **`value`**
<b>Description:</b> The value represents a string of up to 63 characters. It must start with a letter or a number and can contain letters, numbers, hyphens, dots, and underscores. <br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Mandatory <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> Any string up to 63 characters. It must start with a letter or a number and can contain letters, numbers, hyphens, dots, and underscores. <br>
<b>Example Usage:</b>
```yaml
value: runnable # Value
```

### **`effect`**
<b>Description:</b> The effect specifies the action that should be taken when a pod does not tolerate the taint. It can have one of the following values: "NoSchedule", "PreferNoSchedule", or "NoExecute". <br>
<b>Data Type:</b> String <br>
<b>Requirement:</b> Mandatory <br>
<b>Default Value:</b> None <br>
<b>Possible Value:</b> NoSchedule/PreferNoSchedule/NoExecute <br>
<b>Additional Details:</b><br>
- <i>NoSchedule:</i>New pods that do not match the taint are not scheduled on the node, while existing pods on the node remain unaffected.<br>
- <i>PreferNoSchedule:</i>New pods that do not match the taint might be scheduled onto the node, but the scheduler tries to avoid it. Existing pods on the node remain unaffected.<br>
- <i>NoExecute:</i>New pods that do not match the taint cannot be scheduled onto the node, and existing pods on the node that do not have a matching toleration are removed.<br>
<b>Example Usage:</b>
```yaml
effect: NoSchedule # Effect
```