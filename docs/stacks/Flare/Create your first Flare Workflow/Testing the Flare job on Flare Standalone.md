# **Testing the Flare job on Flare Standalone**

# **Pre-requisites**

## **Install Flare Standalone**

Flare Standalone lets you explore DataOS Flare capabilities on your local system. It's a testing interface to let you check your code before implementing it into production. If you have already installed Flare Standalone, you can move on to the next section. If you haven’t navigated, refer to
[Flare Standalone 1.0](https://www.notion.so/Flare-Standalone-1-0-).

# **Testing the Flare Job**

## **Step 1: Download the data to the local system**

To test the Flare Job you need to have the data on the local system. If you don’t have the data download the data from your cloud storage

> 🗣️ While testing your Flare Job on the local system, which has a limited compute restrict the input data to say 10000 to 15000 rows at maximum. Testing big data on local storage might result in slow processing and overheating of the system so limit the input size.

Create a new folder, let’s say by name `city_ingestion` and store the data file `ingestion.csv` in it. Copy the path of the `city_ingestion` folder.

## **Step 2: Make changes to the config YAML**

Change the input dataset address by removing the existing one and adding the prefix `/data/examples` and then adding the name of the folder in which you have stored the data. For e.g. If you have stored the data in the folder `product`, the dataset address will be `/data/examples/product`. 

The output dataset address will be `/dataout/`

```yaml
version: v1
name: wf-city-demo-001
type: workflow
tags:
- Connect
- City
description: The job ingests city data into DataOS
workflow:
  title: Connect City
  dag:
    - name: city-01
      title: City Dimension Ingester
      description: The job ingests city data from Third-party into DataOS
      spec:
        stack: flare:3.0
        compute: runnable-default
        flare:
          job:
            explain: true
            inputs:
            - name: city_ingest
              dataset: /data/examples/city_ingestion
              format: csv

            logLevel: INFO
            outputs:
              - name: output01
                depot: /dataout/
            steps:
              - sink:
                  - sequenceName: cities
                    datasetName: city
                    outputName: output01
                    outputType: Iceberg
                    description: City data ingested from external csv
                    outputOptions:
                      saveMode: overwrite
                      iceberg:
                        properties:
                            write.format.default: parquet
                            write.metadata.compression-codec: gzip
                        partitionSpec:
                          - type: identity
                            column: state_name
                    tags:
                      - Connect
                      - City
                    title: City Source Data

                sequence:
                  - name: cities
                    sql: select * from city_ingest limit 10
```

## **Step 3: Run the Workflow**

To run the Flare workflow we will use the CLI Method. To know more about running Flare Workflow click the below link

**Command**

```bash
dataos-ctl develop start -s <flare-version> -f <config-file-path> -d <data-file-path>
```

In this case, we will be using the flare version `flare:3.0` and the `city_ingestion` folder is inside the `data` folder

```bash
dataos-ctl develop start -s flare:3.0 -f /home/tmdc/standalone/standalone.yaml -d /home/tmdc/standalone/data
```

**Output**

```bash
Flare session is available as flare.
    Welcome to
         ______   _                       
        |  ____| | |                      
        | |__    | |   __ _   _ __    ___ 
        |  __|   | |  / _` | | '__|  / _ \
        | |      | | | (_| | | |    |  __/
        |_|      |_|  \__,_| |_|     \___|  version 1.2.0
        
    Powered by Apache Spark 3.3.0
Using Scala version 2.12.15 (OpenJDK 64-Bit Server VM, Java 1.8.0_262)
Type in expressions to have them evaluated.
Type :help for more information.
```

- **To view the full output, click the arrow**
    
    ```bash
    INFO[0002] 💻 create flare local...                      
    {"status":"Status: Image is up to date for rubiklabs/flare3:5.10.23"}
    INFO[0006] f9648f984b63:right-wasp                      
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
    + exec /usr/bin/tini -s -- /opt/spark/bin/spark-shell -i /opt/spark/work-dir/standalone.scala
    2022-10-18 12:19:14,184 INFO  [main] o.a.spark.util.SignalUtils: Registering signal handler for INT
    2022-10-18 12:19:18,640 INFO  [main] o.a.h.hive.conf.HiveConf: Found configuration file null
    2022-10-18 12:19:18,751 INFO  [main] o.a.spark.SparkContext: Running Spark version 3.3.0
    2022-10-18 12:19:18,815 WARN  [main] o.a.h.u.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
    2022-10-18 12:19:18,887 INFO  [main] o.a.s.r.ResourceUtils: ==============================================================
    2022-10-18 12:19:18,888 INFO  [main] o.a.s.r.ResourceUtils: No custom resources configured for spark.driver.
    2022-10-18 12:19:18,888 INFO  [main] o.a.s.r.ResourceUtils: ==============================================================
    2022-10-18 12:19:18,888 INFO  [main] o.a.spark.SparkContext: Submitted application: Spark shell
    2022-10-18 12:19:18,904 INFO  [main] o.a.s.r.ResourceProfile: Default ResourceProfile created, executor resources: Map(cores -> name: cores, amount: 1, script: , vendor: , memory -> name: memory, amount: 1024, script: , vendor: , offHeap -> name: offHeap, amount: 0, script: , vendor: ), task resources: Map(cpus -> name: cpus, amount: 1.0)
    2022-10-18 12:19:18,912 INFO  [main] o.a.s.r.ResourceProfile: Limiting resource is cpu
    2022-10-18 12:19:18,913 INFO  [main] o.a.s.r.ResourceProfileManager: Added ResourceProfile id: 0
    2022-10-18 12:19:18,955 INFO  [main] o.a.spark.SecurityManager: Changing view acls to: root
    2022-10-18 12:19:18,956 INFO  [main] o.a.spark.SecurityManager: Changing modify acls to: root
    2022-10-18 12:19:18,956 INFO  [main] o.a.spark.SecurityManager: Changing view acls groups to: 
    2022-10-18 12:19:18,956 INFO  [main] o.a.spark.SecurityManager: Changing modify acls groups to: 
    2022-10-18 12:19:18,956 INFO  [main] o.a.spark.SecurityManager: SecurityManager: authentication disabled; ui acls disabled; users  with view permissions: Set(root); groups with view permissions: Set(); users  with modify permissions: Set(root); groups with modify permissions: Set()
    2022-10-18 12:19:19,138 INFO  [main] o.apache.spark.util.Utils: Successfully started service 'sparkDriver' on port 39227.
    2022-10-18 12:19:19,169 INFO  [main] org.apache.spark.SparkEnv: Registering MapOutputTracker
    2022-10-18 12:19:19,194 INFO  [main] org.apache.spark.SparkEnv: Registering BlockManagerMaster
    2022-10-18 12:19:19,215 INFO  [main] o.a.s.s.BlockManagerMasterEndpoint: Using org.apache.spark.storage.DefaultTopologyMapper for getting topology information
    2022-10-18 12:19:19,216 INFO  [main] o.a.s.s.BlockManagerMasterEndpoint: BlockManagerMasterEndpoint up
    2022-10-18 12:19:19,219 INFO  [main] org.apache.spark.SparkEnv: Registering BlockManagerMasterHeartbeat
    2022-10-18 12:19:19,246 INFO  [main] o.a.s.s.DiskBlockManager: Created local directory at /tmp/blockmgr-a4f8e8a2-1a7f-4ac5-9448-610963440cdf
    2022-10-18 12:19:19,261 INFO  [main] o.a.s.s.memory.MemoryStore: MemoryStore started with capacity 366.3 MiB
    2022-10-18 12:19:19,276 INFO  [main] org.apache.spark.SparkEnv: Registering OutputCommitCoordinator
    2022-10-18 12:19:19,354 INFO  [main] o.s.jetty.util.log: Logging initialized @6295ms to org.sparkproject.jetty.util.log.Slf4jLog
    2022-10-18 12:19:19,481 INFO  [main] o.s.jetty.server.Server: jetty-9.4.46.v20220331; built: 2022-03-31T16:38:08.030Z; git: bc17a0369a11ecf40bb92c839b9ef0a8ac50ea18; jvm 1.8.0_262-b19
    2022-10-18 12:19:19,500 INFO  [main] o.s.jetty.server.Server: Started @6441ms
    2022-10-18 12:19:19,537 INFO  [main] o.s.j.s.AbstractConnector: Started ServerConnector@4d525897{HTTP/1.1, (http/1.1)}{0.0.0.0:4040}
    2022-10-18 12:19:19,538 INFO  [main] o.apache.spark.util.Utils: Successfully started service 'SparkUI' on port 4040.
    2022-10-18 12:19:19,573 INFO  [main] o.s.j.s.h.ContextHandler: Started o.s.j.s.ServletContextHandler@70421a08{/,null,AVAILABLE,@Spark}
    2022-10-18 12:19:19,726 INFO  [main] o.a.s.executor.Executor: Starting executor ID driver on host f9648f984b63
    2022-10-18 12:19:19,734 INFO  [main] o.a.s.executor.Executor: Starting executor with user classpath (userClassPathFirst = false): ''
    2022-10-18 12:19:19,735 INFO  [main] o.a.s.executor.Executor: Using REPL class URI: spark://f9648f984b63:39227/classes
    2022-10-18 12:19:19,764 INFO  [main] o.apache.spark.util.Utils: Successfully started service 'org.apache.spark.network.netty.NettyBlockTransferService' on port 34445.
    2022-10-18 12:19:19,764 INFO  [main] o.a.s.n.n.NettyBlockTransferService: Server created on f9648f984b63:34445
    2022-10-18 12:19:19,766 INFO  [main] o.a.s.storage.BlockManager: Using org.apache.spark.storage.RandomBlockReplicationPolicy for block replication policy
    2022-10-18 12:19:19,776 INFO  [main] o.a.s.s.BlockManagerMaster: Registering BlockManager BlockManagerId(driver, f9648f984b63, 34445, None)
    2022-10-18 12:19:19,781 INFO  [dispatcher-BlockManagerMaster] o.a.s.s.BlockManagerMasterEndpoint: Registering block manager f9648f984b63:34445 with 366.3 MiB RAM, BlockManagerId(driver, f9648f984b63, 34445, None)
    2022-10-18 12:19:19,789 INFO  [main] o.a.s.s.BlockManagerMaster: Registered BlockManager BlockManagerId(driver, f9648f984b63, 34445, None)
    2022-10-18 12:19:19,790 INFO  [main] o.a.s.storage.BlockManager: Initialized BlockManager: BlockManagerId(driver, f9648f984b63, 34445, None)
    2022-10-18 12:19:19,968 INFO  [main] o.s.j.s.h.ContextHandler: Stopped o.s.j.s.ServletContextHandler@70421a08{/,null,STOPPED,@Spark}
    2022-10-18 12:19:19,976 INFO  [main] o.s.j.s.h.ContextHandler: Started o.s.j.s.ServletContextHandler@53fc870f{/jobs,null,AVAILABLE,@Spark}
    2022-10-18 12:19:19,984 INFO  [main] o.s.j.s.h.ContextHandler: Started o.s.j.s.ServletContextHandler@43cbafa6{/jobs/json,null,AVAILABLE,@Spark}
    2022-10-18 12:19:19,985 INFO  [main] o.s.j.s.h.ContextHandler: Started o.s.j.s.ServletContextHandler@5cf3a7f9{/jobs/job,null,AVAILABLE,@Spark}
    2022-10-18 12:19:19,986 INFO  [main] o.s.j.s.h.ContextHandler: Started o.s.j.s.ServletContextHandler@6bd2f039{/jobs/job/json,null,AVAILABLE,@Spark}
    2022-10-18 12:19:19,987 INFO  [main] o.s.j.s.h.ContextHandler: Started o.s.j.s.ServletContextHandler@2d0778d0{/stages,null,AVAILABLE,@Spark}
    2022-10-18 12:19:19,989 INFO  [main] o.s.j.s.h.ContextHandler: Started o.s.j.s.ServletContextHandler@4fc71437{/stages/json,null,AVAILABLE,@Spark}
    2022-10-18 12:19:19,992 INFO  [main] o.s.j.s.h.ContextHandler: Started o.s.j.s.ServletContextHandler@64d53f0d{/stages/stage,null,AVAILABLE,@Spark}
    2022-10-18 12:19:20,003 INFO  [main] o.s.j.s.h.ContextHandler: Started o.s.j.s.ServletContextHandler@4b916cc2{/stages/stage/json,null,AVAILABLE,@Spark}
    2022-10-18 12:19:20,006 INFO  [main] o.s.j.s.h.ContextHandler: Started o.s.j.s.ServletContextHandler@323eecf8{/stages/pool,null,AVAILABLE,@Spark}
    2022-10-18 12:19:20,011 INFO  [main] o.s.j.s.h.ContextHandler: Started o.s.j.s.ServletContextHandler@6e355249{/stages/pool/json,null,AVAILABLE,@Spark}
    2022-10-18 12:19:20,012 INFO  [main] o.s.j.s.h.ContextHandler: Started o.s.j.s.ServletContextHandler@20b67366{/storage,null,AVAILABLE,@Spark}
    2022-10-18 12:19:20,013 INFO  [main] o.s.j.s.h.ContextHandler: Started o.s.j.s.ServletContextHandler@5c0ece6d{/storage/json,null,AVAILABLE,@Spark}
    2022-10-18 12:19:20,013 INFO  [main] o.s.j.s.h.ContextHandler: Started o.s.j.s.ServletContextHandler@7affee54{/storage/rdd,null,AVAILABLE,@Spark}
    2022-10-18 12:19:20,014 INFO  [main] o.s.j.s.h.ContextHandler: Started o.s.j.s.ServletContextHandler@2337bf27{/storage/rdd/json,null,AVAILABLE,@Spark}
    2022-10-18 12:19:20,015 INFO  [main] o.s.j.s.h.ContextHandler: Started o.s.j.s.ServletContextHandler@43719e98{/environment,null,AVAILABLE,@Spark}
    2022-10-18 12:19:20,015 INFO  [main] o.s.j.s.h.ContextHandler: Started o.s.j.s.ServletContextHandler@57e57dc5{/environment/json,null,AVAILABLE,@Spark}
    2022-10-18 12:19:20,016 INFO  [main] o.s.j.s.h.ContextHandler: Started o.s.j.s.ServletContextHandler@147059f8{/executors,null,AVAILABLE,@Spark}
    2022-10-18 12:19:20,017 INFO  [main] o.s.j.s.h.ContextHandler: Started o.s.j.s.ServletContextHandler@838e109{/executors/json,null,AVAILABLE,@Spark}
    2022-10-18 12:19:20,018 INFO  [main] o.s.j.s.h.ContextHandler: Started o.s.j.s.ServletContextHandler@11ee671f{/executors/threadDump,null,AVAILABLE,@Spark}
    2022-10-18 12:19:20,018 INFO  [main] o.s.j.s.h.ContextHandler: Started o.s.j.s.ServletContextHandler@57df09a7{/executors/threadDump/json,null,AVAILABLE,@Spark}
    2022-10-18 12:19:20,029 INFO  [main] o.s.j.s.h.ContextHandler: Started o.s.j.s.ServletContextHandler@81dfdee{/static,null,AVAILABLE,@Spark}
    2022-10-18 12:19:20,030 INFO  [main] o.s.j.s.h.ContextHandler: Started o.s.j.s.ServletContextHandler@5b2ff4df{/,null,AVAILABLE,@Spark}
    2022-10-18 12:19:20,032 INFO  [main] o.s.j.s.h.ContextHandler: Started o.s.j.s.ServletContextHandler@4af606e9{/api,null,AVAILABLE,@Spark}
    2022-10-18 12:19:20,033 INFO  [main] o.s.j.s.h.ContextHandler: Started o.s.j.s.ServletContextHandler@5c9e6d95{/jobs/job/kill,null,AVAILABLE,@Spark}
    2022-10-18 12:19:20,034 INFO  [main] o.s.j.s.h.ContextHandler: Started o.s.j.s.ServletContextHandler@dd07be8{/stages/stage/kill,null,AVAILABLE,@Spark}
    2022-10-18 12:19:20,039 INFO  [main] o.s.j.s.h.ContextHandler: Started o.s.j.s.ServletContextHandler@1e66bf2d{/metrics/json,null,AVAILABLE,@Spark}
    2022-10-18 12:19:20,073 INFO  [main] org.apache.spark.repl.Main: Created Spark session with Hive support
    Spark context Web UI available at http://f9648f984b63:4040
    Spark context available as 'sc' (master = local[*], app id = local-1666095559634).
    Spark session available as 'spark'.
    2022-10-18 12:19:23,869 INFO  [main] o.a.s.s.i.SharedState: Setting hive.metastore.warehouse.dir ('null') to the value of spark.sql.warehouse.dir.
    2022-10-18 12:19:23,877 INFO  [main] o.a.s.s.i.SharedState: Warehouse path is 'file:/opt/spark/work-dir/spark-warehouse'.
    2022-10-18 12:19:23,893 INFO  [main] o.s.j.s.h.ContextHandler: Started o.s.j.s.ServletContextHandler@604125bd{/SQL,null,AVAILABLE,@Spark}
    2022-10-18 12:19:23,894 INFO  [main] o.s.j.s.h.ContextHandler: Started o.s.j.s.ServletContextHandler@13e4a4a0{/SQL/json,null,AVAILABLE,@Spark}
    2022-10-18 12:19:23,895 INFO  [main] o.s.j.s.h.ContextHandler: Started o.s.j.s.ServletContextHandler@63813085{/SQL/execution,null,AVAILABLE,@Spark}
    2022-10-18 12:19:23,905 INFO  [main] o.s.j.s.h.ContextHandler: Started o.s.j.s.ServletContextHandler@5a3783e4{/SQL/execution/json,null,AVAILABLE,@Spark}
    2022-10-18 12:19:23,917 INFO  [main] o.s.j.s.h.ContextHandler: Started o.s.j.s.ServletContextHandler@180ee8dd{/static/sql,null,AVAILABLE,@Spark}
    2022-10-18 12:19:24,518 WARN  [main] o.a.spark.sql.SparkSession: Using an existing Spark session; only runtime SQL configurations will take effect.
    2022-10-18 12:19:24,533 INFO  [main] o.a.s.s.e.s.s.StateStoreCoordinatorRef: Registered StateStoreCoordinator endpoint
    2022-10-18 12:19:24,549 INFO  [main] o.s.j.s.h.ContextHandler: Started o.s.j.s.ServletContextHandler@37f37699{/StreamingQuery,null,AVAILABLE,@Spark}
    2022-10-18 12:19:24,550 INFO  [main] o.s.j.s.h.ContextHandler: Started o.s.j.s.ServletContextHandler@756695e3{/StreamingQuery/json,null,AVAILABLE,@Spark}
    2022-10-18 12:19:24,551 INFO  [main] o.s.j.s.h.ContextHandler: Started o.s.j.s.ServletContextHandler@6304ff53{/StreamingQuery/statistics,null,AVAILABLE,@Spark}
    2022-10-18 12:19:24,552 INFO  [main] o.s.j.s.h.ContextHandler: Started o.s.j.s.ServletContextHandler@54372b03{/StreamingQuery/statistics/json,null,AVAILABLE,@Spark}
    2022-10-18 12:19:24,553 INFO  [main] o.s.j.s.h.ContextHandler: Started o.s.j.s.ServletContextHandler@538ee7ab{/static/sql,null,AVAILABLE,@Spark}
    12:19:24.555 [main] INFO  io.dataos.flare.instrumentation.StreamingQueryMetricsListener$ - Initialize stream listener
    12:19:25.465 [main] INFO  io.dataos.flare.Job - Loading city_ingest table...
    2022-10-18 12:19:25,519 INFO  [main] o.e.hadoop.util.Version: Elasticsearch Hadoop v8.3.1 [2b824b4c2a]
    2022-10-18 12:19:25,808 INFO  [main] o.a.s.s.e.d.InMemoryFileIndex: It took 30 ms to list leaf files for 1 paths.
    2022-10-18 12:19:25,861 INFO  [main] o.a.s.s.e.d.InMemoryFileIndex: It took 1 ms to list leaf files for 1 paths.
    2022-10-18 12:19:26,194 INFO  [main] o.a.s.s.e.d.FileSourceStrategy: Pushed Filters: 
    2022-10-18 12:19:26,195 INFO  [main] o.a.s.s.e.d.FileSourceStrategy: Post-Scan Filters: (length(trim(value#50, None)) > 0)
    2022-10-18 12:19:26,197 INFO  [main] o.a.s.s.e.d.FileSourceStrategy: Output Data Schema: struct<value: string>
    2022-10-18 12:19:26,468 INFO  [main] o.a.s.s.c.e.c.CodeGenerator: Code generated in 144.894373 ms
    2022-10-18 12:19:26,514 INFO  [main] o.a.s.s.memory.MemoryStore: Block broadcast_0 stored as values in memory (estimated size 359.7 KiB, free 365.9 MiB)
    2022-10-18 12:19:26,565 INFO  [main] o.a.s.s.memory.MemoryStore: Block broadcast_0_piece0 stored as bytes in memory (estimated size 34.7 KiB, free 365.9 MiB)
    2022-10-18 12:19:26,568 INFO  [dispatcher-BlockManagerMaster] o.a.s.s.BlockManagerInfo: Added broadcast_0_piece0 in memory on f9648f984b63:34445 (size: 34.7 KiB, free: 366.3 MiB)
    2022-10-18 12:19:26,572 INFO  [main] o.a.spark.SparkContext: Created broadcast 0 from load at FilesInput.scala:66
    2022-10-18 12:19:26,580 INFO  [main] o.a.s.s.e.FileSourceScanExec: Planning scan with bin packing, max size: 4194304 bytes, open cost is considered as scanning 4194304 bytes.
    2022-10-18 12:19:26,680 INFO  [main] o.a.spark.SparkContext: Starting job: load at FilesInput.scala:66
    2022-10-18 12:19:26,695 INFO  [dag-scheduler-event-loop] o.a.s.s.DAGScheduler: Got job 0 (load at FilesInput.scala:66) with 1 output partitions
    2022-10-18 12:19:26,695 INFO  [dag-scheduler-event-loop] o.a.s.s.DAGScheduler: Final stage: ResultStage 0 (load at FilesInput.scala:66)
    2022-10-18 12:19:26,696 INFO  [dag-scheduler-event-loop] o.a.s.s.DAGScheduler: Parents of final stage: List()
    2022-10-18 12:19:26,696 INFO  [dag-scheduler-event-loop] o.a.s.s.DAGScheduler: Missing parents: List()
    2022-10-18 12:19:26,699 INFO  [dag-scheduler-event-loop] o.a.s.s.DAGScheduler: Submitting ResultStage 0 (MapPartitionsRDD[3] at load at FilesInput.scala:66), which has no missing parents
    2022-10-18 12:19:26,764 INFO  [dag-scheduler-event-loop] o.a.s.s.memory.MemoryStore: Block broadcast_1 stored as values in memory (estimated size 11.8 KiB, free 365.9 MiB)
    2022-10-18 12:19:26,773 INFO  [dag-scheduler-event-loop] o.a.s.s.memory.MemoryStore: Block broadcast_1_piece0 stored as bytes in memory (estimated size 5.9 KiB, free 365.9 MiB)
    2022-10-18 12:19:26,774 INFO  [dispatcher-BlockManagerMaster] o.a.s.s.BlockManagerInfo: Added broadcast_1_piece0 in memory on f9648f984b63:34445 (size: 5.9 KiB, free: 366.3 MiB)
    2022-10-18 12:19:26,775 INFO  [dag-scheduler-event-loop] o.a.spark.SparkContext: Created broadcast 1 from broadcast at DAGScheduler.scala:1513
    2022-10-18 12:19:26,785 INFO  [dag-scheduler-event-loop] o.a.s.s.DAGScheduler: Submitting 1 missing tasks from ResultStage 0 (MapPartitionsRDD[3] at load at FilesInput.scala:66) (first 15 tasks are for partitions Vector(0))
    2022-10-18 12:19:26,786 INFO  [dag-scheduler-event-loop] o.a.s.s.TaskSchedulerImpl: Adding task set 0.0 with 1 tasks resource profile 0
    2022-10-18 12:19:26,836 INFO  [dispatcher-event-loop-3] o.a.s.s.TaskSetManager: Starting task 0.0 in stage 0.0 (TID 0) (f9648f984b63, executor driver, partition 0, PROCESS_LOCAL, 4921 bytes) taskResourceAssignments Map()
    2022-10-18 12:19:26,853 INFO  [Executor task launch worker for task 0.0 in stage 0.0 (TID 0)] o.a.s.executor.Executor: Running task 0.0 in stage 0.0 (TID 0)
    2022-10-18 12:19:27,061 INFO  [Executor task launch worker for task 0.0 in stage 0.0 (TID 0)] o.a.s.s.e.d.FileScanRDD: Reading File path: file:///data/examples/city_ingestion/ingestion.csv, range: 0-133438, partition values: [empty row]
    2022-10-18 12:19:27,134 INFO  [Executor task launch worker for task 0.0 in stage 0.0 (TID 0)] o.a.s.n.c.TransportClientFactory: Successfully created connection to f9648f984b63/172.17.0.2:39227 after 34 ms (0 ms spent in bootstraps)
    2022-10-18 12:19:27,164 INFO  [Executor task launch worker for task 0.0 in stage 0.0 (TID 0)] o.a.s.s.c.e.c.CodeGenerator: Code generated in 99.292532 ms
    2022-10-18 12:19:27,216 INFO  [Executor task launch worker for task 0.0 in stage 0.0 (TID 0)] o.a.s.executor.Executor: Finished task 0.0 in stage 0.0 (TID 0). 1618 bytes result sent to driver
    2022-10-18 12:19:27,223 INFO  [task-result-getter-0] o.a.s.s.TaskSetManager: Finished task 0.0 in stage 0.0 (TID 0) in 398 ms on f9648f984b63 (executor driver) (1/1)
    2022-10-18 12:19:27,226 INFO  [task-result-getter-0] o.a.s.s.TaskSchedulerImpl: Removed TaskSet 0.0, whose tasks have all completed, from pool 
    2022-10-18 12:19:27,233 INFO  [dag-scheduler-event-loop] o.a.s.s.DAGScheduler: ResultStage 0 (load at FilesInput.scala:66) finished in 0.520 s
    2022-10-18 12:19:27,236 INFO  [dag-scheduler-event-loop] o.a.s.s.DAGScheduler: Job 0 is finished. Cancelling potential speculative or zombie tasks for this job
    2022-10-18 12:19:27,237 INFO  [dag-scheduler-event-loop] o.a.s.s.TaskSchedulerImpl: Killing all running tasks in stage 0: Stage finished
    2022-10-18 12:19:27,239 INFO  [main] o.a.s.s.DAGScheduler: Job 0 finished: load at FilesInput.scala:66, took 0.558507 s
    2022-10-18 12:19:27,274 INFO  [main] o.a.s.s.c.e.c.CodeGenerator: Code generated in 20.580652 ms
    2022-10-18 12:19:27,334 INFO  [main] o.a.s.s.e.d.FileSourceStrategy: Pushed Filters: 
    2022-10-18 12:19:27,334 INFO  [main] o.a.s.s.e.d.FileSourceStrategy: Post-Scan Filters: 
    2022-10-18 12:19:27,334 INFO  [main] o.a.s.s.e.d.FileSourceStrategy: Output Data Schema: struct<value: string>
    2022-10-18 12:19:27,342 INFO  [main] o.a.s.s.memory.MemoryStore: Block broadcast_2 stored as values in memory (estimated size 359.7 KiB, free 365.5 MiB)
    2022-10-18 12:19:27,350 INFO  [main] o.a.s.s.memory.MemoryStore: Block broadcast_2_piece0 stored as bytes in memory (estimated size 34.7 KiB, free 365.5 MiB)
    2022-10-18 12:19:27,351 INFO  [dispatcher-BlockManagerMaster] o.a.s.s.BlockManagerInfo: Added broadcast_2_piece0 in memory on f9648f984b63:34445 (size: 34.7 KiB, free: 366.2 MiB)
    2022-10-18 12:19:27,352 INFO  [main] o.a.spark.SparkContext: Created broadcast 2 from load at FilesInput.scala:66
    2022-10-18 12:19:27,353 INFO  [main] o.a.s.s.e.FileSourceScanExec: Planning scan with bin packing, max size: 4194304 bytes, open cost is considered as scanning 4194304 bytes.
    12:19:27.409 [main] INFO  io.dataos.flare.Job - flare.conf.keepSystemColumns not set. Will delete the system columns
    12:19:27.410 [main] INFO  io.dataos.flare.Job - flare.conf.keepSystemColumns set to true, deleting the system columns
    12:19:27.475 [main] INFO  io.dataos.flare.step.StepFileExecutor$ - execute step file isRefreshing: false
    12:19:27.554 [main] INFO  io.dataos.flare.step.Step - calculating step cities
    12:19:27.640 [main] INFO  io.dataos.flare.step.Step - write _dataos_job_name=_dataos_run_mapper_id=
    root
     |-- __metadata: map (nullable = false)
     |    |-- key: string
     |    |-- value: string (valueContainsNull = false)
     |-- city_id: string (nullable = true)
     |-- city_name: string (nullable = true)
     |-- county_name: string (nullable = true)
     |-- state_code: string (nullable = true)
     |-- state_name: string (nullable = true)
     |-- zip_code: string (nullable = true)
    
    12:19:27.697 [main] INFO  io.dataos.flare.step.Step - write dataFrameName=[__metadata: map<string,string>, city_id: string ... 5 more fields] isStreaming=false isRefreshing=false
    Schema=
    ()
    12:19:27.697 [main] INFO  io.dataos.flare.step.Step - writing cities
    12:19:27.697 [main] INFO  io.dataos.flare.output.writers.file.IcebergOutputWriter - writing iceberg batch...
    2022-10-18 12:19:27,801 INFO  [main] o.a.i.BaseMetastoreCatalog: Table properties set at catalog level through catalog properties: {}
    2022-10-18 12:19:27,802 INFO  [main] o.a.i.BaseMetastoreCatalog: Table properties enforced at catalog level through catalog properties: {}
    2022-10-18 12:19:28,338 INFO  [dispatcher-BlockManagerMaster] o.a.s.s.BlockManagerInfo: Removed broadcast_0_piece0 on f9648f984b63:34445 in memory (size: 34.7 KiB, free: 366.3 MiB)
    2022-10-18 12:19:28,361 INFO  [dispatcher-BlockManagerMaster] o.a.s.s.BlockManagerInfo: Removed broadcast_1_piece0 on f9648f984b63:34445 in memory (size: 5.9 KiB, free: 366.3 MiB)
    2022-10-18 12:19:28,381 INFO  [dispatcher-BlockManagerMaster] o.a.s.s.BlockManagerInfo: Removed broadcast_2_piece0 on f9648f984b63:34445 in memory (size: 34.7 KiB, free: 366.3 MiB)
    2022-10-18 12:19:28,384 INFO  [main] o.a.i.h.HadoopTableOperations: Committed a new metadata file /dataout/city/metadata/v1.gz.metadata.json
    2022-10-18 12:19:28,450 INFO  [main] o.a.i.BaseMetastoreCatalog: Table loaded by catalog: hadoop.city
    12:19:28.451 [main] INFO  io.dataos.flare.output.writers.file.IcebergOutputWriter - no metastore configured skipping table creation in metastore.
    12:19:28.503 [main] ERROR io.dataos.flare.standalone.Standalone$ - org.apache.spark.sql.AnalysisException: Column 'version' does not exist. Did you mean one of the following? [__metadata, cities.city_id, cities.zip_code, cities.city_name, cities.state_code, cities.state_name, cities.county_name];
    'Sort ['version DESC NULLS LAST], false
    +- Project [map(_dataos_run_mapper_id, , id, uuid(Some(1398746933352070557))) AS __metadata#178, city_id#68, city_name#69, county_name#70, state_code#71, state_name#72, zip_code#73]
       +- SubqueryAlias cities
          +- View (`cities`, [city_id#68,city_name#69,county_name#70,state_code#71,state_name#72,zip_code#73])
             +- GlobalLimit 10
                +- LocalLimit 10
                   +- Project [city_id#68, city_name#69, county_name#70, state_code#71, state_name#72, zip_code#73]
                      +- SubqueryAlias city_ingest
                         +- View (`city_ingest`, [city_id#68,city_name#69,county_name#70,state_code#71,state_name#72,zip_code#73])
                            +- Project [city_id#68, city_name#69, county_name#70, state_code#71, state_name#72, zip_code#73]
                               +- Relation [__metadata#67,city_id#68,city_name#69,county_name#70,state_code#71,state_name#72,zip_code#73] csv
    
    io.dataos.flare.exceptions.FlareWriteFailedException: Failed to write dataFrame: cities to output: Iceberg on step: 3f0550d8-26b0-4ebb-8553-206ce4f0fd40.yaml
    	at io.dataos.flare.step.Step.writeBatch(Step.scala:100) ~[flare.jar:0.0.60-SNAPSHOT]
    	at io.dataos.flare.step.Step.$anonfun$write$1(Step.scala:170) ~[flare.jar:0.0.60-SNAPSHOT]
    	at scala.collection.immutable.List.foreach(List.scala:431) ~[scala-library-2.12.15.jar:?]
    	at io.dataos.flare.step.Step.write(Step.scala:121) ~[flare.jar:0.0.60-SNAPSHOT]
    	at io.dataos.flare.step.StepSet.$anonfun$run$1(StepSet.scala:34) ~[flare.jar:0.0.60-SNAPSHOT]
    	at io.dataos.flare.step.StepSet.$anonfun$run$1$adapted(StepSet.scala:29) ~[flare.jar:0.0.60-SNAPSHOT]
    	at scala.collection.immutable.List.foreach(List.scala:431) ~[scala-library-2.12.15.jar:?]
    	at scala.collection.generic.TraversableForwarder.foreach(TraversableForwarder.scala:38) ~[scala-library-2.12.15.jar:?]
    	at scala.collection.generic.TraversableForwarder.foreach$(TraversableForwarder.scala:38) ~[scala-library-2.12.15.jar:?]
    	at scala.collection.mutable.ListBuffer.foreach(ListBuffer.scala:47) ~[scala-library-2.12.15.jar:?]
    	at io.dataos.flare.step.StepSet.run(StepSet.scala:29) ~[flare.jar:0.0.60-SNAPSHOT]
    	at io.dataos.flare.step.StepFileExecutor$.execute(StepFileExecutor.scala:14) ~[flare.jar:0.0.60-SNAPSHOT]
    	at io.dataos.flare.standalone.Standalone$.process(Standalone.scala:131) ~[flare.jar:0.0.60-SNAPSHOT]
    	at io.dataos.flare.standalone.Standalone$.reload(Standalone.scala:21) ~[flare.jar:0.0.60-SNAPSHOT]
    	at io.dataos.flare.standalone.Standalone$.start(Standalone.scala:29) ~[flare.jar:0.0.60-SNAPSHOT]
    	at $line14.$read$$iw$$iw$$iw$$iw$$iw$$iw$$iw$$iw.<init>(/opt/spark/work-dir/standalone.scala:27) ~[scala-library-2.12.15.jar:?]
    	at $line14.$read$$iw$$iw$$iw$$iw$$iw$$iw$$iw.<init>(/opt/spark/work-dir/standalone.scala:33) ~[scala-library-2.12.15.jar:?]
    	at $line14.$read$$iw$$iw$$iw$$iw$$iw$$iw.<init>(/opt/spark/work-dir/standalone.scala:35) ~[scala-library-2.12.15.jar:?]
    	at $line14.$read$$iw$$iw$$iw$$iw$$iw.<init>(/opt/spark/work-dir/standalone.scala:37) ~[scala-library-2.12.15.jar:?]
    	at $line14.$read$$iw$$iw$$iw$$iw.<init>(/opt/spark/work-dir/standalone.scala:39) ~[scala-library-2.12.15.jar:?]
    	at $line14.$read$$iw$$iw$$iw.<init>(/opt/spark/work-dir/standalone.scala:41) ~[scala-library-2.12.15.jar:?]
    	at $line14.$read$$iw$$iw.<init>(/opt/spark/work-dir/standalone.scala:43) ~[scala-library-2.12.15.jar:?]
    	at $line14.$read$$iw.<init>(/opt/spark/work-dir/standalone.scala:45) ~[scala-library-2.12.15.jar:?]
    	at $line14.$read.<init>(/opt/spark/work-dir/standalone.scala:47) ~[scala-library-2.12.15.jar:?]
    	at $line14.$read$.<init>(/opt/spark/work-dir/standalone.scala:51) ~[scala-library-2.12.15.jar:?]
    	at $line14.$read$.<clinit>(/opt/spark/work-dir/standalone.scala) ~[scala-library-2.12.15.jar:?]
    	at $line14.$eval$.$print$lzycompute(/opt/spark/work-dir/standalone.scala:7) ~[scala-library-2.12.15.jar:?]
    	at $line14.$eval$.$print(/opt/spark/work-dir/standalone.scala:6) ~[scala-library-2.12.15.jar:?]
    	at $line14.$eval.$print(/opt/spark/work-dir/standalone.scala) ~[scala-library-2.12.15.jar:?]
    	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method) ~[?:1.8.0_262]
    	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62) ~[?:1.8.0_262]
    	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43) ~[?:1.8.0_262]
    	at java.lang.reflect.Method.invoke(Method.java:498) ~[?:1.8.0_262]
    	at scala.tools.nsc.interpreter.IMain$ReadEvalPrint.call(IMain.scala:747) ~[scala-compiler-2.12.15.jar:?]
    	at scala.tools.nsc.interpreter.IMain$Request.loadAndRun(IMain.scala:1020) ~[scala-compiler-2.12.15.jar:?]
    	at scala.tools.nsc.interpreter.IMain.$anonfun$interpret$1(IMain.scala:568) ~[scala-compiler-2.12.15.jar:?]
    	at scala.reflect.internal.util.ScalaClassLoader.asContext(ScalaClassLoader.scala:36) ~[scala-reflect-2.12.15.jar:?]
    	at scala.reflect.internal.util.ScalaClassLoader.asContext$(ScalaClassLoader.scala:116) ~[scala-reflect-2.12.15.jar:?]
    	at scala.reflect.internal.util.AbstractFileClassLoader.asContext(AbstractFileClassLoader.scala:41) ~[scala-reflect-2.12.15.jar:?]
    	at scala.tools.nsc.interpreter.IMain.loadAndRunReq$1(IMain.scala:567) ~[scala-compiler-2.12.15.jar:?]
    	at scala.tools.nsc.interpreter.IMain.interpret(IMain.scala:594) ~[scala-compiler-2.12.15.jar:?]
    	at scala.tools.nsc.interpreter.IMain.interpret(IMain.scala:564) ~[scala-compiler-2.12.15.jar:?]
    	at scala.tools.nsc.interpreter.ILoop.$anonfun$pasteCommand$11(ILoop.scala:795) ~[scala-compiler-2.12.15.jar:?]
    	at scala.tools.nsc.interpreter.IMain.withLabel(IMain.scala:111) ~[scala-compiler-2.12.15.jar:?]
    	at scala.tools.nsc.interpreter.ILoop.interpretCode$1(ILoop.scala:795) ~[scala-compiler-2.12.15.jar:?]
    	at scala.tools.nsc.interpreter.ILoop.pasteCommand(ILoop.scala:801) ~[scala-compiler-2.12.15.jar:?]
    	at org.apache.spark.repl.SparkILoop.$anonfun$process$8(SparkILoop.scala:180) ~[spark-repl_2.12-3.3.0.jar:3.3.0]
    	at org.apache.spark.repl.SparkILoop.$anonfun$process$8$adapted(SparkILoop.scala:179) ~[spark-repl_2.12-3.3.0.jar:3.3.0]
    	at scala.collection.immutable.List.foreach(List.scala:431) ~[scala-library-2.12.15.jar:?]
    	at org.apache.spark.repl.SparkILoop.loadInitFiles$1(SparkILoop.scala:179) ~[spark-repl_2.12-3.3.0.jar:3.3.0]
    	at org.apache.spark.repl.SparkILoop.$anonfun$process$4(SparkILoop.scala:169) ~[spark-repl_2.12-3.3.0.jar:3.3.0]
    	at scala.runtime.java8.JFunction0$mcV$sp.apply(JFunction0$mcV$sp.java:23) ~[scala-library-2.12.15.jar:?]
    	at scala.tools.nsc.interpreter.ILoop.$anonfun$mumly$1(ILoop.scala:166) ~[scala-compiler-2.12.15.jar:?]
    	at scala.tools.nsc.interpreter.IMain.beQuietDuring(IMain.scala:206) ~[scala-compiler-2.12.15.jar:?]
    	at scala.tools.nsc.interpreter.ILoop.mumly(ILoop.scala:163) ~[scala-compiler-2.12.15.jar:?]
    	at org.apache.spark.repl.SparkILoop.loopPostInit$1(SparkILoop.scala:156) ~[spark-repl_2.12-3.3.0.jar:3.3.0]
    	at org.apache.spark.repl.SparkILoop.$anonfun$process$10(SparkILoop.scala:224) ~[spark-repl_2.12-3.3.0.jar:3.3.0]
    	at org.apache.spark.repl.SparkILoop.withSuppressedSettings$1(SparkILoop.scala:192) ~[spark-repl_2.12-3.3.0.jar:3.3.0]
    	at org.apache.spark.repl.SparkILoop.startup$1(SparkILoop.scala:204) ~[spark-repl_2.12-3.3.0.jar:3.3.0]
    	at org.apache.spark.repl.SparkILoop.process(SparkILoop.scala:239) ~[spark-repl_2.12-3.3.0.jar:3.3.0]
    	at org.apache.spark.repl.Main$.doMain(Main.scala:78) ~[spark-repl_2.12-3.3.0.jar:3.3.0]
    	at org.apache.spark.repl.Main$.main(Main.scala:58) ~[spark-repl_2.12-3.3.0.jar:3.3.0]
    	at org.apache.spark.repl.Main.main(Main.scala) ~[spark-repl_2.12-3.3.0.jar:3.3.0]
    	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method) ~[?:1.8.0_262]
    	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62) ~[?:1.8.0_262]
    	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43) ~[?:1.8.0_262]
    	at java.lang.reflect.Method.invoke(Method.java:498) ~[?:1.8.0_262]
    	at org.apache.spark.deploy.JavaMainApplication.start(SparkApplication.scala:52) ~[spark-core_2.12-3.3.0.jar:3.3.0]
    	at org.apache.spark.deploy.SparkSubmit.org$apache$spark$deploy$SparkSubmit$$runMain(SparkSubmit.scala:961) ~[spark-core_2.12-3.3.0.jar:3.3.0]
    	at org.apache.spark.deploy.SparkSubmit.doRunMain$1(SparkSubmit.scala:183) ~[spark-core_2.12-3.3.0.jar:3.3.0]
    	at org.apache.spark.deploy.SparkSubmit.submit(SparkSubmit.scala:206) ~[spark-core_2.12-3.3.0.jar:3.3.0]
    	at org.apache.spark.deploy.SparkSubmit.doSubmit(SparkSubmit.scala:90) ~[spark-core_2.12-3.3.0.jar:3.3.0]
    	at org.apache.spark.deploy.SparkSubmit$$anon$2.doSubmit(SparkSubmit.scala:1049) ~[spark-core_2.12-3.3.0.jar:3.3.0]
    	at org.apache.spark.deploy.SparkSubmit$.main(SparkSubmit.scala:1058) ~[spark-core_2.12-3.3.0.jar:3.3.0]
    	at org.apache.spark.deploy.SparkSubmit.main(SparkSubmit.scala) ~[spark-core_2.12-3.3.0.jar:3.3.0]
    Caused by: org.apache.spark.sql.AnalysisException: Column 'version' does not exist. Did you mean one of the following? [__metadata, cities.city_id, cities.zip_code, cities.city_name, cities.state_code, cities.state_name, cities.county_name];
    'Sort ['version DESC NULLS LAST], false
    +- Project [map(_dataos_run_mapper_id, , id, uuid(Some(1398746933352070557))) AS __metadata#178, city_id#68, city_name#69, county_name#70, state_code#71, state_name#72, zip_code#73]
       +- SubqueryAlias cities
          +- View (`cities`, [city_id#68,city_name#69,county_name#70,state_code#71,state_name#72,zip_code#73])
             +- GlobalLimit 10
                +- LocalLimit 10
                   +- Project [city_id#68, city_name#69, county_name#70, state_code#71, state_name#72, zip_code#73]
                      +- SubqueryAlias city_ingest
                         +- View (`city_ingest`, [city_id#68,city_name#69,county_name#70,state_code#71,state_name#72,zip_code#73])
                            +- Project [city_id#68, city_name#69, county_name#70, state_code#71, state_name#72, zip_code#73]
                               +- Relation [__metadata#67,city_id#68,city_name#69,county_name#70,state_code#71,state_name#72,zip_code#73] csv
    
    	at org.apache.spark.sql.catalyst.analysis.package$AnalysisErrorAt.failAnalysis(package.scala:54) ~[spark-catalyst_2.12-3.3.0.jar:3.3.0]
    	at org.apache.spark.sql.catalyst.analysis.CheckAnalysis.$anonfun$checkAnalysis$7(CheckAnalysis.scala:199) ~[spark-catalyst_2.12-3.3.0.jar:3.3.0]
    	at org.apache.spark.sql.catalyst.analysis.CheckAnalysis.$anonfun$checkAnalysis$7$adapted(CheckAnalysis.scala:192) ~[spark-catalyst_2.12-3.3.0.jar:3.3.0]
    	at org.apache.spark.sql.catalyst.trees.TreeNode.foreachUp(TreeNode.scala:367) ~[spark-catalyst_2.12-3.3.0.jar:3.3.0]
    	at org.apache.spark.sql.catalyst.trees.TreeNode.$anonfun$foreachUp$1(TreeNode.scala:366) ~[spark-catalyst_2.12-3.3.0.jar:3.3.0]
    	at org.apache.spark.sql.catalyst.trees.TreeNode.$anonfun$foreachUp$1$adapted(TreeNode.scala:366) ~[spark-catalyst_2.12-3.3.0.jar:3.3.0]
    	at scala.collection.immutable.List.foreach(List.scala:431) ~[scala-library-2.12.15.jar:?]
    	at org.apache.spark.sql.catalyst.trees.TreeNode.foreachUp(TreeNode.scala:366) ~[spark-catalyst_2.12-3.3.0.jar:3.3.0]
    	at org.apache.spark.sql.catalyst.analysis.CheckAnalysis.$anonfun$checkAnalysis$6(CheckAnalysis.scala:192) ~[spark-catalyst_2.12-3.3.0.jar:3.3.0]
    	at org.apache.spark.sql.catalyst.analysis.CheckAnalysis.$anonfun$checkAnalysis$6$adapted(CheckAnalysis.scala:192) ~[spark-catalyst_2.12-3.3.0.jar:3.3.0]
    	at scala.collection.immutable.Stream.foreach(Stream.scala:533) ~[scala-library-2.12.15.jar:?]
    	at org.apache.spark.sql.catalyst.analysis.CheckAnalysis.$anonfun$checkAnalysis$1(CheckAnalysis.scala:192) ~[spark-catalyst_2.12-3.3.0.jar:3.3.0]
    	at org.apache.spark.sql.catalyst.analysis.CheckAnalysis.$anonfun$checkAnalysis$1$adapted(CheckAnalysis.scala:101) ~[spark-catalyst_2.12-3.3.0.jar:3.3.0]
    	at org.apache.spark.sql.catalyst.trees.TreeNode.foreachUp(TreeNode.scala:367) ~[spark-catalyst_2.12-3.3.0.jar:3.3.0]
    	at org.apache.spark.sql.catalyst.analysis.CheckAnalysis.checkAnalysis(CheckAnalysis.scala:101) ~[spark-catalyst_2.12-3.3.0.jar:3.3.0]
    	at org.apache.spark.sql.catalyst.analysis.CheckAnalysis.checkAnalysis$(CheckAnalysis.scala:96) ~[spark-catalyst_2.12-3.3.0.jar:3.3.0]
    	at org.apache.spark.sql.catalyst.analysis.Analyzer.checkAnalysis(Analyzer.scala:187) ~[spark-catalyst_2.12-3.3.0.jar:3.3.0]
    	at org.apache.spark.sql.catalyst.analysis.Analyzer.$anonfun$executeAndCheck$1(Analyzer.scala:210) ~[spark-catalyst_2.12-3.3.0.jar:3.3.0]
    	at org.apache.spark.sql.catalyst.plans.logical.AnalysisHelper$.markInAnalyzer(AnalysisHelper.scala:330) ~[spark-catalyst_2.12-3.3.0.jar:3.3.0]
    	at org.apache.spark.sql.catalyst.analysis.Analyzer.executeAndCheck(Analyzer.scala:207) ~[spark-catalyst_2.12-3.3.0.jar:3.3.0]
    	at org.apache.spark.sql.execution.QueryExecution.$anonfun$analyzed$1(QueryExecution.scala:76) ~[spark-sql_2.12-3.3.0.jar:3.3.0]
    	at org.apache.spark.sql.catalyst.QueryPlanningTracker.measurePhase(QueryPlanningTracker.scala:111) ~[spark-catalyst_2.12-3.3.0.jar:3.3.0]
    	at org.apache.spark.sql.execution.QueryExecution.$anonfun$executePhase$2(QueryExecution.scala:185) ~[spark-sql_2.12-3.3.0.jar:3.3.0]
    	at org.apache.spark.sql.execution.QueryExecution$.withInternalError(QueryExecution.scala:510) ~[spark-sql_2.12-3.3.0.jar:3.3.0]
    	at org.apache.spark.sql.execution.QueryExecution.$anonfun$executePhase$1(QueryExecution.scala:185) ~[spark-sql_2.12-3.3.0.jar:3.3.0]
    	at org.apache.spark.sql.SparkSession.withActive(SparkSession.scala:779) ~[spark-sql_2.12-3.3.0.jar:3.3.0]
    	at org.apache.spark.sql.execution.QueryExecution.executePhase(QueryExecution.scala:184) ~[spark-sql_2.12-3.3.0.jar:3.3.0]
    	at org.apache.spark.sql.execution.QueryExecution.analyzed$lzycompute(QueryExecution.scala:76) ~[spark-sql_2.12-3.3.0.jar:3.3.0]
    	at org.apache.spark.sql.execution.QueryExecution.analyzed(QueryExecution.scala:74) ~[spark-sql_2.12-3.3.0.jar:3.3.0]
    	at org.apache.spark.sql.execution.QueryExecution.assertAnalyzed(QueryExecution.scala:66) ~[spark-sql_2.12-3.3.0.jar:3.3.0]
    	at org.apache.spark.sql.Dataset.<init>(Dataset.scala:206) ~[spark-sql_2.12-3.3.0.jar:3.3.0]
    	at org.apache.spark.sql.Dataset.<init>(Dataset.scala:212) ~[spark-sql_2.12-3.3.0.jar:3.3.0]
    	at org.apache.spark.sql.Dataset$.apply(Dataset.scala:76) ~[spark-sql_2.12-3.3.0.jar:3.3.0]
    	at org.apache.spark.sql.Dataset.withTypedPlan(Dataset.scala:3892) ~[spark-sql_2.12-3.3.0.jar:3.3.0]
    	at org.apache.spark.sql.Dataset.sortInternal(Dataset.scala:3880) ~[spark-sql_2.12-3.3.0.jar:3.3.0]
    	at org.apache.spark.sql.Dataset.sortWithinPartitions(Dataset.scala:1322) ~[spark-sql_2.12-3.3.0.jar:3.3.0]
    	at io.dataos.flare.output.writers.file.FileOutputWriter.write(FileOutputWriter.scala:153) ~[flare.jar:0.0.60-SNAPSHOT]
    	at io.dataos.flare.output.writers.file.IcebergOutputWriter.write(IcebergOutputWriter.scala:35) ~[flare.jar:0.0.60-SNAPSHOT]
    	at io.dataos.flare.step.Step.writeBatch(Step.scala:95) ~[flare.jar:0.0.60-SNAPSHOT]
    	... 74 more
    Flare session is available as flare.
        Welcome to
             ______   _                       
            |  ____| | |                      
            | |__    | |   __ _   _ __    ___ 
            |  __|   | |  / _` | | '__|  / _ \
            | |      | | | (_| | | |    |  __/
            |_|      |_|  \__,_| |_|     \___|  version 1.2.0
            
        Powered by Apache Spark 3.3.0
    Using Scala version 2.12.15 (OpenJDK 64-Bit Server VM, Java 1.8.0_262)
    Type in expressions to have them evaluated.
    Type :help for more information.
    ```
    

## **Step 4: Check the output**

**Run the tables command**

This shows the various tables within the directory that you mounted

```bash
scala> tables
```

```bash
+---------+-----------+-----------+
|namespace|tableName  |isTemporary|
+---------+-----------+-----------+
|         |cities     |true       |
|         |city_ingest|true       |
+---------+-----------+-----------+
```

**Run the printSchema command**

```bash
scala> spark.sql("select * from city_ingest").printSchema
```

```bash
root
 |-- city_id: string (nullable = true)
 |-- city_name: string (nullable = true)
 |-- county_name: string (nullable = true)
 |-- state_code: string (nullable = true)
 |-- state_name: string (nullable = true)
 |-- zip_code: string (nullable = true)
```

> 🗣️ In the situation when you don’t get the expected output, you will have to check the logs and figure out where the thing went wrong.