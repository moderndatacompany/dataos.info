# Attributes of Lakehouse manifest

## Structure of Lakehouse manifest

```yaml
lakehouse:
  type: ${lakehouse-type} 
  compute: ${compute-resource-name} 
  runAsApiKey: ${apikey}
  runAsUser: ${user-id}
  iceberg:
    storage: 
      depotName: ${depot-name} 
      type: ${storage-type} 
			# For gcs-type storage
			gcs:
				bucket: ${gcs-bucket-name}
				format: ${format}
				icebergCatalogType: ${iceberg-catalog-type}
				metastoreType: ${metastore-type}
				metastoreUrl: ${metastore-url}
				relativePath: ${relative-path}
			# For abfss-type storage
			abfss:
				account: ${abfss-account}
				container: ${container}
				endpointSuffix: ${endpoint-suffix}
				format: ${format}
				icebergCatalogType: ${iceberg-catalog-type}
				metastoreType: ${metastore-type}
				metastoreUrl: ${metastore-url}
				relativePath: ${relative-path}
			# For wasbs-type storage
			wasbs:
				account: ${wasbs-account}
				container: ${container}
				endpointSuffix: ${endpoint-suffix}
				format: ${format}
				icebergCatalogType: ${iceberg-catalog-type}
				metastoreType: ${metastore-type}
				metastoreUrl: ${metastore-url}
				relativePath: ${relative-path}
			# For s3-type storage
			s3:
				bucket: ${s3-bucket}
				format: ${format}
				icebergCatalogType: ${iceberg-catalog-type}
				metastoreType: ${metastore-type}
				metastoreUrl: ${metastore-url}
				relativePath: ${relative-path}
				scheme: ${scheme}
			# Instance-secret reference
			secrets:
				- name: ${secret-name} 
					workspace: ${workspace-name} # (for instance-secret workspace is not applicable)
					key: ${secret-key-name}
					keys:
						- ${key1}
						- ${key2}
					allKeys: ${include-allkeys-or-not}
					consumptionType: ${secret-consumption-type}
    metastore:
      type: ${metastore-type} 
      replicas: ${number-of-replicas}
      autoScaling:
        enabled: ${enable-autoscaling}
        minReplicas: ${minimum-number-of-replicas}
        maxReplicas: ${maximum-number-of-replicas}
        targetMemoryUtilizationPercentage: ${target-memory-utilization-percentage}
        targetCPUUtilizationPercentage: ${target-cpu-utilization-percentage}
      resources:
        requests:
          cpu: ${requested-cpu-resource}
          memory: ${requested-memory-resource}
        limits:
          cpu: ${requested-cpu-resource}
          memory: ${requested-memory-resource}
    queryEngine:
      type: ${query-engine-type}
      resources:
        requests:
          cpu: ${requested-cpu-resource}
          memory: ${requested-memory-resource}
        limits:
          cpu: ${requested-cpu-resource}
          memory: ${requested-memory-resource}
      themis:
        envs:
          ${environment-variables}
        themisConf:
          ${themis-configuration}
        spark:
          driver: 
            resources:
              requests:
                cpu: ${requested-cpu-resource}
                memory: ${requested-memory-resource}
              limits:
                cpu: ${requested-cpu-resource}
                memory: ${requested-memory-resource}
            instanceCount: ${instance-count} 
            maxInstanceCount: ${max-instance-count} 
          executor:
            resources:
              requests:
                cpu: ${requested-cpu-resource}
                memory: ${requested-memory-resource}
              limits:
                cpu: ${requested-cpu-resource}
                memory: ${requested-memory-resource}
            instanceCount: ${instance-count}
            maxInstanceCount: ${max-instance-count} 
          sparkConf:
            ${spark-configuration}
      storageAcl: ${storage-acl} 
```

## Configuration

### **`lakehouse`**

**Description:** The `lakehouse` attribute is a YAML mapping that comprises attributes for configuring a Lakehouse in DataOS, including its type, compute resources, Iceberg configurations, etc.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | mandatory | none | none |

**Example Usage:**

```yaml
lakehouse:
  type: iceberg
  compute: query-default
  # Additional Lakehouse-specific attributes...
```

---

### **`type`**

**Description:** The `type` attribute under `lakehouse` specifies the type of Lakehouse.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | iceberg |

**Example Usage:**

```yaml
lakehouse:
	type: iceberg
	# Additional Lakehouse-specific attributes
```

---

### **`compute`**

**Description:** Defines the [Compute Resource](/resources/compute/) to be used by the Lakehouse.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | valid Compute Resource name, e.g. query-default |

