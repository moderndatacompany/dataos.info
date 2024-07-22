---
title: Interfaces
search:
  boost: 2
---

# :material-application-import: Interfaces

Interfaces in DataOS serve as vital points of communication and interaction between different services & the users. They facilitate seamless collaboration and independent functionality within DataOS. These interfaces provide powerful tools for efficient data operations,  and control over various activities. Whether you prefer the flexibility of the API, the command-driven power of the CLI, or the intuitive experience of the GUI, DataOS interfaces enable self-service data management. Let's explore these interfaces and their capabilities.

## Command Line Interface (CLI)

The DataOS CLI provides a command-line environment for efficient and streamlined data operations. It offers quick access to system functionality with flexibility and control making it ideal for data engineers or system administrators. They can interact with DataOS instance through text-based commands, create and manage resources, and perform various data management tasks.  Effective utilization of CLI may require familiarity with the system and its underlying commands. To learn more, click [here](/interfaces/cli/). 

## Graphical User Interface (GUI)

The Graphical User Interface offers an intuitive and visually engaging way to interact with DataOS and its components.  This makes DataOS accessible to users with varying technical expertise, enhancing user experience and usability. For example, applications like Atlas and Lens Explorer provide graphical user interfaces for tasks such as creating visualizations, building dashboards, and interacting with the semantic layer.

## Application Programming Interface (API)

The Application Programming Interface (API) in DataOS provides a way to interact with the core components, libraries, and services. APIs act as intermediaries, allowing users/applications to access DataOS functionality and resources. APIs empower data  developers to create diverse applications and services, leveraging the full functionality of DataOS. Learn about our SDKs on the following page: [DataOS SDKs](/api_docs/).

<aside class="callout">
🗣️ The choice of interface (CLI, GUI or API) depends on factors such as specific applications, user requirements, and the capabilities of individual components. By leveraging these interfaces effectively, users can navigate their data journey within DataOS and unlock its full potential.</aside>

## DataOS Home App- GUI to Interact with DataOS Components

### **Access Native Apps**
From the DataOS Home app, you can access the unique capabilities of the components and apps.
<center>
![dataos_homepage.png](/interfaces/dataos_homepage.png){: style="width:31rem;" }
<figcaption><i>DataOS Home App </i></figcaption>
</center>


Following native apps are available on DataOS Graphical User Interface:



<div class="grid cards" markdown>

-   :material-view-dashboard-outline:{ .lg .middle } **Atlas**

    ---

    Create visualizations, reports, and dashboards. Manage queries, snippets, and alerts.

    [:octicons-arrow-right-24: Read more](/interfaces/atlas/)


-   :interfaces-audiences:{ .lg .middle } **Audience**

    ---

    Leverage semantic models for customer segmentation and data-driven decisions.

    [:octicons-arrow-right-24: See more](/interfaces/audiences/)

-   :material-security-network:{ .lg .middle } **Bifrost**

    ---

    Control access policies with fine-grained ABAC policies for secure data access.

    
    [:octicons-arrow-right-24: Explore more](/interfaces/bifrost/)

-   :interfaces-dataproducthub:{ .lg .middle } **Data Product Hub**

    ---

    Central unit for exploring Data Products, accelerating time-to-value by granting quick access to trusted data with lineage, quality checks, and popularity metrics. 

    [:octicons-arrow-right-24:  Learn more](/interfaces/data_product_hub/)

-   :interfaces-lens:{ .lg .middle } **Lens**

    ---

    Model data, define measures, and create KPIs for data-informed decisions.

    [:octicons-arrow-right-24:  Learn more](/interfaces/lens/)

-   :interfaces-metis:{ .lg .middle } **Metis**

    ---

    Discover and catalog enterprise data with comprehensive metadata management.

    [:octicons-arrow-right-24:  Learn more](/interfaces/metis/)

-   :interfaces-notebook:{ .lg .middle } **Notebook**

    ---

    Use Jupyter Notebook on DataOS for data science projects and analysis.

    [:octicons-arrow-right-24:  Learn more](/interfaces/notebook/)


-   :interfaces-operations:{ .lg .middle } **Operations**

    ---

    Monitor and administer DataOS platform activity and optimize resource allocation.

    [:octicons-arrow-right-24:  Learn more](/interfaces/operations/)

