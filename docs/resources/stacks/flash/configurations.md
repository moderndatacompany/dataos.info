This section involves details of each attribute to help you better understand the Flash Service configurations.

```yaml
name: ${{flash-test}}
version: v1
type: service
tags:
  - ${{service}}
description: ${{flash service}}
workspace: ${{public}}
service:
  servicePort: ${{8080}}
  servicePorts:
  - name: ${{backup}}
    servicePort: ${{5433}}
  ingress:
    enabled: ${{true}}
    stripPath: ${{false}}
    path: ${{/flash/public:flash-test-6}}
    noAuthentication: ${{true}}
  replicas: ${{1}}
  logLevel: ${{info}}
  compute: ${{runnable-default}}
  envs:
    APP_BASE_PATH: ${{'dataos-basepath'}}
    FLASH_BASE_PATH: ${{/flash/public:flash-test-6}}
  resources:
    requests:
      cpu: ${{500m}}
      memory: ${{512Mi}}
    limits:
      cpu: ${{1000m}}
      memory: ${{1024Mi}}
  stack: flash+python:2.0
  stackSpec:
    datasets:
      - name: ${{records}}
        address: ${dataos://icebase:flash/records}}

      - name: ${{f_sales}}
        depot: ${{dataos://bigquery}}
        sql: ${{SELECT * FROM sales_360.f_sales}}
        meta:
          bucket: ${{tmdcdemogcs}}
        refresh:
          expression: ${{"*/2 * * * *"}}
          sql: ${{SELECT MAX(invoice_dt_sk) FROM sales_360.f_sales}}
          where: ${{invoice_dt_sk > PREVIOUS_SQL_RUN_VALUE}}

      - name: ${{duplicate_sales}}
        depot: ${{dataos://bigquery}}
        sql: ${{SELECT * FROM sales_360.f_sales}}
        meta:
          bucket: ${{tmdcdemogcs}}
        refresh:
          expression: ${{"*/4 * * * *"}}
          sql: ${{SELECT MAX(invoice_dt_sk) FROM sales_360.f_sales}}
          where: ${{invoice_dt_sk > CURRENT_SQL_RUN_VALUE}}


    init:
      - ${{create table f_sales as (select * from records)}}

    schedule:
      - expression: ${{"*/2 * * * *"}}
        sql: ${{INSERT INTO f_sales BY NAME (select * from records);}}
```

