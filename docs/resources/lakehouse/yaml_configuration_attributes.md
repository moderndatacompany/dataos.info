# Attributes of Lakehouse YAML

## `lakehouse`

**Description:** The `lakehouse` attribute serves as a mapping that comprises attributes and parameters specific to the Lakehouse Resource.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | mandatory | none | none |

**Example Usage:**

```yaml
lakehouse:
  type: ABFSS
  compute: runnable-default
  # Additional lakehouse-specific attributes...
```

---

### **`type`**

**Description:** The `type` attribute under `lakehouse` specifies the type of storage used by the Lakehouse, such as ABFSS, GCS, or S3.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | ABFSS, GCS, S3 |

**Example Usage:**

```yaml
lakehouse:
  type: ABFSS
  # Other lakehouse attributes...
```

---

### **`compute`**

**Description:** The `compute` attribute under `lakehouse` defines the Compute Resource or environment that the Lakehouse will utilize.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | Any valid Compute Resource name |

**Example Usage:**

```yaml
lakehouse:
  compute: runnable-default
  # Other lakehouse attributes...
```

---

### **`runAsApiKey`**

**Description:** the `runAsApiKey` attribute allows a user to assume the identity of another user through the provision of the latter's API key.

**Additional Details**: The apikey can be obtained by executing the following command from the CLI:

```bash
dataos-ctl user apikey get
```

In case no apikey is available, the below command can be run to create a new apikey

```bash
dataos-ctl user apikey create -n {{name of the apikey}} -d {{duration for the apikey to live}}
```

**Example Usage:**

```yaml
lakehouse:
  runAsApiKey: abcdefghijklmnopqrstuvwxyz
  # Other lakehouse configurations...
```

---

### **`runAsUser`**

**Description:** When the `runAsUser` attribute is configured with the UserID of the use-case assignee, it grants the authority to perform operations on behalf of that user.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | user-id of the user | user-id of the use-case assignee |

```yaml
lakehouse:
  runAsUser: iamgroot
  # Other lakehouse configurations...
```

---

### **`iceberg`**

**Description:** The `iceberg` attribute within `lakehouse` specifies attributes related to Apache Iceberg configuration which is a high-performance table format for huge analytic datasets.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | optional | none | Iceberg-specific attributes |

**Example Usage:**

```yaml
lakehouse:
  # ...other lakehouse attribute
  iceberg:
    storage:
      depotName: depot name
      type: abfss
      # ...other storage attributes
```

---

### **`storage`**

**Description:** The `storage` attribute within `iceberg` defines the storage configurations for the Iceberg tables, including details about the depot name and object store type.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | mandatory | none | Storage configuration settings |

**Example Usage:**

```yaml
lakehouse:
  iceberg:
    storage:
      depotName: depot name
      type: abfss
      # ...other storage attributes
```

---

### **`depotName`**

**Description:** The `depotName` attribute specifies the name of the Depot used in the Iceberg configuration.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | Any valid depot name |

**Example Usage:**

```yaml
lakehouse:
  iceberg:
    storage:
      depotName: depot name
      # ...other storage configurations
```

---

### **`type`**

**Description:** The `type` attribute under `storage` in `iceberg` designates the type of the object store used, such as ABFSS, GCS, WASBS, or S3.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | abfss, gcs, wasbs, s3 |

**Example Usage:**

```yaml
lakehouse:
  iceberg:
    storage:
      type: abfss
      # ...other storage configurations

```

---

### **`[abfss/gcs/wasbs/s3]`**

**Description:** This attribute represents the specific configuration for the chosen object store type under `storage` in `iceberg`. It includes unique attributes for each storage type like ABFSS, GCS, WASBS, or S3.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | optional | none | Specific depot configuration |

**Example Usage:**

```yaml
lakehouse:
  iceberg:
    storage:
      abfss:
        # Specific ABFSS configuration
      # ...other storage configurations
```

---

### **`secret`**

**Description:** The `secret` attribute under `storage` in `iceberg` is used for referencing pre-defined Secrets or Instance-secrets. This includes secret `name`, `workspace` identifiers, `keys`, and other secret-related configurations.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of mappings | optional | none | Secret configuration settings |

**Example Usage:**

```yaml
lakehouse:
  iceberg:
    storage:
      secret:
        - name: mysecret
          workspace: public
          key: username
          # ...other secret referencing attributes
```

---

### **`metastore`**

