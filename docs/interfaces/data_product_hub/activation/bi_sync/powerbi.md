# PowerBI Integration

## Steps

The following steps outline the process for integrating PowerBI with DataOS:

### **Step 1: Navigate to the Data Product Hub**

Access the **Home Page** of DataOS. From there, navigate to the **Data Product Hub** to explore the various Data Products available within the platform.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/image%20(1).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

### **Step 2: Browse and select a Data Product**

In the Data Product Hub, users should browse through the list of Data Products. Clicking on a specific Data Product to integrate with PowerBI. For example, selecting **Sales360** from the list allows exploration of the **Sales360** Data Product.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/image%20(2).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

### **Step 3: Access integration options**

Navigate to the BI Sync option in the Activation tab, scrolling through find the Excel and PowerBI option. Click on the download .pbip file button to download a ZIP folder.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/image%20(3).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

### **Step 4: Download and open the ZIP file**

Locate the downloaded ZIP file on the local system and unzip the folder. Three files will be present in the folder. Open the 'public_sales360' file in Power BI. It is essential to keep all three files togethe for the semantic synchronization of the Data Product.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/Untitled%20(15).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

This downloads a `file.zip` archive that stores the main components of a Power BI project for syncing the Lens Model (here sales360) including folders like the `.Report` and `.SemanticModel`:

- **public_sales360-table.Report:** This folder holds contains `definition.pbir` file related to the report definition in Power BI. These files define the visual representation of data, such as tables and charts, without storing actual data. They connect the semantic model and data sources to create the report views.

- **public-sales360-table.SemanticModel:** This folder contains files that define the underlying data model for your Power BI project. The Semantic Model plays a crucial role in managing how Power BI interacts with data, setting up relationships, hierarchies, and measures.

    - **definition.bism:** This file represents the Business Intelligence Semantic Model (BISM). It defines the structure of your data, including data sources, relationships, tables, and measures for your Lens Model. The `.bism` file holds essential metadata that helps Power BI understand and query the data, forming the core of the data model for report creation and analysis.

    - **model.bim:** Power BI uses the `.bim` file to generate queries and manage interactions with the dataset. When you build reports or dashboards in Power BI, it references this semantic model to ensure the correct structure is applied to the data.

- **public-sales-360-table.pbip:** This file serves as a Power BI project template or configuration file. Power BI uses files like `.pbip` or `.pbix` to encapsulate reports, datasets, and visualizations. The `.pbip` file ties together the semantic model and report definitions from the other folders, acting as the entry point for working on the project in Power BI Desktop or the Power BI service.

### **Step 5: Enter credentials**

Once the file is opened, a popup will appear prompting for the DataOS username and API key.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/Untitled%20(16).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/Untitled17.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

### **Step 6: Establish connection**

Click the connect button. A popup will appear; click OK.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/untitled18.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

### **Step 7: View data in Power BI**

After connecting, users can see tables and views containing dimensions and measures.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/Untitled%20(19).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

---

## Important considerations

- Measures in Power BI are typically named as **`m_total_revenue`**.
- The connection is live, meaning any changes to the underlying data or measure logic will be reflected in Power BI.
- If schema changes occur, such as the addition of new dimensions and measures, the steps outlined above will need to be repeated.

## Best practices

Adhering to best practices ensures that you effectively utilize the Data Product Hub and maintain compatibility with the latest features and updates. Following these guidelines will help optimize your workflow, enhance performance, and prevent potential issues.

### **Version compatibility**

- Power BI versions released after **June 15, 2023**, support `.pbib` files. It is advisable to use a version released after this date.

- Beginning with Version 2.132.908.0 (August 2024), `.pbip` files have moved from preview to general availability. This transition allows for the use of `.pbip` files without the need to enable any preview settings. It is strongly recommended to download Power BI Version 2.132.908.0 or later to fully utilize `.pbip` files. 

<!-- 
In earlier versions, enabling a preview feature was necessary, but this is no longer required in the latest version. -->

### **File handling**

Ensure that `.pbip` folders are fully extracted before opening them. Failure to do so may result in missing file errors, as shown below:

<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/image.png" alt="Superset Configuration" style="max-width: 60%; height: auto; border: 1px solid #000;">
</div>

### **Data retrieval and field selection considerations**

- **Row Limit:** The Lens API has a maximum return limit of 50,000 rows per request. To obtain additional data, it is necessary to set an offset. This row limit is in place to manage resources efficiently and ensure optimal performance.

- **Selection:** It is important to select fields from tables that are directly related or logically joined, as the system does not automatically identify relationships between tables through transitive joins. Selecting fields from unrelated tables may result in incorrect or incomplete results.


### **Data policies and security**

Data masking, restrictions, or permissions established by the publisher are automatically enforced for all report viewers, ensuring consistent data security and compliance. The behavior of these data policies, such as masking, may vary based on the user of the Power BI desktop.

### **Regular testing and validation**

Regular testing and validation of reports are recommended after changes are made to the Lens definitions. This practice ensures that updates to dimensions, measures, or data models are accurately reflected in the reports and helps identify any issues early in the process.


---

## Governance of Model on Power BI

When the Lens Model is activated via BI Sync on Power BI, the process is handled through authentication and authorization using the DataOS user ID and API key when accessing synced data models. This ensures that columns redacted by Lens data policies are restricted based on the user's group permissions.

For instance, if a user named **iamgroot** in the "**Analyst**" group is restricted from viewing the "Annual Salary" column, this column will not be visible in either the Data Product exploration page or in PowerBI after syncing. Power BI requires the DataOS user ID and API key for authentication, ensuring that users can access the full model, except for any columns restricted by their data policies. This approach maintains security and guarantees that users only see the data they are authorized to view.
