# BigQuery Transformation with DataOS PyFlare

This example demonstrates how to read data from a BigQuery table and write it to a DataOS Iceberg table using PyFlare. The steps include session setup, data loading, and data persistence. The entire process is conducted within a PySpark environment configured for use with the DataOS platform.

## Prerequisites

Ensure the following dependencies and configurations are available before executing the samples:

- DataOS FQDN (Fully Qualified Domain Name)
- User API Token
- SparkSession with appropriate configurations
- Access to the Lakehouse Depot
- Access to the BigQuery Depot

```python
# Import required libraries
from pyspark.sql import SparkSession
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
    .with_depot(depot_name="bigquerydepot", acl="rw") \
    .with_depot(depot_name="lakehouse", acl='rw') \
    .build_session()

# Load data from the BigQuery table using PyFlare
# The URI format is: dataos://<depot_name>:<database>/<table>
df_bq = load(name="dataos://bigquerydepot:creditcard/credit_card_details", format="bigquery")

# Display the first 10 records from the loaded DataFrame
df_bq.show(10)

# Persist the DataFrame to a DataOS-compatible Iceberg table
# Change the path and format as necessary
save(name="dataos://lakehouse:sandbox3/test_pyflare2", dataframe=df_bq, format="iceberg", mode="overwrite")

# Stop the Spark session to release resources
spark.stop()
```
!!! success "Note"
    
    Replace all placeholder values such as the authentication token, `DATAOS_FQDN`, and depot names according to the target environment.

    **Important Placeholder Changes Required:**

    - **`DATAOS_FQDN`**: Replace `example-dataos.dataos.app` with the actual FQDN of the target DataOS instance.
    - **`token`**: Replace with a valid DataOS API key.
    - **`depot_name` in `.with_depot(...)`**: Confirm that the depots (e.g., `bigquerydepot`, `lakehouse`) exist and have proper permissions.
    - **`load(...)` and `save(...)` URIs**: Replace the table and path values to match the desired source and target datasets.


# Additional links 

- [How to perform Merge into transformation in pyflare ?](/api_docs/dataos_pyflare/code_samples/lakehouse_pyflare/#merge-into-iceberg-table)
- [How can the "FQDN Resolution Failure" error be resolved in DataOS PyFlare SDK?](/api_docs/dataos_pyflare/troubleshoot/#fqdn-resolution-failure)
- [What causes the "Unauthorized Access to Depot Metadata" error in DataOS PyFlare SDK and how can it be fixed?](/api_docs/dataos_pyflare/troubleshoot/#unauthorized-access-to-depot-metadata)