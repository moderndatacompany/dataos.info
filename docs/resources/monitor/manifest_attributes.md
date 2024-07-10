# Attributes of Monitor YAML


```yaml
monitor:
  schedule: '*/2 * * * *'
  properties:
    alpha: beta
  timezone: ${{timezone}}
  incident: # mandatory
    incident_type: field_profiling
    asset: output_1
    column: column_2
    severity: critical
  type: equation_monitor # mandatory
  equation: 
    leftExpression:  # mandatory
      queryCoefficient: 1 # mandatory
      queryConstant: 0 # mandatory
      query: # mandatory
        type: prom # mandatory
        cluster: thanos # mandatory
        ql: certmanager_certificate_expiration_timestamp_seconds{container="cert-manager-controller", endpoint="9402", exported_namespace="caretaker", instance="10.212.4.9:9402", issuer_group="cert-manager.io", issuer_kind="ClusterIssuer", issuer_name="ca", job="cert-manager-ds", name="caretaker-api-cert", namespace="cert-manager", pod="cert-manager-ds-7d8cc489dd-d46sb", service="cert-manager-ds"} - time() # mandatory
    rightExpression: # mandatory
      queryCoefficient: 1 # mandatory
      queryConstant: 7766092 # mandatory
      query: # mandatory
        type: trino # mandatory
        cluster: themis # mandatory
        ql: SELECT metric_value FROM icebase.soda.soda_check_metrics_01 WHERE metric_name = 'missing_count' ORDER BY timestamp DESC LIMIT 1; # mandatory
      operator: equals # mandatory
  report: 
    source: # mandatory
      dataOSInstance:
        path: /collated/api/v1/reports/resources/runtime?id=workflow:v1:snowflakescannerdepotis:public # mandatory
  conditions: # mandatory
    - valueComparison:
        observationType: runtime # mandatory
        valueJqFilter: '.value' # mandatory
        operator: equals # mandatory
        value: running # mandatory
      durationComparison: 
        observationType: runtime # mandatory
        selectorJqFilter: # mandatory
        startedJqFilter: # mandatory
        completedJqFilter: # mandatory
        operator: # mandatory
        value: # mandatory
  runAsUser: iamgroot
```

## **`monitor`**

**Description:** Defines the monitoring configuration, including how frequently it runs, its specific properties, and the conditions under which incidents are reported.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | mandatory | none | none |

**Example Usage:**

```yaml
monitor:
  schedule: '4 18 2 * *'
  equation:
    left_expression:
      query_coefficient: 1
      query_constant: 0
      query:
        type: trino
        cluster: themis
        ql: SELECT metric_value FROM icebase.soda.soda_check_metrics_01 WHERE metric_name = 'missing_count' ORDER BY timestamp DESC LIMIT 1;
    right_expression:
      query_coefficient: 0
      query_constant: 0
    operator: equals
  incident:
    incident_type: field_profiling
    asset: output_1
    column: column_2
    severity: critical
```

---

### **`schedule`**

**Description:** A cron expression determining how often the Monitor is executed.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | valid cron expression |

**Example Usage:**

```yaml
monitor:
  schedule: '*/2 * * * *'
```

---

### **`properties`**

**Description:** Custom key-value pairs providing additional configuration for the Monitor.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | optional | none | any valid key-value pairs |

**Example Usage:**

```yaml
properties:
  alpha: beta
```

---

### **`timezone`**

**Description:** Specifies the timezone for the Monitor schedule.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | Timezone identifiers (e.g., `America/New_York`) |

**Example Usage:**

```yaml
monitor:
  timezone: America/New_York
```

---

### **`incident`**

**Description:** Configuration for incidents that should be raised by the Monitor.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | optional | none | valid key-value incident attributes |

**Additional details:** The below attributes provide a sample, you can add further more depending on your use case:
- **`incident_type`**: The category of the incident.
- **`asset`**: Identifies the asset involved in the incident.
- **`column`**: Specifies the data column related to the incident.
- **`severity`**: The urgency level of the incident.


**Example Usage:**

```yaml
monitor:
  incident:
    incident_type: field_profiling
    asset: output_1
    column: column_2
    severity: critical
```

---

### **`type`**

**Description:** The type of Monitor being configured, indicating the logic and methodology behind the monitoring process.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | equation_monitor, report_monitor, stream_monitor |

**Example Usage:**

```yaml
monitor: 
  type: equation_monitor
```

---

### **`equation`**

**Description:** Defines the mathematical equation used for monitoring, consisting of left and right expressions and an operator to evaluate them.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | optional | none | valid equation attributes |

**Example Usage:**

```yaml
monitor:
  equation:
    left_expression:
      query_coefficient: 1
      query_constant: 0
      query:
        type: trino
        cluster: themis
        ql: SELECT metric_value FROM icebase.soda.soda_check_metrics_01 WHERE metric_name = 'missing_count' ORDER BY timestamp DESC LIMIT 1;
    right_expression:
      query_coefficient: 0
      query_constant: 0
    operator: equals
```

---

#### **`leftExpression`**

**Description:** Specifies the left part of the equation, including its query, coefficient, and constant.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | mandatory | none | valid expression configuration |

**Example Usage:**

```yaml
monitor:
  equation:
    leftExpression:
      queryCoefficient: 1
      queryConstant: 0
      query:
        type: prom
        cluster: thanos
        ql: certmanager_certificate_expiration_timestamp_seconds{...} - time()
```

