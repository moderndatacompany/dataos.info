# How to write data in Avro Format from Iceberg format using DataOS PyFlare?

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
    .with_depot("dataos://icebase:pyflaresdk/test_write_04", "rw") \
    .build_session()

# Define options for saving data in Iceberg format with Avro write format and partitioning
opts = {
    "fanout-enabled": "true",
    "write-format": "avro",
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

# Generate random data and create a DataFrame
avro_iceberg = spark.createDataFrame(GenerateData()).repartition(1)

# Save DataFrame to DataOS in Iceberg format with Avro write format and overwrite mode
save(name="dataos://icebase:pyflaresdk/test_write_04", dataframe=avro_iceberg, format="iceberg", mode="overwrite", options=opts)

# Load and display data from DataOS in Iceberg format
load(name="dataos://icebase:pyflaresdk/test_write_04", format="iceberg").show(10)

# Uncomment the following line if you wish to stop the Spark session
# spark.stop()

```