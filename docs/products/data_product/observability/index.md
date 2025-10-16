# Observability

This documentation provides a comprehensive guide that explains how to set up and use Observability in DataOS to keep track of how different Resources are working. It helps users understand how to monitor performance, check system health, and get alerts when something goes wrong with the Resources used to build the Data Products. Each section focuses on a specific layer, monitoring, logging, and alerting, and includes instructions, usage examples, and pre-built dashboard integrations.

<div style="text-align: center;">
  <img src="/products/data_product/observability/observability.png" style="width: 70%; height: auto;">
  <figcaption><i>Observability in DataOS</i></figcaption>
</div>

## Key Concepts

This section introduces the key concepts that power monitoring, logging, alerting, and analysis of observability data in DataOS. Understanding these concepts will help users better track Resource health, investigate issues, and design effective observability setups across different DataOS Resources.

[Key Concepts of Observability](/products/data_product/observability/key_concepts/)

## Monitoring

Monitoring in DataOS helps users track the health, performance, and behavior of system components using collected metrics. It allows users to detect trends, identify issues early, get alerts, and understand how different resources are running over time.

### **View the health of the Resources**

This section describes how users can view the [status](/products/data_product/observability/key_concepts/#status) and [runtime](/products/data_product/observability/key_concepts/#runtime) of DataOS Resources through the DataOS CLI, Metis UI, or Operations App. 

<aside class="callout">
🗣 Monitoring the status of a static (non-runnable) Resource is most helpful when that Resource depends on other runnable Resources such as Workflows or Services. 
</aside>

- [Monitor the status of Instance Secret](/products/data_product/observability/status/monitor_instance_secret/)
- [Monitor the status of Secrets](/products/data_product/observability/status/monitor_secrets/)
- [Monitor the Status of Volume](/products/data_product/observability/status/monitor_volume/)
- [Monitor the Status of Lakehouse](/products/data_product/observability/status/monitor_lakehouse/)
- [Monitor the Status and Runtime of the Depot](/products/data_product/observability/status/monitor_depot/)
- [Monitor the Status and Runtime of the Workflow](/products/data_product/observability/status/monitor_workflow/)
- [Monitor the Status and Runtime of the Cluster](/products/data_product/observability/status/monitor_cluster/)
- [Monitor the Status and Runtime of the Service](/products/data_product/observability/status/monitor_service/)
- [Monitor the Status and Runtime of the Worker](/products/data_product/observability/status/monitor_worker/)
- [Monitor the Status and Runtime of the Lens](/products/data_product/observability/status/monitor_lens/)
- [Monitor the Status of the Compute](/products/data_product/observability/status/monitor_compute/)
- [Monitor the Status of the Bundle](/products/data_product/observability/status/monitor_bundle/)

### **Monitor the CPU and memory usage of the Resources**

This section outlines how users can track CPU and memory usage across various DataOS Resources such as Workflows, Clusters, Services, Workers, and Lenses. It highlights multiple ways to observe these metrics using tools like Grafana, Metis UI, and the Operations App. Monitoring resource consumption helps teams ensure performance, detect bottlenecks, and optimize workloads effectively.

- [Monitor the CPU and memory usage of a Workflow](/products/data_product/observability/cpu/monitor_workflow_cpu_memory/)
- [Monitor the CPU and memory usage of a Cluster](/products/data_product/observability/cpu/monitor_cluster_cpu_memory/)
- [Monitor the CPU and memory usage of a Service](/products/data_product/observability/cpu/monitor_service_cpu_memory/)
- [Monitor the CPU and memory usage of a Worker](/products/data_product/observability/cpu/monitor_worker_cpu_memory/)
- [Monitor the CPU and memory usage of a Lens](/products/data_product/observability/cpu/monitor_lens_cpu_memory/)
- [Monitor the CPU and memory usage of a Depot](/products/data_product/observability/cpu/monitor_depot_cpu_memory/)

### **Explore system metrics through Grafana dashboards**

System metrics for DataOS Resources can be explored through Grafana dashboards. These dashboards offer detailed insights into CPU, memory, and runtime behavior across clusters, pods, and services. Users can navigate these dashboards to quickly assess resource health, analyze trends, and troubleshoot issues using visual cues.

- [K8 Cluster Infrastructure Dashboard](/products/data_product/observability/dashboards/k8_cluster_infrastructure_dashboard/)
- [K8 Cluster Entities Dashboard](/products/data_product/observability/dashboards/k8_cluster_entities_dashboard/)

## Logging

This section focuses on how users can explore and analyze logs generated by various DataOS Resources such as Workflows, Clusters, Services, and more. Logs help in understanding execution details, identifying errors, and troubleshooting issues. Users can access logs through the CLI, Metis UI, Grafana, or the Operations App, depending on the Resource type and preferred interface.

- [Monitor the logs of a Workflow](/products/data_product/observability/logs/monitor_workflow_logs/)
- [Monitor the logs of a Cluster](/products/data_product/observability/logs/monitor_cluster_logs/)
- [Monitor the logs of a Service](/products/data_product/observability/logs/monitor_service_logs/)
- [Monitor the logs of a Worker](/products/data_product/observability/logs/monitor_worker_logs/)
- [Monitor the logs of a Lens](/products/data_product/observability/logs/lens/)
- [Monitor the logs of a Depot](/products/data_product/observability/logs/depot/)

## Alerting

This section explains how alerts are set up when issues occur in DataOS Resources. By using Monitor and Pager Resources, users can define conditions for incidents and configure notifications for channels like email, Microsoft Teams, or webhooks. This enables faster response to failures, improves system reliability, and supports proactive monitoring.

### **Set Up Alerts for High CPU Usage**

This section explains how users can configure alerts when the CPU usage of a Resource exceeds a defined threshold. Monitoring CPU consumption helps teams detect performance bottlenecks early and prevent resource exhaustion.

[Alerts for High CPU Usage](/products/data_product/observability/alerts/alerts_high_cpu_usage/)

### **Set Up Alerts for High Memory Usage**

This section shows how to set alerts for cases where memory usage crosses safe operational limits. By observing memory trends and configuring alerts, users can identify memory leaks, optimize workloads, and avoid service crashes or slowdowns.

[Alerts for High Memory Usage](/products/data_product/observability/alerts/alerts_high_memory_usage/)

### **Set Up Alerts for Runtime Failure**

This section describes how to detect when a Resource fails to complete successfully. Users can configure monitors to trigger alerts on specific failure statuses, enabling faster response and recovery from disruptions.

[Alerts for Resource Runtime Failure](/products/data_product/observability/alerts/alerts_runtime_failure/)

### **Set Up Alerts for Resource Status**

This section guides users on how to monitor the operational status of DataOS Resources. It includes steps to configure alerts for conditions like inactive or stalled components, helping teams stay aware of changes in system behavior and availability.

[Alerts for Resource Status Change](/products/data_product/observability/alerts/alerts_resource_status_change/)

## Observing Data Product Metrics

This section provides step-by-step instructions to observe a [Data Product](https://dataos.info/products/data_product/) in DataOS, so users can continuously monitor core business KPIs to receive immediate alerts when those metrics degrade and route incidents to the Teams channel or email.

[Observability for Data Product Metrics](/products/data_product/observability/data-product-metrics/)

## Use cases

This section describes a real-world example of how users handle alerts in DataOS. 

[Observability Use Case](/products/data_product/observability/usecase/)

## FAQs

1. **How do we decide the CPU request and limit for a Resource?**
    
    Set the CPU request based on the minimum expected usage under normal load, ensuring stable scheduling. For critical Resources that should never fail, avoid setting CPU limits entirely. If uncertain about requirements, start without limits and observe actual usage patterns. Once you have reasonable assumptions about CPU needs from testing and observation, you can define appropriate limits if necessary. There is no precise way for determining accurate limits; continuous monitoring via the Operations App helps establish optimal configurations.
    
2. **What happens when the DataOS Resources hit CPU limits?**
    
    When a Resource exceeds its CPU limit, workloads begin to fail or become unresponsive. This can cause job timeouts, degraded performance, and alert triggers if configured. Immediate remediation involves raising the limit in the YAML config and reapplying the Resource.
    
3. **How do I get alerted when a DataOS Resource crosses its resource limits?**
    
    You must configure a Monitor Resource with threshold-based conditions (e.g., CPU usage > 80%) and associate it with a Pager Resource that sends alerts to Teams or other endpoints. The alert condition uses a Prometheus expression to evaluate usage and push incidents to the Pager.
    
4. **How do I debug if I didn't receive an alert?**
    
    Check:
    
    - The condition logic in the Monitor.
    - The Pager filter `.valueJqFilter` and `value`.
    - The logs of the Pager API pod in the Operations App.
    
    Use `dataos-ctl resource get -t pager` to verify deployment.
    
5. **Can I send alerts to both Teams and Email?**
    
    Yes. In the `pager.output` section of the manifest includes both `emailTargets` and `msTeams.webHookUrl` as shown below. The same incident can trigger notifications across all configured channels.
    
    ```yaml
    version: v1alpha
    type: pager
    description: Hurry up! mycluster CPU usage have reached the 80% of its limits
    workspace: public
    pager:
      conditions:
        - valueJqFilter: .properties.name
          operator: equals
          value: cpualerts
      output:
        msTeams:
          webHookUrl: https://rubikdatasolutions.webhook.office.com/webhookb2/092-92a8-4d59-9621-9217305bf6ed@2e22bdde-3ec2-43f5-bf92-78e9f35a44fb/IncomingWebhook/92dcd2acdac129e48f/631bd149-c8d3b-8979-8e364f62b419/V23AwNxCZx9JkwfToWpqDSYeRkQefDZ-cPn74pY601
        email:
          - iamgroot@tmdc.io 
    ```
    
6. **How do I test my alert before production?**
    
    Use a test Monitor with safe dummy thresholds and a Pager pointed to a test Teams channel or email. Use `dataos-ctl resource apply -f monitor.yaml` to deploy and simulate metric spikes if needed.
    
7. **How do I query resource usage in real time?**
    
    Use Grafana dashboards backed by Prometheus/Thanos data sources. Panels like CPU Usage, Memory Pressure, and Disk Utilization provide real-time insight. You can also execute PromQL queries directly to validate thresholds.
