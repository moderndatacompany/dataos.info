# Quick Guide for Flare Workflow


DataOS uses Flare Workflows to carry out large-scale data transformation, ingestion, syndication, and even a combination of these tasks.

<div style="text-align: center;">
  <img src="/resources/stacks/flare/basic_concepts/diagram_03.jpg" alt="diagram 03.jpg" style="border:1px solid black; width: 80%; height: auto box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.3);">
</div>


Flare is a declarative stack designed to process large-scale data Workflows using sequential manifest configurations. In contrast, a Workflow is a primitive, or Resource, within DataOS that executes a defined sequence of jobs in a specific order. Each Workflow is represented as a Directed Acyclic Graph (DAG) of jobs. For additional information on Workflows, refer to the [Workflow Resource documentation](/resources/workflow/).


<aside class="callout">

🗣️ In this section and all subsequent sections, the term Flare Workflow refers to a Workflow represented as a Directed Acyclic Graph (DAG) that includes one or more jobs utilizing the Flare stack. To submit a job that uses the Flare stack (referred to as a Flare Job), a Workflow must be defined.

</aside>

## Deep Diving into a Flare Job

A job defines a transformation task based on a specific scenario or use case. Each job requires a supporting stack to execute the task and is fully dependent on the successful completion of its preceding job. For example, a **Flare Job** represents a data processing workload—such as ingestion, transformation, profiling, or syndication—executed on the Flare stack.

In the manifest configuration, a Flare Job defined within a DAG consists of three main sections:

* **Input**: Specifies the data source.
* **Output**: Specifies the data destination.
* **Steps**: Defines the data transformation logic.


![Build.svg](/resources/stacks/flare/basic_concepts/build.svg)


In order to grasp the intricacies of creating a Flare Job and the process of testing and deploying it, we shall explore a specific example of Data Ingestion. The data ingestion process will involve acquiring batch data in CSV format from an external source, applying various transformations on top of it, and ultimately storing the data within DataOS internal storage, Icebase.

However, before delving into the technical aspects of this task, it is vital to verify certain prerequisites for smooth execution.

## Prerequisites

### **Required Permissions**

Before executing a Flare Workflow, the necessary permission tags must be in place. To run a Flare Workflow using the CLI, the following tags are required:

* `roles:id:data-dev`
* `roles:id:system-dev`

> A `Forbidden Error` will be returned if the required permissions are not assigned.

The following command can be used to verify the assigned permission tags. Authentication to the DataOS CLI must be completed prior to executing the command.

```bash
dataos-ctl user get

#expected Output

INFO[0000] 😃 user get...                           
INFO[0000] 😃 user get...complete

      NAME     |     ID      |  TYPE  |        EMAIL         |              TAGS               
---------------|-------------|--------|----------------------|---------------------------------
    IamGroot   |   iamgroot  | person |   iamgroot@tmdc.io   | roles:id:data-dev,
               |             |        |                      | roles:id:system-dev,            
               |             |        |                      | roles:id:user,                  
               |             |        |                      | users:id:iamgroot
```

> **Note:** If the required permission tags are not assigned, contact an administrator within the organization who holds Operator-level permissions. The administrator is responsible for assigning the necessary tags to enable Workflow execution.



### **Check the required Depot**

To execute a Flare Workflow, Depots must be configured to interface with both source and sink systems for data read and write operations. To retrieve a list of Depots created by all DataOS users, execute the following command in the CLI:

```bash
dataos-ctl resource get -t depot -a

# Expected Output
INFO[0000] 🔍 get...                                     
INFO[0000] 🔍 get...complete                             

        NAME      | VERSION | TYPE  | WORKSPACE | STATUS  |  RUNTIME  |          OWNER           
-----------------|---------|-------|-----------|---------|-----------|--------------------------
  lakehouse01        | v2alpha     | depot |           | active  | running:1 | dataos-resource-manager  
  redshiftdepot  | v2alpha     | depot |           | active  |           | user03                
  retail         | v2alpha     | depot |           | active  | running:1 | user02             
  snowflake01    | v2alpha     | depot |           | active  |           | dataos-resource-manager         
  thirdparty01   | v2alpha     | depot |           | active  | running:1 | user02

```


If a suitable Depot already exists, proceed to the next step of creating a Flare Job. Metis may be used to explore datasets across various Depots.
If the required Depot is not present in the list, a manifest configuration file can be created for the appropriate source Depot and applied using the CLI.
Following template display the manifest configuration for a Snowflake Depot: 

