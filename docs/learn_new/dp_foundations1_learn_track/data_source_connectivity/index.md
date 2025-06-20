
# Source Data Connectivity

Before you can build a data product, you need to connect to the data itself. In this module, you’ll learn how to configure **Depots** in DataOS—your gateway to accessing external data sources securely, without needing to move the data.

---

## 📘 Scenario

Your team is expanding its use of DataOS and needs to integrate multiple data sources into the platform. Using **Depots**, you can establish secure connections to these data sources, enhancing data interoperability while keeping the data securely in place. This approach not only preserves data security but also facilitates interaction with various DataOS Resources.

---

## Quick Concepts: What Are Depots?

The **Depot Resource** in DataOS provides a standardized way to connect to a variety of enterprise data sources, such as:

- Cloud-based object stores
- Databases
- Data warehouses
- NoSQL data stores

Depots allow you to:

- Build high-quality data pipelines  
- Query data efficiently using query clusters  
- Support semantic modeling for better data understanding

---

## Prerequisites

Before diving into configuring data source connections, make sure you have everything ready:

1. **Check required Permissions**: Some tasks require specific permissions typically assigned to DataOS Operators. Ensure you have access to one of the following permission sets either via use-case or via tags:

    | **Access Permission (via use-cases)**       | **Access Permissions (via tags)**      |
    |--------------------------------------------|---------------------------------------|
    | Read Workspace                             | `roles:id:data-dev `                  |
    | Manage All Depot                           | `roles:id:system-dev`                   |
    | Read All Dataset                           | `roles:id:user`                      |
    | Read all secrets from Heimdall             |                                |

2. **Check CLI installation**: You need this text-based interface that allows you to interact with the DataOS context via command prompts. Open a command terminal and follow the <a href="/interfaces/cli/installation/">installation guide</a> for your operating system. Once the installation is complete, proceed with the initialization.

3. **DataOS context initialization & login**:After successful installation of dataos-ctl,  lets initialize and log in to the DataOS context using CLI.

  a. Open Terminal 
  b. Type `dataos-ctl init`
  c. Follow the prompts and provide inputs depending on your user role:

    ```bash
    dataos-ctl init

    INFO[0000] The DataOS® is already initialized, do you want to add a new context? (Y,n)  
    ->Y   # input the answer: Y or n
    INFO[0255] 🚀 initialization...

    INFO[0255] The DataOS® is not initialized, do you want to proceed with initialization? (Y,n)  
    ->Y

    INFO[0269] Please enter a name for the current DataOS® Context?  
    ->{{name of the DataOS context}}
    # Example: marmot (or any name you prefer).
    # Your enterprise may offer multiple contexts — pick one to start.
    # You can switch context anytime using a CLI command after login. 

    INFO[0383] Please enter the fully qualified domain name of the DataOS® instance?  
    ->{{domain name}} 
    # Example: apparent-marmot.dataos.app
    INFO[0408] entered DataOS®: marmot : apparent-marmot.dataos.app 
    INFO[0429] Are you operating the DataOS®? (Y,n)         
    ->n  
    # If you are the operator(admin) for your enterprise, type Y
    # If you type Y, the installation steps will change.
    INFO[0452] 🚀 initialization...complete
    ```

  d. Now, log in with the following command.
    
    ```bash
    modern@ask ~ % dataos-ctl login
    INFO[0000] 🔑 login...                                   
    INFO[0000] 🔑 refresh...                                 
    INFO[0003] authorize...                                 
    INFO[0004] authorize...complete                         
    INFO[0004] 🔑 refresh...complete                         
    INFO[0004] 🔑 login...complete 
    ```
  e. Enter the following commands to verify the CLI installation.

    ```bash
    dataos-ctl version
    dataos-ctl health
    ```    
4. **Install any IDE, such as Visual Studio Code**: This is necessary for creating YAML files for your data product. Installation links for various operating systems are provided.

  **Installation links by Operating System**

  - **Linux**: Follow the detailed steps to install VS Code on your Linux system by accessing the [Install VS Code on Linux guide](https://code.visualstudio.com/docs/setup/linux).
  - **Windows**: To install VS Code on a Windows machine, refer to the [Install VS Code on Windows guide](https://code.visualstudio.com/docs/setup/windows).
  - **MacOS**: For MacOS users, installation instructions can be found in the [Install VS Code on macOS guide](https://code.visualstudio.com/docs/setup/mac).

## **Checklist:**

- [ ]  CLI is installed 
- [ ]  CLI is initialized and logged in
- [ ]  IDE (like VS Code) is installed
 

## Next Step: Setting Up Depots
You’re now ready to configure depots and start connecting to your source systems.

👉 Next Topic: [Setting Up Depots](/learn_new/dp_foundations1_learn_track/data_source_connectivity/setting_up_depots/)
