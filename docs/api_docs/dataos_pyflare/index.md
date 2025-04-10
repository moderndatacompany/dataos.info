---
title: DataOS PyFlare
search:
  boost: 2
tags:
    - PyFlare
    - SDK
    - Python
    - DataOS PyFlare
---


# DataOS PyFlare

The DataOS PyFlare is a Python library that streamlines data operations and facilitate seamless interactions with Apache Spark within DataOS. Its a wrapper around [Flare](/resources/stacks/flare/), to enable Python support with DataOS capabilities. The library abstracts complexities inherent in data flow, allowing users to direct their focus toward data transformations and the formulation of business logic by simplifying the loading, transformation, and storage of data. It facilitates the integration of existing Spark Job code bases with DataOS, requiring minimal modifications.

<aside class="callout">
🗣 Delve into the comprehensive <a href="/api_docs/dataos_pyflare/docs/pyflare.html">Pyflare Library Reference</a> for detailed insights into the diverse modules and classes encompassed by the Flare package. To know more about Flare's key features and initiation procedures, refer to the following sections.
</aside>


## Key Features

### **Streamlined Data Operations**

Pyflare offers a unified interface for data loading, transformation, and storage, thereby significantly reducing development intricacies and accelerating the project timeline.

### **Data Connector Integration**

It seamlessly integrates with various data connectors, including depot and non-depot sources, by leveraging the SDK's built-in capabilities.

### **Customizability and Extensibility**

Pyflare empowers users with the flexibility to tailor it to their specific project requirements. It seamlessly integrates with existing Python libraries and frameworks designed for data manipulation.

### **Optimized for DataOS**

Pyflare is finely tuned for the DataOS platform, rendering it an ideal choice for the management and processing of data within DataOS environments.

## Installation

The Pyflare module is compatible with DataOS-native [Jupyter Notebooks](/interfaces/notebook/) and can also be utilized in various Python programs across different environments, provided that the necessary JAR files are incorporated.

><b>Note:</b> If you are using DataOS-native Jupyter Notebooks or Python environment, you can skip the installation part and directly navigate to the <a href="#getting-started">Getting Started</a> section as the JAR files and modules are included automatically as part of the environment setup.

### **Prerequisites**

This section describes the steps to follow before installing Pyflare.

**Ensure you have Python ≥ 3.7 Installed**

Prior to installation, ensure that you have Python 3.7 and above installed on your system. You can check the Python version by running:

*For Linux/macOS*

```bash
python3 --version
```

*For Windows*

```bash
py --version
```