**Example Usage:**

```yaml
lakehouse:
	compute: query-default
	# Additional Lakehouse-specific attributes
```

---

### **`runAsApiKey`**

**Description:** The `runAsApiKey` attribute allows a user to assume the identity of another user by providing the latter's API key.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | apikey of the owner applying the Resource | apikey of the use-case assignee |

**Additional Details**: The apikey can be obtained by executing the following command from the CLI:

```shell
dataos-ctl user apikey get
```

In case no apikey is available, the below command can be run to create a new apikey:

```shell
dataos-ctl user apikey create -n ${name-of-the-apikey} -d ${duration-for-the-apikey-to-live}
```

This sample command below creates a new API key named `myapikey` that will remain valid for 30 days.

```shell
dataos-ctl user apikey create -n myapikey -d 30d
```

**Example Usage:**

```yaml
lakehouse:
  runAsApiKey: abcdefghijklmnopqrstuvwxyz
  # Additional Lakehouse-specific attributes...
```

---

### **`runAsUser`**

**Description:** When the `runAsUser` attribute is configured with the UserID of the use-case assignee, it grants the authority to perform operations on behalf of that user.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | user-id of the owner applying the Resource | user-id of the use-case assignee |

```yaml
lakehouse:
  runAsUser: iamgroot
  # Additional Lakehouse-specific attributes...
```

---

### **`iceberg`**

**Description:** The `iceberg` attribute contains configurations for Lakehouse built on the Iceberg table format, including storage settings, metastore, and query engine configurations.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | mandatory | none | valid Iceberg Lakehouse-specific attributes |

**Example Usage:**

```yaml
lakehouse:
	iceberg:
		storage:
			depotName: icebasedev
			type: ABFSS
			# additional Storage section attributes
		metastore:
			# additional Metastore section attributes
		queryEngine:
			# additional Query Engine section attributes
	# Additional Lakehouse-specific attributes
```

---

### **`storage`**

**Description:** The `storage` attribute within the `iceberg` defines the storage configurations for the Lakehouse to connect to the underlying cloud storage solution (such as ABFSS, WASBS, Amazon S3, or GCS), and also the references for the Instance-secrets.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | mandatory | none | none |

**Example Usage:**

```yaml
lakehouse:
	iceberg:
		storage:
			depotName: icebasedev
			type: ABFSS
			# other Storage section attributes
```

---

#### **`depotName`**

**Description:** Specifies the name for the Depot associated with the Lakehouse Resource instance. If `depotName` is not provided within the Storage section of the configuration, DataOS generates a default name. This default is formed by concatenating the Lakehouse Resource name, the Workspace name, and the suffix `storage`, separated by `0`. For example, for a Lakehouse Resource named `newlakehouse` in the `sandbox` Workspace without a specified `depotName`, the generated Depot name would be `newlakehouse0sandbox0storage`.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | ${lakehouse-name}0${workspace}0storage | A valid string that matches the regex pattern `[a-z]([a-z0-9]*)`. Special characters, except for hyphens/dashes, are not allowed. The maximum length is 48 characters. |

**Example Usage:**

```yaml
lakehouse:
  iceberg:
    storage:
      depotName: icebasestage
      # Additional attributes for the Storage section
```

---

#### **`type`**

**Description:** Specifies the type of cloud storage Depot associated with the Lakehouse Resource instance. The type attribute determines what configuration would need to be declared for the storage connection

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | abfss, gcs, s3, wasbs |

**Example Usage:**

```yaml
lakehouse:
  iceberg:
    storage:
      type: abfss
      # Additional attributes for the Storage section
```


#### **abfss**

**Description:** Specifies the configuration for the `abfss` source-type.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | valid abfss configuration |

**Additional details:** The code block given below provides the sub-attributes for ABFSS data source:

```yaml
abfss: 
  account: ${abfss-account} # optional
  container: ${container} # optional
  endpointSuffix: ${endpoint-suffix}
  format: ${format} # optional
  icebergCatalogType: ${iceberg-catalog-type} # optional
  metastoreType: ${metastore-type} # optional
  metastoreUrl: ${metastore-url} # optional
  relativePath: ${relative-path} # optional
```

**Attribute Definitions:**

