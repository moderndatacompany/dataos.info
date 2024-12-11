# Power BI Integration

The following document outlines the process for integrating Power BI with DataOS.

## Steps

Follow the below steps:

### **Step 1: Navigate to the Data Product Hub**

Access the Home Page of DataOS. From there, navigate to the Data Product Hub to explore the various Data Products available within the platform.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/image%20(1).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

### **Step 2: Browse and select a Data Product**

Browse the list of Data Products and select a specific Data Product to initiate integration with Power BI. For example, selecting 'Sales360' allows detailed exploration and integration of the Sales360 Data Product.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/image%20(2).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

### **Step 3: Access integration options**

Go to the BI Sync option under the Access Options tab. Scroll down to locate the Excel and Power BI section, and click the Download .pbip File button to download the ZIP folder.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/powerbi/Powerbi3.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

### **Step 4: Download and open the ZIP file**

Access the downloaded ZIP file on the local system and extract its contents to the specified directory. The extracted folder will contain three files. Ensure all three files remain in the same directory to maintain semantic synchronization of the Data Product.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/Untitled%20(15).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

The folder contains the main components of a Power BI project for syncing the Lens model (here `sales360`) including folders like the `.Report` and `.SemanticModel`. Following is the brief description of each:

- **public_sales360-table.Report:** This folder contains `definition.pbir` file related to the report definition in Power BI. These files define the visual representation of data, such as tables and charts, without storing actual data. They connect the semantic model and data sources to create the report views.

- **public-sales360-table.SemanticModel:** This folder contains files that define the underlying data model for your Power BI project. The semantic model plays a crucial role in managing how Power BI interacts with data, setting up relationships, hierarchies, and measures.

    - **definition.bism:** This file represents the Business Intelligence Semantic Model (BISM). It defines the structure of your data, including data sources, relationships, tables, and measures for your Lens semantic model. The `.bism` file holds essential metadata that helps Power BI understand and query the data, forming the core of the data model for report creation and analysis.

    - **model.bim:** Power BI uses the `.bim` file to generate queries and manage interactions with the dataset. When you build reports or dashboards in Power BI, it references this semantic model to ensure the correct structure is applied to the data.

- **public-sales-360-table.pbip:** This file serves as a Power BI project template or configuration file. Power BI uses files like `.pbip` or `.pbix` to encapsulate reports, datasets, and visualizations. The `.pbip` file ties together the semantic model and report definitions from the other folders, acting as the entry point for working on the project in Power BI Desktop or the Power BI service.

### **Step 5: Enter credentials**

Open the `public_sales360` file in Power BI, once the file is opened, a popup will appear prompting for the DataOS username and API key.

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


## Supported data types

| **Category**   | **Data Types**                                                                  | **Support Status**                       |
|----------------|---------------------------------------------------------------------------------|------------------------------------------|
| **Dimension**  | `time`, `string`, `number`, `boolean`                                                   | Supported                                |
| **Measure**    | `max`, `min`, `number`, `sum`, `count`, `boolean`, `string`, `time`, `avg`, `count_distinct`         | Supported                                |
| **Measure**    | `count_distinct_approx`                                                           | Not Supported                            |
| **Rolling Window** | -                                                                           | Not Supported (Power BI doesn’t support) |

## Important considerations

- In Power BI, measures typically have an 'm_' prefix to indicate they represent a measure. For example, a measure calculating total revenue might be named `m_total_revenue`.
- The connection is live, meaning any changes to the underlying data or measure logic will be reflected in Power BI.
- If schema changes occur, such as the addition of new dimensions and measures, the steps outlined above will need to be repeated.
- Custom measures or dimensions created in Power BI may be lost during re-sync operations. It is recommended to implement custom logic directly within the Lens when possible to ensure persistence of customizations.

## Best practices

Adhering to best practices ensures that you effectively utilize the Data Product Hub and maintain compatibility with the latest features and updates. Following these guidelines will help optimize workflow, enhance performance, and prevent potential issues.

### **Version compatibility**

- Power BI versions released after June 15, 2023, support `.pbib` files. It is advisable to use a version released after this date.

- Beginning with Version 2.132.908.0 (August 2024), `.pbip` files have moved from preview to general availability. This transition allows for the use of `.pbip` files without the need to enable any preview settings. It is strongly recommended to download Power BI Version 2.132.908.0 or later to fully utilize `.pbip` files. 

<!-- 
In earlier versions, enabling a preview feature was necessary, but this is no longer required in the latest version. -->

### **File handling**

Ensure that `.pbip` folders are fully extracted before opening them. Failure to do so may result in missing file errors, as shown below:

<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/image.png" alt="Superset Configuration" style="max-width: 25%; height: auto; border: 1px solid #000;">
</div>

### **Data retrieval and field selection considerations**

- **Row Limit:** The Lens API has a maximum return limit of 50,000 rows per request. To obtain additional data, it is necessary to set an offset. This row limit is in place to manage resources efficiently and ensure optimal performance.

- **Selection:** It is important to select fields from tables that are directly related or logically joined, as the system does not automatically identify relationships between tables through transitive joins. Selecting fields from unrelated tables may result in incorrect or incomplete results.

### **Regular testing and validation**

Regular testing and validation of reports are recommended after changes are made to the Lens definitions. This practice ensures that updates to dimensions, measures, or data models are accurately reflected in the reports and helps identify any issues early in the process.

## Limitations

Power BI’s ‘Direct Query’ mode does not support querying the rolling window measure. The lack of support for date hierarchy in 'Direct Query' prevents the application of granularity for the rolling window measure type.

## Governance of model on Power BI

Data masking, restrictions, and permissions established by the publisher are automatically enforced for all report viewers, ensuring consistent data security and compliance. The behavior of these data policies, such as masking, may vary based on the use of Power BI Desktop or other interfaces.

When the Lens semantic model is activated via BI Sync on Power BI, authentication and authorization are handled using the DataOS user ID and API key. This ensures that columns redacted by Lens data policies are restricted based on the user's group permissions.

For example, if a user named iamgroot, belonging to the 'Analyst' group, is restricted from viewing the 'Annual Salary' column, this column will not appear in either the Data Product exploration page or in Power BI after synchronization. Power BI requires the DataOS user ID and API key for authentication, ensuring that users can access the full model except for columns restricted by their data policies.

This approach ensures that users only see the data they are authorized to view, maintaining security and compliance.






