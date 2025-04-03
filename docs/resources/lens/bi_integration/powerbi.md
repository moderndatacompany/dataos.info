---
title: Semantic model sync with Power BI
search:
  exclude: true
---

# Semantic model sync with Power BI

The semantic model can be integrated with Power BI using the following ways:

- [Using Data Product Hub(Recommended - GUI based)](/resources/lens/bi_integration/#using-data-product-hub): Download `.pbip` file through an intuitive graphical interface.

- [Using cURL command (Command-Line based)](/resources/lens/bi_integration/#using-curl-command): Download `.pbip` Power BI connection via cURL command.


## Using Data Product Hub

### Prerequisite

- **Power BI Desktop version:** Use `2.132.908.0` or later.

- **DataOS API Key:** Obtain your key from DPH Page > Profile Icon (bottom-left) > Name/Email > Tokens Tab.

    - If no API key is listed, click **`+Add API Key`**, provide a name for the token, and set an expiration duration (e.g., 24h or a specific date).

    - Once the key appears, click the eye icon to reveal it, then click the API key to copy.

Follow the below steps to integrate semantic model with Power BI using Data Product Hub:

### **Step 1: Navigate to the Data Product Hub**

Access the Home Page of DataOS. Click on Data Product Hub to explore the various Data Products available within the platform.

<img src="/resources/lens/bi_integration/powerbi(1).png" alt="DPH" style="width:40rem; border: 1px solid black;" />

### **Step 2: Browse and select a Data Product**

Browse the list of Data Products and select a specific Data Product to initiate integration with Power BI. For instance 'Productaffinity'.

<img src="/resources/lens/bi_integration/powerbi(2).png" alt="DPH" style="width:40rem; border: 1px solid black;" />


### **Step 3: Access integration options**

Navigate to the Access options > BI Sync > Excel and Power BI. Click the Download `.pbip` file button to download the ZIP folder.

<img src="/resources/lens/bi_integration/powerbi(3).png" alt="DPH" style="width:40rem; border: 1px solid black;" />

### **Step 4: Download and open the ZIP file**

Access the downloaded ZIP file on the local system and extract its contents to the specified directory. The extracted folder will contain three files. Ensure all three files remain in the same directory to maintain semantic synchronization of the Data Product.

<img src="/resources/lens/bi_integration/extracted_files.png" alt="DPH" style="width:40rem; border: 1px solid black;" />

The folder contains the main components of a Power BI project for syncing the semantic model (here `productaffinity`) including folders such as the `.Report` and `.SemanticModel`. 

Following is the brief description of each:

* **public_productaffinity.Report:** This folder contains `definition.pbir` file related to the report definition in Power BI. These files define the visual representation of data, such as tables and charts, without storing actual data. They connect the semantic model and data sources to create the report views.

* **public_productaffinity.SemanticModel:** This folder contains files that define the underlying semantic model for your Power BI project. The semantic model plays a crucial role in managing how Power BI interacts with data, setting up relationships, hierarchies, and measures.

    * **definition.bism:** This file represents the Business Intelligence Semantic Model (BISM). It defines the structure of your data, including data sources, relationships, tables, and measures for your semantic model. The `.bism` file holds essential metadata that helps Power BI understand and query the data, forming the core of the semantic model for report creation and analysis.

    * **model.bim:** Power BI uses the `.bim` file to generate queries and manage interactions with the dataset. When you build reports or dashboards in Power BI, it references this semantic model to ensure the correct structure is applied to the data.

* **public_productaffinity** This file serves as a Power BI project template or configuration file. Power BI uses files `.pbip` or `.pbix` to encapsulate reports, datasets, and visualizations. The `.pbip` file ties together the semantic model and report definitions from the other folders, acting as the entry point for working on the project in Power BI Desktop or the Power BI service.


###  **Step 5: Enter credentials**

Open the `public_productaffinity` file in Power BI, and enter the DataOS username and API key when prompted. Click the connect button. A popup will appear; click OK.

![DPH](/interfaces/data_product_hub/activation/bi_sync/Untitled%20(16).png)

### **Step 6: View data in Power BI**

Once connected, users can explore tables and views containing dimensions and measures to build and customize dashboards.

![DPH](/interfaces/data_product_hub/activation/bi_sync/Untitled%20(19).png)

## Using cURL command

### **Prerequisites**

- **cURL**: Ensure you have `curl` installed on your system. Windows users may need to use `curl.exe`.

- **Power BI version:** Use `2.132.908.0` or later for full `.pbip` file support.

- **Lens API endpoint**: The API endpoint provided by Lens to sync semantic model, enabling integration with Power BI.

- **Power BI Desktop**: Ensure you have the Power BI Desktop app installed.

- **DataOS API key**: Ensure you have your DataOS API key. The API key can be obtained by executing the command below.

    ```bash
    dataos-ctl user apikey get
    ```

    If apikey is not listed already execute the below command to create one:

    ```bash
    dataos-ctl user apikey create #it will generate a apikey with default expiration time of 24h

    #or

    dataos-ctl user apikey create -n apikey_for_powerbi -d 48 h
    ```

### **cURL command**

Prepare the cURL command:

```bash
curl --location --request POST '${URL}' --header 'apikey: ${APIKEY}' --output ${FILE_NAME}.zip
```

**Parameters:**

1. **URL:**  This is the API endpoint for syncing semantic model with Power BI. It contains DATAOS FQDN, name and workspace of Lens (semantic model). 

    ```bash
    https://<DATAOS_FQDN>/lens2/sync/api/v1/power-bi/<workspace_name>:<lens_name> 
    ```

    - **DATAOS_FQDN:** Replace <DATAOS_FQDN> with the current Fully Qualified Domain Name (FQDN) where the Lens is deployed. For example, `liberal-donkey.dataos.app`,. is the FQDN and `liberal donkey` is the context name.

    - **WORKSPACE_NAME:** Replace <workspace_name> with the actual workspace where Lens has been deployed. for e.g., `public`, `sandbox`, `curriculum`.

    - **LENS_NAME:** The name of the semantic model. For example `productaffinity`.


2. **Headers:**

    - **apikey:** User's API key for the current context in Lens.

    The DataOS API key for the user can be obtained by executing the command below.

    ```bash
    dataos-ctl user apikey get
    ```


3. **Output:** Replace `${File_name}` placeholder with the file name to save the file for example `file`. A `file.zip` archive is downloaded, containing the main components of a Power BI project. The name of the zip file can be specified during the curl command execution, and it will be saved accordingly. 

The `file.zip` includes essential components for syncing a semantic model with Power BI, organized into folders such as `.Report` and `.SemanticModel`.

- **public_productaffinity.Report:** This folder contains the `definition.pbir` file, which is related to the report definition in Power BI. These files define the visual representation of data, such as tables and charts, without storing the actual data. They link the semantic model and data sources to create report views.

- **public-productaffinity.SemanticModel:** This folder includes files that establish the underlying data model for a Power BI project. The Semantic Model is crucial for managing data interactions, including the setup of relationships, hierarchies, and measures.

    - **definition.bism:** This file represents the Business Intelligence Semantic Model (BISM). It defines the structure of the data, detailing data sources, relationships, tables, and measures. The `.bism` file contains essential metadata that enables Power BI to understand and query the data, forming the foundation of the data model for report creation and analysis.

    - **model.bim:** The `.bim` file is utilized to generate queries and manage interactions with the dataset. This semantic model is referenced to ensure the correct structure is applied to the data during report or dashboard creation in Power BI.

- **public_productaffinity** This file serves as a Power BI project template or configuration file. Files such as `.pbip` or `.pbix` encapsulate reports, datasets, and visualizations. The `.pbip` file integrates the semantic model and report definitions from the other folders, acting as the entry point for project work in Power BI Desktop or the Power BI service.

<aside class="callout">

Ensure `file.zip` is fully extracted before opening. Failure to do so may result in missing file errors, as shown below:

<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/image.png" alt="Power BI Configuration" style="max-width: 25%; height: auto; border: 1px solid #000;">
</div>

</aside>

### **Steps**

To begin syncing the semantic model, the following steps should be followed:

**Step 1: Run the curl command:** For example, if the Lens named `productaffinity` is located in the `public` workspace deployed on the `liberal-donkey` context, the curl command would be:

```bash
curl --location --request POST 'https://tcp.liberal-donkey.dataos.app/lens2/sync/api/v1/power-bi/public:productaffinity' --header 'apikey: abcdefgh==' --output file.zip 
```

**Step 2 Download the zip file:**  Once the command is executed, a zip file will be downloaded to the specified directory. The downloaded file should be unzipped. Three folders will be found inside, all of which are necessary for semantic synchronization with Power BI.

<img src="/resources/lens/bi_integration/powerbi2.png" alt="Power BI Configuration" style="max-width: 40rem; height: auto; border: 1px solid #000;">

**Step 4 Open the Power BI file:** Open the Power BI file using Power BI Desktop.

<img src="/resources/lens/bi_integration/powerbi2.png" alt="Power BI Configuration" style="max-width: 40rem; height: auto; border: 1px solid #000;">

**Step 5 Enter credentials:**  After opening the file, a popup will prompt for credentials. The DataOS username and API key should be entered.

<img src="/resources/lens/bi_integration/powerbi4.png" alt="Power BI Configuration" style="max-width: 40rem; height: auto; border: 1px solid #000;">


**Step 6 Connect to DataOS:** Click on the connect button. A popup will appear. Click Ok.



<img src="/resources/lens/bi_integration/powerbi6.png" alt="Power BI Configuration" style="max-width: 40rem; height: auto; border: 1px solid #000;">


**Step 7 Access tables with dimensions and measures:** Upon successful connection, tables and views will be accessible, displaying dimensions and measures.



<img src="/resources/lens/bi_integration/powerbi7.png" alt="Power BI Configuration" style="max-width: 40rem; height: auto; border: 1px solid #000;">


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
- When schema changes occur, such as CRUD operations (Create, Read, Update, Delete) on dimensions, measures, or other elements of the semantic model, a re-sync is required. To prevent losing previously created reports after the re-sync, download the new `.pbip` zip file from the Data Product Hub, extract the zip file, and replace the existing folder with the new one.

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

### **Unknown cluster**

Whenever you encounter the error 'unknown cluster: <cluster_name>' as shown below, please check if the cluster has been deleted. If it has, redeploy the cluster. After redeploying the cluster, go to Power BI Desktop and click the 'Refresh' button to update the connection.

<img src="/interfaces/data_product_hub/activation/bi_sync/powerbi/cluster_error.png" alt="DPH" style="width:25rem; border: 1px solid black;" />

## Limitations

- Power BI fails to handle special characters (e.g., &, %, #) when generating queries through the synced semantic model, causing errors in visualizations. Thus, it is best practice to address or remove special characters directly in the data itself.
- Power BI's Direct Query mode does not support creating custom dimensions and measures or querying the rolling window measure due to the lack of date hierarchy.
- DAX functions and Import query mode are not supported.

## Governance of Semantic Model in Power BI integration

Data masking, restrictions, and permissions established by the publisher are automatically enforced for all report viewers, ensuring consistent data security and compliance. The behavior of these data policies, such as masking, may vary based on the user of Power BI Desktop.

When the Lens semantic model is activated via BI Sync on Power BI, authentication and authorization are handled using the DataOS user ID and API key. This ensures that columns redacted by Lens data policies are restricted based on the user's group permissions.

For example, if a user named iamgroot, belonging to the 'Analyst' group, is restricted from viewing the 'Annual Salary' column, this column will not appear in either the Data Product exploration page or in Power BI after synchronization. Power BI requires the DataOS user ID and API key for authentication, ensuring that users can access the full model except for columns restricted by their data policies.

This approach ensures that users only see the data they are authorized to view, maintaining security and compliance.