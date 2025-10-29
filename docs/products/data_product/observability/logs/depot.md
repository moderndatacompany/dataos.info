# Monitor the logs of a Depot

<aside class="callout">
🗣 Only Depots created on Object Storage will have logs available.
</aside>

Whenever an Object Storage Depot is created, a pod is provisioned in the backend with three containers. One is the main container, named after the Depot itself. The other two are init containers, automatically generated with suffixes `-dbi` and `-dbc` appended to the Depot’s identifier. 

- `dbi` stands for Database Independent Interface. It provides an abstraction layer to interact with underlying metadata databases in a standard way, ensuring flexibility across various database types that may be integrated with object storage for tracking object metadata.

- `dbc` refers to Database Connectivity, responsible for handling the actual connection and communication setup with the metadata database during the pod initialization. It ensures the main container can successfully retrieve or store metadata related to stored objects.

Together, these init containers ensure the object storage environment is correctly configured and ready before the main container starts execution.

The below section involves the steps to observe the logs of a Depot on different endpoints, such as DataOS CLI, Metis UI, and Operations App. 

## Monitor the logs of a Depot using DataOS CLI

To monitor the  logs of a Depot using DataOS CLI, follow the steps below:

<aside class="callout">
🗣 Only logs from the main container are available via the DataOS CLI. Logs from init containers (such as `dbi` and `dbc`) can only be accessed through the Metis UI or the Operations App.
If CLI logs appear blank, the issue might lie in one of the init containers. In such cases, check the init container logs in Metis or Operations to diagnose the failure.
If the init container logs also do not appear, it may indicate that there are insufficient resources (CPU, memory, nodes) to initialize the pod, or there could be other runtime or infrastructure-level issues blocking startup.
</aside>

1. On DataOS CLI, execute the following command by replacing the placeholders with the actual values. 
    
    ```bash
    dataos-ctl log -t depot -n ${{depot-name}}
    ```
    
    **Example Usage:**
    
    ```bash
    dataos-ctl log -t depot -n thirdparty
    INFO[0000] 📃 log(public)...                             
    INFO[0002] 📃 log(public)...complete                     
    
         NODE NAME    │ CONTAINER NAME │ ERROR  
    ──────────────────┼────────────────┼────────
      thirdparty-ss-0 │ thirdparty     │        
                        # ^ main container
    -------------------LOGS-------------------
    15-06-2025 02:35:33 [INFO] Configuring...
    15-06-2025 02:35:33 [INFO] Configuring...
    15-06-2025 02:35:33 [INFO] Starting Hive Metastore service. Command: /opt/hive-metastore/bin/start-metastore
    SLF4J: Class path contains multiple SLF4J bindings.
    SLF4J: Found binding in [jar:file:/opt/apache-hive-metastore-3.1.3-bin/lib/log4j-slf4j-impl-2.17.1.jar!/org/slf4j/impl/StaticLoggerBinder.class]
    SLF4J: Found binding in [jar:file:/opt/hadoop-3.3.4/share/hadoop/common/lib/slf4j-reload4j-1.7.36.jar!/org/slf4j/impl/StaticLoggerBinder.class]
    SLF4J: See http://www.slf4j.org/codes.html#multiple_bindings for an explanation.
    SLF4J: Actual binding is of type [org.apache.logging.slf4j.Log4jLoggerFactory]
    2025-06-15 02:35:36: Starting Metastore Server
    SLF4J: Class path contains multiple SLF4J bindings.
    SLF4J: Found binding in [jar:file:/opt/apache-hive-metastore-3.1.3-bin/lib/log4j-slf4j-impl-2.17.1.jar!/org/slf4j/impl/StaticLoggerBinder.class]
    SLF4J: Found binding in [jar:file:/opt/hadoop-3.3.4/share/hadoop/common/lib/slf4j-reload4j-1.7.36.jar!/org/slf4j/impl/StaticLoggerBinder.class]
    SLF4J: See http://www.slf4j.org/codes.html#multiple_bindings for an explanation.
    SLF4J: Actual binding is of type [org.apache.logging.slf4j.Log4jLoggerFactory]
    
    ```
    
    This log confirms that the `thirdparty` Depot has:
    
    - Completed its configuration process.
    - Successfully initiated the Hive Metastore service.
    - Encountered minor SLF4J multiple binding warnings that do not affect critical functionality.
    
    No errors are present in the output, and the startup appears to be smooth and complete.
    

## Monitor the logs of a Depot using Metis UI

To monitor the logs of a Depot on the Metis Catalog UI, follow the steps below:

1. Open the Metis Catalog.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/logs/depot/image%20(21).png" style="border:1px solid black; width: 70%; height: auto">
    </div>
    
2. Search for the Depot by name.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/logs/depot/image%20(22).png" style="border:1px solid black; width: 70%; height: auto">
    </div>
    
3. Click on the Depot that needs to be monitored and navigate to the ‘Runtime’ section.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/logs/depot/image%20(23).png" style="border:1px solid black; width: 70%; height: auto">
    </div>
    
4. Click on the pod and navigate to the ‘Pod Logs’ section. In the ‘Pog Logs’ section, users can monitor the logs of the init and main containers.
    
    **Main container logs:**
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/logs/depot/image%20(24).png" style="border:1px solid black; width: 70%; height: auto">
    </div>
    
    **`dbi` container logs:**
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/logs/depot/image%20(25).png" style="border:1px solid black; width: 70%; height: auto">
    </div>
    
    **`dbc` container logs:**
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/logs/depot/image%20(26).png" style="border:1px solid black; width: 70%; height: auto">
    </div>
    

## Monitor the logs of a Depot using the Operations app

To monitor the logs of a Depot on the Operations App, follow the steps below:

1. Open the Operations app.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/logs/depot/image%20(27).png" style="border:1px solid black; width: 70%; height: auto">
    </div>
    
2. Navigate to User Space → Resources → Depot and search for the Depot by name.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/logs/depot/image%20(28).png" style="border:1px solid black; width: 70%; height: auto">
    </div>
    
3. Click on the Depot that needs to be monitored and navigate to the ‘Resource Runtime’ section.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/logs/depot/image%20(29).png" style="border:1px solid black; width: 70%; height: auto">
    </div>
    
4. Click on the runtime node for which you want to monitor the logs, and navigate to the ‘Runtime Node Logs’ section.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/logs/depot/image%20(30).png" style="border:1px solid black; width: 70%; height: auto">
    </div>
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/logs/depot/image%20(31).png" style="border:1px solid black; width: 70%; height: auto">
    </div>
    
    These logs confirm that:
    
    - The `dbi` init container performed the Hive schema setup tasks by executing SQL scripts to prepare the metastore.
    - The `dbc` init container initialized the Kyuubi server, loaded environment variables, and launched the process that connects query engines to the depot.
    - The main `thirdparty` container successfully started the Hive Metastore service and confirmed the system is ready to handle metadata operations.
    
    This three-stage initialization confirms that the object storage Depot is fully operational and ready for use.