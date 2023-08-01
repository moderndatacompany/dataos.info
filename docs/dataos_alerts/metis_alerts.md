# Metis Alerts

Metis in DataOS offers an alerts and notifications feature for informing users about metadata changes, ensuring better data governance and control. These alerts enhance observability empowering users to ensure the integrity and reliability of their data assets. 
 
Below are examples of metadata changes that trigger alerts.
1. Metadata Schema Change

Whenever there is a modification to the schema of a dataset in the Metis catalogue, an alert is triggered. It notifies users about changes to fields, data types, or any other alterations that could impact data compatibility or usage downstream.

2. Data Asset Ownership Change

Whenever ownership of a data asset is transferred or changed, an alert is activated. It ensures users are aware of who currently holds responsibility for managing the data, helping maintain accountability and access control.

3. Metadata Tag Change

If there are changes to the tags or labels assigned to a data asset, the alert is sent out. Tags play a crucial role in categorizing and organizing data, so this notification is crucial for ensuring proper data classification.

5. Data Asset Access Policy Change

This alert is generated whenever there are changes to the access policies or permissions associated with a specific data asset. Users are promptly notified of any updates to access controls, ensuring data security and compliance.

6. Data Asset Description Change

Whenever there is a change in the description or metadata documentation of a data asset, this alert is activated. Keeping users informed about modifications to data asset descriptions helps in better understanding and utilization of data.



## Event Notification via Webhooks
Metis allows you to integrate with tools such as Slack, Webhook, Microsoft Teams, etc., that receive all the data changes happening in your organization through APIs. This will generate organization-specific notifications when a change is made to data assets.
To configure event notifications to the registered webhooks, enter the following:
1. Webhook name and description
2. End Point URL to receive HTTP call back on.
3. Event filters to receive notifications for specific events of interest like when the metadata entity is created, updated or deleted.

[image](dataos_alerts/webhook.png)