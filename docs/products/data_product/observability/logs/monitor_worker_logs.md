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
        DEBUG: checksum /etc/dataos/work/dp-automation/demo_1/textile-analytics/data-product/consumer-aligned/build/semantic-model-view/model => 3496a3e69c00
        DEBUG: copyEnv: LENS2_DOCKER_IMAGE_VERSION -> CUBEJS_DOCKER_IMAGE_VERSION
        DEBUG: copyEnv: LENS2_DOCKER_IMAGE_TAG -> CUBEJS_DOCKER_IMAGE_TAG
        DEBUG: copyEnv: LENS2_BUILD_DATE -> CUBEJS_BUILD_DATE
        DEBUG: copyEnv: LENS2_HEIMDALL_BASE_URL -> CUBEJS_HEIMDALL_BASE_URL
        DEBUG: copyEnv: LENS2_API_SECRET -> CUBEJS_API_SECRET
        DEBUG: copyEnv: LENS2_SOURCE_TYPE -> CUBEJS_SOURCE_TYPE
        DEBUG: copyEnv: LENS2_NAME -> CUBEJS_NAME
        DEBUG: copyEnv: LENS2_WRITE_TRANSPILED_YAML -> CUBEJS_WRITE_TRANSPILED_YAML
        DEBUG: copyEnv: LENS2_TAGS -> CUBEJS_TAGS
        DEBUG: copyEnv: LENS2_DESCRIPTION -> CUBEJS_DESCRIPTION
        DEBUG: copyEnv: LENS2_SOURCE_NAME -> CUBEJS_SOURCE_NAME
        DEBUG: copyEnv: LENS2_SOURCE_CATALOG_NAME -> CUBEJS_SOURCE_CATALOG_NAME
        DEBUG: copyEnv: LENS2_AGENT_ENDPOINT_URL -> CUBEJS_AGENT_ENDPOINT_URL
        DEBUG: copyEnv: LENS2_SCHEMA_PATH -> CUBEJS_SCHEMA_PATH
        DEBUG: copyEnv: LENS2_AGENT_USE_UNSAFE -> CUBEJS_AGENT_USE_UNSAFE
        DEBUG: copyEnv: LENS2_LOG_LEVEL -> CUBEJS_LOG_LEVEL
        DEBUG: copyEnv: LENS2_SCHEDULED_REFRESH_TIMEZONES -> CUBEJS_SCHEDULED_REFRESH_TIMEZONES
        DEBUG: copyEnv: LENS2_ALLOW_UNGROUPED_WITHOUT_PRIMARY_KEY -> CUBEJS_ALLOW_UNGROUPED_WITHOUT_PRIMARY_KEY
        DEBUG: copyEnv: LENS2_RESOURCE_ID -> CUBEJS_RESOURCE_ID
        DEBUG: copyEnv: LENS2_AUTHORS -> CUBEJS_AUTHORS
        DEBUG: copyEnv: LENS2_DEFAULT_API_SCOPES -> CUBEJS_DEFAULT_API_SCOPES
        DEBUG: copyEnv: LENS2_API_BASEPATH -> CUBEJS_API_BASEPATH
        DEBUG: copyEnv: LENS2_DB_TYPE -> CUBEJS_DB_TYPE
        DEBUG: copyEnv: LENS2_DB_HOST -> CUBEJS_DB_HOST
        DEBUG: copyEnv: LENS2_DB_PORT -> CUBEJS_DB_PORT
        DEBUG: copyEnv: LENS2_DB_USER -> CUBEJS_DB_USER
        DEBUG: copyEnv: LENS2_DB_PASS -> CUBEJS_DB_PASS
        DEBUG: copyEnv: LENS2_MODELS_CHECKSUM -> CUBEJS_MODELS_CHECKSUM
        DEBUG: copyEnv: ROUTER_SERVER_NAME -> CUBESTORE_SERVER_NAME
        DEBUG: copyEnv: ROUTER_WORKER_PORT -> CUBESTORE_WORKER_PORT
        DEBUG: copyEnv: ROUTER_WORKERS -> CUBESTORE_WORKERS
        DEBUG: copyEnv: ROUTER_META_ADDR -> CUBESTORE_META_ADDR
        DEBUG: copyEnv: ROUTER_LOG_LEVEL -> CUBESTORE_LOG_LEVEL
        DEBUG: copyEnv: ROUTER_TELEMETRY -> CUBESTORE_TELEMETRY
        DEBUG: copyEnv: ROUTER_DATA_DIR -> CUBESTORE_DATA_DIR
        DEBUG: ENV ->  CACHE_MINIO_ACCESS_KEY_ID : ********************
        DEBUG: ENV ->  CACHE_MINIO_BUCKET : lens2
        DEBUG: ENV ->  CACHE_MINIO_REGION : eastus2
        DEBUG: ENV ->  CACHE_MINIO_SECRET_ACCESS_KEY : ********************
        DEBUG: ENV ->  CACHE_MINIO_SERVER_ENDPOINT : http://juicefs-gateway-lens2.juicefs-system.svc.cluster.local:9000
        DEBUG: ENV ->  CACHE_MINIO_SUB_PATH : lens-v2/public-textile-insights
        DEBUG: ENV ->  COLLATION_SERVICE_URL : http://poros-collation-server.poros.svc.cluster.local:37000/collated
        DEBUG: ENV ->  CUBEJS_AGENT_ENDPOINT_URL : https://lens2-audit-receiver.caretaker.svc.cluster.local:4295/audit-service/lens2
        DEBUG: ENV ->  CUBEJS_AGENT_USE_UNSAFE : true
        DEBUG: ENV ->  CUBEJS_ALLOW_UNGROUPED_WITHOUT_PRIMARY_KEY : true
        DEBUG: ENV ->  CUBEJS_API_BASEPATH : /lens2/api/public:textile-insights
        DEBUG: ENV ->  CUBEJS_API_SECRET : ********************
        DEBUG: ENV ->  CUBEJS_AUTHORS : abhishekgupta
        DEBUG: ENV ->  CUBEJS_BUILD_DATE : 12/18/2024 12:50:30 +0530
        DEBUG: ENV ->  CUBEJS_DB_HOST : textile-flash.public.svc.cluster.local
        DEBUG: ENV ->  CUBEJS_DB_PORT : 5433
        DEBUG: ENV ->  CUBEJS_DB_TYPE : flash
        DEBUG: ENV ->  CUBEJS_DB_USER : abhishekgupta
        DEBUG: ENV ->  CUBEJS_DEFAULT_API_SCOPES : meta,data,graphql,source
        DEBUG: ENV ->  CUBEJS_DESCRIPTION : Data model for textile analytics insights covering inventory, production, and sales data
        DEBUG: ENV ->  CUBEJS_DOCKER_IMAGE_TAG : 0.35.60-20
        DEBUG: ENV ->  CUBEJS_DOCKER_IMAGE_VERSION : 0.35.60-20
        DEBUG: ENV ->  CUBEJS_HEIMDALL_BASE_URL : https://dataos-training.dataos.app/heimdall
        DEBUG: ENV ->  CUBEJS_LOG_LEVEL : debug
        DEBUG: ENV ->  CUBEJS_MODELS_CHECKSUM : 3496a3e69c00
        DEBUG: ENV ->  CUBEJS_NAME : public:textile-insights
        DEBUG: ENV ->  CUBEJS_RESOURCE_ID : lens:v1alpha:textile-insights:public
        DEBUG: ENV ->  CUBEJS_SCHEDULED_REFRESH_TIMEZONES : UTC,America/Vancouver,America/Toronto
        DEBUG: ENV ->  CUBEJS_SCHEMA_PATH : dp-automation/demo_1/textile-analytics/data-product/consumer-aligned/build/semantic-model-view/model
        DEBUG: ENV ->  CUBEJS_SOURCE_CATALOG_NAME : undefined
        DEBUG: ENV ->  CUBEJS_SOURCE_DESCRIPTOR : eyJzb3VyY2UiOnsidHlwZSI6ImZsYXNoIiwiZGlhbGVjdCI6ImR1Y2tkYiIsImNvbm5lY3Rpb24iOiJmbGFzaCIsIm1ldGEiOnsidXNlcklkIjoiYWJoaXNoZWtndXB0YSIsImhvc3QiOiJ0ZXh0aWxlLWZsYXNoLnB1YmxpYy5zdmMuY2x1c3Rlci5sb2NhbCIsInBvcnQiOjU0MzN9fX0=
        DEBUG: ENV ->  CUBEJS_SOURCE_NAME : textile-flash
        DEBUG: ENV ->  CUBEJS_SOURCE_TYPE : flash
        DEBUG: ENV ->  CUBEJS_TAGS : Tier.Gold, Domain.Textile
        DEBUG: ENV ->  CUBEJS_USER_GROUPS : eyJ1c2VyR3JvdXBzIjpbeyJuYW1lIjoiZGVmYXVsdCIsImRlc2NyaXB0aW9uIjoiQWRtaW5pc3RyYXRvcnMgd2l0aCBmdWxsIGFjY2VzcyB0byB0ZXh0aWxlIGFuYWx5dGljcyBkYXRhIHByb2R1Y3QiLCJpbmNsdWRlcyI6IioiLCJhcGlfc2NvcGVzIjpbIm1ldGEiLCJkYXRhIiwiZ3JhcGhxbCIsImpvYnMiLCJzb3VyY2UiXSwiYWxsb3dfcHJpdmF0ZV9tZW1iZXJzX2FjY2VzcyI6ZmFsc2V9XX0=
        DEBUG: ENV ->  CUBEJS_USER_GROUP_NAMES : default
        DEBUG: ENV ->  CUBEJS_WRITE_TRANSPILED_YAML : true
        DEBUG: ENV ->  CUBESTORE_DATA_DIR : /var/work/.store
        DEBUG: ENV ->  CUBESTORE_LOG_LEVEL : error
        DEBUG: ENV ->  CUBESTORE_META_ADDR : textile-insights-router.public.svc.cluster.local:9999
        DEBUG: ENV ->  CUBESTORE_SERVER_NAME : textile-insights-worker-gqjk-ss-0.textile-insights-worker.public.svc.cluster.local:10001
        DEBUG: ENV ->  CUBESTORE_TELEMETRY : false
        DEBUG: ENV ->  CUBESTORE_WORKERS : textile-insights-worker-gqjk-ss-0.textile-insights-worker.public.svc.cluster.local:10001
        DEBUG: ENV ->  CUBESTORE_WORKER_PORT : 10001
        DEBUG: ENV ->  DATAOS_CONFIG_DIR : /etc/dataos/config
        DEBUG: ENV ->  DATAOS_DESCRIPTION : 
        DEBUG: ENV ->  DATAOS_FQDN : dataos-training.dataos.app
        DEBUG: ENV ->  DATAOS_IS_DRY_RUN : false
        DEBUG: ENV ->  DATAOS_LOG_LEVEL : debug
        DEBUG: ENV ->  DATAOS_NAME : textile-insights-worker
        DEBUG: ENV ->  DATAOS_RESOURCE_ID : worker:v1beta:textile-insights-worker:public
        DEBUG: ENV ->  DATAOS_RUN_AS_APIKEY : aGZoZmhmaC5hYWUzYmQ5Ni04MzY0LTRhMjctOTAyNC00OGYzNjQyYWQ5NmM=
        DEBUG: ENV ->  DATAOS_RUN_AS_USER : abhishekgupta
        DEBUG: ENV ->  DATAOS_RUN_ID : emjhc0znalts
        DEBUG: ENV ->  DATAOS_SECRET_DIR : /etc/dataos/secret
        DEBUG: ENV ->  DATAOS_STAMP : -gqjk
        DEBUG: ENV ->  DATAOS_TAGS : Tier.Gold,Domain.Textile
        DEBUG: ENV ->  DATAOS_TCP_FQDN : tcp.dataos-training.dataos.app
        DEBUG: ENV ->  DATAOS_TEMP_DIR : /var/dataos/temp_data
        DEBUG: ENV ->  DATAOS_TYPE : worker
        DEBUG: ENV ->  DATAOS_UID : 0c554e93-d740-47f2-becd-9533d99b0a64
        DEBUG: ENV ->  DATAOS_WORKSPACE : public
        DEBUG: ENV ->  DEPOT_SERVICE_INTERNAL_URL : https://depotservice-api.depot.svc.cluster.local:8443/ds
        DEBUG: ENV ->  DEPOT_SERVICE_SSL_ENABLED : false
        DEBUG: ENV ->  DEPOT_SERVICE_SSL_HOSTNAME_VERIFICATION : false
        DEBUG: ENV ->  DEPOT_SERVICE_URL : https://dataos-training.dataos.app/ds
        DEBUG: ENV ->  GATEWAY_INTERNEL_URL : http://gateway.network-gateway.svc.cluster.local:8090/gateway
        DEBUG: ENV ->  GATEWAY_URL : https://dataos-training.dataos.app/gateway
        DEBUG: ENV ->  GITSYNC_USERNAME : abhiitis
        DEBUG: ENV ->  HEIMDALL_INTERNAL_URL : https://heimdall-api.heimdall.svc.cluster.local:32010/heimdall
        DEBUG: ENV ->  HEIMDALL_URL : https://dataos-training.dataos.app/heimdall
        DEBUG: ENV ->  HOME : /root
        DEBUG: ENV ->  HOSTNAME : textile-insights-worker-gqjk-ss-0
        DEBUG: ENV ->  KUBERNETES_PORT : tcp://10.214.0.1:443
        DEBUG: ENV ->  KUBERNETES_PORT_443_TCP : tcp://10.214.0.1:443
        DEBUG: ENV ->  KUBERNETES_PORT_443_TCP_ADDR : 10.214.0.1
        DEBUG: ENV ->  KUBERNETES_PORT_443_TCP_PORT : 443
        DEBUG: ENV ->  KUBERNETES_PORT_443_TCP_PROTO : tcp
        DEBUG: ENV ->  KUBERNETES_SERVICE_HOST : 10.214.0.1
        DEBUG: ENV ->  KUBERNETES_SERVICE_PORT : 443
        DEBUG: ENV ->  KUBERNETES_SERVICE_PORT_HTTPS : 443
        DEBUG: ENV ->  LENS2_AGENT_ENDPOINT_URL : https://lens2-audit-receiver.caretaker.svc.cluster.local:4295/audit-service/lens2
        DEBUG: ENV ->  LENS2_AGENT_USE_UNSAFE : true
        DEBUG: ENV ->  LENS2_ALLOW_UNGROUPED_WITHOUT_PRIMARY_KEY : true
        DEBUG: ENV ->  LENS2_API_BASEPATH : /lens2/api/public:textile-insights
        DEBUG: ENV ->  LENS2_API_SECRET : ********************
        DEBUG: ENV ->  LENS2_AUTHORS : abhishekgupta
        DEBUG: ENV ->  LENS2_BUILD_DATE : 12/18/2024 12:50:30 +0530
        DEBUG: ENV ->  LENS2_DB_HOST : textile-flash.public.svc.cluster.local
        DEBUG: ENV ->  LENS2_DB_PORT : 5433
        DEBUG: ENV ->  LENS2_DB_TYPE : flash
        DEBUG: ENV ->  LENS2_DB_USER : abhishekgupta
        DEBUG: ENV ->  LENS2_DEFAULT_API_SCOPES : meta,data,graphql,source
        DEBUG: ENV ->  LENS2_DESCRIPTION : Data model for textile analytics insights covering inventory, production, and sales data
        DEBUG: ENV ->  LENS2_DOCKER_IMAGE_TAG : 0.35.60-20
        DEBUG: ENV ->  LENS2_DOCKER_IMAGE_VERSION : 0.35.60-20
        DEBUG: ENV ->  LENS2_HEIMDALL_BASE_URL : https://dataos-training.dataos.app/heimdall
        DEBUG: ENV ->  LENS2_LOG_LEVEL : debug
        DEBUG: ENV ->  LENS2_MODELS_CHECKSUM : 3496a3e69c00
        DEBUG: ENV ->  LENS2_NAME : public:textile-insights
        DEBUG: ENV ->  LENS2_RESOURCE_ID : lens:v1alpha:textile-insights:public
        DEBUG: ENV ->  LENS2_SCHEDULED_REFRESH_TIMEZONES : UTC,America/Vancouver,America/Toronto
        DEBUG: ENV ->  LENS2_SCHEMA_PATH : dp-automation/demo_1/textile-analytics/data-product/consumer-aligned/build/semantic-model-view/model
        DEBUG: ENV ->  LENS2_SOURCE_CATALOG_NAME : 
        DEBUG: ENV ->  LENS2_SOURCE_NAME : textile-flash
        DEBUG: ENV ->  LENS2_SOURCE_TYPE : flash
        DEBUG: ENV ->  LENS2_TAGS : Tier.Gold, Domain.Textile
        DEBUG: ENV ->  LENS2_WRITE_TRANSPILED_YAML : true
        DEBUG: ENV ->  LOG_LEVEL : debug
        DEBUG: ENV ->  MEILISEARCH_HOST : meilisearch.caretaker.svc.cluster.local
        DEBUG: ENV ->  MEILISEARCH_KEY : 549f3b31593e4517827fef74c68fccc8
        DEBUG: ENV ->  MEILISEARCH_PORT : 7700
        DEBUG: ENV ->  METIS_AUTH_PROVIDER : dataos-apikey
        DEBUG: ENV ->  METIS_URL : https://dataos-training.dataos.app/metis
        DEBUG: ENV ->  MINERVA_JDBC_URL : jdbc:trino://tcp.dataos-training.dataos.app:7432
        DEBUG: ENV ->  MINERVA_TCP_HOST : tcp.dataos-training.dataos.app
        DEBUG: ENV ->  MINERVA_TCP_PORT : 7432
        DEBUG: ENV ->  NODE_ENV : production
        DEBUG: ENV ->  NODE_PATH : /usr/lib/node_modules:/src/node_modules:/etc/dataos/work
        DEBUG: ENV ->  NODE_VERSION : 18.20.3
        DEBUG: ENV ->  PATH : /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
        DEBUG: ENV ->  POD_NAME : textile-insights-worker-gqjk-ss-0
        DEBUG: ENV ->  POROS_SERVICE_URL : https://dataos-training.dataos.app/poros
        DEBUG: ENV ->  PULSAR_SERVICE_URL : pulsar+ssl://pulsar-proxy.caretaker.svc.cluster.local:6651
        DEBUG: ENV ->  PULSAR_TLS_ALLOW_INSECURE_CONNECTION : true
        DEBUG: ENV ->  PULSAR_TLS_VALIDATE_HOSTNAME : false
        DEBUG: ENV ->  PULSAR_USE_TLS : true
        DEBUG: ENV ->  PUSHGATEWAY_URL : http://prometheus-pushgateway.sentinel.svc.cluster.local:9091
        DEBUG: ENV ->  PYTHONUNBUFFERED : 1
        DEBUG: ENV ->  ROUTER_DATA_DIR : /var/work/.store
        DEBUG: ENV ->  ROUTER_LOG_LEVEL : error
        DEBUG: ENV ->  ROUTER_META_ADDR : textile-insights-router.public.svc.cluster.local:9999
        DEBUG: ENV ->  ROUTER_SERVER_NAME : textile-insights-worker-gqjk-ss-0.textile-insights-worker.public.svc.cluster.local:10001
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