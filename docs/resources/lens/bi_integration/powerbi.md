# Power BI

## Prerequisites

- **Curl**: Ensure you have `curl` installed on your system. Windows users may need to use `curl.exe`.

- **Lens API endpoint**: The API endpoint provided by Lens to sync data with meta endpoint access.

- **Access credentials**: You will need access credentials such as username, password, and host for Power BI.

- **DataOS API key**: Ensure you have your DataOS API key. The API key can be obtained by executing the command below.

    ```bash
    dataos-ctl user apikey get
    ```

**Curl command**

```bash
curl --location --request POST '${URL}' --header 'apikey: ${APIKEY}' --output ${FILE_NAME}.zip
```

**Paramters:**

1. **URL:**  This is the api endpoint for syncing lens with PowerBI. It contains dataos_fqdn, name and workspace of lens. 

    ```bash
    https://<DATAOS_FQDN>/lens2/sync/api/v1/power-bi/<lens_name> 
    ```

    - **DATAOS_FQDN:** Replace <DATAOS_FQDN> with the current Fully Qualified Domain Name (FQDN) where the Lens is deployed. For example, liberal-monkey.dataos.app,. is the FQDN and `liberal monkey` is the context name.

    - **WORKSPACE_NAME:** Replace <workspace_name> with the actual workspace where Lens has been deployed. for e.g., `public`, `sandbox`, `curriculum`.

    - **LENS_NAME:** The name of the Lens model to be synced with Tableau. For example sales360.


2. **Headers:**

    - **apikey:** User's API key for the current context in Lens.


    The DataOS API key for the user can be obtained by executing the command below.

    ```bash
    dataos-ctl user apikey get
    ```

3. **Output:** A `file.zip` archive is downloaded, containing the main components of a Power BI project. The name of the zip file can be specified during the curl command execution, and it will be saved accordingly. The `file.zip` includes essential components for syncing a Lens Model with Power BI, organized into folders such as `.Report` and `.SemanticModel`:

- **public_sales360-table.Report:** This folder contains the `definition.pbir` file, which is related to the report definition in Power BI. These files define the visual representation of data, such as tables and charts, without storing the actual data. They link the semantic model and data sources to create report views.

- **public-sales360-table.SemanticModel:** This folder includes files that establish the underlying data model for a Power BI project. The Semantic Model is crucial for managing data interactions, including the setup of relationships, hierarchies, and measures.

    - **definition.bism:** This file represents the Business Intelligence Semantic Model (BISM). It defines the structure of the data, detailing data sources, relationships, tables, and measures. The `.bism` file contains essential metadata that enables Power BI to understand and query the data, forming the foundation of the data model for report creation and analysis.

    - **model.bim:** The `.bim` file is utilized to generate queries and manage interactions with the dataset. This semantic model is referenced to ensure the correct structure is applied to the data during report or dashboard creation in Power BI.

- **public-sales-360-table.pbip:** This file serves as a Power BI project template or configuration file. Files such as `.pbip` or `.pbix` encapsulate reports, datasets, and visualizations. The `.pbip` file integrates the semantic model and report definitions from the other folders, acting as the entry point for project work in Power BI Desktop or the Power BI service.

## Steps

To begin syncing a Lens model, the following steps should be followed:

**Step 1: Run the curl command:** For example, if the lens named `sales360` is located in the `curriculum` workspace deployed on the `liberal-monkey` context, the curl command would be:

```bash
curl --location --request POST 'https://liberal-monkey.dataos.app/lens2/sync/api/v1/power-bi/curriculum:sales360' --header 'apikey: abcdefgh==' --output file.zip 
```

**Step 2 Download the zip file:**  Once the command is executed, a zip file will be downloaded to the specified directory.

<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/powerbi1.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>


**Step 3 Unzip the file:** The downloaded file should be unzipped. Three folders will be found inside, all of which are necessary for semantic synchronization with Power BI.

<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/powerbi2.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

**Step 4 Open the PowerBI file:** Open the Power BI file using Power BI Desktop.

<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/powerbi3.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

**Step 5 Enter credentials:**  After opening the file, a popup will prompt for credentials. The DataOS username and API key should be entered.

<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/powerbi4.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/powerbi5.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

**Step 6 Connect to DataOS:** Click on the connect button. A popup will appear. Click OK.


<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/powerbi6.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

**Step 7 Access tables with dimensions and measures:** Upon successful connection, tables and views will be accessible, displaying dimensions and measures.


<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/powerbi7.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

## Important considerations

- Measures in Power BI are typically named as **`m_total_revenue`**.
- The connection is live, meaning any changes to the underlying data or measure logic will be reflected in Power BI.
- If schema changes occur, such as the addition of new dimensions and measures, the steps outlined above will need to be repeated.

## Best practices

Adhering to best practices ensures that you effectively utilize the Data Product Hub and maintain compatibility with the latest features and updates. Following these guidelines will help optimize your workflow, enhance performance, and prevent potential issues.

### **Version compatibility**

- Power BI versions released after **June 15, 2023**, support .pbib files. It is advisable to use a version released after this date.

- Beginning with Version 2.132.908.0 (August 2024), .pbip files have moved from preview to general availability. This transition allows for the use of .pbip files without the need to enable any preview settings. It is strongly recommended to download Power BI Version 2.132.908.0 or later to fully utilize .pbip files. In earlier versions, enabling a preview feature was necessary, but this is no longer required in the latest version.

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
