# Power BI

In this guide, you will learn how to integrate a Data Product with Power BI and activate it to build rich, interactive dashboards.

**Prerequesite**

[Power BI Desktop](https://powerbi.microsoft.com/desktop) installed on the system(version released after June 15, 2023).

### **Step 1: Navigate to the BI sync option**
    
To start the integration, go to the 'Access Options' tab and scroll to the 'Excel and PowerBI' option in the 'BI Sync' section. Click on the 'Download `.pbip` File' button to initiate the download of a ZIP folder.
    
![powerbi_conn_details.png](/learn/dp_consumer_learn_track/integrate_bi_tools/powerbi/powerbi_conn_details.png)
    
### **Step 2: Extract the files**
    
After downloading the ZIP file, extract it to a directory on your local machine. Inside the extracted folder, you will find the essential files that help maintain semantic synchronization between the Data Product and Power BI.
    
The folder stores the main components of a Power BI project for syncing the Lens Model (here `Product Affinity`), including folders like the`.Report` and `.SemanticModel`. 
    
![folder_structure.png](/learn/dp_consumer_learn_track/integrate_bi_tools/powerbi/folder_structure.png)
    
Following is a brief description of each:
    
- **public_productaffinity.Report:** This folder holds contains `definition.pbir` file related to the report definition in Power BI. This file defines the visual representation of data, such as tables and charts, without storing actual data. It connects the semantic model and data sources to create the report views.
- **public-productaffinity.SemanticModel:** This folder contains files that define the underlying data model for your Power BI project. The Semantic Model is crucial in managing how Power BI interacts with data and setting up relationships, hierarchies, and measures.
    - **definition.bism:** This file represents the Business Intelligence Semantic Model (BISM). It defines the structure of your data, including data sources, relationships, tables, and measures for your Lens Model. The `.bism` file holds essential metadata that helps Power BI understand and query the data, forming the core of the data model for report creation and analysis.
    - **model.bim:** Power BI uses the `.bim` file to generate queries and manage interactions with the dataset. When you build reports or dashboards in Power BI, it references this semantic model to ensure the correct structure is applied to the data.
- **public-productaffinity.pbip:** This file is a Power BI project template or configuration file. Power BI uses files like `.pbip` or `.pbix` to encapsulate reports, datasets, and visualizations. The `.pbip` file ties together the semantic model and report definitions from the other folders, acting as the entry point for working on the project in Power BI Desktop or the Power BI service.

### **Step 3: Open the file in Power BI and connect**

Open the `public_productaffinity.pbip` file in Power BI. A popup will appear prompting you to enter your 'DataOS username' and 'API key'.

![powerbi_ui.png](/learn/dp_consumer_learn_track/integrate_bi_tools/powerbi/powerbi_ui.png)

After entering your credentials, click 'Connect'. A confirmation popup will appear; click 'OK' to proceed.

![powerbi_pop_up.png](/learn/dp_consumer_learn_track/integrate_bi_tools/powerbi/powerbi_pop_up.png)

### **Step 4: Access data tables and start building dashboards**

Once connected, you can see tables and views containing all dimensions and measures from the Data Product. You can now start building your dashboard by selecting the relevant fields for analysis.

![powerbi_dashboard.png](/learn/dp_consumer_learn_track/integrate_bi_tools/powerbi/powerbi_dashboard.png)


## Using PowerBI Service Account

To publish the created report to the Power BI service account for sharing and collaboration follow the below steps:

### **Step 1: Publish the report to Power BI Service**

In the PowerBI, click 'Publish'. This action will push the report to your online Power BI service account, making it available for access in the Power BI workspace. Choose the required workspace.

<aside class="callout">
💡 This step requires a valid Power BI service account, as the report will be published to the online service.

</aside>

![powerbi_publish.png](/learn/dp_consumer_learn_track/integrate_bi_tools/powerbi/excel/powerbi_publish.png)

### **Step 2: Confirm publishing in the chosen workspace**

The image below shows the power BI is publishing the report in the chosen workspace.

![powerbi_publishing.png](/learn/dp_consumer_learn_track/integrate_bi_tools/powerbi/excel/powerbi_publishing.png)

### **Step 3: Navigate to your workspace**

Once published, go to your 'workspace' where the report has been saved. Here it is Demo Testing.

![powerrbi_workspace.png](/learn/dp_consumer_learn_track/integrate_bi_tools/powerbi/excel/powerrbi_workspace.png)

Click on the connected semantic model below the workspace with the name `cross-sell-affinity`.

![powerbi_settings.png](/learn/dp_consumer_learn_track/integrate_bi_tools/powerbi/excel/powerbi_settings.png)

### **Step 4: Locate and access report settings**

Scroll down to the 'Gateway and Cloud Connections' section. Toggle the switch to 'enable the gateway connection'. Click on the 'Add to Gateway' button to initiate the connection process.

![powerbi_gateway.png](/learn/dp_consumer_learn_track/integrate_bi_tools/powerbi/excel/powerbi_gateway.png)

### **Step 5: Enable gateway connection**

After clicking the 'Add to Gateway' button, you'll be prompted to enter the necessary 'connection details' for the data source. Once you’ve entered the required connection information, finalize the connection setup.

![powerbi_gateway_connection.png](/learn/dp_consumer_learn_track/integrate_bi_tools/powerbi/excel/powerbi_gateway_connection.png)

### **Step 7: Confirm successful connection**

After successfully connecting,you will be mapped to the semantic model as shown in the image below:

![powerbi_gateway_conn1.png](/learn/dp_consumer_learn_track/integrate_bi_tools/powerbi/excel/powerbi_gateway_conn1.png)

### **Step 8: Access the semantic model**

After successfully connecting, you will be able to access the dashboard. 

![powerbi_chart.png](/learn/dp_consumer_learn_track/integrate_bi_tools/powerbi/excel/powerbi_chart.png)


<aside class="callout">
🗣️ Power BI also provides the functionality to interact with the downloaded file in Excel.

</aside> 

## Supported data types

| **Category**   | **Data Types**                                                                  | **Support Status**                       |
|----------------|---------------------------------------------------------------------------------|------------------------------------------|
| **Dimension**  | `time`, `string`, `number`, `boolean`                                                   | Supported                                |
| **Measure**    | `max`, `min`, `number`, `sum`, `count`, `boolean`, `string`, `time`, `avg`, `count_distinct`         | Supported                                |
| **Measure**    | `count_distinct_approx`                                                           | Not Supported                            |
| **Rolling Window** | -                                                                           | Not Supported (Power BI doesn’t support) |

## Important considerations

- In Power BI, measures typically have an 'm_' prefix to indicate they represent a measure. For example, a measure calculating total revenue might be named `m_total_revenue`.
- The connection is live, meaning any changes to the underlying data will be reflected in Power BI.
- When schema changes occur, such as CRUD operations (Create, Read, Update, Delete) on dimensions, measures, or other elements of the semantic model, a re-sync is required. To prevent losing previously created reports after the re-sync, download the model folder from the Data Product Hub, extract the contents, and replace the existing folder with the new one.

## Best practices

Adhering to best practices ensures that you effectively utilize the Data Product Hub and maintain compatibility with the latest features and updates. Following these guidelines will help optimize workflow, enhance performance, and prevent potential issues.

### **File handling**

Ensure that `.pbip` folders are fully extracted before opening them. Failure to do so may result in missing file errors, as shown below:

<img src="/resources/lens/bi_integration/image.png" alt="DPH" style="width:15rem; border: 1px solid black;" />

### **Data retrieval and field selection considerations**

It is important to select fields from tables that are directly related or logically joined, as the system does not automatically identify relationships between tables through transitive joins. Selecting fields from unrelated tables may result in incorrect or incomplete results.

### **Connection reset**

If you encounter a 'connection reset' error during Power BI sync:

- Go to the Home tab in Power BI Desktop.
- Click the Refresh button in the Queries section.

<img src="/interfaces/data_product_hub/activation/bi_sync/powerbi/refresh_key.png" alt="DPH" style="width:25rem; border: 1px solid black;" />

This should resolve the error and restore the sync.

## Limitations

- Power BI fails to handle special characters (e.g., &, %, #) when generating queries through the synced semantic model, causing errors in visualizations. Thus, it is best practice to address or remove special characters directly in the data itself.
- Power BI's Direct Query mode does not support creating custom dimensions and measures or querying the rolling window measure due to the lack of date hierarchy.
- DAX functions and Import query mode are not supported.


## Governance of model on Power BI

Data masking, restrictions, and permissions established by the publisher are automatically enforced for all report viewers, ensuring consistent data security and compliance. The behavior of these data policies, such as masking, may vary based on the use of Power BI Desktop or other interfaces.

When the Lens semantic model is activated via BI Sync on Power BI, authentication and authorization are handled using the DataOS user ID and API key. This ensures that columns redacted by Lens data policies are restricted based on the user's group permissions.

For example, if a user named iamgroot, belonging to the 'Analyst' group, is restricted from viewing the 'Annual Salary' column, this column will not appear in either the Data Product exploration page or in Power BI after synchronization. Power BI requires the DataOS user ID and API key for authentication, ensuring that users can access the full model except for columns restricted by their data policies.

This approach ensures that users only see the data they are authorized to view, maintaining security and compliance.

<!-- 
## Excel via PowerBI

Follow the below link to analyze in Excel via PowerBI.

[Excel via Power BI](/learn/dp_consumer_learn_track/integrate_bi_tools/powerbi/excel/)

 -->
