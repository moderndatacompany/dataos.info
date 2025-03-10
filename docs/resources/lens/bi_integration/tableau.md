# Tableau

The semantic model can be integrated with Tableau using the following Ways

* [Using Data Product Hub(Recommended - GUI based)](/resources/lens/bi_integration/Tableau#using-data-product-hub): This method provides a user-friendly, graphical interface for integrating the semantic model with Tableau.  This approach is ideal for those who prefer an intuitive, no-code setup.

* [Using cURL command (Command-Line based)](/resources/lens/bi_integration/Tableau#using-curl-command): By executing a simple cURL request, users can fetch and connect the semantic model directly to Tableau. This method is suitable for advanced users looking to script or automate the integration process.

## Using Data Product Hub

### **Navigate to the Data Product Hub**

Access the Home Page of DataOS. From the home page, navigate to the Data Product Hub to explore the various Data Products available.

![](/image.png)


### **Browse and select a Data Product**

Browse through the list of available Data Products. Select a specific Data Product to integrate with Tableau. For instance, `Product360` can be chosen to explore the Data Product on Tableau for data visualisation and getting insights.

![DPH](https://dataos.info/interfaces/data_product_hub/activation/bi_sync/Tableau/Tableau0.png)

Browse through the list of available Data Products. Select a specific Data Product to integrate with Tableau. For instance, **Product 360** can be chosen to explore the Data Product on Tableau for data visualisation and getting insights.

![DPH](https://dataos.info/interfaces/data_product_hub/activation/bi_sync/Tableau/Tableau0.png)

### **Navigate to the Access Options tab**

After selecting a Data Product, navigate to the **BI Sync** option in the **Access Options** tab. Scroll through the BI Sync and locate the **Tableau Cloud** option. Now, Click on the **Add Connection** button

![DPH](https://dataos.info/interfaces/data_product_hub/activation/bi_sync/Tableau/Tableau1.png)


### **Enter connection details and click Activate button**

A connection window will open, prompting the entry of the necessary connection details. There are following two ways to pass the connection details:

=== "Using  username and password"

    Following are the connection details of the Tableau username and password:

    - **Project Name**: Enter the Tableau project name. If a project with that name does not already exist, it will be created automatically. If you do not specify a name, the project will default to the name of the Data Product, which will register all associated data sources under that project.
    For optimal organization within Tableau, we recommend providing a custom project name it facilitates easier navigation of your data sources.

    - **Server Name**: The address of the Tableau server (e.g., https://prod-apnortheast-a.online.tableau.com).

    - **Site ID**: The site ID (e.g., tableausuer@123).

    - **Username**: The Tableau username.(e.g., labs@tmdc.io)

    - **Password**: The password associated with the Tableau account.

    These details can be obtained upon logging into Tableau. The URL format will appear as follows:

    [`https://prod-apnortheast-a.online.tableau.com/#/site/site_id`](https://prod-apnortheast-a.online.tableau.com/#/site/tableauuser@123)

    **Sample URL**:

    [`https://prod-apnortheast-a.online.tableau.com/#/site/tableauuser@123/home`](https://prod-apnortheast-a.online.tableau.com/#/site/tableauuser@123/home)

    In this example, `tableuuser@123` represents the site_id.

    After entering the required credentials, click the Activate button to establish the connection. A confirmation message will appear upon successful connection.

=== "Using Personal Access Token"

    In addition to using standard Tableau credentials, users can also opt to use Personal Access Tokens (PAT) for authentication.

    #### **Prerequisites**

    **Tableau Personal Access Token (PAT):** Before integrating the semantic model with Tableau using a PAT, ensure that you generate a PAT in Tableau by following the instructions provided in [this guide](https://help.tableau.com/current/online/en-us/security_personal_access_tokens.htm).

    * **Project Name**: Enter the Tableau project name. If a project with that name does not already exist, it will be created automatically. If you do not specify a name, the project will default to the name of the Data Product, which will register all associated data sources under that project. For optimal organization within Tableau, we recommend providing a custom project name it facilitates easier navigation of your data sources.

    * **Server Name**: The address of the Tableau server (e.g., `https://prod-apnortheast-a.online.tableau.com`).

    * **Site ID**: The site ID (e.g., `tableausuer@123`).

    * **Username**: The Tableau username.(e.g., `labs@tmdc.io`)

    * **Password**: The password associated with the Tableau account.

    These details can be obtained upon logging into Tableau. The URL format will appear as follows:

    [`https://prod-apnortheast-a.online.tableau.com/#/site/site_id`](https://prod-apnortheast-a.online.tableau.com/#/site/tableauuser@123)

    **Sample URL**:

    [`https://prod-apnortheast-a.online.tableau.com/#/site/tableauuser@123/home`](https://prod-apnortheast-a.online.tableau.com/#/site/tableauuser@123/home)

    In this example, `tableuuser@123` represents the **site\_id**.

    After entering the required credentials, click the Activate button to establish the connection. A confirmation message will appear upon successful connection.

## Exploring the semantic model on Tableau

Once the sync is successful, the data source is published to the Tableau cloud/server:

### **Log in to Tableau Cloud**

Users should log in to Tableau Cloud using the same credentials of Tableau. This will redirect to the Tableau Cloud home page.

![DPH](https://dataos.info/interfaces/data_product_hub/activation/bi_sync/Tableau/Tableau5.png)


### **Manage projects**

Click on the Manage Projects option on the home page.

![DPH](https://dataos.info/interfaces/data_product_hub/activation/bi_sync/image%20\(13\).png)


### **Access the project interface**

This will open an interface displaying all projects, including the newly created project titled **Product Analysis**.

![DPH](https://dataos.info/interfaces/data_product_hub/activation/bi_sync/Tableau/Tableau5.1.png)


### **Select the project**

Click on the project to view the available data sources for dashboard creation. This project will contains semantic model and all it's views (entities and metrics).

![DPH](https://dataos.info/interfaces/data_product_hub/activation/bi_sync/Tableau/Tableau5.2.png)


### **Create a new workbook**

Click on the menu option in the upper right corner of the data source and select the New Workbook option.

![DPH](https://dataos.info/interfaces/data_product_hub/activation/bi_sync/Tableau/Tableau6.png)


### **Provide credentials**

To create a new workbook where dashboard creation can commence, users will be prompted to provide their DataOS username and API key as the password to access the data source. The API can be retrieved by navigating to the profile page in the bottom left corner of the Data Product Hub.

![DPH](https://dataos.info/interfaces/data_product_hub/activation/bi_sync/Tableau/Tabelau7.png)


### **Start creating the dashboard**

Now, users can create dashboard and extract relevant insights.

![DPH](https://dataos.info/interfaces/data_product_hub/activation/bi_sync/Tableau/tableau8.png)


### **Publishing workbook/dashboard**

The publisher can embed their credentials (DataOS username and API Token) or ask users to provide credentials whenever they want to access the published Workbook/Sheet/Dashboard. If the publisher has chosen to ‘Embed password for data source’, users can access the published workbook and dashboard without providing credentials.s

## Using cURL Command

### **Prerequisites**

- **Curl**: Ensure that `curl` is installed on the system. For Windows systems, `curl.exe` may be necessary.
- **Lens API endpoint**: The API endpoint provided by Lens to sync semantic model, enabling integration with Tableau.
- **Access credentials**: Access credentials such as username, password, project name etc., are required for Tableau.
- **DataOS API key**: Ensure the DataOS API key is available. Get it by using the following command:

```bash
dataos-ctl user apikey get
```

### **Steps**

To sync the semantic model with Tableau, follow the steps below:

**Step 1: Run the curl command**

```bash
curl --location --request POST 'http://tcp.<DATAOS_FQDN>/lens2/sync/api/v1/tableau-cloud/<WORKSPACE_NAME>:<LENS_NAME>' \
--header 'apikey: <APIKEY>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "project_name": "<SAMPLE>",
    "username": "{USER_NAME/EMAIL}",
    "password": "<PASSWORD>",
    "site_id": "<SITE_ID>",
    "server_address": "https://prod-apnortheast-a.online.tableau.com"
}'
```

1. **URL:**

    - This endpoint is used to sync a specific semantic model to Tableau for public access.
    - Replace <DATAOS_FQDN> with the Fully Qualified Domain Name (FQDN) where Lens is hosted. Example: liberal-monkey.dataos.app.
    - Replace <WORKSPACE_NAME> with the name of the workspace where the semantic model (Lens) is deployed. e.g., `public`, `curriculum`.
    - Replace <LENS_NAME> with the name of the semantic model to sync. e.g., `sales360`.

2. **Headers:**

    - **apikey:** User's API key for the current context in Lens. The DataOS API key for the user can be obtained by executing the below command.

        ```bash
        dataos-ctl user apikey get
        ```

    - **`Content-Type application/json`:** Specifies that the data being sent is in JSON format.
 
3. **Raw data payload:**

    This section defines the details of the user's Tableau credentials and project configuration:

    - **project_name:** The name of the Tableau project where the data will be synced. Replace "<sample>" with the actual project name. If the project does not already exist, Tableau will create a new project with the given name.

    - **username:** Tableau account username, typically the email ID used to log in to Tableau.

    - **password:** Tableau account password.
    
    - **site_id:** The site ID associated with the current Tableau connection.

    - **server_address:** The URL of the Tableau server.  Replace <server_address> with the correct server address (e.g., https://prod-apnortheast-a.online.tableau.com). This information can be obtained upon logging in to Tableau. The URL will appear as follows:

        > https://prod-apnortheast-a.online.tableau.com/#/site/iamgroot1086a891fef336/home

         Here: **iamgroot1086a891fef336**  is the **site_id**.

**Step 2: Go to Tableau:** Access the Explore tab on the left side. The required tables and views will be visible in the project. In the screenshot below, there are three sources: one for tables and two for views.

<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/tableau1.png" alt="Tableau Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

**Step 3: Explore and create visualizations** Navigate to the Home tab on the left side and click on 'New'. Under this option, select 'Workbook'.

<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/tableau2.png" alt="Tableau Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

**Step 4: Connect to data** After clicking on 'Workbook', the 'Connect to Data' page will be displayed. Select either views or tables and click on 'Connect'.

<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/tableau3.png" alt="Tableau Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

Upon clicking 'Connect', a prompt will request the username and password. Enter the DataOS username and API key.


<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/tableau4.png" alt="Tableau Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

**Step 5: Start using the semantic model** After entering the credentials and clicking on 'Sign In', the model will be ready for visualization purposes.

<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/tableau5.png" alt="Tableau Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>


<aside class="callout">
🗣️

The publisher can embed their credentials (DataOS username and API Token) or ask users to provide credentials whenever they want to access the published Workbook/Sheet/Dashboard. If the publisher has chosen to ‘Embed password for data source’, users can access the published workbook and dashboard without providing credentials.

Once the credentials are embedded, they cannot be accessed. You need to overwrite and ‘publish-as’ the workbook to reconfigure the embedding password optionality.

</aside>


## Supported data types

| Category        | Data Type              | Support Status                        | Recommended Approach                                                                 |
|-----------------|------------------------|---------------------------------------|--------------------------------------------------------------------------------------|
| Dimension       | `time`                 | Supported                             | NA                                                                                   |
| Dimension       | `string`               | Supported                             | NA                                                                                   |
| Dimension       | `number`               | Supported                             | NA                                                                                   |
| Dimension       | `boolean`              | Supported                             | NA                                                                                   |
| Measure         | `max`                  | Supported                             | NA                                                                                   |
| Measure         | `min`                  | Supported                             | NA                                                                                   |
| Measure         | `number`               | Supported                             | NA                                                                                   |
| Measure         | `sum`                  | Supported                             | NA                                                                                   |
| Measure         | `count`                | Supported                             | NA                                                                                   |
| Measure         | `boolean`              | Auto-converts to Dimension            | NA                                                                                   |
| Measure         | `string`               | Auto-converts to Dimension            | NA                                                                                   |
| Measure         | `time`                 | Auto-converts to Dimension            | NA                                                                                   |
| Measure         | `avg`                  | Not Supported                         | Option 1: To use measure of type ‘avg’, define an additional measure of type 'count' in that entity:<br>  <br>name: count<br>type: count<br>sql: '1'<br>  <br> Option 2: Use measure of type 'number' and define average logic in SQL:<br>  <br>measures:<br>&nbsp;&nbsp;- name: total_accounts<br> &nbsp;&nbsp;&nbsp; type: number<br> &nbsp;&nbsp;&nbsp; sql: "avg({accounts})”<br> |
| Measure        | `count_distinct`         | Not Supported                            | Option 1: To use measure of type ‘count_distinct’, additionally define a measure of type 'count' in that entity:<br>  <br>name: count<br>type: count<br>sql: '1'<br> <br> Option 2: Or, use measure of type 'number' and define logic for count_distinct in SQL:<br>  <br>measures:<br>&nbsp;&nbsp;- name: total_accounts<br> &nbsp;&nbsp;&nbsp; type: number<br> &nbsp;&nbsp;&nbsp; sql: "count(distinct({accounts}))”<br> |
| Measure         | `count_distinct_approx`| Not Supported                         | NA                                                                                   |
| Rolling Window  | -                      | Supported                             | NA                                                                                   |


## Important considerations for Tableau integration

**1. Handling Entities without Relationships:** An error will occur during synchronization if any entity in the data model lacks a defined relationship. To resolve this issue, the entity can be hidden to avoid synchronization errors.

**2. Live connection:** The connection between the Lens semantic layer and Tableau Cloud is live meaning that any changes to the underlying data will automatically be reflected in Tableau.

**3. Schema changes:** If there are schema updates, such as adding new dimensions or measures, the integration steps will need to be repeated to incorporate these changes into Tableau.

**4. Avoiding cyclic dependencies:** Tableau does not support cyclic dependencies within data models. To prevent integration issues, it is essential to ensure that the data model is free of cyclic dependencies prior to syncing with Tableau.

**5. Visualization with multiple data sources:** You cannot build a visualization that incorporates data from multiple data sources. For live connections, Tableau does not support data blending. Only a single data source can be used to create a visualization.

<!-- **6. Calculated Fields on Dimensions/Measures:** Any calculated field defined on top of a dimension or measure that is part of the semantic model is not supported. This means you cannot create custom calculations based on these predefined dimensions or measures within the semantic model. -->

**6. Centralized management:** All data sources should be managed and published by the admin on the server, with everyone else using this source.

**7. Single authority for Desktop publications:** If data sources are published via Tableau Desktop, ensure that all sources are published by a single authority to avoid multiple data source conflicts on the server.

**8. Row limit:** The Lens API has a maximum return limit of 50,000 rows per request. To obtain additional data, it is necessary to set an offset. This row limit is in place to manage resources efficiently and ensure optimal performance.

**9. Selection:** It is important to select fields from tables that are directly related or logically joined, as the system does not automatically identify relationships between tables through transitive joins. Selecting fields from unrelated tables may result in incorrect or incomplete results.

**10. Parameter Action:** Action filters can be defined on measures/dimensions to filter visualizations effectively.

**11. Default chart types:** All default chart types provided by Tableau can be plotted and visualized without issues.

**12. Rolling Window Measure:** For querying a rolling window measure, it is necessary to provide a time dimension and apply a date range filter to this time dimension. When querying a rolling window measure, follow these steps:

- Select the rolling window measure.
- Select the time dimension.
- To define granularity, right-click on the selected time dimension and set granularity (choose a granularity where the complete time, along with the year, is shown).
- Add the time dimension to the filter, and define the range filter.

<aside class="callout">
🗣️ Be aware that custom calculations or fields (measures/dimensions) created in BI tools may be lost during re-sync. It is preferable to create custom logic directly in Tableau's Lens.
</aside>

## Error handling 

**Scenario 1: Handling syntactical errors in measures or dimensions** 

If a measure or dimension contains a syntactical error (and is also not functioning in Explore studio of Data Product Hub), the following error will appear when attempting to select it:

<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/image02.png" alt="Tableau Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

After correcting the syntactical error in the measure or dimension within Lens, the error will no longer appear. To reflect the changes in Tableau, refreshing the data source and re-selecting the measure or dimension will be necessary to display it in the chart.


<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/image03.png" alt="Tableau Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

**Scenario 2: Handling inactive Lens in the environment** 

If the Lens is not active in the environment while working on an existing workbook in Tableau or when attempting to establish a new connection, an error will be encountered. This may prevent access to or querying data from the Lens. Verify that the Lens exists and is active before syncing.


**Scenario 3: Handling data source errors due to access restrictions**

If the Account table is set to `public = false`, a data source error will occur in Tableau. The error message will indicate that the 'Account table not found,' which will prevent querying or using data from that table.

<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/image06.png" alt="Tableau Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

To resolve this issue, ensure the Account table is accessible (set to `public = true` or assign appropriate permissions) and then resync the Lens in Tableau to regain access.


## Governance of model on Tableau Cloud

When the semantic model is activated via BI Sync in Tableau, data masking, restrictions, and permissions set by the publisher are automatically applied, ensuring consistent data security and compliance. The behavior of these policies (e.g., masking) may vary based on the Tableau user.

The Tableau management process involves authentication and authorization using the DataOS user ID and API key when accessing synced data models. This ensures that columns redacted by Lens data policies are restricted based on the user's group permissions.

For example, if a user named **iamgroot** in the **Analyst** group is restricted from viewing the 'Annual Salary' column, this column will not be visible in either the Data Product exploration page or Tableau after syncing. Tableau Cloud requires the DataOS user ID and API key for authentication, ensuring that users can access the full model, except for any columns restricted by any data policies. This approach maintains security and guarantees that users only see the data they are authorized to view.
