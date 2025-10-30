# K8 Cluster Infrastructure Dashboard

<aside class="callout">
ℹ️

This document provides insights for interpreting and responding to the metrics shown in the Kubernetes Cluster Infrastructure Dashboard, hosted via Grafana within DataOS. While the dashboard provides powerful visualization, this documentation adds value by translating visual data into operational understanding, diagnostic workflows, and strategic decisions.

<br><b>Intended Audience:</b> Site Reliability Engineers (SREs), Kubernetes Administrators, Platform Engineers, and Data Product Developers responsible for sustaining infrastructure reliability, cluster efficiency, and service uptime.

</aside>

## Overview

The Kubernetes Cluster Infrastructure Dashboard provides a unified observability layer for monitoring health, performance, capacity, and operational bottlenecks within a DataOS-managed Kubernetes cluster. The dashboard is organized into seven sections, which are described one by one in the sections below: 

![image.png](K8%20Cluster%20Infrastructure%20Dashboard/b7258376-0626-418f-b9f6-f92c1568c5f0.png)

- Kubernetes Cluster Overview
- API Server
- Networking
- Storage
- Certificates
- Workloads
- Secrets

## Explore metrics

Users can explore the Prometheus query used to power the metrics visualized in the dashboard. To do so, follow the steps below.

1. Hover over any graph that you want to explore.
    
    ![image.png](K8%20Cluster%20Infrastructure%20Dashboard/image.png)
    
2. Click on the three-dot menu, then click on the ‘Explore’ option.
    
    ![image.png](K8%20Cluster%20Infrastructure%20Dashboard/image%201.png)
    
3. On clicking the ‘Explore’ option, an explore interface will open, where you can see the query used to derive those metrics, as shown below.
    
    ![image.png](K8%20Cluster%20Infrastructure%20Dashboard/image%202.png)
    

## Kubernetes Cluster Overview

This section provides an overview of the Kubernetes cluster's topology and health at a high level. Understanding the cluster’s composition and its readiness is essential for validating environment setup, onboarding applications, and pre-scaling planning.

![image.png](K8%20Cluster%20Infrastructure%20Dashboard/image%203.png)

### **Key Metrics**

#### Total Nodes

Indicates the number of worker nodes that are part of the Cluster in which the DataOS environment is running. Useful for capacity estimation and node-level troubleshooting. This metric is derived from the following query:

```bash
count by(origin_prometheus)(kube_node_info{origin_prometheus=~".*"})
```

It counts the number of unique nodes that are part of the Kubernetes cluster. `kube_node_info` contains metadata about each node. The count by(...) function groups data by the `origin_prometheus` label and counts the number of nodes found. 

#### Namespaces

Logical boundaries for organizing workloads. A high number may indicate strong tenant isolation or over-segmentation. This metric is derived from the following query:

```bash
count(kube_namespace_created)
```

This query uses the `kube_namespace_created` metric, which captures the creation timestamp of each namespace. The `count()` function calculates how many distinct namespace records exist, thus reflecting the total number of namespaces in the cluster. 

<aside class="callout">
ℹ️

In Kubernetes, namespaces provide a mechanism for isolating groups of resources within a single cluster. Names of resources need to be unique within a namespace, but not across namespaces. Namespace-based scoping is applicable only for namespaced objects (e.g., Deployments, Services, etc.) and not for cluster-wide objects (e.g., StorageClass, Nodes, PersistentVolumes, etc.).

</aside>

#### No Taint Nodes

This metric determines how many nodes in the cluster are not tainted and are therefore generally available for scheduling all kinds of workloads. Untainted nodes are considered open and schedulable unless constrained by other affinity rules

```bash
by(origin_prometheus)(kube_node_info{origin_prometheus=~".*"})
-
count by(origin_prometheus)(kube_node_spec_taint{origin_prometheus=~".*", key=~"node.kubernetes.io/.*"})
```

This subtracts the number of tainted nodes from the total number of nodes. The first part counts all nodes using `kube_node_info`. The second part counts nodes that have taints applied using the `kube_node_spec_taint` metric. The difference gives the number of nodes without taints, i.e., available for general-purpose workloads.

#### Taint: Dedicated Nodes

This metric counts nodes that have specific taints applied using the key prefix `node.kubernetes.io/`, which is often used to isolate workloads on dedicated infrastructure.

```bash
count by(key, origin_prometheus)(kube_node_spec_taint{origin_prometheus=~".*", key=~"node.kubernetes.io/.*"})
```

Here, `kube_node_spec_taint` lists taints applied to nodes. The query filters taints whose `key` matches the common Kubernetes taint pattern and groups them by `key` and `origin_prometheus`. This count reflects how many taint groups are applied, which helps identify nodes reserved for specialized use cases like GPU jobs or system-critical workloads.

#### Total Pods

This metric shows the number of pods currently present in the cluster. It helps assess workload density and identify trends such as pod churn or autoscaling activity.

```bash
count(kube_pod_info{origin_prometheus=~".*"})
```

The `kube_pod_info` metric provides metadata about each pod, such as name, namespace, and node association. The `count()` function simply returns how many pod entries exist. This includes all phases pending, running, failed, etc.

#### PVCs (Persistent Volume Claims)

This metric provides the total number of Persistent Volume Claims, which represent requests for storage resources by workloads. PVCs are essential for Resources such as Lakesearch Stack, Flash Stack, etc.

```bash
count(kube_persistentvolumeclaim_info)
```

The metric `kube_persistentvolumeclaim_info` lists PVCs across namespaces. By applying `count()`, this query tallies the number of storage volumes requested. This number is useful for tracking the footprint of storage-backed Resources.

#### Total Workloads

This metric aggregates all types of workload controllers such as Deployments, DaemonSets, StatefulSets, and ReplicaSets. It reflects the scale and design of the cluster's workload topology.

```bash
count({__name__=~"kube_deployment_metadata_generation|kube_daemonset_metadata_generation|kube_statefulset_metadata_generation|kube_replicaset_metadata_generation",origin_prometheus=~".*"})
```

Each of these `*_metadata_generation` metrics reports the current generation of a workload controller, meaning how many times the configuration has been updated. Counting these across all types gives a combined view of all workload definitions present in the cluster.

### **Cluster Health**

![image.png](K8%20Cluster%20Infrastructure%20Dashboard/image%203.png)

#### ENV Status

“UP” implies the cluster is responding to health checks. Indicates whether the API Server, Scheduler, or Controller manager is down. 

```bash
min(up{job=~"apiserver"})
```

The `up` metric returns `1` for a reachable target and `0` otherwise. Using the `min()` function ensures that if any API server instance is down, the entire metric reflects it. This is vital for monitoring the health of the Kubernetes API layer.

#### Kubernetes Versions

This panel shows the current Kubernetes version of the selected cluster.

```bash
count by(kubelet_version)(kube_node_info)
```

The `kube_node_info` metric provides metadata about each node, including its Kubelet version. Grouping by `kubelet_version` and counting allows the user to see how many nodes are running each version. It's useful for managing upgrade rollouts and ensuring compatibility across the cluster.

#### Node Health

**Healthy Nodes**

This metric provides the number of worker nodes that are currently schedulable, meaning they are available to host pods.

```bash
count(kube_node_spec_unschedulable==0)
```

`kube_node_spec_unschedulable` returns `0` for nodes that are not cordoned. Counting only those with a value of `0` yields the total number of healthy, active nodes. This is critical for capacity planning and detecting resource availability issues.

**Unhealthy Nodes**

