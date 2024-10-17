# Attributes of Flash Service Manifest File

This section provides detailed descriptions of the attributes within the Flash Service manifest file, assisting in understanding the configuration required for effective Flash Service deployment.

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

## Resource-specific section

Click [here](/resources/manifest_attributes/) to know Resource meta section configuration.

## Service-specific section

### **`service`**

**Description:** Configuration details specific to the service.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| mapping | mandatory | none | Contains various sub-attributes |

---

### **`servicePort`**

**Description:** Specifies the port on which the service will run.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| integer | mandatory | none | Any valid port number |

**Example Usage:**

```yaml
servicePort: 8080
```

---


### **`servicePorts`**

**Description:** A list of additional service ports, such as a backup service port.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| list | optional | none | A list of valid port numbers |

**Example Usage:**

```yaml
servicePorts:
  - name: backup
    servicePort: 5433
```

---

### **`ingress`**

**Description:** Configuration for exposing the service to external HTTP/HTTPS routes. This attribute specifies how external access is handled.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| mapping | optional | none | none |

**Example Usage:**

```yaml
service:
  ingress: 
      enabled: true
      noAuthentication: true
      path: /flash/public:flash-test 
      stripPath: true
```

---

### **`replicas`**

**Description:** Defines the number of service replicas to deploy.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| integer | mandatory | none | Any positive integer |

**Example Usage:**

```yaml
replicas: 1
```

---

### **`logLevel`**

**Description:** The level of logging details captured for the service.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| string | mandatory | none | DEBUG, INFO, WARN, ERROR |

**Example Usage:**

```yaml
logLevel: info
```

---

### **`compute`**

**Description:** Specifies the compute environment or type for the service.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| string | mandatory | none | Valid compute environment identifier |

**Example Usage:**

```yaml
compute: runnable-default
```

---

### **`envs`**

**Description:** Defines environment variables for the service.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| mapping | optional | none | Key-value pairs representing environment variables |

**Example Usage:**

```yaml
envs:
  APP_BASE_PATH: 'dataos-basepath'
  FLASH_BASE_PATH: /flash/public:flash-test
```
---

### **`resources`**

**Description:** Specifies resource allocation, including CPU and memory for the service.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| mapping | mandatory | none | Contains `requests` and `limits` sub-attributes |

**Example Usage:**

```yaml
resources:
  requests:
    cpu: 500m
    memory: 512Mi
  limits:
    cpu: 1000m
    memory: 1024Mi
```

---

### **`requests`**

**Description:** Defines the minimum CPU and memory resources requested for the service.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| mapping | mandatory | none | Contains `cpu` and `memory` sub-attributes |

**Example Usage:**

```yaml
requests:
  cpu: 500m
  memory: 512Mi
```

---

### **`limits`**

**Description:** Defines the maximum CPU and memory resources that the service is allowed to use.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| mapping | mandatory | none | Contains `cpu` and `memory` sub-attributes |

**Example Usage:**

```yaml
limits:
  cpu: 1000m
  memory: 1024Mi
```

---

### **`stack`**

**Description:** Specifies the stack (runtime environment) to be used by the service.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| string | mandatory | none | Stack version and type identifier |

**Example Usage:**

```yaml
stack: flash+python:2.0
```

---

## Flash Stack-specific Section

### **`stackSpec`**

**Description:** Defines stack-specific configurations, such as datasets, initialization SQL, and scheduling for data refresh.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| mapping | mandatory | none | Contains `datasets`, `init`, and `schedule` sub-attributes |

**Example Usage:**

```yaml
stackSpec:
  datasets:
    - name: records
      address: dataos://icebase:flash/records
```

---

### **`datasets`**

**Description:** A list specifying the datasets to be cached by the Flash Service.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| list | mandatory | none | Contains `address` and `name` sub-attributes |

**Example Usage:**

```yaml
datasets:
  - name: records
    address: dataos://icebase:flash/records
```

---

### **`init`**

**Description:** Initialization SQL commands to be executed when the service starts.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| list of strings | optional | none | SQL commands for initialization |

**Example Usage:**

```yaml
init:
  - create table f_sales as (select * from records)
```

---

### **`schedule`**

**Description:** Defines periodic tasks using cron expressions for scheduling queries.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| list | optional | none | Contains `expression` and `sql` sub-attributes |

**Example Usage:**

```yaml
schedule:
  - expression: "*/2 * * * *"
    sql: INSERT INTO f_sales BY NAME (select

 * from records);
```

---

### **`expression`**

**Description:** Cron expression for scheduling periodic queries.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| string | mandatory | none | Valid cron expression |

**Example Usage:**

```yaml
expression: "*/2 * * * *"
```

---

### **`sql`**

**Description:** SQL query that executes according to the specified cron schedule.

| **Data Type** | **Requirement** | **Default Value** | **Possible Values** |
| --- | --- | --- | --- |
| string | mandatory | none | Any valid SQL command |

**Example Usage:**

```yaml
sql: INSERT INTO f_sales BY NAME (select * from records);
```