---

#### **`rightExpression`**

**Description:** Specifies the right part of the equation, which is structured similarly to `leftExpression` but may involve different queries or constants.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | mandatory | none | valid query configuration |

**Example Usage:**

```yaml
monitor:
  equation:
    rightExpression:
      queryCoefficient: 1
      queryConstant: 7766092
      query:
        type: trino
        cluster: themis
        ql: SELECT metric_value FROM icebase.soda.soda_check_metrics_01 WHERE metric_name = 'missing_count' ORDER BY timestamp DESC LIMIT 1;
```


---

##### **`queryCoefficient`**

**Description:** Multiplier for the query result.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| number | mandatory | none | any number |

**Example Usage:**

```yaml
monitor:
  equation:
    leftExpression:
      queryCoefficient: 1
```

---

##### **`queryConstant`**

**Description:** A constant value added to the query result.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| number | mandatory | none | any number |

**Example Usage:**

```yaml
monitor:
  equation:
    leftExpression:
      queryConstant: 0
```

---

##### **`query`**

**Description:** Defines the query details for the left and right expression.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | mandatory | none | valid query attributes |

**Example Usage:**

```yaml
monitor:
  equation:
    leftExpression:
      query:
        type: prom
        cluster: thanos
        ql: certmanager_certificate_expiration_timestamp_seconds{...} - time()
```

---

###### **`type`**

**Description:** The query source type.
| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | prom, trino |

**Example Usage:**

```yaml
monitor:
  equation:
    leftExpression:
      query:
        type: prom
```

---


###### **`cluster`**

**Description:** Specifies the Cluster where the query should be executed.
| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | thanos, minerva, themis  |

**Example Usage:**

```yaml
monitor:
  equation:
    leftExpression:
      query:
        cluster: thanos
```

---

###### **`ql`**

**Description:** The query language statement to be executed.
| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | valid query  |

**Example Usage:**

```yaml
monitor:
  equation:
    leftExpression:
      query:
        cluster: thanos
```

---

#### **`operator`**

**Description:** The operator used to compare the results of the `leftExpression` and `rightExpression`.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | equals, greater_than, less_than, not_equals, greater_than_equals, less_than_equals |

**Example Usage:**

```yaml
monitor:
  equation:
    operator: equals
```

---

### **`report`**

**Description:** Configures the report generation based on the Monitor, specifying data sources and conditions for the report.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | optional | none | none |

**Example Usage:**

```yaml
monitor:
  report:
    {}
```


#### **`source`**

**Description:** Defines the data source for generating the report.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | mandatory | none | none |

**Example Usage:**

```yaml
monitor:
  report: 
    source:
      dataOSInstance:
        path: /collated/api/v1/reports/resources/runtime?id=workflow:v1:snowflakescannerdepotis:public
```

---


#### **`dataOSInstance`**

**Description:** Specifies the DataOS instance paths from which to fetch report data.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | mandatory | none | none |

**Example Usage:**

```yaml
monitor:
  report: 
    source:
      dataOSInstance:
        path: /collated/api/v1/reports/resources/runtime?id=workflow:v1:snowflakescannerdepotis:public
```

###### **`path`**

**Description:** API path to the report resource.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | API endpoint paths |

**Example Usage:**

```yaml
monitor:
  report: 
    source:
      dataOSInstance:
        path: /collated/api/v1/reports/resources/runtime?id=workflow:v1:snowflakescannerdepotis:public
```

---

#### **`conditions`**

**Description:** Lists the conditions that trigger report generation, based on value and duration comparisons.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | mandatory | none | none |

**Example Usage:**

```yaml
monitor:
  report: 
    source:
      dataOSInstance:
        path: /collated/api/v1/reports/resources/runtime?id=workflow:v1:snowflakescannerdepotis:public
```

##### **`valueComparison`**

**Description:** Compares the value from the observation against a specified value.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | optional | none | valid sub-attributes |

**Sub-Attributes**

- **`observationType`**: The type of observation to compare.
- **`valueJqFilter`**: JQ filter to extract the value from the observation.
- **`operator`**: Comparison operator (e.g., `equals`, `greater_than`, `less_than`).
- **`value`**: The value to compare against.

**Example Usage:**

```yaml
monitor:
  report:
    conditions:
      - valueComparison:
          observationType: runtime
          valueJqFilter: '.value'
          operator: equals
          value: running
```

#### **`durationComparison`**

**Description:** Compares the duration of an event against a specified value.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | optional | none | valid sub-attributes |


**Sub-Attributes:**

- **`observationType`**: The type of observation for duration comparison.
- **`selectorJqFilter`**: JQ filter to select the relevant data for comparison.
- **`startedJqFilter`**: JQ filter to determine the start time of the event.
- **`completedJqFilter`**: JQ filter to determine the end time of the event.
- **`operator`**: Comparison operator for the duration.
- **`value`**: The duration value to compare against.

```yaml
monitor:
  report:
    conditions: # mandatory
      - durationComparison: 
          observationType: runtime # mandatory
          selectorJqFilter: ""# mandatory
          startedJqFilter: ""# mandatory
          completedJqFilter: ""# mandatory
          operator: ""# mandatory
          value: ""# mandatory

```



---

#### **`runAsUser`**

**Description:** Identifies the user under whose authority the report generation process executes.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | default user-id | user-id of use-case assignee |

**Example Usage:**

```yaml
monitor:
  runAsUser: iamgroot
```

---