This metric determines the number of Kubernetes nodes that are unschedulable, typically due to manual cordoning (e.g., for maintenance) or automatic exclusion from scheduling by the control plane. An "unschedulable" node does not accept new pods, which can affect workload distribution and scalability.

```bash
count(kube_node_spec_unschedulable!=0) OR on() vector(0)
```

The query checks for all nodes where the field `kube_node_spec_unschedulable` is not equal to `0`, indicating that those nodes have been marked unschedulable. The use of `count(...)` ensures we aggregate the total number of such nodes across the cluster. The `OR on() vector(0)` clause ensures that the expression always returns a numerical result, even if no unscheduled nodes exist, by defaulting the output to `0`. 

**Unschedulable Nodes**

This metric represents the total number of nodes in a Kubernetes cluster that are marked as unschedulable, meaning they are not eligible to run new pods. Nodes can become unschedulable due to administrative actions, automated maintenance policies, or resource exhaustion.

```bash
sum(kube_node_spec_unschedulable)
```

The expression `sum(kube_node_spec_unschedulable)` adds up all instances where nodes have been flagged as unschedulable (`true`). Each unschedulable node contributes a `1` to the sum, while schedulable nodes contribute `0`. The resulting value gives a total count of nodes currently excluded from scheduling decisions by the Kubernetes control plane.

**NotReady Nodes**

This metric identifies nodes that are not in a `Ready` state, indicating that they may be unreachable or experiencing issues.

```bash
sum(kube_node_status_condition{condition="Ready", status!="true"})
```

The `kube_node_status_condition` metric reflects the health status of each node. Filtering for the `Ready` condition and excluding `true` status captures nodes in `False` or `Unknown` state. Summing across all such conditions gives a clear count of problematic nodes.

<aside class="callout">
💡

<b>Best Practice:</b> Set up alerts for node status changes and use `kubectl describe node <node-name>` for root cause analysis.

</aside>

### **CPU Metrics**

![image.png](K8%20Cluster%20Infrastructure%20Dashboard/image%203.png)

#### Global CPU Usage

This metric shows the percentage of total CPU being used across all running containers in the cluster.

```bash
sum(rate(container_cpu_usage_seconds_total{container_name!="POD", image!=""}[5m])) / sum(machine_cpu_cores) * 10
```

The numerator sums the rate of CPU usage (per second) over the past 5 minutes for all non-pause containers. The denominator sums the total CPU cores available in the cluster. This gives a normalized CPU utilization percentage at the cluster level.

#### Node CPU Pressure

In Kubernetes, Node CPU Pressure is a condition that indicates the node is under significant CPU stress. It means the node does not have enough available CPU cycles to keep up with all the running workloads. 

```bash
sum(kube_node_status_condition{condition="PIDPressure", status!="false"})
```

The `PIDPressure` condition reflects whether the node is constrained on PID allocations (indirectly indicating CPU and process stress). A non-zero value here implies that nodes may throttle or reject pods due to resource exhaustion.

<aside class="callout">
⚠️

<b>Typical Pitfall:</b> Forgetting to set limits can allow runaway CPU usage.

</aside>

#### Global CPU Requests and Limits

This metric visualizes CPU resource guarantees and constraints in percentage terms across the cluster. It consists of three parts:

- **Real**: Represents the actual usage over time
- **Requests**: Minimum guaranteed CPU allocated
- **Limits**: Maximum allowed CPU usage

Each is calculated as a ratio of total CPU resources.

```bash
Actual: sum(rate(container_cpu_usage_seconds_total{container_name!="POD", image!=""}[5m])) / sum(machine_cpu_cores) * 100
Requests: sum(kube_pod_container_resource_requests{unit="core"}) / sum(machine_cpu_cores) * 100
Limits: sum(kube_pod_container_resource_limits{unit="core"}) / sum(machine_cpu_cores) * 100
```

This helps evaluate overcommitment or underutilization across workloads.

#### Global CPU Core Requests and Limits

This panel displays the absolute values (in CPU cores) associated with workload scheduling and enforcement:

- **Real**: Current CPU usage across all nodes
- **Requests**: Total CPU cores requested
- **Limits**: Maximum CPU cores allowed
- **Total**: Cluster capacity baseline

```
Real: sum(rate(container_cpu_usage_seconds_total[5m]))
Requests: sum(kube_pod_container_resource_requests{unit="core"})
Limits: sum(kube_pod_container_resource_limits{unit="core"})
Total: sum(machine_cpu_cores)
```

### **Memory Metrics**

![image.png](K8%20Cluster%20Infrastructure%20Dashboard/image%203.png)

#### Global Memory Requests and Limits

This metric compares total memory requests and limits to cluster allocatable memory:

**Queries:**

```
Requests: sum(kube_pod_container_resource_requests{unit="byte"}) / sum(machine_memory_bytes) * 100
Limits: sum(kube_pod_container_resource_limits{unit="byte"}) / sum(machine_memory_bytes) * 100
```

This view provides clarity on how much of the cluster memory is committed versus constrained.

#### obal Memory Usa

This metric displays the percentage of physical memory consumed across the cluster.

![image.png](K8%20Cluster%20Infrastructure%20Dashboard/image%204.png)

```bash
sum(container_memory_working_set_bytes{container_name!="POD", image!=""}) / sum(machine_memory_bytes) * 100
```

The `working_set_bytes` includes resident memory used by containers, excluding cache. Dividing by the total allocatable memory across nodes gives the memory usage percentage cluster-wide.

#### Node Memory Pressure

This metric identifies whether any node is experiencing memory pressure, which could result in pods being evicted. A value of `1` indicates that at least one node is under memory stress. The Prometheus query for this metric is:

```
sum(kube_node_status_condition{condition="MemoryPressure", status!="false"})
```

It sums all nodes where the condition `MemoryPressure` is active (not `false`). This is critical for the early detection of memory saturation issues that could impact workload stability.

### **Disk Metrics**

![image.png](K8%20Cluster%20Infrastructure%20Dashboard/image%203.png)

#### Global Disk Usage (%)

This metric shows the percentage of total disk space used across the cluster:

```
sum(container_fs_usage_bytes{device=~"^/dev/.*$",id="/"}) / sum(container_fs_limit_bytes{device=~"^/dev/.*$",id="/"}) * 100
```

It helps detect storage saturation, which can lead to failed writes or node instability.

#### Global Disk Usage

This panel displays the absolute values for disk space usage and capacity in the cluster.

- **Used:** This is the actual amount of disk space consumed across all nodes.
- **Total:** This is the total allocatable or mounted disk space available for workloads and system components across all nodes.

### **Pod Status Summary**

This section helps operationalize workload readiness, triage failures, and manage application health.

![image.png](K8%20Cluster%20Infrastructure%20Dashboard/image%205.png)

- **Pods Running**: Pods in `Running` phase
    
    ```
    sum(kube_pod_status_phase{phase="Running"})
    ```
    
    This Prometheus query uses the `sum()` aggregator to count all pods where `kube_pod_status_phase` has `phase="Running"`, giving us the total number of actively running pods across the entire Kubernetes cluster. The metric `kube_pod_status_phase` tracks pod lifecycle states, and filtering for the Running phase specifically captures pods that have been successfully scheduled and have at least one active container.
    
- **Pods Succeeded**: Successfully completed pods.
    
    ```
    sum(kube_pod_status_phase{phase="Succeeded"})
    ```
    
    This query aggregates the total count of pods that have completed their execution successfully. It uses the `kube_pod_status_phase` metric and filters for pods in the "Succeeded" phase, then applies the `sum()` function to get the total count across the cluster. This metric is particularly useful for monitoring batch jobs and one-time tasks that are expected to complete rather than run continuously.
    
