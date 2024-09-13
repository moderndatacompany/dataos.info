---
title: Exploration of Lens using Iris Board
search: 
  exclude: true
---
<!-- 
# Exploration of Lens using Iris Board

Iris serves as an operational dashboard, providing a swift overview of your key performance metrics(measures) over time. It enables you to delve deeper into these metrics(measures) across various dimensions, aiding in the understanding of anomalies or observed differences. You can expose your Lens View to Iris boards, allowing you to observe measures across various dimensions defined within it.

For instance the following ‘wallet_sales_view’ iris board shows weekly performance of revenue and wallet share

<div style="text-align: center;">
    <img src="/resources/lens/consumption_of_deployed_lens/iris/iris_board.png" alt="Iris board" style="max-width: 80%; height: auto; border: 1px solid #000;">
    <figcaption> wallet_sales_view View in Iris Board</figcaption>
</div>

## Working with Iris board?

You can create operational boards powered by Lens Views for streamlined operations. 

### **Step 1: Add the following detail in View’s YAML within the meta section**

```yaml
views:
  - name: #name of the view 
    description: #description of the view
    public: #ensure this property is set as 'true', so that it is accessible for the consumer
    #Here you can define whether you want this view to be exported to the IRIS board
    meta:
      export_to_iris: true
      timezones: # come from lens meta
      iris:
        timeseries: process_event.process_file_modified_date
```

<aside class="callout">
💡 When working with the Iris board, make sure that the measures displayed in the view also include their dependent dimensions.

</aside>

### **Step 2: Deploy Lens**

You can learn more about deploying Lens [here](/resources/lens/lens_deployment/)

### **Step 3: Access the IRIS board for your Lens**

As of now, you can view the IRIS board on the following URL:

=== "URL Syntax"

    ```yaml

    <DataOS env-link>/lens2/iris/<workspace>:<lens_name>

    #<DataOS env-link>:  Add the link of DataOS env, where you have deployed your Lens
    #<workspace> example public, sandbox etc.
    # <lens_name>: Name of the deployed Lens 
    ```

=== "Example"

    ```yaml
    [https://emerging-hawk.dataos.app/lens2/iris/public:sales360](https://emerging-hawk.dataos.app/lens2/iris/public:sales360/source/account_source)
    ```

Alternatively, you can navigate through the following steps:

- Go to the **DataOS Home Page**.
- Click on **Metis**.
- Access the **Resources** section.
- Select the **Lens** resource.
- Locate your deployed Lens and click on it.
- You will find the **Iris** link button—click it to view your View in Iris Board. -->