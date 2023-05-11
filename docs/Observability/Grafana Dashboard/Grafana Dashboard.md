# Grafana Dashboard

## Features

Grafana provides you the tools to create insightful dashboards and enables you to query, visualize,  and explore your metrics, logs, and traces for the running DataOS context. 

You can use it to assess the health of Kubernetes clusters. It makes that data useful again by integrating all data sources into one single organized view.

Grafana provides the following features:

- Visualize: Grafana has a plethora of visualization options to help you understand your data, from graphs to histograms.
- Alerts: Grafana lets you define thresholds and create alerts, and get notified via Slack, PagerDuty, and more.
- Unify: You can bring your data together to get better context from multiple sources. In DataOS, the data is loaded from logs and *Prometheus.
(Prometheus is a monitoring and alerting software tool we use with Kubernetes. Grafana UI runs on top of Prometheus)*
- Open-Source: It’s completely open source. You can use Grafana Cloud, or easily install it on any platform.
- Explore Logs: You can quickly filter and search through the logs using label filters.
- Display dashboards: You can visualize data with templated or custom reports.

The dashboards can be created for the following:

- State of containers from Cluster.
- State of Pods from Cluster.
- State of Jobs from Cluster.
- Deployment and ReplicationController state of Cluster.
- Number of Nodes  and their state
- Network Activity by namespaces.
- CPU use in the cluster and CPU use in the cluster by namespaces.
- RAM memory used in the cluster, and RAM memory used in the cluster by namespaces.
- Total and used cluster resources: CPU, memory, filesystem. And total cluster network I/O pressure.
- Kubernetes pods usage: CPU, memory, network I/O.

## Search Dashboards

On Dashboard Home, click on the arrow.

<img src="Grafana%20Dashboard/Screen_Shot_2022-07-25_at_1.51.39_PM.png"
        alt="Picture"
        style="display: block; margin: auto" />

You will get the search option and the list of available dashboards. Enter the details or select a dashboard from the list.

<img src="Grafana%20Dashboard/Screen_Shot_2022-07-25_at_1.44.40_PM.png"
        alt="Picture"
        style="display: block; margin: auto" />

### Filter Dashboards

You can also search the dashboards by tags. Enter the tags or select from the list.

<img src="Grafana%20Dashboard/Screen_Shot_2022-07-25_at_3.37.40_PM.png"
        alt="Picture"
        style="display: block; margin: auto" />

## Example Dashboards

### Kubernetes Compute Resources for Cluster

<img src="Grafana%20Dashboard/Screen_Shot_2022-07-25_at_1.36.21_PM.png"
        alt="Picture"
        style="display: block; margin: auto" />

### Kubernetes Persistent Volumes

<img src="Grafana%20Dashboard/Screen_Shot_2022-07-25_at_2.01.50_PM.png"
        alt="Picture"
        style="display: block; margin: auto" />

### Kubernetes Compute Resources Namespace(Workloads)

<img src="Grafana%20Dashboard/Screen_Shot_2022-07-25_at_2.03.45_PM.png"
        alt="Picture"
        style="display: block; margin: auto" />

### Spark Operator

<img src="Grafana%20Dashboard/Screen_Shot_2022-07-25_at_1.32.10_PM.png"
        alt="Picture"
        style="display: block; margin: auto" />

### Metis

<img src="Grafana%20Dashboard/Screen_Shot_2022-07-25_at_1.41.28_PM.png"
        alt="Picture"
        style="display: block; margin: auto" />