```yaml
name: ${{snowflake-depot}}
version: v2alpha
type: depot
tags:
    - ${{tag1}}
    - ${{tag2}}
layer: user
depot:
    type: snowflake
    description: ${{snowflake-depot-description}}
    snowflake:
    warehouse: ${{warehouse-name}}
    url: ${{snowflake-url}}
    database: ${{database-name}}
    external: true
    secrets:
    - name: ${{redshift-instance-secret-name}}-r
        allkeys: true

    - name: ${{redshift-instance-secret-name}}-rw
        allkeys: true

```

For detailed instructions on creating a Depot on different sources, refer to the [Create Depot](/resources/depot/) documentation.


## Crating the Flare Job


To define a workflow for executing a Flare job, configuration parameters must be specified as key-value pairs within a manifest configuration file. Prior to constructing the manifest file, the Uniform Data Locator (UDL) values for both the input and output Depots must be identified.

For this scenario:

* **Input**

  * `dataset`: `dataos://thirdparty01:none/city`
  * `format`: `CSV`

* **Output**

  * `dataset`: `dataos://lakehouse01:retailsample`

This configuration requires integration with two Depots—`thirdparty01` and `lakehouse01`—to enable data ingestion from the source and data persistence to the sink. These Depots serve as endpoints for reading and writing operations, respectively.


```yaml
name: ${{cnt-city-demo-001}}                                        # Name of the Workflow
version: v1                                                         # Version of the Workflow
type: workflow                                                      # Type of Workflow
tags:                                                               # Tags for classification
- ${{tag}}                                         
- ${{tag}}                                         
description: The job ingests city data from dropzone into raw zone  # Description of the workflow

workflow:                                                           # Workflow block
  title: Connect City                                               # Title of the workflow
  dag:                                                              # DAG (Directed Acyclic Graph)
  - name: ${{wf-sample-job-001}}                                    # Job identifier
    title: ${{City Dimension Ingester}}                             # Job title
    description: The job ingests city data from dropzone into raw zone                    # Job description
    spec:                                                           # Job specifications
      tags:                                                         # Additional classification tags
      - Connect
      - City
      stack: flare:7.0                                              # Runtime stack to use 
      compute: runnable-default                                     # Compute resource profile
      stackSpec:                                                    # Stack-specific configuration
        job:
          explain: true                                             # Enable explain plan for transformations
          logLevel: INFO                                            # Log level

          inputs:                                                   # Input dataset specifications
           - name: city_connect                                     # Input alias
             dataset: dataos://thirdparty01:none/city               # Source dataset path
             format: csv                                            # Input file format
             schemaPath: dataos://thirdparty01:none/schemas/avsc/city.avsc             # Avro schema location

          outputs:                                                  # Output dataset specifications
            - name: cities                                          # Output alias
              dataset: dataos://lakehouse01:retailsample/city?acl=rw    # Output dataset path
              format: Iceberg                                       # Output format
              description: City data ingested from external csv     # Output description
              options:                                              # Write options
                saveMode: append                                    # Save mode for writing (append)
                sort:                                               # Sorting configuration for partitions
                  mode: partition
                  columns:
                    - name: version                                 # Partition column
                      order: desc                                   # Sorting order
                iceberg:                                            # Iceberg-specific settings
                  properties:                                       # Additional Iceberg properties
                    write.format.default: parquet                   # Default file format
                    write.metadata.compression-codec: gzip          # Metadata compression
                  partitionSpec:                                    # Iceberg partitioning
                    - type: identity
                      column: version                               # Partition by version column

          steps:                                                    # Steps for data transformation
          - sequence:                                               # Step sequence
              - name: cities                                        # Step name
                doc: Pick all columns from cities and add version as yyyyMMddHHmm formatted timestamp.      # Step description
                sql: |                                                                                      # SQL transformation logic
                    SELECT
                      *,
                      date_format (now(), 'yyyyMMddHHmm') AS version,  
                      now() AS ts_city             
                    FROM
                      city_connect                 

```

Save the manifest file and copy its path. Path could be either relative or absolute.

> To know more about the various Flare Stack manifest file configurations, click [here](/resources/stacks/flare/configurations/).


### **Applying the Flare Workflow**

Apply the Workflow manifest by executing the below command:

