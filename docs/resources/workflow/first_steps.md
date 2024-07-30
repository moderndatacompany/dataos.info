# Workflow: First Steps

## Create a Workflow

A Workflow Resource instance can be deployed by applying the manifest file. But before creating a Workflow Resource, ensure you have required use-cases assigned.

### **Get Appropriate Access Permission Use Case**

In DataOS, different actions require specific use cases that grant the necessary permissions to execute a task. You can grant these use cases directly to a user or group them under a tag, which is then assigned to the user. The following table outlines various actions related to Workflow Resources and the corresponding use cases required:


| **Action** | **Required Use Cases** |
|------------|------------------------|
| Get        | Read Workspaces, Read Resources in User Specified Workspace / Read Resources in User Workspaces (for curriculum and sandbox workspaces) |
| Create     | Create and Update Resources in User Workspace       |
| Apply      | Create and Update Resources in User Workspace          |
| Delete     | Delete Resources in User Workspace               |
| Log        | Read Resource Logs in User Workspace                 |
            
To assign use cases, you can either contact the DataOS Operator or create a Grant Request by creating a Grant Resource. The request will be validated by the DataOS Operator.

### **Create a manifest file**

To create a Workflow Resource, data developers can define a set of attributes in a manifest file, typically in YAML format, and deploy it using the DataOS Command Line Interface (CLI) or API. Below is a sample manifest file for a Workflow Resource:

???tip "Sample Workflow manifest"

    ```yaml title="sample_worker.yml"
    --8<-- "examples/resources/workflow/workflow.yml"
    ```

The manifest file for a Workflow Resource consists of three main sections, each requiring specific configuration:

