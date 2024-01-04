#  Get Command Group
You run the following `get` commands by appending them to *dataos-ctl get*.

## `runtime`

Get the runtime details of a resource in the DataOS.

```bash
Usage:
dataos-ctl get runtime [flags]

Flags:
  -d, --details               Print lots of details
  -h, --help                  help for runtime
      --id string             Resource ID, like: TYPE:VERSION:NAME:WORKSPACE(optional), depot:v1:icebase or service:v1:ping:sandbox
  -i, --identifier string     Identifier of resource, like: NAME:VERSION:TYPE:WORKSPACE
  -f, --manifestFile string   Manifest file location
  -n, --name string           Name to query
      --node string           Node name to get details
  -r, --refresh               Auto refresh the results
      --refreshRate int       Refresh rate in seconds (default 5)
  -t, --type string           The resource type to get. Workspace resources: workflow, service, worker, cluster. Instance resources: depot.
  -v, --version string        Version to query (default "v1")
  -w, --workspace string      Workspace to query
  -y, --yaml                  Print the full node as yaml
```

**Examples:**

```bash
dataos-ctl get runtime -t depot -n icebase
dataos-ctl get runtime -w system -t cluster -n minervaa
dataos-ctl get runtime -w system -t service -n iosa-receiver
dataos-ctl get runtime -w public -t workflow -n cnt-city-demo-01
dataos-ctl -i "quality-checks-test-cases | v1beta1 | workflow | public"  get runtime
```

You can also provide a string to get the runtime information.

```bash
dataos-ctl -i "quality-checks-test-cases | v1beta1 | workflow | public"  get runtime
```

**Output:**

```bash
INFO[0000] 🔍 workflow...                                
INFO[0002] 🔍 workflow...complete                        

            NAME            | VERSION |   TYPE   | WORKSPACE |     TITLE      |        OWNER         
----------------------------|---------|----------|-----------|----------------|----------------------
  quality-checks-test-cases | v1beta1 | workflow | public    | Quality-Checks | rakeshvishvakarma21  

           JOB NAME          |   STACK    |        JOB TITLE        |    JOB DEPENDENCIES     
-----------------------------|------------|-------------------------|-------------------------
  dataos-tool-quality-checks | toolbox    |                         | quality-checks-summary  
  quality-checks-summary     | flare:1.0  | quality-checks datasets |                         
  system                     | dataos_cli | System Runnable Steps   |                         

  SCHEDULED RUNTIME |    LAST SCHEDULED TIME     
--------------------|----------------------------
  RUNNING           | 2021-11-01T14:30:00+05:30  

  RUNTIME | PROGRESS |          STARTED          | FINISHED  
----------|----------|---------------------------|-----------
  running | 2/3      | 2021-11-01T14:30:00+05:30 |           

                NODE NAME               |        JOB NAME        |                       POD NAME                       |     TYPE     |       CONTAINERS        |   PHASE    
----------------------------------------|------------------------|------------------------------------------------------|--------------|-------------------------|------------
  quality-checks-summary-bviw-driver    | quality-checks-summary | quality-checks-summary-bviw-driver                   | pod-flare    | spark-kubernetes-driver | running    
  quality-checks-summary-execute        | quality-checks-summary | quality-checks-test-cases-bviw-1635757200-996077945  | pod-workflow | main                    | running    
  quality-checks-summary-start-rnnbl    | quality-checks-summary | -checks-test-cases-bviw-1635757200-3571325227 |
```

These commands get the runtime info and display the "node"s that are involved, then you can get the details of a specific node which then gives you the pod details of that node:

**Example:**

```bash
dataos-ctl -i "quality-checks-test-cases | v1beta1 | workflow | public" --node quality
-checks-summary-bviw-driver  get runtime
```

**Output:**

```bash
INFO[0000] 🔍 node...                                    
INFO[0003] 🔍 node...complete                            

              NODE NAME              |              POD NAME              |    IMAGE PULL SECRETS     |   PHASE    
-------------------------------------|------------------------------------|---------------------------|------------
  quality-checks-summary-bviw-driver | quality-checks-summary-bviw-driver | dataos-container-registry | Succeeded  

      CONTAINER NAME      |         CONTAINER IMAGE          | CONTAINER IMAGE PULL POLICY  
--------------------------|----------------------------------|------------------------------
  spark-kubernetes-driver | docker.io/rubiklabs/flare:5.5.48 | IfNotPresent                 

  POD CONDITION TYPE | POD CONDITION STATUS | MESSAGE |           TIME             
---------------------|----------------------|---------|----------------------------
  Initialized        | True                 |         | 2021-11-01T15:45:26+05:30  
  PodScheduled       | True                 |         | 2021-11-01T15:45:26+05:30  
  Ready              | False                |         | 2021-11-01T15:47:25+05:30  
  ContainersReady    | False                |         | 2021-11-01T15:47:25+05:30  

      CONTAINER NAME      |        CONTAINER STATE         |          STARTED          |         FINISHED           
--------------------------|--------------------------------|---------------------------|----------------------------
  spark-kubernetes-driver | Terminated Reason:Completed    | 2021-11-01T15:45:28+05:30 | 2021-11-01T15:47:25+05:30  
                          | Message: ExitCode: 0           |                           |                            

  EVENT TYPE | EVENT REASON |   EVENT SOURCE    |                    EVENT MESSAGE                    |       LAST OCCURRED       | COUNT  
-------------|--------------|-------------------|-----------------------------------------------------|---------------------------|--------
  Warning    | FailedMount  | kubelet           | MountVolume.SetUp failed for                        | 2021-11-01T15:00:31+05:30 | 1      
             |              |                   | volume "spark-conf-volume-driver"                   |                           |        
             |              |                   | : configmap                                         |                           |        
             |              |                   | "spark-drv-9f60d37cdad602e6-conf-map"               |                           |        
             |              |                   | not found                                           |                           |
```