```bash
dataos-ctl resource apply -f <file-path>

# Example 

dataos-ctl resource apply -f /home/Desktop/city_flare.yaml

# Expected Output

INFO[0000] 🛠 apply...                                   
INFO[0000] 🔧 applying(public) cnt-city-demo-001:v1beta1:workflow... 
INFO[0002] 🔧 applying(public) cnt-city-demo-001:v1beta1:workflow...created 
INFO[0002] 🛠 apply...complete
```


If a workspace is not explicitly defined, the resource is applied to the `public` workspace by default.

!!! info "Best Practice"

      It is recommended that workflows be created within a specific workspace aligned to the client's context, such as by environment (e.g., `dev`) or domain (e.g., `marketing`).

To apply a resource within a specific workspace, use the following syntax:

```bash
dataos-ctl resource apply -f <file-path> -w <workspace-name>
```

If the specified workspace does not exist, create it using the following command:

```bash
dataos-ctl workspace create -n <workspace-name>
```




### **Workflow Runtime Information**

To obtain runtime status for a specific workflow, execute the following command:

```bash
dataos-ctl get runtime -w <workspace-name> -t workflow -n <workflow-name>

# Example:

dataos-ctl get runtime -w public -t workflow -n cnt-city-demo-001
```

**Alternative Method:**

Workflow runtime details can also be retrieved by passing workflow metadata as a string. Extract the segment from the `NAME` to `WORKSPACE` column in the `get` command output and use the `-i` flag.

```bash
dataos-ctl -i " cnt-city-demo-001 | v1      | workflow | public" get runtime

# Expected Output

INFO[0000] 🔍 workflow...                                
INFO[0001] 🔍 workflow...complete                        

        NAME        | VERSION |   TYPE   | WORKSPACE |    TITLE     |   OWNER     
--------------------|---------|----------|-----------|--------------|-------------
  cnt-city-demo-001 | v1      | workflow | public    | Connect City |   tmdc  

  JOB NAME |   STACK    |        JOB TITLE        | JOB DEPENDENCIES  
-----------|------------|-------------------------|-------------------
  city-001 | flare:6.0  | City Dimension Ingester |                   
  system   | dataos_cli | System Runnable Steps   |                   

  RUNTIME | PROGRESS |          STARTED          |         FINISHED           
----------|----------|---------------------------|----------------------------
  failed  | 6/6      | 2022-06-24T17:11:55+05:30 | 2022-06-24T17:13:23+05:30  

                NODE NAME              | JOB NAME |             POD NAME              |     TYPE     |       CONTAINERS        |   PHASE    
--------------------------------------|----------|-----------------------------------|--------------|-------------------------|------------
  city-001-bubble-failure-rnnbl       | city-001 | cnt-city-demo-001-c5dq-2803083439 | pod-workflow | wait,main               | failed     
  city-001-c5dq-0624114155-driver     | city-001 | city-001-c5dq-0624114155-driver   | pod-flare    | spark-kubernetes-driver | failed     
  city-001-execute                    | city-001 | cnt-city-demo-001-c5dq-3254930726 | pod-workflow | main                    | failed     
  city-001-failure-rnnbl              | city-001 | cnt-city-demo-001-c5dq-3875756933 | pod-workflow | wait,main               | succeeded  
  city-001-start-rnnbl                | city-001 | cnt-city-demo-001-c5dq-843482008  | pod-workflow | wait,main               | succeeded  
  cnt-city-demo-001-run-failure-rnnbl | system   | cnt-city-demo-001-c5dq-620000540  | pod-workflow | wait,main               | succeeded  
  cnt-city-demo-001-start-rnnbl       | system   | cnt-city-demo-001-c5dq-169925113  | pod-workflow | wait,main               | succeeded
```

To view live updates of workflow progress, append the `-r` flag:

```bash
dataos-ctl -i " cnt-city-demo-001 | v1      | workflow | public" get runtime -r
```

Press `Ctrl + C` to exit the runtime stream.



## Additional Link

- [Flare Stack Manifest Configurations](/resources/stacks/flare/configurations/) – Configuration settings for reading, writing, and transforming data.

- [Flare Functions List](/resources/stacks/flare/functions/list/) – List of supported functions for Flare-based data processing.

- [Flare Optimizations](/resources/stacks/flare/optimizations/) – Techniques for tuning and optimizing Flare stack jobs.

- [Case Scenario](/resources/stacks/flare/case_scenario/) – Examples of real-world data processing using the Flare stack.




<!-- 
### **Troubleshoot Errors**

#### **Check Logs for Errors**

Run the same workflow again with the same specifications

Check the logs using the following command. You can run the runtime command to get the names of nodes that failed

