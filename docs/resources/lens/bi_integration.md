# BI Integrations 

**Pre-requisites**

- **Curl**: Ensure you have `curl` installed on your system. For Windows users, you may need to use `curl.exe`. 
- **Lens API Endpoint**: The API endpoint provided by Lens to sync the data with meta endpoint access.
- **Access Credentials**: For bi tools you will need access credentials such as username, password, and host.
- **DATA_OS API KEY:** : Ensure you have your DATAOS APIKEY.
    The DataOS API key for the user can be obtained by executing the command below.
    ```bash
    dataos-ctl user apikey get
    ```

## Superset

The following `curl` command is used to synchronize data from Lens to a Superset. It posts configuration details required for integration.

**Step 1 Run the curl command:** To sync your Lens model with Superset, execute the following curl command:

=== "Syntax"

    ```bash
    curl --location --request POST 'https://<DATAOS_FQDN>/lens2/sync/api/v1/superset/public:<LENS-NAME>' \
    --header 'apikey: <apikey>' \
    --header 'Content-Type: application/json' \
    --data-raw '
    {
        "username": "<superset username>",
        "password": "<superset password>",
        "host": "https://superset-<DATAOS_FQDN>"
    }
    ```

=== "Example"

    ```bash
    curl --location --request POST 'https://liberal-donkey.dataos.app/lens2/sync/api/v1/superset/public:company-intelligence' \
    --header 'apikey: abcdefghijkQq=' \
    --header 'Content-Type: application/json' \
    --data-raw '
    {
        "username": "adder_1",
        "password": "adder_1",
        "host": "https://superset-liberal-donkey.dataos.app""
    }
    ```

**Command Parameters:**

- **`URL`**: `https://liberal-donkey.dataos.app/lens2/sync/api/v1/superset/public:sales360` This is the endpoint for syncing with Superset.

- **`DataOS FQDN`: any current DataOS  FQDN. For example,** `liberal-donkey.dataos.app`

- **`--header 'Content-Type: application/json'`**: This specifies the content type as JSON.

- **`Lens_Name`: Your lens name. Example `sales360`.**

- **`API_Key`: Your DataOS API key in your `docker-compose.yaml`.**

Upon initiation, you will receive a response:

```bash
{
    "message": "started"
}
...
{
    "message": "Superset project creation and sync completed successfully."
}
```

Once you execute the command in the terminal, the results will be visible in the Superset app, as demonstrated below:

Please follow the steps outlined to see the result:

**Step 2 Go to DataOS**: Select Superset.

  <div style="text-align: center;">
      <img src="/resources/lens/bi_integration/superset2.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
  </div>

**Step 3 Navigate to Datasets Tab:** Here, each entity will be available in the form of datasets.

  <div style="text-align: center;">
      <img src="/resources/lens/bi_integration/superset3.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
  </div>

Everything is set up now. Explore and perform further analysis in Superset.

## Tableau

### **Prerequisites**

- Tableau Credentials
- DataOS username(User Id)
- DataOS API Key

To sync your Lens model with Tableau, execute the following curl command:

**Step 1: Run the curl command**

To sync your Lens model with Tableau, you need the following credentials:

```bash
curl --location --request POST 'http://127.0.0.1:5000/lens2/sync/api/v1/tableau/public:company-intelligence' \
--header 'apikey: <apikey>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "project_name": "sample",
    "username": "user1",
    "password": "password1",
    "site_id": "site1",
    "server_address": "https://prod-apnortheast-a.online.tableau.com"
}'
```

**Command Parameters:**

**`<URL>`:** This endpoint is used to sync a specified Lens model to Tableau for public access. 

**Parameters**

**`DATAOS_FQDN`**: Replace `<DATAOS_FQDN>` with the current Fully Qualified Domain Name (FQDN) where you have deployed your Lens instance. For example, if your FQDN is `liberal-monkey.dataos.app`, replace it accordingly. In this case, "liberal monkey" would be your context name.

**`<LENS_NAME>`**: The name of the Lens model that you wish to sync with Tableau. For example `sales360`.

**`<apikey>`**:  your apikey of the current context.

**`H "Content-Type: application/json"`:** This header specifies that the data being sent is in JSON format.

**`-data-raw`:** Sends the raw JSON payload directly to the server:

- `project_name`: Replace `<PROJECT_NAME>` with the Tableau project name.
- `username`: The Tableau username.
- `password`: The password associated with the Tableau account.
- `site_id`: The site ID, in this case `tableausuer@123`.
- `server_address`: The address of the Tableau server (e.g., `https://prod-apnortheast-a.online.tableau.com`). Tableau server config are only needed in case of user wants to publish generated tds files at tableau server.

You can obtain these when you **log in** to Tableau. You’ll see the **URL** like below:

https://prod-apnortheast-a.online.tableau.com/#/site/iamgroot1086a891fef336/home

