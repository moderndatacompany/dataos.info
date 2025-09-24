---
description: >-
  This guide provides instructions for implementing, configuring, and deploying
  Custom Sources.
---

# Custom Source

Nilus includes a growing collection of built-in connectors for commonly used databases, APIs, and platforms. For data sources that are not natively supported, integration is enabled through **Custom Sources**.

Custom Sources allow the development of **user-defined connectors** while utilizing Nilus infrastructure for orchestration, incremental data loading, and movement into the DataOS Lakehouse or other [Supported Destinations](/resources/stacks/nilus/supported_destinations/).

## Implementation Overview of Custom Sources

1. **Custom Sources** are used to extend the Nilus platform with additional connectors.
2. A Custom Source is implemented by subclassing the `CustomSource` class and defining one or more **resources**.
3. In Custom Sources, configuration and parameterization are handled through **URI-based connection strings**.
4. Incremental loading is also supported in the Custom Sources when state tracking is enabled within the connector.
5. Custom sources are deployed by referring to the custom source repository within a Nilus workflow.

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




## Implementation Guide

Here's a streamlined guide to help you implement custom sources for user-defined connectors effectively.



**Step 1: Base Class Requirements**

All custom sources must subclass the `CustomSource` base class:

```python
from nilus import CustomSource

class MyCustomSource(CustomSource):
    def handles_incrementality(self) -> bool:
        return False

    def nilus_source(self, uri: str, table: str, **kwargs):
        return my_source_function(uri, table, **kwargs)
```

* `handles_incrementality()`: Returns `True` If
* &#x20;The connector supports incremental loading.
* `nilus_source()`: Defines the entry point Nilus will invoke during execution.



**Step 2: Resource Definition**

Resources represent discrete data-fetching operations. Each resource must be defined as a Python generator function and registered using Nilus decorators:

```python
import nilus

@nilus.resource()
def fetch_data():
    for item in data:
        yield item

@nilus.source
def my_source_function(uri, table, **kwargs):
    return fetch_data()
```

* `@nilus.resource()`: Used to annotate resource functions.
* `@nilus.source`: Used to register the source entry point.
* Resource functions must yield one item at a time.



**Step 3: URI and Parameter Handling**

Nilus uses URI-based connection strings to configure custom sources. Parameters can be passed using standard query syntax:

```yaml
custom://MyCustomSource?param1=value1&param2=value2
```

To extract parameters:

```python
from urllib.parse import urlparse, parse_qs

def nilus_source(self, uri: str, table: str, **kwargs):
    parsed_uri = urlparse(uri)
    params = parse_qs(parsed_uri.query)

    return my_source_function(
        uri=uri,
        table=table,
        param1=params.get("param1", [None])[0],
        param2=params.get("param2", [None])[0],
        **kwargs
    )
```



**Step 4: Incremental Loading**

To support incremental data extraction, state tracking must be implemented. Nilus persists resource state between runs:

```python
class MyIncrementalSource(CustomSource):
    def handles_incrementality(self) -> bool:
        return True

    @nilus.resource()
    def fetch_incremental_data(last_processed_id=None):
        state = nilus.current.resource_state()
        last_id = state.get("last_id", last_processed_id)

        data = get_data_after_id(last_id)
        if data:
            state["last_id"] = data[-1]["id"]

        for item in data:
            yield item
```



**Step 5: Error Handling**

Connection and data-fetching errors must be handled explicitly to ensure reliability:

!!! info
    If `table_name` is not defined in the `@nilus.resource` decorator; it defaults to the function name. Check the Example Implementations section below for more details.


    <pre class="language-python"><code class="lang-python"><strong>@nilus.resource()
    </strong>def fetch_data_with_error_handling():
    try:
        conn = establish_connection()
        try:
            data = conn.get_data()
            for item in data:
                yield item
        finally:
            conn.close()
    except Exception as e:
        logger.error(f"Error fetching data: {str(e)}")
        raise
    </code></pre>



    **Step 6: Performance Optimization**

    For large datasets, batching and pagination must be implemented to ensure efficiency:

```python
@nilus.resource()
def fetch_large_dataset(batch_size=1000):
    page = 1
    has_more = True

    while has_more:
        data, has_more = get_paginated_data(page=page, size=batch_size)
        for item in data:
            yield item
        page += 1
```



## Deployment Configuration

After creating the source files for your custom sources, deploy them using the Workflow as follows:

### **Repository Structure**

Custom sources must follow a standard Python package layout:

```yaml
my-custom-sources/
├── __init__.py
├── source1.py
├── source2.py
└── utils.py
```

### **Workflow Configuration**

To deploy the custom source, reference the repository in a Nilus Workflow:

```yaml
repo:
  url: "https://github.com/your-repo"
  syncFlags:
    - "--ref=main"
  baseDir: "my-custom-sources"

source:
  address: custom://MyCustomSource?param1=value1
  options:
    source-table: "my_data"

sink:
  address: dataos://lakehouse
  options:
    incremental-strategy: append
    dest-table: "raw"
```

## Example Implementations

The following examples illustrate various methods for creating custom sources in Nilus. Each example shows how resources and sources can be defined for specific use cases.

1.  **Static Source**

    This example produces a small, fixed dataset.

    ```python
    @nilus.resource()
    def fetch_random_users():
        for d in [{"id": 1, "name": "Alice"}]:
            yield d

    @nilus.source
    def random_user_source(uri, table, **kwargs):
        return fetch_random_users()
    ```

    * **`fetch_random_users`**: Defines a resource that yields static data.
    * **`random_user_source`**: Registers the entry point Nilus uses to execute the resource.

