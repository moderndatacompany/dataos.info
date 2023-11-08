# How to write data in Avro Format from Iceberg format using DataOS PyFlare?

```python

# Import necessary libraries
from pyspark.sql import Row
import random
from datetime import datetime, timedelta
from pyspark.sql.functions import col
from pyflare.sdk import load, save, session_builder

# Generate a random date of birth
def generate_random_date_of_birth():
    start_date = datetime(1998, 1, 1)
    end_date = datetime(1998, 12, 31)
    random_days = random.randint(0, (end_date - start_date).days)
    return (start_date + timedelta(days=random_days)).strftime("%Y-%m-%d")

# Generate random data records
def GenerateData():
    num_rows = random.randint(1000, 10000)
    first_names = ["Alice", "Bob", "Charlie", "David", "Emily", "Frank", "Grace", "Henry", "Ivy", "Jack", "Karen", "Leo",
                   "Mia", "Noah", "Olivia", "Peter", "Quinn", "Rachel", "Sam", "Tom", "Uma", "Victor", "Wendy", "Xander",
                   "Yvonne", "Zane"
                   ]

    data = []
    for _ in range(num_rows):
        name = random.choice(first_names)
        date_of_birth_str = generate_random_date_of_birth()
        date_of_birth_ts = datetime.strptime(date_of_birth_str, "%Y-%m-%d")
        age = random.randint(20, 99)
        data.append(Row(name=name, date_of_birth=date_of_birth_ts, age=age))
    return data

# Define Spark configuration
sparkConf = [
    ("spark.app.name", "Dataos Sdk Spark App"),  # Set the Spark application name
    ("spark.master", "local[*]"),  # Use local mode for Spark execution
]

# DataOS configuration
DATAOS_FQDN = "{{dataos fqdn}}"
token = "{{dataos apikey token}}"

# Create a Spark session with DataOS settings
spark = session_builder.SparkSessionBuilder(log_level = "INFO") \
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