# DataOS PyFlare SDK

The DataOS PyFlare SDK is a Python library that streamlines data operations and faciltate seamless interactions with Apache Spark within DataOS. The library abstracts complexities inherent in data flow, allowing users to direct their focus toward data transformations and the formulation of business logic by simplifying the loading, transformation, and storage of data.

## Key Features

### **Streamlined Data Operations**

Dataos PyFlare offers a unified interface for data loading, transformation, and storage, thereby significantly reducing development intricacies and accelerating the project timeline.

### **Data Connector Integration**

It seamlessly integrates with various data connectors, including depot and non-depot sources, by leveraging the SDK's built-in capabilities.

### **Customizability and Extensibility**

Dataos PyFlare empowers users with the flexibility to tailor it to their specific project requirements. It seamlessly integrates with existing Python libraries and frameworks designed for data manipulation.

### **Optimized for DataOS**

Dataos PyFlare is finely tuned for the DataOS platform, rendering it an ideal choice for the management and processing of data within DataOS environments.

## Installation

The DataOS PyFlare module is compatible with DataOS-native Jupyter Notebooks and can also be utilized in various Python programs across different environments, provided that the necessary JAR files are incorporated.

<aside class = "callout">
🗣 If you are using DataOS-native Jupyter Notebooks, you can skip the installation part and directly navigate to the <a href="#getting-started">Getting Started</a> section as the JAR files and modules are included automatically as part of the environment setup.
</aside>

### **Prerequisites**

This section describes the steps to follow before installing DataOS PyFlare.

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