- **Pods Pending**: Awaiting scheduling
    
    ```
    sum(kube_pod_status_phase{phase="Pending"})
    ```
    
    This Prometheus query sums up all pods in the "Pending" phase across the Kubernetes cluster. It uses the `kube_pod_status_phase` metric with a filter for `phase="Pending"` to count pods that have been accepted by the control plane but haven't been scheduled to any node yet. This typically happens due to resource constraints, node affinity rules, or volume claim issues.
    
- **Pods Failed**: Pods terminated with errors
    
    ```
    sum(kube_pod_status_phase{phase="Failed"})
    ```
    
    This Prometheus query uses the `sum()` aggregator to count all pods that have terminated with errors (phase="Failed") across the Kubernetes cluster. A pod enters the `Failed` state when it terminates unsuccessfully, which can happen due to container crashes, OOM kills, failed probes, or when pods are evicted due to node pressure.
    
- **Pods Unknown**: State not determined
    
    ```
    sum(kube_pod_status_phase{phase="Unknown"})
    ```
    
    This Prometheus query uses the `sum()` aggregator to count all pods where `kube_pod_status_phase` has `phase="Unknown"`, providing a total count of pods whose state cannot be determined by the Kubernetes control plane. This typically happens when there are communication issues between the control plane and nodes.
    
- **Pods in ErrImagePull:** A metric that counts the number of pods that are in a failed state due to container image pull errors.
    
    ```
    count(kube_pod_container_status_waiting_reason{reason="ErrImagePull"}
    ```
    
    This Prometheus query counts the number of pods that are in a waiting state, specifically due to image pull errors. It uses the metric `kube_pod_container_status_waiting_reason` and filters for instances where the `reason` label equals "ErrImagePull", which indicates that Kubernetes was unable to pull the container image. This helps identify deployment issues related to invalid image references, registry authentication problems, or network connectivity issues.
    
- **Pods OOM Killed:** This metric tracks the number of pods that were terminated because they exceeded their memory limits (Out of Memory Killed).
    
    ```
    count(kube_pod_container_status_terminated_reason{reason="OOMKilled"})
    ```
    
    This Prometheus query counts the number of pods that were terminated due to Out-of-Memory (OOM) conditions. It uses the metric `kube_pod_container_status_terminated_reason` and filters for instances where the `reason` equals "OOMKilled", indicating that Kubernetes terminated the pod because it exceeded its memory limits. 
    
- **Pods in CrashLoopBackOff:** A Pod in CrashLoopBackOff status indicates that a container is repeatedly starting, crashing, and restarting in a continuous cycle.
    
    ```
    count(kube_pod_container_status_waiting_reason{reason="CrashLoopBackOff"})
    ```
    
    This Prometheus query counts the number of pods that are currently in a `CrashLoopBackOff` state. It uses the metric `'kube_pod_container_status_waiting_reason'` and filters for instances where the 'reason' equals `"CrashLoopBackOff"`. This status indicates that containers within pods are repeatedly crashing and restarting in a continuous cycle.
    
- **Pods in ImagePullBackOff:** Pods with Failed Container Image Downloads
    
    ```
    count(kube_pod_container_status_waiting_reason{reason=~"ImagePullBackOff|ErrImagePull"})
    ```
    
    This Prometheus query counts the total number of pods that are in a waiting state due to either `ImagePullBackOff` or `ErrImagePull` errors. It uses the metric `kube_pod_container_status_waiting_reason` and filters for both error types using a regular expression pattern match (=~). This helps identify pods that are failing to start because of container image download issues, which could be due to invalid image references, registry authentication problems, or network connectivity issues.
    

### **Namespace Distribution**

The ‘Running Pods by Namespace’ metric presents a breakdown of all active pods currently in the `Running` phase, grouped by Kubernetes namespace. Each segment of the chart represents the number of running pods within a specific namespace, reflecting how compute workloads are distributed.

![image.png](K8%20Cluster%20Infrastructure%20Dashboard/image%206.png)

```bash
count by(namespace) (
rate(kube_pod_container_status_running{namespace=~".*"}[$__rate_interval])
)
```

This query calculates the rate of running containers per namespace in Kubernetes. It uses the `'rate'` function to measure the change in running container status over a time interval (defined by `$__rate_interval`), then groups these rates by namespace using `'count by(namespace)'`. The regex pattern `'.*'` matches all namespaces, providing a comprehensive view of pod distribution across the cluster.

## API Server Insights

This component ensures that the API server, the control plane’s central hub, is responsive, performant, and error-free.

![image.png](K8%20Cluster%20Infrastructure%20Dashboard/image%207.png)

![image.png](K8%20Cluster%20Infrastructure%20Dashboard/image%208.png)

### **Health Status**

Health Status indicates whether the Kubernetes API server is currently operational and reachable. A status of UP confirms that the API server's health endpoints are responding successfully, meaning the control plane is live and functional.

### **API Server – Read Success Rate**

Read Success Rate shows the percentage of successful read-only API operations (e.g., `GET`, `LIST`, `WATCH`) processed by the API server within the observed interval. A high value (e.g., 99.6%) suggests consistent, reliable reads from the cluster's data store and control plane.

```bash
sum(irate(apiserver_request_total{code=~"20.*",verb=~"GET|LIST"}[5m]))/sum(irate(apiserver_request_total{verb=~"GET|LIST"}[5m]))
```

### **API Server – Write Success Rate**

Write Success Rate represents the percentage of successful write operations (e.g., `POST`, `PUT`, `PATCH`, `DELETE`) processed by the API server. A lower value (e.g., 95.8%) compared to read success may indicate failed mutation requests, often due to validation errors, authorization issues, or webhook rejections.

```bash
sum(irate(apiserver_request_total{code=~"20.*",verb!~"GET|LIST|WATCH|CONNECT"}[5m]))/sum(irate(apiserver_request_total{verb!~"GET|LIST|WATCH|CONNECT"}[5m]))
```

This Prometheus query calculates the API server's write success rate by dividing successful write operations (those with HTTP 200-series response codes) by the total number of write operations. It identifies write operations by excluding read verbs (GET, LIST, WATCH, CONNECT) and uses the irate() function to measure the per-second instantaneous rate over the last 5 minutes. A lower success rate (compared to read operations) may indicate validation errors, authorization issues, or webhook rejections that are preventing successful resource mutations in the Kubernetes cluster.

### **API Server – CPU Usage in CPU Seconds**

CPU Usage in CPU Seconds displays the total CPU time consumed by the API server, sampled over time. This is a measure of the compute load on the API server pods, influenced by control plane activity such as high pod churn, watch requests, or configuration reloads.

```bash
rate(process_cpu_seconds_total{job=~"kubernetes-apiservers|apiserver"}[1m])
```

This Prometheus query calculates the per-second CPU usage rate of the Kubernetes API server over a 1-minute window. It uses the `rate()` function on the `process_cpu_seconds_total` metric, filtering for jobs matching either the "kubernetes-apiservers" or "apiserver" pattern. The result shows how many CPU seconds are being consumed by the API server processes, which helps monitor control plane resource utilization and identify performance bottlenecks or scaling needs.

### **API Server – HTTP Request Latency by Instance**

HTTP Request Latency by Instance shows the response time of API server requests, broken down by individual API server pods or nodes. This metric helps isolate performance degradation at the replica level, useful in multi-master clusters.

```bash
sum(rate(apiserver_request_duration_seconds_sum{job=~"kubernetes-apiservers|apiserver"}[1m])) by (instance)
/
sum(rate(apiserver_request_duration_seconds_count{job=~"kubernetes-apiservers|apiserver"}[1m])) by (instance)
```

