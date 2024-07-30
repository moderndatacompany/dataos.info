# Google Bigquery Depots

Flare stack enables execution of jobs on top of Google Bigquery data source. To do so, you first need to create a Bigquery depot. If you have already created a depot, you can proceed with the following instructions. Otherwise, please refer to the [Biguery Depot](/resources/depot/depot_config_templates/google_bigquery/).

## Read Configuration

For reading data using Flare stack, the `name`, `dataset`, and `format` properties in the `inputs` section of the YAML configuration need to be configured. Here's an example configuration for the `inputs` section:

```yaml
inputs:
  - name: city_connect # name of the dataset
    dataset: dataos://bqdepot:state/city # address of the input dataset
    format: bigquery # format
```

<details><summary>Sample Read configuration YAML</summary>

Consider a scenario where the dataset named `city` is stored in a BigQuery Depot at the address `dataos://bqdepot:state/city`, and you need to read this data from the source Bigquery depot, perform some transformation steps, and write it to Icebase, a managed depot within DataOS. The read config YAML will be as follows:

```yaml title="bigquery_depot_read.yml"
--8<-- "examples/resources/stacks/flare/bigquery_depot_read.yml"
```

</details>

## Write Configuration

For writing the data to a depot on a Bigquery depot, we need to configure the `name`,  `dataset` and `format` properties in the `outputs` section of the YAML. For instance, if your dataset is to be stored at the UDL address is `dataos://yakdevbq:dev/city_bq?acl=rw`  by the name `finaldf` and the file format is `Bigquery`. Then the outputs section will be as follows

```yaml
outputs:
	- name: finalDf
    dataset: dataos://yakdevbq:dev/city_bq?acl=rw
    format: Bigquery
    options:
	    saveMode: append
      bigquery:
	      temporaryBucket: tmdc-development-new
```

**Sample Write configuration YAML**

Let’s take a case scenario where the output dataset is to be stored in Bigquery Depot and you have to read data from the Icebase depot within the DataOS The write config YAML will be as follows


```yaml title="bigquery_depot_write.yml"
--8<-- "examples/resources/stacks/flare/bigquery_depot_write.yml"
```

### **Methods for Writing Data to BigQuery**

Writing data to BigQuery can be achieved using two methods: [Direct](#direct-write-method) and [Indirect](#indirect-write-method).

<aside class="callout">
🗣 The default <code>writeMethod</code> is indirect.

</aside>

#### **Direct Write Method**

The direct method writes data directly into a BigQuery table without using a temporary bucket. This method uses the [BigQuery Storage Write API](https://cloud.google.com/bigquery/docs/write-api). To enable this, set the `writeMethod` to `direct`:

```yaml
outputs:
  - dataset: dataos://sanitybigquery:dev/bigquery_table?acl=rw
    format: bigquery
    name: finalDf
    options:
      saveMode: append
      extraOptions:
        writeMethod: direct
```

<aside class="callout">
🗣 Writing to existing partitioned tables (date partitioned, ingestion time partitioned, and range partitioned) in APPEND mode and OVERWRITE mode (only date and range partitioned) is fully supported by the connector and the BigQuery Storage Write API. The use of <code>datePartition</code>, <code>partitionField</code>, <code>partitionType</code>, <code>partitionRangeStart</code>, <code>partitionRangeEnd</code>, <code>partitionRangeInterval</code> is not supported by the direct write method.

</aside>

#### **Indirect Write Method**

In the indirect method, data is first written to a GCS bucket and then loaded into BigQuery via a load operation. A GCS bucket must be configured to indicate the temporary data location. Data is temporarily stored using `parquet`, `orc`, or `avro` formats, with `parquet` being the default.

> Parquet does not support Map data types. If using Flare to write data, which adds a `__metadata` column of Map type, use `avro` as the `intermediateFormat`.
> 

```yaml
outputs:
  - dataset: dataos://sanitybigquery:dev/bigquery_write_nabeel_103?acl=rw
    format: bigquery
    name: finalDf
    options:
      bigquery:
        temporaryBucket: tmdc-development-new
        persistentBucket: tmdc-development-new
      saveMode: append
      extraOptions:
        temporaryGcsBucket: tmdc-development-new
        persistentGcsBucket: tmdc-development-new
        intermediateFormat: avro
```

> There are two ways to specify the bucket, either in `bigquery` or `extraOptions`. But for `indirect` write method, it has to be specified in the `extraOptions`.
> 

**Attributes Description**

| Attribute | Description | Usage |
| --- | --- | --- |
| `writeMethod` | Controls the method for writing data to BigQuery. Available values are direct for the BigQuery Storage Write API and indirect for writing data first to GCS and then triggers a BigQuery load operation. (Optional, defaults to indirect) | Write |
| `temporaryGcsBucket` | The GCS bucket temporarily holding data before loading into BigQuery. Not supported by the direct write method. | Write |
| `persistentGcsBucket` | The GCS bucket holding data before loading into BigQuery. If set, data won't be deleted after writing to BigQuery. Not supported by the direct write method. | Write |
| `intermediateFormat` | Format of data before loading into BigQuery, either "parquet", "orc", or "avro". Defaults to parquet. Supported only for the indirect write method. | Write |

<aside class="callout">
🗣 Reading all data types is supported except `BIGNUMERIC`. BigQuery's BigNumeric has a precision of 76.76 (the 77th digit is partial) and scale of 38. Since this precision and scale is beyond spark's DecimalType (38 scale and 38 precision) support, it means that BigNumeric fields with precision larger than 38 cannot be used.

</aside>