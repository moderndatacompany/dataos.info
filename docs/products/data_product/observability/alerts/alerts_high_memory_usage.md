# Alerts for High Memory Usage

Whenever a DataOS Resource is created, it runs as a single pod in the underlying Kubernetes cluster. These pods inherit resource definitions such as CPU and memory limits or requests from the Resource configurations. Observability in this context is applied at the pod level by monitoring pod metrics, considering a single pod per Resource, which effectively helps in understanding the behavior and performance of the higher-level DataOS Resources that generated them.

## Memory limit breach

This section outlines how to configure both a Monitor Resource to observe memory usage at the pod level and a Pager Resource to send alerts when usage crosses a defined percentage of the pod’s total memory limit. This alert helps detect when a pod is approaching its maximum memory allocation, which could lead to OOM (Out Of Memory) kills or degraded performance.

1. Create a Monitor Resource manifest file. This manifest compares the total memory usage of the pod against its defined memory limit. An incident is triggered if usage exceeds 80% of the limit.
    
    ```yaml
    name: pod-memory-limit-monitor
    description: Monitor for memory usage of the pod perspectivedb-rest-yx2r-d-5b7bdb5648-p9tdr
    version: v1alpha
    type: monitor
    monitor:
      schedule: '*/2 * * * *'
      type: equation_monitor
      equation:
        leftExpression:
          queryCoefficient: 1
          queryConstant: 0
          query:
            type: prom
            ql: >
              sum by(pod) (
                container_memory_usage_bytes{pod="perspectivedb-rest-yx2r-d-5b7bdb5648-p9tdr"}
              )
              /
              sum by(pod) (
                kube_pod_container_resource_limits{pod="perspectivedb-rest-yx2r-d-5b7bdb5648-p9tdr", resource="memory"}
              )  
              
             # replace the pod name with actual pod name of the Resource 
    
        rightExpression:
          queryCoefficient: 1
          queryConstant: 0.8
          query:
            type: prom
            ql: 'scalar(1)'
        operator: greater_than
      incident:
        type: prom
        name: memory-limit-violation
        category: usage
        severity: high
    ```
    
    <aside class="callout">
    🗣️ Before applying the Monitor manifest, make sure to replace the placeholder pod name (`perspectivedb-rest-yx2r-d-5b7bdb5648-p9tdr`) in the PromQL query with the actual pod name of the Resource you want to monitor.
    </aside>
    
2. Validate the incident condition by executing the command below.
    
    ```bash
    dataos-ctl develop observability monitor equation -f /office/monitor/pod_memory_limit_monitor.yaml
    ```
    
    **Expected output when the condition is not met:**
    
    The pod’s memory usage is below 80% of the defined limit. No incident is triggered.
    
    ```bash
    INFO[0000] 🔮 develop observability...
    INFO[0000] 🔮 develop observability...monitor tcp-stream...starting
    INFO[0001] 🔮 develop observability...monitor tcp-stream...running
    INFO[0002] 🔮 develop observability...monitor tcp-stream...stopping
    INFO[0002] 🔮 context cancelled, monitor tcp-stream is closing.
    INFO[0003] 🔮 develop observability...complete
    
    RESULT (maxRows: 10, totalRows:0): 🟧 monitor condition not met
    ```
    
    **Expected output when the condition is met:**
    
    The pod's memory usage exceeds 80% of its limit. The monitor triggers an incident.
    
    ```bash
    INFO[0000] 🔮 develop observability...
    INFO[0000] 🔮 develop observability...monitor tcp-stream...starting
    INFO[0001] 🔮 develop observability...monitor tcp-stream...running
    INFO[0001] 🔮 develop observability...monitor tcp-stream...stopping
    INFO[0001] 🔮 context cancelled, monitor tcp-stream is closing.
    INFO[0002] 🔮 develop observability...complete
    
    RESULT (maxRows: 10, totalRows:1): 🟩 monitor condition met
    ```
    
3. Apply the Monitor using the command below.
    
    ```bash
    dataos-ctl resource apply -f pod-memory-limit-monitor.yaml
    ```
    
4. Verify the Monitor runtime to ensure it’s registered and running properly.
    
    ```bash
    dataos-ctl get runtime -t monitor -w <your-workspace> -n pod-memory-limit-monitor -r
    ```
    
5. Create a Pager Resource manifest file. This configures where and how alerts should be delivered when memory usage crosses the threshold.
    
    ```yaml
    name: pod-memory-limit-pager
    version: v1alpha
    type: pager
    description: Pager to alert when pod memory usage exceeds 80% of its defined memory limit
    workspace: <your-workspace>
    pager:
      conditions:
        - valueJqFilter: .properties.name
          operator: equals
          value: memory-limit-violation
      output:
        msTeams:
          webHookUrl: https://rubikdatasolutions.webhook.office.com/webhookb2/IncomingWebhook/92dcd2
        email:
          - iamgroot@tmdc.io  
    ```
    
6. Apply the Pager Resource using the command below.
    
    ```bash
    dataos-ctl resource apply -f pod-memory-limit-pager.yaml
    ```
    
