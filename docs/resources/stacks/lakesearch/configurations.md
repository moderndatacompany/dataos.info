This section provides details of configuring and indexing Lakehouse tables via Lakesearch.

```yaml
# service specific section
name: testingls
version: v1
type: service
tags:
  - service
  - dataos:type:resource
  - dataos:resource:service
  - dataos:layer:user
description: Lakesearch Service Simple Index Config
workspace: public
service:
  servicePort: 4080
  ingress:
    enabled: true
    stripPath: false
    path: /lakesearch/public:testingls
    noAuthentication: true
  replicas: 1
  logLevel: 'DEBUG'
  compute: runnable-default
  envs:
    LAKESEARCH_SERVER_NAME: "public:testingls"
    DATA_DIR: public/testingls/sample
    USER_MODULES_DIR: /etc/dataos/config
  persistentVolume:
    name: ls-v2-test-vol
    directory: public/testingls/sample
  resources:
    requests:
      cpu: 1000m
      memory: 1536Mi
  stack: lakesearch:6.0
  stackSpec:
    lakesearch:
# index specific section    
      source:
        datasets:
          - name: city
            dataset: dataos://icebase:retail/city
            options:
              region: ap-south-1
      index_tables:
        - name: city
          description: "index for cities"
          tags:
            - cities
          properties:
            morphology: stem_en
          columns:
            - name: city_id
              type: keyword
            - name: zip_code
              type: bigint  
            - name: id
              description: "mapped to row_num"
              tags:
                - identifier
              type: bigint
            - name: city_name
              type: keyword
            - name: county_name
              type: keyword
            - name: state_code
              type: keyword
            - name: state_name
              type: text
            - name: version
              type: text
            - name: ts_city
              type: timestamp

      indexers:
        - index_table: city
          base_sql: |
            SELECT 
              city_id,
              zip_code,
              zip_code as id,
              city_name,
              county_name,
              state_code,
              state_name,
              version,
              cast(ts_city as timestamp) as ts_city

            FROM 
              city
          options:
            start: 1734979551
            step: 86400
            batch_sql: |
              WITH base AS (
                  {base_sql}
              ) SELECT 
                * 
              FROM 
                base 
              WHERE 
                epoch(ts_city) >= {start} AND epoch(ts_city) < {end}
            throttle:
              min: 10000
              max: 60000
              factor: 1.2
              jitter: true
```

The service YAML is divided into two main sections, Service-specific configurations and Index specific configurations.

## Service-specific configuration

### **name**

**Description:** Declare a name for the Resource.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | Alphanumeric values with regex `[a-z0-9]([-a-z0-9]*[a-z0-9])` (max length: 48 characters) |

**Additional Information:** Two resources in the same workspace cannot have the same name.

**Example usage:**

```
name: testingls
```

---

### **version**

**Description:** The version of the Resource.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | v1, v1beta, v1alpha, v2alpha |

**Example usage:**

```
version: v1
```

---

### **type**

**Description:** Provide the type of the Resource.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | cluster, compute, depot, policy, secret, service, stack, workflow |

**Example usage:**

```
type: service
```

---

### **tags**

**Description:** Assign tags to the Resource instance.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list | mandatory | none | Any string; special characters allowed |

**Example usage:**

```
tags:
  - service
  - dataos:type:resource
  - dataos:resource:service
  - dataos:layer:user
```

---

### **description**

**Description:** Assign a description to the Resource.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | Any string |

**Additional Information:** The description can be within quotes or without.

**Example usage:**

```
description: "Lakesearch Service Simple Index Config"
```

---

### **workspace**

**Description:** Defines the workspace where the Resource belongs.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | Any valid workspace name |

**Example usage:**

```
workspace: public
```

---

### **service**

**Description:** Defines the service configuration.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | mandatory | none | Contains attributes like `servicePort`, `ingress`, `replicas`, `logLevel`, `compute`, etc. |

**Example usage:**

