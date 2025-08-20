---
title: Notebook
search:
  boost: 2
---

# :interfaces-notebook: Notebook

<aside class="callout">
🗣 The Notebook application has been deprecated from the default DataOS® UI experience. However, it can be made available on demand for customers who require its capabilities. Please contact your DataOS® administrator to enable access to the Notebook app in your environment.
</aside>

DataOS Notebook interface is based on Jupyter Notebook which is a popular open-source web-based application that allows users to create and share documents that contain live code, equations, visualisations, and narrative text. It provides a user-friendly interface for interactive computing, data analysis, and data visualisation in several programming languages, including Python, and Scala.

In a Notebook, you can write and execute code in cells, which are units of code that can be run independently or in a specific order. You can also include text, images, videos, and equations in markdown cells to explain your code and provide context. 
Notebooks are especially useful for "showing the work" that your data team has done through a combination of code, markdown, links, and images.

## Features of Notebook on DataOS 
DataOS is configured to take advantage of the Jupyter ecosystem's open-source tooling. When using Notebook on DataOS, there are several advantages and features that make it a valuable tool for data science projects:

- **Secure Environments**: Jupyter kernels on DataOS come with pre-installed libraries essential for data science projects. These environments are secure and isolated, ensuring that your model pipelines and data remain protected. 
- **Depot Connectivity**: The PyFlare SDK provides seamless connectivity to your existing depots within the Jupyter environment. This enables easy access to data stored in depots.
- **Multi-Language Support**: Jupyter Notebooks offer support for multiple programming languages, including Python, R, Julia, and Scala. This versatility allows you to choose the language that best suits your needs and work with a wide range of data analysis and machine learning tools.
- **Apache Toree**: DataOS supports Apache Toree, a Scala-based Jupyter Kernel. This kernel enables Jupyter Notebooks to execute Scala code and seamlessly connect to Apache Spark. With Apache Toree, you can build interactive applications, leverage the power of Spark for big data processing, and perform advanced analytics within your Jupyter environment.


## Use Case- Writing Data To Lakehouse
This use case demonstrates how to write a test dataset to DataOS Lakehouse using PyFlare on Jupyter Notebook. We achieve the objective with help of `PyFlare` and `PySpark` on Notebook hosted on DataOS. 

### **Prerequisites**
- DataOS credentials and access to Lakehouse depot.
- Hosted Jupyter Notebook on DataOS.

Launch Notebook from DataOS Home and navigate to persistent-systems directory.

1. Install PyFlare on Jupyter
2. Input credentials and connect to Lakehouse with a spark session
3. Read and save data to lakehouse using PyFlare

### **Installation**

Use the following command to install PyFlare on the hosted Jupyter environment. It will enable Spark capabilities in your Jupyter Notebook environment.

```python

pip install pyflare

# Import necessary libraries
from pyflare import session, logger, sdk
```

### **Connection to Spark**
Connect to Lakehouse with a Spark session. Enter your tokens and table address, we are writing a test dataset on vehicle collision to Lakehouse. 

#### **Define Datasets to be Read**
Define the datasets to be read, including the dataset path. 
```python
log = logger.get(__name__, "info")

inputs = {
    'collision': " "   ##leave blank if data in same directory     
		}                   # else path
```
#### **Output Table address**
Specify the output table address in Lakehouse where you want to write the data. `c181` is the name of the view.
```python
outputs = {
    "c181": "dataos://lakehouse:<schema>/vehiclecollision"   ##address of table
}
```

#### **Specific spark conf for Lakehouse**  
Set up the necessary Spark configurations that would be needed for Lakehouse depot.
```python
sparkConf = [
    ("spark.app.name", "Dataos Sdk Spark App"),
    ("spark.master", "local[*]"),
    ("spark.jars.packages", "org.apache.iceberg:iceberg-spark3:0.13.2,org.apache.spark:spark-sql_2.12:3.3.0,"
                            "com.microsoft.azure:azure-storage:8.6.6,org.apache.hadoop:hadoop-azure:3.3.3")
]
```
#### **DataOS FQDN and DataOS API Token**
Provide the DataOS Fully Qualified Domain Name (FQDN) and your DataOS API token.

```python
DATAOS_FQDN = "engaging-ocelot.dataos.app"

token = "<api token>"
```
#### **Create Spark Session to Connect with LAKEHOUSE**
Create a Spark session to connect with Lakehouse using the provided credentials and configurations.
```python
spark = session(api_key=token, dataos_url=DATAOS_FQDN, inputs=inputs, outputs=outputs,
                spark_conf_options=sparkConf)
```

#### **Read and Save Data to Lakehouse**

Read your dataset using the Spark object created in the previous step. Supported data formats include CSV, JDBC, JSON, ORC, Parquet, Table, and Text. Create a temporary view with a name of your choice for further processing.

```python
 
df = spark.read.csv("Motor_Vehicle_Collisions_-_Crashes.csv",header=True)
### temporary view
df.createOrReplaceTempView("c181")
```

#### **Configurations for Output Dataset**

Configure the output dataset options, such as compression and file format, for the data to be saved in Lakehouse.
Use the PyFlare SDK to save the dataset to Lakehouse with the specified options.

```python
write_options = {
    "compression": "gzip",
    "write.format.default": "parquet",
    "iceberg": {
        "partition": [
            {
                "type": "identity",
                "column": "state_code",
            }
        ]
    }
}

dataset = sdk.save(name = "c181",format = "iceberg", mode='overwrite', options=write_options)
```
#### **Set Metadata**
To show the dataset on the workbench and start querying, run set-metadata command on DataOS CLI.
```bash
dataos-ctl dataset set-metadata -a dataos://lakehouse:shopper_360/model_prediction -v latest
```
<aside class="callout">
🗣 You can run the SQL query on the intermediate view to check the data before writing it to the Icabase.
</aside>

## Example Code

```python
log = logger.get(__name__, "info")
# Define the datasets to be read
inputs = {
    'collision': ""  # Leave blank if the data is in the same directory, otherwise provide the path
}

# Specify the output table address in Lakehouse
outputs = {
    "c181": "dataos://lakehouse:<schema>/vehiclecollision"  # Address of the table
}

# Specify the Spark configurations for Lakehouse
sparkConf = [
    ("spark.app.name", "Dataos Sdk Spark App"),
    ("spark.master", "local[*]"),
    ("spark.jars.packages", "org.apache.iceberg:iceberg-spark3:0.13.2,org.apache.spark:spark-sql_2.12:3.3.0,"
                            "com.microsoft.azure:azure-storage:8.6.6,org.apache.hadoop:hadoop-azure:3.3.3")
]

# Provide the DataOS FQDN and API token
DATAOS_FQDN = "engaging-ocelot.dataos.app"
token = "<api token>"

# Create a Spark session to connect with Lakehouse
spark = session(api_key=token, dataos_url=DATAOS_FQDN, inputs=inputs, outputs=outputs,
                spark_conf_options=sparkConf)

# Read your dataset and create a temporary view
df = spark.read.csv("Motor_Vehicle_Collisions_-_Crashes.csv", header=True)
df.createOrReplaceTempView("c181")

# Configure the output dataset options
write_options = {
    "compression": "gzip",
    "write.format.default": "parquet"
}

# Save the dataset to Lakehouse using PyFlare SDK
dataset = sdk.save(name="c181", format="iceberg", mode='overwrite', options=write_options)
```
Your data is successfully written in Lakehouse. Make sure to customize the database name, table name, and any additional options based on your specific use case.