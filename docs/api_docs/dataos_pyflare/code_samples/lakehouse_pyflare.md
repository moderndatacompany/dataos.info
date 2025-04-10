# Lakehouse Operations with DataOS PyFlare

This document provides code samples and usage instructions for performing common Lakehouse operations using the DataOS PyFlare SDK. The operations include reading and writing data, merging records into Iceberg tables, and configuring partitioning strategies.

## Prerequisites

Ensure the following dependencies and configurations are available before executing the samples:

- DataOS FQDN (Fully Qualified Domain Name)
- User API Token
- SparkSession with appropriate configurations
- Access to the Lakehouse depot

## Read and Write Operations

Following script demonstrates how to read data from and write data to a Lakehouse table in Iceberg format using DataOS PyFlare SDK:

```python
# import required libraries
from pyspark.sql import SparkSession
from pyflare.sdk import load, save, session_builder

# Define DataOS connection parameters
DATAOS_FQDN = "example-dataos.dataos.app"
token = "<your_auth_token>"

# Spark configuration settings
sparkConf = [
    ("spark.app.name", "Pyflare App"),
    ("spark.master", "local[*]"),
]

# Build Spark session connected to DataOS
spark = session_builder.SparkSessionBuilder(log_level="INFO") \
    .with_spark_conf(sparkConf) \
    .with_user_apikey(token) \
    .with_dataos_fqdn(DATAOS_FQDN) \
    .with_depot(depot_name="lakehouse", acl="rw") \
    .build_session()

# Load Iceberg data from Lakehouse
df = load(name="dataos://lakehouse:test_crm/product_data", format="iceberg")
df.show(10)

# Save the data back to Lakehouse in overwrite mode
save(name="dataos://lakehouse:sandbox3/test_pyflare2", dataframe=df, format="iceberg", mode="overwrite")

# Stop Spark session
spark.stop()

```

## Merge Into Iceberg Table

The following script shows how to perform a merge-into (upsert) operation on an Iceberg table using DataOS PyFlare:

```python
from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyflare.sdk import load, save, session_builder

# Define DataOS connection parameters
DATAOS_FQDN = "example-dataos.dataos.app"
token = "<your_auth_token>"

# Spark configuration
sparkConf = [
    ("spark.app.name", "Pyflare App"),
    ("spark.master", "local[*]"),
]

# Build Spark session
spark = session_builder.SparkSessionBuilder(log_level="INFO") \
    .with_spark_conf(sparkConf) \
    .with_user_apikey(token) \
    .with_dataos_fqdn(DATAOS_FQDN) \
    .with_depot(depot_name="lakehouse", acl="rw") \
    .build_session()

# Loading and displaying data need to be Updated 
load(name="dataos://lakehouse:sandbox3/test_pyflare2", format="iceberg").show()

# Create new data to be updated and merged 
new_data = [
    Row(id=10, name="self", age=32, city="selfish"),  # Will update
    Row(id=11, name="not-self", age=32, city="not-selfish")  # Will insert
]
new_df = spark.createDataFrame(new_data)

# Define merge options for Iceberg
opts = {
    "iceberg": {
        "merge": {
            "onClause": "source.id = target.id",
            "whenClause": "when matched then update set * when not matched then insert *"
        }
    }
}

# Perform merge into
save(name="dataos://lakehouse:sandbox3/test_pyflare2", dataframe=new_df, format="iceberg", mode="overwrite", options=opts)

# Verify the merged result
load(name="dataos://lakehouse:sandbox3/test_pyflare2", format="iceberg").show()

# Stop session
spark.stop()
```

## Partitioning in Iceberg

The following script writes data to an Iceberg table with multiple partitioning strategies using the DataOS PyFlare SDK.

```python
# Importing necessary libraries

from pyspark.sql import SparkSession
from pyspark.sql import Row
from datetime import datetime
from pyflare.sdk import load, save, session_builder

# DataOS credentials and config
DATAOS_FQDN = "example-dataos.dataos.app"
token = "<your_auth_token>"

sparkConf = [
    ("spark.app.name", "Pyflare App"),
    ("spark.master", "local[*]"),
]

# Start DataOS Spark session
spark = session_builder.SparkSessionBuilder(log_level="INFO") \
    .with_spark_conf(sparkConf) \
    .with_user_apikey(token) \
    .with_dataos_fqdn(DATAOS_FQDN) \
    .with_depot(depot_name="lakehouse", acl="rw") \
    .build_session()


# Sample dataset with partition-relevant fields
data = [
    Row(id=1, name="Alice", age=28, date_of_birth=datetime(1995, 5, 12)),
    Row(id=2, name="Bob", age=35, date_of_birth=datetime(1988, 8, 22)),
    Row(id=3, name="Charlie", age=22, date_of_birth=datetime(2001, 3, 9)),
    Row(id=4, name="David", age=29, date_of_birth=datetime(1994, 11, 3)),
    Row(id=5, name="Eve", age=24, date_of_birth=datetime(1999, 1, 17)),
    Row(id=6, name="Frank", age=31, date_of_birth=datetime(1992, 7, 28)),
    Row(id=7, name="Grace", age=26, date_of_birth=datetime(1997, 12, 5)),
    Row(id=8, name="Hank", age=39, date_of_birth=datetime(1984, 9, 15)),
    Row(id=9, name="Ivy", age=27, date_of_birth=datetime(1996, 6, 20)),
    Row(id=10, name="Jack", age=32, date_of_birth=datetime(1991, 2, 10))
]

# Create DataFrame
df = spark.createDataFrame(data)

# Partitioning options for Iceberg table
opts = {
    "fanout-enabled": "true",
    "iceberg": {
        "partition": [
            {"type": "bucket", "column": "age", "bucket_count": 3},
            {"type": "identity", "column": "name"},
            {"type": "year", "column": "date_of_birth"}
        ]
    }
}

# Save the partitioned table
save(name="dataos://lakehouse:sandbox3/test_pyflare2", dataframe=df, format="iceberg", mode="overwrite", options=opts)

# Validate written data
load(name="dataos://lakehouse:sandbox3/test_pyflare2", format="iceberg").show()

# End session
spark.stop()
```

<aside class="best-practice" style="border-left: 4px solid #28a745; background-color: #e6f4ea; color: #1e4620; padding: 1rem; border-radius: 0.5rem; margin: 1rem 0;">
<b>Note:</b> Placeholder values such as depot names, schema names, FQDN, and token will be updated to representative examples, and every script will explicitly include `spark.stop()` at the end to terminate the Spark session.
</aside>

**Important Placeholder Changes Required:**

- **`DATAOS_FQDN`**: Replace `"example-dataos.dataos.app"` with the actual FQDN of the target DataOS instance.
- **`token`**: Replace with a valid DataOS API key.
- **`depot_name` in `.with_depot(...)`**: Confirm that the depots (e.g., `"lakehouse"`) exist and have proper permissions.
- **`load(...)` and `save(...)` URIs**: Replace the table and path values to match the desired source and target datasets.

## Command Line Interface (CLI) References

### Update Partition Information

To update the partitioning options, execute the following command in the CLI:

```bash
dataos-ctl dataset update-partition -a dataos://icebase:retail/city \
-p "<partition_type>:<column_name>:<partition_name>" \
-p "<partition_type>:<column_name>" \
-p "<partition_type>:<column_name>:<partition_name>:<number_of_buckets>"
```

### Drop Dataset from Metastore

To delete the entry from the metastore and remove the associated files, use the following code:

```bash
dataos-ctl dataset drop -a dataos://icebase:retail/city --purge true
```