- **account:** The name of the abfss storage account.
- **container:** The container for the abfss storage account.
- **endpointSuffix:** The endpoint suffix of the ABFSS account.
- **format:** Specifies the data format for storage. Common formats include PARQUET, AVRO, ORC, and ICEBERG.
- **icebergCatalogType:** Defines the catalog type when using Apache Iceberg. Examples include HIVE or HADOOP.
- **metastoreType:** Indicates the metastore's type. For example, hive or hadoop.
- **metastoreUrl:** Provides the URL to the metastore. 
- **relativePath:** Specifies a folder path within the bucket where data is stored or accessed, allowing for structured data organization within a single bucket.


**Example Usage:**

```yaml
lakehouse:
  iceberg:
    storage:
      type: abfss
      abfss:
        depotName: abfsslakehouse
        account: abfssstorage
        container: lake01
        relativePath: "/dataos"
        format: ICEBERG
        endpointSuffix: dfs.core.windows.net
      # Additional attributes for the Storage section
```

#### **gcs**

**Description:** Specifies the type of cloud storage Depot associated with the Lakehouse Resource instance. The type attribute determines what configuration would need to be declared for the storage connection

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | abfss, gcs, s3, wasbs |

**Additional details:** The code block given below provides the attributes of details of sub-attributes provided for GCS configuration are as follows:

```yaml
gcs: # mandatory
  bucket: ${gcs-bucket} # mandatory
  format: ${format} # mandatory
  icebergCatalogType: ${iceberg-catalog-type} # optional
  metastoreType: ${metastore-type} # optional
  metastoreUrl: ${metastore-url} # optional
  relativePath: ${relative-path} # optional
```

**Attribute Definitions:**

- **bucket:** The name of the Google Cloud Storage bucket to be used. This is a mandatory attribute.
- **format:** Specifies the data format for storage. Common formats include PARQUET, AVRO, ORC, and ICEBERG.
- **icebergCatalogType:** Defines the catalog type when using Apache Iceberg. Examples include HIVE or HADOOP.
- **metastoreType:** Indicates the metastore's type. For example, HIVE or GLUE.
- **metastoreUrl:** Provides the URL to the metastore. This is essential for environments where the metastore is not co-located or is accessed over the network.
- **relativePath:** Specifies a folder path within the bucket where data is stored or accessed, allowing for structured data organization within a single bucket.


**Example Usage:**

```yaml
lakehouse:
  iceberg:
    storage:
      type: gcs
      gcs:
        bucket: dataos-testing
        relativePath: "/sanity"
        format: ICEBERG
      # Additional attributes for the Storage section
```

---

#### **s3**

**Description:** Specifies the configuration for the `s3` source-type.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | valid s3 configuration |

**Additional details:** The code block given below provides the sub-attributes for S3 data source:

```yaml
s3: # mandatory
  bucket: ${s3-bucket} # mandatory
  format: ${format} # mandatory
  icebergCatalogType: ${iceberg-catalog-type} # optional
  metastoreType: ${metastore-type} # optional
  metastoreUrl: ${metastore-url} # optional
  relativePath: ${relative-path} # optional
  scheme: ${scheme} # optional
```

**Attribute Definitions:**

