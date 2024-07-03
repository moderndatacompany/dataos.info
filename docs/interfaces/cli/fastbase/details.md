# Fastbase Command Group
You run the following `fastbase` sub commands by appending them to *dataos-ctl fastbase*.

## `namespace`
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
### **`list`**
List namespaces in the DataOS® FastBase

```shell

Usage:
  dataos-ctl fastbase namespace list [flags]

Flags:
  -h, --help            help for list
  -t, --tenant string   FastBase tenant
```
## `tenant`
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
### **`list`**
List tenants in the DataOS® FastBase

```shell

Usage:
  dataos-ctl fastbase tenant list [flags]

Flags:
  -h, --help   help for list
```

## `topic`
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

### **`consume`**
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

### **`permissions`**
List Permissions of a Topic in the DataOS® FastBase
```shell

Usage:
  dataos-ctl fastbase topic permissions [flags]

Flags:
  -h, --help           help for permissions
  -t, --topic string   FastBase topic to read message from
```

### **`read`**
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