# Compute

In the DataOS ecosystem, a Compute is a Primitive/Resource that defines the processing power required for any data processing or query workloads. It allows for the creation of a node pool, which is a group of virtual machines (VMs) with similar configurations, and makes them available to DataOS as a compute resource, addressable via a specific name. By defining a Compute, it eliminates the need to individually define the virtual machines to be provisioned. 

<center>

![Diagrammatic representation of a Compute](./DataOS_PrimitiveResource_which_is_a_Node_Pool_known_to_DataOS_and_addressable_via_a_specific_name_(Here_its_name_is_query-default)_(1).svg)

</center>

<figcaption align = "center">Diagrammatic representation of a Compute</figcaption>
<br>

During the setup of DataOS, a Compute is one of the first resources created as it acts as the foundation for all other resources. A Compute is simply processing power without any specific application identity associated with it. At its core, a Compute consists of basic server components such as CPUs and RAM (or VMs). It can be a node pool of Amazon EC2, Azure VM, Google Cloud Instances, or any other cloud provider. These can then be referred to as a Compute and referenced in Clusters for querying data or executing Workflows/Services within DataOS.

> 🗣️ Creating a `compute` requires setting up node pools, which is a task that can only be performed by the system administrator within the organization.

## Types of Compute

When configuring DataOS, two types of Computes are automatically provisioned by default: the `runnable-default` Compute on which data processing workloads such as Workflows/Services operate, and the `query-default` Compute, which supports Minerva Clusters.

## Create Compute

DataOS supports creating your own Compute for varied data processing/query workloads. To define a Compute in DataOS, follow the three steps process given below:

### Step 1: Provision Virtual Machines (VMs)

DataOS uses Kubernetes for cluster and container management. It supports creating/defining groups of VMs (node pools) that have a particular profile - A specific CPU, memory, and disk capacity. To get started with creating a Compute resource, you first need to provision a group of VMs and register those with Kubernetes.

> 🗣️ Please get in touch with the administrator in your organization to create a node pool.

### Step 2: Registering Compute in DataOS

Once the node pool is created, you can register them with the DataOS. You need to associate the group of VMs (Node Pool) with your compute structure. 

#### Default Compute

For default compute, you can create a YAML configuration with the given properties in the below format:

```yaml
- name: configure-dataos-resources-system # Name
    values: # Value
      install_and_upgrade: # Install and Upgrade 

# Both default Computes can be declared within the same YAML

# runnable-default compute for data processing workloads such as workflows/services
        - version: v1beta1 # Manifest Version
					name: "runnable-default"  # Name of the Compute      
          type: compute # Resource Type (Here its compute)
          layer: system # System Layer 
          description: "default runnable compute" # Description of the Compute 
          compute: # Compute Properties
            type: K8SNodePoolLocal # Type
            defaultFor: runnable # Default the Node Pool for Runnable
            nodePool: # Node Pool Properties
              nodeSelector: # Node Selector
                "dataos.io/purpose": "runnable" # Node Selection for runnable purpose
              tolerations: # Tolerations
                - key: "dedicated" # Keys
                  operator: "Equal" # Operator
                  value: "runnable" # Value
                  effect: "NoSchedule" # Effect

# query-default compute for query processing
        - version: v1beta1 # Manifest Version
					name: "query-default" # Name of the Compute    
          type: compute # Resource Type (Here it's compute)
          layer: system # System Layer
          description: "default query compute" # Description of the Compute
          compute: # Compute Properties
            type: K8SNodePoolLocal # Type
            defaultFor: query # Default the Nodepool for
            nodePool: # Nodepool Properties
              nodeSelector: # Nodeselector
                "dataos.io/purpose": "query" # Node Selection for query purpose
              tolerations: # Tolerations
                - key: "dedicated" # Key
                  operator: "Equal" # Operator
                  value: "query" # Value
                  effect: "NoSchedule" # Effect
```

#### Custom Compute

To create a custom compute, you can use the YAML syntax below. The properties and their descriptions of the YAML are tabulated at the end of the page:

```yaml
name: "query-default01" # Name of the custom compute
version: v1beta1 # Manifest Version
type: compute # Resource Type (Here it's compute)
layer: system # Layer
description: "default myquery compute" # Description of the Compute
compute: # Compute Properties
  type: K8SNodePoolLocal # Node pool type
  defaultFor: myquery # Default for myquery
  nodePool: # Node pool properties
    nodeSelector: # Node Selector Properties
      "cloud.google.com/gke-nodepool": "myquery" # Google Cloud Node Pool Configurations
    tolerations: # Tolerations
      - key: "dedicated" # Key
        operator: "Equal" # Operator
        value: "query" # Value
        effect: "NoSchedule" # Effect
```

### Step 3: Apply the YAML to create a Compute resource

After creating the YAML for compute, you can use the `apply` command to create a compute resource in the DataOS environment

```bash
dataos-ctl apply -f <path/file-name>
```

Once you have created a compute resource, you can refer to it in Clusters for data processing (workflow/services) and query workloads by its name.

### Step 4: Check available Compute within DataOS

You can use the CLI to get all the available compute within the DataOS. Execute the below command

```bash
dataos-ctl -t compute get -a

# Expected Output
INFO[0000] 🔍 get...                                     
INFO[0000] 🔍 get...complete                             

        NAME       | VERSION |  TYPE   | WORKSPACE | STATUS | RUNTIME |     OWNER       
-------------------|---------|---------|-----------|--------|---------|-----------------
  query-default    | v1beta  | compute |           | active |         | dataos-manager  
  runnable-default | v1beta  | compute |           | active |         | dataos-manager
```

