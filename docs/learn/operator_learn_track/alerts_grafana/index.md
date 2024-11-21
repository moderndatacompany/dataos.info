# Configuring Alerts and Dashboards using Grafana

This topic details the steps to configure alerts for key performance indicators and troubleshooting performance issues.

## Scenario

Imagine you're responsible for ensuring the reliability of a critical application in DataOS. Your job is to monitor the system for any signs of issues, such as unexpected traffic spikes, high CPU usage, or incoming alerts that indicate something might be wrong. To do this effectively, you need a tool that lets you visualize what’s happening within your system in real-time.

## Grafana as observability tool

In DataOS, Grafana helps you track the health and performance of your systems by creating visual dashboards. Grafana gathers data from Prometheus, a monitoring system that collects time-series metrics (like CPU usage, memory consumption, or alert counts) about your infrastructure. This setup allows you to see trends, spot unusual patterns, and respond to issues before they impact users.



![image1.png](/learn/operator_learn_track/alerts_grafana/image1.png)

In the example shown, Grafana is displaying a dashboard that tracks ‘Total alerts received’ over the past six hours. This metric shows the number of alerts received by the alert manager, giving insights into potential issues. You can see a steady increase in alerts over time, represented by the green line.

With Grafana, you can customize these visualizations to suit your monitoring needs. You can filter by specific labels (such as the environment or container) and adjust the time range to focus on different periods. This flexibility helps you quickly diagnose issues, identify trends, and keep your systems running smoothly.

## Configure the Prometheus data source

<aside class="callout">
🗣 Prometheus is a system monitoring and alerting toolkit. It is used for collecting, storing, and analyzing metrics from various services and systems in real time.

</aside>

Follow the below steps to configure the Prometheus data source in Grafana.

1. Open the Grafana app.
    
    ![image2.png](/learn/operator_learn_track/alerts_grafana/image2.png)
    
2. Navigate to the connections section.
    
    ![image3.png](/learn/operator_learn_track/alerts_grafana/image3.png)
    
3. Search for the Prometheus.
    
    ![image4.png](/learn/operator_learn_track/alerts_grafana/image4.png)
    
4. On clicking the Prometheus data source, navigate to the ‘Add new data source’ button.
    
    ![image5.png](/learn/operator_learn_track/alerts_grafana/image5.png)
    
5. On clicking the ‘Add new data source’ button, you now here need to provide the name, Prometheus server URL, and authentication details for setting up the connection. Then click on the ‘save and test’ button.
    
    ![image6.png](/learn/operator_learn_track/alerts_grafana/image6.png)
    
6. Now you can create the dashboard.

## Create a Grafana dashboard

After successfully connecting to the Prometheus, now you can move into building the dashboard. This section provides a step-by-step walk through for creating dashboards.

**Before you begin**

- Ensure that you have the necessary tags to create the dashboard.
- Understand the query language (PromQL) of the target data source (Prometheus).

### **Steps to create a dashboard**

This section provides a step-by-step walk-through for creating dashboards.

1. Click Dashboards in the left-side menu.
    
    ![image7.png](/learn/operator_learn_track/alerts_grafana/image7.png)
    
2. Click New and select New Dashboard.
3. On the empty dashboard, click + Add visualization.
    
    ![image8.png](/learn/operator_learn_track/alerts_grafana/image8.png)
    
4. In the dialog box that opens, do one of the following:

    - Select one of your existing data sources.

    - Click Configure a new data source to set up a new one (Admins only).
    
    ![image9.png](/learn/operator_learn_track/alerts_grafana/image9.png)
    
    The Edit panel view will open when you select the data source. You can change the panel data source later using the drop-down in the Query tab of the panel editor if needed.
    
5. Write or construct a query in PromQL.
    
    ![image10.png](/learn/operator_learn_track/alerts_grafana/image10.png)
    
6. Click the Refresh dashboard icon to query the data source.


    <img src="/learn/operator_learn_track/alerts_grafana/image11.png" alt="image" style="width:20rem;" />

    
    
