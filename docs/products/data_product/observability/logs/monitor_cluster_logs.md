# Monitor the Logs of a Cluster

This section involves the steps to observe the logs of a Cluster on different endpoints such as DataOS CLI, Metis UI, and Operations App.

## DataOS CLI

To monitor the  logs of a Cluster using DataOS CLI, follow the steps below:

1. On DataOS CLI, execute the following command by replacing the placeholders with the actual values. 
    
    ```bash
    dataos-ctl log -t cluster -w ${{workspace-name}} -n ${{workflow-name}}
    ```
    
    **Example Usage:**
    
    ```bash
    dataos-ctl log -t cluster -w public -n minion
    INFO[0000] 📃 log(public)...                             
    INFO[0001] 📃 log(public)...complete                     
    
               NODE NAME           │ CONTAINER NAME │ ERROR  
    ───────────────────────────────┼────────────────┼────────
      minion-jqtw-64c658f857-wwq6j │ themis         │        
             # ^ pod name
    -------------------LOGS-------------------
    ++ id -u
    + myuid=10009
    ++ id -g
    + mygid=0
    + set +e
    ++ getent passwd 10009
    + uidentry=kyuubi:x:10009:0::/home/kyuubi:/bin/sh
    + set -e
    + '[' -z kyuubi:x:10009:0::/home/kyuubi:/bin/sh ']'
    + '[' -z /usr/lib/jvm/zulu8 ']'
    + SPARK_CLASSPATH=':/opt/spark/jars/*'
    + env
    + grep SPARK_JAVA_OPT_
    + sort -t_ -k4 -n
    + sed 's/[^=]*=\(.*\)/\1/g'
    + readarray -t SPARK_EXECUTOR_JAVA_OPTS
    + '[' -n '' ']'
    + '[' -z ']'
    + '[' -z ']'
    + '[' -n '' ']'
    + '[' -z ']'
    + '[' -z ']'
    + '[' -z x ']'
    + SPARK_CLASSPATH='/opt/spark/conf::/opt/spark/jars/*'
    + case "$1" in
    + echo 'Non-spark-on-k8s command provided, proceeding in pass-through mode...'
    Non-spark-on-k8s command provided, proceeding in pass-through mode...
    + CMD=("$@")
    + exec /usr/bin/tini -s -- ./bin/kyuubi run
    Warn: Not find kyuubi environment file /opt/kyuubi/conf/kyuubi-env.sh, using default ones...
    JAVA_HOME: /usr/lib/jvm/zulu8
    KYUUBI_HOME: /opt/kyuubi
    KYUUBI_CONF_DIR: /opt/kyuubi/conf
    KYUUBI_LOG_DIR: /opt/kyuubi/logs
    KYUUBI_PID_DIR: /opt/kyuubi/pid
    KYUUBI_WORK_DIR_ROOT: /opt/kyuubi/work
    FLINK_HOME: 
    FLINK_ENGINE_HOME: /opt/kyuubi/externals/engines/flink
    SPARK_HOME: /opt/spark
    SPARK_CONF_DIR: /opt/spark/conf
    SPARK_ENGINE_HOME: /opt/kyuubi/externals/engines/spark
    TRINO_ENGINE_HOME: /opt/kyuubi/externals/engines/trino
    HIVE_ENGINE_HOME: /opt/kyuubi/externals/engines/hive
    HADOOP_CONF_DIR: 
    YARN_CONF_DIR: 
    Starting org.apache.kyuubi.server.KyuubiServer
    SLF4J: Class path contains multiple SLF4J bindings.
    SLF4J: Found binding in [jar:file:/opt/kyuubi/jars/slf4j-reload4j-1.7.36.jar!/org/slf4j/impl/StaticLoggerBinder.class]
    SLF4J: Found binding in [jar:file:/opt/kyuubi/jars/dataos-spark-auth_2.12-1.9.2.jar!/org/slf4j/impl/StaticLoggerBinder.class]
    SLF4J: Found binding in [jar:file:/opt/kyuubi/jars/log4j-slf4j-impl-2.24.1.jar!/org/slf4j/impl/StaticLoggerBinder.class]
    SLF4J: Found binding in [jar:file:/opt/kyuubi/jars/slf4j-log4j12-1.7.25.jar!/org/slf4j/impl/StaticLoggerBinder.class]
    SLF4J: See http://www.slf4j.org/codes.html#multiple_bindings for an explanation.
    SLF4J: Actual binding is of type [org.slf4j.impl.Reload4jLoggerFactory]
    Missing log4j-defaults.properties
    log4j:WARN No appenders could be found for logger (org.apache.kyuubi.server.KyuubiServer).
    log4j:WARN Please initialize the log4j system properly.
    log4j:WARN See http://logging.apache.org/log4j/1.2/faq.html#noconfig for more info.
    ```
    
    These logs show:
    
    - The container started successfully.
    - All major environment variables were configured.
    - KyuubiServer started, despite minor logging configuration warnings.
    - The pod is running and healthy.
    
    This output is typical for a Spark/SQL gateway container like Kyuubi deployed in a cluster resource.
    

