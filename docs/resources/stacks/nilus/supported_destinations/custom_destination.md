# Custom Destination

Nilus includes different [Supported Destination](/resources/stacks/nilus/supported_destinations/), but you can also push data to **any target system** by implementing a **Custom Destination**.

Custom destinations let you:

* Send data to APIs, webhooks, queues, or proprietary systems.
* Control batching, serialization, retries, and error handling.
* Convert Nilus runtime batches (e.g., PyArrow / row-like structures) into JSON or other formats.
* Run post-load hooks for notifications, metrics, or cleanup.

> Place your destination files in a repository and reference them directly in your Nilus workflow (`repo` block + `sink.address: custom://<ClassName>`). Nilus will sync and execute your code.

!!! warning

        **Dependency Management for Custom Sources**

        * Only include **new dependencies** required by the custom source or destination.
        * Do **not** add libraries that are already part of the existing environment.
        * This prevents duplication and avoids version conflicts.

        **Pre-Installed Packages**

        The following packages are already included by default and should **NOT** be listed in `requirements.txt`:

        ??? note "Existing Packages"

            ```bash
                aiobotocore==2.21.1
                    # via s3fs
                aiohappyeyeballs==2.4.8
                    # via aiohttp
                aiohttp==3.11.15
                    # via
                    #   -r requirements.in
                    #   aiobotocore
                    #   facebook-business
                    #   gcsfs
                    #   s3fs
                aioitertools==0.12.0
                    # via aiobotocore
                aiosignal==1.3.2
                    # via aiohttp
                alembic==1.15.1
                    # via
                    #   databricks-sql-connector
                    #   sqlalchemy-spanner
                annotated-types==0.7.0
                    # via pydantic
                asana==3.2.3
                    # via -r requirements.in
                asn1crypto==1.5.1
                    # via snowflake-connector-python
                asynch==0.2.4
                    # via clickhouse-sqlalchemy
                attrs==25.1.0
                    # via
                    #   aiohttp
                    #   zeep
                backoff==2.2.1
                    # via rudder-sdk-python
                bcrypt==4.3.0
                    # via paramiko
                boto3==1.37.1
                    # via pyathena
                botocore==1.37.1
                    # via
                    #   aiobotocore
                    #   boto3
                    #   pyathena
                    #   s3transfer
                cachetools==5.5.2
                    # via google-auth
                certifi==2025.1.31
                    # via
                    #   clickhouse-connect
                    #   elastic-transport
                    #   influxdb-client
                    #   requests
                    #   smartsheet-python-sdk
                    #   snowflake-connector-python
                cffi==1.17.1
                    # via
                    #   cryptography
                    #   pynacl
                    #   snowflake-connector-python
                charset-normalizer==3.4.1
                    # via
                    #   requests
                    #   snowflake-connector-python
                ciso8601==2.3.2
                    # via asynch
                click==8.1.8
                    # via
                    #   dlt
                    #   typer
                clickhouse-connect==0.8.14
                    # via -r requirements.in
                clickhouse-driver==0.2.9
                    # via
                    #   -r requirements.in
                    #   clickhouse-sqlalchemy
                clickhouse-sqlalchemy==0.2.7
                    # via -r requirements.in
                confluent-kafka==2.8.0
                    # via -r requirements.in
                crate==2.0.0
                    # via sqlalchemy-cratedb
                cryptography==44.0.2
                    # via
                    #   paramiko
                    #   pyjwt
                    #   pyopenssl
                    #   snowflake-connector-python
                curlify==2.2.1
                    # via facebook-business
                databricks-sql-connector==2.9.3
                    # via -r requirements.in
                databricks-sqlalchemy==1.0.2
                    # via -r requirements.in
                dataclasses-json==0.6.7
                    # via -r requirements.in
                decorator==5.2.1
                    # via gcsfs
                deprecation==2.1.0
                    # via rudder-sdk-python
                #dlt==1.10.0
                dlt @ git+https://github.com/tmdc-io/dlt.git@iceberg/rest-catalog-support#egg=dlt
                    # via
                    #   -r requirements.in
                    #   dlt-cratedb
                dlt-cratedb==0.0.1
                    # via -r requirements.in
                dnspython==2.7.0
                    # via pymongo
                duckdb==1.2.1
                    # via
                    #   -r requirements.in
                    #   duckdb-engine
                duckdb-engine==0.17.0
                    # via -r requirements.in
                ecdsa==0.19.1
                    # via python-jose
                elastic-transport==8.17.1
                    # via elasticsearch
                elasticsearch==8.10.1
                    # via -r requirements.in
                enum-compat==0.0.3
                    # via intuit-oauth
                et-xmlfile==2.0.0
                    # via openpyxl
                facebook-business==23.0.0
                    # via -r requirements.in
                filelock==3.17.0
                    # via snowflake-connector-python
                flatten-json==0.1.14
                    # via -r requirements.in
                frozenlist==1.5.0
                    # via
                    #   aiohttp
                    #   aiosignal
                fsspec==2025.3.2
                    # via
                    #   dlt
                    #   gcsfs
                    #   pyathena
                    #   s3fs
                future==1.0.0
                    # via intuit-oauth
                gcsfs==2025.3.2
                    # via -r requirements.in
                geojson==3.2.0
                    # via sqlalchemy-cratedb
                gitdb==4.0.12
                    # via gitpython
                gitpython==3.1.44
                    # via dlt
                giturlparse==0.12.0
                    # via dlt
                google-ads==25.1.0
                    # via -r requirements.in
                google-analytics-data==0.18.17
                    # via -r requirements.in
                google-api-core==2.24.1
                    # via
                    #   google-ads
                    #   google-analytics-data
                    #   google-api-python-client
                    #   google-cloud-bigquery
                    #   google-cloud-bigquery-storage
                    #   google-cloud-core
                    #   google-cloud-spanner
                    #   google-cloud-storage
                    #   sqlalchemy-bigquery
                google-api-python-client==2.130.0
                    # via -r requirements.in
                google-auth==2.38.0
                    # via
                    #   gcsfs
                    #   google-analytics-data
                    #   google-api-core
                    #   google-api-python-client
                    #   google-auth-httplib2
                    #   google-auth-oauthlib
                    #   google-cloud-bigquery
                    #   google-cloud-core
                    #   google-cloud-storage
                    #   sqlalchemy-bigquery
                google-auth-httplib2==0.2.0
                    # via google-api-python-client
                google-auth-oauthlib==1.2.1
                    # via
                    #   gcsfs
                    #   google-ads
                google-cloud-bigquery==3.30.0
                    # via sqlalchemy-bigquery
                google-cloud-bigquery-storage==2.24.0
                    # via -r requirements.in
                google-cloud-core==2.4.2
                    # via
                    #   google-cloud-bigquery
                    #   google-cloud-spanner
                    #   google-cloud-storage
                google-cloud-spanner==3.54.0
                    # via
                    #   -r requirements.in
                    #   sqlalchemy-spanner
                google-cloud-storage==3.1.0
                    # via gcsfs
                google-crc32c==1.6.0
                    # via
                    #   google-cloud-storage
                    #   google-resumable-media
                google-resumable-media==2.7.2
                    # via
                    #   google-cloud-bigquery
                    #   google-cloud-storage
                googleapis-common-protos==1.69.0
                    # via
                    #   google-ads
                    #   google-api-core
                    #   grpc-google-iam-v1
                    #   grpcio-status
                grpc-google-iam-v1==0.14.2
                    # via google-cloud-spanner
                grpc-interceptor==0.15.4
                    # via google-cloud-spanner
                grpcio==1.70.0
                    # via
                    #   google-ads
                    #   google-api-core
                    #   googleapis-common-protos
                    #   grpc-google-iam-v1
                    #   grpc-interceptor
                    #   grpcio-status
                grpcio-status==1.62.3
                    # via
                    #   google-ads
                    #   google-api-core
                hdbcli==2.23.27
                    # via sqlalchemy-hana
                hexbytes==1.3.0
                    # via dlt
                httplib2==0.22.0
                    # via
                    #   google-api-python-client
                    #   google-auth-httplib2
                humanize==4.12.1
                    # via dlt
                ibm-db==3.2.6
                    # via
                    #   -r requirements.in
                    #   ibm-db-sa
                ibm-db-sa==0.4.1
                    # via -r requirements.in
                idna==3.10
                    # via
                    #   requests
                    #   snowflake-connector-python
                    #   yarl
                inflection==0.5.1
                    # via pyairtable
                influxdb-client==1.41.0
                    # via -r requirements.in
                intuit-oauth==1.2.4
                    # via python-quickbooks
                isodate==0.7.2
                    # via zeep
                jmespath==1.0.1
                    # via
                    #   aiobotocore
                    #   boto3
                    #   botocore
                jsonpath-ng==1.7.0
                    # via dlt
                leb128==1.0.8
                    # via asynch
                lxml==5.3.1
                    # via zeep
                lz4==4.4.3
                    # via
                    #   asynch
                    #   clickhouse-connect
                    #   databricks-sql-connector
                makefun==1.15.6
                    # via dlt
                mako==1.3.9
                    # via alembic
                markdown-it-py==3.0.0
                    # via rich
                markupsafe==3.0.2
                    # via mako
                marshmallow==3.26.1
                    # via dataclasses-json
                mdurl==0.1.2
                    # via markdown-it-py
                monotonic==1.6
                    # via rudder-sdk-python
                more-itertools==10.6.0
                    # via simple-salesforce
                multidict==6.1.0
                    # via
                    #   aiobotocore
                    #   aiohttp
                    #   yarl
                mypy-extensions==1.0.0
                    # via typing-inspect
                mysql-connector-python==9.2.0
                    # via -r requirements.in
                numpy==2.2.3
                    # via
                    #   databricks-sql-connector
                    #   pandas
                oauthlib==3.2.2
                    # via
                    #   databricks-sql-connector
                    #   requests-oauthlib
                openpyxl==3.1.5
                    # via databricks-sql-connector
                orjson==3.10.15
                    # via
                    #   crate
                    #   dlt
                packaging==24.2
                    # via
                    #   deprecation
                    #   dlt
                    #   duckdb-engine
                    #   google-cloud-bigquery
                    #   marshmallow
                    #   requirements-parser
                    #   snowflake-connector-python
                    #   sqlalchemy-bigquery
                    #   sqlalchemy-redshift
                pandas==2.2.3
                    # via databricks-sql-connector
                paramiko==3.5.1
                    # via -r requirements.in
                pathvalidate==3.2.3
                    # via dlt
                pendulum==3.0.0
                    # via
                    #   -r requirements.in
                    #   dlt
                platformdirs==4.3.6
                    # via
                    #   snowflake-connector-python
                    #   zeep
                pluggy==1.5.0
                    # via dlt
                ply==3.11
                    # via jsonpath-ng
                propcache==0.3.0
                    # via
                    #   aiohttp
                    #   yarl
                proto-plus==1.26.0
                    # via
                    #   google-ads
                    #   google-analytics-data
                    #   google-api-core
                    #   google-cloud-bigquery-storage
                    #   google-cloud-spanner
                protobuf==4.25.8
                    # via
                    #   google-ads
                    #   google-analytics-data
                    #   google-api-core
                    #   google-cloud-bigquery-storage
                    #   google-cloud-spanner
                    #   googleapis-common-protos
                    #   grpc-google-iam-v1
                    #   grpcio-status
                    #   proto-plus
                psutil==6.1.1
                    # via -r requirements.in
                psycopg2-binary==2.9.10
                    # via
                    #   -r requirements.in
                    #   dlt
                py-machineid==0.6.0
                    # via -r requirements.in
                pyairtable==2.3.3
                    # via -r requirements.in
                pyarrow==18.1.0
                    # via
                    #   -r requirements.in
                    #   databricks-sql-connector
                pyasn1==0.6.1
                    # via
                    #   pyasn1-modules
                    #   python-jose
                    #   rsa
                pyasn1-modules==0.4.1
                    # via google-auth
                pyathena==3.12.2
                    # via -r requirements.in
                pycountry==24.6.1
                    # via facebook-business
                pycparser==2.22
                    # via cffi
                pydantic==2.10.6
                    # via pyairtable
                pydantic-core==2.27.2
                    # via pydantic
                pygments==2.19.1
                    # via rich
                pyjwt==2.10.1
                    # via
                    #   simple-salesforce
                    #   snowflake-connector-python
                pymongo==4.11.1
                    # via -r requirements.in
                pymysql==1.1.1
                    # via -r requirements.in
                pynacl==1.5.0
                    # via paramiko
                pyopenssl==25.0.0
                    # via snowflake-connector-python
                pyparsing==3.2.1
                    # via httplib2
                pyrate-limiter==3.7.0
                    # via -r requirements.in
                python-dateutil==2.9.0.post0
                    # via
                    #   aiobotocore
                    #   botocore
                    #   google-cloud-bigquery
                    #   influxdb-client
                    #   pandas
                    #   pendulum
                    #   pyathena
                    #   python-quickbooks
                    #   rudder-sdk-python
                    #   smartsheet-python-sdk
                    #   time-machine
                python-dotenv==1.0.1
                    # via rudder-sdk-python
                python-jose==3.5.0
                    # via intuit-oauth
                python-quickbooks==0.9.2
                    # via -r requirements.in
                pytz==2025.1
                    # via
                    #   asynch
                    #   clickhouse-connect
                    #   clickhouse-driver
                    #   dlt
                    #   pandas
                    #   snowflake-connector-python
                    #   zeep
                pyyaml==6.0.2
                    # via
                    #   dlt
                    #   google-ads
                rauth==0.7.3
                    # via python-quickbooks
                reactivex==4.0.4
                    # via influxdb-client
                requests==2.32.4
                    # via
                    #   asana
                    #   clickhouse-sqlalchemy
                    #   curlify
                    #   databricks-sql-connector
                    #   dlt
                    #   facebook-business
                    #   gcsfs
                    #   google-api-core
                    #   google-cloud-bigquery
                    #   google-cloud-storage
                    #   intuit-oauth
                    #   pyairtable
                    #   python-quickbooks
                    #   rauth
                    #   requests-file
                    #   requests-oauthlib
                    #   requests-toolbelt
                    #   rudder-sdk-python
                    #   simple-salesforce
                    #   smartsheet-python-sdk
                    #   snowflake-connector-python
                    #   stripe
                    #   zeep
                requests-file==2.1.0
                    # via zeep
                requests-oauthlib==1.3.1
                    # via
                    #   asana
                    #   google-auth-oauthlib
                    #   intuit-oauth
                requests-toolbelt==1.0.0
                    # via
                    #   smartsheet-python-sdk
                    #   zeep
                requirements-parser==0.11.0
                    # via dlt
                rich==13.9.4
                    # via
                    #   -r requirements.in
                    #   rich-argparse
                    #   typer
                rich-argparse==1.7.0
                    # via dlt
                rsa==4.9
                    # via
                    #   google-auth
                    #   python-jose
                rudder-sdk-python==2.1.4
                    # via -r requirements.in
                s3fs==2025.3.2
                    # via -r requirements.in
                s3transfer==0.11.3
                    # via boto3
                semver==3.0.4
                    # via dlt
                setuptools==78.1.1
                    # via
                    #   dlt
                    #   influxdb-client
                    #   python-quickbooks
                    #   types-setuptools
                shellingham==1.5.4
                    # via typer
                simple-salesforce==1.12.6
                    # via -r requirements.in
                simplejson==3.20.1
                    # via
                    #   dlt
                    #   python-quickbooks
                six==1.17.0
                    # via
                    #   ecdsa
                    #   facebook-business
                    #   flatten-json
                    #   intuit-oauth
                    #   python-dateutil
                    #   python-quickbooks
                    #   smartsheet-python-sdk
                    #   thrift
                smartsheet-python-sdk==3.0.5
                    # via -r requirements.in
                smmap==5.0.2
                    # via gitdb
                snowflake-connector-python==3.14.0
                    # via snowflake-sqlalchemy
                snowflake-sqlalchemy==1.6.1
                    # via -r requirements.in
                sortedcontainers==2.4.0
                    # via snowflake-connector-python
                sqlalchemy==1.4.52
                    # via
                    #   -r requirements.in
                    #   alembic
                    #   clickhouse-sqlalchemy
                    #   databricks-sql-connector
                    #   databricks-sqlalchemy
                    #   duckdb-engine
                    #   ibm-db-sa
                    #   snowflake-sqlalchemy
                    #   sqlalchemy-bigquery
                    #   sqlalchemy-cratedb
                    #   sqlalchemy-hana
                    #   sqlalchemy-redshift
                    #   sqlalchemy-spanner
                sqlalchemy-bigquery==1.12.1
                    # via -r requirements.in
                sqlalchemy-cratedb==0.41.0
                    # via -r requirements.in
                sqlalchemy-hana==2.0.0
                    # via -r requirements.in
                sqlalchemy-redshift==0.8.14
                    # via -r requirements.in
                sqlalchemy-spanner==1.11.0
                    # via -r requirements.in
                sqlalchemy2-stubs==0.0.2a38
                    # via -r requirements.in
                sqlglot==26.12.1
                    # via dlt
                sqlparse==0.5.3
                    # via google-cloud-spanner
                stripe==10.7.0
                    # via -r requirements.in
                tenacity==9.0.0
                    # via
                    #   dlt
                    #   pyathena
                thrift==0.16.0
                    # via databricks-sql-connector
                time-machine==2.16.0
                    # via pendulum
                tomlkit==0.13.2
                    # via
                    #   dlt
                    #   snowflake-connector-python
                tqdm==4.67.1
                    # via -r requirements.in
                typer==0.13.1
                    # via -r requirements.in
                types-requests==2.32.0.20240907
                    # via -r requirements.in
                types-setuptools==78.1.0.20250329
                    # via requirements-parser
                typing-extensions==4.12.2
                    # via
                    #   alembic
                    #   dlt
                    #   pyairtable
                    #   pydantic
                    #   pydantic-core
                    #   pyopenssl
                    #   reactivex
                    #   simple-salesforce
                    #   snowflake-connector-python
                    #   sqlalchemy2-stubs
                    #   stripe
                    #   typer
                    #   typing-inspect
                typing-inspect==0.9.0
                    # via dataclasses-json
                tzdata==2025.1
                    # via
                    #   dlt
                    #   pandas
                    #   pendulum
                tzlocal==5.3
                    # via
                    #   asynch
                    #   clickhouse-driver
                uritemplate==4.1.1
                    # via google-api-python-client
                urllib3==2.5.0
                    # via
                    #   botocore
                    #   clickhouse-connect
                    #   crate
                    #   databricks-sql-connector
                    #   elastic-transport
                    #   influxdb-client
                    #   pyairtable
                    #   requests
                    #   types-requests
                verlib2==0.2.0
                    # via
                    #   crate
                    #   sqlalchemy-cratedb
                wrapt==1.17.2
                    # via aiobotocore
                yarl==1.18.3
                    # via aiohttp
                zeep==4.3.1
                    # via simple-salesforce
                zstandard==0.23.0
                    # via clickhouse-connect
                zstd==1.5.6.5
                    # via
                    #   -r requirements.in
                    #   asynch

                # Nilus Added packeges
                adlfs==2024.12.0
                azure-core==1.33.0
                azure-datalake-store==0.0.53
                azure-identity==1.21.0
                azure-storage-blob==12.25.1

                jsonschema
                jproperties
                    # to read java properties file and write
                dataos-sdk-py==0.0.6
                    # dataos-sdk
                db-dtypes==1.4.2
                databricks-sdk==0.50.0
                nats-py==2.9.0
                flatten_json==0.1.14
                PyYaml
                pyiceberg==0.9.0
                pyjnius==1.6.1
                    # for java interaction
                prometheus-client==0.21.1
                fastapi==0.116.1
                uvicorn[standard]==0.34.2
                sqlalchemy-trino==0.5.0
                nkeys==0.2.1
                pydantic-settings==2.10.1
                pyiceberg-core==0.6.0

                # Custom Soda packages with Presidio integration for profile source
                soda-core @ git+https://github.com/tmdc-io/soda-understand.git@feature/presidio-soda-integration#subdirectory=soda/core
                soda-core-postgres @ git+https://github.com/tmdc-io/soda-understand.git@feature/presidio-soda-integration#subdirectory=soda/postgres
                soda-core-bigquery @ git+https://github.com/tmdc-io/soda-understand.git@feature/presidio-soda-integration#subdirectory=soda/bigquery
                soda-core-snowflake @ git+https://github.com/tmdc-io/soda-understand.git@feature/presidio-soda-integration#subdirectory=soda/snowflake

                presidio_analyzer==2.2.359
                presidio_structured==0.0.6

                # Security vulnerability fixes for transitive dependencies
                starlette==0.47.2  # CVE-2025-54121 (MEDIUM)
            ```




