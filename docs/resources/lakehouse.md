# Lakehouse

DataOS Lakehouse, is a [DataOS Resource](../resources.md) that integrates Apache Iceberg table format and cloud object storage to provide a fully managed storage solution. It emulates traditional data warehouses, enabling table creation with defined schemas, data manipulation via various tools, and data access regulation through [Heimdall](../architecture.md#heimdall).

<aside class="callout">

🗣️ Unlike traditional <a href="./depot/depot_config_templates.md">object storage or Data Lake depots</a> that are instantiated at the <a href="./types_of_dataos_resources.md#instance-level-resources">Instance-level</a>, Lakehouses are created at the <a href="./types_of_dataos_resources.md#workspace-level-resources">Workspace-level</a>.

</aside>


## Key Features of a Lakehouse

**Managed Storage**

DataOS Lakehouse offers a fully managed storage solution. It utilizes Apache Iceberg tables and cloud object storage, mimicking traditional warehouse functionalities.

**Computing Environment Flexibility**

Supports a multitude of computing environments for cloud-native storage. Users can deploy various compute engines, including DataOS native stacks such as [Flare](./stacks/flare.md), [Soda](./stacks/soda.md), etc.

**Apache Iceberg Integration**

Incorporates a hosted implementation of Apache Iceberg REST catalog, facilitating interaction with DataOS Lakehouse through Iceberg REST catalog API.

## How to create a Lakehouse?

### **Prerequisites**

Data developers can create a Lakehouse Resource by creating a YAML manifest and applying it via the DataOS [CLI](../interfaces/cli.md).

### **Create a YAML manifest for Lakehouse**

A Lakehouse YAML manifest can be structurally broken down into following sections:

- [Resource meta section](#configure-the-resource-meta-section)
- [Lakehouse-specific section](#configure-the-lakehouse-specific-section)
	- [Metastore configuration](#metastore-configuration)
	- [Storage configuration](#storage-configuration)
		- [GCS](#gcs)
		- [ABFSS](#abfss)
		- [WASBS](#wasbs)
		- [S3](#s3)
	- [Query Engine configuration](#query-engine-configuration)
		- [Themis](#themis)
		- [Minerva](#minerva)

#### **Configuring the Resource meta section**

In DataOS, a Lakehouse is categorized as a [Resource-type](https://dataos.info/resources/types_of_dataos_resources/). The Resource meta section within the YAML manifest encompasses attributes universally applicable to all Resource-types. The provided YAML codeblock elucidates the requisite attributes for this section: 

```yaml
# Resource meta section
name: {{my-lakehouse}} # Resource name (mandatory)
version: v1alpha # Manifest version (mandatory)
type: lakehouse # Resource-type (mandatory)
tags: # Resource Tags (optional)
  - {{dataos:type:resource}}
  - {{dataos:resource:lakehouse}}
description: {{This is a lakehouse yaml manifest}} # Resource Description (optional)
owner: {{iamgroot}} # Resource Owner (optional)
bundle: # Bundle-specific section mapping(mandatory)
  {{Attributes of Lakehouse-specific section}}
```
<center><i>Resource meta section</i></center>

For more information, refer to the [Attributes of Resource Meta Section.](../resources/resource_attributes.md)

#### **Configuring the Lakehouse-specific section**

```yaml
metastore: # Metastore section (optional)
	type: {{iceberg-rest-catlog}} # Metastore type (mandatory)
	replicas: {{2}} # Number of replicas (optional)
	autoScaling: # Autoscaling configuration (optional)
		enabled: {{true}} # Enable autoscaling (optional)
		minReplicas: {{2}} # Minimum number of replicas (optional)
		maxReplicas: {{4}} # Maximum number of replicas (optional)
		targetMemoryUtilizationPercentage: {{60}} # Target Memory Utilization Percentage (optional)
		targetCPUUtilizationPercentage: {{60}} # Target CPU Utilization Percentage (optional)
	resources: # CPU and memory resources (optional)
		requests: 
			cpu: {{1Gi}} # Requested CPU resources (optional)
			memory: {{400m}} # Requested Memory resources (optional)
		limits:
			cpu: {{1Gi}} # CPU resource limits (optional)
			memory: {{400m}} # Memory resource limits (optional)
```

<center>

| Attribute | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| [`lakehouse`](./lakehouse/yaml_configuration_attributes.md#lakehouse) | object | none | none | mandatory |
| [`type`](./lakehouse/yaml_configuration_attributes.md#type) | string | none | ABFSS, GCS, S3 | mandatory |
| [`compute`](./lakehouse/yaml_configuration_attributes.md#compute) | string | none | any valid string | mandatory |
| [`runAsApiKey`](./lakehouse/yaml_configuration_attributes.md#runasapikey) | string | none | any valid string | optional |
| [`runAsUser`](./lakehouse/yaml_configuration_attributes.md#runasuser) | string | none | any valid string | optional |
| [`iceberg`](./lakehouse/yaml_configuration_attributes.md#iceberg) | object | none | none | optional |
| [`storage`](./lakehouse/yaml_configuration_attributes.md#storage) | object | none | none | mandatory in `iceberg` |
| [`metastore`](./lakehouse/yaml_configuration_attributes.md#metastore) | object | none | none | optional in `iceberg` |
| [`queryEngine`](./lakehouse/yaml_configuration_attributes.md#queryengine) | object | none | none | optional in `iceberg` |

</center>

This table is designed to assist users in understanding and configuring the Lakehouse-specific section of a YAML file.


#### **Metastore configuration**

```yaml
metastore: # Metastore section (optional)
	type: {{iceberg-rest-catlog}} # Metastore type (mandatory)
	replicas: {{2}} # Number of replicas (optional)
	autoScaling: # Autoscaling configuration (optional)
		enabled: {{true}} # Enable autoscaling (optional)
		minReplicas: {{2}} # Minimum number of replicas (optional)
		maxReplicas: {{4}} # Maximum number of replicas (optional)
		targetMemoryUtilizationPercentage: {{60}} # Target Memory Utilization Percentage (optional)
		targetCPUUtilizationPercentage: {{60}} # Target CPU Utilization Percentage (optional)
	resources: # CPU and memory resources (optional)
		requests: 
			cpu: {{1Gi}} # Requested CPU resources (optional)
			memory: {{400m}} # Requested Memory resources (optional)
		limits:
			cpu: {{1Gi}} # CPU resource limits (optional)
			memory: {{400m}} # Memory resource limits (optional)
```


<center>

| Attribute | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| [`metastore`](./lakehouse/yaml_configuration_attributes.md#metastore) | object | none | none | optional |
| [`type`](./lakehouse/yaml_configuration_attributes.md#type) | string | none | iceberg-rest-catlog | mandatory |
| [`replicas`](./lakehouse/yaml_configuration_attributes.md#replicas) | integer | none | any valid integer | optional |
| [`autoScaling`](./lakehouse/yaml_configuration_attributes.md#autoscaling) | object | none | none | optional |
| [`enabled`](./lakehouse/yaml_configuration_attributes.md#enabled) | boolean | none | true/false | optional |
| [`minReplicas`](./lakehouse/yaml_configuration_attributes.md#minreplicas) | integer | none | any valid integer | optional |
| [`maxReplicas`](./lakehouse/yaml_configuration_attributes.md#maxreplicas) | integer | none | any valid integer | optional |
| [`targetMemoryUtilizationPercentage`](./lakehouse/yaml_configuration_attributes.md#targetmemoryutilizationpercentage) | integer | none | any valid percentage | optional |
| [`targetCPUUtilizationPercentage`](./lakehouse/yaml_configuration_attributes.md#targetcpuutilizationpercentage) | integer | none | any valid percentage | optional |
| [`resources`](./lakehouse/yaml_configuration_attributes.md#resources) | object | none | none | optional |
| [`requests`](./lakehouse/yaml_configuration_attributes.md#requests) | object | none | none | optional |
| [`cpu`](./lakehouse/yaml_configuration_attributes.md#cpu) | string | none | any valid resource amount | optional |
| [`memory`](./lakehouse/yaml_configuration_attributes.md#memory) | string | none | any valid resource amount | optional |
| [`limits`](./lakehouse/yaml_configuration_attributes.md#limits) | object | none | none | optional |
| [`cpu`](./lakehouse/yaml_configuration_attributes.md#cpu) | string | none | any valid resource amount | optional |
| [`memory`](./lakehouse/yaml_configuration_attributes.md#memory) | string | none | any valid resource amount | optional |

</center>

#### **Storage configuration**

```yaml
storage: 
	depotName: {{depot name}} # Name of depot (optional)
	type: {{abfss}} # Object store type (mandatory)
	abfss/gcs/wasbs/s3: # Depot type (optional)
		{{depot configuration}}
	secret: 
		- name: {{mysecret}} # Secret Name (mandatory)
			workspace: {{public}} # Workspace Name (optional)
			key: {{username}} # Key (optional)
			keys: # Keys (optional)
				- {{username}}
				- {{password}} 
			allKeys: true # All Keys (optional)
			consumptionType: {{envVars}} # Secret consumption type (optional)
```

<center>

| Attribute | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| [`storage`](./lakehouse/yaml_configuration_attributes.md#storage) | object | none | none | mandatory |
| [`depotName`](./lakehouse/yaml_configuration_attributes.md#depotname) | string | none | any valid string | optional |
| [`type`](./lakehouse/yaml_configuration_attributes.md#type) | string | none | abfss | mandatory |
| [`abfss/gcs/wasbs/s3`](./lakehouse/yaml_configuration_attributes.md#abfssgcswasbss3) | object | none | none | optional |
| [`depot configuration`](./lakehouse/yaml_configuration_attributes.md#depotconfiguration) | object | none | none | as per depot type |
| [`secret`](./lakehouse/yaml_configuration_attributes.md#secret) | object | none | none | mandatory |
| [`name`](./lakehouse/yaml_configuration_attributes.md#name) (under `secret`) | string | none | any valid string | mandatory |
| [`workspace`](./lakehouse/yaml_configuration_attributes.md#workspace) (under `secret`) | string | none | any valid string | optional |
| [`key`](./lakehouse/yaml_configuration_attributes.md#key) (under `secret`) | string | none | any valid string | optional |
| [`keys`](./lakehouse/yaml_configuration_attributes.md#keys) (under `secret`) | array | none | any valid strings | optional |
| [`allKeys`](./lakehouse/yaml_configuration_attributes.md#allkeys) (under `secret`) | boolean | none | true/false | optional |
| [`consumptionType`](./lakehouse/yaml_configuration_attributes.md#consumptiontype) (under `secret`) | string | none | envVars | optional |

</center>

##### **GCS**

```yaml
gcs:
	bucket: {{bucket-testing}} # GCS Bucket (optional)
	format: {{format}} # Format (optional)
	icebergCatalogType: {{hadoop}} # Iceberg Catalog Type (optional)
	metastoreType: {{iceberg-rest}} # Meta Store type (optional)
	metastoreUrl: {{}} # Meta Store URL (optional)
	relativePath: {{}} # Relative Path (optional)
```

<center>

| Attribute | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| [`gcs`](./lakehouse/yaml_configuration_attributes.md#gcs) | object | none | none | optional |
| [`bucket`](./lakehouse/yaml_configuration_attributes.md#bucket) | string | none | any valid GCS bucket name | optional |
| [`format`](./lakehouse/yaml_configuration_attributes.md#format) | string | none | any valid format | optional |
| [`icebergCatalogType`](./lakehouse/yaml_configuration_attributes.md#icebergcatalogtype) | string | none | hadoop | optional |
| [`metastoreType`](./lakehouse/yaml_configuration_attributes.md#metastoretype) | string | none | iceberg-rest | optional |
| [`metastoreUrl`](./lakehouse/yaml_configuration_attributes.md#metastoreurl) | string | none | any valid URL | optional |
| [`relativePath`](./lakehouse/yaml_configuration_attributes.md#relativepath) | string | none | any valid relative path | optional |

</center>

##### **ABFSS**

```yaml
abfss:
	account: {{}} # ABFSS Account (optional)
	container: {{}} # 
	endpointSuffix: {{}} # End Point Suffix (optional)
	format: {{}} # File Format (optional)
	icebergCatalogType: {{}} # Iceberg Catalog Type (optional)
	metastoreType: {{}} # Metastore type (optional)
	metastoreUrl: {{}} # Metastore URL (optional)
	relativePath: {{}} # Relative Path (optional)
```

<center>

| Attribute | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| [`abfss`](./lakehouse/yaml_configuration_attributes.md#abfss) | object | none | none | optional |
| [`account`](./lakehouse/yaml_configuration_attributes.md#account) | string | none | any valid ABFSS account | optional |
| [`container`](./lakehouse/yaml_configuration_attributes.md#container) | string | none | any valid container name | optional |
| [`endpointSuffix`](./lakehouse/yaml_configuration_attributes.md#endpointsuffix) | string | none | any valid endpoint suffix | optional |
| [`format`](./lakehouse/yaml_configuration_attributes.md#format) | string | none | any valid file format | optional |
| [`icebergCatalogType`](./lakehouse/yaml_configuration_attributes.md#icebergcatalogtype) | string | none | any valid Iceberg catalog type | optional |
| [`metastoreType`](./lakehouse/yaml_configuration_attributes.md#metastoretype) | string | none | any valid metastore type | optional |
| [`metastoreUrl`](./lakehouse/yaml_configuration_attributes.md#metastoreurl) | string | none | any valid URL | optional |
| [`relativePath`](./lakehouse/yaml_configuration_attributes.md#relativepath) | string | none | any valid relative path | optional |

</center>

##### **WASBS**

```yaml
wasbs:
	account: {{}} # ABFSS Account (optional)
	container: {{}} # 
	endpointSuffix: {{}} # End Point Suffix (optional)
	format: {{}} # File Format (optional)
	icebergCatalogType: {{}} # Iceberg Catalog Type (optional)
	metastoreType: {{}} # Metastore type (optional)
	metastoreUrl: {{}} # Metastore URL (optional)
	relativePath: {{}} # Relative Path (optional)
```

<center>

| Attribute | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| [`wasbs`](./lakehouse/yaml_configuration_attributes.md#wasbs) | object | none | none | optional |
| [`account`](./lakehouse/yaml_configuration_attributes.md#account) | string | none | any valid WASBS account | optional |
| [`container`](./lakehouse/yaml_configuration_attributes.md#container) | string | none | any valid container name | optional |
| [`endpointSuffix`](./lakehouse/yaml_configuration_attributes.md#endpointsuffix) | string | none | any valid endpoint suffix | optional |
| [`format`](./lakehouse/yaml_configuration_attributes.md#format) | string | none | any valid file format | optional |
| [`icebergCatalogType`](./lakehouse/yaml_configuration_attributes.md#icebergcatalogtype) | string | none | any valid Iceberg catalog type | optional |
| [`metastoreType`](./lakehouse/yaml_configuration_attributes.md#metastoretype) | string | none | any valid metastore type | optional |
| [`metastoreUrl`](./lakehouse/yaml_configuration_attributes.md#metastoreurl) | string | none | any valid URL | optional |
| [`relativePath`](./lakehouse/yaml_configuration_attributes.md#relativepath) | string | none | any valid relative path | optional |

</center>


##### **S3**

```yaml
s3:
	bucket: {{bucket-testing}} # GCS Bucket (optional)
	format: {{format}} # Format (optional)
	icebergCatalogType: {{hadoop}} # Iceberg Catalog Type (optional)
	metastoreType: {{iceberg-rest}} # Meta Store type (optional)
	metastoreUrl: {{}} # Meta Store URL (optional)
	relativePath: {{}} # Relative Path (optional)
	scheme: {{}} # Scheme (optional)
```

<center>

| Attribute | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| [`s3`](./lakehouse/yaml_configuration_attributes.md#s3) | object | none | none | optional |
| [`bucket`](./lakehouse/yaml_configuration_attributes.md#bucket) | string | none | any valid S3 bucket name | optional |
| [`format`](./lakehouse/yaml_configuration_attributes.md#format) | string | none | any valid format | optional |
| [`icebergCatalogType`](./lakehouse/yaml_configuration_attributes.md#icebergcatalogtype) | string | none | hadoop | optional |
| [`metastoreType`](./lakehouse/yaml_configuration_attributes.md#metastoretype) | string | none | iceberg-rest | optional |
| [`metastoreUrl`](./lakehouse/yaml_configuration_attributes.md#metastoreurl) | string | none | any valid URL | optional |
| [`relativePath`](./lakehouse/yaml_configuration_attributes.md#relativepath) | string | none | any valid relative path | optional |
| [`scheme`](./lakehouse/yaml_configuration_attributes.md#scheme) | string | none | any valid scheme | optional |

</center>

#### **Query Engine configuration**

```yaml
queryEngine:
	type: {{themis}} # Query Engine type (mandatory)
	resources: # CPU and memory resources (optional)
		requests: 
			cpu: {{1Gi}} # Requested CPU resources (optional)
			memory: {{400m}} # Requested Memory resources (optional)
		limits:
			cpu: {{1Gi}} # CPU resource limits (optional)
			memory: {{400m}} # Memory resource limits (optional)
	themis/minerva: # Cluster-specific configuration (optional)
		{{themis/minerva specific attributes}}
```

<center>

| Attribute | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| [`queryEngine`](./lakehouse/yaml_configuration_attributes.md#queryengine) | object | none | none | mandatory |
| [`type`](./lakehouse/yaml_configuration_attributes.md#type) | string | none | themis | mandatory |
| [`resources`](./lakehouse/yaml_configuration_attributes.md#resources) | object | none | none | optional |
| [`requests`](./lakehouse/yaml_configuration_attributes.md#requests) | object | none | none | optional |
| [`cpu`](./lakehouse/yaml_configuration_attributes.md#cpu) (under `requests`) | string | none | any valid CPU resource amount | optional |
| [`memory`](./lakehouse/yaml_configuration_attributes.md#memory) (under `requests`) | string | none | any valid memory resource amount | optional |
| [`limits`](./lakehouse/yaml_configuration_attributes.md#limits) | object | none | none | optional |
| [`cpu`](./lakehouse/yaml_configuration_attributes.md#cpu) (under `limits`) | string | none | any valid CPU resource limit | optional |
| [`memory`](./lakehouse/yaml_configuration_attributes.md#memory) (under `limits`) | string | none | any valid memory resource limit | optional |
| [`themis/minerva`](./lakehouse/yaml_configuration_attributes.md#themisminerva) | object | none | none | optional |
| [`themis/minerva specific attributes`](./lakehouse/yaml_configuration_attributes.md#themisminervaspecificattributes) | object | none | none | as per themis/minerva type |

</center>

##### **Themis**

```yaml
themis: 
	envs: 
		
	themisConf:
	
	spark: 
		driver: # Spark driver configuration (mandatory)
			memory: {{400m}} # Driver memory (mandatory)
			cpu: {{1Gi}} # Driver CPU (mandatory)
		executor: # Spark executor configuration (mandatory)
			memory: {{400m}} # Driver memory (mandatory)
			cpu: {{1Gi}} # Driver CPU (mandatory)
			instanceCount: {{2}} # Executor Instance count (mandatory)
			maxInstanceCount: {{4}} # Maximum executor Instance count (mandatory)
		sparkConf: # Spark environment configuration (optional)
```

<center>

| Attribute | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| [`themis`](./lakehouse/yaml_configuration_attributes.md#themis) | object | none | none | mandatory |
| [`envs`](./lakehouse/yaml_configuration_attributes.md#envs) | object | none | none | optional |
| [`themisConf`](./lakehouse/yaml_configuration_attributes.md#themisconf) | object | none | none | optional |
| [`spark`](./lakehouse/yaml_configuration_attributes.md#spark) | object | none | none | mandatory |
| [`driver`](./lakehouse/yaml_configuration_attributes.md#driver) (under `spark`) | object | none | none | mandatory |
| [`memory`](./lakehouse/yaml_configuration_attributes.md#memory) (under `driver`) | string | none | any valid memory amount | mandatory |
| [`cpu`](./lakehouse/yaml_configuration_attributes.md#cpu) (under `driver`) | string | none | any valid CPU resource | mandatory |
| [`executor`](./lakehouse/yaml_configuration_attributes.md#executor) (under `spark`) | object | none | none | mandatory |
| [`memory`](./lakehouse/yaml_configuration_attributes.md#memory) (under `executor`) | string | none | any valid memory amount | mandatory |
| [`cpu`](./lakehouse/yaml_configuration_attributes.md#cpu) (under `executor`) | string | none | any valid CPU resource | mandatory |
| [`instanceCount`](./lakehouse/yaml_configuration_attributes.md#instancecount) (under `executor`) | integer | none | any valid integer | mandatory |
| [`maxInstanceCount`](./lakehouse/yaml_configuration_attributes.md#maxinstancecount) (under `executor`) | integer | none | any valid integer | mandatory |
| [`sparkConf`](./lakehouse/yaml_configuration_attributes.md#sparkconf) (under `spark`) | object | none | none | optional |

</center>


##### **Minerva**

```yaml
minerva: 
	replicas: {{2}} # Number of replicas (mandatory)
	coordinatorEnvs: # Coordinator environment variables (optional)
		
	workerEnvs: # Worker environment variables (optional)

	overrideDefaultEnvs: {{true}} # Override Default Environment Variables (optional)
	spillOverVolume: {{alpha}} # Spill Over Volume (optional)
	debug: # Debug (optional)
		logLevel: {{INFO}} # LogLevel (optional)
		trinoLogLevel: {{DEBUG}} # Trino Log Level (optional)
```

<center>

| Attribute | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| [`minerva`](./lakehouse/yaml_configuration_attributes.md#minerva) | object | none | none | mandatory |
| [`replicas`](./lakehouse/yaml_configuration_attributes.md#replicas) | integer | none | any valid integer | mandatory |
| [`coordinatorEnvs`](./lakehouse/yaml_configuration_attributes.md#coordinatorenvs) | object | none | none | optional |
| [`workerEnvs`](./lakehouse/yaml_configuration_attributes.md#workerenvs) | object | none | none | optional |
| [`overrideDefaultEnvs`](./lakehouse/yaml_configuration_attributes.md#overridedefaultenvs) | boolean | none | true/false | optional |
| [`spillOverVolume`](./lakehouse/yaml_configuration_attributes.md#spillovervolume) | string | none | any valid volume name | optional |
| [`debug`](./lakehouse/yaml_configuration_attributes.md#debug) | object | none | none | optional |
| [`logLevel`](./lakehouse/yaml_configuration_attributes.md#loglevel) (under `debug`) | string | none | INFO, DEBUG, etc. | optional |
| [`trinoLogLevel`](./lakehouse/yaml_configuration_attributes.md#trinologlevel) (under `debug`) | string | none | any valid log level for Trino | optional |

</center>

### **Apply the Lakehouse YAML**

After creating the YAML configuration file for the Lakehouse Resource, it's time to apply it to instantiate the Resource-instance in the DataOS environment. To apply the Lakehouse YAML file, utilize the [`apply`](../interfaces/cli/command_reference.md#apply) command.

```shell
dataos-ctl apply -f {{yaml config file path}} - w {{workspace name}}
# Sample
dataos-ctl apply -f dataproducts/new-lakehouse.yaml -w curriculum
```

<details>
<summary>Sample Lakehouse YAML</summary>
    
```yaml
version: v1alpha
name: {{s3-depot-name}}
layer: user
type: lakehouse
tags:
  - Iceberg
  - Azure
description: "Icebase depot of storage-type S3"
lakehouse:
  type: iceberg
  compute: runnable-default
  iceberg:
    storage:
      type: s3
      s3:
        bucket: {{s3 bucket name}}        # "tmdc-dataos-testing"
        relativePath: {{relative path}}
      secrets:
        - name: {{s3-depot-name}}-rw
          keys:
            - {{s3-depot-name}}-rw
          allkeys: true    
        - name: {{s3-depot-name}}-r
          keys:
            - {{s3-depot-name}}-r
          allkeys: true 
    metastore:
      type: "iceberg-rest-catalog"
    queryEngine:
      type: {{query engine}}
```
</details>

### **Verify Lakehouse Creation**

To ensure that your Lakehouse has been successfully created, you can verify it in two ways:

Check the name of the newly created Lakehouse in the list of lakehouses created by you in a particular Workspace:

```shell
dataos-ctl get -t lakehouse - w {{workspace name}}
# Sample
dataos-ctl get -t lakehouse -w curriculum
```

Alternatively, retrieve the list of all Lakehouses created in the Workspace by appending `-a` flag:

```shell
dataos-ctl get -t lakehouse -w {{workspace name}} -a
# Sample
dataos-ctl get -t lakehouse -w curriculum
```

You can also access the details of any created Lakehouse through the DataOS GUI in the Resource tab of the  [Operations App.](../interfaces/operations.md)

### **Deleting a Lakehouse**

Use the [`delete`](../interfaces/cli/command_reference.md#delete) command to remove the specific Lakehouse Resource-instance from the DataOS environment. There are three ways to delete a Lakehouse as shown below.

**Method 1:** Copy the name to Workspace from the output table of the [`get`](../interfaces/cli/command_reference.md#get) command and use it as a string in the delete command.

Command

```shell
dataos-ctl delete -i "{{name to workspace in the output table from get status command}}"
```

Example:

```shell
dataos-ctl delete -i "cnt-lakehouse-demo-01 | v1alpha | lakehouse | public"
```

Output:

```shell
INFO[0000] 🗑 delete...
INFO[0001] 🗑 deleting(public) cnt-lakehouse-demo-01:v1alpha:lakehouse...
INFO[0003] 🗑 deleting(public) cnt-lakehouse-demo-01:v1alpha:lakehouse...deleted
INFO[0003] 🗑 delete...complete
```

**Method 2:** Specify the path of the YAML file and use the [`delete`](../interfaces/cli/command_reference.md#delete) command.

Command:

```shell
dataos-ctl delete -f {{file-path}}
```

Example:

```shell
dataos-ctl delete -f /home/desktop/connect-city/config_v1alpha.yaml
```

Output:

```shell
INFO[0000] 🗑 delete...
INFO[0000] 🗑 deleting(public) cnt-lakehouse-demo-010:v1alpha:lakehouse...
INFO[0001] 🗑 deleting(public) cnt-lakehouse-demo-010:v1alpha:lakehouse...deleted
INFO[0001] 🗑 delete...complete
```

**Method 3:** Specify the Workspace, Resource-type, and Lakehouse name in the [`delete`](../interfaces/cli/command_reference.md#delete) command.

Command:

```shell
dataos-ctl delete -w {{workspace}} -t lakehouse -n {{lakehouse name}}
```

Example:

```shell
dataos-ctl delete -w public -t lakehouse -n cnt-product-demo-01
```

Output:

```shell
INFO[0000] 🗑 delete...
INFO[0000] 🗑 deleting(public) cnt-city-demo-010:v1alpha:lakehouse...
INFO[0001] 🗑 deleting(public) cnt-city-demo-010:v1alpha:lakehouse...deleted
INFO[0001] 🗑 delete...complete
```


## Attributes of Lakehouse YAML

The Attributes of Lakehouse YAML define the key properties and configurations that can be used to specify and customize Lakehouse Resources within a YAML file. These attributes allow data developers to define the structure and behavior of their Lakehouse Resources. For comprehensive information on each attribute and its usage, please refer to the link: [Attributes of Lakehouse YAML.](./lakehouse/yaml_configuration_attributes.md)

## Lakehouse Command Reference

Here is a reference to the various commands related to managing Lakehouses in DataOS:

- **Applying a Lakehouse:** Use the following command to apply a Lakehouse using a YAML configuration file:
    
    ```shell 
    dataos-ctl apply -f {{yaml config file path}} -w {{workspace}}
    dataos-ctl resource apply -f {{yaml config file path}} -w {{workspace}}
    # Sample
    dataos-ctl resource apply -f lakehouse/lakehouse.yaml -w curriculum
    dataos-ctl resource apply -f lakehouse/lakehouse.yaml -w curriculum
    ```
    
- **Get Lakehouse Status:** To retrieve the status of a specific Lakehouse, use the following command:
    
    ```shell
    dataos-ctl get -t lakehouse -w {{workspace name}}
    # Sample
    dataos-ctl get -t lakehouse -w curriculum
    ```
    
- **Get Status of all Workers within a Workspace:** To get the status of all Workers within the current context, use this command:
    
    ```shell
    dataos-ctl get -t lakehouse -w {{workspace name}} -a
    # Sample
    dataos-ctl get -t lakehouse -w curriculum -a
    ```
    
- **Generate Lakehouse JSON Schema:** To generate the JSON schema for a Lakehouse with a specific version (e.g., v1alpha), use the following command:
    
    ```shell
    dataos-ctl develop schema generate -t lakehouse -v {{version}}
    # Sample
    dataos-ctl develop schema generate -t lakehouse -v v1alpha
    ```
    
- **Get Lakehouse JSON Resource Schema:** To obtain the JSON resource schema for a Lakehouse with a specific version (e.g., v1alpha), use the following command:
    
    ```shell
    dataos-ctl develop get resource -t lakehouse -v {{version}}
    # Sample
    dataos-ctl develop get resource -t lakehouse -v v1alpha
    ```
    
- **Delete Workers:** To delete a specific lakehouse you can use the below command
    
    ```shell
    dataos-ctl delete -t lakehouse -w {{workspace name}} -n {{name of lakehouse}}
    # Sample
    dataos-ctl delete -t lakehouse -w curriculum -n benthos3-lakehouse
    ```

## Case Scenario

- [How to create a Lakehouse on ABFSS data source?](./lakehouse/how_to_create_a_lakehouse_on_abfss_data_source.md)
- [How to create a Lakehouse on WASBS data source?](./lakehouse/how_to_create_a_lakehouse_on_wasbs_data_source.md)
- [How to create a Lakehouse on S3 data source?](./lakehouse/how_to_create_a_lakehouse_on_s3_data_source.md)
- [How to create a Lakehouse on GCS data source?](./lakehouse/how_to_create_a_lakehouse_on_gcs_data_source.md)