```
service:
  servicePort: 4080
  ingress:
    enabled: true
    stripPath: false
    path: /lakesearch/public:testingls
    noAuthentication: true
  replicas: 1
  logLevel: 'DEBUG'
  compute: runnable-default
```

---

### **servicePort**

**Description:** Defines the port on which the service runs.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| integer | mandatory | none | Any valid port number (e.g., 1024–65535) |

**Example usage:**

```yaml

servicePort: 4080

```

---

### **ingress**

**Description:**

The `ingress` attribute defines the network exposure configuration for the **LakeSearch** service. It controls how external requests are routed to the service, whether authentication is required, and how paths are handled.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| object | optional | none | Contains **enabled**, **stripPath**, **path**, and **noAuthentication** |

---

### **ingress.enabled**

**Description:**

Determines whether ingress is enabled for exposing the service.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| boolean | mandatory | false | `true` (ingress is enabled), `false` (ingress is disabled) |

**Example Usage:**

```yaml

ingress:
  enabled: true

```

---

### **ingress.stripPath**

**Description:**

Controls whether the request path should be stripped before forwarding it to the service.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| boolean | optional | false | `true` (removes path prefix), `false` (keeps full path) |

**Example Usage:**

```yaml

ingress:
  stripPath: false

```

---

### **ingress.path**

**Description:**

Specifies the URL path that will be exposed through ingress.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | A valid URL path |

**Example Usage:**

```yaml

ingress:
  path: /lakesearch/public:testingls

```

In this example, the service is exposed at `/lakesearch/public:testingls`.

---

### **ingress.noAuthentication**

**Description:**

Defines whether authentication is required to access the exposed service.

<aside class="callout">

To remove the `noAuthentication: true` key from the ingress section, a DataOS operator needs to create a usecase in Bifrost and grant the use case to a user tag. 
</aside>

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| boolean | optional | false | `true` (no authentication required), `false` (authentication required) |

**Example Usage:**

```yaml

ingress:
  noAuthentication: true

```

This allows unrestricted public access to the service.

### **replicas**

**Description:** Specifies the number of service instances to run.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| integer | optional | 1 | Any positive integer |

**Example usage:**

```yaml

replicas: 1

```

---

### **logLevel**

**Description:** Defines the logging level for debugging and monitoring.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | INFO | DEBUG, INFO, WARN, ERROR |

**Example usage:**

```yaml

logLevel: 'DEBUG'

```

---

### **compute**

**Description:** Specifies the compute environment where the service runs.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | runnable-default, custom environments |

**Example usage:**

```yaml

compute: runnable-default

```

---

### **envs**

**Description:** Defines environment variables for configuring the service.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| object | optional | none | Key-value pairs defining runtime settings |

**Example usage:**

```yaml

envs:
  LAKESEARCH_SERVER_NAME: "public:testingls"
  DATA_DIR: public/testingls/sample
  USER_MODULES_DIR: /etc/dataos/config

```

---

### **LAKESEARCH_SERVER_NAME**

**Description:** Defines the server name that exposes the ingress path.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | Any alphanumeric string following naming conventions and `<workspace>:<servie_name>` nomenclature |

**Example Usage:**

```yaml

envs:
  LAKESEARCH_SERVER_NAME: "public:testingls"

```

In this example, the server name is set to `public:testingls`, which uniquely identifies the LakeSearch instance.

---

### **DATA_DIR**

**Description:** Sets the path for the persistent volume where indexes are stored. This always follows the below nomenclature.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | A valid directory path that follows `<workspace>/<servie_name>/<folder_name>` nomenclature |

**Example Usage:**

```yaml

envs:
  DATA_DIR: public/testingls/sample

```

This configuration sets the data directory to `public/testingls/sample`, where LakeSearch stores its indexed datasets.

---

### **USER_MODULES_DIR**

**Description:**

Specifies the directory path for user-defined modules and configurations used by **LakeSearch**.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | optional | none | A valid absolute directory path |

**Example Usage:**

```yaml
envs:
  USER_MODULES_DIR: /etc/dataos/config
```

This indicates that user-specific configuration files are located in `/etc/dataos/config`.