here: **iamgroot1086a891fef336**  is your **site_id.**


```bash
{
"project_name": "tableau project name" ,
"username": "tableau username", 
"password": "tableau password",
"site_id": "tableau site id",
"server_address": "https://prod-apnortheast-a.online.tableau.com"
}
```

**Step 2 Go to tableau:** Go to the Explore tab on the left side. You’ll see the required tables and views in your project.In the screenshot below, there are three sources: one for tables and two for views.

<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/tableau1.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

**Step 3 Explore and Create Visualizations:** Go to the Home tab on the left side and click on 'New'. Under it, click on 'Workbook'.


<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/tableau2.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

**Step 4 Connect to Data:** Once you click on 'Workbook', it’ll take you to 'Connect to Data'. Select either views or tables and click on 'Connect'.


<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/tableau3.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>


As you click on 'Connect', it’ll ask you for username and password. Enter the **DataOS username and API key**


<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/tableau4.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

**Step 5 Start Using the Model:** Once you enter the credentials and click on 'Sign In', you’re ready to use the model for your visualization purposes.

<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/tableau5.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

### **Important Considerations for Tableau Integration**

1. **Building Connections Twice**: For views and tables, you need to establish the connection twice to ensure proper integration with Tableau.
2. **Handling Entities Without Relationships**: If any entity in the data model lacks a defined relationship, an error will occur during synchronization. To resolve this, you can hide the entity to avoid errors.
3. **Live Connection**: The connection between the Lens semantic layer and Tableau Cloud is live, meaning any changes to the underlying data or measure logic will automatically reflect in Tableau.
4. **Schema Changes**: If there are any schema updates, such as the addition of new dimensions or measures, you will need to repeat the integration steps to incorporate these changes into Tableau.
5. **Avoiding Cyclic Dependencies**: Tableau does not support cyclic dependencies within data models. Before syncing with Tableau, ensure that your data model is free of any cyclic dependencies to avoid integration issues.

### **Handling Specific Data Types in Tableau**

1. **Time Data Type as Measure in Tableau**  

    When syncing the Lens semantic layer with Tableau, note that Tableau does not support the time data type as a measure. While Lens allows time-based measures, Tableau defaults to treating date and time fields as dimensions.As a result, Tableau will not correctly interpret any measure with a **time data type**.


    **Recommended Actions**:

    To avoid synchronization issues:

    - Use time or date fields in Tableau only for **dimension-based** filtering or grouping.
    - For time-based calculations, limit aggregations to **MIN()** or **MAX()** functions.
    <aside class="callout">
    📌 This limitation is specific to Tableau's handling of time data types as measures and does not affect other aspects of the Lens semantic layer's functionality.

    </aside>

2. **String Data Type to Geographical**

When connecting a dataset to Tableau, it automatically detects fields such as **City** and **Country** and converts them from string data types to **Geography** types. This enables Tableau to treat these fields as geographical locations, allowing features like map visualizations and geospatial analysis without the need for manual adjustments.

## Power BI

**Step 1 Run the curl command:** To sync your Lens model with Power BI, execute the following curl command in your terminal:

```bash
curl --location --request POST 'https://liberal-donkey.dataos.app/lens2/sync/api/v1/powerbi/public:sales360' --header 'apikey: <apikey>'
```

```yaml
https://liberal-donkey.dataos.app/lens2/sync/api/v1/<source_name>/<lens_name> --header 'apikey: <apikey>'
```

**Step 2 Download the Zip File:** After running the command, a zip file will be downloaded to your chosen directory.

<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/powerbi1.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>



**Step 3 Unzip the File:** Unzip the file. You will find three folders inside.


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

**Note:**

- Measures will be named in Power BI as `m_total_revenue`.
- The connection is live, so any changes to the underlying data or measure logic will reflect in Power BI.
- If there are schema changes, such as adding new dimensions and measures, you will need to repeat the steps above.

## Excel

**Step 1 Install the Analyze in Excel Feature:** Visit the [Analyze in Excel for Power BI Desktop](https://www.sqlbi.com/tools/analyze-in-excel-for-power-bi-desktop/) link and follow the instructions to download and install the necessary extension.

**Step 2 Use the Analyze in Excel Feature:** Once the extension is installed, a new tab labeled "Analyze in Excel" will appear in Power BI Desktop.

<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/excel1.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

**Step 3 Export to Excel:**

- Click on the "Analyze in Excel" tab.
- This action will open Excel and establish a connection to the Power BI dataset or report.

**Step 4 Verify Power BI is Running:** Ensure that Power BI Desktop remains open while you are working in Excel, as Power BI acts as the server for the data connection.

**Step 5 Work in Excel:** In Excel, you can now use PivotTables, charts, and other Excel features to analyze the data coming from Power BI.

<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/excel2.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>