This Prometheus query calculates the average request latency for the Kubernetes API server by instance. It divides the sum of request duration in seconds by the count of requests, grouped by instance. The query uses the rate function over a 1-minute window to measure the per-second rate of change for both duration sum and request count metrics, filtering for jobs matching either "kubernetes-apiservers" or "apiserver". This provides visibility into how each API server instance is performing, helping to identify specific instances that might be experiencing latency issues or performance degradation.

### **API Server – Errors by Instance**

Errors by Instance counts the number of failed HTTP API requests handled by each API server instance. Failures include client-side issues (`4xx`) and server-side errors (`5xx`). A spike here indicates misconfigured clients, webhook issues, or degraded API responsiveness.

```bash
sum by(instance) (rate(apiserver_request_total{code=~"5..", job=~"kubernetes-apiservers|apiserver"}[1m]))
```

This Prometheus query calculates the rate of HTTP 5xx server errors per second from the Kubernetes API server, grouped by instance. It uses the rate() function to measure the change over a 1-minute interval, filters for error codes starting with "5" (server-side errors), and includes jobs matching either "kubernetes-apiservers" or "apiserver" patterns. The query helps identify which specific API server instances are experiencing internal failures, making it easier to troubleshoot stability issues in the control plane.

### **API Server – HTTP Request Latency by Verb**

HTTP Request Latency by Verb measures average API latency, categorized by HTTP verb (e.g., `GET`, `LIST`, `POST`, `WATCH`). It helps identify specific types of requests (e.g., `WATCH`) that are taking longer to process, often due to resource size, controller pressure, or API complexity.

```bash
sum(rate(apiserver_request_duration_seconds_sum{job=~"kubernetes-apiservers|apiserver"}[1m])) by (verb)
/
sum(rate(apiserver_request_duration_seconds_count{job=~"kubernetes-apiservers|apiserver"}[1m])) by (verb)
```

This Prometheus query calculates the average HTTP request latency for the Kubernetes API server, broken down by HTTP verb (GET, LIST, POST, etc.). It divides the sum of request duration seconds by the count of requests, grouped by verb, using the rate function over a 1-minute window to measure the per-second change. The query filters for jobs matching either "kubernetes-apiservers" or "apiserver" patterns. This provides visibility into which types of API operations are experiencing latency issues, helping to identify performance bottlenecks in specific request categories.

### **API Server – CONNECT Error Count by HTTP Code (Non-2xx)**

CONNECT Error Count by HTTP Code shows the volume of failed API requests returning non-2xx status codes, such as:

```bash
sum by (code) (increase(apiserver_request_total{verb="CONNECT", subresource="proxy", component="apiserver", endpoint="https", code!~"2.."}[1m0s]))
```

This Prometheus query calculates the number of failed CONNECT requests to the Kubernetes API server over a 1-minute interval, grouped by HTTP response code. It specifically filters for requests with the CONNECT verb targeting the proxy subresource of the apiserver component over HTTPS endpoints, and only counts responses with non-2xx status codes (indicating errors). The query uses the `increase()` function to measure the absolute change in error count over the interval, then aggregates results by error code using `sum by (code)`, providing visibility into different types of proxy connection failures.

- `403 Forbidden`: RBAC/authorization failures
- `503 Service Unavailable`: API server overload or readiness failure

This metric highlights API access or availability issues and helps detect infrastructure or permission-related disruptions.

### **Slowest Requests (Top 10)**

![image.png](K8%20Cluster%20Infrastructure%20Dashboard/image%209.png)

Slowest Requests (Top 10) lists the API operations with the highest observed latency, ranked by response time.

```bash
topk(10, cluster_quantile:apiserver_request_duration_seconds:histogram_quantile{job=~".+",quantile="0.9", subresource=""})
```

This Prometheus query uses the `topk(10)` function to identify and display the 10 API requests with the highest latency in the Kubernetes cluster. It specifically examines the 90th percentile (`quantile="0.9"`) of request duration times, meaning these are requests that are consistently slow for most users. The query filters for API requests that don't target specific subresources (`subresource=""`) and includes all jobs (using the regex pattern `job=~".+"`) in the cluster. This metric is particularly useful for identifying performance bottlenecks in the Kubernetes API server and prioritizing optimization efforts for the slowest API operations.

## Networking Metrics

Evaluate network health from pod ingress/egress, DNS resolution, and service routing.

![image.png](K8%20Cluster%20Infrastructure%20Dashboard/image%2010.png)

### **Check Average Image Pull Duration**

![image.png](K8%20Cluster%20Infrastructure%20Dashboard/image%2011.png)

This panel presents the average time taken to pull container images across the cluster, segmented by image size buckets:

- `0–10MB`
- `10MB–100MB`
- `100MB–500MB`
- `500MB–1GB`
- `1GB–5GB`
- `5GB–10GB`

This data helps visualize how long it takes to download container images of different sizes during pod initialization. A prolonged image pull time increases pod startup latency, affecting deployment and auto-scaling responsiveness.

```bash
avg(kubelet_image_pull_duration_seconds_sum) by (image_size_in_bytes)
```

This Prometheus query calculates the average duration it takes to pull container images in a Kubernetes cluster, categorized by image size. The query uses `avg()` to compute the mean pull time across all nodes and containers, while `by (image_size_in_bytes)` groups these averages according to predefined image size buckets. This metric helps identify whether larger images are causing noticeable delays during pod initialization, which can impact deployment speed and scaling responsiveness in the cluster.

### **Container Network Errors**

![image.png](K8%20Cluster%20Infrastructure%20Dashboard/image%2012.png)

This panel tracks network-related failures for each node in the cluster, specifically those reported at the container level under "Receive" operations.

Each entry maps to a pod/node interface, and a non-zero error count here usually signals:

- Interface-level packet drops
- MTU mismatch
- CNI plugin misconfiguration
- Underlying host network failures

In the dashboard, all nodes report `0` container network errors. This indicates that the container network layer is stable, and no packet loss or receive errors have been observed during the captured interval. Sustained non-zero values here would require checking CNI plugin logs, inspecting node-level network interfaces, and verifying DNS and routing policies within the cluster.

```bash
sum by (env, node) (increase(container_network_receive_errors_total[1m0s]))
```

This Prometheus query calculates the total number of network receive errors on container interfaces across a Kubernetes cluster over a 1-minute interval, grouped by environment and node. It uses the `increase()` function to measure the absolute change in the `container_network_receive_errors_total` counter metric during this timeframe, then aggregates results with `sum by (env, node)` to organize errors by their source location. This metric helps identify nodes experiencing network communication issues like packet drops, MTU mismatches, or CNI plugin misconfiguration.

### **Count of HTTP Fallback Usage (Env - Node)**

![image.png](K8%20Cluster%20Infrastructure%20Dashboard/image%2013.png)

This graph tracks the number of HTTP fallback requests issued per environment-node pair when a primary endpoint failed to respond or deliver the expected result. 

- Monitoring fallback behavior helps identify underlying instability in service-to-service communication.
- High fallback rates might not cause application crashes but could lead to performance degradation, non-deterministic behavior, or cascading delays.
- In the current state, the fallback usage count is consistently `0`, which is a strong signal that primary service endpoints are responding reliably and without error.

```bash
sum by (env, node) (increase(kubelet_lifecycle_handler_http_fallbacks_total[1m0s]))
```