7. In the visualization list, select a visualization type.
    
    ![image12.png](/learn/operator_learn_track/alerts_grafana/image12.png)
    
    Grafana displays a preview of your query results with the visualization applied.
    
    For more information about individual visualizations, refer to [Visualizations options](https://grafana.com/docs/grafana/latest/panels-visualizations/visualizations/).
    
8. Under Panel options, enter a title and description for your panel.
9. After editing your panel, click Save to save the dashboard.
    
    Alternatively, click Apply to see your changes applied to the dashboard first. Then click the save icon in the dashboard header.
    
    For more information about panel editing, refer to [Panel Editing](https://www.notion.so/Panel-Editing-59b0d0ec8ed546baa732aa69b967f3ea?pvs=21).
    
10. Enter a title for your dashboard and select a folder.
11. Click Save.
12. To add more panels to the dashboard, click Add in the dashboard header and select Visualization in the drop-down.
    
    ![image13.png](/learn/operator_learn_track/alerts_grafana/image13.png)
    
    When you add additional panels to the dashboard, you’re taken straight to the Edit panel view.
    

To know more about managing the dashboards, refer to [Manage Dashboard](https://www.notion.so/Manage-Grafana-Dashboard-00701b8d4cc1474c94e98863c6166161?pvs=21).

## Explore the system metrics

Exploration in Grafana allows you to query data from connected data sources (Prometheus) and visualize it to monitor the metrics without creating dashboards. You can retrieve the metrics either by querying using PromQL in the Code view or by manually selecting the metrics and their labels in the Builder view.

### Builder View

Builder View is the default view in the Explore section. It allows you to build queries using a graphical interface interactively. Here's how to use it:

1. Click Explore in the left-side menu.
2. Choose the data source you want to query from the dropdown menu.
3. Use the query builder to select metrics, specify filters, and define aggregations.
4. Set the time range for your query.
5. View the results of your query in a tabular format.
6. Optionally, visualize your data using various chart types.

Builder View is great for exploring your data interactively and quickly creating queries without writing any code.

You can also explore the metrics, using Metrics Explorer.

![image14.png](/learn/operator_learn_track/alerts_grafana/image14.png)

### Code view

Code View allows you to write and execute queries directly using the query language supported by your data source such as Prometheus supports PromQL. 

![image15.png](/learn/operator_learn_track/alerts_grafana/image15.png)

Here's how to use it:

1. Click Explore in the left-side menu.
2. Choose the data source you want to query from the dropdown menu.
3. Write your query in the query editor using PromQL.
4. Set the time range for your query.
5. Click the Refresh icon to run the query.
6. View the results of your query in a tabular format.

Code View provides more flexibility and control over your queries, especially if you're familiar with the query language of your data source.

You can also manually select the metrics, labels, and values which will automatically generate the query in PromQL using the metrics browser.

![image16.png](/learn/operator_learn_track/alerts_grafana/image16.png)

## Set up Alerting

Alerting in Grafana allows you to define rules and conditions based on your data queries to trigger notifications or take actions when certain criteria are met. This section guides you to setting up and managing alerts within Grafana.

![image17.png](/learn/operator_learn_track/alerts_grafana/image17.png)

Before you begin Configure your Prometheus data source.

To set up Alerting, you need to:

1. **Configure alert rules**
    - Create Grafana-managed or Mimir/Loki-managed alert rules and recording rules.
        
        ![image18.png](/learn/operator_learn_track/alerts_grafana/image18.png)
        
2. **Configure contact points**
    - Check the default contact point and update the email address.
    - [Optional] Add new contact points and integrations.
        
        ![image19.png](/learn/operator_learn_track/alerts_grafana/image19.png)
        
    
    - To verify the contact points, click on the Test, which will send a test alert to the mentioned email.
3. **Configure notification policies**
    - Check the default notification policy.
        
        ![image20.png](/learn/operator_learn_track/alerts_grafana/image20.png)
        
    - [Optional] Add additional nested policies.
    - [Optional] Add labels and label Values to control alert routing.
        
        ![image21.png](/learn/operator_learn_track/alerts_grafana/image21.png)
        
4. **Connect alerts to the dashboard and panel**
    - Go to the existing alert rules, click on **Link dashboard and panel,** then select the dashboard and panels of your choice to link the alert.
    - After successfully linking the alert to the dashboard or panel, you can check the alert status directly on the dashboard or panel.
        
        ![image22.png](/learn/operator_learn_track/alerts_grafana/image22.png)
        
    
For more information on managing alerts, refer to [Manage Alerts](/learn/operator_learn_track/alerts_grafana/manage_alerts/).