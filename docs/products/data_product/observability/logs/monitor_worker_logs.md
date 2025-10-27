# Monitor the Logs of a Worker

This section involves the steps to observe the logs of the Worker on different endpoints such as DataOS CLI, Metis UI, and Operations App.

<aside class="callout">
🗣
- <b>Init Container Logs</b>: These are the logs from the init container, which runs before the main container starts. In workflows, it often handles preparation tasks, such as loading artifacts or mounting volumes. If something fails here, the main logic won’t even start.
- <b>Container Logs</b>: These are from the primary container, where the actual workload or execution logic runs. This is where the core of the Worker pipeline executes, and most application-level logs will appear.
</aside>

## Monitor the logs of a Worker using DataOS CLI

To monitor the  logs of a Worker using DataOS CLI, follow the steps below:

1. On DataOS CLI, execute the following command by replacing the placeholders with the actual values. 
    
    ```bash
    dataos-ctl log -t worker -w ${{workspace-name}} -n ${{workflow-name}}
    ```
    
    **Example Usage:**
    
    - **Example Usage**
        
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
        DEBUG: /etc/dataos/work/dp-automation/demo_1/textile-analytics/data-product/consumer-aligned/build/semantic-model-view/model/sqls/inventory_view.sql:205:1749852016065.9807
        DEBUG: /etc/dataos/work/dp-automation/demo_1/textile-analytics/data-product/consumer-aligned/build/semantic-model-view/model/sqls/production_view.sql:242:1749852016065.9807
        DEBUG: /etc/dataos/work/dp-automation/demo_1/textile-analytics/data-product/consumer-aligned/build/semantic-model-view/model/sqls/sales_view.sql:232:1749852016065.9807
        DEBUG: /etc/dataos/work/dp-automation/demo_1/textile-analytics/data-product/consumer-aligned/build/semantic-model-view/model/tables/inventory_view.yml:2220:1749852016065.9807
        DEBUG: /etc/dataos/work/dp-automation/demo_1/textile-analytics/data-product/consumer-aligned/build/semantic-model-view/model/tables/production_view.yml:2918:1749852016065.9807
        DEBUG: /etc/dataos/work/dp-automation/demo_1/textile-analytics/data-product/consumer-aligned/build/semantic-model-view/model/tables/sales_view.yml:2491:1749852016065.9807
        DEBUG: ENV ->  ROUTER_TELEMETRY : false
        DEBUG: ENV ->  ROUTER_WORKERS : textile-insights-worker-gqjk-ss-0.textile-insights-worker.public.svc.cluster.local:10001
        DEBUG: ENV ->  ROUTER_WORKER_PORT : 10001
        DEBUG: ENV ->  RUNNABLE_ARTIFACT_DIR : /etc/dataos/work
        DEBUG: ENV ->  RUNNABLE_TYPE : worker
        DEBUG: ENV ->  RUST_BACKTRACE : true
        DEBUG: ENV ->  SCS_SERVICE_URL : https://stack-exec-context-sink.poros.svc.cluster.local:39100/sink
        DEBUG: ENV ->  STORE_INTERNAL_URL : http://stores-api.caretaker.svc.cluster.local:8891/stores
        DEBUG: ENV ->  STORE_SERVICE_SSL_ENABLED : false
        DEBUG: ENV ->  STORE_SERVICE_SSL_HOSTNAME_VERIFICATION : false
        DEBUG: ENV ->  STORE_SERVICE_URL_PATH : /api/v1
        DEBUG: ENV ->  STORE_URL : https://dataos-training.dataos.app/stores
        DEBUG: ENV ->  TERM : rxvt-unicode
        DEBUG: ENV ->  YARN_VERSION : 1.22.19
        args:  [ 'router' ] , cwd:  /etc/dataos/work
        
        ```
        

## Monitor the logs of a Worker using Metis UI

To monitor the logs of a Worker on the Metis Catalog UI, follow the steps below:

1. Open the Metis Catalog.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/observability.png" style="width: 70%; height: auto;">
    </div>
    
2. Search for the Worker by name.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/observability.png" style="width: 70%; height: auto;">
    </div>
    
3. Click on the Worker that needs to be monitored and navigate to the ‘Runtime’ section.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/observability.png" style="width: 70%; height: auto;">
    </div>
    
4. Click on any pod name for which you want to monitor the logs, and navigate to the ‘Pod Logs’ section.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/observability.png" style="width: 70%; height: auto;">
    </div>
    

## Monitor the logs of a Worker using the Operations app

<aside class="callout">
🗣
Logs for a Worker are available on the Operations App only while the Workflow is still in progress (e.g., in a `scheduled` or `running` state). Once the Workflow succeeds or fails to execute, its logs are no longer visible in Operations. To access logs after completion, refer to the Metis UI or DataOS CLI, which retains historical logs.
</aside>

To monitor the logs of a Worker on the Operations App, follow the steps below:

1. Open the Operations app.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/observability.png" style="width: 70%; height: auto;">
    </div>
    
2. Navigate to User Space → Resources → Worker and search for the Worker by name.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/observability.png" style="width: 70%; height: auto;">
    </div>
    
3. Click on the Worker that needs to be monitored and navigate to the ‘Resource Runtime’ section.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/observability.png" style="width: 70%; height: auto;">
    </div>
    
4. Click on any runtime node for which you want to monitor the logs, and navigate to the ‘Runtime Node Logs’ section. Here, users can monitor the init container and main container logs.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/observability.png" style="width: 70%; height: auto;">
    </div>