This Prometheus query calculates the total number of HTTP fallback requests that occurred across a Kubernetes cluster over a 1-minute interval, grouped by environment and node. It uses the `increase()` function to measure the absolute change in the `kubelet_lifecycle_handler_http_fallbacks_total` counter during this timeframe, then aggregates these counts with `sum by (env, node)` to organize them by their source location. This metric helps identify nodes experiencing connectivity issues where primary HTTP endpoints failed, requiring fallback mechanisms to maintain operations.

### **Ephemeral Containers Usage (Debug Containers)**

![image.png](K8%20Cluster%20Infrastructure%20Dashboard/image%2014.png)

This metric reflects the count of ephemeral containers, also referred to as debug containers, in use at any given time across the cluster. Ephemeral containers are introduced to live pods to troubleshoot issues without restarting them. While extremely useful for diagnostics, their usage should be controlled due to:

- Security risks (e.g., bypassing access controls)
- Potential disruption if misused
- Resource contention

A value of `0` here indicates no ongoing debugging activity using ephemeral containers, which is expected in a healthy, stable cluster.

If this count spikes, it may signal:

- Repeated debugging of application failures
- Delayed resolution of incidents
- Poor CI/CD validation that pushes broken images

RBAC and audit logs should be monitored when ephemeral containers are used.

```bash
sum(kubelet_managed_ephemeral_containers)
```

This Prometheus query uses the `sum()` function to calculate the total number of ephemeral debugging containers currently being managed across the entire Kubernetes cluster. Ephemeral containers are temporary containers that can be added to running pods for troubleshooting purposes without restarting the pod. The metric `kubelet_managed_ephemeral_containers` tracks these special-purpose debug containers, and summing them provides visibility into how frequently administrators are performing live debugging in the production environment.

### **Kubernetes Scheduler Latency by Job**

![image.png](K8%20Cluster%20Infrastructure%20Dashboard/image%2015.png)

This panel reports the latency experienced by the Kubernetes scheduler when binding pods to nodes, segmented by job or workload identity. Latency here represents the time between when a pod is ready for scheduling and when it is successfully assigned to a node. This metric is critical for assessing scheduling efficiency and cluster responsiveness.

In the current state, jobs like `thanos-bucketweb` and `thanos-compactor` show scheduler latencies ranging between 76.7 microseconds to 709 microseconds. These are the latency values, indicating that:

- The cluster has sufficient available compute
- There are minimal scheduling constraints (e.g., taints/tolerations, node selectors)
- Scheduler is performing optimally under the current load

Prolonged or spiking latencies (especially over 1–2 seconds) may indicate resource fragmentation, node pressure, or bottlenecks in affinity rule resolution, and should be reviewed using `kubectl describe node`.

```bash
histogram_quantile(0.99, rate(go_sched_latencies_seconds_bucket[1m0s]))
```

This Prometheus query uses the histogram_quantile function to calculate the 99th percentile (0.99) of scheduler latency in the Kubernetes cluster. It measures how long it takes the Go scheduler to complete scheduling operations by analyzing the rate of change in the go_sched_latencies_seconds_bucket metric over a 1-minute window. This helps identify if nearly all (99%) scheduling decisions are completing within an acceptable timeframe, which is crucial for understanding cluster responsiveness when placing pods on nodes.

---

## Storage  Monitoring

Used to track the capacity, performance, and cleanup behavior of persistent storage.

### **PVC Storage Usage (Tabular Breakdown)**

![image.png](K8%20Cluster%20Infrastructure%20Dashboard/image%2016.png)

This panel provides a granular view of individual PVCs across the environment, showing their associated namespace, allocated capacity, current usage, percentage used, and projected time until full.

Each row includes the following fields:

#### PVC (Name)

This column shows the name of the PersistentVolumeClaim. It is derived from the label `persistentvolumeclaim` in the metrics.

```bash
label_values(kubelet_volume_stats_used_bytes, persistentvolumeclaim)
```

This query extracts all unique values from the 'persistentvolumeclaim' label in the 'kubelet_volume_stats_used_bytes' metric. It's used to populate the PVC name column in the storage monitoring dashboard, allowing you to see a list of all PersistentVolumeClaims that have storage usage metrics being collected by Kubelet.

---

#### Env (Environment URL)

This is the cluster or environment where the PVC resides, inferred from the `env` or `origin_prometheus` label.

```
label_values(kubelet_volume_stats_used_bytes, origin_prometheus)
```

This query is used to extract all unique values from the 'origin_prometheus' label in the 'kubelet_volume_stats_used_bytes' metric. It retrieves a list of environment URLs where volume storage metrics are being collected by Kubelet, which helps identify which environments or clusters are reporting storage usage data.

---

#### Namespaces

The namespace of the PVC, taken from the `namespace` label.

```
label_values(kubelet_volume_stats_used_bytes, namespace)
```

This PromQL query uses the `label_values()` function to extract all unique values from the 'namespace' label in the 'kubelet_volume_stats_used_bytes' metric. This helps identify which Kubernetes namespaces are reporting storage volume statistics through Kubelet's metrics system.

---

#### Usage (Bytes used)

The current space is used by the PVC.

```
max by (persistentvolumeclaim, namespace) (
  kubelet_volume_stats_used_bytes{origin_prometheus=~".*"}
)
```

This query finds the maximum number of bytes used by each PersistentVolumeClaim (PVC) across the cluster. The query uses `max by` to aggregate the highest value for each unique combination of PVC name and namespace, while filtering metrics from any Prometheus origin using the wildcard pattern `.*`. This measurement helps track storage consumption for individual persistent volumes.

---

#### Total (Bytes capacity)

The total capacity = used + available.

```
(
  max by (persistentvolumeclaim, namespace) (
    kubelet_volume_stats_used_bytes{origin_prometheus=~".*"}
  )
  +
  min by (persistentvolumeclaim, namespace) (
    kubelet_volume_stats_available_bytes{origin_prometheus=~".*"}
  )
)
```

This query calculates the total storage capacity of each PersistentVolumeClaim (PVC) by combining two metrics. It takes the maximum used bytes for each PVC and namespace combination, and adds it to the minimum available bytes for the same PVC and namespace. The query uses aggregation operators (max by and min by) to ensure accurate pairing of used and available space measurements for each unique PVC.

---

#### Used (%)

Percentage of total capacity consumed.

```bash
max by (persistentvolumeclaim, namespace) (
  kubelet_volume_stats_used_bytes{origin_prometheus=~".*"}
)
/
(
  max by (persistentvolumeclaim, namespace) (
    kubelet_volume_stats_used_bytes{origin_prometheus=~".*"}
  )
  +
  min by (persistentvolumeclaim, namespace) (
    kubelet_volume_stats_available_bytes{origin_prometheus=~".*"}
  )
)
* 100
```

This PromQL query calculates the percentage of storage space used for each PersistentVolumeClaim (PVC) in the cluster. It does this by dividing the maximum used bytes by the total capacity (used + available bytes) for each PVC and namespace combination, then multiplying by 100 to get a percentage. The query uses aggregation operators (max by and min by) to ensure accurate matching of used and available space measurements for each unique PVC.

---

#### Days to Full

This is a projected estimate based on the current usage growth rate. It is often derived externally via Grafana transformations or recording rules using `predict_linear`:

```bash
predict_linear(
  kubelet_volume_stats_used_bytes{origin_prometheus=~".*"}[6h],
  86400 * 14
)
```

This PromQL query uses the predict_linear function to forecast storage usage growth over the next 14 days. It analyzes the past 6 hours of volume usage data (kubelet_volume_stats_used_bytes) across all Prometheus instances (.*) to calculate a linear projection. The 86400*  14 parameter converts 14 days into seconds, which is the time-frame for the prediction.

