# Setting Up Dashboard Alerts

This guide will walk you through the process of creating custom dashboard alerts. To stay updated with daily metrics such as sales, stock, revenue, orders, and operating costs. DataOS provides numerous alert options, including Email, Slack, Webhook, Mattermost, Chatworks, and Pagerduty.

## Step 1: Query from Workbench

From the DataOS home page, navigate to the Workbench. Select the appropriate Catalog, Schema, and Table. Then, write an SQL query to extract the data you want to display on your dashboard.

![image](dashboard_alerts/query_workbench.png)

## Step 2: Export to Atlas

Once you've obtained the required output from the SQL query, click on the ellipsis (three dots) to export your results to Atlas.

![image](dashboard_alerts/export.png)

## Step 3: Add Visualization

Click on the 'Add Visualization' button.

![image](dashboard_alerts/add_visualization.png)

Edit the visualization as needed and save your changes.

![image](dashboard_alerts/save.png)

## Step 4: Create Alerts

To set up alerts, select the interval at which you want to be alerted and click 'Alerts'.

![image](dashboard_alerts/create_alert.png)

Customize the alert settings as per your requirements and click 'Next'. You can now select the individuals to be notified.

![image](dashboard_alerts/notify.png)

In the following screen, add the destinations for your alerts and further customize them as needed.

![image](dashboard_alerts/destinations.png)

The system will check the conditions at fixed intervals. If any conditions are met, the query status will be set to 'TRIGGERED', and the designated contacts will be alerted.

![image](dashboard_alerts/trigger.png)

## Alert Example

By following these steps, you have successfully set up customized alerts for your dashboard. These alerts will ensure you and your team are promptly informed when important changes occur, allowing for immediate action.

![Untitled](dashboard_alerts/example.png)

 