# Routine checks and configuration

In this module, you’ll learn how to manage Kubernetes and Pulsar configurations to keep DataOS running smoothly. These tools are key to ensuring the stability and scalability of the platform. You’ll gain hands-on experience with essential commands, resource adjustments, and monitoring techniques for troubleshooting, optimizing, and maintaining your DataOS infrastructure.

## Scenario 

Imagine you're working on a DataOS platform with varying traffic loads. One day, the system experiences a sudden surge in traffic, and resources need to be scaled quickly to handle the load. Additionally, you're dealing with a persistent issue in the `poros` namespace affecting the platform’s performance. With the help of Kubernetes and Pulsar, you need to troubleshoot the issue, adjust resources, and ensure everything runs smoothly. Follow the commands given in this topic, to manage these tasks and maintain a robust, efficient platform.

## DataOS Operate CLI command

### **`operate`**
Operate the DataOS®

```shell

Usage:
  dataos-ctl operate [command]

Available Commands:
  chart-export   Exports a Helm Chart from a Chart Registry
  exec-stream    Execute-stream a command on a specific target
  get-dataplanes Get the dataplanes
  get-secret     Gets a secret from Heimdall
  log-stream     Stream the logs on a specific target
  pulsar         Pulsar management
  tcp-stream     Tcp-stream a specific address

Flags:
  -h, --help   help for operate

Global Flags:
      --tls-allow-insecure   Allow insecure TLS connections

Use "dataos-ctl operate [command] --help" for more information about a command.
```
<aside class="callout"> 🗣 The<i> <b>operate </b></i>command is intended for use by system administrators. If you would like more information about its various subcommands, please reach out to our Customer Success team.</aside>

## Operate Command Group
You run the following `operate` sub commands by appending them to *dataos-ctl operate*.


Operate the DataOS.

```bash
Usage:
dataos-ctl operate [command]

Available Commands:
apply        Apply manifest
chart-export Exports a Helm Chart from a Chart Registry
git          Git component manifests
install      Install components
ping         Ping
upgrade      Upgrade components
view         View DataOS® Operator Services
zip          Zip install files

Flags:
  -h, --help   help for operate

Use "dataos-ctl operate [command] --help" for more information about a command.
```

### **Operate Apply**

Apply manifest on the DataOS.

```bash
Usage:
dataos-ctl operate apply [flags]

Flags:
-h, --help                  help for apply
-f, --manifestFile string   Single Manifest File Location
-n, --namespace string      Namespace
```

### **Operate Chart-Export**

Exports a Helm Chart from a Chart Registry.

```bash
Usage:
dataos-ctl operate chart-export [flags]

Flags:
    --accessKey string      The AWS Access Key for ECR Chart Registry
    --accessSecret string   The AWS Access Secret for ECR Chart Registry
-c, --chart string          The chart ref
-d, --exportDir string      The directory to export the Helm chart
-h, --help                  help for chart-export
    --region string         The AWS Region for ECR Chart Registry
    --registry string       The AWS ECR Chart Registry
```

### **Operate Get-Secret**

Gets a secret from Heimdall.

```bash
Usage:
dataos-ctl operate get-secret [flags]

Flags:
-h, --help        help for get-secret
-i, --id string   The secret id
```

### **Operate Git**

Git component manifests on the DataOS.

```bash
Usage:
dataos-ctl operate git [flags]

Flags:
-e, --email string   Operator email
-h, --help           help for git
-l, --localOnly      Perform local only
-n, --name string    Operator name
-p, --push           Push changes
-r, --resetGitDir    Reset the local git directory
```

### **Operate Install**

When you create a new server, you want to install new applications on the server. Use this command to install one or more applications/components on the server.

```bash
Usage:
dataos-ctl operate install [flags]

Flags:
-h, --help                    help for install
-i, --imagesFile string       Installation Images File Location
-f, --installFile string      Installation Manifest File Location
-n, --noGitOps                Do not push changes to the GitOps repo in DataOS®
    --oldReleaseManifest      Use old install manifest format
    --renderOnly              Render only
-r, --replaceIfExists         Replace existing resources
-s, --secretsFile string      Installation Secrets File Location
    --useExternalPostgresql   Use external postgresql
-v, --valuesFile string       Installation Values File Location
```

### **Operate Ping**

```bash
Usage:
dataos-ctl operate ping [flags]

Flags:
-h, --help   help for ping
```

### **Operate Upgrade**

Upgrade components on the DataOS.

```bash
Usage:
dataos-ctl operate upgrade [flags]

Flags:
-h, --help                    help for upgrade
-i, --imagesFile string       Installation Images File Location
-f, --installFile string      Installation Manifest File Location
    --oldReleaseManifest      Use old install manifest format
-s, --secretsFile string      Installation Secrets File Location
    --useExternalPostgresql   Use external postgresql
-v, --valuesFile string       Installation Values File Location
```