---

### **persistentVolume**

**Description:** Specifies a common storage location for Lakehouse services. This accepts the following two keys:

- `name`: Name of the persistent volume claim.
- `directory`: Path where you intend to store the indexed documents. It is important to ensure that the path defined here and the one defined in the `DATA_DIR` environment variable are the same. This always follows the below nomenclature.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| object | mandatory | none | Defines storage location with `<workspace>/<servie_name>/<folder_name>` nomenclature and volume name |

If a Volume is not already configured in the environment, create a new one by referring to [this link](/resources/volume/).

**Example usage:**

```yaml
persistentVolume:
  name: ls-v2-test-vol
  directory: public/testingls/sample
```

---

### **resources**

**Description:** Specifies resource requests and limits for compute allocation.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| object | optional | none | Defines CPU and memory allocation |

**Additional Information:**

- `requests.cpu`: CPU units requested (e.g., 1000m = 1 core).
- `requests.memory`: Memory requested (in MiB or GiB).

**Example usage:**

```yaml

resources:
  requests:
    cpu: 1000m
    memory: 1536Mi

```

---

### **stack**

**Description:** Indicates the version of the Lakesearch Stack for the Service to run.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | Format: `<stack-name>:<version>` |

**Example usage:**

```yaml
stack: lakesearch:6.0
```

---

### **stackSpec**

**Description:** The `stackSpec` attribute defines the stack-specific configurations required to deploy and manage the indexing pipeline for **LakeSearch**. It encapsulates settings related to data sources, indexing tables, and indexing processes.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| object | mandatory | none | Contains **lakesearch** configurations |

---

### **lakesearch**

**Description:** The `lakesearch` attribute within `stackSpec` specifies configurations for indexing data in LakeSearch, including data sources, index tables, and indexing processes.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| object | mandatory | none | Contains **source**, **index_tables**, and **indexers** |

---

## Index specific configuration

This section handles specific table details and indexing configurations. Lakesearch supports indexing either a single table or multiple tables within a service, depending on the setup in the `stackSpec`.

### **source**

**Description:** Defines the dataset(s) that act as input for indexing.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| object | mandatory | none | Contains **datasets** |


Lakesearch supports four types of sources.

<div class="grid" markdown>

=== "Dataset"
    === "Syntax"
        ```yaml
        source:
          datasets:
            - name: <name of the dataset>
              dataset: <fully qualified name of the dataset>
              options: (optional)
                region: <region> (required for Env. created on AWS cloud) 
        ```
    === "Example"
        ```yaml
        source:
          datasets:
            - name: devices
              dataset: dataos://icebase:lenovo_ls_data/devices_with_d
              options:
        ```       



=== "Flash"
    === "Syntax"
        ```yaml
        source:
          flash: <workspace>:<name of Flash service>
          options:
            sslmode: disable
        # or
        source:
          postgres: flash://<workspace>.<name of Flash service>
        ```
    === "Example"
        ```yaml
        source:
          flash: public:flash-test-9
          options:
            sslmode: disable
        ---- OR ----
        source:
          postgres: flash://public.flash-test-9
        ```


=== "PostgreSQL"
    === "Syntax"
        ```yaml
        source:
          postgres: postgresql://username:password@host:port/database?sslmode=disable
        ---- OR ----
        source:
          postgres: depot://<depot_name>
        ```
    === "Example"
        ```yaml
        source:
          postgres: postgresql://admin:admin@flash:5433/main?sslmode=disable
        ---- OR ----
        source:
          postgres: depot://stpostgres
        ```


=== "Depot (Postgres)"
    === "Syntax"
        ```yaml
        source:
          depot: dataos://<name of the depot>
        ```
    === "Example"
        ```yaml
        source:
          depot: dataos://mysqltest
        ```
</div>




---

### **datasets**

**Description:** Defines the input datasets used by LakeSearch.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list | mandatory | none | List of dataset objects containing `name`, `dataset`, and `options` |

**Additional Information:**

