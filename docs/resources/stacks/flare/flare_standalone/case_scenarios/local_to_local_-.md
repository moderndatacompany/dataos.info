# Local to Local - Using DataOS CLI


This article is a step-by-step guide to run Flare Standalone using DataOS Command Line Interface to test your workflows and explore the sample data using SparkSQL.

# Pre-Requisites

## Install DataOS CLI

DataOS CLI should be installed on your system. If it's not installed, please look at this document for the installation steps.

[CLI](https://www.notion.so/CLI-742ef5c014484aee897d1b9b4d54ac6b?pvs=21) 

## Operationalize Docker if you want to Read/Write IO Locally

Docker should be installed and running on the system. If Docker is installed on your system, move to the next step. In case it's not installed, visit the official Docker installation page for the same by clicking the [link](https://docs.docker.com/get-docker/)

## Get the toolbox-user tag

The user must have the `dataos:u:toolbox-user` tag. To check whether you have a tag, please go ahead and execute the below command and check in the `TAGS` section. In case you don’t have the tag, contact the system administrator

```bash
dataos-ctl user get
```

> Note: Ensure you are logged into DataOS before executing the above command. In case you haven’t logged in, run `dataos-ctl login` in the terminal.
> 

<aside>
🗣️ Some basic knowledge of Scala Programming Language is also needed

</aside>

# Getting started with Flare Standalone

## Download and Unzip Sample Data

1. Copy the below link in the browser to download `sampledata.zip`.

```bash
https://mockdataosnew.blob.core.windows.net/dropzone001/customer-resources/sampledata.zip?sv=2021-04-10&st=2022-09-15T07%3A36%3A43Z&se=2024-09-16T07%3A36%3A00Z&sr=b&sp=r&sig=KRUcakck4i7yHWYS6L0IgYA6YJjVMdkB9JWjmCdpKFw%3D
```

1. Extract the downloaded `sampledata.zip` file. It contains two folders:
2. Open the `sampledata` folder. It includes a `flareconfig` folder, which has a flare workflow file `config.yaml`, and sample data contained in the `city`, `stores`, and `transactions` folder to test the installation of Flare standalone and run Spark SQL queries. 
- **MacOSX Users -** MacOSX users will only see one folder, i.e., `sampledata`. The other folder, `__MACOSX`, will automatically get hidden.
- **Linux Users -** Linux users, will see two folders, i.e., `sampledata` and `__MACOSX.`

![Untitled](Local%20to%20Local%20-%20Using%20Docker%2078f07945f9fa42fe9b874142799042ae/Untitled.png)

## Run Sample Workflow

1. Open the terminal and navigate to the just extracted folder named `sampledata`.
2. Open the `config.yaml` file using the code editor.
3. Edit the dataset paths for `transactions` to `/data/examples/transactions` and `city` to `/data/examples/city`, respectively. The path must include `/data/examples`.

> **Note:** The paths given in the sample `config.yaml` are the docker container paths where the dataset contained in the data folder will be mounted
> 

```yaml

On successful execution, the Scala command line shell will open as below:

```bash
Flare session is available as flare.
    Welcome to
         ______   _                       
        |  ____| | |                      
        | |__    | |   __ _   _ __    ___ 
        |  __|   | |  / _` | | '__|  / _ \
        | |      | | | (_| | | |    |  __/
        |_|      |_|  \__,_| |_|     \___|  version 1.1.0
        
    Powered by Apache Spark 3.2.1
Using Scala version 2.12.15 (OpenJDK 64-Bit Server VM, Java 1.8.0_262)
Type in expressions to have them evaluated.
Type :help for more information.

scala>
```

<aside>
💡 **Note**: If you’re running the command for the first time or using an old image, executing the command will download the latest image.

</aside>


Table of Contents