### **Operate View**

View DataOS Operator Services from the local machine without going to server. You can create a data pipe from server to local machine.

```bash
Usage:
dataos-ctl operate view [flags]

Flags:
-h, --help                            help for view
-p, --localPort int                   The starting local port to port-forward services to (default 8081)
-s, --servicesToPortForward strings   The comma separated list of services to port-forward local: 
                                        metis,cerebro,aurora-beanstalkd,git,prometheus,
                                        service-mesh,cruise-control,kibana,spark-history
```

```bash
➜  ~ dataos-ctl operate view -s metis
INFO[0000] 📚 metis view...                              
INFO[0000] 🔭 metis port-forward..                       
INFO[0003] close connections hit enter/return?
INFO[0004] 🔭 metis port-forward.. ready
INFO[0004] : metis http://localhost:8081
```
## DataOS Fastbase command

### **`fastbase`**

Interact with the FastBase Depot in the DataOS®

```shell

Usage:
  dataos-ctl fastbase [command]

Available Commands:
  namespace   Interact with namespaces in the DataOS® FastBase
  tenant      Interact with tenants in the DataOS® FastBase
  topic       Interact with topics in the DataOS® FastBase

Flags:
  -h, --help   help for fastbase

Global Flags:
      --tls-allow-insecure   Allow insecure TLS connections

Use "dataos-ctl fastbase [command] --help" for more information about a command.
```
## Fastbase Command Group
You run the following `fastbase` sub commands by appending them to *dataos-ctl fastbase*.

### `namespace`
Interact with namespaces in the DataOS® FastBase

```shell

Usage:
  dataos-ctl fastbase namespace [command]

Aliases:
  namespace, namespaces

Available Commands:
  list        List namespaces in the DataOS® FastBase

Flags:
  -h, --help   help for namespace
```
#### **`list`**
List namespaces in the DataOS® FastBase

```shell

Usage:
  dataos-ctl fastbase namespace list [flags]

Flags:
  -h, --help            help for list
  -t, --tenant string   FastBase tenant
```
### `tenant`
Interact with tenants in the DataOS® FastBase

```shell

Usage:
  dataos-ctl fastbase tenant [command]

Aliases:
  tenant, tenants

Available Commands:
  list        List tenants in the DataOS® FastBase

Flags:
  -h, --help   help for tenant
```
#### **`list`**
List tenants in the DataOS® FastBase

```shell

Usage:
  dataos-ctl fastbase tenant list [flags]

Flags:
  -h, --help   help for list
```

### `topic`
Interact with topics in the DataOS® FastBase

```shell

Usage:
  dataos-ctl fastbase topic [command]

Aliases:
  topic, topics

Available Commands:
  consume     Consume Messages from a Topic
  list        List topics in the DataOS® FastBase
  permissions List Permissions of a Topic
  read        Read Message from a Topic

Flags:
  -h, --help   help for topic
```

#### **`consume`**
Consume Messages from a Topic in the DataOS® FastBase
```shell

Usage:
  dataos-ctl fastbase topic consume [flags]

Flags:
  -h, --help                  help for consume
  -l, --logMessage            Log message (default true)
  -p, --logPayload            Log payload with message
  -s, --startAtFirstMessage   Start at the first message in the topic
  -t, --topic string          FastBase topic to consume messages from
```

### **`list`**
List topics in the DataOS® FastBase
```shell

Usage:
  dataos-ctl fastbase topic list [flags]

Flags:
  -h, --help               help for list
  -n, --namespace string   FastBase namespace
```

#### **`permissions`**
List Permissions of a Topic in the DataOS® FastBase
```shell

Usage:
  dataos-ctl fastbase topic permissions [flags]

Flags:
  -h, --help           help for permissions
  -t, --topic string   FastBase topic to read message from
```

#### **`read`**
Read Message from a Topic in the DataOS® FastBase

```shell

Usage:
  dataos-ctl fastbase topic read [flags]

Flags:
  -d, --duration string    FastBase duration to seek in the past
  -h, --help               help for read
  -l, --logMessage         Log message (default true)
  -p, --logPayload         Log payload with message
  -m, --messageId string   FastBase message id to start reading from
  -t, --topic string       FastBase topic to read message from
```

**Example:**
In Fastbase, topics are the endpoints for publishing and consuming messages. They are organized in three level heirarchy. 
**Tenant -> Namespace -> Topic**

- List tenants
```shell
➜  ~ dataos-ctl fastbase tenant list
INFO[0000] 🔍 list...                                    
INFO[0003] 🔍 list...complete                            

  TENANT  
──────────
  public  
  pulsar  
  system  

➜  ~ 

```
- List namespaces - You need to specify tenant for the namespace
```shell
 ~ dataos-ctl fastbase namespace -t public list
INFO[0000] 🔍 list...                                    
INFO[0002] 🔍 list...complete                            

     NAMESPACE      
────────────────────
  public/default    
  public/functions  
```