```bash
dataos-ctl -i "<copy the name-to-workspace in the output table from get status command" --node <failed-node-name-from-get-runtime-command> log
```

**Example**

```bash
dataos-ctl -i " cnt-city-demo-001 | v1 | workflow | public" --node city-001-c5dq-0624114155-driver log
```
<details>
<summary>Output</summary>
    
```bash
INFO[0000] 📃 log(public)...                             
INFO[0001] 📃 log(public)...complete                     

              NODE NAME            |     CONTAINER NAME      | ERROR  
----------------------------------|-------------------------|--------
  city-001-c5dq-0624114155-driver | spark-kubernetes-driver |        

-------------------LOGS-------------------
++ id -u
+ myuid=0
++ id -g
+ mygid=0
+ set +e
++ getent passwd 0
+ uidentry=root:x:0:0:root:/root:/bin/bash
+ set -e
+ '[' -z root:x:0:0:root:/root:/bin/bash ']'
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
+ '[' -z x ']'
+ SPARK_CLASSPATH='/opt/spark/conf::/opt/spark/jars/*'
+ case "$1" in
+ shift 1
+ CMD=("$SPARK_HOME/bin/spark-submit" --conf "spark.driver.bindAddress=$SPARK_DRIVER_BIND_ADDRESS" --deploy-mode client "$@")
+ exec /usr/bin/tini -s -- /opt/spark/bin/spark-submit --conf spark.driver.bindAddress=10.212.6.129 --deploy-mode client --properties-file /opt/spark/conf/spark.properties --class io.dataos.flare.Flare local:///opt/spark/jars/flare.jar -c /etc/dataos/config/jobconfig.yaml
2022-06-24 11:42:37,146 WARN  [main] o.a.h.u.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
build version: 5.9.16-dev; workspace name: public; workflow name: cnt-city-demo-001; workflow run id: 761eea3b-693b-4863-a83d-9382aa078ad1; run as user: mebinmoncy; job name: city-001; job run id: 03b60c0e-ea75-4d08-84e1-cd0ff2138a4e; 
found configuration: Map(explain -> true, appName -> city-001, outputs -> List(Map(depot -> dataos://lakehouse01:retailsample?acl=rw, name -> output01)), inputs -> List(Map(dataset -> dataos://thirdparty01:none/city, format -> csv, name -> city_connect, schemaPath -> dataos://thirdparty01:none/schemas/avsc/city.avsc)), steps -> List(/etc/dataos/config/step-0.yaml), logLevel -> INFO)
22/06/24 11:42:41 INFO Flare$: context is io.dataos.flare.contexts.ProcessingContext@49f40c00
22/06/24 11:42:41 ERROR Flare$: =>Flare: Job finished with error build version: 5.9.16-dev; workspace name: public; workflow name: cnt-city-demo-001; workflow run id: 761eea3b-693b-4863-a83d-9382aa078ad1; run as user: mebinmoncy; job name: city-001; job run id: 03b60c0e-ea75-4d08-84e1-cd0ff2138a4e; 
io.dataos.flare.exceptions.FlareInvalidConfigException: Could not alter output datasets for workspace: public, job: city-001. There is an existing job with same workspace: public and name: city-001 writing into below datasets
  1. dataos://aswathama:retail/city
  You should use a different job name for your job as you cannot change output datasets for any job.
        at io.dataos.flare.configurations.mapper.StepConfigMapper$.$anonfun$validateSinkWithPreviousJob$3(StepConfigMapper.scala:180)
        at io.dataos.flare.configurations.mapper.StepConfigMapper$.$anonfun$validateSinkWithPreviousJob$3$adapted(StepConfigMapper.scala:178)
        at scala.collection.immutable.List.foreach(List.scala:431)
        at scala.collection.generic.TraversableForwarder.foreach(TraversableForwarder.scala:38)
        at scala.collection.generic.TraversableForwarder.foreach$(TraversableForwarder.scala:38)
        at scala.collection.mutable.ListBuffer.foreach(ListBuffer.scala:47)
        at io.dataos.flare.configurations.mapper.StepConfigMapper$.validateSinkWithPreviousJob(StepConfigMapper.scala:178)
        at io.dataos.flare.configurations.mapper.StepConfigMapper$.validate(StepConfigMapper.scala:38)
        at io.dataos.flare.contexts.ProcessingContext.setup(ProcessingContext.scala:37)
        at io.dataos.flare.Flare$.main(Flare.scala:61)
        at io.dataos.flare.Flare.main(Flare.scala)
        at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
        at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
        at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
        at java.lang.reflect.Method.invoke(Method.java:498)
        at org.apache.spark.deploy.JavaMainApplication.start(SparkApplication.scala:52)
        at org.apache.spark.deploy.SparkSubmit.org$apache$spark$deploy$SparkSubmit$$runMain(SparkSubmit.scala:958)
        at org.apache.spark.deploy.SparkSubmit.doRunMain$1(SparkSubmit.scala:183)
        at org.apache.spark.deploy.SparkSubmit.submit(SparkSubmit.scala:206)
        at org.apache.spark.deploy.SparkSubmit.doSubmit(SparkSubmit.scala:90)
        at org.apache.spark.deploy.SparkSubmit$$anon$2.doSubmit(SparkSubmit.scala:1046)
        at org.apache.spark.deploy.SparkSubmit$.main(SparkSubmit.scala:1055)
        at org.apache.spark.deploy.SparkSubmit.main(SparkSubmit.scala)

Exception in thread "main" io.dataos.flare.exceptions.FlareInvalidConfigException: Could not alter output datasets for workspace: public, job: city-001. There is an existing job with same workspace: public and name: city-001 writing into below datasets
  1. dataos://aswathama:retail/city
  You should use a different job name for your job as you cannot change output datasets for any job.
    
22/06/24 11:42:42 INFO Flare$: Gracefully stopping Spark Application
22/06/24 11:42:42 **ERROR** ProcessingContext: =>Flare: Job finished with error=Could not alter output datasets for workspace: public, job: city-001. **There is an existing job with same workspace**: public and name: city-001 writing into below datasets
  1. dataos://aswathama:retail/city
  **You should use a different job name for your job as you cannot change output datasets for any job.**
Exception in thread "shutdownHook1" io.dataos.flare.exceptions.FlareException: Could not alter output datasets for workspace: public, job: city-001. There is an existing job with same workspace: public and name: city-001 writing into below datasets
  1. dataos://aswathama:retail/city
  You should use a different job name for your job as you cannot change output datasets for any job.
        at io.dataos.flare.contexts.ProcessingContext.error(ProcessingContext.scala:87)
        at io.dataos.flare.Flare$.$anonfun$addShutdownHook$1(Flare.scala:84)
        at scala.sys.ShutdownHookThread$$anon$1.run(ShutdownHookThread.scala:37)
2022-06-24 11:42:42,456 INFO  [shutdown-hook-0] o.a.s.u.ShutdownHookManager: Shutdown hook called
2022-06-24 11:42:42,457 INFO  [shutdown-hook-0] o.a.s.u.ShutdownHookManager: Deleting directory /tmp/spark-bb4892c9-0236-4569-97c7-0b610e82ff52
```
</details>