## Key Components

1. **Destination Function (`@nilus.destination`)**

   Receives a batch (`items`) and table metadata (`table`), transforms it, and sends it to your system.

2. **Wrapper Class (`CustomDestination`)**

   Defines which function Nilus should call and how run parameters (dataset/table names) are passed.

3. **Serialization**

   Normalizes PyArrow mixed Python types into a safe format such as JSON.

4. **Configuration**

   Point `sink.address` at your custom class and set `dest-table` in `sink.options`.

## Base Class Pattern

A typical custom destination wrapper looks like this:

```python
from nilus import CustomDestination

class MyCustomDestination(CustomDestination):
    """Custom destination wiring for Nilus."""

    def nilus_dest(self, uri: str, **kwargs):
        """Return the destination function to run."""
        return my_destination_func

    def nilus_run_params(self, uri: str, table: str, **kwargs):
        """Return run parameters (dataset/table names)."""
        parts = table.split(".")
        if len(parts) == 2:
            return {"dataset_name": parts[0], "table_name": parts[1]}
        return {"dataset_name": "default", "table_name": table}

    def post_load(self) -> None:
        """Optional hook after a successful load."""
        pass
```

## Destination Function Pattern

The destination function **delivers batches** to your system:

```python
import nilus
from typing import Any, Dict, List
import datetime, decimal, uuid, json, requests

# JSON serialization helper
def json_serializer(obj):
    if isinstance(obj, (datetime.datetime, datetime.date, datetime.time)):
        return obj.isoformat()
    if isinstance(obj, datetime.timedelta):
        return str(obj)
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    if isinstance(obj, uuid.UUID):
        return str(obj)
    if hasattr(obj, "as_py"):  # PyArrow scalar
        return obj.as_py()
    if hasattr(obj, "__dict__"):
        return obj.__dict__
    raise TypeError(f"Not JSON serializable: {type(obj)}")

# Convert Nilus batches to JSON-safe dicts
def convert_pyarrow_to_json(items) -> List[Dict[str, Any]]:
    if hasattr(items, "to_pylist"):          # PyArrow Table/RecordBatch
        return items.to_pylist()
    if isinstance(items, (list, tuple)):     # Iterable of rows
        out = []
        for row in items:
            if hasattr(row, "to_pydict"):
                out.append(row.to_pydict())
            elif isinstance(row, dict):
                norm = {}
                for k, v in row.items():
                    if hasattr(v, "as_py"):
                        v = v.as_py()
                    if isinstance(v, (datetime.datetime, datetime.date, datetime.time)):
                        v = v.isoformat()
                    elif isinstance(v, decimal.Decimal):
                        v = float(v)
                    elif isinstance(v, uuid.UUID):
                        v = str(v)
                    norm[k] = v
                out.append(norm)
            else:
                out.append(row)
        return out
    try:
        return list(items)
    except Exception:
        return []

# Example destination
@nilus.destination
def my_destination_func(items, table):
    table_name = table.get("name", "unknown")
    records = convert_pyarrow_to_json(items)
    if not records:
        return

    payload = {
        "table": table_name,
        "data": records,
        "metadata": {
            "count": len(records),
            "timestamp": datetime.datetime.now().isoformat(),
        },
    }

    body = json.dumps(payload, default=json_serializer)
    resp = requests.post(
        "https://your-api.example.com/ingest",
        data=body,
        headers={"Content-Type": "application/json"},
        timeout=30,
    )
    resp.raise_for_status()
```

