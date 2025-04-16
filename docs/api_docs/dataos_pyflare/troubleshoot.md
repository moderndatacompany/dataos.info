# Troubleshooting in DataOS PyFlare
This section outlines common errors encountered while using the DataOS PyFlare SDK and provides actionable steps to diagnose and resolve these issues effectively.

## FQDN Resolution Failure

**Error Message:**
```plaintext
ConnectionError: HTTPSConnectionPool(host='example-training.dataos.app', port=443): Max retries exceeded with url...
```

**Cause:**  
This error indicates that the fully qualified domain name (FQDN) is incorrect or cannot be resolved by the system.

**Solution:**  
Ensure the `DATAOS_FQDN` is set to the correct domain.

```python
DATAOS_FQDN = "example-training.dataos.app"
```

Confirm that the hostname is valid and resolvable from your network.

## Unauthorized Access to Depot Metadata

**Error Message:**
```plaintext
HTTPError: Something went wrong in depot metadata API for depot: lakehouse with status code: 401
```

**Cause:**  
An invalid or missing API key or token is being used.

**Solution:**  
Verify and provide the correct API key or token with appropriate permissions. 
The apikey `token` can be obtained by executing the following command on the CLI:

```bash
dataos-ctl user apikey get

# Expected Output
INFO[0000] 🔑 user apikey get...                         
INFO[0000] 🔑 user apikey get...complete                 

                                                   TOKEN                                                   │  TYPE  │        EXPIRATION         │                   NAME                     
───────────────────────────────────────────────────────────────────────────────────────────────────────────┼────────┼───────────────────────────┼────────────────────────────────────────────
  dG9rZW5faG9wZWZ1bGx5X2xvdWRsedHJpa2luZ19uZXd0LmFiMzAyMTdjLTExYzAtNDg2Yi1iZjEyLWJkMjY1ZWM2YzgwOA==     │ apikey │ 2025-04-13T05:30:00+05:30 │ token_hopefully_loudly_striking_newt       
  dG9rZW5fdGlnaHRseV9uZWVkbGVzcX2xpYmVyYWxfcGFuZ29saW4uNTY0ZDc4ZTQtNWNhMy00YjI1LWFkNWMtYmFlMTcwYTM5MWU1 │ apikey │ 2025-04-11T05:30:00+05:30 │ token_tightly_needlessly_liberal_pangolin  
```
If there are no apikey's present, create a new one by using the `create` command as shown below:

```bash
dataos-ctl user apikey create
```

## Depot Not Loaded or Invalid Dataset

**Error Message:**
```plaintext
PyflareReadException: Check if dataset dataos://lakehouse:sandbox3/test_pyflare2 exists and you have read access...
InvalidInputException: Depot not loaded in current session
```

**Cause:**  
The required depot is not included in the Spark session, or the dataset does not exist.

**Solution:**  
Ensure that the depot is correctly configured in the session:

```python
spark = session_builder.SparkSessionBuilder(log_level="INFO") \
    .with_spark_conf(sparkConf) \
    .with_user_apikey(token) \
    .with_dataos_fqdn(DATAOS_FQDN) \
    .with_depot(depot_name="icebase", acl="rw") \
    .build_session()

load(name="dataos://lakehouse:sandbox3/test_pyflare2", format="iceberg").show()
```

If using multiple depots, include all of them in the session:

```python
spark = session_builder.SparkSessionBuilder(log_level="INFO") \
    .with_spark_conf(sparkConf) \
    .with_user_apikey(token) \
    .with_dataos_fqdn(DATAOS_FQDN) \
    .with_depot(depot_name="sfdepot01", acl="rw") \
    .with_depot(depot_name="bigquerydepot", acl="rw") \
    .with_depot(depot_name="lakehouse", acl="rw") \
    .build_session()
```

## Incorrect Dataset Format

**Code Example:**
```python
load(name="dataos://lakehouse:sandbox3/test_pyflare2", format="snowflake").show()
```

**Error Message:**
```plaintext
IllegalArgumentException: A snowflake URL must be provided with 'sfurl' parameter...
```

**Cause:**  
The format specified does not match the actual format of the dataset. In this case, the dataset is stored in Iceberg format but `snowflake` is specified incorrectly.

**Solution:**  
Use the correct format based on the dataset's storage type:

```python
load(name="dataos://lakehouse:sandbox3/test_pyflare2", format="iceberg").show()
```
