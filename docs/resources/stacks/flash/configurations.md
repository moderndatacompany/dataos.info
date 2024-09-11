This section involves details of each attribute to help you better understand the Flash Service configurations.

```yaml
# resource meta section
name: ${{flash-service}} # mandatory
version: v1 # mandatory
type: service # mandatory
tags: # optional
  - service
description: Flash service # optional
workspace: public # optional
# resource specific section
service: # mandatory
  servicePort: 5433
  replicas: 1
  logLevel: info
  compute: runnable-default
  resources:
    requests:
      cpu: 1000m
      memory: 1024Mi
  stack: flash+python:1.0
  stackSpec: # mandatory
    summarise: true
    datasets: # mandatory
      - address: dataos://icebase:retail/customer # mandatory
        name: customer # mandatory
    init:
      - create table mycustomer as (select * from customer)
    schedule:
      - expression: "*/2 * * * *"
        sql: INSERT INTO mycustomer BY NAME (select * from customer);
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
servicePort: 5433
```

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