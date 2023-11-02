# How to read write partitioned data within Icebase using DataOS PyFlare?

```python

# Import necessary libraries
from pyspark.sql import SparkSession
from pyspark.sql import Row
import random
from datetime import datetime, timedelta
from pyflare.sdk import load, save, session_builder

# Define Spark configuration
sparkConf = [
    ("spark.app.name", "Iceberg Read Write Partitioned Data"),  # Set the Spark application name
    ("spark.master", "local[*]"),  # Use local mode for Spark execution
]

# DataOS configuration
DATAOS_FQDN = "{{dataos-fqdn}}"
token = "{{dataos-apikey-token}}"

# Create a Spark session with DataOS settings
spark = session_builder.SparkSessionBuilder(log_level="INFO") \
    .with_spark_conf(sparkConf) \
    .with_user_apikey(token) \
    .with_dataos_fqdn(DATAOS_FQDN) \
    .with_depot(depot_name="icebase", acl="rw") \
    .build_session()

# Generate random data and create a DataFrame
def GenerateData():
    num_rows = random.randint(1000, 10000)  # Randomly determine the number of rows
    first_names = ["Alice", "Bob", "Charlie", "David", "Emily", "Frank", "Grace", "Henry", "Ivy", "Jack", "Karen", "Leo",
                   "Mia", "Noah", "Olivia", "Peter", "Quinn", "Rachel", "Sam", "Tom", "Uma", "Victor", "Wendy", "Xander",
                   "Yvonne", "Zane"
                   ]

    data = []
    for _ in range(num_rows):
        name = random.choice(first_names)
        date_of_birth = generate_random_date_of_birth()
        age = random.randint(20, 99)
        data.append(Row(name=name, date_of_birth=date_of_birth, age=age))
    return data

# Function to generate a random date of birth within a specified range
def generate_random_date_of_birth():
    start_date = datetime(1998, 1, 1)
    end_date = datetime(1998, 12, 31)
    random_days = random.randint(0, (end_date - start_date).days)
    return (start_date + timedelta(days=random_days)).strftime("%Y-%m-%d")

# Create DataFrame with generated data and repartition it
df = spark.createDataFrame(GenerateData()).repartition(1)

# Display the first 10 records
df.show(10)

# Ignore warning for "The specified path does not exist."

# Define partitioning options for Iceberg format
opts = {
    "fanout-enabled": "true",
    "iceberg": {
        "partition":
            [
                {
                    "type": "bucket",
                    "column": "age",
                    "bucket_count": 2
                },
                {
                    "type": "identity",
                    "column": "name"
                },
                {
                    "type": "year",
                    "column": "date_of_birth"
                }
            ]
    }
}

# Save DataFrame to DataOS in Iceberg format with partitioning
save(name="dataos://icebase:pyflaresdk/test_write_02", dataframe=df, format="iceberg", mode="overwrite", options=opts)

# Load and display data from DataOS in Iceberg format
load(name="dataos://icebase:pyflaresdk/test_write_02", format="iceberg").show()

# Count the total number of records in the stored dataset
load(name="dataos://icebase:pyflaresdk/test_write_02", format="iceberg").count()

# Stop the Spark session
spark.stop()


```