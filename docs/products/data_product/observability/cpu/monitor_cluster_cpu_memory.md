# Monitor the CPU and Memory Usage of a Cluster

When a Cluster Resource is created, a corresponding pod is automatically provisioned in the backend. This section involves steps to monitor the CPU and memory usage of a Cluster’s pod using different endpoints.

## Monitor the CPU and memory usage of a Cluster using Metis UI

To monitor the CPU and memory usage of a Cluster on the Metis Catalog UI, follow the steps below:

1. Open the Metis Catalog.
    
    <div style="text-align: center;">
      <img src="/products/data_product/observability/dashboards/entities/entities_home_dashboards_infrastructure_cluster_entities_dup.png" style="width: 70%; height: auto;">
      <figcaption><i>I~ Home » Dashboards > Infrastructure > K8s Cluster Entities | ENV | https://pro- n.dataos.app » | nodes Ally | Names...</i></figcaption>
    </div>
    
2. Search for the Cluster by name.
    
    <div style="text-align: center;">
      <img src="/products/data_product/observability/dashboards/entities/entities_home_dashboards_infrastructure_cluster_entities_dup.png" style="width: 70%; height: auto;">
      <figcaption><i>I~ Home » Dashboards > Infrastructure > K8s Cluster Entities | ENV | https://pro- n.dataos.app » | nodes Ally | Names...</i></figcaption>
    </div>
    
3. Click on the Cluster that needs to be monitored and navigate to the ‘Runtime’ section.
    
    <div style="text-align: center;">
      <img src="/products/data_product/observability/dashboards/infra/infra_home_dashboards_infrastructure_cluster_infrastructure_dup.png" style="width: 70%; height: auto;">
      <figcaption><i>I~ Home > Dashboards > Infrastructure > Ks Cluster Infrastructure Q Search ctisk| +» | @ w Edit | | Export » ENV | ht...</i></figcaption>
    </div>
    
4. Click on the run name for which you want to monitor the CPU and memory usage, and navigate to the ‘Pod Usage’ section.
    
    <div style="text-align: center;">
      <img src="/products/data_product/observability/dashboards/infra/infra_home_dashboards_infrastructure_cluster_infrastructure_dup.png" style="width: 70%; height: auto;">
      <figcaption><i>I~ Home > Dashboards > Infrastructure > Ks Cluster Infrastructure Q Search ctisk| +» | @ w Edit | | Export » ENV | ht...</i></figcaption>
    </div>
    
    **CPU usage:**
    
    - Usage (blue line) shows actual CPU consumed by the Cluster pod, increasing steadily and reaching just above 600 millicores.
    - Request (green line) is fixed at approximately 250 millicores, indicating the CPU guaranteed for the pod at scheduling time.
    - Limit (yellow line) is flat at 2000 millicores, representing the maximum CPU the pod is allowed to use if resources are available.
    
    <aside class="callout">
    🗣 The actual usage exceeds the requested value, meaning the pod consumed more than what was guaranteed but stayed well below the limit. This could result in temporary throttling, and it may be worth revisiting the request configuration for better scheduling efficiency.
    </aside>
    
    <div style="text-align: center;">
      <img src="/products/data_product/observability/dashboards/entities/entities_containers_utilization_maximum100associable_nodes_1205.png" style="width: 70%; height: auto;">
      <figcaption><i>Pod Containers CPU Utilization (Maximum100%Associable Nodes) © 12:05 12:10 12:15 12:20 12:25 Name v Mean Max = zookee...</i></figcaption>
    </div>
    
    **Memory usage:**
    
    - Usage (blue line) shows actual memory consumed by the workflow pod, increasing over time and reaching just under 1000 MiB.
    - Request (green line) is not visible in the graph, which indicates that memory was not explicitly requested or the request value is not available in this dataset.
    - Limit (yellow line) remains constant at 2500 MiB, indicating the maximum memory the pod is allowed to consume.
    
    <aside class="callout">
    🗣 The memory usage is well below the defined limit. Since no request value is shown, the scheduler may not have reserved memory explicitly. Overall, the workload appears to be operating within safe limits, with potential to optimize further if needed.
    </aside>
    
    <div style="text-align: center;">
      <img src="/products/data_product/observability/cpu/workflow/workflow_aggregates_states_time_slices_type.png" style="width: 70%; height: auto;">
      <figcaption><i>Aggregates (pod states: 20 time slices: 2) Type cpu memory memory memory Name usage request limit usage request limit...</i></figcaption>
    </div>
    
    **Details:**
    
    - **Type**: Indicates whether the metric refers to CPU or memory.
    - **Name**: Describes the metric subtype `usage` (actual consumption), `request` (minimum reserved), or `limit` (maximum allowed).
    - **Mean / Median / Min / Max**: Statistical summaries over the measured time slices.
    - **Sum**: Total usage across all time slices.
    - **Unit**: CPU is in millicores (1000 millicores = 1 core); memory is in mebibytes (1 MiB = 1,048,576 bytes).
    - **CPU Usage**: Average CPU usage was 460 millicores, peaking at 690 millicores. The pod used significantly more than its request, but stayed within the limit.
    - **CPU Request**: Set at 200 millicores consistently, meaning the pod was guaranteed a small baseline of CPU.
    - **CPU Limit**: Fixed at 2000 millicores (2 cores), providing ample room for the workload to scale under load.
    - **Memory Usage**: Average memory usage was approximately 527.72 MiB, with a maximum usage of 791.58 MiB.
    - **Memory Request**: Set at 2432 MiB, meaning this much memory was reserved and guaranteed to the pod.
    - **Memory Limit**: Also set at 2432 MiB, indicating that the pod could not use more memory than requested.
    
    > The Cluster was allowed to consume significantly more CPU than it requested, and it did so, but stayed under the defined limit. Memory usage remained far below both the request and limit. This suggests an opportunity to reduce memory allocation to free up resources for other workloads.
    > 