- [Resource Meta Section](#resource-meta-section): Contains attributes shared among all types of Resources.
- [Workflow-Specific Section](#workflow-specific-section): Includes attributes unique to the Workflow Resource.
- [Job-specific Section](#job-specific section): Includes attributes unique to the Job.
- [Stack-Specific Section](#stack-specific-section): Encompasses attributes specific to the Stack orchestrated by the Workflow, which can vary depending on the Stack.

#### **Resource meta section**

In DataOS, a Workflow is categorized as a Resource type. The YAML configuration file for a Workflow Resource includes a Resource meta section, which contains attributes shared among all Resource types.

The following YAML excerpt illustrates the attributes specified within this section:

=== "Syntax"

      ```yaml
      name: ${{resource_name}} # Name of the Resource (mandatory)
      version: v1beta # Manifest version of the Resource (mandatory)
      type: workflow # Type of Resource (mandatory)
      tags: # Tags for categorizing the Resource (optional)
        - ${{tag_example_1}} 
        - ${{tag_example_2}} 
      description: ${{resource_description}} # Description (optional)
      owner: ${{resource_owner}} # Owner of the Resource (optional, default value: user-id of user deploying the resource)
      layer: ${{resource_layer}} # DataOS Layer (optional, default value: user)
      workflow: # Workflow-specific Section
        ${{Attributes of Workflow-specific Section}}
      ```
=== "Example"

      ```yaml
      name: my-first-workflow # Name of the Resource
      version: v1beta # Manifest version of the Resource
      type: workflow # Type of Resource
      tags: # Tags for categorizing the Resource
        - dataos:workflow 
        - workflow 
      description: Common attributes applicable to all DataOS Resources # Description
      owner: iamgroot # Owner of the Resource
      layer: user # DataOS Layer
      workflow: 
      ```

To configure a Workflow Resource, replace the values of `name`, `layer`, `tags`, `description`, and `owner` with appropriate values. For additional configuration information about the attributes of the Resource meta section, refer to the link: [Attributes of Resource meta section](/resources/manifest_attributes/).

#### **Workflow-specific section**

The Workflow-specific sectionThe Workflow-specific section contains configurations specific to the Workflow Resource. DataOS supports two types of Workflows: [single-run](/resources/workflow/how_to_guide/single_run_workflow/) and [scheduled](/resources/workflow/how_to_guide/scheduled_workflow/) Workflow, each with its own YAML syntax. of a manifest file encompasses attributes specific to the Workflow Resource.

**Single-Run Workflow YAML configuration**

A [Single-run Workflow](#single-run-workflow) executes only once. It does not include a schedule section. The YAML configuration for a single-run Workflow is as follows:

```yaml
workflow:
  dag:
    ${{list-of-jobs}}
```
<center><i>Workflow-specific Section configuration for Single-run Workflow</i></center>

**Scheduled Workflow YAML configuration**

A [Scheduled Workflow](#scheduled-workflow) triggers a series of jobs or tasks at particular intervals or predetermined times. To create a scheduled Workflow, specify the [attributes](/resources/workflow/configuration/#schedule) in the `schedule` section, in the following format:
```yaml
workflow:
  schedule:
    cron: ${{'/10 * * * *'}}
  dag:
    ${{list-of-jobs}}
```
<center><i>Workflow-specific section configuration for Scheduled Workflow</i></center>

#### **Configure the Job-specific Section**

A [Directed Acyclic Graph (DAG)](#workflow-and-directed-acyclic-graph-dag) represents the sequence and dependencies between various jobs within the Workflow. A DAG must contain at least one job.

**Job**

A Job denotes a single processing task. Multiple jobs within a DAG can be linked sequentially or concurrently to achieve a specific result through [`dependencies`](/resources/workflow/configurations/#dependency). Here is an example YAML syntax for two jobs linked by dependencies:
```yaml
dag: 
  - name: ${{job1 name}}
    spec: 
      stack: ${{stack1:version}}
      compute: ${{compute name}}
      resources:
        requests:
          cpu: ${{requested cpu}}
          memory: ${{requested memory}}
        limits:
          cpu: ${{cpu limits}}
          memory: ${{memory limits}}
      stack1: 
        ${{stack1 specific attributes}}
  - name: ${{job2-name}}
    spec: 
      stack: ${{stack2:version}}
      compute: ${{compute name}}
      stack2: 
        ${{stack2 specific configuration}}
    dependencies: 
      - ${{job1-name}}
```
<center><i>Job-specific section YAML configuration</i></center>

Further, jobs can be retried automatically by pre-defining the retry strategy within the Workflow YAML. This could be helpful in case of job failures or unexpected errors. Learn about job retries by navigating to the following link: [How to retry failed jobs within a Workflow?](/resources/workflow/how_to_guide/retry_jobs/)

<aside class=callout>

🗣️ Please be aware that the code block above outlines only the general configuration for a job. The actual attributes may differ based on the specific <a href="/resources/stacks/">Stack</a> utilized within a job.

</aside>

#### **Configure the Stack-specific Section**

The Stack-specific Section allows you to specify the desired [Stack](/resources/stacks) for executing your Workflow. Depending on your requirements, you can choose from the following supported Stacks:

- [Flare Stack](/resources/stacks/flare/): The Flare stack provides advanced capabilities for data processing and analysis.

- [Container Stack](/resources/stacks/container/): The Container stack offers a powerful environment for hosting web-application, and custom Docker images atop DataOS.

- [Data Toolbox Stack](/resources/stacks/data_toolbox/): The Data Toolbox stack provides a set of utilities for Depots storing Iceberg datasets, for e.g. Icebase.

- [Scanner Stack](/resources/stacks/scanner/): The Scanner Stack provides metadata ingestion capabilities from a source.

For more detailed instructions on setting up and customizing the Stack-specific Section attributes according to your needs, refer to the respective documentation of [Flare](/resources/stacks/flare/configurations/), [Container](/resources/stacks/container/#container-stack-section), [Data Toolbox](/resources/stacks/data_toolbox/data_toolbox_grammar/), [Scanner](/resources/stacks/scanner/field_ref/) Stack. Each Stack has its unique attributes that can enhance the functionality of your job.


<details>
<summary>
Click here to view a sample Workflow YAML configuration
</summary>

The sample Workflow code snippet provide below consists of a single job that leverages the <a href="/resources/stacks/flare/">Flare</a> Stack for transforming data read from the <a href="/resources/depot/icebase/">Icebase</a> Depot and storing it in the <code>thirdparty01</code> Depot.
<br>
<br>
<b>Code Snippet</b>

```yaml
# Resource Section
name: abfss-write-avro
version: v1
type: workflow
tags:
  - Connect
  - City
description: This workflow reads data from Icebase depot and stores it in thirdparty depot.

# Workflow-specific Section
workflow:
  title: Connect City avro
  dag:

# Job-specific Section
    - name: city-abfss-write-avro
      title: City Dimension Ingester
      description: The job ingests data from Icebase to thirdparty depot.
      spec:
        tags:
          - Connect
          - City
        stack: flare:5.0
        compute: runnable-default

# Stack-specific Section
        stackSpec:
          job:
            explain: true
            inputs:
              - name: city_connect
                dataset: dataos://icebase:retail/city
                format: iceberg
            logLevel: INFO
            outputs:
              - name: output01 # output name (same as name of the step to be materialized)
                dataset: dataos://thirdparty01:sampledata?acl=rw 
                format: avro 
            steps:
              - sequence:
                  - name: output01 # step name
                    sql: SELECT * FROM city_connect
```

</details>

## Apply the Workflow YAML

Once you have constructed the Workflow YAML file, it's time to [apply](/resources/#apply) it and create the Workflow [Resource](/resources/) within the DataOS environment. Use the following [`apply`](/interfaces/cli/command_reference/#apply) 

=== "Command"

    ```shell
    dataos-ctl apply -f ${{yaml file path}} -w ${{workspace}}
    ```
===  "Example"

    ```shell
    dataos-ctl apply -f home/iamgroot/resource/workflow.yml -w curriculum
    ```

Workspace specification is optional. In case its not provided the Workflow runs in the `curriculum` Workspace. To create a new Workspace, execute the [`workspace create`](/interfaces/cli/command_reference/#workspace) command as shown below and then execute the above command:

=== "Command"

    ```shell
    dataos-ctl workspace create -n ${{name of your workspace}}
    ```

===  "Example"

    ```shell
    dataos-ctl workspace create -n new_workspace
    ```

## How to Monitor a Workflow?

### **Get Status of the Workflow**

To retrieve information about the Workflow, use the [`get`](/interfaces/cli/command_reference/#get) command in the [CLI](/interfaces/cli). The command below lists workflows created by the user in a specific Workspace. 

=== "Command"

    ```shell
    dataos-ctl get -t ${workflow} -w ${curriculum}
    ```
=== "Example"

    ```shell
    dataos-ctl get -t workflow -w curriculum
    #expected_output
    INFO[0000] 🔍 get...
    INFO[0001] 🔍 get...complete

              NAME        | VERSION |   TYPE   | WORKSPACE | STATUS | RUNTIME |   OWNER
    ----------------------|---------|----------|-----------|--------|---------|-------------
      cnt-product-demo-01 | v1      | workflow | curriculum    | active | running |   tmdc
    ```


To check this information for all users in a specific Workspace, add the `-a` flag to the command as shown below.


```shell
dataos-ctl get -t workflow -w curriculum -a
#expected_output
INFO[0000] 🔍 get...
INFO[0001] 🔍 get...complete

          NAME           | VERSION |   TYPE   | WORKSPACE | STATUS |  RUNTIME  |       OWNER
-------------------------|---------|----------|-----------|--------|-----------|--------------------
  checks-sports-data     | v1      | workflow | curriculum    | active | succeeded | user01
  cnt-product-demo-01    | v1      | workflow | curriculum    | active | running   | tmdc
  cnt-product-demo-01-01 | v1      | workflow | curriculum    | active | succeeded | otheruser
  cnt-city-demo-01001    | v1      | workflow | curriculum    | active | succeeded | user03
```

### **Get Runtime Information**

To obtain the runtime status of the Workflow, use the [`get runtime`](/interfaces/cli/command_reference/#get-runtime) 

=== "Command"

    ```shell
    dataos-ctl get runtime -w ${{workspace-name}} -t workflow -n ${{name of workflow}}
    ```

=== "Example"

    ```shell
    dataos-ctl get runtime -w curriculum -t workflow -n cnt-product-demo-01
    ```

Alternatively, you can extract the Workflow information from the output of the [`get`](/interfaces/cli/command_reference/#get) command and pass it as a string to the [`get runtime`](/interfaces/cli/command_reference/#get-runtime) command. Look for the relevant information (highlighted) in the [`get`](/interfaces/cli/command_reference/#get) command output:

=== "Command"

    ```shell
    dataos-ctl get -t workflow -w ${curriculum}
    ```

=== "Example"

    ```shell
    dataos-ctl get -t workflow -w curriculum
    # the output is shown below
              NAME        | VERSION |   TYPE   | WORKSPACE | STATUS | RUNTIME |   OWNER     
    ----------------------|---------|----------|-----------|--------|---------|-------------
      cnt-product-demo-01 | v1      | workflow | curriculum    | active | running |   tmdc
    ```

Select the workflow details from Name to Workspace tab, for example, `cnt-product-demo-01 | v1 | workflow | curriculum`.


```shell
dataos-ctl get runtime -i "cnt-product-demo-01 | v1 | workflow | curriculum"
```

<details>

<summary>Output</summary>

```shell
INFO[0000] 🔍 workflow...
INFO[0001] 🔍 workflow...complete

        NAME          | VERSION |   TYPE   | WORKSPACE |    TITLE     |   OWNER
----------------------|---------|----------|-----------|--------------|-------------
  cnt-product-demo-01 |   v1    | workflow | curriculum    | Connect City |   tmdc

  JOB NAME |   STACK    |        JOB TITLE        | JOB DEPENDENCIES
-----------|------------|-------------------------|-------------------
  city-001 | flare:5.0  | City Dimension Ingester |                   
  system   | dataos_cli | System Runnable Steps   |                   

  RUNTIME | PROGRESS |          STARTED          |         FINISHED
----------|----------|---------------------------|----------------------------
  failed  |   6/6    | 2022-06-24T17:11:55+05:30 | 2022-06-24T17:13:23+05:30

                NODE NAME               | JOB NAME |             POD NAME                |     TYPE     |       CONTAINERS        |   PHASE
----------------------------------------|----------|-------------------------------------|--------------|-------------------------|------------
  city-001-bubble-failure-rnnbl         | city-001 | cnt-product-demo-01-c5dq-2803083439 | pod-workflow | wait,main               | failed
  city-001-c5dq-0624114155-driver       | city-001 | city-001-c5dq-0624114155-driver     | pod-flare    | spark-kubernetes-driver | failed
  city-001-execute                      | city-001 | cnt-product-demo-01-c5dq-3254930726 | pod-workflow | main                    | failed
  city-001-failure-rnnbl                | city-001 | cnt-product-demo-01-c5dq-3875756933 | pod-workflow | wait,main               | succeeded
  city-001-start-rnnbl                  | city-001 | cnt-product-demo-01-c5dq-843482008  | pod-workflow | wait,main               | succeeded
  cnt-product-demo-01-run-failure-rnnbl | system   | cnt-product-demo-01-c5dq-620000540  | pod-workflow | wait,main               | succeeded
  cnt-product-demo-01-start-rnnbl       | system   | cnt-product-demo-01-c5dq-169925113  | pod-workflow | wait,main               | succeeded
```
</details>

### **Get Runtime Refresh**

To refresh or see updates on the Workflow progress, add the `-r` flag to the [`get runtime`](/interfaces/cli/command_reference#get-runtime) command:

```shell
dataos-ctl -i get runtime " cnt-product-demo-01 | v1 | workflow | curriculum" -r
```

Press `Ctrl + C` to exit.

For any additional flags, use help by appending `-h` with the respective command.

## How to troubleshoot Workflow errors?

### **Check Logs for Errors**

To check the logs for errors, retrieve the node name from the output of the `get runtime` command for the failed node, as shown [here](/interfaces/cli/command_reference/#get-runtime), and execute the command as shown below

=== "Command"

    ```shell
    dataos-ctl -i "${{copy the name to workspace in the output table from get command}}" --node ${{failed node name from get runtime command}} log
    ```

=== "Example"

    ```shell
    dataos-ctl -i " cnt-product-demo-01 | v1 | workflow | curriculum" --node city-001-c5dq-0624114155-driver log
    ```

<details>
<summary>Output</summary>
    
```bash
INFO[0000] 📃 log(curriculum)...                             
INFO[0001] 📃 log(curriculum)...complete                     

              NODE NAME           |     CONTAINER NAME      | ERROR  
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
build version: 5.9.16-dev; workspace name: curriculum; workflow name: cnt-city-demo-001; workflow run id: 761eea3b-693b-4863-a83d-9382aa078ad1; run as user: mebinmoncy; job name: city-001; job run id: 03b60c0e-ea75-4d08-84e1-cd0ff2138a4e; 
found configuration: Map(explain -> true, appName -> city-001, outputs -> List(Map(depot -> dataos://icebase:retailsample?acl=rw, name -> output01)), inputs -> List(Map(dataset -> dataos://thirdparty01:none/city, format -> csv, name -> city_connect, schemaPath -> dataos://thirdparty01:none/schemas/avsc/city.avsc)), steps -> List(/etc/dataos/config/step-0.yaml), logLevel -> INFO)
22/06/24 11:42:41 INFO Flare$: context is io.dataos.flare.contexts.ProcessingContext@49f40c00
22/06/24 11:42:41 ERROR Flare$: =>Flare: Job finished with error build version: 5.9.16-dev; workspace name: curriculum; workflow name: cnt-city-demo-001; workflow run id: 761eea3b-693b-4863-a83d-9382aa078ad1; run as user: mebinmoncy; job name: city-001; job run id: 03b60c0e-ea75-4d08-84e1-cd0ff2138a4e; 
io.dataos.flare.exceptions.FlareInvalidConfigException: Could not alter output datasets for workspace: curriculum, job: city-001. There is an existing job with same workspace: curriculum and name: city-001 writing into below datasets
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

Exception in thread "main" io.dataos.flare.exceptions.FlareInvalidConfigException: Could not alter output datasets for workspace: curriculum, job: city-001. There is an existing job with same workspace: curriculum and name: city-001 writing into below datasets
  1. dataos://aswathama:retail/city
  You should use a different job name for your job as you cannot change output datasets for any job.
    
22/06/24 11:42:42 INFO Flare$: Gracefully stopping Spark Application
22/06/24 11:42:42 **ERROR** ProcessingContext: =>Flare: Job finished with error=Could not alter output datasets for workspace: curriculum, job: city-001. **There is an existing job with same workspace**: curriculum and name: city-001 writing into below datasets
  1. dataos://aswathama:retail/city
  **You should use a different job name for your job as you cannot change output datasets for any job.**
Exception in thread "shutdownHook1" io.dataos.flare.exceptions.FlareException: Could not alter output datasets for workspace: curriculum, job: city-001. There is an existing job with same workspace: curriculum and name: city-001 writing into below datasets
  1. dataos://aswathama:retail/city
  You should use a different job name for your job as you cannot change output datasets for any job.
        at io.dataos.flare.contexts.ProcessingContext.error(ProcessingContext.scala:87)
        at io.dataos.flare.Flare$.$anonfun$addShutdownHook$1(Flare.scala:84)
        at scala.sys.ShutdownHookThread$$anon$1.run(ShutdownHookThread.scala:37)
2022-06-24 11:42:42,456 INFO  [shutdown-hook-0] o.a.s.u.ShutdownHookManager: Shutdown hook called
2022-06-24 11:42:42,457 INFO  [shutdown-hook-0] o.a.s.u.ShutdownHookManager: Deleting directory /tmp/spark-bb4892c9-0236-4569-97c7-0b610e82ff52
```
</details>

You will notice an error message: "*There is an existing job with the same workspace. You should use a different job name for your job as you cannot change output datasets for any job.*"

### **Fix the Errors**

Modify the YAML configuration by changing the name of the Workflow. For example, rename it from `cnt-product-demo-01` to `cnt-city-demo-999`.

### **Delete the Previous Workflow**

Before re-running the Workflow, delete the previous version from the environment. There are three ways to delete the Workflow as shown below.

=== "Method1"

    Copy the name to Workspace from the output table of the [`get`](/interfaces/cli/command_reference#get) command and use it as a string in the delete command.

    === "Command"

        ```shell
        dataos-ctl delete -i "${{name to workspace in the output table from get status command}}"
        ```

    === "Example"

        ```shell
        dataos-ctl delete -i "cnt-product-demo-01 | v1 | workflow | curriculum"
        #Expected_Output
        INFO[0000] 🗑 delete...
        INFO[0001] 🗑 deleting(curriculum) cnt-product-demo-01:v1:workflow...
        INFO[0003] 🗑 deleting(curriculum) cnt-product-demo-01:v1:workflow...deleted
        INFO[0003] 🗑 delete...complete
        ```

=== "Method 2"

    Specify the path of the YAML file and use the [`delete`](/interfaces/cli/command_reference#delete) command.

    ===  "Command"

        ```shell
        dataos-ctl delete -f ${{file-path}}
        ```

    === "Example"

        ```shell
        dataos-ctl delete -f /home/desktop/flare/connect-city/config_v1.yaml
        #expected_output
        INFO[0000] 🗑 delete...
        INFO[0000] 🗑 deleting(curriculum) cnt-city-demo-010:v1:workflow...
        INFO[0001] 🗑 deleting(curriculum) cnt-city-demo-010:v1:workflow...deleted
        INFO[0001] 🗑 delete...complete
        ```

=== "Method 3" 

    Specify the Workspace, Resource-type, and Workflow name in the [`delete`](/interfaces/cli/command_reference#delete) command.

    === "Command"

        ```shell
        dataos-ctl delete -w ${{workspace}} -t workflow -n ${{workflow name}}
        ```

    === "Example"

        ```shell
        dataos-ctl delete -w curriculum -t workflow -n cnt-product-demo-01
        #expected_output
        INFO[0000] 🗑 delete...
        INFO[0000] 🗑 deleting(curriculum) cnt-city-demo-010:v1:workflow...
        INFO[0001] 🗑 deleting(curriculum) cnt-city-demo-010:v1:workflow...deleted
        INFO[0001] 🗑 delete...complete
        ```

### **Rerun the Workflow**

Run the Workflow again using the [`apply`](/interfaces/cli/command_reference#apply) command. 

Command:

```shell
dataos-ctl apply -f ${{file path}} -w ${{workspace}}
```
Once you have applied the Workflow, check the runtime for its success by using the [`get runtime`](/interfaces/cli/command_reference/#get-runtime) command

=== "Command"

    ```shell
    dataos-ctl get runtime -i "${{copy the name to workspace in the output table from get status command}}" -r
    ```

=== "Example"

    ```shell
    dataos-ctl -i "cnt-city-demo-999 | v1 | workflow | curriculum" get runtime -r
    ```

<details>

<summary>Output</summary>

```shell
INFO[0000] 🔍 workflow...
INFO[0002] 🔍 workflow...complete

        NAME        | VERSION |   TYPE   | WORKSPACE |    TITLE     |   OWNER
--------------------|---------|----------|-----------|--------------|-------------
  cnt-city-demo-999 | v1 | workflow | curriculum    | Connect City | mebinmoncy

  JOB NAME |   STACK    |        JOB TITLE        | JOB DEPENDENCIES
-----------|------------|-------------------------|-------------------
  city-999 | flare:2.0  | City Dimension Ingester |                   
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

Make sure to replace `${{name to workspace in the output table from get status command}}` and `${{file path}}` with the actual values according to your Workflow.

</details>

<aside class="best-practice">

📖 <i>Best Practice:</i><br> It is part of the best practice to add relevant <code>description</code>, <code>title</code> and <code>tags</code> for your Workflow. <code>description</code> helps to determine what the Workflow will help you accomplish, <code>title</code> and <code>tags</code> can help in faster searching in <a href="/interfaces/metis/">Metis</a> and <a href="/interfaces/operations/">Operations</a> App.

</aside>

## How to setup alerts on Workflows?

Workflow alerts play a vital role in the effective management of extensive Workflows and Jobs, enabling streamlined monitoring and prompt notifications in the event of failures. For detailed instructions on configuring Workflow alerts, refer to the documentation link: [Setting Up Workflow Alerts.](/dataos_alerts/workflow_alerts/)


<aside class="callout">

DataOS offers a diverse range of integrated alert mechanisms, emphasizing observability and active monitoring.  To learn more about them, refer to <a href="/dataos_alerts/">DataOS Alerts</a> page.

</aside>


## Next Steps

To deepen your understanding of Workflow Resource, explore the following case scenarios that cover different aspects and functionalities:

- [How to implement Single-run Workflow?](/resources/workflow/how_to_guide/single_run_workflow/)

- [How to run a Cron Workflow or a Scheduled Workflow?](/resources/workflow/how_to_guide/scheduled_workflow/)

- [How to orchestrate multiple Workflows from a single Workflow?](/resources/workflow/how_to_guide/multiple_workflows_from_a_single_workflow)/

- [How to retry a job in the Workflow?](/resources/workflow/how_to_guide/retry_jobs/)

- [How to apply a workflow and get a runtime status of it using CLI Stack?](/resources/workflow/how_to_guide/apply_a_workflow_and_get_runtime_status_using_cli_stack/)