## Example Implementations

Here's a streamlined guide to help you implement custom destination for user-defined connectors effectively.



**Step 1: Webhook Destination (simple batched POST)**

```python
@nilus.destination
def webhook_destination_func(items, table):
    table_name = table.get("name", "unknown")
    records = convert_pyarrow_to_json(items)
    if not records:
        return

    payload = {"table": table_name, "data": records, "timestamp": datetime.datetime.now().isoformat()}
    resp = requests.post(
        "https://webhook.site/your-endpoint",
        data=json.dumps(payload, default=json_serializer),
        headers={"Content-Type": "application/json"},
        timeout=30,
    )
    resp.raise_for_status()
    print(f"✅ Sent {len(records)} records to {table_name}")

class WebhookDestination(CustomDestination):
    def nilus_dest(self, uri: str, **kwargs):
        return webhook_destination_func
    def nilus_run_params(self, uri: str, table: str, **kwargs):
        return {"table_name": table}
    def post_load(self) -> None:
        pass
```



**Step 2: API Destination (with Nilus load metadata)**

```python
@nilus.destination
def api_destination_func(items, table):
    table_name = table.get("name", "unknown")
    records = convert_pyarrow_to_json(items)
    if not records:
        print(f"📭 No items to send for table {table_name}")
        return

    payload = {
        "table": table_name,
        "data": records,
        "schema": table.get("columns", {}),
        "metadata": {
            "load_id": records[0].get("_dlt_load_id") if records else None,
            "item_count": len(records),
            "data_type": "json_converted_from_pyarrow",
            "timestamp": datetime.datetime.now().isoformat(),
        },
    }

    body = json.dumps(payload, default=json_serializer)
    resp = requests.post(
        "http://0.0.0.0:7654/webhook",
        data=body,
        headers={"Content-Type": "application/json"},
        timeout=30,
    )
    resp.raise_for_status()
    print(f"✅ API destination sent {len(records)} items for {table_name}")

class ApiDestination(CustomDestination):
    def nilus_dest(self, uri: str, **kwargs):
        return api_destination_func
    def nilus_run_params(self, uri: str, table: str, **kwargs):
        parts = table.split(".")
        if len(parts) == 2:
            return {"dataset_name": parts[0], "table_name": parts[1]}
        return {"dataset_name": "default", "table_name": table}
    def post_load(self) -> None:
        pass
```