- `name`: Defines the dataset identifier.
- `dataset`: Specifies the dataset reference.
- `options`: Contains configuration settings (e.g., region).

**Example usage:**

```yaml

source:
  datasets:
    - name: city
      dataset: dataos://icebase:retail/city
      options:
        region: ap-south-1

```

---

### **index_tables**

**Description:** Defines the structure and metadata of an index table used in LakeSearch.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list | mandatory | none | List of index table definitions |

---

### **index_tables.name**

**Description:** The name of the index table.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | Alphanumeric string (max length: 48 characters) |

**Example usage:**

```yaml
name: city
```

---

### **index_tables.description**

**Description:** A brief description of the index table’s purpose.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | Any descriptive text |

**Example usage:**

```yaml
description: "index for cities"
```

---

### **index_tables.tags**

**Description:** Labels used to categorize the index table.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list | optional | none | List of strings |

**Example usage:**

```yaml
tags:
  - cities
```

---

### **index_tables.properties**

**Description:** Defines specific properties for text processing and indexing behavior.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| object | optional | none | Configuration parameters (e.g., morphology) |

**Example usage:**

```yaml

properties:
  morphology: stem_en
```

---

### **index_tables.columns**

**Description:** Specifies the schema of the indexed data, including column names, types, and metadata. Users can choose to include all columns from the dataset or exclude specific columns from indexing based on their requirements..

<aside class="callout">

Note that while adding the columns while indexing a table it is required to add an additional column named `id` of type `bigint` as shown below:

```yaml
      index_tables:
        - name: newcity
          description: "index for cities"
          tags:
            - cities
          properties:
            morphology: stem_en
          columns:
            - name: city_id
              type: keyword
            - name: zip_code
              type: bigint  
            - name: id              # additional column (mandatory)
              description: "mapped to row_num"
              tags:
                - identifier
              type: bigint
            - name: city_name
              type: keyword
            - name: county_name
              type: keyword
            - name: state_code
              type: keyword
            - name: state_name
              type: text
            - name: version
              type: text
            - name: ts_city
              type: timestamp
```

This will be mapped with the primary key column in the indexer base SQL as `id`.

```yaml
      indexers:
        - index_table: newcity
          base_sql: |
            SELECT 
              city_id,
              zip_code,
              zip_code as id,  # primary key
              city_name,
              county_name,
              state_code,
              state_name,
              version,
              cast(ts_city as timestamp) as ts_city

            FROM 
              city
```

</aside>

| Data Type | Requirement | Default Value | Possible Value              |
|-----------|------------|---------------|-----------------------------|
| list      | mandatory  | none          | List of column definitions  |


---

### **index_tables.columns.name**

**Description:** The name of the column in the index table.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | Alphanumeric string |

**Example usage:**

```yaml

name: city_id

```

---

### **index_tables.columns.type**

**Description:** The data type of the column.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | keyword, bigint, text, timestamp, etc. |

**Example usage:**

```yaml

type: keyword

```

<aside class="callout">

The data types defined in the `source.index_table` is different from standard SQL data types. For instance, a column with a `VARCHAR` data type in SQL should be defined as `TEXT` in the index_table. Similarly, an `INTEGER` column should be specified as `BIGINT`. If keyword-based searching is required for a column, its data type should be set to `KEYWORD`. Additionally, the `index_table` in the indexer must include an extra column named `ID` to designate the primary key.

</aside>

**Data types allowed**

| Data Type | Description | Category |
| --- | --- | --- |
| `text` | The text data type forms the full-text part of the table. Text fields are indexed and can be searched for keywords. | full-text field |
| `keyword` | Unlike full-text fields, string attributes are stored as they are received and cannot be used in full-text searches. Instead, they are returned in results, can be used to filter, sort and aggregate results. In general, it's not recommended to store large texts in string attributes, but use string attributes for metadata like names, titles, tags, keys, etc. | attribute |
| `int` | Integer type allows storing 32 bit **unsigned** integer values. | attribute |
| `bigint` | Big integers (bigint) are 64-bit wide **signed** integers. | attribute |
| `bool` | Declares a boolean attribute. It's equivalent to an integer attribute with bit count of 1. | attribute |
| `timestamp` | The timestamp type represents Unix timestamps, which are stored as 32-bit integers. The system expects a date/timestamp type object from the base_sql. | attribute |
| `float` | Real numbers are stored as 32-bit IEEE 754 single precision floats. | attribute |