- **bucket:** The name of the wasbs storage account.
- **format:** Specifies the data format for storage. Common formats include PARQUET, AVRO, ORC, and ICEBERG.
- **icebergCatalogType:** Defines the catalog type when using Apache Iceberg. Examples include HIVE or HADOOP.
- **metastoreType:** Indicates the metastore's type. For example, hive or hadoop.
- **metastoreUrl:** Provides the URL to the metastore. 
- **relativePath:** Specifies a folder path within the bucket where data is stored or accessed, allowing for structured data organization within a single bucket.
- **scheme:** Valid scheme (e.g., s3://)


**Example Usage:**

```yaml
lakehouse:
  iceberg:
    storage:
      type: s3
      s3:
        bucket: lake001-dev    
        relativePath: /sanitys3 
      # Additional attributes for the Storage section
```

---

#### **wasbs**

**Description:** Specifies the configuration for the `wasbs` source-type.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | valid wasbs configuration |

**Additional details:** The code block given below provides the sub-attributes for WASBS data source:

```yaml
wasbs: 
  account: ${wasbs-account} # optional
  container: ${container} # optional
  endpointSuffix: ${endpoint-suffix}
  format: ${format} # optional
  icebergCatalogType: ${iceberg-catalog-type} # optional
  metastoreType: ${metastore-type} # optional
  metastoreUrl: ${metastore-url} # optional
  relativePath: ${relative-path} # optional
```

**Attribute Definitions:**

- **account:** The name of the wasbs storage account.
- **container:** The container for the wasbs storage account.
- **endpointSuffix:** The endpoint suffix of the WASBS account.
- **format:** Specifies the data format for storage. Common formats include PARQUET, AVRO, ORC, and ICEBERG.
- **icebergCatalogType:** Defines the catalog type when using Apache Iceberg. Examples include HIVE or HADOOP.
- **metastoreType:** Indicates the metastore's type. For example, hive or hadoop.
- **metastoreUrl:** Provides the URL to the metastore. 
- **relativePath:** Specifies a folder path within the bucket where data is stored or accessed, allowing for structured data organization within a single bucket.


**Example Usage:**

```yaml
lakehouse:
  iceberg:
    storage:
      type: wasbs
      wasbs:
        depotName: wasbslakehouse
        account: wasbsstorage
        container: lake01
        relativePath: "/dataos"
        format: ICEBERG
        endpointSuffix: dfs.core.windows.net
      # Additional attributes for the Storage section
```

---

#### **`secret`**

**Description:** The `secret` attribute under `storage` in `iceberg` is used for referencing pre-defined Instance-secrets. This includes secret `name`, `workspace` identifiers, `keys`, and other secret-related configurations. Instance-secrets are securely managed secret stored within the Heimdall vault.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of mappings | optional | none | Secret configuration settings |

**Example Usage:**

```yaml
lakehouse:
  iceberg:
    storage:
      secret:
        - name: random        # mandatory
          workspace: delta    # mandatory
          key: hola
          keys:
            - list
            - hola
          allKeys: false
          consumptionType: envVars
```

**Sub-Attributes:**

- **`name`**: Name of the secret.
- **`workspace`**: Workspace where the secret is located (not applicable for instance-secrets).
- **`key`, `keys`**: Specific key(s) within the secret.
- **`allKeys`**: Whether all keys within the secret are to be used.
- **`consumptionType`**: How the secret is consumed (envVars, propFile, file).

---

### **`metastore`**

**Description:** The `metastore` attribute within `iceberg` defines the configuration for the metastore used by the Iceberg tables. This includes metastore `type`, `replicas`, `autoscaling` settings, and `resource` specifications.

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
      # ...other metastore attributes`
```

---

#### **`type`**

**Description:** The `type` attribute under `metastore` in `iceberg` specifies the type of metastore being used, such as `iceberg-rest-catlog`.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | iceberg-rest-catalog |

**Example Usage:**

```yaml
lakehouse:
  iceberg:
    metastore:
      type: iceberg-rest-catalog
      # ...other metastore attributes`
```

---

#### **`replicas`**

**Description:** The `replicas` attribute under `metastore` in `iceberg` defines the number of replicas for the metastore service.

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

#### **`autoScaling`**

**Description:** The `autoScaling` attribute under `metastore` in `iceberg` configures the autoscaling properties of the metastore service, including the enabling status, minimum and maximum number of replicas, and target utilization percentages.

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
        # ...other autoscaling attributes`
```

**Sub-attributes:**

Sub-attributes of `autoScaling` can be found on this [link](/resources/service/configurations/#autoscaling).

---

#### **`resources`**

**Description:** The `resources` attribute under `metastore` in `iceberg` provides the configuration for CPU and memory resources allocated to the metastore. It includes settings for both requests and limits of these resources.

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
          memory: 400m`
```

**Sub-attributes:**

Sub-attributes of `resources` can be found on this [link](/resources/service/yaml_configuration_attributes/#resources).

---

### **`queryEngine`**

**Description:** The `queryEngine` attribute within `iceberg` specifies the configuration for the query engine associated with the Lakehouse, defining its type and resource allocations.

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
        # ...other query engine attributes`
```

---

#### **`type`**

**Description:** The `type` attribute under `queryEngine` in `iceberg` determines the type of query engine used. Currently it supports only one query engine `themis`.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | Specific query engine type |

**Example Usage:**

```yaml
lakehouse:
  iceberg:
    queryEngine:
      type: themis
      # ...other query engine attributes`
```

---

#### **`resources`**

**Description:** The `resources` attribute under `queryEngine` in `iceberg` configures the CPU and memory resources allocated to the query engine. It includes specifications for both requests and limits.

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
          memory: 400m`
```

**Sub-attributes:**

Sub-attributes of `themis` can be found on this [link](/resources/cluster/configurations/#resources).

---


#### **`themis`**

**Description:** The `themis` attribute under `queryEngine` in `iceberg` provides specific configuration settings for the Themis query engine. It includes various Themis-specific attributes that customize its performance and behavior.

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

**Sub-attributes:**

Sub-attributes of `themis` can be found on this [link](/resources/cluster/configurations/#themis).