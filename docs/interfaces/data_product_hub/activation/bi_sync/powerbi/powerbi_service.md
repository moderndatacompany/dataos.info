---
title: Integrate semantic model with Power BI Desktop and Publish report to the Power BI Service
search:
  boost: 2
tags:
  - PowerBI Service
hide:
  - tags
---

# Integrate semantic model with Power BI Desktop and Publish report to the Power BI Service

This document outlines the steps required to integrate Power BI with the semantic model, ensuring a seamless connection to the data product consumption layer.

## Prerequisites

<aside class="callout">
💡 <b>Important: Firewall and VPN Configuration Required</b>

  <ul>
    <li>If DataOS is installed in a Virtual Private Cloud (VPC), port <code>6432</code> must be whitelisted to allow communication between the Power BI data gateway and the DataOS. Ensure that firewall rules permit inbound and outbound traffic on port <code>6432</code>.</li>
    <li>If the customer connects to the VPC via VPN, additional firewall rules may be required to allow communication between the VPN network and Power BI Service.</li>
  </ul>
</aside>

Before proceeding with the data gateway configuration, ensure the following components are installed:

- [Power BI Desktop](https://powerbi.microsoft.com/desktop) version 2.132.908.0 or later (version released after June 15, 2023).

- Power BI service account.

- [Npgsql](#installing-npgsql-for-postgresql-connectivity) (`v4.0.16` version or before).

- [On-premises data gateway](#installing-the-on-prem-data-gateway).

- Ensure that necessary ports (such as `6432`) and services are whitelisted.


<aside class="callout">
🗣️ Organizations are responsible for managing the installation and configuration of both the Power BI gateway and Npgsql within the VPC. We are happy to collaborate with your technical teams to ensure a smooth setup.
</aside>

## Installing the on-prem data gateway

1. Download the gateway installer from [Microsoft](https://www.microsoft.com/en-us/power-platform/products/power-bi/gateway).

2. Run the installer, keep the default installation path, accept the terms, and select Install.

    <img src="/interfaces/data_product_hub/activation/bi_sync/powerbi/powerbi_service/pb_on_prem_07.png" alt="DPH" style="width:25rem; height:15% border: 1px solid black;" />
    
3. Enter the email address for your Office 365 organization account, then select Sign in.

    <img src="/interfaces/data_product_hub/activation/bi_sync/powerbi/powerbi_service/pn_on_prem_mail_08.png" alt="DPH" style="width:25rem; height:15%; border: 1px solid black;" />

    <aside class="callout">
    💡 The account used must be an organization account.
    </aside>

    You're now signed in to your account.

4. Select Register a new gateway on this computer > Next.
    
    <img src="/interfaces/data_product_hub/activation/bi_sync/powerbi/powerbi_service/p_serv_on_prem_09.png" alt="DPH" style="width:25rem; height:15%; border: 1px solid black;" />
    

5. Enter a name for the gateway. The name must be unique across the tenant. Also, enter a recovery key. You'll need this key if you ever want to recover or move your gateway. Select Configure.
    
    <img src="/interfaces/data_product_hub/activation/bi_sync/powerbi/powerbi_service/pb_service_on_prem_10.png.png" alt="DPH" style="width:25rem; height:15%; border: 1px solid black;" />  

6. Review the information in the final window. Select Close.
    
    <img src="/interfaces/data_product_hub/activation/bi_sync/powerbi/powerbi_service/pb_on_prem_serv_11.png" alt="DPH" style="width:25rem; height:15%; border: 1px solid black;" />   

Now that you've installed a gateway, install a `npgsql`.

## Installing Npgsql for PostgreSQL connectivity

1. Download the `Npgsql.msi` installer from [GitHub](https://github.com/npgsql/npgsql/releases/tag/v4.0.10) Make sure to download the `v4.0.16` or earlier version.

2. Open the installer and click Next to begin the setup.
    
    <img src="/interfaces/data_product_hub/activation/bi_sync/powerbi/powerbi_service/npgsql_01.png" alt="DPH" style="width:25rem; height:15%; border: 1px solid black;" />

3. Accept the terms and conditions of use and click Next.

    <img src="/interfaces/data_product_hub/activation/bi_sync/powerbi/powerbi_service/npgsql_02.png" alt="DPH" style="width:25rem; height:15%; border: 1px solid black;" />  

4. Ensure you select 'Npgsql GAC Installation'. Verify that both the default-checked and unchecked files are selected before proceeding.
    
    <img src="/interfaces/data_product_hub/activation/bi_sync/powerbi/powerbi_service/npgsql_03.png" alt="DPH" style="width:25rem; height:15% ;border: 1px solid black;" /> 

5. Click 'Install' to begin the installation.
    
    <img src="/interfaces/data_product_hub/activation/bi_sync/powerbi/powerbi_service/npgsql_04.png" alt="DPH" style="width:25rem; height:15%; border: 1px solid black;" />   

6. Once completed, click Finish to exit the setup wizard.

## Create and publish a Power BI Desktop report

Follow the steps below to integrate the `productaffinity` semantic model with Power BI Desktop, create a basic report, and publish it to the Power BI Service.

### **Step 1: Navigate to the BI sync option**

In Data Product Hub, choose a Data Product let's say `product-affinity` Navigate to the Access Options tab on the Data Product Hub application on DataOS. Within a specific Data Product, and under the BI Sync options, select 'Excel and Power BI'. Click on the download icon to download the `.pbip` file.
    
<img src="/interfaces/data_product_hub/activation/bi_sync/powerbi/powerbi_service/pb_service_access_option_01.png" alt="DPH" style="width:40rem; height:auto; border: 1px solid black;" />

### **Step 2: Extract the files**

Once downloaded, locate the ZIP file in your file manager and extract it to your desired destination. The necessary files will then be available.

<img src="/interfaces/data_product_hub/activation/bi_sync/powerbi/powerbi_service/pb_serv_02.png" alt="DPH" style="width:40rem; height:auto; border: 1px solid black;" />
  
The folder stores the main components of a Power BI project for syncing the semantic model (here `Product Affinity`). Here is the brief description of each:

- **public_productaffinity.Report:** This folder contains `definition.pbir` file related to the report definition in Power BI. It stores the report metadata such as the version and dataset reference in JSON format.

- **public_productaffinity.SemanticModel:** This folder contains files that define the underlying data model for Power BI project. The semantic model plays a crucial role in managing how Power BI interacts with data, setting up relationships, and measures.

    - **definition.bism:** Contains the overall definition of a semantic model and core settings. This file also specifies the supported semantic model definition formats through the 'version' property.

    - **model.bim:** The model.bim file is a JSON file that contains the Tabular Model Scripting Language (TMSL) definition of a Power BI semantic model. It's used to create a database from scratch by defining objects such as measures, tables, and connection sources.

- **public_productaffinity.pbip:** The `.pbip` file contains a pointer to a report folder, opening a `.pbip` opens the targeted report and model.


### **Step 4: Open the file in Power BI and connect**

Open the `public_productaffinity` file in Power BI Desktop. A popup will appear prompting you to enter your 'DataOS username' and 'API key'.

<img src="/interfaces/data_product_hub/activation/bi_sync/powerbi/enter_username_and_apikey.png" alt="DPH" style="width:40rem; height:auto; border: 1px solid black;" />


After entering your credentials, click 'Connect'. A confirmation popup will appear; click 'OK' to proceed.

<img src="/interfaces/data_product_hub/activation/bi_sync/powerbi/popup_confirmation.png" alt="DPH" style="width:25rem; height:auto; border: 1px solid black;" />

Customize and create your report as required.

<img src="/interfaces/data_product_hub/activation/bi_sync/powerbi/powerbi_service/pb_report_05.png" alt="DPH" style="width:40rem; height:auto; border: 1px solid black;" />
        
### **Step 5: Publish the report to PowerBI Service Account**

On the Home tab, select Publish.

On the Publish to Power BI screen, choose My Workspace, and then select Select. Sign in to the Power BI service if necessary.

When the Success message appears, select Open `productaffinity.pbip` in Power BI. If prompted, sign in to your Power BI service account to complete the process.

<img src="/interfaces/data_product_hub/activation/bi_sync/powerbi/powerbi_service/pb_publish_06.png" alt="DPH" style="width:40rem; height:auto; border: 1px solid black;" />
    
## Configuring a data gateway for PostgreSQL interface

In Power BI Desktop, you connected directly to your on-premises PostgreSQL interface. In the Power BI service, you need a data gateway to act as a bridge between the cloud and your on-premises network. Follow these steps to add your on-premises PostgreSQL interface as a data source to a gateway and connect your semantic model to this data source.

### **Add a Gateway connection**

To connect Power BI to the on-premises PostgreSQL interface via the data gateway, follow these steps:

1. In Power BI Service, navigate to the workspace where the semantic model has been published.

2. Locate the `productaffinity` semantic model in the content list.
   
    <img src="/interfaces/data_product_hub/activation/bi_sync/powerbi/powerbi_service/confgi_gateway_01.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    
    
3. From the File dropdown, select Settings.
 
    <img src="/interfaces/data_product_hub/activation/bi_sync/powerbi/powerbi_service/config_gateway_02.png" alt="DPH" style="width:40rem; border: 1px solid black;" />   

    
4. In the Settings screen, locate and expand the Gateway and cloud connections section, and click the Create a connection button.
    
    <img src="/interfaces/data_product_hub/activation/bi_sync/powerbi/powerbi_service/config_gateway_04.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
    
    
5. A New Connection screen will appear, here ensure On-premises is selected and complete the following fields(some fields are pre-configured):
    
    <img src="/interfaces/data_product_hub/activation/bi_sync/powerbi/powerbi_service/config_gateway_05.png" 
        alt="DPH" 
        style="width:25rem; height:15%; border: 1px solid black;" />

        
6. Complete the following fields(some fields are pre-configured):

    - **Gateway Cluster Name**: Enter or verify the configured gateway name.
    - **Connection Name**: Provide a descriptive name (e.g., `productaffinity-testing`).
    - **Connection Type**: Ensure PostgreSQL interface is selected.
    - **Server**: Enter the PostgreSQL interface instance (e.g., `tcp.dataos-training-dataos.app:6432`).
    - **Database**: Specify the database name (e.g., `lens:public:productaffinity`).
    - **Authentication**: Select Basic authentication and enter the UserID and API Key (retrievable from the DataOS profile page).
    - **General encryption**: The encrypted connection should be set to 'Not encrypted'.

<aside class="callout">
💡 To retrieve your API Key and Username, click your profile icon in the Data Product Hub interface and select 'Profile'. Then, navigate to the Tokens section. Click the eye icon to reveal and copy your API Key. Your Username is your User ID.

<img src="/interfaces/data_product_hub/activation/bi_sync/powerbi/powerbi_service/apikey.png" alt="API Key" width="800" height="400" />


</aside>

After filling out the required fields, click Add to create the connection.

1. In the Settings screen, verify that the data gateway is running under the configured name (e.g., `productaffinity-testing`). Click Apply.
    
    <img src="/interfaces/data_product_hub/activation/bi_sync/powerbi/powerbi_service/config_gateway_07.png" alt="DPH" style="width:40rem; border: 1px solid black;" />  
    
2. Click the `public_productaffinity` report icon to confirm the connection is active.
    
    <img src="/interfaces/data_product_hub/activation/bi_sync/powerbi/powerbi_service/config_gateway_08.png" alt="DPH" style="width:40rem; border: 1px solid black;" />   
    
## Supported data types

| **Category** | **Data Types** | **Support Status** |
| --- | --- | --- |
| **Dimension** | `time`, `string`, `number`, `boolean` | Supported |
| **Measure** | `max`, `min`, `number`, `sum`, `count`, `boolean`, `string`, `time`, `avg`, `count_distinct` | Supported |
| **Measure** | `count_distinct_approx` | Not Supported |
| **Rolling Window** | - | Not Supported (Power BI doesn’t support) |

## Important considerations

- In Power BI, measures typically have an 'm_' prefix to indicate they represent a measure. For example, a measure calculating total revenue might be named `m_total_revenue`.
- The connection is live, meaning any changes to the underlying data will be reflected in Power BI.
- When schema changes occur, such as CRUD operations (Create, Read, Update, Delete) on dimensions, measures, or other elements of the semantic model, a re-sync is required. To prevent losing previously created reports after the re-sync, download the `.pbip` folder from the Data Product Hub, extract the contents, and replace the existing `.SemanticModel` folder with the new `.SemanticModel`.

## Best practices

Adhering to best practices ensures you effectively utilize the Data Product Hub and maintain compatibility with the latest features and updates. Following these guidelines will help optimize workflow, enhance performance, and prevent potential issues.

### **File handling**

Ensure `.pbip` folders are fully extracted before opening them. Failure to do so may result in missing file errors, as shown below:

<img src="/resources/lens/bi_integration/image.png" alt="DPH" style="width:15rem; border: 1px solid black;" />

### **Data retrieval and field selection considerations**

It is important to select fields from tables that are directly related or logically joined, as the system does not automatically identify relationships between tables through transitive joins. Selecting fields from unrelated tables may result in incorrect or incomplete results.

## Troubleshooting

### **Connection reset**

If you encounter a 'connection reset' error during Power BI Desktop sync as shown below:

<img src="/interfaces/data_product_hub/activation/bi_sync/powerbi/connection_reset.png" alt="DPH" style="width:25rem; border: 1px solid black;" />

- Go to the Home tab in Power BI Desktop.
- Click the Refresh button in the Queries section.

<img src="/interfaces/data_product_hub/activation/bi_sync/powerbi/refresh_key.png" alt="DPH" style="width:25rem; border: 1px solid black;" />

This should resolve the error and restore the sync.

### **Unknown cluster**

Whenever you encounter the error 'unknown cluster: <cluster_name>' as shown below, please check if the cluster has been deleted. If it has, redeploy the cluster. After redeploying the cluster, go to Power BI Desktop and click the 'Refresh' button to update the connection.

<img src="/interfaces/data_product_hub/activation/bi_sync/powerbi/cluster_error.png" alt="DPH" style="width:25rem; border: 1px solid black;" />

## Limitations

- Power BI fails to handle special characters (e.g.,) when generating queries through the synced semantic model, causing errors in visualizations. Thus, it is best practice to address or remove special characters directly in the data itself.
- Power BI's Direct Query mode does not support creating custom dimensions and measures or querying the rolling window measure due to the lack of date hierarchy.
- DAX functions and Import query mode are not supported.


<!-- - Power BI’s DAX and Import functions are not supported.
- Special characters cannot be handled through DAX function hence it’s best practice to remove the special character from dataset if any. -->

## Governance of semantic model on Power BI Service

Data masking policies are enforced based on the user who creates and registers the gateway connection for the semantic model in PowerBI Service.

## FAQs

**1. Can models be synced directly to Power BI Service?**

No, the semantic model must first be synced via Power BI Desktop. Direct synchronization to the Power BI Service is not supported. 

**2. How does the Power BI Service connection work?**

To establish a connection between the Power BI Service and DataOS, an on-premises data gateway is required. This acts as a secure bridge between Power BI’s cloud environment and on-premises infrastructure hosting the data source.

**Prerequisites include:**

- Microsoft Gateway application must be installed and configured.

- Npgsql driver version 4.0.16 or earlier must be installed. During installation, the “Npgsql GAC Installation” option should be selected.

**Connection setup process:**

- Install the Microsoft gateway application and the Npgsql driver.

- Publish the .pbip report from Power BI Desktop to Power BI Service.

**Steps:**

- Navigate to the semantic model and open File > Settings.

- Enable the on-premises gateway toggle.

- Create a new connection by specifying a unique connection name.

- Provide DataOS username and API token for authentication.

- Set the connection type to "Not encrypted".

- Map this connection to the configured gateway.

Once these steps are completed, the Power BI Service can communicate with the DataOS semantic model through the gateway.

**3. How does governance work in Power BI Service?**

Governance is enforced through access control and semantic data policies at the gateway connection level.

**Access control mechanisms:**

Each data product requires a distinct connection setup in Power BI Service. The connection includes specific details such as host, port, and database name for the model. Authentication must be done using a valid DataOS username and API token.

**Permission management:**

Data masking and filtering policies are applied based on the user who creates the gateway connection. This user must either be the owner of the semantic model or have administrative rights within the workspace. These policies are enforced automatically across dashboards and reports, ensuring secure access and compliance.

**4. How does Power BI sync work when syncing Model-First Data Products?**

Once the report is published from Desktop to the Power BI Service, a semantic model is created but initially contains no data. To enable data access and interaction:

- The Power BI On-Premises Data Gateway must be configured to link the published semantic model to its data source in DataOS. This gateway acts as a bridge between the cloud-based Power BI Service and the on-premises PostgreSQL interface exposed by DataOS.

- Queries from visuals in Power BI Service are routed through the npgsql driver via the gateway to the Postern Service.

- The Postern Service sends the query to the PgSQL API, which translates and executes it on the relevant Data Sources.

Results are returned along the same path back to Power BI Service for rendering in the dashboard.

**5. What connection mode does Power BI use to connect to DataOS when working with a ‘model-first data product’?**

Power BI uses the DirectQuery mode to connect to DataOS. This connection is established through the Postern service, which routes queries from Power BI Desktop or Service to the appropriate semantic model in Lens. As a result, visuals are refreshed in real-time based on live data, with refresh latency depending on the performance of the data source.

**6. Where does the computation happen for the Power BI semantic model sync?**

Computation is performed at two levels:

- Within DataOS, where the Lens service translates semantic queries into the appropriate source-specific SQL syntax.

- Within the data source itself, where the query is executed and the results are returned.

**7. What data sources are supported to sync the model-first data product to Power BI?**

All data sources that are compatible with Lens-based semantic modeling can be synchronized with Power BI. You can find the full list of supported data sources here.

If you are not using model-first data products and want to connect directly to Power BI use the [Presto ODBC Driver](/resources/cluster/bi_tools/powerbi/using_odbc_driver/#requirements).


**8. Do we need to register a separate connection for each ‘model-first data product’ in Power BI Service?**

Yes, each model-first data product must be registered independently through the Power BI On-Premises Data Gateway. The connection credentials and configuration must be provided for every unique semantic model to ensure secure and isolated access.

**9. Do semantic model changes reflect directly in Power BI Service upon refresh?**

No, changes made to the Lens-based semantic model do not automatically propagate to the Power BI Service. Users must republish the updated .pbip file from Power BI Desktop to Service to reflect semantic updates in dashboards or reports.

**10. Is custom measure and dimension creation supported for model-first data products in Power BI?**

No, custom definitions are not supported in Power BI when using model-first data products. All logic must be implemented in the semantic model using Lens. To support frequent measure changes, work directly with physical data. More guidance is available here.

**11. What are the known limitations when syncing model-first data products to Power BI?**

**No direct publishing:**

Semantic model updates cannot be published directly from the Lens interface to Power BI Service. Manual download and project replacement are required.

**Gateway dependency:**

Power BI Service must use the On-Premises Data Gateway and the Npgsql driver to connect with PostgreSQL-based semantic models. PostgreSQL is not supported natively in Power BI cloud-based DirectQuery sources.

**Special character handling:**

Power BI has limited support for special characters in semantic models. It is recommended to resolve such characters either in the raw dataset or during semantic modeling within DataOS.

