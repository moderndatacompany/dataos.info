# DataOS SDK for Python

The DataOS SDK for Python includes functionality to accelerate development with Python for the DataOS platform. It provides a cohesive set of APIs, each accessible through its respective services, enabling seamless interaction with the platform. By utilizing the SDK, data developers unlock the potential to construct innovative solutions and integrate them seamlessly into their existing resources.

<aside class="callout">

🗣 The <b>DataOS SDK for Python</b> is currently in the stress testing phase. The interfaces are finalized. Additional information expected in further releases.

</aside>

## Installation

### **Prerequisites**

This section describes the steps to follow before installing DataOS SDK for Python.

**Ensure you have Python ≥ 3.7 Installed**

Prior to installation, ensure that you have Python 3.7 and above installed on your system. You can check the Python version by running:

*For Linux/macOS*

```shell
python3 --version
```

*For Windows*

```shell
py --version
```

If you do not have Python, please install the latest version from [python.org](https://www.python.org/).

> <b>Note:</b> If you’re using an enhanced shell like IPython or Jupyter notebook, you can run system commands like those given above by prefacing them with a <code>!</code> character:
```shell
In [1]: import sys
        !{sys.executable} --version
# Output
Python 3.7.3
```
<aside class="best-practice">

<b>Best Practice:</b> It’s recommended to write <code>{sys.executable}</code> rather than plain <code>python</code> in order to ensure that commands are run in the Python installation matching the currently running notebook (which may not be the same Python installation that the <code>python</code> command refers to).

</aside>

**Ensure you have `pip` installed**

Additionally, you’ll need to make sure you have `pip` available. You can check this by running:

*For Linux/macOS*

```shell
python3 -m pip --version
```

*For Windows*

```shell
py -m pip --version
```

If you installed Python from source, with an installer from [python.org](https://www.python.org/), or via [Homebrew](https://brew.sh/) you should already have pip. If you’re on Linux and installed using your OS package manager, you may have to install pip separately, see [Installing pip/setuptools/wheel with Linux Package Managers](https://packaging.python.org/en/latest/guides/installing-using-linux-tools/).

### **Installing `dataos-sdk-py` from PyPI**

The DataOS SDK for Python can be installed from the Python Package Index (PyPI) using the following command:

*For Linux/macOS*

```shell
# For latest version
python3 -m pip install dataos-sdk-py
# For specific version
python3 -m pip install dataos-sdk-py=={{version specifier}}
# e.g. python3 -m pip install dataos-sdk-py==0.0.1
```

*For Windows*

```shell
# For latest version
py -m pip install dataos-sdk-py
# For specific version
py -m pip install dataos-sdk-py=={{version specifier}}
# e.g. py -m pip install dataos-sdk-py==0.0.1
```

<aside class="callout">

🗣 <b>Note:</b> If you’re using an enhanced shell like IPython or Jupyter notebook, you must restart the runtime in order to use the newly installed package.

</aside>

### **Upgrading from PyPI**

Upgrade DataOS SDK for Python to the latest from PyPI.

*For Linux/macOS*

```shell
python3 -m pip install --upgrade dataos-sdk-py
```

*For Windows*

```shell
py -m pip install --upgrade dataos-sdk-py
```

## Getting Started

Upon successful installation of the DataOS SDK for Python, it is now time to commence your coding journey.

### **List Metadata of a Dataset**

To get started, let's walk through a straightforward example of establishing a connection with DataOS, configuring it with the required parameters, and accessing metadata for a dataset.

**Code Snippet**

```python
# Import the DepotServiceClientBuilder class from the depot_service.depot_service_client module
from depot_service.depot_service_client import DepotServiceClientBuilder

# Define your DataOS user API key token 
# (Replace '{{dataos user apikey token}}' with your actual DataOS API key token. e.g. abcdefghijklmnopqrst)
# Fetch the DataOS User API key token using `dataos-ctl user apikey get/create` command on DataOS CLI
apikey = "{{dataos user apikey token}}"

# Define the base URL for the DataOS Depot service 
# (Replace the '{{dataos instance fqdn}}' with your specific DataOS Instance FQDN e.g. https://sunny-prawn.dataos.app/ds)
base_url = "https://{{dataos instance fqdn}}/ds"

# Create an instance of the DepotServiceClientBuilder
ds_client = DepotServiceClientBuilder()

# Configure the DepotServiceClientBuilder with the API key and base URL
ds_client.set_apikey(apikey)
ds_client.set_base_url(base_url)

# Build the DepotServiceClient, which is ready to interact with DataOS
ds_client_instance = ds_client.build()

# Access the dataset_api and list metadata for a specific dataset
metadata = ds_client_instance.dataset_api.list_metadata(depot="icebase", collection="retail", dataset="city")

# Print Metadata
print(metadata)

```

**Expected Output**

```python
[MetadataVersionResponse(version='v1.gz.metadata.json', timestamp=1696940109201), MetadataVersionResponse(version='v2.gz.metadata.json', timestamp=1696940212855), MetadataVersionResponse(version='v3.gz.metadata.json', timestamp=1697550809632), MetadataVersionResponse(version='v4.gz.metadata.json', timestamp=1698387825353), MetadataVersionResponse(version='v5.gz.metadata.json', timestamp=1699016002681)]
```

For additional information regarding the [subpackages](./dataos_python_sdk/depot_service.html#subpackages) and [submodules](./dataos_python_sdk/depot_service.html#submodules) contained within the [`depot_service`](./dataos_python_sdk/modules.html#depot-service) package, please refer to the respective links within the [Python SDK Library Reference](./dataos_python_sdk/reference_index.html).

### **Retrieve Dataset Statistics**

In the following code snippet, we demonstrate the setup of the Depot Service client and the process of retrieving statistics for a dataset using the DataOS SDK for Python.

**Code Snippet**

```python
# Import the DepotServiceClientBuilder class from the depot_service.depot_service_client module
from depot_service.depot_service_client import DepotServiceClientBuilder

# Create an instance of DepotServiceClientBuilder for setting up the DataOS client
ds_client = DepotServiceClientBuilder()

# Configure the DataOS client with the following parameters in a method chain:
# - Set the base URL for DataOS.
# - Provide the DataOS API key.
# - Build the DataOS client.
ds_client = ds_client.set_base_url("https://{{dataos fqdn}}/ds") \
                     .set_apikey("{{dataos user apikey token}}") \
                     .build()

# Show statistics for a specific dataset in DataOS by specifying the depot, collection, and dataset name.
stats = ds_client.dataset_api.show_stats(depot="{{depot name}}", collection="{{collection name}}", dataset="{{dataset name}}")

# Print the stats to the console.
print(stats)
```

<details><summary>Expected Output</summary>
    
```python
stats = {
    'totalRecords': '213500',
    'totalPartitions': '0',
    'totalSnapshots': '4',
    'totalFileSize': '6742016',
    'totalDataFiles': '4'
}

timeline = {
    '1697550809632': {
        'recordCount': '53375',
        'operation': 'append',
        'schema': {
            "type": "record",
            "name": "defaultName",
            "fields": [
                {"name": "__metadata", "type": {"type": "map", "values": "string", "key-id": 10, "value-id": 11}, "field-id": 1},
                {"name": "city_id", "type": ["null", "string"], "default": None, "field-id": 2},
                {"name": "zip_code", "type": ["null", "int"], "default": None, "field-id": 3},
                {"name": "city_name", "type": ["null", "string"], "default": None, "field-id": 4},
                {"name": "county_name", "type": ["null", "string"], "default": None, "field-id": 5},
                {"name": "state_code", "type": ["null", "string"], "default": None, "field-id": 6},
                {"name": "state_name", "type": ["null", "string"], "default": None, "field-id": 7},
                {"name": "version", "type": "string", "field-id": 8},
                {"name": "ts_city", "type": {"type": "long", "logicalType": "timestamp-micros", "adjust-to-utc": True}, "field-id": 9}
            ]
        },
        'versionFile': 'v3.gz.metadata.json'
    },
    '1696940212855': {
        'recordCount': '53375',
        'operation': 'append',
        'schema': {
            "type": "record",
            "name": "defaultName",
            "fields": [
                {"name": "__metadata", "type": {"type": "map", "values": "string", "key-id": 10, "value-id": 11}, "field-id": 1},
                {"name": "city_id", "type": ["null", "string"], "default": None, "field-id": 2},
                {"name": "zip_code", "type": ["null", "int"], "default": None, "field-id": 3},
                {"name": "city_name", "type": ["null", "string"], "default": None, "field-id": 4},
                {"name": "county_name", "type": ["null", "string"], "default": None, "field-id": 5},
                {"name": "state_code", "type": ["null", "string"], "default": None, "field-id": 6},
                {"name": "state_name", "type": ["null", "string"], "default": None, "field-id": 7},
                {"name": "version", "type": "string", "field-id": 8},
                {"name": "ts_city", "type": {"type": "long", "logicalType": "timestamp-micros", "adjust-to-utc": True}, "field-id": 9}
            ]
        },
        'versionFile': 'v2.gz.metadata.json'
    },
    '1696940109201': {
        'versionFile': 'v1.gz.metadata.json'
    },
    '1699016002681': {
        'recordCount': '53375',
        'operation': 'append',
        'schema': {
            "type": "record",
            "name": "defaultName",
            "fields": [
                {"name": "__metadata", "type": {"type": "map", "values": "string", "key-id": 10, "value-id": 11}, "field-id": 1},
                {"name": "city_id", "type": ["null", "string"], "default": None, "field-id": 2},
                {"name": "zip_code", "type": ["null", "int"], "default": None, "field-id": 3},
                {"name": "city_name", "type": ["null", "string"], "default": None, "field-id": 4},
                {"name": "county_name", "type": ["null", "string"], "default": None, "field-id": 5},
                {"name": "state_code", "type": ["null", "string"], "default": None, "field-id": 6},
                {"name": "state_name", "type": ["null", "string"], "default": None, "field-id": 7},
                {"name": "version", "type": "string", "field-id": 8},
                {"name": "ts_city", "type": {"type": "long", "logicalType": "timestamp-micros", "adjust-to-utc": True}, "field-id": 9}
            ]
        },
        'versionFile': 'v5.gz.metadata.json'
    },
    '1698387825353': {
        'recordCount': '53375',
        'operation': 'append',
        'schema': {
            "type": "record",
            "name": "defaultName",
            "fields": [
                {"name": "__metadata", "type": {"type": "map", "values": "string", "key-id": 10, "value-id": 11}, "field-id": 1},
                {"name": "city_id", "type": ["null", "string"], "default": None, "field-id": 2},
                {"name": "zip_code", "type": ["null", "int"], "default": None, "field-id": 3},
                {"name": "city_name", "type": ["null", "string"], "default": None, "field-id": 4},
                {"name": "county_name", "type": ["null", "string"], "default": None, "field-id": 5},
                {"name": "state_code", "type": ["null", "string"], "default": None, "field-id": 6},
                {"name": "state_name", "type": ["null", "string"], "default": None, "field-id": 7},
                {"name": "version", "type": "string", "field-id": 8},
                {"name": "ts_city", "type": {"type": "long", "logicalType": "timestamp-micros", "adjust-to-utc": True}, "field-id": 9}
            ]
        },
        'versionFile': 'v4.gz.metadata.json'
    }
}

properties = {
    'write.format.default': 'parquet',
    'write.metadata.compression-codec': 'gzip'
}
```

</details>



## Python SDK Reference

For a detailed reference guide on the Python SDK and its subpackages, modules, and classes, please visit the [Python SDK Reference.](./dataos_python_sdk/reference_index.html). 

