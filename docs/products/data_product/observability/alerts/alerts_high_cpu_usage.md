# Alerts for High CPU Usage

Whenever a DataOS Resource is created, it runs as a single pod in the underlying Kubernetes cluster. These pods inherit resource definitions such as CPU and memory limits or requests from the Resource configurations. Observability in this context is applied at the pod level by monitoring pod metrics, considering a single pod per Resource, and this effectively helps in understanding the behavior and performance of the higher-level DataOS Resources that generated them.

## CPU limit breach

This section outlines how to configure both a Monitor Resource to observe the incident condition and a Pager Resource to send alerts when the condition is met. This type of alert is useful when CPU limits are configured for the Resource. Exceeding the CPU limit can lead to throttling, affecting the Resource's performance. This alert helps in proactively detecting such behavior.

1. Execute the following command in DataOS CLI to get the pod name corresponding to the Resource that needs to be monitored.
    
    ```bash
    dataos-ctl log -t ${{resource-type}} -n ${{resource-name}}
    ```
    
    **Example usage:**
    
    ```bash
    dataos-ctl log -t service -n perspectivedb-rest
    # output
    INFO[0000] 📃 log(public)...                             
    INFO[0001] 📃 log(public)...complete                     
    
        NODE NAME    │ CONTAINER NAME │ ERROR  
    ─────────────────┼────────────────┼────────
      perspectivedb-rest-yx2r-d-5b7bdb5648-p9tdr │ perspectivedb-rest     │        
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
    
2. Create a Monitor Resource manifest file as example below and replace the pod name with the pod name of the Resource which you want to monitor. This manifest defines the logic for comparing actual CPU usage against the pod's total CPU limit. The incident will be triggered if usage exceeds 80% of the limit.
    
    ```yaml
    name: cpu-monitor
    description: Monitor for CPU usage of the perspectivedb-rest container
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
            ql: '100 * (sum by(pod) (rate(container_cpu_usage_seconds_total{pod="perspectivedb-rest-yx2r-d-5b7bdb5648-p9tdr"}[5m])))/sum by(pod) (kube_pod_container_resource_limits{pod="perspectivedb-rest-yx2r-d-5b7bdb5648-p9tdr", resource="cpu"})'
    
        rightExpression:
          queryCoefficient: 0
          queryConstant: 80
        operator: greater_than
      incident:
        type: prom
        name: cpualerts
        category: equation
        severity: info
        operator: greater_than
    ```
    
    <aside class="callout">
    🗣️ Before applying the Monitor manifest, make sure to replace the placeholder pod name (`perspectivedb-rest-yx2r-d-5b7bdb5648-p9tdr`) in the PromQL query with the actual pod name of the Resource you want to monitor.
    </aside>
    
3. Validate the incident condition if it is configured correctly by executing the command below.
    
    ```bash
    dataos-ctl develop observability monitor equation -f /office/monitor/pod_cpu_limit_monitor.yaml
    ```
    
    **Expected output when the condition is not met:**
    
    The monitor ran successfully, but CPU usage was below 80% of the pod's limit. No incident is triggered.
    
    ```bash
    bash
    CopyEdit
    INFO[0000] 🔮 develop observability...
    INFO[0000] 🔮 develop observability...monitor tcp-stream...starting
    INFO[0001] 🔮 develop observability...monitor tcp-stream...running
    INFO[0002] 🔮 develop observability...monitor tcp-stream...stopping
    INFO[0002] 🔮 context cancelled, monitor tcp-stream is closing.
    INFO[0003] 🔮 develop observability...complete
    
    RESULT (maxRows: 10, totalRows:0): 🟧 monitor condition not met
    ```
    
    **Expected output when the condition is met:**
    
    The pod's CPU usage exceeded 80% of its CPU limit. The monitor triggered an incident.
    
    ```bash
    bash
    CopyEdit
    INFO[0000] 🔮 develop observability...
    INFO[0000] 🔮 develop observability...monitor tcp-stream...starting
    INFO[0001] 🔮 develop observability...monitor tcp-stream...running
    INFO[0001] 🔮 develop observability...monitor tcp-stream...stopping
    INFO[0001] 🔮 context cancelled, monitor tcp-stream is closing.
    INFO[0002] 🔮 develop observability...complete
    
    RESULT (maxRows: 10, totalRows:1): 🟩 monitor condition met
    ```
    
4. Run the following command to apply the Monitor.
    
    ```bash
    dataos-ctl resource apply -f pod-cpu-limit-monitor.yaml
    ```
    
5. Verify the Monitor runtime. This step ensures that the Monitor has been successfully registered and is running as expected.
    
    ```bash
    dataos-ctl get runtime -t monitor -w <your-workspace> -n pod-cpu-limit-monitor -r
    ```
    
6. Create a Pager Resource manifest file. This manifest configures the alert delivery path. It listens for the incident triggered by the Monitor and sends the alert to a Teams channel or any other webhook.
    
    ```yaml
    name: pod-cpu-limit-pager
    version: v1alpha
    type: pager
    description: Pager to alert when pod CPU usage exceeds 80% of its defined CPU limit
    workspace: <your-workspace>
    pager:
      conditions:
        - valueJqFilter: .properties.name
          operator: equals
          value: cpu-limit-violation
      output:
        msTeams:
          webHookUrl: https://rubikdatasolutions.webhook.office.com/webhookb2/09239cd8-9d59-9621-9217305bf6e22bdde-3ec2-4392-78e9f35a44fb/IncomingWebhook/92dcd2acdaee4e6cac125ac4a729e48f/631bd149-c89d-4d3b-8979-8e364b419/V23AwNxCZx9fToWpqDSYeRkQefDZ-cPn74pY60
        email:
          emailTargets:
            - iamgroot@tmdc.io  
    ```
    
7. Once defined, apply the Pager Resource using the command below.
    
    ```bash
    dataos-ctl resource apply -f pod-cpu-limit-pager.yaml
    ```
    
8. Get notified! When the CPU usage condition is met, the incident is triggered, and the Pager sends the notification to the configured destination.

## Usage exceeds request

This section outlines how to configure both a Monitor Resource to observe the incident condition and a Pager Resource to send alerts when the condition is met. This alert is useful when a pod consumes more CPU than what was originally requested, indicating possible scheduling pressure or a need to adjust resource allocation.

1. Create a Monitor Resource manifest file. This manifest defines the logic for comparing the total CPU usage of the pod against its total requested CPU. The incident will be triggered if usage exceeds 80% of the requested amount.
    
    ```yaml
    name: cpu-monitor
    description: Monitor for CPU usage of the nilus-server container
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
            ql: '100 * (sum by(pod) (rate(container_cpu_usage_seconds_total{pod="perspectivedb-rest-yx2r-d-5b7bdb5648-p9tdr"}[5m])))/sum by(pod) (kube_pod_container_resource_requests{pod="perspectivedb-rest-yx2r-d-5b7bdb5648-p9tdr", resource="cpu"})'
    
        rightExpression:
          queryCoefficient: 0
          queryConstant: 80
        operator: greater_than
      incident:
        type: prom
        name: cpualerts
        category: equation
        severity: info
        operator: greater_than
    ```
    
    <aside class="callout">
    🗣️ Before applying the Monitor manifest, make sure to replace the placeholder pod name (`perspectivedb-rest-yx2r-d-5b7bdb5648-p9tdr`) in the PromQL query with the actual pod name of the Resource you want to monitor.
    </aside>
    
2. Validate the incident condition if it is configured correctly by executing the command below.
    
    ```bash
    dataos-ctl develop observability monitor equation -f /office/monitor/pod_cpu_request_monitor.yaml
    ```
    
    **Expected output when the condition is not met:**
    
    The monitor runs successfully, but the CPU usage is below 80% of the pod’s request. No incident is triggered.
    
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
    
    CPU usage crossed 80% of the total CPU requested for the pod. An incident is triggered.
    
    ```bash
    INFO[0000] 🔮 develop observability...
    INFO[0000] 🔮 develop observability...monitor tcp-stream...starting
    INFO[0001] 🔮 develop observability...monitor tcp-stream...running
    INFO[0001] 🔮 develop observability...monitor tcp-stream...stopping
    INFO[0001] 🔮 context cancelled, monitor tcp-stream is closing.
    INFO[0002] 🔮 develop observability...complete
    
    RESULT (maxRows: 10, totalRows:1): 🟩 monitor condition met
    ```
    
3. Run the following command to apply the Monitor.
    
    ```bash
    dataos-ctl resource apply -f pod-cpu-request-monitor.yaml
    ```
    
4. Verify the Monitor runtime. This step ensures that the Monitor has been successfully registered and is running as expected.
    
    ```bash
    dataos-ctl get runtime -t monitor -w <your-workspace> -n pod-cpu-request-monitor -r
    ```
    
5. Create a Pager Resource manifest file. This manifest configures the alert delivery path. It listens for the incident triggered by the Monitor and sends the alert to a Teams channel or any other webhook.
    
    ```yaml
    name: pod-cpu-request-pager
    version: v1alpha
    type: pager
    description: Pager to alert when pod CPU usage exceeds 80% of its requested CPU
    workspace: <your-workspace>
    pager:
      conditions:
        - valueJqFilter: .properties.name
          operator: equals
          value: cpu-request-violation
      output:
        msTeams:
          webHookUrl: https://rubikdatasolutions.webhook.office.com/webhookb2/09239cd8-9d59-9621-9217305bf6e22bdde-3ec2-4392-78e9f35a44fb/IncomingWebhook/92dcd2acdaee4e6cac125ac4a729e48f/631bd149-c89d-4d3b-8979-8e364b419/V23AwNxCZx9fToWpqDSYeRkQefDZ-cPn74pY60
        email:
          emailTargets:
            - iamgroot@tmdc.io  
    ```
    
6. Once defined, apply the Pager Resource using the command below.
    
    ```bash
    dataos-ctl resource apply -f pod-cpu-request-pager.yaml
    ```
    
7. Get notified! When the CPU usage condition is met, the incident is triggered, and the Pager sends the notification to the configured destination.
