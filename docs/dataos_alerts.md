# Event Monitoring and Alerting
DataOS, as a data operating system, provides robust observability and active monitoring for your data workloads. It's designed to offer real-time notifications about critical events impacting your business.

This page provides a comprehensive overview of the alert mechanisms integrated within DataOS, offering a range of routes to bolster your decision-making process and optimize efficiency. 

<!-- ## Dashboard Alerts

Dashboard alerts provide immediate notifications regarding significant changes or updates in your business performance metrics or other crucial dashboard data. To learn more, refer to [Setting Up Dashboard Alerts in Atlas](dataos_alerts/dashboard_alerts.md). -->

## Grafana Alerts

The DataOS Alerting mechanism with Grafana is designed to issue pre-set alerts based on specific resource usage parameters. The type of alerts Sentinel generates for your Kubernetes cluster is contingent upon the designated metrics and threshold values. Regular alerts include but are not limited to CPU Throttling Alert, and Kube API Server Error Budget Burn, among others. Regular inspection and adjustment of these configurations can facilitate the delivery of pertinent alerts, thereby aiding in maintaining the optimal health of your cluster.

Events within the Kubernetes ecosystem are indicative of potential disturbances concerning the performance, dependability, or steadiness of your applications and infrastructure. DataOS harnesses Kubernetes events to create a robust alert and monitoring system with Grafana. It also gives you the ability to create dashboards to comprehend the origins and impacts of these alerts. It is possible to preemptively pinpoint issues and employ suitable remedies to sustain the expected level of performance and reliability.

## Metis Alerts

Metis provides a comprehensive set of alerts and notifications mechanisms to notify users about any changes to metadata within the DataOS context. These alerts enable users to stay informed about the updates in their data assets, ensuring better data governance and control over the data lifecycle. To learn more, refer to [Metis Alerts](dataos_alerts/metis_alerts.md).  

## Metric Alerts

Metric alerts are tailored to monitor key performance indicators and other important metrics of your business. These alerts are triggered when predefined thresholds or benchmarks are exceeded or not met, providing a mechanism for timely intervention and corrective actions.

Leveraging DataOS's broad spectrum of alerts will enable you to maintain an informed, proactive stance on impactful business events, thereby enhancing operational efficiency and decision-making effectiveness. To learn more, refer to [Setting Up Metric Alerts](dataos_alerts/metric_alerts.md).

## Workflow Alerts

Workflow alerts are designed to monitor your running workflows and jobs continuously, notifying you instantly when a specific workflow encounters an issue or failure. These alerts act as safeguards, ensuring the smooth operation of your Workflow. To learn more, refer to [Setting Up Workflow Alerts](dataos_alerts/workflow_alerts.md).