You will notice the error “*There is an existing job with the same workspace. You should use a different job name for your job as you cannot change output datasets for any job.”*

#### **Fix the Errors**

Modify the YAML by changing the name of the workflow. For this example, it is renamed as `cnt-city-demo-999` from `cnt-city-demo-001`

#### **Delete the Workflows**

Now before you rerun the workflow, you need to `delete` the previous version of this workflow from the environment. You can delete the workflow in two ways as shown below. 

**Method 1:** **Select the name to workspace from get command output and copy it as a string as shown below** 

Command

```bash
dataos-ctl -i "<name-to-workspace in the output table from get status command>" delete
```

Example

```bash
dataos-ctl -i " cnt-city-demo-001 | v1 | workflow | public" delete
# this is the output
INFO[0000] 🗑 delete...                                  
INFO[0001] 🗑 deleting(public) cnt-city-demo-001:v1beta1:workflow... 
INFO[0003] 🗑 deleting(public) cnt-city-demo-001:v1beta1:workflow...deleted 
INFO[0003] 🗑 delete...complete
```

**Method 2: Select the path of the YAML file and use the `delete` Command**

Command

```bash
dataos-ctl delete -f <file-path>
```

Example

```bash
dataos-ctl delete -f /home/desktop/flare/connect-city/config_v2beta1.yaml 
# this is the output
INFO[0000] 🗑 delete...                                  
INFO[0000] 🗑 deleting(public) cnt-city-demo-010:v1beta1:workflow... 
INFO[0001] 🗑 deleting(public) cnt-city-demo-010:v1beta1:workflow...deleted 
INFO[0001] 🗑 delete...complete
```

