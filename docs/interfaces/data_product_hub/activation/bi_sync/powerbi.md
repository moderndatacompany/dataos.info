# PowerBI Integration

<<<<<<< HEAD
## Steps
=======
1. Navigate to the **Data Product Hub**, Access the **Home Page** of DataOS. From there, navigate to the **Data Product Hub**, where you can explore various Data Products available within the platform.
>>>>>>> 83f1c68a2524e022232f273f92e8edb848d70816

The following steps outline the process for integrating PowerBI with DataOS:

### **Step 1: Navigate to the Data Product Hub**

<<<<<<< HEAD
Access the **Home Page** of DataOS. From there, navigate to the **Data Product Hub** to explore the various data products available within the platform.
=======
2. In the Data Product Hub, browse through the list of Data Products. Click on the specific data product you wish to integrate with PowerBI. For example, select **Sales360** from the list to explore **Sales360** Data Product.
>>>>>>> 83f1c68a2524e022232f273f92e8edb848d70816

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/image%20(1).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

### **Step 2: Browse and Select a Data Product**

In the Data Product Hub, users should browse through the list of data products. Clicking on a specific data product to integrate with PowerBI. For example, selecting **Sales360** from the list allows exploration of the **Sales360** data product.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/image%20(2).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

### **Step 3: Access Integration Options**

<<<<<<< HEAD
After selecting a data product, navigate to the **Access Options** tab. Within this tab, various methods to access and interact with the data product can be found, including options for **Excel and PowerBI**.
=======
4. Locate the downloaded ZIP file on the local system and unzip the folder. Three files will be present in the folder. Open the 'public_sales360' file in Power BI. Ensure that all three files are kept together, as the other two files are essential for the semantic sync of the Data Product. 
>>>>>>> 83f1c68a2524e022232f273f92e8edb848d70816

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/image%20(3).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

### **Step 4: Download and Open the ZIP File**

Locate the downloaded ZIP file on the local system and unzip the folder. Three files will be present in the folder. Open the 'public_sales360' file in Power BI. It is essential to keep all three files together, as the other two files are necessary for the semantic synchronization of the data product.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/Untitled%20(15).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

This downloads a `file.zip` archive that stores the main components of a Power BI project. When running the curl command, you can specify any name for the zip file, and it will be downloaded with that name. The `file.zip` contains key components for syncing the Lens Model (here sales360) to Power BI, including folders like the `.Report` and `.SemanticModel`:

- **public_sales360-table.Report:** This folder holds contains `definition.pbir` file related to the report definition in Power BI. These files define the visual representation of data, such as tables and charts, without storing actual data. They connect the semantic model and data sources to create the report views.

- **public-sales360-table.SemanticModel:** This folder contains files that define the underlying data model for your Power BI project. The Semantic Model plays a crucial role in managing how Power BI interacts with data, setting up relationships, hierarchies, and measures.

    - **definition.bism:** This file represents the Business Intelligence Semantic Model (BISM). It defines the structure of your data, including data sources, relationships, tables, and measures for your Lens Model. The `.bism` file holds essential metadata that helps Power BI understand and query the data, forming the core of the data model for report creation and analysis.

    - **model.bim:** Power BI uses the `.bim` file to generate queries and manage interactions with the dataset. When you build reports or dashboards in Power BI, it references this semantic model to ensure the correct structure is applied to the data.

- **public-sales-360-table.pbip:** This file serves as a Power BI project template or configuration file. Power BI uses files like `.pbip` or `.pbix` to encapsulate reports, datasets, and visualizations. The `.pbip` file ties together the semantic model and report definitions from the other folders, acting as the entry point for working on the project in Power BI Desktop or the Power BI service.

### **Step 5: Enter Credentials**

Once the file is opened, a popup will appear prompting for the DataOS username and API key.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/Untitled%20(16).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/Untitled17.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

### **Step 6: Establish Connection**

Click the connect button. A popup will appear; click OK.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/untitled18.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

### ** Step 7: View Data in Power BI**

After connecting, users can see tables and views containing dimensions and measures.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/Untitled%20(19).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

---

## Governance of Model on Power BI

When the Lens Model is activated via BI Sync on Power BI, the management process is handled through authentication and authorization using the DataOS user ID and API key when accessing synced data models. This ensures that columns redacted by Lens data policies are restricted based on the user's group permissions.

For instance, if a user named **iamgroot** in the "**Analyst**" group is restricted from viewing the "Annual Salary" column, this column will not be visible in either the Data Product exploration page or in PowerBI after syncing. Power BI requires the DataOS user ID and API key for authentication, ensuring that users can access the full model, except for any columns restricted by their data policies. This approach maintains security and guarantees that users only see the data they are authorized to view.