To know more about the Resource meta section, please [refer to this](https://dataos.info/resources/manifest_attributes/).

## Resource Specific Section

### **`service`**

**Description:** Configuration details specific to the service.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| object | mandatory | none | Contains various sub-attributes |

### **`servicePort`**

**Description:** The port on which the service will run.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| integer | mandatory | none | Any valid port number |

**Example Usage:**

```yaml
servicePort: 8080
```

### **`servicePorts`**

**Description:** A backup Service port. 

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| integer | optional | none | Any valid port number |

**Example Usage:**

```yaml
servicePorts:
  - name: backup
    servicePort: 5433
```

### **`ingress`**

**Description:** configuration for the service's ingress. Ingress exposes HTTP and HTTPS routes from outside DataOS to services within DataOS. Configure the incoming port for the service to allow access to DataOS resources from external links.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| --- | --- | --- | --- |
| mapping | optional | none | none |

**Example Usage:**

``` yaml
service:
  ingress: 
      enabled: true
      noAuthentication: true
      path: /flash/public:flash-test 
      stripPath: true
```

You can access the ingress path on [Metis](/interfaces/metis/), as shown below.

<center>
  <img src="/resources/stacks/flash/annotely_image%20(30).png" alt="Metis" style="width:40rem; border: 1px solid black; padding: 5px;" />
  <figcaption><i>Metis Interface</i></figcaption>
</center>



### **`enabled`**
**Description:** indicates whether ingress is enabled for the service.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| --- | --- | --- | --- |
| boolean | optional | false | true/false |

**Example Usage:**

``` yaml
service:
  ingress:
    enabled: true
```


### **`path`**
**Description:** the path for the Service's ingress configuration. If a Service by the same path already exists, it would get replaced.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| --- | --- | --- | --- |
| string | optional | none | any valid path |

**Example Usage:**

``` yaml
service:
  ingress:
    path: /flash/public:flash-test 
```

### **`stripPath`**

**Description:** indicates whether to strip the path from incoming requests in the ingress configuration.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| --- | --- | --- | --- |
| boolean | optional | false | true/false |

**Example Usage:**

``` yaml
service:
  ingress:
    stripPath: true
```


### **`noAuthentication`**

**Description:** indicates whether authentication is disabled for the ingress configuration.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| --- | --- | --- | --- |
| boolean | optional | true | true or false. |




### **`replicas`**

**Description:** The number of replicas for the service.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| integer | mandatory | none | Any positive integer |

**Example Usage:**

```yaml
replicas: 1
```

### **`logLevel`**

**Description:** The level of logging detail for the service.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| string | mandatory | none | DEBUG, INFO, WARN, ERROR |

**Example Usage:**

```yaml
logLevel: info
```

### **`compute`**

**Description:** Specifies the compute environment or type.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| string | mandatory | none | Any valid compute environment |

**Example Usage:**

```yaml
compute: runnable-default
```

### **`envs`**

**Description:** environment variables for the service.

| **Data Type** | **Requirement** | **Default Value** | **Possible Value** |
| --- | --- | --- | --- |
| mapping | optional | none | key-value configurations |

**Example Usage:**

``` yaml
envs:
  APP_BASE_PATH: 'dataos-basepath'
  FLASH_BASE_PATH: /flash/public:flash-test
```

### **`resources`**

**Description:** Resource allocation details for the service.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| object | mandatory | none | Contains `requests` sub-attribute |

**Example Usage:**

```yaml
resources:
  requests:
    cpu: 1000m
    memory: 1024Mi
```

### **`requests`**

**Description:** Specifies the minimum resources required for the service.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| object | mandatory | none | Contains `cpu` and `memory` sub-attributes |

**Example Usage:**

```yaml
requests:
  cpu: 1000m
  memory: 1024Mi
```

### **`cpu`**

**Description:** The amount of CPU resources requested.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| string | mandatory | none | Any valid CPU resource specification (e.g., `1000m`) |

**Example Usage:**

```yaml
cpu: 1000m
```

### **`memory`**

**Description:** The amount of memory resources requested.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| string | mandatory | none | Any valid memory resource specification (e.g., `1024Mi`) |

**Example Usage:**

```yaml
memory: 1024Mi
```

### **`stack`**

**Description:** Specifies the stack or runtime environment for the service.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| string | mandatory | none | Any valid stack or runtime specification |

**Example Usage:**

```yaml
stack: flash+python:1.0
```

## Stack Specific Section

### **`stackSpec`**

**Description:** Specification details for the stack used by the service.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| object | mandatory | none | Contains `datasets`, `init`, and `schedule` sub-attributes |

**Example Usage:**

```yaml
  stackSpec: # mandatory
    summarise: true
    datasets: # mandatory
      - address: dataos://icebase:retail/customer # mandatory
        name: customer # mandatory
```

### **`summarise`**

**Description:** Showcases a summary of all the datasets being cached inside Flash.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| boolean | optional | false | `true`, `false` |

**Example Usage:**

```yaml
stackSpec:
  summarise: true
  datasets:
    - address: dataos://icebase:retail/customer
      name: customer
```

### **`datasets`**

**Description:** List of mappings each specifying the name and address of the specific dataset.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| array of objects | mandatory | none | Contains `address` and `name` sub-attributes |

**Example Usage:**

```yaml
datasets: # mandatory
  - address: dataos://icebase:retail/customer # mandatory
    name: customer # mandatory
```

### **`address`**

**Description:** The address of the dataset.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| string | mandatory | none | Any valid dataset address |

**Example Usage:**

```yaml
- address: dataos://icebase:retail/customer
```

### **`name`**

**Description:** The name of the dataset.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| string | mandatory | none | Any valid dataset name |

**Example Usage:**

```yaml
name: customer
```

### **`init`**

**Description:** Initialization commands or SQL statements to run on service start.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| array of strings | optional | none | Any valid SQL or command strings |

<aside class="callout">
🗣 **Best Practice:** Create views instead of tables while caching datasets. It uses less infrastructure resources - CPU and memory. Also, the View or table name should not be the same as the dataset address name. For example: creating view sales as (select * from sales) is not allowed.

</aside>

**Example Usage:**

```yaml
init:
  - create table mycustomer as (select * from customer)
```

### **`schedule`**

**Description:** Scheduling details for periodic tasks.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| array of objects | optional | none | Contains `expression` and `sql` sub-attributes |

**Example Usage:**

```yaml
schedule:
  - expression: "*/2 * * * *"
    sql: INSERT INTO mycustomer BY NAME (select * from customer);
```

### **`expression`**

**Description:** The cron expression for scheduling tasks.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| string | mandatory | none | Any valid cron expression |

**Example Usage:**

```yaml
expression: "*/2 * * * *"
```

### **`sql`**

**Description:** The SQL command executes on schedule.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| string | mandatory | none | Any valid SQL statement |

**Example Usage:**

```yaml
sql: INSERT INTO mycustomer BY NAME (select * from customer);
```