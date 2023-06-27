
# Compute Templates


## runnable template

### **For ETL Workloads**

```yaml
compute:
  dataplane: hub
  purpose: runnable
  nodePool:
    nodeSelector:
      {{"dataos.io/purpose": "runnable"}}
    tolerations:
      - key: {{"dedicated"}}
        operator: {{"Equal"}}
        value: {{"runnable"}}
        effect: {{"NoSchedule"}}
```


<details>
<summary> 
Sample Runnable Compute YAML</summary>

```yaml
# Resource Section
name: "runnable-default-01"
version: v1
type: compute
layer: system
description: "runnable compute"
# Compute-specific Section (for runnables)
compute:
  dataplane: hub
  purpose: runnable
  nodePool:
    nodeSelector:
      "dataos.io/purpose": "runnable"
    tolerations:
      - key: "dedicated"
        operator: "Equal"
        value: "runnable"
        effect: "NoSchedule"
```

</details>

## query-default

### **For Query Workloads**

```yaml
compute:
  dataplane: hub
  purpose: query
  nodePool:
    nodeSelector:
      {{"dataos.io/purpose": "query"}}
    tolerations:
      - key: {{"dedicated"}}
        operator: {{"Equal"}}
        value: {{"query"}}
        effect: {{"NoSchedule"}}
```

<details>
<summary> 
Sample query-default Compute YAML</summary>

```yaml
# Resource Section
name: "query-default"
version: v1
type: compute
layer: system
description: "default query compute"
# Compute-specific Section (for query)
compute:
  dataplane: hub
  purpose: query
  nodePool:
    nodeSelector:
      "dataos.io/purpose": "query"
    tolerations:
      - key: "dedicated"
        operator: "Equal"
        value: "query"
        effect: "NoSchedule"
```

</details>

## gpu template

### **For Machine Learning Workloads**

```yaml
compute:
  dataplane: {{hub}}
  purpose: gpu
  nodePool:
    nodeSelector:
      ${"dataos.io/purpose": "gpu"}
    tolerations:
      - key: {{"dedicated"}}
        operator: {{"Equal"}}
        value: {{"gpu"}}
        effect: {{"NoSchedule"}}
```

<details>
<summary> 
Sample query-default Compute YAML</summary>

```yaml
# Resource Section
name: gpu
version: v1
type: compute
layer: system
description: gpu compute for jobs
# Compute-specific Section (for gpu)
compute:
  dataplane: hub
  purpose: gpu
  nodePool:
    nodeSelector:
      "dataos.io/purpose": "gpu"
    tolerations:
      - key: "dedicated"
        operator: "Equal"
        value: "gpu"
        effect: "NoSchedule"
```

</details>