2. **API Integration**

    This example shows how to fetch data from an external API.

    ```python
    @nilus.resource()
    def fetch_api_data(api_url, api_key, endpoint):
        headers = {"Authorization": f"Bearer {api_key}"}
        data = requests.get(f"{api_url}/{endpoint}", headers=headers).json()
        for item in data:
            yield item
    ```

    * API parameters (`api_url`, `api_key`, `endpoint`) are passed into the function.
    * The API response is iterated, and each record is yielded individually.

3. **Multi-Resource Source**
    This example defines multiple resources within a single source.

    ```python
    @nilus.resource(write_disposition="replace")
    def users():
        yield from fetch_users()

    @nilus.resource(write_disposition="append")
    def activities():
        yield from fetch_activities()

    @nilus.source
    def multi_resource_source(uri, table, **kwargs):
        return users(), activities()
    ```

    * **Users resource**: Produces user records and replaces existing data.
    * **Activities resource**: Produces activity records and appends them to existing data.
    * **multi_resource_source**: Groups both resources so Nilus can run them together.

### **Creating a Random User Custom Source**

This example shows how to implement a custom source that returns a static dataset of random users. It illustrates how to separate resource logic from the `CustomSource` implementation.

**`random_users.py`**

```python
import nilus

# Dummy static dataset
dummy_data = [
  {
    "gender": "female",
    "name": {"title": "Ms", "first": "Aisha", "last": "Patel"},
    "location": {
      "city": "Bengaluru",
      "state": "Karnataka",
      "country": "India"
    },
    "email": "aisha.patel@example.com",
    "dob": {"date": "1988-04-12T10:15:30.000Z", "age": 36},
    "phone": "080-12345678"
  },
  {
    "gender": "male",
    "name": {"title": "Mr", "first": "Rahul", "last": "Sharma"},
    "location": {
      "city": "Mumbai",
      "state": "Maharashtra",
      "country": "India"
    },
    "email": "rahul.sharma@example.com",
    "dob": {"date": "1992-11-05T08:05:10.000Z", "age": 32},
    "phone": "022-23456789"
  },
  {
    "gender": "female",
    "name": {"title": "Mrs", "first": "Neha", "last": "Reddy"},
    "location": {
      "city": "Chennai",
      "state": "Tamil Nadu",
      "country": "India"
    },
    "email": "neha.reddy@example.com",
    "dob": {"date": "1975-07-22T12:30:45.000Z", "age": 49},
    "phone": "044-34567890"
  }
]

@nilus.resource()
def fetch_random_users():
    for d in dummy_data:
        yield d

@nilus.source
def random_user_source(uri, table, **kwargs):
    return fetch_random_users()
```

**`nilus_custom_source.py`**

```python
from examples.custom_source.random_users import random_user_source
from nilus import CustomSource

class RandomUserSource(CustomSource):
    def handles_incrementality(self) -> bool:
        return False

    def nilus_source(self, uri: str, table: str, **kwargs):
        return random_user_source(uri, table, **kwargs)
```

### **How It Works**

* **`random_users.py`**
    * Defines a resource (`fetch_random_users`) that yields static user data.
    * Registers a Nilus source (`random_user_source`) to expose the resource.
* **`nilus_custom_source.py`**
    * Wraps the source in a `CustomSource` class (`RandomUserSource`).
    * Nilus expects this class when running the custom source.
*   The name of the destination will be defined:

    * Explicitly through the table_name parameter in the `@nilus.resource` decorator.

    ```python
    @nilus.resource(table_name="my_table")   
    def fetch_random_users():
    ```

    * If `table_name` is not defined in the `@nilus.resource` decorator; it defaults to the function name.
    * Looking at the actual example in `random_users.py`

    ```python
    @nilus.resource()
    def fetch_random_users():
        response = dummy_data
        for d in response:
            yield d
    ```

    * Since the `table_name` parameter is not defined in the `@nilus.resource()`, the destination table name will be `fetch_random_users` (the function name).
* Nilus executes the custom source like any other built-in connector, streaming the yielded records into downstream pipelines.

## Best Practices

When implementing custom sources, follow these guidelines to ensure maintainability, performance, and reliability:

1. **Code Organization**
     1. Keep resources, sources, and utility functions in separate modules.
     2. Maintain a clear repository structure.
2. **Error Handling**
     1. Implement logging for all failures.
     2. Ensure errors are handled gracefully without leaving open connections.
3. **Performance**
     1. Use batching or pagination for large datasets.
     2. Apply indexing where applicable to optimize data retrieval.
4. **Testing**
     1. Test sources independently before deploying in a workflow.
     2. Validate correctness and data completeness.
5. **Documentation**
     1. Document all required parameters for each source.
     2. Provide usage examples where possible.

## Security Considerations

Custom Sources must follow secure development practices to protect credentials, control access, and ensure data compliance.

1. **Secrets Management**
     1. Store sensitive credentials in **DataOS Secrets** or environment variables.
     2. Avoid hardcoding API keys or credentials in the source code.
     3. Rotate authentication tokens and API keys regularly.
2. **Access Control**
     1. Apply the principle of least privilege to database or API users.
     2. Monitor and audit access logs for suspicious activity.
3. **Data Protection**
     1. Use TLS or equivalent encryption when connecting to external APIs or databases.
     2. Mask, encrypt, or hash sensitive fields when required.
     3. Ensure compliance with relevant regulations such as GDPR or HIPAA.