---

### **index_tables.columns.description**

**Description:** A brief explanation of the column’s role.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | Any descriptive text |

**Example usage:**

```yaml

description: "mapped to row_num"

```

---

### **index_tables.columns.tags**

**Description:** Labels to classify the column (e.g., identifier columns).

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list | optional | none | List of strings |

**Example usage:**

```yaml

tags:
  - identifier

```

---

### **indexers**

**Description:** Defines indexing operations for tables, including SQL queries and execution parameters.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list | mandatory | none | List of indexers defining SQL transformations and processing options |

**Additional Information:**

- `index_table`: Name of the indexed table.
- `base_sql`: SQL query for extracting indexed data.
- `options`: Additional indexing settings (e.g., start time, batch size).
- `throttle`: Controls indexing rate with min/max limits.

**Example usage:**

```yaml

indexers:
  - index_table: city
    base_sql: |
      SELECT
        city_id,
        zip_code,
        zip_code as id,
        city_name,
        county_name,
        state_code,
        state_name,
        version,
        cast(ts_city as timestamp) as ts_city
      FROM
        city
    options:
      start: 1734979551
      step: 86400
      batch_sql: |
        WITH base AS (
            {base_sql}
        ) SELECT
          *
        FROM
          base
        WHERE
          epoch(ts_city) >= {start} AND epoch(ts_city) < {end}
    throttle:
      min: 10000
      max: 60000
      factor: 1.2
      jitter: true

```

### **indexers.index_table**

**Description:** Specifies the target index table where data will be stored.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | Name of an existing index table |

**Example usage:**

```yaml

index_table: city

```

---

### **indexers.base_sql**

**Description:** The SQL query used to extract data from the source dataset before indexing.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string (SQL) | mandatory | none | Valid SQL query |

**Example usage:**

```yaml

base_sql: |
  SELECT
    city_id,
    zip_code,
    zip_code as id,
    city_name,
    county_name,
    state_code,
    state_name,
    version,
    cast(ts_city as timestamp) as ts_city
  FROM
    city

```

---

### **indexers.options**

**Description:** Defines additional indexing parameters such as batch processing settings.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| object | optional | none | Contains `start`, `step`, and `batch_sql` |

---

### **indexers.options.start**

**Description:** Specifies the starting epoch timestamp for indexing data.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| integer | optional | none | UNIX timestamp (e.g., `1734979551`) |

**Example usage:**

```yaml

start: 1734979551

```

---

### **indexers.options.step**

**Description:** Defines the time step in seconds between batch executions.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| integer | optional | none | Time interval in seconds (e.g., `86400` for daily indexing) |

**Example usage:**

```yaml

step: 86400

```

---

### **indexers.options.batch_sql**

**Description:** SQL query used for batch processing of indexed data based on time intervals.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string (SQL) | optional | none | Valid SQL query |

**Example usage:**

```yaml

batch_sql: |
  WITH base AS (
      {base_sql}
  ) SELECT
    *
  FROM
    base
  WHERE
    epoch(ts_city) >= {start} AND epoch(ts_city) < {end}

```

---

### **indexers.throttle**

**Description:** Controls the rate at which indexing operations are executed.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| object | optional | none | Contains `min`, `max`, `factor`, and `jitter` |


- **`min`**: Minimum number of records processed per batch.
- **`max`**: Maximum number of records processed per batch.
- **`factor`**: Scaling factor for adjusting batch size dynamically.
- **`jitter`**: Enables randomness to prevent synchronized execution patterns.

**Example usage:**

```yaml

throttle:
  min: 10000
  max: 60000
  factor: 1.2
  jitter: true

```