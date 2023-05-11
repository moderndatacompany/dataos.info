# Case Scenario: Creating and Getting Dataset

## Create Dataset / Index

The following command can be used to create a dataset

```bash
dataos-ctl dataset -a dataos://icebase:retail/city create \
-f <manifest-file-path>
```

Creating a dataset will require a YAML File, whose path has to be provided in the above path. The sample format for the YAML file is provided below.

YAML Example for Dataset Creation (Manifest File For Iceberg)

```yaml
schema: # <mandatory>
  type: "avro"
  avro: '{"type":"record","name":"defaultName","fields":[{"name":"__metadata","type":{"type":"map","values":"string","key-id":10,"value-id":11},"field-id":1},{"name":"city_id","type":["null","string"],"default":null,"field-id":2},{"name":"zip_code","type":["null","int"],"default":null,"field-id":3},{"name":"city_name","type":["null","string"],"default":null,"field-id":4},{"name":"county_name","type":["null","string"],"default":null,"field-id":5},{"name":"state_code","type":["null","string"],"default":null,"field-id":6},{"name":"state_name","type":["null","string"],"default":null,"field-id":7},{"name":"version","type":"string","field-id":8},{"name":"ts_city","type":{"type":"long","logicalType":"timestamp-micros","adjust-to-utc":true},"field-id":9}]}'
iceberg: # <optional>
  specs: # <optional>
    - index: 1
      type: "identity"
      column: "state_name"
			name: "state_name" # <optional>
		- index: 2
      type: year
      column: __ts
	    name: "year" # <optional>
  properties: # <optional>
    write.format.default: "parquet"
    prop1: "value1"
```

Let’s say we want to create a new dataset by the name the YAML for which is given below

```yaml
schema: # <mandatory>
  type: "avro"
  avro: '{"type":"record","name":"defaultName","fields":[{"name":"__metadata","type":{"type":"map","values":"string","key-id":10,"value-id":11},"field-id":1},{"name":"city_id","type":["null","string"],"default":null,"field-id":2},{"name":"zip_code","type":["null","int"],"default":null,"field-id":3},{"name":"city_name","type":["null","string"],"default":null,"field-id":4},{"name":"county_name","type":["null","string"],"default":null,"field-id":5},{"name":"state_code","type":["null","string"],"default":null,"field-id":6},{"name":"state_name","type":["null","string"],"default":null,"field-id":7},{"name":"version","type":"string","field-id":8},{"name":"ts_city","type":{"type":"long","logicalType":"timestamp-micros","adjust-to-utc":true},"field-id":9}]}'
iceberg: # <optional>
  specs: # <optional>
    - index: 1
      type: identity
      column: state_name
  properties: # <optional>
    write.format.default: "parquet"
    prop1: "value1"
```

Save the file and copy its path, then execute the command as 

```yaml
dataos-ctl dataset -a dataos://icebase:retail/city2 create -f /home/folder/new.yml
```

Output (on successful execution)

```yaml
INFO[0000] 📂 create dataset...                          
INFO[0003] 📂 create dataset...completed
```

## Get Dataset

To get an existing dataset, the following command can be used.

```bash
dataos-ctl dataset -a dataos://icebase:retail/city get
```

Output

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