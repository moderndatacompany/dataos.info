# Monitor the Logs of a Service

This section involves the steps to observe the logs of a Service on different endpoints, such as DataOS CLI, Metis UI, and Operations App.

## DataOS CLI

To monitor the  logs of a Service using DataOS CLI, follow the steps below:

1. On DataOS CLI, execute the following command by replacing the placeholders with the actual values. 
    
    ```bash
    dataos-ctl log -t service -w ${{workspace-name}} -n ${{workflow-name}}
    ```
    
    **Example Usage:**
    
    ```bash
    dataos-ctl log -t service -w public -n lakehouse-ms  
    INFO[0000] 📃 log(public)...                             
    INFO[0001] 📃 log(public)...complete                     
    
                   NODE NAME              │ CONTAINER NAME │ ERROR  
    ──────────────────────────────────────┼────────────────┼────────
      lakehouse-ms-mgn0-d-dd7d977f6-9mnc4 │ lakehouse-ms   │        
                # ^ pod name
    -------------------LOGS-------------------
    SLF4J(I): Connected with provider of type [ch.qos.logback.classic.spi.LogbackServiceProvider]
    2025-06-15 23:11:49.493 INFO  [main] i.d.i.rest.RestCatalogApplication - Rest catalog service configured depot: lakehouse depotSecretName: icebase-rw depotSecretAcl: rw
    WARNING: An illegal reflective access operation has occurred
    WARNING: Illegal reflective access by retrofit2.Platform (file:/usr/lib/iceberg-rest/iceberg-rest-catalog.jar) to constructor java.lang.invoke.MethodHandles$Lookup(java.lang.Class,int)
    WARNING: Please consider reporting this to the maintainers of retrofit2.Platform
    WARNING: Use --illegal-access=warn to enable warnings of further illegal reflective access operations
    WARNING: All illegal access operations will be denied in a future release
    2025-06-15 23:11:52.163 INFO  [main] i.d.i.rest.RestCatalogApplication - Creating Iceberg catalog with properties: {catalog-impl=io.dataos.iceberg.rest.HadoopCatalog, warehouse=abfss://lake001@dlake0bnoss0dsck0stg.dfs.core.windows.net/lakehouse01}
    2025-06-15 23:11:52.372 WARN  [main] o.a.hadoop.util.NativeCodeLoader - Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
    2025-06-15 23:11:52.877 ERROR [main] o.a.h.f.a.AzureBlobFileSystemStore - Failed to get primary group for root, using user name as primary group name
    2025-06-15 23:11:52.968 INFO  [main] org.apache.iceberg.CatalogUtil - Loading custom FileIO implementation: org.apache.iceberg.hadoop.HadoopFileIO
    2025-06-15 23:11:52.994 INFO  [main] org.eclipse.jetty.util.log - Logging initialized @4326ms to org.eclipse.jetty.util.log.Slf4jLog
    2025-06-15 23:11:53.094 INFO  [main] org.eclipse.jetty.server.Server - jetty-9.4.43.v20210629; built: 2021-06-30T11:07:22.254Z; git: 526006ecfa3af7f1a27ef3a288e2bef7ea9dd7e8; jvm 11.0.24+8-post-Debian-2deb11u1
    2025-06-15 23:11:53.165 INFO  [main] o.e.j.server.handler.ContextHandler - Started o.e.j.s.ServletContextHandler@73bb573d{/,null,AVAILABLE}
    2025-06-15 23:11:53.174 INFO  [main] o.e.jetty.server.AbstractConnector - Started ServerConnector@27e44e9c{HTTP/1.1, (http/1.1)}{0.0.0.0:8099}
    2025-06-15 23:11:53.174 INFO  [main] org.eclipse.jetty.server.Server - Started @4506ms
    2025-06-15 23:11:53.174 INFO  [main] i.d.i.rest.RestCatalogApplication - Iceberg REST service started on port 8099
    ```
    
    The logs in the above example show that:
    
    - The Service has started successfully.
    - It initialized logging, environment configuration, and integration with Azure.
    - Warnings during startup are safe to ignore.
    - The REST API is exposed on port `8099`.
    
    This is expected behavior for a healthy Service in DataOS.
    

## Metis UI

To monitor the logs of a Service on the Metis Catalog UI, follow the steps below:

1. Open the Metis Catalog.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/logs/service/image%20(40).png" style="border:1px solid black; width: 70%; height: auto">
    <figcaption><i>Open the Metis Catalog</i></figcaption>
    </div>
    
2. Search for the Service by name.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/logs/service/image%20(41).png" style="border:1px solid black; width: 70%; height: auto">
    <figcaption><i>Search the Service in Metis</i></figcaption>
    </div>
    
3. Click on the Service that needs to be monitored and navigate to the ‘Runtime’ section.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/logs/service/image%20(42).png" style="border:1px solid black; width: 70%; height: auto">
    <figcaption><i>Service runtime in Metis</i></figcaption>
    </div>
    
4. Click on any run name for which you want to monitor the logs, and navigate to the ‘Pod Logs’ section.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/logs/service/image%20(43).png" style="border:1px solid black; width: 70%; height: auto">
    <figcaption><i>Pod Logs in Metis</i></figcaption>
    </div>
    
    The logs in the above example show that:
    
    - The Service has started successfully.
    - It initialized logging, environment configuration, and integration with Azure.
    - Warnings during startup are safe to ignore.
    - The REST API is exposed on port `8099`.
    
    This is expected behavior for a healthy Service in DataOS.
    

## Operations App

To monitor the logs of a Service on the Operations App, follow the steps below:

1. Open the Operations app.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/logs/service/image%20(44).png" style="border:1px solid black; width: 70%; height: auto">
    <figcaption><i>Open the Operations app</i></figcaption>
    </div>
    
2. Navigate to User Space → Resources → Service and search for the Service by name.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/logs/service/image%20(45).png" style="border:1px solid black; width: 70%; height: auto">
    <figcaption><i>Operations > Resources > Service</i></figcaption>
    </div>
    
3. Click on the Service that needs to be monitored and navigate to the ‘Resource Runtime’ section.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/logs/service/image%20(46).png" style="border:1px solid black; width: 70%; height: auto">
    <figcaption><i>Service resource runtime in Operations</i></figcaption>
    </div>
    
4. Click on any runtime node for which you want to monitor the logs, and navigate to the ‘Runtime Node Logs’ section.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/logs/service/image%20(47).png" style="border:1px solid black; width: 70%; height: auto">
    <figcaption><i>Runtime Node Logs in Operations</i></figcaption>
    </div>
    
    The logs in the above example show that:
    
    - The Service has started successfully.
    - It initialized logging, environment configuration, and integration with Azure.
    - Warnings during startup are safe to ignore.
    - The REST API is exposed on port `8099`.
    
    This is expected behavior for a healthy Service in DataOS.