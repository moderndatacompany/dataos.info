# `config.yaml` configurations

## Talos Specific Configurations

The `config.yaml` file is the main configuration file for a Talos project. It defines the essential settings and parameters to configure your Talos application. Below is a detailed explanation of each section of the `config.yaml` file:

```yaml
name: employee
description: A talos app
version: 0.0.1
logLevel: DEBUG
auth:
    heimdallUrl: https://liberal-donkey.dataos.app/heimdall
    userGroups:
    - name : intern
      description: intern group
      includes:
        - users:id:iamgroot
    - name : datadev
      description: data dev group
      includes:
        - roles:id:data-dev
       
metrics:
  type: summary
  percentiles: [ 0.5, 0.75, 0.95, 0.98, 0.99, 0.999 ]
rateLimit:
  enabled: true
  options:
    interval:
      min: 1
    max: 100
    delayAfter: 4
cors:
  enabled: true
  options:
    origin: 'https://google.com'
    allowMethods: 'GET'  
cachePath: tmp       
sources:
    - name: pg 
      type: pg
      connection:
        host: pg-db
        port: 5432
        user: postgres
        password: '12345'
        database: employee
```

### `name`

**Description:** Unique identifier for the Talos.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | Alphanumeric values with the RegEx [a-z0-9]([-a-z0-9]*[a-z0-9])
A hyphen/dash is allowed as a special character
The total length of the string should be less than or equal to 48 characters |

**Example Usage:**

```yaml
name: employee
```

### `description`

**Description:** Brief description of the Talos.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | Any descriptive text |

**Example Usage:**

```yaml
description: A talos app
```

### `version`

**Description:** The version of the Talos.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | Alphanumeric values with the RegEx [a-z0-9]([-a-z0-9]*[a-z0-9])
A hyphen/dash is allowed as a special character
The total length of the string should be less than or equal to 48 characters |

**Example Usage:**

```yaml
version: 0.1.6
```

### `logLevel`

**Description:** The level of logging detail.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | DEBUG, INFO, WARN, ERROR |

**Example Usage:**

```yaml
logLevel: DEBUG
```

### `auth`

**Description:** Authentication configuration.

### **`heimdallUrl`**

**Description:** URL for the authentication service.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | Any valid URL |

### **`userGroups`**

**Description:** Defines user groups with specific permissions.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| list | mandatory | none | List of user groups with their details |

**Example Usage:**

```yaml
auth:
    heimdallUrl: https://liberal-donkey.dataos.app/heimdall
    userGroups:
    - name: intern
      description: intern group
      includes:
        - users:id:iamgroot
    - name: datadev
      description: data dev group
      includes:
        - roles:id:data-dev
```

- **name**: Name of the user group.
- **description**: Description of the user group.
- **includes**: Specifies roles or users included in the group.
- **excludes**: Specifies roles or users excluded from the group.

### `metrics`

**Description:** Configuration for metrics collection.

### **`type`**

**Description:** Defines the type of metrics. It can be a `histogram` or `summary`.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | summary, histogram |

### **`percentiles`**

**Description:**  (For summary) Defines the percentiles to be calculated.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| list of floats | mandatory | none | List of percentiles |

**Example Usage:**

```yaml
metrics:
  type: summary
  percentiles: [0.5, 0.75, 0.95, 0.98, 0.99, 0.999]
```

### **`buckets`**

**Description:** (For histogram) Defines bucket boundaries for the histogram.

### `rateLimit`

**Description:** Rate limiting configuration.

**Example Usage:**

```yaml
rateLimit:
  enabled: true
  options:
    interval:
      min: 1
    max: 100
    delayAfter: 4
```

### **`enabled`**

**Description:** Enables or disables rate limiting.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| boolean | mandatory | none | true, false |

### **`options`**

**Description:** Configures rate limiting options.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| object | mandatory | none | Contains interval and max options |

### **`interval`**

**Description:** Defines the time interval for rate limiting.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| object | mandatory | none | Contains min option |

### **`min`**

**Description:** The minimum number of requests is allowed at the interval.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| integer | mandatory | none | Minimum interval in minutes |

### **`max`**

**Description:**  Maximum number of requests allowed in the interval.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| integer | mandatory | none | Maximum number of requests allowed |

**`delayAfter`**

**Description:** Number of requests after which a delay is enforced.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| integer | mandatory | none | Number of requests after which delay is applied |

### `cors`

**Description:** Cross-Origin Resource Sharing configuration.

### **`enabled`**

**Description:** Enables or disables CORS.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| boolean | mandatory | none | true, false |

### **`options`**

**Description:** Configures CORS settings.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| object | mandatory | none | Contains origin and allow methods options |

### **`origin`**

**Description:** Specifies the allowed origin for requests.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | Any valid URL |

### **`allowMethods`**

**Description:** Specifies the HTTP methods allowed for requests.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | List of HTTP methods |

**Example Usage:**

```yaml
cors:
  enabled: true
  options:
    origin: 'https://google.com'
    allowMethods: 'GET'
```

### `cachePath`

**Description:** Path for cache storage.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | Any valid file path |

**Example Usage:**

```yaml
cachePath: tmp
```

### `sources`

**Description:** Configuration for data sources.

### **`name`**

**Description:** Name of the data source.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | Any valid name |

### **`type`**

**Description:** Type of the data source (e.g., `duckdb`, `pg`).

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | Type of the data source (e.g., pg) |

### **`connection`**

**Description:** Defines the connection details for the PostgreSQL database.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| object | mandatory | none | Contains host, port, user, password, and database options |

### **`host`**

**Description:** Hostname of the PostgreSQL server.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | Any valid hostname |

### `port`

**Description:** Port for database access.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| integer | mandatory | none | Any valid port number |

### `user`

**Description:** Username for database access.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | Any valid username |

### `password`

**Description:** Password for database access.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | Any valid password |

### `database`

**Description:** Name of the database.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | Any valid database name |

**Example Usage:**

```yaml
yamlCopy code
sources:
  - name: pg
    type: pg
    connection:
      host: pg-db
      port: 5432
      user: postgres
      password: '12345'
      database: employee

```