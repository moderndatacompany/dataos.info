# How to Overwrite Dynamic Iceberg Partitions Using DataOS PyFlare?

```python
# Import necessary libraries
from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyflare.sdk import load, save, session_builder

# Define Spark configuration
sparkConf = [
    ("spark.app.name", "Dataos Sdk Spark App"),  # Set the Spark application name
    ("spark.master", "local[*]"),  # Use local mode for Spark execution
]

# DataOS configuration
DATAOS_FQDN = "current-joey.dataos.app"
token = "cmFrZXNoX3Rlc3RpbmcuNTQ4NGEwZWEtNTcwNi00Zjc1LWE2YTgtYTlhZTE3Nzg2OGI2"

# Create a Spark session with DataOS settings
spark = session_builder.SparkSessionBuilder() \
    .with_spark_conf(sparkConf) \
    .with_user_apikey(token) \
    .with_dataos_fqdn(DATAOS_FQDN) \
    .with_depot("dataos://icebase:pyflaresdk/test_write_03", "rw") \
    .build_session()

# Ignore warning for "The specified path does not exist."

# Generate random data and create a DataFrame for overwriting
overwriteDf = spark.createDataFrame(GenerateData()).repartition(1)

# Define options for saving data in Iceberg format with partitioning
opts = {
    "fanout-enabled": "true",
    "iceberg": {
        "partition":
            [
                {
                    "type": "identity",
                    "column": "name"
                }
            ]
    }
}

# Save DataFrame to DataOS in Iceberg format with overwrite mode
save(name="dataos://icebase:pyflaresdk/test_write_03", dataframe=overwriteDf, format="iceberg", mode="overwrite", options=opts)

# Load data from DataOS in Iceberg format
temp_df_part = load(name="dataos://icebase:pyflaresdk/test_write_03", format="iceberg")

# Display the total number of records
print("Total Records: ", temp_df_part.count())

# Filter records where name is 'Alice'
f_df = temp_df_part.where("name = 'Alice'")
f_df.show(5)

# Count the number of records with name 'Alice'
alice_records = f_df.count()
print("Alice Records: ", alice_records)
```