If you do not have Python, please install the latest version from [python.org](https://www.python.org/).


> <b>Note:</b> If you’re using an enhanced shell like IPython or Jupyter notebook, you can run system commands by prefacing them with a <code>!</code> character:

```bash
In [1]: import sys
        !{sys.executable} --version
# Output
Python 3.6.3
```

<aside class="best-practice">

📖 <b>Best Practice:</b> It’s recommended to write <code>{sys.executable}</code> rather than plain <code>python</code> in order to ensure that commands are run in the Python installation matching the currently running Notebook (which may not be the same Python installation that the <code>python</code> command refers to).

</aside>

**Ensure you have `pip` installed**

Additionally, you’ll need to make sure you have pip available. You can check this by running:

*For Linux/macOS*

```bash
python3 -m pip --version
```

*For Windows*

```bash
py -m pip --version
```

If you installed Python from source, with an installer from [python.org](https://www.python.org/), or via [Homebrew](https://brew.sh/) you should already have pip. If you’re on Linux and installed using your OS package manager, you may have to install pip separately, see [Installing pip/setuptools/wheel with Linux Package Managers](https://packaging.python.org/en/latest/guides/installing-using-linux-tools/).



### **Installing from PyPI**

The `dataos-pyflare` library can be installed from the Python Package Index (PyPI) using the following command:

<aside class="best-practice" style="border-left: 4px solid #28a745; background-color: #e6f4ea; color: #1e4620; padding: 1rem; border-radius: 0.5rem; margin: 1rem 0;">
<b>Recommendation:</b> Install the <code>dataos-pyflare==0.1.13</code> version of Pyflare, as it is the designated stable release.
</aside>

**For Linux/macOS**

```bash
python3 -m pip install dataos-pyflare==0.1.13

```

**For Windows**

```bash

py -m pip install dataos-pyflare==0.1.13
```

><b>Note:</b> If you’re using an enhanced shell like IPython or Jupyter notebook, you must restart the runtime in order to use the newly installed package.


### **Install from Source Distribution**

pip can install from either [Source Distributions (sdist)](https://files.pythonhosted.org/packages/b8/f7/aab336433a50d0ebd8eee9cce96bfaadc37c456dad47bbd3836d637fd916/dataos-pyflare-0.1.6.tar.gz) or [Wheels](https://files.pythonhosted.org/packages/78/6b/c350ee12542572e8cb3faf311c5c96772d326655d59c2ba771dafcf70343/dataos_pyflare-0.1.6-py3-none-any.whl), but if both are present on PyPI, pip will prefer a compatible wheel. You can override pip`s default behavior by e.g. using its [–no-binary](https://pip.pypa.io/en/latest/cli/pip_install/#install-no-binary) option.

If `pip` does not find a wheel to install, it will locally build a wheel and cache it for future installs, instead of rebuilding the source distribution in the future.


## Getting Started

The following code snippet exemplifies the configuration of a Flare session for generating fictitious data, applying transformations, and saving the results to Icebase depot.

### **Import the Requisite Libraries**

```python
from pyspark.sql import Row
from pyspark.sql.functions import col
from pyflare.sdk import load, save, session_builder
```

### **Data loading**

```python
# Load Iceberg data from Lakehouse
df = load(name="dataos://lakehouse:test_crm/product_data", format="iceberg")
df.show(10)

```

### **DataOS Configuration**

The DataOS configuration is established with the DataOS Fully Qualified Domain Name (FQDN) and an authentication token.

```python
DATAOS_FQDN = "{{fully-qualified-domain-name-of-dataos-instance}}" # e.g. sunny-prawn.dataos.app
token = "{{dataos-user-apikey-token}}" # e.g. abcdefghijklmnopqrstuvwxyz=
```

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

### **Flare Session Setup**

A Flare session can be created using the configuration settings using the `SparkSessionBuilder()`. This session serves as the foundation for subsequent data operations.

```python
# Spark configuration settings
sparkConf = [
    ("spark.app.name", "Pyflare App"),
    ("spark.master", "local[*]"),
]

# Build the session
spark = session_builder.SparkSessionBuilder(log_level="INFO") \
    .with_spark_conf(sparkConf) \
    .with_user_apikey(token) \
    .with_dataos_fqdn(DATAOS_FQDN) \
    .with_depot(depot_name="${{lakehouse}}", acl="rw") \
    .build_session()

```

### **Data Storage**

The `save` method is used to store the transformed DataFrame in the designated destination (`dataos://${{depot_name}}:${{Schema}}/${{table_name}}`) in respective format. For example:

```python
# Save the DataFrame to DataOS with specified path
save(name="dataos://lakehouse:sandbox3/test_pyflare2", dataframe=df, format="iceberg", mode="overwrite")

```

### **Data Retrieval**

The `load` method is employed to retrieve data from a specified source (`dataos://${{depot_name}}:${{Schema}}/${{table_name}}`) in respective format. The result is a governed DataFrame. For example:


```python
# Read data from DataOS using Iceberg format and display the first 10 records
load(name="dataos://lakehouse:sandbox3/test_pyflare2", format="iceberg").show(10)

# Count the total number of records in the stored dataset
load(name="dataos://lakehouse:sandbox3/test_pyflare2", format="iceberg").count()
```

### **Session Termination**

The Spark session is terminated at the end of the code execution.

```python
# Stop the session
spark.stop()
```

## Code Samples

- [ How to read and write partitioned data within Icebase Depot using Pyflare?](/api_docs/dataos_pyflare/code_samples/read_write_partitioned_data/)

- [How to overwrite dynamic Iceberg partitions using Pyflare?](/api_docs/dataos_pyflare/code_samples/overwrite_dynamic_iceberg_partitions/)

- [How to write data in Avro format from Iceberg using Pyflare?](/api_docs/dataos_pyflare/code_samples/write_avro_read_iceberg/)


## Pyflare Library Reference

For a comprehensive reference guide to Pyflare, including detailed information on its modules and classes, please consult the [Pyflare Library Reference.](/api_docs/dataos_pyflare/docs/pyflare.html)