## Monitor the CPU and memory usage of a Cluster using the Operations App

When a Cluster Resource is created, a corresponding pod is automatically provisioned in the backend. You can monitor the CPU and memory usage of this pod directly through the Operations app.

To monitor the CPU and memory usage of a Cluster on the Operations app, follow the steps below:

1. Open the Operations app.
    
    <div style="text-align: center;">
      <img src="/products/data_product/observability/dashboards/entities/entities_home_dashboards_infrastructure_cluster_entities_dup.png" style="width: 70%; height: auto;">
      <figcaption><i>I~ Home » Dashboards > Infrastructure > K8s Cluster Entities | ENV | https://pro- n.dataos.app » | nodes Ally | Names...</i></figcaption>
    </div>
    
2. Navigate to User Space → Resources → types, select the Cluster as type, and search for the Cluster that needs to be monitored.
    
    <div style="text-align: center;">
      <img src="/products/data_product/observability/dashboards/entities/entities_home_dashboards_infrastructure_cluster_entities_dup.png" style="width: 70%; height: auto;">
      <figcaption><i>I~ Home » Dashboards > Infrastructure > K8s Cluster Entities | ENV | https://pro- n.dataos.app » | nodes Ally | Names...</i></figcaption>
    </div>
    
3. Click on the Cluster, navigate to the ‘Resource Runtime’ section.
    
    <div style="text-align: center;">
      <img src="/products/data_product/observability/dashboards/infra/infra_home_dashboards_infrastructure_cluster_infrastructure_dup.png" style="width: 70%; height: auto;">
      <figcaption><i>I~ Home > Dashboards > Infrastructure > Ks Cluster Infrastructure Q Search ctisk| +» | @ w Edit | | Export » ENV | ht...</i></figcaption>
    </div>
    