**Step 3: Local Test Webhook Server (optional helper)**

```python
# dummy_server.py
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import datetime

app = FastAPI(title="Test Webhook Server", version="1.0.0")
received_data = []

@app.post("/{path:path}")
async def catch_all_post(path: str, request: Request):
    try:
        body = await request.body()
        try:
            json_data = await request.json()
        except:
            json_data = None

        received_data.append({
            "timestamp": datetime.datetime.now().isoformat(),
            "path": f"/{path}",
            "headers": dict(request.headers),
            "body_size": len(body),
            "json_data": json_data,
        })
        return JSONResponse(status_code=200, content={"status": "success"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": "error", "message": str(e)})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7654)
```





## Deployment Configuration 

After creating the source files for your custom destination, deploy them using the Workflow as follows:

### **Repository Structure**

Custom destination must follow a standard Python package layout:

```bash
my-custom-destinations/
├── __init__.py
├── api_destination.py            # destination function + helpers
├── nilus_custom_destination.py   # CustomDestination wrapper
└── utils.py                      # optional shared helpers
```

### **Workflow Configuration**

To deploy the custom source, reference the repository in a Nilus Workflow:

```yaml
repo:
  url: "https://github.com/your-repo"
  syncFlags:
    - "--ref=main"
  baseDir: "examples/custom_destination"

source:
  address: postgresql://user:pass@localhost:5432/db
  options:
    source-table: "public.users"

sink:
  address: custom://ApiDestination   # must match class name
  options:
    dest-table: "processed.users"
    incremental-strategy: append
```

