# `config.yaml` configurations

The `config.yaml` file is the main configuration file for a Talos project. It defines the essential settings and parameters to configure your Talos application. Below is a detailed explanation of each section of the `config.yaml` file:

## Sample manifest file:

```yaml
name: ${{superstore}}
description: ${{A talos-depot-postgres app}} # description
version: 0.1.26 # talos image version
logLevel: ${{'DEBUG'}}
auth:
  userGroups:
  - name: datadev    # name of the user group
    description: data dev group
    includes:
      - users:id:iamgroot
      - users:id:thisisthor
  - name: default
    description: Default group to accept everyone
    includes: "*"
 
 metrics:
  type: ${{summary}}    # type of metric collection: histogram or summary
  percentiles: [ 0.5, 0.75, 0.95, 0.98, 0.99, 0.999 ]  # (For summary) Defines the percentiles to be calculated
# buckets: [ 0.003, 0.03, 0.1, 0.3, 1.5, 10, 20, 50 ]  # (For histogram) Defines bucket boundaries for the histogram.
rateLimit:
  enabled: true
  options:
    interval:
      min: 1          # interval in minutes 
    max: 100        # max number of api request in interarval
    delayAfter: 5     # delay of 5 min after max attempt  
    
cors:                # Cross-Origin Resource Sharing
  enabled: true        
  options:
    origin: ${{'https://google.com'}}   # allowed origin for requests.
    allowMethods: 'GET'            # HTTP methods allowed
cachePath: tmp       
sources: # source details
  - name: ${{snowflakedepot}} # source name
    type: ${{depot}} # source type
    
    
```

### **`name`**

**Description:** Unique identifier for the Talos.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| string | mandatory | none | Alphanumeric values with the RegEx `[a-z0-9]([-a-z0-9]*[a-z0-9])` |

<aside class="callout">
🗣️ A hyphen (-) is allowed as a special character, and the string length must not exceed 48 characters.
  </aside>
**Example Usage:**

```yaml
name: employee
```

### **`description`**

**Description:** Brief description of the Talos.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| string | mandatory | none | Any descriptive text |

**Example Usage:**

```yaml
description: A talos app
```

### **`version`**

**Description:** The version of the Talos.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| string | mandatory | none | Alphanumeric values with the RegEx `[a-z0-9]([-a-z0-9]*[a-z0-9])` |

<aside class='callout'>
🗣️ A hyphen (-) is allowed as a special character, and the string length must not exceed 48 characters.
</aside>

**Example Usage:**

```yaml
version: "0.1.26-dev"
```

### **`logLevel`**

**Description:** The level of logging detail.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| string | mandatory | none | DEBUG, INFO, WARN, ERROR |

**Example Usage:**

```yaml
logLevel: DEBUG
```

### **`auth`**

**Description:** Authentication configuration.

### **`userGroups`**

**Description:** Defines user groups with specific permissions.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| list | mandatory | none | List of user groups with their details |

**Example Usage:**

```yaml
auth:
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

### **`metrics`**

**Description:** Configuration for metrics collection.

### **`type`**

**Description:** Defines the type of metrics. It can be a `histogram` or `summary`.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| string | mandatory | none | summary, histogram |

### **`percentiles`**

**Description:** (For summary) Defines the percentiles to be calculated.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| list of floats | mandatory | none | List of percentiles |

**Example Usage:**

```yaml
metrics:
  type: summary
  percentiles: [0.5, 0.75, 0.95, 0.98, 0.99, 0.999]
```

### **`buckets`**

**Description:** (For histogram) Defines bucket boundaries for the histogram.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| list of floats | mandatory | none | List of scaling  |

**Example Usage:**

```yaml
metrics:
  type: histogram
  buckets: [ 0.003, 0.03, 0.1, 0.3, 1.5, 10, 20, 50 ] 
```

### `rateLimit`

**Description:** The rate limiting configuration that defines the maximum number of requests allowed per minute.

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

**Description:** Enables or disables rate limiting

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| boolean | mandatory | none | true, false |

### **`options`**

**Description:** Configures rate limiting options.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| object | mandatory | none | Contains interval and max options |

### **`interval`**

**Description:** Defines the time interval for rate limiting.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| object | mandatory | none | Contains ‘min’ option |

### **`min`**

**Description:** The time interval, in minutes, during which the maximum number of allowed API requests can be made.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| integer | mandatory | none | Interval in minutes |

### **`max`**

**Description:** Maximum number of requests allowed in the interval.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| integer | mandatory | none | Maximum number of requests allowed |

### **`delayAfter`**

**Description:** The delay time, in minutes, imposed after the maximum number of API requests has been reached.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| integer | mandatory | none | Delayed time in Minutes |

### `cors`

**Description:** Cross-Origin Resource Sharing configuration.

### **`enabled`**

**Description:** Enables or disables CORS.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| boolean | mandatory | none | true, false |

### **`options`**

**Description:** Configures CORS settings.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| object | mandatory | none | Contains origin and allow methods options |

### **`origin`**

**Description:** Specifies the allowed origin for requests.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| string | mandatory | none | Any valid URL |

### **`allowMethods`**

**Description:** Specifies the HTTP methods allowed for requests.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
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

**Description:** Path for cache storage.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| string | mandatory | none | Any valid file path |

**Example Usage:**

```yaml
cachePath: tmp
```

### `sources`

**Description:** Configuration for data sources.

### **`name`**

**Description:** Name of the data source.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| string | mandatory | none | Any valid name |

### **`type`**

**Description:** Type of the data source (e.g., Depot, `duckdb`, `pg`).

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| string | mandatory | none | Type of the data source (e.g., pg, mySQL) or Depot  |