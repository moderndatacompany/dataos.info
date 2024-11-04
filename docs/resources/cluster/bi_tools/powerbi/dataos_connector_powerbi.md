---
search:
  exclude: true
---

# DataOS Power BI Connector

The DataOS connector is engineered to facilitate integration between the DataOS platform and Power BI. It provides an additional interface for accessing data from DataOS and leveraging Power BI's visualization and dashboarding capabilities.

This connector uses the Minerva query engine to channel data from DataOS into Power BI for exploration and analysis. Initially, users need to configure the connection settings. These settings enable Power BI to establish a secure and reliable connection to DataOS.

With the connector set up, users can start designing queries within Power BI. When a query is submitted from Power BI, the DataOS connector acts as an intermediary and sends it to the Minerva cluster for processing. Minerva then performs distributed SQL queries across connected data sources, potentially spanning multiple data lakes, databases, or external data services and returns the results to the connector. The selection of the appropriate Minerva cluster is automated and guided by a predefined criterion, which factors in sources(query origins), priority, and alphabetical order. In scenarios where these criteria are not applicable, a default cluster is designated for query execution. 

End users have the capability to execute queries on any data source, provided a corresponding depot is established or a connector configuration is done for the data source to access it as a ‘catalog’ within the selected Minerva cluster. Additionally, it supports the execution of Lens queries within Power BI.

The DataOs connector functions in alignment with existing data and access policies. Users can confidently explore and analyze data from DataOS within Power BI, adhering to access policy decisions and data governance through data policy decisions such as masking and filtering of data.

## Prerequisites

- Contact your customer success representative to obtain the connector installer file.
- DataOS API key is required to authenticate and access DataOS from the Power BI interface. To learn more about generating an API key/token, refer to [Create API Key](https://dataos.info/interfaces/create_token/).

<aside class="callout">
🗣 Please note that this custom connector is designed to integrate DataOS with Power BI Desktop only and is not compatible with other Power BI versions.</aside>

The following section contains further information about configuring this connector to retrieve and analyze data from DataOS within Power BI Desktop.

## Installation of DataOS connector

1. Run the connector installer file.

    <center>
      <div style="text-align: center;">
        <img src="/resources/cluster/bi_tools/powerbi/powerbi_custom_connector/installer.png" alt="Connector installer" style="width: 40rem; border: 1px solid black;">
        <figcaption>Connector installer</figcaption>
      </div>
    </center>

    <center>
      <div style="text-align: center;">
        <img src="/resources/cluster/bi_tools/tableau/integration-tableau-visualization.png" alt="Tableau visualization" style="width: 40rem; border: 1px solid black;">
        <figcaption>Tableau visualization</figcaption>
      </div>
    </center>


2. Click the **Next** button to proceed.

3. Choose a destination folder for the connector installation and click **Next**.

    <center>
      <div style="text-align: center;">
        <img src="/resources/cluster/bi_tools/powerbi/powerbi_custom_connector/destination_folder.png" alt="Selecting folder for installation" style="width: 40rem; border: 1px solid black;">
        <figcaption>Selecting folder for installation</figcaption>
      </div>
    </center>

4. Click **Install** to begin connector installation.

    <center>
      <div style="text-align: center;">
        <img src="/resources/cluster/bi_tools/powerbi/powerbi_custom_connector/begin_installation.png" alt="Connector installation process" style="width: 40rem; border: 1px solid black;">
        <figcaption>Connector installation process</figcaption>
      </div>
    </center>

5. Once the installation is complete, click the **Finish** button to exit the installer.

6. Open Power BI Desktop and navigate to **Get Data > More**. You should now see DataOS listed as an available data source.

    <center>
      <div style="text-align: center;">
        <img src="/resources/cluster/bi_tools/powerbi/powerbi_custom_connector/getdata_dataos_option.png" alt="Data sources" style="width: 40rem; border: 1px solid black;">
        <figcaption>Data sources</figcaption>
      </div>
    </center>

## Access data from DataOS on Power BI

Once DataOS appears as a data source in Power BI Desktop, data from DataOS can be accessed. There are two methods to retrieve datasets from DataOS:

### **Select tables from DataOS data lake**

1. Open Power BI Desktop and select **Get Data** > **More.**

2. Choose ‘DataOS’ from the list of available data sources.

    <center>
      <div style="text-align: center;">
        <img src="/resources/cluster/bi_tools/powerbi/powerbi_custom_connector/getdata_dataos.png" alt="DataOS as data source" style="width: 40rem; border: 1px solid black;">
        <figcaption>DataOS as data source</figcaption>
      </div>
    </center>

3. A pop-up appears. Fill in the required and optional fields to establish communication with your DataOS environment.
   - Basic connection information such as the URL of the DataOS instance, including the port used. Ask the DataOS administrator for this information. It is essential to provide the URL with `tcp` for TCP/IP connection.
   - Configure the following optional information, such as specific catalog, user, etc.

4. Leave the `Custom SQL Query` field blank.

5. Click "OK" to scan all objects and retrieve schema and tables within the selected catalog(s).

    <center>
      <div style="text-align: center;">
        <img src="/resources/cluster/bi_tools/powerbi/powerbi_custom_connector/connection_details.png" alt="Connect with DataOS" style="width: 40rem; border: 1px solid black;">
        <figcaption>Connect with DataOS</figcaption>
      </div>
    </center>

6. Enter your Username and Password (APIKEY) and proceed.

    <center>
      <div style="text-align: center;">
        <img src="/resources/cluster/bi_tools/powerbi/powerbi_custom_connector/username.png" alt="Credentials to connect" style="width: 40rem; border: 1px solid black;">
        <figcaption>Credentials to connect</figcaption>
      </div>
    </center>

7. Choose a table from the available list of catalogs and schemas. You'll be able to preview the data.

    <center>
      <div style="text-align: center;">
        <img src="/resources/cluster/bi_tools/powerbi/powerbi_custom_connector/catalogs.png" alt="Catalogs and schemas" style="width: 40rem; border: 1px solid black;">
        <figcaption>Catalogs and schemas</figcaption>
      </div>
    </center>

8. Click the 'Load' option to import the data. Subsequently, you can explore and craft visualizations within Power BI using the loaded data.

### **Fetch the result of a specific query**

1. Open Power BI Desktop and select **Get Data** > **More.**
2. Select ‘DataOS’ from the available data sources.
3. Provide connection information. Ask the DataOS administrator for the DataOS URL and port.
4. In the `Custom SQL Query` field, enter the desired query (or a Lens Query) and fill in the other mandatory fields.
        
    <center>
      <div style="text-align: center;">
        <img src="/resources/cluster/bi_tools/powerbi/powerbi_custom_connector/custom_query.png" alt="Query to get the result data" style="width: 40rem; border: 1px solid black;">
        <figcaption>Query to get the result data</figcaption>
      </div>
    </center>

    <aside class="callout">
    🗣 Ensure that you have access to the datasets mentioned in the query to avoid the “forbidden access” error. Reach out to the administrator to request access to the specific datasets mentioned in your query.
    </aside>

5. Enter your Username and Password (APIKEY) and press Enter.

6. The result of that query will be fetched instead of the catalog and table views and loaded into Power BI. Click on ‘Load’ to view the data.

    <center>
      <div style="text-align: center;">
        <img src="/resources/cluster/bi_tools/powerbi/powerbi_custom_connector/query_result.png" alt="Query result" style="width: 40rem; border: 1px solid black;">
        <figcaption>Query result</figcaption>
      </div>
    </center>

Once you have retrieved the data from DataOS into Power BI, you can create your dashboard(s) according to your business requirements.