**Description:** The `metastore` attribute within `iceberg` defines the configuration for the metastore used by the Iceberg tables. This includes metastore `type`, `replicas`, `autoscaling` settings, and `resource` specifications.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | optional | none | Metastore configuration settings |

**Example Usage:**

```yaml
lakehouse:
  iceberg:
    metastore:
      type: iceberg-rest-catlog
      replicas: 2
      # ...other metastore attributes
```

---

### **`type`**

**Description:** The `type` attribute under `metastore` in `iceberg` specifies the type of metastore being used, such as `iceberg-rest-catlog`.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | Specific metastore type |

**Example Usage:**

```yaml
lakehouse:
  iceberg:
    metastore:
      type: iceberg-rest-catlog
      # ...other metastore attributes
```

---

### **`replicas`**

**Description:** The `replicas` attribute under `metastore` in `iceberg` defines the number of replicas for the metastore service.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| integer | optional | none | Any valid integer |

**Example Usage:**

```yaml
lakehouse:
  iceberg:
    metastore:
      replicas: 2
      # ...other metastore attributes
```

---

### **`autoScaling`**

**Description:** The `autoScaling` attribute under `metastore` in `iceberg` configures the autoscaling properties of the metastore service, including the enabling status, minimum and maximum number of replicas, and target utilization percentages.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | optional | none | Autoscaling configuration settings |

**Example Usage:**

```yaml
lakehouse:
  iceberg:
    metastore:
      autoScaling:
        enabled: true
        minReplicas: 2
        maxReplicas: 4
        # ...other autoscaling attributes
```

---

### **`resources`**

**Description:** The `resources` attribute under `metastore` in `iceberg` provides the configuration for CPU and memory resources allocated to the metastore. It includes settings for both requests and limits of these resources.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | optional | none | CPU and memory resource configurations |

**Example Usage:**

```yaml
lakehouse:
  iceberg:
    metastore:
      resources:
        requests:
          cpu: 1Gi
          memory: 400m
        limits:
          cpu: 1Gi
          memory: 400m

```

---

### **`queryEngine`**

**Description:** The `queryEngine` attribute within `iceberg` specifies the configuration for the query engine associated with the Lakehouse, defining its type and resource allocations.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | optional | none | Query engine configuration settings |

**Example Usage:**

```yaml
lakehouse:
  iceberg:
    queryEngine:
      type: themis
      resources:
        requests:
          cpu: 1Gi
          memory: 400m
        # ...other query engine attributes
```

---

### **`type`**

**Description:** The `type` attribute under `queryEngine` in `iceberg` determines the type of query engine used. Currently it supports two query engines `themis` and `minerva`.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | Specific query engine type |

**Example Usage:**

```yaml
lakehouse:
  iceberg:
    queryEngine:
      type: themis
      # ...other query engine attributes
```

---

### **`resources`**

**Description:** The `resources` attribute under `queryEngine` in `iceberg` configures the CPU and memory resources allocated to the query engine. It includes specifications for both requests and limits.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | optional | none | CPU and memory resource configurations |

**Example Usage:**

```yaml
lakehouse:
  iceberg:
    queryEngine:
      resources:
        requests:
          cpu: 1Gi
          memory: 400m
        limits:
          cpu: 1Gi
          memory: 400m
```

---

### **`[themis/minerva]`**

**Description:** This attribute represents specific configurations for the chosen query engine type under `queryEngine` in `iceberg`, such as `themis` or `minerva`.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | optional | none | Specific query engine configuration |

**Example Usage:**

```yaml
lakehouse:
  iceberg:
    queryEngine:
      themis/minerva:
        # Specific Themis/Minerva configuration
      # ...other query engine configurations

```

---

### **`themis`**

**Description:** The `themis` attribute under `queryEngine` in `iceberg` provides specific configuration settings for the Themis query engine. It includes various Themis-specific attributes that customize its performance and behavior.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | optional | none | Themis-specific attributes |

**Example Usage:**

```yaml
lakehouse:
  iceberg:
    queryEngine:
      themis:
        # Specific Themis configuration parameters
```

---

### **`minerva`**

**Description:** The `minerva` attribute under `queryEngine` in `iceberg` is used for setting up specific configurations for the Minerva query engine. This includes a range of attributes tailored to optimize the Minerva engine's functionality.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | optional | none | Minerva-specific configuration parameters |

**Example Usage:**

```yaml
lakehouse:
  iceberg:
    queryEngine:
      minerva:
        # Specific Minerva configuration parameters
```