If you do not have Python, please install the latest version from [python.org.](https://www.python.org/)

<aside class="callout">
🗣 <b>Note:</b> If you’re using an enhanced shell like IPython or Jupyter notebook, you can run system commands by prefacing them with a <code>!</code> character:

```bash
In [1]: import sys
        !{sys.executable} --version
# Output
Python 3.6.3
```

It’s recommended to write <code>{sys.executable}</code> rather than plain <code>python</code> in order to ensure that commands are run in the Python installation matching the currently running notebook (which may not be the same Python installation that the <code>python</code> command refers to).

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

**Spark Environment Configuration**

To ensure the proper functioning of the system, a Spark environment must be configured with the necessary settings tailored to the specific use case.

**Inclusion of Additional JARs**

The inclusion of JAR files is contingent on the unique use case in question. Nevertheless, a standard set of essential JARs consistently aids in facilitating governance. The obligatory JAR files encompass:

- `io.dataos.sdk.commons`
- `io.dataos.sdk.heimdall`
- `io.dataos.sdk.spark-authz`
- A single consolidated JAR file named `io.dataos.sdk.flare_2.12`

<aside class="callout">

Please be advised that these JARs are indispensable for the specified use case and should be incorporated as per the requirements of your project.

</aside>

### **Installing from PyPI**

The DataOS PyFlare library can be installed from the Python Package Index (PyPI) using the following command:

**For Linux/macOS**

```bash
# For latest version
python3 -m pip install dataos-pyflare
# For specific version
python3 -m pip install dataos-pyflare=={{version specifier}}
# e.g. python3 -m pip install dataos-pyflare==0.0.6
```

**For Windows**

```bash
# For latest version
py -m pip install dataos-pyflare
# For specific version
py -m pip install dataos-pyflare=={{version specifier}}
# e.g. py -m pip install dataos-pyflare==0.0.6
```

<aside class="callout">
🗣 <b>Note:</b> If you’re using an enhanced shell like IPython or Jupyter notebook, you must restart the runtime in order to use the newly installed package.

</aside>

### **Install from Source Distribution**

pip can install from either [Source Distributions (sdist)](https://files.pythonhosted.org/packages/08/a6/ebc36b838374e3cf81d6dc429ff57e56c4c69d802ca171af927a2d382924/dataos-pyflare-0.0.7.tar.gz) or [Wheels](https://files.pythonhosted.org/packages/7e/ed/726abfa8ff1b6827dcb684224f0d75c0206aa41e4addacda09dba9e011cb/dataos_pyflare-0.0.7-py3-none-any.whl), but if both are present on PyPI, pip will prefer a compatible wheel. You can override pip`s default behavior by e.g. using its [–no-binary](https://pip.pypa.io/en/latest/cli/pip_install/#install-no-binary) option.

If `pip` does not find a wheel to install, it will locally build a wheel and cache it for future installs, instead of rebuilding the source distribution in the future.

### **Upgrading from PyPI**

Upgrade DataOS PyFlare to the latest from PyPI.

**For Unix/macOS** 

```bash
python3 -m pip install --upgrade dataos-pyflare
```

**For Windows**

```bash
py -m pip install --upgrade dataos-pyflare
```

## Getting Started

The following code snippet exemplifies the configuration of a DataOS PyFlare session for generating fictitious data, applying transformations, and saving the results to Icebase depot.

### **Import the Requisite Libraries**

```python
from pyspark.sql import Row
import random
from datetime import datetime, timedelta
from pyspark.sql.functions import col
from pyflare.sdk import load, save, session_builder
```

### **Data Generation**

```python
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
# If there are no apikey's present, create a new one by using the `create` command
dataos-ctl user apikey create
```

### **PyFlare Session Setup**

A PyFlare session can be created using the configuration settings using the [`SparkSessionBuilder()`](./dataos_pyflare_sdk/io/dataos/spark/session/SparkSessionBuilder.html) object. This session serves as the foundation for subsequent data operations.

```python
# Spark configuration settings
sparkConf = [
    ("spark.app.name", "Dataos Sdk Spark App"),
    ("spark.master", "local[*]"),
]

# Build the session
spark = session_builder.SparkSessionBuilder(log_level="INFO") \\
    .with_spark_conf(sparkConf) \\
    .with_user_apikey(token) \\
    .with_dataos_fqdn(DATAOS_FQDN) \\
    .with_depot(depot_name="icebase", acl="rw") \\
    .build_session()

# Create a DataFrame with generated data and repartition it
df = spark.createDataFrame(GenerateData()).repartition(1)
df.show(10)
```

### **Data Storage**

The [`save`](./dataos_pyflare_sdk/io/dataos/spark/session/FlareSession.html#save(address:String,df:org.apache.spark.sql.DataFrame,format:String,datasetOutputOptions:Option[io.dataos.spark.models.output.DatasetOutputOptions]):org.apache.spark.sql.streaming.StreamingQuery) method is used to store the transformed DataFrame in the designated destination (`dataos://icebase:pyflaresdk/test_write_01`) in Iceberg format.

```python
# Save the DataFrame to DataOS with specified path
save(name="dataos://icebase:pyflaresdk/test_write_01", dataframe=df, format="iceberg", mode="overwrite")
```

### **Data Retrieval**

The [`load`](./dataos_pyflare_sdk/io/dataos/spark/session/FlareSession.html#load(address:String,format:String,isStream:Boolean,datasetInputOptions:Option[io.dataos.spark.models.input.DatasetInputOptions],sparkOptions:Option[Map[String,String]]):org.apache.spark.sql.DataFrame) method is employed to retrieve data from a specified source (`dataos://icebase:pyflaresdk/test_write_01`) in Iceberg format. The result is a governed DataFrame.

```python
# Read data from DataOS using Iceberg format and display the first 10 records
load(name="dataos://icebase:pyflaresdk/test_write_01", format="iceberg").show(10)

# Count the total number of records in the stored dataset
load(name="dataos://icebase:pyflaresdk/test_write_01", format="iceberg").count()
```

### **Session Termination**

The Spark session is terminated at the end of the code execution.

```python
# Stop the session
spark.stop()
```

## Code Samples

- [ How to Read and Write Partitioned Data within Icebase depot?](./dataos_pyflare_sdk/code_samples/read_write_partitioned_data.md)

- [How to Overwrite Dynamic Iceberg Partitions Using DataOS PyFlare?](./dataos_pyflare_sdk/code_samples/overwrite_dynamic_iceberg_partitions.md)

- [How to write data in Avro format from Iceberg using DataOS PyFlare?](./dataos_pyflare_sdk/code_samples/write_avro_read_iceberg.md)



## Library Reference

[PyFlare SDK Library Reference](./dataos_pyflare_sdk/io/index.html)


