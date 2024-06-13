## **How to utilize Depots?**

Once a Depot is created, you can leverage its Uniform Data Links (UDLs) to access data without physically moving it. The UDLs play a crucial role in various scenarios within DataOS.

### **Work with Stacks**

Depots are compatible with different Stacks in DataOS. [Stacks](./stacks.md) provide distinct approaches to interact with the system and enable various programming paradigms in DataOS. Several Stacks are available that can be utilized with depots, including [Scanner](./stacks/scanner.md) for introspecting depots, [Flare](./stacks/flare.md) for data ingestion, transformation, syndication, etc., [Benthos](./stacks/benthos.md) for stream processing and [Data Toolbox](./stacks/data_toolbox.md) for managing [Icebase](./depot/icebase.md) DDL and DML. 

[Flare](./stacks/flare.md) and [Scanner](./stacks/scanner.md) Stacks are supported by all Depots, while [Benthos](./stacks/benthos.md), the stream-processing Stack, is compatible with read/write operations from streaming depots like [Fastbase](./depot/fastbase.md) and Kafka Depots.

The UDL references are used as addresses for your input and output datasets within the manifest configuration file.

### **Limit Data Source's File Format**

Another important function that a Depot can play is to limit the file type which you can read from and write to a particular data source. In the `spec` section of manifest config file, simply mention the `format` of the files you want to allow access for.

``` yaml
depot:
  type: S3
  description: ${{description}}
  external: true
  spec:
    scheme: ${{s3a}}
    bucket: ${{bucket-name}}
    relativePath: "raw" 
    format: ${{format}}  # mention the file format, such as JSON
```
For File based systems, if you define the format as ‘Iceberg’, you can choose the meta-store catalog between Hadoop and Hive. This is how you do it:

``` yaml
depot:
  type: ABFSS
  description: "ABFSS Iceberg depot for sanity"
  compute: runnable-default
  spec:
    account: 
    container: 
    relativePath:
    format: ICEBERG
    endpointSuffix:
    icebergCatalogType: Hive
```
If you do not mention the catalog name as Hive, it will use Hadoop as the default catalog for Iceberg format.


![Depot Hierarchy](./depot/depot_catalog.png)
<center><i>Flow when Hive is chosen as the catalog type</i></center>

Hive, automatically keeps the pointer updated to the latest metadata version. If you use Hadoop, you have to manually do this by running the set metadata command as described on this page: [Set Metadata](../resources/depot/icebase.md)

### **Scan and Catalog Metadata**

By running the [Scanner](./stacks/scanner.md), you can scan the metadata from a source system via the Depot interface. Once the metadata is scanned, you can utilize [Metis](../interfaces/metis.md) to catalog and explore the metadata in a structured manner. This allows for efficient management and organization of data resources.

### **Add Depot to Cluster Sources to Query the Data**

To enable the [Minerva](./cluster.md#minerva) Query Engine to access a specific source system, you can add the Depot to the list of sources in the [Cluster](./cluster.md). This allows you to query the data and create dashboards using the DataOS [Workbench](../interfaces/workbench.md) and [Atlas](../interfaces/atlas.md). 

### **Create Policies upon Depots to Govern the Data**

[Access](./policy.md#access-policy) and [Data Policies](./policy.md#data-policy) can be created upon Depots to govern the data. This helps in reducing data breach risks and simplifying compliance with regulatory requirements. Access Policies can restrict access to specific depots, collections, or datasets, while Data Policies allow you to control the visibility and usage of data.

### **Building Data Models**

You can use Lens to create Data Models on top of Depots and explore them using the [Lens App UI.](../interfaces/lens.md)