### **Data Processing Notes**

* `items` can be a PyArrow `Table`/`RecordBatch` or iterable of rows.
* `table` contains metadata (e.g., `name`, `columns`).
* Nilus load metadata fields (e.g., `_dlt_load_id`) may appear in rows.
* Use `convert_pyarrow_to_json` and `json_serializer` for safe type conversion.

## Best Practices

1. **Error Handling**
     1. Raise errors for HTTP/driver issues and implement retry/backoff mechanisms for transient failures.
     2. Log response codes and handle partial failures appropriately.
     3. Ensure protection against processing empty batches.
2. **Batching & Throughput**
     1. Break down large payloads into smaller chunks (e.g., 500-5,000 records per request).
     2. Reuse HTTP sessions or SDK clients.
     3. Follow the downstream rate limits.
3. **Serialization**
     1. Normalize timestamps to ISO-8601 format.
     2. Convert decimal values to strings or floats according to your target schema.
     3. Ensure keys and values are sanitized to meet API requirements.
4. **Security**
     1. Store secrets in environment variables or instance secrets; avoid hardcoding.
     2. Utilize HTTPS/TLS for all network communications.
     3. Refrain from logging sensitive information.
5. **Observability**
     1. Track the number of records sent, number of batches processed, and retry attempts.
     2. Monitor latency and error rates.
     3. Include correlation IDs (load_id, table_name) for tracing purposes.

### **Quick Checklist**

Ensure you verify the following when creating a custom destination:

* Destination function created with `@nilus.destination`.
* `CustomDestination` subclass implemented.
* Workflow uses `sink.address: custom://<ClassName>`.
* Secrets configured via environment / Instance Secrets.
* (Optional) Local webhook server tested.