4. Click on the pod name for which you want to monitor the CPU and memory usage, and navigate to the ‘Runtime Node Usage’ section.
    
    <div style="text-align: center;">
      <img src="/products/data_product/observability/dashboards/infra/infra_home_dashboards_infrastructure_cluster_infrastructure_dup.png" style="width: 70%; height: auto;">
      <figcaption><i>I~ Home > Dashboards > Infrastructure > Ks Cluster Infrastructure Q Search ctisk| +» | @ w Edit | | Export » ENV | ht...</i></figcaption>
    </div>
    
    **Details:**
    
    - **Type**: Indicates whether the metric is related to CPU or memory.
    - **Name**: Specifies the metric subtype, `usage` (actual consumption), `request` (guaranteed minimum), and `limit` (maximum allocable resource).
    - **Mean / Median / Min / Max**: Statistical summaries of the metric over the evaluated time slices.
    - **Sum**: Total value accumulated across all time slices.
    - **Unit**: Measurement unit (millicore for CPU, mebibyte for memory).
    - **CPU Usage**: Average CPU usage was ~55.95 millicores, peaking at 535 millicores (1 core = 1000 millicores). Millicores provide fine-grained control over how much CPU each pod or container should receive.
    - **CPU Request**: The pods are configured to request 1200 millicores of CPU each, consistently across time slices.
    - **CPU Limit**: The pods are configured to limit 1200 millicores of CPU each, consistently across time slices.
    - **Memory Usage**: Average memory consumption stands at ~1305.46 MiB, with a peak at 1808.15 MiB (1 MiB = 2²⁰ bytes = 1,048,576 bytes).
    - **Memory Request**: Each pod has been allocated 2048.00 MiB as a guaranteed memory reservation.
    - **Memory Limit**: Each pod has been allocated 2048.00 MiB as a limited memory.
    
    <div style="text-align: center;">
      <img src="/products/data_product/observability/dashboards/entities/entities_containers_utilization_maximum100associable_nodes_1205.png" style="width: 70%; height: auto;">
      <figcaption><i>Pod Containers CPU Utilization (Maximum100%Associable Nodes) © 12:05 12:10 12:15 12:20 12:25 Name v Mean Max = zookee...</i></figcaption>
    </div>
    
    **CPU usage:**
    
    - Usage (blue line) shows intermittent spikes in CPU consumption, peaking close to 600 millicores. Between spikes, CPU usage drops near zero, indicating short bursts of activity followed by idle periods.
    - Request (green line) is not plotted, suggesting no CPU request was explicitly configured or it’s not captured here.
    - Limit (yellow line) remains constant at around 1200 millicores, representing the maximum CPU the pod can consume.
    
    <aside class="callout">
    🗣 The CPU usage exhibits bursty behavior, likely due to periodic task execution. Since usage stays well within the limit, throttling is unlikely, but the absence of a visible request means scheduling guarantees may not be enforced.
    </aside>
    
    **Memory usage:**
    
    - Usage (blue line) steadily increases, reaching up to 1900 MiB, then dips temporarily and stabilizes again around 1200–1400 MiB. This indicates a consistent memory footprint with some momentary drops.
    - Request (green line) is missing, indicating it was either not set or not shown in this view.
    - Limit (yellow line) is fixed at 2048 MiB, defining the upper bound for memory allocation.
    
    <aside class="callout>
    🗣 Memory usage is close to the limit but stays within bounds, suggesting the pod is memory-intensive. A configured memory request would improve scheduling reliability.
    </aside>
    

## Monitor the CPU and memory usage of a Cluster using Grafana (WIP)

When a Cluster Resource is created, a corresponding pod is automatically provisioned in the back-end. You can monitor the CPU and memory usage of this pod directly through the Grafana app.

<div style="text-align: center;">
  <img src="/products/data_product/observability/cpu/workflow/workflow_aggregates_states_time_slices_type.png" style="width: 70%; height: auto;">
  <figcaption><i>Aggregates (pod states: 20 time slices: 2) Type cpu memory memory memory Name usage request limit usage request limit...</i></figcaption>
</div>

To monitor the CPU and memory usage of a Cluster on the Grafana app, follow the steps below:

1. Execute the following command in DataOS CLI to get the pod name corresponding to the Cluster Resource.
    
    ```bash
    dataos-ctl log -t cluster -n bqcluster
    ```
    
    **Example usage:**
    
    ```bash
    INFO[0000] 📃 log(public)...                             
    INFO[0001] 📃 log(public)...complete                     
    
        NODE NAME    │ CONTAINER NAME │ ERROR  
    ─────────────────┼────────────────┼────────
      bqcluster-ss-0 │ bqcluster      │        
     # ^ pod name
    -------------------LOGS-------------------
        Task executor: pool=0, active=0, queue=0
        Concurrency control: slots=4, available=3
        Reservations:
            (pending)
    Query tasks:
    
    2025-06-03T09:01:32.289Z	INFO	Notification Thread	io.airlift.stats.JmxGcMonitor	Major GC: application 275994ms, stopped 61ms: 374.09MB -> 322.10MB
    2025-06-03T09:01:58.045Z	DEBUG	task-executor-scheduler-0	io.trino.execution.executor.dedicated.ThreadPerDriverTaskExecutor	
    Queue:
        Baseline weight: 0
        Groups:
        Task executor: pool=0, active=0, queue=0
        Concurrency control: slots=4, available=3
        Reservations:
            (pending)
    
    ```
    
2. Open the Grafana app. 
    
    ![image.png](attachment:c620a0a4-2311-4c84-9b78-8fd822d80410:image.png)
    