**Method 3:**

Command

```bash
dataos-ctl -w <workspace> -t workflow -n <workflow-name> delete
```

Example

```bash
dataos-ctl -w public -t workflow -n cnt-city-demo-001 delete
# this is the output
INFO[0000] 🗑 delete...                                  
INFO[0000] 🗑 deleting(public) cnt-city-demo-010:v1beta1:workflow... 
INFO[0001] 🗑 deleting(public) cnt-city-demo-010:v1beta1:workflow...deleted 
INFO[0001] 🗑 delete...complete
```

#### **Rerun the Workflow**

Run the workflow again using `apply` command. Check the Runtime for its success. Scroll to the right to see the status as shown in the previous steps.

**Command**

```bash
dataos-ctl -i "copy the name-to-workspace in the output table from get status command" get runtime -r
```

**Example**

```bash
dataos-ctl -i " cnt-city-demo-999 | v1 | workflow | public" get runtime -r
```
<details>
<summary>
Output</summary>
    
```bash
INFO[0000] 🔍 workflow...                                
INFO[0002] 🔍 workflow...complete                        

        NAME        | VERSION |   TYPE   | WORKSPACE |    TITLE     |   OWNER     
--------------------|---------|----------|-----------|--------------|-------------
  cnt-city-demo-999 | v1beta1 | workflow | public    | Connect City | mebinmoncy  

  JOB NAME |   STACK    |        JOB TITLE        | JOB DEPENDENCIES  
-----------|------------|-------------------------|-------------------
  city-999 | flare:6.0  | City Dimension Ingester |                   
  system   | dataos_cli | System Runnable Steps   |                   

    RUNTIME  | PROGRESS |          STARTED          |         FINISHED           
------------|----------|---------------------------|----------------------------
  succeeded | 5/5      | 2022-06-24T17:29:37+05:30 | 2022-06-24T17:31:50+05:30  

                NODE NAME              | JOB NAME |             POD NAME              |     TYPE     |       CONTAINERS        |   PHASE    
--------------------------------------|----------|-----------------------------------|--------------|-------------------------|------------
  city-999-execute                    | city-999 | cnt-city-demo-999-lork-1125088085 | pod-workflow | main                    | succeeded  
  city-999-lork-0624115937-driver     | city-999 | city-999-lork-0624115937-driver   | pod-flare    | spark-kubernetes-driver | completed  
  city-999-start-rnnbl                | city-999 | cnt-city-demo-999-lork-1790287599 | pod-workflow | wait,main               | succeeded  
  city-999-success-rnnbl              | city-999 | cnt-city-demo-999-lork-2939697963 | pod-workflow | wait,main               | succeeded  
  cnt-city-demo-999-run-success-rnnbl | system   | cnt-city-demo-999-lork-2544494600 | pod-workflow | wait,main               | succeeded  
  cnt-city-demo-999-start-rnnbl       | system   | cnt-city-demo-999-lork-2374735668 | pod-workflow | wait,main               | succeeded

```
</details>
    

#### **Check Registered Dataset with Metis**

Check the registered dataset on the Metis UI.

> You have just run your first Flare Workflow and successfully ingested a dataset within the Icebase. We have also checked it on the Datanet. Once we are done with the ingestion and transformation, we can start querying the data using the Workbench and build analytics Dashboard.

But wait! The work doesn’t end here

**Delete the Workflow**

It’s always good to clean your desk, after getting the work done. You should delete the workflow from the environment after your job is successfully run. The workflow, otherwise, will keep floating in the environment for three days.

First, list the workflows.

```bash
dataos-ctl -t workflow -w public get
```

Output

```bash
INFO[0000] 🔍 get...                                     
INFO[0001] 🔍 get...complete                             

          NAME          | VERSION |   TYPE   | WORKSPACE | STATUS |  RUNTIME  |  OWNER     
------------------------|---------|----------|-----------|--------|-----------|-----------
  cnt-city-demo-999     | v1      | workflow | public    | active | succeeded |  tmdc  
```

And then delete using the below command

```bash
dataos-ctl -i "cnt-city-demo-999     | v1 | workflow | public " delete
```

Output

```bash
INFO[0000] 🗑 delete...                                  
INFO[0001] 🗑 deleting(public) cnt-city-demo-999:v1beta1:workflow... 
INFO[0003] 🗑 deleting(public) cnt-city-demo-999:v1beta1:workflow...deleted 
INFO[0003] 🗑 delete...complete
``` -->