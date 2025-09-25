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

    - Only include **new dependencies** required by the custom source or destination.
    - Do **not** add libraries that are already part of the existing environment.
    - This prevents duplication and avoids version conflicts.

    **Pre-Installed Packages:** See the [requirements.txt](/resources/stacks/nilus/requirments.txt), to know the installed packages or [Download](/resources/stacks/nilus/requirments.zip).   
    


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