## Building Blocks of Compute

| Property | Description | Example | Default Value | Possible Value | Rules/ Additional Details | Field (Optional / Mandatory) |
| --- | --- | --- | --- | --- | --- | --- |
| `name` | Defines the name of the resource (Here its compute) | `name: query-default` | `runnable-default` , `query-default` | Any string that conforms to the rule given in the next cell. | Rules for name: 37 alphanumeric characters and a special character '-' allowed. `[a-z0-9]([-a-z0-9]*[a-z0-9])`. The maximum permissible length for the name is 47, as showcased on CLI. Still, it's advised to keep the name length less than 30 characters because Kubernetes appends a Unique ID in the `name`, which is usually 17 characters. Hence reduce the name length to 30, or your workflow will fail. | Mandatory |
| `version` | Version allows iteration on the schema.  | `version: v1`  | NA | `v1` | Configure all the properties according to the manifest version. Currently, it's `v1`. | Mandatory |
| `type` | Resource type is declared here. In the current case, it's compute. | `type: compute` | NA | Any of the available resources in DataOS | The name of the primitive/resource should be only in lowercase characters. Else it will throw an error. | Mandatory |
| `layer` | Represents the layer of Kubernetes. | `layer: system` | NA | `system` |  | Mandatory |
| `description` | Text describing the Compute. | `description: default query compute` | NA | Any string | There is no limit on the length of the string | Optional |
| `tags` | Tags are arrays of strings. These are attributes and keywords. They are used in access control and for quick searches within Metis. | `tags:` <br> &nbsp;&nbsp;&nbsp;&nbsp;`- Connect` <br> &nbsp;&nbsp;&nbsp;&nbsp;`- Customer` | NA | NA | The tags are case-sensitive, so `Compute` and `COMPUTE` will be different tags. There is no limit on the length of the `tag`.  | Optional |
| `compute` | Section for declaring the compute properties. | `compute:` <br> &nbsp;&nbsp;&nbsp;&nbsp;`{}` | NA | NA | NA | Mandatory |
| `type` | Here we describe the node pool type. | `type: K8SNodePoolLocal` | NA | `K8SNodePoolLocal` | NA | Mandatory |
| `defaultFor` | Make the compute default for | `defaultFor: query` | NA | `query`/`runnable` or any string | NA | Mandatory |
| `nodePool` | Nodepool specific properties | `nodepool:` <br> &nbsp;&nbsp;&nbsp;&nbsp;`{}` | NA | NA | NA | Mandatory |
| `nodeSelector` | To specify the node labels desired for the target node, the `nodeSelector` property can be added to the Pod specification. Kubernetes will only schedule the Pod onto nodes that possess each of the labels specified. This method of node selection constraint is the simplest form recommended by Kubernetes. | `nodeSelector:` <br> `"dataos.io/purpose": "query"` | NA | `nodeSelector:` <br> &nbsp;&nbsp;&nbsp;&nbsp;`"dataos.io/purpose": "query"`/ <br> &nbsp;&nbsp;&nbsp;&nbsp;`"dataos.io`/`purpose": "runnable"` | NA | Mandatory |
| `tolerations` | Taints and tolerations help prevent your pods from scheduling to undesirable nodes. Taints are properties of nodes that repel pods. To schedule certain pods on tainted nodes, add tolerations to the pods and specify the `key`, `operator`, `value`, and `effect` properties within them. Apply one or more taints to a node, like labels. The node will not accept pods that do not tolerate all the taints on that node. | `tolerations:` <br> &nbsp;&nbsp;&nbsp;`- key: “dedicated"` <br> &nbsp;&nbsp;&nbsp;&nbsp;`operator: “Equal”` <br> &nbsp;&nbsp;&nbsp;&nbsp;`value: “query”`<br> &nbsp;&nbsp;&nbsp;&nbsp;`effect: “NoSchedule”` | `tolerations:` <br> &nbsp;&nbsp;&nbsp;`- key: NA` <br> &nbsp;&nbsp;&nbsp;&nbsp;`operator: “Equal”` <br> &nbsp;&nbsp;&nbsp;&nbsp;`value: “query”` <br> &nbsp;&nbsp;&nbsp;&nbsp;`effect: NA` | `tolerations:` <br> &nbsp;&nbsp;&nbsp;`- key: Any string` <br> &nbsp;&nbsp;&nbsp;&nbsp;`operator: "Equal"`/`"Exists"` <br> &nbsp;&nbsp;&nbsp;&nbsp;`value: “query”`/`"runnable"` <br> &nbsp;&nbsp;&nbsp;&nbsp;`effect: NoSchedule`/ <br> `PreferNoSchedule`/ <br> `NoExecute` | `key`: The key is any string up to 253 characters. It must begin with a letter or a number and may contain letters, numbers, hyphens, dots, and underscores. <br/><br/> `value`: The value is any string up to 63 characters. The value must begin with a letter or number and may contain letters, numbers, hyphens, dots, and underscores. <br/><br/> `effect`: The effect is one of the following: <br> -` NoSchedule`: New pods that don’t match the taint are not scheduled on that node, and existing pods on the node remain. <br> -` PreferNoSchedule`: New pods that do not match the taint might be scheduled onto that node, but the scheduler tries not to, and existing pods on the node remain. <br> -` NoExecute`: New pods that do not match the taint cannot be scheduled onto that node; existing pods on the node that do not have a matching toleration are removed. <br/><br/> `operator`: The following two operators are there <br> -` Equal`: The key/value/effect parameters must match. This is the default. <br> -` Exists`: The key/effect parameters must match. You must leave a blank value parameter that matches any. | Mandatory |