## Metis UI

To monitor the logs of a Cluster on the Metis Catalog UI, follow the steps below:

1. Open the Metis Catalog.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/logs/cluster/image%20(32).png" style="border:1px solid black; width: 70%; height: auto">
    <figcaption><i>Open the Metis Catalog</i></figcaption>
    </div>
    
2. Search for the Cluster by name.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/logs/cluster/image%20(38).png" style="border:1px solid black; width: 70%; height: auto">
    <figcaption><i>Search the Cluster in Metis</i></figcaption>
    </div>
    
3. Click on the Cluster that needs to be monitored and navigate to the ‘Runtime’ section.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/logs/cluster/image%20(33).png" style="border:1px solid black; width: 70%; height: auto">
    <figcaption><i>Cluster runtime in Metis</i></figcaption>
    </div>
    
4. Click on any pod name for which you want to monitor the logs, and navigate to the ‘Pod Logs’ section.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/logs/cluster/image%20(34).png" style="border:1px solid black; width: 70%; height: auto">
    <figcaption><i>Pod Logs in Metis</i></figcaption>
    </div>
    
    These logs show:
    
    - The container started successfully.
    - All major environment variables were configured.
    - KyuubiServer started, despite minor logging configuration warnings.
    - The pod is running and healthy.
    
    This output is typical for a Spark/SQL gateway container like Kyuubi deployed in a cluster resource.
    

## Operations App

To monitor the logs of a Cluster on the Operations App, follow the steps below:

1. Open the Operations app.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/logs/cluster/image%20(35).png" style="border:1px solid black; width: 70%; height: auto">
    <figcaption><i>Open the Operations app</i></figcaption>
    </div>
    
2. Navigate to User Space → Resources → Cluster and search for the Cluster by name.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/logs/cluster/image%20(39).png" style="border:1px solid black; width: 70%; height: auto">
    <figcaption><i>Operations > Resources > Cluster</i></figcaption>
    </div>
    
3. Click on the Cluster that needs to be monitored and navigate to the ‘Resource Runtime’ section.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/logs/cluster/image%20(36).png" style="border:1px solid black; width: 70%; height: auto">
    <figcaption><i>Cluster resource runtime in Operations</i></figcaption>
    </div>
    
4. Click on any runtime node for which you want to monitor the logs, and navigate to the ‘Runtime Node Logs’ section. 
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/logs/cluster/image%20(37).png" style="border:1px solid black; width: 70%; height: auto">
    <figcaption><i>Runtime Node Logs in Operations</i></figcaption>
    </div>
    
    These logs show:
    
    - The container started successfully.
    - All major environment variables were configured.
    - KyuubiServer started, despite minor logging configuration warnings.
    - The pod is running and healthy.
    
    This output is typical for a Spark/SQL gateway container like Kyuubi deployed in a cluster resource.