3. Navigate to the Explore section and select ‘Thanos’ as a source and search for the metric `cpu_container_usage_total`, and in the label filters select pod and paste the pod name which we have gotten from step 1, then click on ‘Run Query’. 
    
    <div style="text-align: center;">
      <img src="/products/data_product/observability/dashboards/infra/infra_home_explore_thanos_search_ctik.png" style="width: 70%; height: auto;">
      <figcaption><i>o Home > Explore > thanos Q Search... ctik| tv | @ © Query history | e@ Share Q thanos »~ | Q Goqueryless split Add» ...</i></figcaption>
    </div>
    
4. After clicking on the ‘Run Query’, you can find the usage of CPU by a Cluster within the selected time range.
    
    <div style="text-align: center;">
      <img src="/products/data_product/observability/dashboards/infra/infra_home_explore_thanos_search_ctik.png" style="width: 70%; height: auto;">
      <figcaption><i>o Home > Explore > thanos Q Search... ctik| tv | @ © Query history | e@ Share Q thanos »~ | Q Goqueryless split Add» ...</i></figcaption>
    </div>
    
    The graph represents CPU usage over time for multiple containers (including both init and main containers) that exist within a single pod belonging to a Cluster Resource named `bqcluster`.
    
    - All lines represent actual CPU usage, not requests or limits. This is confirmed by the use of the `container_cpu_usage_seconds_total` metric, which measures cumulative CPU seconds consumed by each container.
    - These containers collectively make up the pod that runs the `bqcluster` workload.
    - Having visibility into per-container usage helps distinguish whether performance issues originate in the main container or from its supporting components (init containers).
5. To monitor the memory usage, select the `container_memory_working_set_bytes` in the query explorer and select the pod name as the label filter of the corresponding Cluster and run the query.
    
    <div style="text-align: center;">
      <img src="/products/data_product/observability/dashboards/infra/infra_home_explore_thanos_search_ctik.png" style="width: 70%; height: auto;">
      <figcaption><i>o Home > Explore > thanos Q Search... ctik| tv | @ © Query history | e@ Share Q thanos »~ | Q Goqueryless split Add» ...</i></figcaption>
    </div>
    
6. On executing the query, users can see the memory used by the pod in the last thirty minutes. 
    
    <div style="text-align: center;">
      <img src="/products/data_product/observability/cpu/cluster/cluster_bgclusterss0_runtime_node_details_runtime.png" style="width: 70%; height: auto;">
      <figcaption><i>> bgcluster-ss-0: Runtime Node Details Runtime Node Details Runtime Node YAML Runtime Node Logs Runtime Node Usage In...</i></figcaption>
    </div>
    
    The graph represents memory usage over time for multiple containers inside a single pod. 
    
    - **Blue Line**: Represents the main container. The usage here is very low and consistent throughout the time window, indicating a lightweight container that consumes very little memory.
    - **Yellow and Green Lines:** Both lines represent memory usage of the init containers inside the same pod.
    
    Their usage shows a progressive increase over time, especially the yellow line, which rises from 6 GiB to 8+ GiB. This indicates a growing workload.
    
7. Users can further select the time range for which they want to see the CPU or memory usage of the pod.
    
    <div style="text-align: center;">
      <img src="/products/data_product/observability/dashboards/entities/entities_home_dashboards_infrastructure_cluster_entities_dup.png" style="width: 70%; height: auto;">
      <figcaption><i>I~ Home » Dashboards > Infrastructure > K8s Cluster Entities | ENV | https://pro- n.dataos.app » | nodes Ally | Names...</i></figcaption>
    </div>
    

## Configure alerts for CPU usage

To automatically track the CPU usage, users can configure a Monitor and a Pager to send alerts when the CPU usage exceeds certain limits. This enables teams to respond immediately to resource failures that may impact dependent components. [Click here to view the steps to set up alerts for CPU usage](https://www.notion.so/Alerts-for-High-CPU-Usage-20fc5c1d48768026ada4e7dfa2a0f802?pvs=21).

## Configure alerts for memory usage

To automatically track the memory usage, users can configure a Monitor and a Pager to send alerts when the memory usage exceeds certain limits. This enables teams to respond immediately to resource failures that may impact dependent components. [Click here to view the steps to set up alerts for memory usage](https://www.notion.so/Alerts-for-High-Memory-Usage-20fc5c1d487680a4ba64f082a07857f3?pvs=21).