> `predict_linear` predicts future value based on historical trend. The [6h] window can vary.
> 

In the current state, no PVCs are close to full, and all are well under critical thresholds (e.g., none exceed 30% usage).

---

### **PVCs Full in 7 Days – Based on Daily Usage**

![image.png](K8%20Cluster%20Infrastructure%20Dashboard/a05673af-b5a6-4d34-ada1-7a9234b7ccc5.png)

This panel forecasts the number of PVCs that are expected to reach full capacity within the next 7 days, based on recent average daily usage.

```bash
count(
  (
    kubelet_volume_stats_available_bytes{namespace=~"${k8s_namespace}"}
    and
    (predict_linear(kubelet_volume_stats_available_bytes{namespace=~"${k8s_namespace}"}[1d], 7 * 24 * 60 * 60) < 0)
  )
) or vector(0)

```

- This query predicts future exhaustion of storage based on linear regression and counts PVCs expected to run out within 7 days:

A value of `0` indicates that no PVCs are projected to be exhausted in the short term. This means:

- The writing rates are moderate.
- Volume sizing strategies are currently sufficient.
- No immediate scale-up or cleanup actions are required.

If this metric rises, it may require action such as resizing volumes, offloading logs, or increasing replica sharding to distribute storage load.

---

### **PVCs Above 80%**

![image.png](K8%20Cluster%20Infrastructure%20Dashboard/05345fde-3be5-4f29-94cc-2aebf1e358d2.png)

This metric counts the number of PVCs that have crossed 80% of their provisioned capacity, a critical threshold for preemptive alerting.

This checks for PVCs where the usage exceeds 80% of the total capacity:

```bash
count(
  (
    max by (persistentvolumeclaim,namespace) (kubelet_volume_stats_used_bytes{})
    /
    max by (persistentvolumeclaim,namespace) (kubelet_volume_stats_capacity_bytes{})
  ) >= (80 / 100)
) or vector(0)

```

A high count here can indicate:

- Imminent risk of application disruption
- Lack of automated volume expansion
- Inefficient data cleanup policies

The dashboard reports `0`, which is ideal and suggests that volume usage is well under control.

---

### **PVCs in Pending State**

![image.png](K8%20Cluster%20Infrastructure%20Dashboard/06b581e3-460c-44f5-beb2-e33cc71af11d.png)

This metric reflects the count of PVCs that have been created but not yet successfully bound to a Persistent Volume (PV).

**PVCs in Pending State**

The below query counts PVCs currently in a Pending state.

```bash
count(
  (
    kube_persistentvolumeclaim_status_phase{namespace=~"${k8s_namespace}",phase="Pending"} == 1
  )
) or vector(0)
```

A value of `0` means all PVCs are properly bound and available for use. If this number increases, it may signal:

- Insufficient available storage classes
- Misconfigured storage policies
- Cluster storage pressure or provisioning failures

Pending PVCs often lead to pod scheduling delays or crashes, so this metric is a key indicator of volume provisioning health.

---

### **PVCs in Lost State**

![image.png](K8%20Cluster%20Infrastructure%20Dashboard/a7b63ff6-939b-442a-badc-ce6295ccefc4.png)

This metric displays the number of PVCs marked as `Lost`, which occurs when the underlying Persistent Volume becomes unavailable or is deleted outside the control of Kubernetes. Counts PVCs marked as "Lost" by Kubernetes:

```bash
sum(kube_persistentvolumeclaim_status_phase{phase="Lost"})
```

A lost PVC cannot be recovered or remounted and typically results in application data loss.

With `0` lost PVCs reported, the environment shows strong volume lifecycle hygiene and no recent volume deletions that affected data integrity.

---

### **Volume Cleanup Failures Count**

![image.png](K8%20Cluster%20Infrastructure%20Dashboard/image%2017.png)

This panel tracks the number of failed attempts to clean up volumes (e.g., after PVC deletion), grouped by environment and node.

```bash
count(kubelet_orphan_pod_cleaned_volumes_errors) by (env, node)
```

Volume cleanup failures can occur due to:

- Improper access permissions
- Stuck finalizers on PV resources
- Node-level issues with volume detach/unmount logic

The dashboard shows 21 failures per node across multiple environments, which suggests that the cleanup logic is encountering repeated issues, potentially with storage class deprovisioners, CSI drivers, or node taints that block cleanup jobs.

This is a deviation from expected behavior and should be triaged by inspecting:

- Finalizer logs (`kubectl get pv -o yaml`)
- CSI plugin logs
- Cloud provider or storage backend APIs
- Counts cleanup failures of orphaned PVCs grouped by environment and node:

### **PVC Usage %**

![image.png](K8%20Cluster%20Infrastructure%20Dashboard/image%2018.png)

This panel shows the percentage of storage capacity used for individual Persistent Volume Claims (PVCs) over time. Each colored line represents a PVC, with its usage plotted as a percentage of its total allocated volume. The graph helps identify PVCs that are:

- Growing rapidly
- Consistently high in usage
- Approaching saturation thresholds

In the current view, all PVCs remain under 30% utilization, with most below 10%, indicating no immediate risk. The highest usage is seen for `data-zookeeper-stream-2` (~30%), which should be monitored, but does not yet warrant action. This panel is essential for trend-based capacity forecasting, allowing teams to detect abnormal growth patterns early and act before pods fail due to full volumes. The below query calculates the real-time percentage of used space per PVC:

```bash
kubelet_volume_stats_used_bytes / kubelet_volume_stats_capacity_bytes * 100
```

---

## Certificates

Monitors certificates (e.g., kubelet client certs, admission webhooks, TLS secrets) for expiry.

![image.png](K8%20Cluster%20Infrastructure%20Dashboard/image%2019.png)

### **Time Left**

This panel shows how much time remains before certificates expire in the cluster. It helps track certificate lifecycle and ensure timely renewal to prevent service disruptions.

![image.png](K8%20Cluster%20Infrastructure%20Dashboard/image%2020.png)

### **Expired Certificates**

This panel displays the number of certificates that have already expired and are still present in the cluster. Currently, it shows “No data”, meaning no certificates are expired, which indicates good operational hygiene and active certificate management.

![image.png](K8%20Cluster%20Infrastructure%20Dashboard/3ef3b153-77bb-404a-a9d4-540c960a233c.png)

```bash
(certmanager_certificate_expiration_timestamp_seconds - time()) < 0
```

This PromQL query identifies certificates that have already expired in the Kubernetes cluster. It works by calculating the difference between each certificate's expiration timestamp (certmanager_certificate_expiration_timestamp_seconds) and the current time (time()). When this calculation results in a value less than 0, it indicates that the certificate has passed its expiration date. This query is crucial for monitoring certificate health and identifying security risks from expired certificates that could potentially cause service disruptions or compromise TLS security.

---

### **Certificates Expiring in ≤ 7 Days**

This panel highlights any certificates that are due to expire within the next 7 days.

![image.png](K8%20Cluster%20Infrastructure%20Dashboard/10c6c9bc-1d44-4744-b757-ec55270afcc6.png)

A value of `0` here means there are no certificates at immediate risk of expiring, which is ideal for maintaining uninterrupted cluster security, especially in production environments.

```bash
sort(sum by( exported_namespace, env, name) (certmanager_certificate_expiration_timestamp_seconds) - time() < 604800)
```

This PromQL query identifies certificates that will expire within the next 7 days (604,800 seconds). It first calculates the remaining time for each certificate by subtracting the current time from the expiration timestamp, groups these results by exported namespace, environment, and certificate name, and then sorts them in ascending order. The query also applies a filter with the "< 604800" condition to only show certificates with less than 7 days remaining until expiration. This provides operators with a prioritized list of certificates requiring immediate renewal attention.