7. Get notified! When the memory usage crosses the threshold, the incident is triggered, and the Pager sends the notification to the configured destination.

## Usage exceeds request

This section outlines how to configure a Monitor Resource to observe pod memory usage relative to its defined memory requests, and a Pager Resource to send alerts when usage crosses a defined percentage. This is useful for detecting pods that are exceeding their expected baseline allocation and may need to be scaled or reconfigured.

<aside class="callout">

💡 Note: While most DataOS Resources run one container per pod, in some cases, multiple containers are used. Monitoring memory at the pod level gives a more accurate picture of total consumption in such scenarios.

</aside>

1.  Create a Monitor Resource manifest file
    
    This manifest compares the total memory usage of the pod against the requested memory values. An incident is triggered if memory usage exceeds 80% of the total requested memory.
    
    ```yaml
    yaml
    CopyEdit
    name: pod-memory-request-monitor
    description: Monitor for memory usage of the pod perspectivedb-rest-yx2r-d-5b7bdb5648-p9tdr
    version: v1alpha
    type: monitor
    monitor:
      schedule: '*/2 * * * *'
      type: equation_monitor
      equation:
        leftExpression:
          queryCoefficient: 1
          queryConstant: 0
          query:
            type: prom
            ql: >
              sum by(pod) (
                container_memory_usage_bytes{pod="perspectivedb-rest-yx2r-d-5b7bdb5648-p9tdr"}
              )
              /
              sum by(pod) (
                kube_pod_container_resource_requests{pod="perspectivedb-rest-yx2r-d-5b7bdb5648-p9tdr", resource="memory"}
              )
        rightExpression:
          queryCoefficient: 1
          queryConstant: 0.8
          query:
            type: prom
            ql: 'scalar(1)'
        operator: greater_than
      incident:
        type: prom
        name: memory-request-violation
        category: usage
        severity: warning
    ```
    
    <aside class="callout">
    🗣️ Before applying the Monitor manifest, make sure to replace the placeholder pod name (`perspectivedb-rest-yx2r-d-5b7bdb5648-p9tdr`) in the PromQL query with the actual pod name of the Resource you want to monitor.
    </aside>
    
2. Validate the incident condition, run the following command to test whether the condition works before applying it.
    
    ```bash
    dataos-ctl develop observability monitor equation -f /office/monitor/pod_memory_request_monitor.yaml
    ```
    
    **Expected result when the condition is NOT met**:
    
    ```bash
    INFO[0000] 🔮 develop observability...
    INFO[0000] 🔮 develop observability...monitor tcp-stream...starting
    INFO[0001] 🔮 develop observability...monitor tcp-stream...running
    INFO[0002] 🔮 develop observability...monitor tcp-stream...stopping
    INFO[0002] 🔮 context cancelled, monitor tcp-stream is closing.
    INFO[0003] 🔮 develop observability...complete
    
    RESULT (maxRows: 10, totalRows:0): 🟧 monitor condition not met
    ```
    
    **Expected result when the condition is met**:
    
    ```bash
    INFO[0000] 🔮 develop observability...
    INFO[0000] 🔮 develop observability...monitor tcp-stream...starting
    INFO[0001] 🔮 develop observability...monitor tcp-stream...running
    INFO[0001] 🔮 develop observability...monitor tcp-stream...stopping
    INFO[0001] 🔮 context cancelled, monitor tcp-stream is closing.
    INFO[0002] 🔮 develop observability...complete
    
    RESULT (maxRows: 10, totalRows:1): 🟩 monitor condition met
    ```
    
3. Apply the Monitor Resource.
    
    ```bash
    dataos-ctl resource apply -f pod-memory-request-monitor.yaml
    ```
    
4. Verify the Monitor runtime.
    
    ```bash
    dataos-ctl get runtime -t monitor -w <your-workspace> -n pod-memory-request-monitor -r
    ```
    
5. Create a Pager Resource manifest.
    
    This Pager will listen for the memory request incident and send an alert to a Teams channel webhook and Outlook.
    
    ```yaml
    name: pod-memory-request-pager
    version: v1alpha
    type: pager
    description: Pager to alert when pod memory usage exceeds requested memory
    workspace: <your-workspace>
    pager:
      conditions:
        - valueJqFilter: .properties.name
          operator: equals
          value: memory-request-violation
      msTeams:
        webHookUrl: https://rubikdatasolutions.webhook.office.com/webhookb2/09239cd8-9d59-9621-9217305bf6e22bdde-3ec2-4392-78e9f35a44fb/IncomingWebhook/92dcd2acdaee4e6cac125ac4a729e48f/631bd149-c89d-4d3b-8979-8e364b419/V23AwNxCZx9fToWpqDSYeRkQefDZ-cPn74pY60
        email:
          - iamgroot@tmdc.io  
    ```
    
6. Apply the Pager Resource.
    
    ```bash
    dataos-ctl resource apply -f /home/pod-memory-request-pager.yaml
    ```
    
7. Get notified once memory usage exceeds 80% of the requested value, an incident is triggered, and an alert is sent to your configured destination.