- List topics
```shell
 ~ dataos-ctl fastbase topic -n public/default list
INFO[0000] 🔍 list...                                    
INFO[0001] 🔍 list...complete                            

                        TOPIC                        │ PARTITIONED  
─────────────────────────────────────────────────────┼──────────────
  persistent://public/default/__change_events        │ N            
  persistent://public/default/databricks_pipeline_01 │ N            
  persistent://public/default/dataos_soda_29         │ N            
  persistent://public/default/monitor-incident-new   │ N            
  persistent://public/default/random_users001        │ N            
  persistent://public/default/random_users_test_01   │ N            
  persistent://public/default/write_pulsar_12        │ N            


```

- Consume Topic

```shell
~ dataos-ctl fastbase topic consume -p -s -t persistent://public/default/random_users_test_01
INFO[0000] 🔍 consume...                                 
WARN[0002] code: 404 reason: Subscription not found     
INFO[0003] Connecting to broker                          remote_addr="pulsar+ssl://tcp.fun-bluegill.dataos.app:6651"
INFO[0003] TCP connection established                    local_addr="192.168.1.164:60450" remote_addr="pulsar+ssl://tcp.fun-bluegill.dataos.app:6651"
INFO[0003] Connection is ready                           local_addr="192.168.1.164:60450" remote_addr="pulsar+ssl://tcp.fun-bluegill.dataos.app:6651"
INFO[0004] Connecting to broker                          remote_addr="pulsar+ssl://tcp.fun-bluegill.dataos.app:6651"
INFO[0004] TCP connection established                    local_addr="192.168.1.164:60451" remote_addr="pulsar+ssl://tcp.fun-bluegill.dataos.app:6651"
INFO[0004] Connection is ready                           local_addr="192.168.1.164:60451" remote_addr="pulsar+ssl://tcp.fun-bluegill.dataos.app:6651"
INFO[0004] Connected consumer                            consumerID=1 name=fyita subscription=fa25137869f8fd0411138ecf63b3c2a9b3e92c2e405efa119c108e4800dc0976 topic="persistent://public/default/random_users_test_01"
INFO[0004] Created consumer                              consumerID=1 name=fyita subscription=fa25137869f8fd0411138ecf63b3c2a9b3e92c2e405efa119c108e4800dc0976 topic="persistent://public/default/random_users_test_01"
{"id":"CJYDEAAYACAA","string_id":"406:0:0","payload":{"age":"","city":"Randers Nø","country":"Denmark","email":"mads.thomsen@example.com","first_name":"Mads","gender":"male","id":"0dc8a0eb-0560-4ccc-81d9-0ddec98ac6d0","last_name":"","phone":"69276918","postcode":"58430","state":"Midtjylland","title":"Mr"},"publish_time":"2023-12-27T13:02:19.823+05:30","event_time":"2023-12-27T13:02:19.823+05:30","producer_name":"pulsar-1-12","topic":"persistent://public/default/random_users_test_01"}
{"id":"CJYDEAEYACAA","string_id":"406:1:0","payload":{"age":"","city":"Gorakhpur","country":"India","email":"maanas.babu@example.com","first_name":"Maanas","gender":"male","id":"953c048e-1ace-4f2f-aa42-cbcf61eb5ef1","last_name":"","phone":"7414476524","postcode":"39965","state":"Uttar Pradesh","title":"Mr"},"publish_time":"2023-12-27T13:02:20.149+05:30","event_time":"2023-12-27T13:02:20.149+05:30","producer_name":"pulsar-1-12","topic":"persistent://public/default/random_users_test_01"}
{"id":"CJYDEAIYACAA","string_id":"406:2:0","payload":{"age":"","city":"Logroño","country":"Spain","email":"alex.vargas@example.com","first_name":"Alex","gender":"male","id":"e6f652ec-8388-4384-a3f2-c3e7f0541f1f","last_name":"","phone":"959-740-232","postcode":"32826","state":"Comunidad de Madrid","title":"Mr"},"publish_time":"2023-12-27T13:02:20.472+05:30","event_time":"2023-12-27T13:02:20.472+05:30","producer_name":"pulsar-1-12","topic":"persistent://public/default/random_users_test_01"}

```
- Read topics
```shell
~ dataos-ctl fastbase topic read -p -t persistent://public/default/random_users_test_01
INFO[0000] 🔍 read...                                    
INFO[0000] Connecting to broker                          remote_addr="pulsar+ssl://tcp.fun-bluegill.dataos.app:6651"
INFO[0000] TCP connection established                    local_addr="192.168.1.164:60561" remote_addr="pulsar+ssl://tcp.fun-bluegill.dataos.app:6651"
INFO[0001] Connection is ready                           local_addr="192.168.1.164:60561" remote_addr="pulsar+ssl://tcp.fun-bluegill.dataos.app:6651"
INFO[0001] Connecting to broker                          remote_addr="pulsar+ssl://tcp.fun-bluegill.dataos.app:6651"
INFO[0001] TCP connection established                    local_addr="192.168.1.164:60562" remote_addr="pulsar+ssl://tcp.fun-bluegill.dataos.app:6651"
INFO[0001] Connection is ready                           local_addr="192.168.1.164:60562" remote_addr="pulsar+ssl://tcp.fun-bluegill.dataos.app:6651"
INFO[0001] Connected consumer                            consumerID=1 name=fa25137869f8fd0411138ecf63b3c2a9b3e92c2e405efa119c108e4800dc0976 subscription=reader-aeosu topic="persistent://public/default/random_users_test_01"
INFO[0001] Created consumer                              consumerID=1 name=fa25137869f8fd0411138ecf63b3c2a9b3e92c2e405efa119c108e4800dc0976 subscription=reader-aeosu topic="persistent://public/default/random_users_test_01"
INFO[0001] Broker notification of Closed consumer: 1     local_addr="192.168.1.164:60562" remote_addr="pulsar+ssl://tcp.fun-bluegill.dataos.app:6651"
INFO[0001] Reconnecting to broker in 113.791763ms        consumerID=1 name=fa25137869f8fd0411138ecf63b3c2a9b3e92c2e405efa119c108e4800dc0976 subscription=reader-aeosu topic="persistent://public/default/random_users_test_01"
INFO[0001] Connected consumer                            consumerID=1 name=fa25137869f8fd0411138ecf63b3c2a9b3e92c2e405efa119c108e4800dc0976 subscription=reader-aeosu topic="persistent://public/default/random_users_test_01"
INFO[0001] Reconnected consumer to broker                consumerID=1 name=fa25137869f8fd0411138ecf63b3c2a9b3e92c2e405efa119c108e4800dc0976 subscription=reader-aeosu topic="persistent://public/default/random_users_test_01"
{"id":"CJkREKzDARgAIAA=","string_id":"2201:25004:0","payload":"SDlkNTlhNDViLTYwNTQtNDdmOC1hMDMxLTIwNTlmZDJmNjczMwZNcnMOR2VvcmdpYQAMZmVtYWxlNGdlb3JnaWEud2lsbGlzQGV4YW1wbGUuY29tFEJpcm1pbmdoYW0ISW93YRpVbml0ZWQgU3RhdGVzCjcwNTMxABwoMzE0KSA5NjktNDU5Mw==","publish_time":"2024-01-04T16:20:34.785+05:30","event_time":"2024-01-04T16:20:34.785+05:30","producer_name":"pulsar-44-4","topic":"persistent://public/default/random_users_test_01"}
INFO[0003] no more messages to read...exiting           
INFO[0003] Closing consumer=1                            consumerID=1 name=fa25137869f8fd0411138ecf63b3c2a9b3e92c2e405efa119c108e4800dc0976 subscription=reader-aeosu topic="persistent://public/default/random_users_test_01"
INFO[0003] Closed consumer                               consumerID=1 name=fa25137869f8fd0411138ecf63b3c2a9b3e92c2e405efa119c108e4800dc0976 subscription=reader-aeosu topic="persistent://public/default/random_users_test_01"
INFO[0003] close consumer, exit reconnect                consumerID=1 name=fa25137869f8fd0411138ecf63b3c2a9b3e92c2e405efa119c108e4800dc0976 subscription=reader-aeosu topic="persistent://public/default/random_users_test_01"
INFO[0003] 🔍 read...complete   
```

## **Configuring Pulsar**

Configuring Pulsar is crucial to managing message queues efficiently. Here’s how you can adjust key settings:

### **Key Pulsar adjustments**

- **Broker configuration:**
    
    You may need to tweak the broker stats interval for better performance:
    
    ```bash
    pulsar.brokerStatsIntervalSeconds=60
    ```
    
- **Restarting brokers:**
    
    After making changes, restart the broker deployment:
    
    ```bash
    kubectl rollout restart deployment <broker-deployment> --namespace <namespace>
    ```
    

### **Storage and retention policies**

Ensure that Pulsar has sufficient storage and that you’ve set proper message retention policies:

- **Message retention policy:** Configure how long messages are retained in topics.
- **Scaling Pulsar:** Use Kubernetes Horizontal Pod Autoscaler to adjust broker and bookie replicas when needed.

By following these steps, you’ll be able to manage Kubernetes and Pulsar effectively, ensuring the stability, scalability, and efficiency of your DataOS platform.