---

### **Certificate Signing Requests Approved**

This metric shows the number of approved CSR (Certificate Signing Requests).

![image.png](K8%20Cluster%20Infrastructure%20Dashboard/39764d65-dded-4aec-bdb9-92a43d8699a3.png)

In Kubernetes, CSRs are submitted when components request client certificates (e.g., kubelet, kube-controller-manager). A value of `0` may indicate:

- No new cert requests
- Auto-renewal mechanisms are already handling certificates
- Or certificate issuance is manually controlled

```bash
count(kube_certificatesigningrequest_condition{condition="approved"})
```

This PromQL query counts the number of Certificate Signing Requests (CSRs) in the Kubernetes cluster that have been approved. It uses the metric `kube_certificatesigningrequest_condition` with the filter `condition="approved"` to specifically count only those CSRs that have received approval. This metric is important for tracking certificate lifecycle management and understanding how many certificate requests have been successfully processed in the cluster.

---

### **Certificate Signing Requests Denied**

This tracks CSRs that were explicitly denied, often due to:

- Failed validation policies
- Improper request format
- Lack of RBAC permissions

![image.png](K8%20Cluster%20Infrastructure%20Dashboard/84841f12-84fc-4c90-8a73-9b7e387b7b62.png)

Currently at `0`, which suggests no abnormal request attempts or security policy violations.

```bash
count(kube_certificatesigningrequest_condition{condition="denied"})
```

This PromQL query counts the number of Certificate Signing Requests (CSRs) in the Kubernetes cluster that have been explicitly denied. It uses the metric `kube_certificatesigningrequest_condition` with the filter `condition="denied"` to specifically count only those CSRs that were rejected. This metric is important for monitoring potential security issues or policy violations, as denied CSRs often indicate requests that failed validation checks, had improper formatting, or lacked sufficient RBAC permissions.

---

### **Certificate Signing Requests Pending**

This shows how many CSRs are currently waiting for approval or denial.

![image.png](K8%20Cluster%20Infrastructure%20Dashboard/d0c1810b-0057-43a6-b93c-a17ffed5166c.png)

A value of `0` means no outstanding certificate requests are awaiting manual review, ensuring there are no bottlenecks in the cert issuance process.

```bash
count(kube_certificatesigningrequest_condition{condition="pending"})
```

This PromQL query counts the number of Certificate Signing Requests (CSRs) in the Kubernetes cluster that are currently in a pending state. It uses the metric `kube_certificatesigningrequest_condition` with the filter `condition="pending"` to specifically count only those CSRs that are awaiting approval or denial. This metric is important for monitoring certificate management workflows and identifying potential bottlenecks in the certificate issuance process that might require manual intervention.

---

### **Number of Issued Certificates**

This panel counts the total certificates issued in the current time window (e.g., last hour or day).

![image.png](K8%20Cluster%20Infrastructure%20Dashboard/6e7878b4-b05c-4d80-9513-b7545fa59efe.png)

Right now, it’s at `0`, which is expected if there hasn’t been recent certificate rotation, onboarding of new nodes, or service deployments requiring new TLS identities.

```bash
count(kube_certmanager_certificate_ready)
```

This PromQL query `count(kube_certmanager_certificate_ready)` counts the total number of certificates managed by cert-manager that are currently in a ready state within the Kubernetes cluster. It provides a quick overview of the functioning certificates in the environment, helping administrators monitor certificate health and deployment status without detailing individual certificates.

---

## Workloads Breakdown

Aims to break down Kubernetes controllers by health, to aid in pinpointing deployment or scaling issues.

![image.png](K8%20Cluster%20Infrastructure%20Dashboard/image%2021.png)

### **Deployments**

This panel tracks the health of Kubernetes Deployments, which are used to manage applications with automatic rollout and rollback capabilities.

![image.png](K8%20Cluster%20Infrastructure%20Dashboard/48d3aff7-1449-4122-881c-aad200657b81.png)

In the given state, 112 deployments are running successfully, representing the majority. One deployment is marked as underprovisioned, meaning it may not have sufficient resources to scale as intended, or its replicas are not fully scheduled. Additionally, one deployment is reported as down, which typically indicates that no pods are available or the deployment is failing liveness or readiness checks. There are no deployments marked as “not running,” confirming that no deployment is idle without any active pods. This reflects a healthy deployment posture overall, with only two needing investigation.

```bash
label_replace(
  (
    label_replace(
      kube_deployment_status_replicas_ready > 0 and on(namespace, deployment)
      kube_deployment_status_replicas_ready == kube_deployment_spec_replicas,
      "status", "Running", "", ""
    )
    or label_replace(
      kube_deployment_spec_replicas == 0 and kube_deployment_status_replicas_ready == 0,
      "status", "NotRunning", "", ""
    )
    or label_replace(
      kube_deployment_status_replicas_ready < kube_deployment_spec_replicas and kube_deployment_status_replicas_ready > 0,
      "status", "UnderProvisioned", "", ""
    )
    or label_replace(
      kube_deployment_spec_replicas > 0 and kube_deployment_status_replicas_ready == 0,
      "status", "Down", "", ""
    )
  ),
  "deployment", "$1", "deployment", "(.*)"
)
```

This PromQL query categorizes Kubernetes deployments into four status types using a series of logical conditions and label replacements. It first identifies deployments as "Running" when all replicas are ready, "NotRunning" when zero replicas are specified and zero are ready, "UnderProvisioned" when some but not all replicas are ready, and "Down" when replicas are specified but none are ready. The final label_replace function ensures consistent naming of deployment labels. This query powers the Deployments panel in the dashboard, providing a clear breakdown of deployment health across the cluster for operational monitoring.

---

### **StatefulSets**

This panel displays the status of StatefulSets, which are used for stateful applications where persistent storage and stable network identity are required (e.g., Lakesearch, Flash).

![image.png](K8%20Cluster%20Infrastructure%20Dashboard/59980662-f8f1-404e-8be4-506f008fc36a.png)

Out of the 71 total StatefulSets, 60 are currently running. However, 10 are in the “not running” category, implying pods were created but are not active. One StatefulSet is down, likely failing at the pod or controller level. No StatefulSets are underprovisioned, meaning all required replicas have at least been attempted, though not necessarily running.

This signals moderate operational risk. Non-running StatefulSets should be checked for volume attachment errors, misconfigurations, or readiness failures.

```bash
label_replace(
  (
    label_replace(
      kube_statefulset_status_replicas_ready > 0 and on(namespace, statefulset)
      kube_statefulset_status_replicas_ready == kube_statefulset_replicas,
      "status", "Running", "", ""
    )
    or label_replace(
      kube_statefulset_replicas == 0 and kube_statefulset_status_replicas_ready == 0,
      "status", "NotRunning", "", ""
    )
    or label_replace(
      kube_statefulset_status_replicas_ready < kube_statefulset_replicas and kube_statefulset_status_replicas_ready > 0,
      "status", "UnderProvisioned", "", ""
    )
    or label_replace(
      kube_statefulset_replicas > 0 and kube_statefulset_status_replicas_ready == 0,
      "status", "Down", "", ""
    )
  ),
  "statefulset", "$1", "statefulset", "(.*)"
)

```

