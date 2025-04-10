# Snowflake Operations with DataOS PyFlare

This example outlines the process of reading data from a Snowflake table and writing it to a DataOS Iceberg table using PyFlare. The workflow includes Spark session initialization, data loading from Snowflake, and writing to a DataOS-compatible storage format.

## Prerequisites

Ensure the following dependencies and configurations are available before executing the samples:

- DataOS FQDN (Fully Qualified Domain Name)
- User API Token
- SparkSession with appropriate configurations
- Access to the Lakehouse Depot
- Access to the Snowflake Depot


```python
# Import required libraries
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyflare.sdk import load, save, session_builder

# Define the DataOS Fully Qualified Domain Name (FQDN)
# Replace this with the actual FQDN of the DataOS environment
DATAOS_FQDN = "example-dataos.dataos.app"

# Define the authentication token
# Replace with a valid DataOS API key
token = "<your_auth_token>"

# Define Spark configuration settings
sparkConf = [
    ("spark.app.name", "Pyflare App"),
    ("spark.master", "local[*]"),
]

# Build the Spark session using PyFlare's session builder
# Ensure that depot names are accessible in the specified environment
spark = session_builder.SparkSessionBuilder(log_level="INFO") \
    .with_spark_conf(sparkConf) \
    .with_user_apikey(token) \
    .with_dataos_fqdn(DATAOS_FQDN) \
    .with_depot(depot_name="sfdepot01", acl="rw") \
    .with_depot(depot_name="lakehouse", acl='rw') \
    .build_session()

# Load data from the Snowflake table using PyFlare
# The URI format is: dataos://<depot_name>:<schema>/<table>
df_sf = load(name="dataos://sfdepot01:PUBLIC/product", format="snowflake")

# Display the first 10 records from the loaded DataFrame
df_sf.show(10)

# Persist the DataFrame to a DataOS-compatible Iceberg table
# Change the path and format as necessary
save(name="dataos://lakehouse:sandbox3/test_pyflare2", dataframe=df_sf, format="iceberg", mode="overwrite")

# Stop the Spark session to release resources
spark.stop()
```

<aside class="best-practice" style="border-left: 4px solid #28a745; background-color: #e6f4ea; color: #1e4620; padding: 1rem; border-radius: 0.5rem; margin: 1rem 0;">
<b>Note:</b> Replace all placeholder values such as the authentication token, `DATAOS_FQDN`, and depot names according to the target environment.
</aside>

**Important Placeholder Changes Required:**

- **`DATAOS_FQDN`**: Replace `"example-dataos.dataos.app"` with the actual FQDN of the target DataOS instance.
- **`token`**: Replace with a valid DataOS API key.
- **`depot_name` in `.with_depot(...)`**: Confirm that the depots (e.g., `"sfdepot01"`, `"lakehouse"`) exist and have proper permissions.
- **`load(...)` and `save(...)` URIs**: Replace the schema, table, and output path values to match the required source and target datasets.