-   :interfaces-workbench:{ .lg .middle } **Workbench**

    ---

    Query and explore data using SQL with the Minerva/Themis query engine.

    [:octicons-arrow-right-24:  Learn more](/interfaces/workbench/)
</div>

<!-- **Superset**

Superset is a business intelligence solution seamlessly integrated into DataOS. It simplifies the creation of customized reports and dashboards, making it easy to visualize complex data. With a wide range of visualization options, Superset enables clear interpretation, aiding informed decision-making. to learn more, click [here](/interfaces/superset/). -->

### **Manage Profile**

DataOS Home app also enables you to manage your profile.

<center>
  <div style="text-align: center;">
    <img src="/interfaces/profileinfo.png" alt="Profile Information" style="width:26rem; border:1px solid black;">
    <figcaption align="center"><i>Profile Information</i></figcaption>
  </div>
</center>


### **Create Tokens**

API keys/tokens are used to authenticate requests to  DataOS resources. For example, when calling a service endpoint, you need to supply a valid API token in the HTTP `Authorization` header, with a valid token specified as the header value. You can generate API keys/tokens from DataOS Home app as well as using DataOS CLI commands.

#### **Create Tokens using GUI**

1.  On the 'Profile' page, click on **Tokens**.

2. Click on the **Add API Key** link.

<center>
  <div style="text-align: center;">
    <img src="/interfaces/token_apikey.png" alt="Adding API key" style="width:41rem; border:1px solid black;">
    <figcaption align="center"><i>Adding API key</i></figcaption>
  </div>
</center>


3. Type in the name for this token and also set the validity period of your token based on the security requirements as per your business needs. Click **Save** to create one for you.

<center>
  <div style="text-align: center;">
    <img src="/interfaces/add_key.png" alt="Providing name for the token" style="width:41rem; border:1px solid black;">
    <figcaption align="center"><i>Providing name for the token</i></figcaption>
  </div>
</center>


4. The API key is listed below. Clicking on the “eye icon” will make the full API key visible. Click on the API key to copy it.

<center>
  <div style="text-align: center;">
    <img src="/interfaces/key_created.png" alt="API key created" style="width:41rem; border:1px solid black;">
    <figcaption align="center"><i>API key created</i></figcaption>
  </div>
</center>

 

#### **Create Tokens Using CLI**

Use the commands to:

- List existing key
- Create a new API key

**List Existing Key**

```bash
tmdc@tmdc:~$ dataos-ctl user apikey get
INFO[0000] 🔑 user apikey get...                         
INFO[0000] 🔑 user apikey get...complete                 

                                                 TOKEN                                                 |  TYPE  |      EXPIRATION      |                  NAME                   
-------------------------------------------------------------------------------------------------------|--------|----------------------|-----------------------------------------
  aH9sAY5fcXVpY2tseVXXXXXXXXXXXXppppppppppppppppcXTUzLTgaH999999999sAY5fcXaH9ssssssssssAY5fcX0| apikey | 2023-08-10T23:00:00Z | token_ad9baade458c5c6f3  
  bbbbbbbbbI9sAY5fcXVpY2tseV9ldmVubHlfVjdF9raXQuM2ZiO0000000TI4ZTYaaaaaaaH9sAY5fcXTUzLTgaH9sAY5fcX5fcX0| apikey | 2023-06-19T08:00:00Z | token_bc6hggaa435v8b5f3
```

**Create a new API key**

```bash
tmdc@tmdc:~$ dataos-ctl user apikey create
INFO[0000] 🔑 user apikey...                             
INFO[0000] 🔑 user apikey...complete                     

                                                   TOKEN                                                   |  TYPE  |      EXPIRATION      |                  NAME                    
-----------------------------------------------------------------------------------------------------------|--------|----------------------|------------------------------------------
  aH9sAY5fcXVpY2tseV9ldmVubHlfY29ycmVjdF9raXQuM2ZiOTI4ZTYaH9sAY5fcXTUzLTgaH9sAY5fcXaH9sAY5fcX0 | apikey | 2022-06-22T12:00:00Z | token_bc6hggaa435v8b5f3
```

### **View Depots**
You can see a complete list of depots created in your DataOS context for accessing data sources.

<center>
  <div style="text-align: center;">
    <img src="/interfaces/depots.png" alt="Depots" style="width:41rem; border:1px solid black;">
    <figcaption align="center"><i>Depots</i></figcaption>
  </div>
</center>

