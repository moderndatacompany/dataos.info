# Power BI

In this guide, you will learn how to integrate a data product with Power BI and activate it to build rich, interactive dashboards.


### Scenario:

Imagine you are part of the sales team at a growing retail company, and you need to analyze sales data to track performance trends, monitor regional sales distribution, and identify product affinities. By integrating your sales data product into Power BI, you can create interactive dashboards that allow you to dive deep into metrics, explore relationships, and make actionable business decisions.

1. **Navigate to the BI Sync Option**
    
    To start the integration, go to the **Access Options** tab and scroll to the **Excel and PowerBI** option in the **BI Sync** section. Click on the **Download `.pbip` File** button to initiate the download of a ZIP folder.
    
    ![powerbi_conn_details.png](/learn/dp_consumer_learn_track/integrate_bi_tools/powerbi/powerbi_conn_details.png)
    
2. **Extract the Files**
    
    After downloading the ZIP file, extract it to a directory on your local machine. Inside the extracted folder, you will find the essential files that help maintain semantic synchronization between the Data Product and Power BI.
    
    The folder stores the main components of a Power BI project for syncing the Lens Model (here `product360`), including folders like the`.Report` and `.SemanticModel`. 
    
    ![folder_structure.png](/learn/dp_consumer_learn_track/integrate_bi_tools/powerbi/folder_structure.png)
    
    Following is a brief description of each:
    
    - **public_product360.Report:** This folder holds contains `definition.pbir` file related to the report definition in Power BI. This file defines the visual representation of data, such as tables and charts, without storing actual data. It connects the semantic model and data sources to create the report views.
    - **public-product360.SemanticModel:** This folder contains files that define the underlying data model for your Power BI project. The Semantic Model is crucial in managing how Power BI interacts with data and setting up relationships, hierarchies, and measures.
        - **definition.bism:** This file represents the Business Intelligence Semantic Model (BISM). It defines the structure of your data, including data sources, relationships, tables, and measures for your Lens Model. The `.bism` file holds essential metadata that helps Power BI understand and query the data, forming the core of the data model for report creation and analysis.
        - **model.bim:** Power BI uses the `.bim` file to generate queries and manage interactions with the dataset. When you build reports or dashboards in Power BI, it references this semantic model to ensure the correct structure is applied to the data.
    - **public-product360.pbip:** This file is a Power BI project template or configuration file. Power BI uses files like `.pbip` or `.pbix` to encapsulate reports, datasets, and visualizations. The `.pbip` file ties together the semantic model and report definitions from the other folders, acting as the entry point for working on the project in Power BI Desktop or the Power BI service.

### **Step 3: Open the File in Power BI and Connect**

Open the **`public_product360`** file in Power BI. A popup will appear prompting you to enter your **DataOS username** and **API key**.

![powerbi_ui.png](/learn/dp_consumer_learn_track/integrate_bi_tools/powerbi/powerbi_ui.png)

After entering your credentials, click **Connect**. A confirmation popup will appear; click **OK** to proceed.

![powerbi_pop_up.png](/learn/dp_consumer_learn_track/integrate_bi_tools/powerbi/powerbi_pop_up.png)

### **Step 4: Access Data Tables and Start Building Dashboards**

Once connected, you can see tables and views containing all dimensions and measures from the Data Product. You can now start building your dashboard by selecting the relevant fields for analysis.

![powerbi_dashboard.png](/learn/dp_consumer_learn_track/integrate_bi_tools/powerbi/powerbi_dashboard.png)

Happy dashboarding!

<aside>
💡

Power BI also provides the functionality to interact with the downloaded file in Excel.

</aside>

## Excel via PowerBI

Follow the below link to analyze in Excel via PowerBI.

[Excel via Power BI](/learn/dp_consumer_learn_track/integrate_bi_tools/powerbi/excel/)