This PromQL query categorizes Kubernetes StatefulSets into four distinct operational statuses by evaluating their replica metrics. It first identifies StatefulSets as "Running" when all requested replicas are ready and match the specified count, "NotRunning" when zero replicas are specified and zero are ready, "UnderProvisioned" when some but not all replicas are ready, and "Down" when replicas are specified but none are ready. The query uses multiple label_replace functions to tag each StatefulSet with its appropriate status, and the final label_replace ensures a consistent labeling format. This comprehensive query powers the StatefulSets panel in the dashboard, providing operators with a clear breakdown of StatefulSet health across the cluster for effective monitoring and troubleshooting.

---

### **DaemonSets**

This panel covers DaemonSets, which ensure that a specific pod runs on all (or selected) nodes. Common examples include monitoring agents or log collectors.

![image.png](K8%20Cluster%20Infrastructure%20Dashboard/ffd02ed3-fb87-4bf1-a46a-28d6a93481ef.png)

There are 14 DaemonSets running successfully, with 4 showing as “not running.” This suggests that some expected pods are not deployed on one or more nodes. No DaemonSets are underprovisioned or down, indicating that resource availability is not currently the issue.

The mismatch between expected and actual pod count is usually due to taints, nodeSelector conflicts, or node scheduling errors, and should be reviewed against node configurations.

```bash
label_replace(
  (
    label_replace(
      kube_daemonset_status_number_ready > 0 and on(namespace, daemonset)
      kube_daemonset_status_number_ready == kube_daemonset_status_desired_number_scheduled,
      "status", "Running", "", ""
    )
    or label_replace(
      kube_daemonset_status_desired_number_scheduled == 0 and kube_daemonset_status_number_ready == 0,
      "status", "NotRunning", "", ""
    )
    or label_replace(
      kube_daemonset_status_number_ready < kube_daemonset_status_desired_number_scheduled and kube_daemonset_status_number_ready > 0,
      "status", "UnderProvisioned", "", ""
    )
    or label_replace(
      kube_daemonset_status_desired_number_scheduled > 0 and kube_daemonset_status_number_ready == 0,
      "status", "Down", "", ""
    )
  ),
  "daemonset", "$1", "daemonset", "(.*)"
)

```

This PromQL query categorizes Kubernetes DaemonSets into four operational statuses using a series of logical conditions and label replacements. It identifies DaemonSets as "Running" when all pods are ready across desired nodes, "NotRunning" when no pods are scheduled or ready, "UnderProvisioned" when some but not all desired pods are ready, and "Down" when pods are desired but none are ready. The query uses multiple label_replace functions to tag each DaemonSet with its appropriate status, creating a comprehensive health visualization that helps operators quickly identify problematic DaemonSets requiring attention.

---

### **ReplicaSets**

This panel reports on ReplicaSets, the low-level controller that ensures a specified number of pod replicas are maintained. Deployments automatically manage ReplicaSets under the hood, but standalone ReplicaSets may also exist.

![image.png](K8%20Cluster%20Infrastructure%20Dashboard/6488426e-fe54-4b0e-8d69-f3ec11038edb.png)

There are 453 ReplicaSets reported as running, with 340 marked as “not running.” While this seems high, it's common behavior in Kubernetes. Older ReplicaSets from past deployment rollouts often persist even when their pods are scaled to zero. Only two ReplicaSets are considered down, which indicates they are failing to maintain any pods.

Although this panel shows a large volume of inactive ReplicaSets, the low number of “down” entries suggests that most are simply dormant, not faulty. If needed, older ReplicaSets can be cleaned up to reduce dashboard noise and controller overhead.

```bash
label_replace(
  (
    label_replace(
      kube_replicaset_status_ready_replicas > 0 and on(namespace, replicaset)
      kube_replicaset_status_ready_replicas == kube_replicaset_spec_replicas,
      "status", "Running", "", ""
    )
    or label_replace(
      kube_replicaset_spec_replicas == 0 and kube_replicaset_status_ready_replicas == 0,
      "status", "NotRunning", "", ""
    )
    or label_replace(
      kube_replicaset_status_ready_replicas < kube_replicaset_spec_replicas and kube_replicaset_status_ready_replicas > 0,
      "status", "UnderProvisioned", "", ""
    )
    or label_replace(
      kube_replicaset_spec_replicas > 0 and kube_replicaset_status_ready_replicas == 0,
      "status", "Down", "", ""
    )
  ),
  "replicaset", "$1", "replicaset", "(.*)"
)

```

This PromQL query categorizes Kubernetes ReplicaSets into four operational statuses using logical conditions and label replacements. It identifies ReplicaSets as "Running" when all requested replicas are ready, "NotRunning" when zero replicas are specified and ready, "UnderProvisioned" when some but not all replicas are ready, and "Down" when replicas are specified but none are ready. The query uses multiple label_replace functions to apply these status labels, with a final label_replace ensuring consistent naming. This provides operators with a clear breakdown of ReplicaSet health across the cluster for monitoring and troubleshooting purposes.

---

## Kubernetes Secrets

This section helps maintain visibility into sensitive configuration data.

### **Kubernetes Secrets Count**

This panel displays the total number of Kubernetes Secrets currently stored in the cluster. Secrets are used to securely store sensitive data such as passwords, tokens, SSH keys, and TLS certificates. The current count is 660, which includes all secrets across all namespaces in the environment.

![image.png](K8%20Cluster%20Infrastructure%20Dashboard/0038c978-cb17-48ec-ab61-406d3021fb67.png)

While this number alone doesn’t indicate an issue, a steadily increasing secret count over time may suggest:

- Lack of cleanup of expired or unused secrets
- Frequent secret generation by controllers (e.g., cert-manager, service accounts)
- Overuse of secrets per pod/app that could impact etcd size or API server performance

Proper lifecycle management and automated secret rotation policies help maintain a healthy and secure cluster state.

```bash
count(kube_secret_info)
```

This PromQL query `count(kube_secret_info)` simply counts the total number of Kubernetes Secrets currently stored in the cluster across all namespaces. It provides a high-level metric that helps administrators track the overall volume of secrets without filtering by type, namespace, or other attributes. This count is useful for monitoring secret sprawl, potential etcd performance impacts, and maintaining awareness of sensitive configuration data in the environment.

---

### **Secret Count by Env and Namespace**

This table breaks down the secret count across different environments and namespaces, helping identify where secrets are concentrated.

![image.png](K8%20Cluster%20Infrastructure%20Dashboard/f9479106-263c-45f2-a40a-5c7febfcb21c.png)

In the current view:

- The `system` namespace holds 288 secrets, which is high and typically includes internal Kubernetes secrets, service account tokens, and possibly automatically generated certificates.
- The `public` namespace contains 92 secrets, which may relate to application-level credentials, config-based tokens, or ingress/TLS secrets.
- The `research` namespace has 32 secrets, reflecting lighter usage — likely test or isolated workloads.

Tracking secret distribution by namespace helps identify:

- High-volume namespaces that may require rotation automation or secret pruning
- Potential misuse or overprovisioning of secrets (e.g., redundant credentials)
- Clusters at risk of reaching etcd size limits due to secret sprawl

The values are color-coded: higher counts (e.g., red for `288`) signal areas where closer inspection may be needed.

```bash
sort_desc(count by(namespace, env) (increase(kube_secret_created[5m])))
```

This PromQL query sorts in descending order the count of newly created Kubernetes secrets within the last 5 minutes, grouped by namespace and environment. The query uses the `increase(kube_secret_created[5m])` function to track the rate of secret creation in the specified time window, then counts and organizes these by both namespace and environment labels, finally presenting the results with the highest counts first through `sort_desc`. This helps administrators quickly identify which namespaces and environments are experiencing the most rapid secret creation activity, which could indicate normal operations, potential security issues, or problematic automation.
