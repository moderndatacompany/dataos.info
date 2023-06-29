# Schema Configurations

This section demonstrates how to supply schema when reading data using Flare stack from a Depot. There are different schema options available, including **AVRO Schema**, **SparkJson Schema**, and **SparkDDL Schema.**

### **Input Options for Schema**

To specify the schema for your data in Flare, you can use the following YAML configuration:

```yaml
inputs:
  - name: city_connect
    dataset: dataos://thirdparty01:none/city
    format: csv
    schemaType:
    schemaPath: 
    schemaString: 
```

If you don't define the `schemaType` field but provide a `schemaPath`, Flare will consider it as an AVRO schema.

### **AVRO Schema**

To apply an AVRO schema, you have three options:

- Without specifying the schema type, you can provide the `schemaPath` field, and Flare will automatically consider it as an AVRO schema.

```yaml
inputs:
  - name: city_connect
    dataset: dataos://thirdparty01:none/city
    format: csv
    schemaPath: dataos://thirdparty01:none/schemas/avsc/city.avsc
```

- Create a `.avsc` file, upload it to a location, and use it with a Depot.

```yaml
inputs:
  - name: city_connect
    dataset: dataos://thirdparty01:none/city
    format: csv
    schemaType: AVRO
    schemaPath: dataos://thirdparty01:none/schemas/avsc/city.avsc
```

- You can also provide the AVRO schema directly as a schema string:

```yaml
inputs:
  - name: city_connect
    dataset: dataos://thirdparty01:none/city
    format: csv
    schemaType: AVRO
    schemaString: '{"type":"record","name":"defaultName","namespace":"defaultNamespace","fields":[{"name":"city_id","type":["null","string"],"default":null},{"name":"zip_code","type":["null","int"],"default":null},{"name":"city_name","type":["null","string"],"default":null},{"name":"county_name","type":["null","string"],"default":null},{"name":"state_code","type":["null","string"],"default":null},{"name":"state_name","type":["null","string"],"default":null}]}'
```

### **SparkJson Schema**

Similar to the AVRO schema, you can use SparkJson schema with the same combinations of `schemaType`, `schemaPath`, and `schemaString`. The only difference lies in the format of the file containing the schema when using `schemaPath`.

```yaml
inputs:
  - name: city_connect
    dataset: dataos://thirdparty01:none/city
    format: csv
    schemaType: sparkJson
    schemaPath: dataos://thirdparty01:none/schemas/avsc/city.json
    schemaString: "schema json schema string"
```

### **SparkDDL Schema**

For applying SparkDDL schema, use the following YAML configuration:

```yaml
inputs:
  - name: city_connect
    dataset: dataos://thirdparty01:none/city
    format: csv
    schemaType: sparkJson
    schemaPath: dataos://thirdparty01:none/schemas/avsc/city.ddl
    schemaString: "city_id string, zip_code integer, city_name string, county_name string, state_code string, state_name string"
```

Make use of these schema options in Flare to effectively define the structure of your data and enhance your data development workflows.