# Power BI Service Integration

This document outlines the steps required to integrate Power BI with DataOS, ensuring a seamless connection to the Data Product Hub.

## Prerequisites

<aside class="callout">
🗣️ <b>Important: Firewall and VPN Configuration Required</b>

- If DataOS is installed in a Virtual Private Cloud (VPC), port `6432` must be whitelisted to allow communication between the Power BI data gateway and the DataOS. Ensure that firewall rules permit inbound and outbound traffic on port `6432`.
- If the customer connects to the VPC via VPN, additional firewall rules may be required to allow communication between the VPN network and Power BI Service. Ensure that Power BI can access the PostgreSQL database over the VPN connection.
</aside>
Before proceeding with the data gateway configuration, ensure the following components are installed:

- [Power BI Desktop](https://powerbi.microsoft.com/desktop) installed on the local system(version released after June 15, 2023).

- A Power BI service account.

- [Npgsql](#installing-npgsql-for-postgresql-connectivity) version `v4.0.10` (or earlier, up to `v4.0.16`).

- [On-premises data gateway](#installing-the-on-prem-data-gateway).

- Ensure that necessary ports (such as `6432`) and services are whitelisted.


<aside class="callout">
💡 Organizations are responsible for managing the installation and configuration of both the Power BI gateway and Npgsql within the VPC. We are happy to collaborate with your technical teams to ensure a smooth setup.
</aside>

## Installing the on-prem data gateway

1. Download the gateway installer from [Microsoft](https://www.microsoft.com/en-us/power-platform/products/power-bi/gateway).

2. Run the installer, keep the default installation path, accept the terms, and select Install.

    <img src="/interfaces/data_product_hub/activation/bi_sync/powerbi/powerbi_service/pb_on_prem_07.png" alt="DPH" style="width:40rem; height:20% border: 1px solid black;" />
    
3. Enter the email address for your Office 365 organization account, then select Sign in.

    <img src="/interfaces/data_product_hub/activation/bi_sync/powerbi/powerbi_service/pn_on_prem_mail_08.png" alt="DPH" style="width:40rem; height:auto; border: 1px solid black;" />

    <aside class="callout">
    💡 The account used must be an organization account.
    </aside>

    You're now signed in to your account.

4. Select Register a new gateway on this computer > Next.
    
    <img src="/interfaces/data_product_hub/activation/bi_sync/powerbi/powerbi_service/p_serv_on_prem_09.png" alt="DPH" style="width:40rem; height:auto; border: 1px solid black;" />
    

5. Enter a name for the gateway. The name must be unique across the tenant. Also, enter a recovery key. You'll need this key if you ever want to recover or move your gateway. Select Configure.
    
    <img src="/interfaces/data_product_hub/activation/bi_sync/powerbi/powerbi_service/pb_service_on_prem_10.png.png" alt="DPH" style="width:40rem; height:auto; border: 1px solid black;" />  

6. Review the information in the final window. Select Close.
    
    <img src="/interfaces/data_product_hub/activation/bi_sync/powerbi/powerbi_service/pb_on_prem_serv_11.png" alt="DPH" style="width:40rem; height:auto; border: 1px solid black;" />   

Now that you've installed a gateway, install a `npgsql`.

## Installing Npgsql for PostgreSQL connectivity

1. Download the `Npgsql.msi` installer from [GitHub](https://github.com/npgsql/npgsql/releases/tag/v4.0.10) Make sure to download the `v4.0.10` or earlier version.

2. Open the installer and click Next to begin the setup.
    
    <img src="/interfaces/data_product_hub/activation/bi_sync/powerbi/powerbi_service/npgsql_01.png" alt="DPH" style="width:40rem; height:auto; border: 1px solid black;" />

3. Accept the terms and conditions of use and click Next.

    <img src="/interfaces/data_product_hub/activation/bi_sync/powerbi/powerbi_service/npgsql_02.png" alt="DPH" style="width:40rem; height:auto; border: 1px solid black;" />  

4. Ensure 'Npgsql GAC Installation' is selected. Verify that both the default-checked and unchecked files are selected before proceeding.
    
    <img src="/interfaces/data_product_hub/activation/bi_sync/powerbi/powerbi_service/npgsql_03.png" alt="DPH" style="width:40rem; height:auto;border: 1px solid black;" /> 

5. Click Install to begin the installation.
    
    <img src="/interfaces/data_product_hub/activation/bi_sync/powerbi/powerbi_service/npgsql_04.png" alt="DPH" style="width:40rem; height:auto; border: 1px solid black;" />   

6. Once completed, click Finish to exit the setup wizard.

## Create and publish a Power BI Desktop file

Follow the below steps to sync the integrate the `productaffinity` semantic model with the Power BI and create a basic Power BI report Publish the report to the Power BI service to get a Power BI semantic model.

### **Step 1: Navigate to the BI sync option**

In Data Product Hub, choose a Data Product let's say `product-affinity` Navigate to the Access Options tab on the Data Product Hub application on DataOS. Within a specific Data Product, and under the BI Sync options, select 'Excel and Power BI'. Click on the download icon to download the `.pbip` file.
    
<img src="/interfaces/data_product_hub/activation/bi_sync/powerbi/powerbi_service/pb_service_access_option_01.png" alt="DPH" style="width:40rem; height:auto; border: 1px solid black;" />

### **Step 2: Extract the files**

Once downloaded, locate the ZIP file in your file manager and extract it to your desired destination. The necessary files will then be available.

<img src="/interfaces/data_product_hub/activation/bi_sync/powerbi/powerbi_service/pb_serv_02.png" alt="DPH" style="width:40rem; height:auto; border: 1px solid black;" />
  
The folder stores the main components of a Power BI project for syncing the Lens Model (here Product Affinity), including folders like the.Report and .SemanticModel.

- **public_sales360-table.Report:** This folder contains `definition.pbir` file related to the report definition in Power BI. These files define the visual representation of data, such as tables and charts, without storing actual data. They connect the semantic model and data sources to create the report views.

- **public-sales360-table.SemanticModel:** This folder contains files that define the underlying data model for your Power BI project. The semantic model plays a crucial role in managing how Power BI interacts with data, setting up relationships, hierarchies, and measures.

    - **definition.bism:** This file represents the Business Intelligence Semantic Model (BISM). It defines the structure of your data, including data sources, relationships, tables, and measures for your Lens semantic model. The `.bism` file holds essential metadata that helps Power BI understand and query the data, forming the core of the data model for report creation and analysis.

    - **model.bim:** Power BI uses the `.bim` file to generate queries and manage interactions with the dataset. When you build reports or dashboards in Power BI, it references this semantic model to ensure the correct structure is applied to the data.

- **public-sales-360-table.pbip:** This file serves as a Power BI project template or configuration file. Power BI uses files like `.pbip` or `.pbix` to encapsulate reports, datasets, and visualizations. The `.pbip` file ties together the semantic model and report definitions from the other folders, acting as the entry point for working on the project in Power BI Desktop or the Power BI service.


### **Step 4: Open the file in Power BI and connect**

Open the `public_productaffinity` file in Power BI Desktop. A popup will appear prompting you to enter your 'DataOS username' and 'API key'.

<!-- ![image.png](attachment:e0514197-9d8c-4961-80a6-634f3a94a543:image.png) -->

After entering your credentials, click 'Connect'. A confirmation popup will appear; click 'OK' to proceed.

<!-- ![image.png](attachment:9512f7de-1358-4d44-938a-7416cea52ff2:image.png) -->

Customize and create your report as required.

<img src="/interfaces/data_product_hub/activation/bi_sync/powerbi/powerbi_service/pb_report_05.png" alt="DPH" style="width:40rem; height:auto; border: 1px solid black;" />
        
### **Step 5: Publish the report to PowerBI Service Account**

On the Home tab, select Publish.

On the Publish to Power BI screen, choose My Workspace, and then select Select. Sign in to the Power BI service if necessary.

When the Success message appears, select Open `productaffinity.pbip` in Power BI. If prompted, sign in to your Power BI service account to complete the process.

<img src="/interfaces/data_product_hub/activation/bi_sync/powerbi/powerbi_service/pb_publish_06.png" alt="DPH" style="width:40rem; height:auto; border: 1px solid black;" />
    
## Configuring a Data Gateway for PostgreSQL Server

In Power BI Desktop, you connected directly to your on-premises PostgreSQL Server database. In the Power BI service, you need a data gateway to act as a bridge between the cloud and your on-premises network. Follow these steps to add your on-premises PostgreSQL Server database as a data source to a gateway and connect your semantic model to this data source.

### **Add a Gateway connection**

To connect Power BI to the on-premises PostgreSQL database via the data gateway, follow these steps:

1. In Power BI Service, navigate to the workspace where the semantic model has been published.

2. Locate the `productaffinity` semantic model in the content list.
   
    <img src="/interfaces/data_product_hub/activation/bi_sync/powerbi/powerbi_service/confgi_gateway_01.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    
    
3. From the File dropdown, select Settings.
 
    <img src="/interfaces/data_product_hub/activation/bi_sync/powerbi/powerbi_service/config_gateway_02.png" alt="DPH" style="width:40rem; border: 1px solid black;" />   

    
4. In the Settings screen, locate and expand the Gateway and cloud connections section, and click the Create a connection button.
    
    <img src="/interfaces/data_product_hub/activation/bi_sync/powerbi/powerbi_service/config_gateway_04.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    
    
5. On the New Connection screen with On-premises selected, complete or verify the following fields. Most fields are already filled in.
    
    <img src="/interfaces/data_product_hub/activation/bi_sync/powerbi/powerbi_service/config_gateway_05.png" 
        alt="DPH" 
        style="width:40rem; height:20rem; border: 1px solid black;" />

        
6. In the New Connection screen, ensure On-premises is selected and complete the following fields(some fields are pre-configured):

    - **Gateway Cluster Name**: Enter or verify the configured gateway name.
    - **Connection Name**: Provide a descriptive name (e.g., `productaffinity-testing`).
    - **Connection Type**: Ensure PostgreSQL is selected.
    - **Server**: Enter the PostgreSQL instance (e.g., `tcp.dataos-training-dataos.app:6432`).
    - **Database**: Specify the database name (e.g., `lens:public:productaffinity`).
    - **Authentication**: Select Basic authentication and enter the UserID and API Key (retrievable from the DataOS profile page).
    - **General encryption**: The encrypted connection should be set to 'Not encrypted'.

<aside class="callout">
💡 To retrieve your API Key and Username, click your profile icon in the Data Product Hub interface and select 'Profile'. Then, navigate to the Tokens section. Click the eye icon to reveal and copy your API Key. Your Username is your User ID.

<img src="/interfaces/data_product_hub/activation/bi_sync/powerbi/powerbi_service/apikey.png" alt="API Key" />

</aside>

After filling out the required fields, click Add to create the connection.

1. In the Settings screen, verify that the data gateway is running under the configured name (e.g., `productaffinity-testing`). Click Apply.
    
    <img src="/interfaces/data_product_hub/activation/bi_sync/powerbi/powerbi_service/config_gateway_07.png" alt="DPH" style="width:40rem; border: 1px solid black;" />  
    
2. Click the `public_productaffinity` report icon to confirm the connection is active.
    
    <img src="/interfaces/data_product_hub/activation/bi_sync/powerbi/powerbi_service/config_gateway_08.png" alt="DPH" style="width:40rem; border: 1px solid black;" />   
    
### **Supported data types**

| **Category** | **Data Types** | **Support Status** |
| --- | --- | --- |
| **Dimension** | `time`, `string`, `number`, `boolean` | Supported |
| **Measure** | `max`, `min`, `number`, `sum`, `count`, `boolean`, `string`, `time`, `avg`, `count_distinct` | Supported |
| **Measure** | `count_distinct_approx` | Not Supported |
| **Rolling Window** | - | Not Supported (Power BI doesn’t support) |

### **Important considerations**

- In Power BI, measures typically have an 'm_' prefix to indicate they represent a measure. For example, a measure calculating total revenue might be named `m_total_revenue`.
- The connection is live, meaning any changes to the underlying data will be reflected in Power BI.
- When schema changes occur, such as CRUD operations (Create, Read, Update, Delete) on dimensions, measures, or other elements of the semantic model, a re-sync is required. To prevent losing previously created reports after the re-sync, replace the `.pbip` file in the existing folder with the `.pbip` file from the newly downloaded folder.
- Power BI fails to handle special characters (e.g.,) when generating queries through the synced semantic model, causing errors in visualizations. Thus, it is best practice to address or remove special characters directly in the data itself.
- Power BI's Direct Query mode does not support creating custom dimensions and measures or querying the rolling window measure due to the lack of date hierarchy.

### **Best practices**

Adhering to best practices ensures that you effectively utilize the Data Product Hub and maintain compatibility with the latest features and updates. Following these guidelines will help optimize workflow, enhance performance, and prevent potential issues.

#### **File handling**

Ensure that `.pbip` folders are fully extracted before opening them. Failure to do so may result in missing file errors, as shown below:

<img src="/resources/lens/bi_integration/image.png" alt="DPH" style="width:40rem; height:30%; border: 1px solid black;" />

#### **Data retrieval and field selection considerations**

It is important to select fields from tables that are directly related or logically joined, as the system does not automatically identify relationships between tables through transitive joins. Selecting fields from unrelated tables may result in incorrect or incomplete results.

<!-- - Power BI’s DAX and Import functions are not supported.
- Special characters cannot be handled through DAX function hence it’s best practice to remove the special character from dataset if any. -->
<!-- 
## Governance of model on Power BI

Data masking, restrictions, and permissions established by the publisher are automatically enforced for all report viewers, ensuring consistent data security and compliance. The behavior of these data policies, such as masking, may vary based on the use of Power BI Desktop or other interfaces.

When the Lens semantic model is activated via BI Sync on Power BI, authentication and authorization are handled using the DataOS user ID and API key. This ensures that columns redacted by Lens data policies are restricted based on the user's group permissions.

For example, if a user named `iamgroot`, belonging to the 'Analyst' group, is restricted from viewing the 'Annual Salary' column, this column will not appear in either the Data Product exploration page or in Power BI after synchronization. Power BI requires the DataOS user ID and API key for authentication, ensuring that users can access the full model except for columns restricted by their data policies.

This approach ensures that users only see the data they are authorized to view, maintaining security and compliance. -->