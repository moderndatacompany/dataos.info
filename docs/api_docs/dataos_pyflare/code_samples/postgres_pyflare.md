# Postgres Transformation with DataOS PyFlare

This example provides a complete process for reading data from a PostgreSQL table and writing it to a DataOS Iceberg table using PyFlare. The procedure includes Spark session setup, data retrieval from PostgreSQL, and persistence to DataOS storage.

## Prerequisites

Ensure the following dependencies and configurations are available before executing the samples:

- DataOS FQDN (Fully Qualified Domain Name)
- User API Token
- SparkSession with appropriate configurations
- Access to the Lakehouse Depot
- Access to the Postgres Depot


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
    .with_depot(depot_name="postgres", acl="rw") \
    .with_depot(depot_name="lakehouse", acl='rw') \
    .build_session()

# Load data from the PostgreSQL table using PyFlare
# The URI format is: dataos://<depot_name>:<schema>/<table>
df_pg = load(name="dataos://postgres:public/marketing_data", format="postgresql")

# Display the first 10 records from the loaded DataFrame
df_pg.show(10)

# Persist the DataFrame to a DataOS-compatible Iceberg table
# Change the path and format as necessary
save(name="dataos://lakehouse:sandbox3/test_pyflare2", dataframe=df_pg, format="iceberg", mode="overwrite")

# Stop the Spark session to release resources
spark.stop()
```

!!! success "Note"

        Replace all placeholder values such as the authentication token, `DATAOS_FQDN`, and depot names according to the target environment.

        **Important Placeholder Changes Required:**

        - **`DATAOS_FQDN`**: Replace `example-dataos.dataos.app` with the actual FQDN of the target DataOS instance.
        - **`token`**: Replace with a valid DataOS API key.
        - **`depot_name` in `.with_depot(...)`**: Ensure the depots (e.g., `postgres`, `lakehouse`) exist and are accessible.
        - **`load(...)` and `save(...)` URIs**: Update the schema, table name, and output path to match the intended source and destination datasets.


# Additional links

- [How can the "Depot Not Loaded or Invalid Dataset" error be troubleshot in DataOS PyFlare SDK?](/api_docs/dataos_pyflare/troubleshoot/#depot-not-loaded-or-invalid-dataset)
- [What should be done if an "Incorrect Dataset Format" error is encountered in DataOS PyFlare SDK?](/api_docs/dataos_pyflare/troubleshoot/#incorrect-dataset-format)
- [How to perform Merge into transformation in pyflare ?](/api_docs/dataos_pyflare/code_samples/lakehouse_pyflare/#merge-into-iceberg-table)