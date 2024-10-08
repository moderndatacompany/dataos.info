
# Power BI

## Prerequisites

- **Curl**: Ensure you have `curl` installed on your system. For Windows users, you may need to use `curl.exe`. 

- **Lens API Endpoint**: The API endpoint provided by Lens to sync the data with meta endpoint access.

- **Access Credentials**: For powerbi you will need access credentials such as username, password, and host.

- **DataOS API KEY:** : Ensure you have your DATAOS APIKEY.
    The DataOS API key for the user can be obtained by executing the command below.

    ```bash
    dataos-ctl user apikey get
    ```

**Curl Command**

```bash
curl --location --request POST **'<URL>'** --header 'apikey: <apikey>' --output <FILE_NAME>>.zip
```

**Paramters:**

1. **URL:**  This is the api endpoint for syncing lens with PowerBI. It contains dataos_fqdn, name and workspace of lens. 

    ```
    https://<DATAOS_FQDN>/lens2/sync/api/v1/powerbi/<lens_name> 
    ```

    - **DATAOS_FQDN:** Replace <DATAOS_FQDN> with the current Fully Qualified Domain Name (FQDN) where you have deployed your Lens instance. For example, if your FQDN is liberal-monkey.dataos.app,. In this case, `liberal monkey` would be your context name.

    - **WORKSPACE_NAME:** Replace <workspace_name> with the actual workspace where you have deployed your lens. for e.g., `public`, `sandbox`, `curriculum`.

    - **LENS_NAME:** The name of the Lens model that you wish to sync with Tableau. For example sales360.


2. **Headers:**

    - **apikey:** Your API key for the current context in Lens.


    The DataOS API key for the user can be obtained by executing the command below.

    ```bash
    dataos-ctl user apikey get
    ```


3. **Output**  This downloads a `file.zip` archive that stores the main components of a Power BI project. When running the curl command, you can specify any name for the zip file, and it will be downloaded with that name. The `file.zip` contains key components for syncing the Lens Model (here sales360) to Power BI, including folders like the `.Report` and `.SemanticModel`:

    - **public_sales360-table.Report:** This folder holds contains `definition.pbir` file related to the report definition in Power BI. These files define the visual representation of data, such as tables and charts, without storing actual data. They connect the semantic model and data sources to create the report views.

    - **public-sales360-table.SemanticModel:** This folder contains files that define the underlying data model for your Power BI project. The Semantic Model plays a crucial role in managing how Power BI interacts with data, setting up relationships, hierarchies, and measures.

        - **definition.bism:** This file represents the Business Intelligence Semantic Model (BISM). It defines the structure of your data, including data sources, relationships, tables, and measures for your Lens Model. The `.bism` file holds essential metadata that helps Power BI understand and query the data, forming the core of the data model for report creation and analysis.

        - **model.bim:** Power BI uses the `.bim` file to generate queries and manage interactions with the dataset. When you build reports or dashboards in Power BI, it references this semantic model to ensure the correct structure is applied to the data.

    - **public-sales-360-table.pbip:** This file serves as a Power BI project template or configuration file. Power BI uses files like `.pbip` or `.pbix` to encapsulate reports, datasets, and visualizations. The `.pbip` file ties together the semantic model and report definitions from the other folders, acting as the entry point for working on the project in Power BI Desktop or the Power BI service.


## Steps

To begin syncing your Lens model follow the below steps:


**Step 1 Run the curl command:** For instance, if the lens `sales360` is in `curriculum` workspace deployed on `liberal-monkey` context which you want to download with name `sales` in your local machine then the curl command will be:


```bash
curl --location --request POST 'https://liberal-monkey.dataos.app/lens2/sync/api/v1/powerbi/curriculum:sales360' --header 'apikey: abcdefgh==' --output file.zip 
```

**Step 2 Download the Zip File:** After running the command, a zip file will be downloaded to your chosen directory.

<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/powerbi1.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>


**Step 3 Unzip the File:** Unzip the file. You will find three folders. All folders and files are necessary for a semantic sync with PowerBI.

<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/powerbi2.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

**Step 4 Open the Power BI File:** Open the Power BI file using Power BI Desktop.

<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/powerbi3.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

**Step 5 Enter Credentials:** Once the file is opened, you will see a popup. Enter your DataOS username and API key.

<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/powerbi4.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/powerbi5.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

**Step 6 Connect to DataOS:** Click the connect button. A popup will appear. Click OK.


<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/powerbi6.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

**Step 7 Access Tables with Dimensions and Measures:** After connecting, you will be able to see tables and views with dimensions and measures.


<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/powerbi7.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>


## **Important Considerations**

- Measures will be named in Power BI as **`m_total_revenue`**.
- The connection is live, so any changes to the underlying data or measure logic will reflect in Power BI.
- If there are schema changes, such as adding new dimensions and measures, you will need to repeat the steps above.


## Best practices

### **Version Compatibility**

- Power BI versions released after **June 15, 2023**, support .pbib files, make sure you're using a version released after this date.

- Starting with Version 2.132.908.0 (August 2024), .pbip files have transitioned from preview to general availability. This update allows you to use .pbip files without needing to enable any preview settings. We strongly recommend that you download Power BI Version 2.132.908.0 or later to fully utilize .pbip files. In earlier versions, you would need to manually enable a preview feature, but this is no longer required in the latest version.


### **File Handling**

Ensure that .pbip folders are fully extracted before opening them. Failure to do so may result in missing file errors, as shown below:

<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/image.png" alt="Superset Configuration" style="max-width: 60%; height: auto; border: 1px solid #000;">
</div>

### **Data Retrieval and Field Selection Considerations**

- **Row Limit:** The Lens API will return a maximum of 50,000 rows in a single request. To retrieve additional data, you will need to set an offset. This row limit helps manage resources efficiently and ensures optimal performance.

- **Selection** Ensure that you select fields from tables that are directly related or logically joined, as the system does not automatically detect relationships between tables through transitive joins. This means that if you select fields from tables that are not directly connected, you may receive incorrect or incomplete results.

### **Data Policies and Security**

- Any data masking, restrictions, or permissions defined by the publisher will automatically be enforced for all viewers of the report, ensuring consistent data security and compliance. However, the behavior of data policies (e.g., masking) depends on who is the user of the PowerBI desktop.

### **Regular Testing and Validation**

It is recommended to regularly test and validate your reports after making changes to the Lens definitions. This ensures that all updates to dimensions, measures, or data models are correctly reflected in the reports, and helps identify any issues early in the process.