# Case Scenario: Create, Get, and Drop Dataset

## Create Dataset/Index

The following command can be used to create a dataset.

```bash
dataos-ctl dataset -a dataos://icebase:retail/city create \
-f <manifest-file-path>
```

Creating a dataset will require a YAML File, whose path has to be provided in the manifest file path. The sample format for the YAML file is provided below.

**YAML Example for Dataset Creation (Manifest File For Iceberg)**

```yaml
schema: # <mandatory>
  type: "avro"
  avro: '{"type": "record", "name": "defaultName", "fields":[{"name": "__metadata", "type" :{"type": "map", "values": "string", "key-id":10, "value-id":11}, "field-id":1},{"name": "city_id", "type" :[ "null", "string"], "default":null, "field-id":2},{"name": "zip_code", "type" :[ "null", "int"], "default":null, "field-id":3},{"name": "city_name", "type" :[ "null", "string"], "default":null, "field-id":4},{"name": "county_name", "type" :[ "null", "string"], "default":null, "field-id":5},{"name": "state_code", "type" :[ "null", "string"], "default":null, "field-id":6},{"name": "state_name", "type" :[ "null", "string"], "default":null, "field-id":7},{"name": "version", "type": "string", "field-id":8},{"name": "ts_city", "type" :{"type": "long", "logicalType": "timestamp-micros", "adjust-to-utc":true}, "field-id":9}]}'
iceberg: # <optional>
  specs: # <optional>
    - index: 1
      type: "identity"
      column: "state_name"
      name: "state_name" # <optional>
    - index: 2
      type: year
      column: ts_city
      name: "year" # <optional>
  properties: # <optional>
    write.format.default: "parquet"
    prop1: "value1"
```

Let’s say we want to create a new dataset by the name `city2`. We can use the YAML provided above, save it, copy its path, and then execute the below command.

```yaml
dataos-ctl dataset -a dataos://icebase:retail/city2 create -f /home/folder/new.yml
```

Output (on successful execution)

```yaml
INFO[0000] 📂 create dataset...                          
INFO[0003] 📂 create dataset...completed
```

## Get Dataset

The `get` command to fetch a dataset from the `udl - dataos://icebase:retail/city` is given below.

```bash
dataos-ctl dataset -a dataos://icebase:retail/city get
```

Expected Output

```bash
INFO[0000] 📂 get dataset...                             

schema:
  type: avro
  avro: '{"type":"record","name":"defaultName","fields":[{"name":"__metadata","type":{"type":"map","values":"string","key-id":10,"value-id":11},"field-id":1},{"name":"city_id","type":["null","string"],"default":null,"field-id":2},{"name":"zip_code","type":["null","long"],"default":null,"field-id":3},{"name":"city_name","type":["null","string"],"default":null,"field-id":4},{"name":"county_name","type":["null","string"],"default":null,"field-id":5},{"name":"state_code","type":["null","string"],"default":null,"field-id":6},{"name":"state_name","type":["null","string"],"default":null,"field-id":7},{"name":"version","type":"string","field-id":8},{"name":"ts_city","type":{"type":"long","logicalType":"timestamp-micros","adjust-to-utc":true},"field-id":9},{"name":"random","type":["null","string"],"default":null,"field-id":25}]}'
iceberg:
  specs:
  - index: 1000
    type: month
    column: month_partition
  properties:
    write.metadata.compression-codec: gzip

INFO[0001] 📂 get dataset...completed
```

## Drop Dataset

<aside style="background-color:#FAF3DD; padding:15px; border-radius:5px;">
🗣 To execute this command, it is necessary to possess the `roles:id:operator` tag or obtain the suitable use case assignment from the DataOS operator.

</aside>

**Delete the Entry from Metastore only (not data files)**

To drop a dataset that already exists within the Icebase depot, you can use the commands given in the code block below; this would delete the corresponding entry from the metastore while leaving the source file intact.

```bash
dataos-ctl dataset -a dataos://icebase:retail/city drop
# OR
dataos-ctl dataset -a dataos://icebase:retail/city drop -p false # -p flag is Purge Value (its by default: false)
# OR
dataos-ctl dataset -a dataos://icebase:retail/city drop --purge false
```

Output

```bash
INFO[0000] 📂 drop dataset...                            
INFO[0001] 📂 drop dataset...completed
```

**Delete the Entry from Metastore and also delete files**

To drop an existing dataset such that both the entry from the metastore gets deleted as well as the source files. It can be accomplished using the following commands.

```bash
dataos-ctl dataset -a dataos://icebase:retail/city drop -p true # -p flag is Purge Value (its by default: false)
# OR
dataos-ctl dataset -a dataos://icebase:retail/city drop --purge true
```

Output

```bash
INFO[0000] 📂 drop dataset...                            
INFO[0001] 📂 drop dataset...completed
```