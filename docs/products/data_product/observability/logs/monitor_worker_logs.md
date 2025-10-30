# Monitor the Logs of a Worker

This section involves the steps to observe the logs of the Worker on different endpoints such as DataOS CLI, Metis UI, and Operations App.

<aside class="callout">
🗣 The logs of a Workflow consist of two types:
<ul>
  <li><b><code>init</code> Logs</b>: These are the logs from the init container, which runs before the main container starts. In Worker, it often handles preparation tasks, such as loading artifacts or mounting volumes. If something fails here, the main logic won’t even start.</li>
  <li><b><code>main</code> Logs</b>: These are from the primary container, where the actual workload or execution logic runs. This is where the core of the Worker pipeline executes, and most application-level logs will appear.</li>
</ul>
</aside>


## DataOS CLI

To monitor the  logs of a Worker using DataOS CLI, follow the steps below:

1. On DataOS CLI, execute the following command by replacing the placeholders with the actual values. 
    
    ```bash
    dataos-ctl log -t worker -w ${{workspace-name}} -n ${{workflow-name}}
    ```
    
    **Example Usage:**
        
    ```bash
    dataos-ctl log -t worker -w public -n textile-insights-worker
    INFO[0000] 📃 log(public)...                             
    INFO[0001] 📃 log(public)...complete                     
    
                  NODE NAME             │     CONTAINER NAME      │ ERROR  
    ────────────────────────────────────┼─────────────────────────┼────────
      textile-insights-worker-gqjk-ss-0 │ textile-insights-worker │        
    
    -------------------LOGS-------------------
    🚀 Lens2 (0.35.60-20) => DataOS:dataos-training.dataos.app
    DEBUG: Configured time-zones: [
      "America/Toronto",
      "America/Vancouver",
      "UTC"
    ]
    DEBUG: source: {
      "type": "flash",
      "dialect": "duckdb",
      "connection": "flash",
      "meta": {
        "userId": "abhishekgupta",
        "host": "textile-flash.public.svc.cluster.local",
        "port": 5433
      }
    }
    DEBUG: 🧑‍🤝‍🧑 /etc/dataos/work/dp-automation/demo_1/textile-analytics/data-product/consumer-aligned/build/semantic-model-view/model/user_groups.yml => [
      {
        "name": "default",
        "description": "Administrators with full access to textile analytics data product",
        "includes": "*",
        "api_scopes": [
          "meta",
          "data",
          "graphql",
          "jobs",
          "source"
        ],
        "allow_private_members_access": false
      }
    ]

    
    ```
        

## Metis UI

To monitor the logs of a Worker on the Metis Catalog UI, follow the steps below:

1. Open the Metis Catalog.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/logs/worker/image%20(20).png" style="border:1px solid black; width: 70%; height: auto">
    <figcaption><i>Open the Metis Catalog</i></figcaption>
    </div>
    
2. Search for the Worker by name.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/logs/worker/image%20(21).png" style="border:1px solid black; width: 70%; height: auto">
    <figcaption><i>Search the Worker in Metis</i></figcaption>
    </div>
    
3. Click on the Worker that needs to be monitored and navigate to the ‘Runtime’ section.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/logs/worker/image%20(22).png" style="border:1px solid black; width: 70%; height: auto">
    <figcaption><i>Worker runtime in Metis</i></figcaption>
    </div>
    
4. Click on any pod name for which you want to monitor the logs, and navigate to the ‘Pod Logs’ section.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/logs/worker/image%20(23).png" style="border:1px solid black; width: 70%; height: auto">
    <figcaption><i>Pod Logs in Metis</i></figcaption>
    </div>
    

## Operations App

<aside class="callout">
🗣
Logs for a Worker are available on the Operations App only while the Worker is still in progress (e.g., in a `scheduled` or `running` state). Once the Worker succeeds or fails to execute, its logs are no longer visible in Operations. To access logs after completion, refer to the Metis UI or DataOS CLI, which retains historical logs.
</aside>

To monitor the logs of a Worker on the Operations App, follow the steps below:

1. Open the Operations app.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/logs/worker/image%20(24).png" style="border:1px solid black; width: 70%; height: auto">
    <figcaption><i>Open the Operations app</i></figcaption>
    </div>
    
2. Navigate to User Space → Resources → Worker and search for the Worker by name.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/logs/worker/image%20(25).png" style="border:1px solid black; width: 70%; height: auto">
    <figcaption><i>Operations > Resources > Worker</i></figcaption>
    </div>
    
3. Click on the Worker that needs to be monitored and navigate to the ‘Resource Runtime’ section.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/logs/worker/image%20(26).png" style="border:1px solid black; width: 70%; height: auto">
    <figcaption><i>Worker resource runtime in Operations</i></figcaption>
    </div>
    
4. Click on any runtime node for which you want to monitor the logs, and navigate to the ‘Runtime Node Logs’ section. Here, users can monitor the init container and main container logs.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/logs/worker/image%20(27).png" style="border:1px solid black; width: 70%; height: auto">
    <figcaption><i>Runtime Node Logs in Operations</i></figcaption>
    </div>
