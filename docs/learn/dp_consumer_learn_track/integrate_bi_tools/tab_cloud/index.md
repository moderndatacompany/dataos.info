# Tableau Cloud

This topic covers how to integrate the semantic model of the Data Product 'Product Affinity' with Tableau Cloud. By the end of this guide, you will be able to independently set up this integration and utilize the semantic model effectively.

## Establishing the data connection

You initiate the process by configuring the connection between 'Product Affinity' and your organization’s selected BI platform, Tableau Cloud. To successfully set up the integration, you need to enable BI-Sync.

### **1. Navigate to Access Options**
    
Go to the 'Access Options' tab for your Data product in Data Product Hub. Under the 'BI Sync' section, locate the 'Tableau Cloud' option.

![tableau_cloud_conn.png](/learn/dp_consumer_learn_track/integrate_bi_tools/tab_cloud/tableau_cloud_conn.png)

This action opens a setup window where you’ll enter the credentials required to connect your DataOS instance to Tableau Cloud.

### **2. Enter Tableau Cloud credentials**
    
In the subsequent setup window, input the required Tableau Cloud credentials:

![tableau_access_options_bisync.png](/learn/dp_consumer_learn_track/integrate_bi_tools/tab_cloud/tableau_access_options_bisync.png)

In the setup window, fill in the required credentials:

- **Project name**: Specify the name of the project within Tableau (e.g., 'Product Affinity Analysis').
- **Server name**: Provide the URL or address of the Tableau Server hosting your cloud instance e.g, (https://prod-apnortheast-a.online.tableau.com).
- **Site id**: Input the Site ID for your specific Tableau Cloud site. You can obtain it when you log in to Tableau (e.g., `https://prod-apnortheast-a.online.tableau.com/#/site/moderndata/` where `moderndata` is the site id).  
- **Username**: Your Tableau account username (e.g., labs@modern.io).
- **Password**: Your Tableau account password. 

![tableau_username_and_pw.png](/learn/dp_consumer_learn_track/integrate_bi_tools/tab_cloud/tableau_username_and_pw.png)

<aside class="callout">
🗣️ For environments requiring Multi-Factor Authentication (MFA), use Personal Access Tokens instead of traditional username and password credentials.
</aside>


In addition to using standard Tableau credentials, you can also opt to use 'Personal Access Tokens (PAT)' for authentication, to create a PAT follow the below steps:

- Log in to your Tableau Cloud account.
- Click your avatar in the top-right corner.
- Select 'Personal Access Tokens' from the menu.
- If available, click 'Create a New Token'.
- Name your token and click 'Create'.
- Copy the token and store it securely.

Enter the following necessary Tableau details:

- **Project name:** The designated name for the project within Tableau. (e.g.  Product-analysis).
- **Server name:** The URL or address of the Tableau Server hosting the cloud instance  (e.g, https://prod-apnortheast-a.online.tableau.com). 
- **Site id:** The identifier for the specific site on Tableau Cloud.  You can obtain it when you log in to Tableau (e.g., `https://prod-apnortheast-a.online.tableau.com/#/site/moderndata/`), where `moderndata` is the site id. 
- **PAT name**: Your Tableau PAT name.
- **PAT**: Personal Access Token.

![tableau_pat.png](/learn/dp_consumer_learn_track/integrate_bi_tools/tab_cloud/tableau_pat.png)

After entering the credentials, click 'Activate' to complete the setup. The *Product Affinity* data product will now be integrated into Tableau Cloud. If the project isn’t created already, a new project, ‘Product Analysis,’ will automatically be established.
    
### **3. Consuming the Data Product on Tableau Cloud**
    
Once the 'Product Affinity' Data Product has been successfully activated, you can proceed to create a dashboard in Tableau Cloud by following these steps:

1. **Login to Tableau Cloud**: Log into Tableau Cloud using the credentials; this action redirects you to the home page.

    ![tableau_ui.png](/learn/dp_consumer_learn_track/integrate_bi_tools/tab_cloud/tableau_ui.png)

2. **Accessing Manage Projects**: Select the Manage Projects option from the home page. This opens an interface displaying all existing projects within your Tableau environment, including the newly created ‘Product Analysis’ project.
    
    ![tableau_projects.png](/learn/dp_consumer_learn_track/integrate_bi_tools/tab_cloud/tableau_projects.png)
    
3. **Selecting the Project**: Locate and select the Product Analysis project. The project contains the newly synced semantic model (Lens) cross-sell-affinity and all it’s metrics.

    ![tableau_projectlens.png](/learn/dp_consumer_learn_track/integrate_bi_tools/tab_cloud/tableau_projectlens.png)

4. **Creating a new workbook**: In the top-right corner of the data source interface, select the menu option and click on New Workbook.

    ![tableau_workbook.png](/learn/dp_consumer_learn_track/integrate_bi_tools/tab_cloud/tableau_workbook.png)

5. **Authenticate with DataOS:** This process prompts you to enter your DataOS Username and API key as the password. The API Key can be generated via clicking on the profile in the bottom left corner.

    ![tab_desk_api.png](/learn/dp_consumer_learn_track/integrate_bi_tools/tab_cloud/tab_desk_api.png)

6. **Creating the dashboard**: After successful authentication, you are redirected to the new workbook interface, where you can begin visualizing and developing dashboards with insights derived from *Product Affinity*.

    ![tableau_dashboard.png](/learn/dp_consumer_learn_track/integrate_bi_tools/tab_cloud/tableau_dashboard.png)

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

If a measure or dimension contains a syntactical error (and is also not functioning in Explore studio of DPH), the following error will appear when attempting to select it:

<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/image02.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

After correcting the syntactical error in the measure or dimension within Lens, the error will no longer appear. To reflect the changes in Tableau, refreshing the data source and re-selecting the measure or dimension will be necessary to display it in the chart.


<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/image03.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

**Scenario 2: Handling inactive Lens in the environment** 

If the Lens is not active in the environment while working on an existing workbook in Tableau or when attempting to establish a new connection, an error will be encountered. This may prevent access to or querying data from the Lens. Verify that the Lens exists and is active before syncing.


**Scenario 3: Handling data source errors due to access restrictions**

If the Account table is set to `public = false`, a data source error will occur in Tableau. The error message will indicate that the 'Account table not found,' which will prevent querying or using data from that table.

<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/image06.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

To resolve this issue, ensure the Account table is accessible (set to `public = true` or assign appropriate permissions) and then resync the Lens in Tableau to regain access.


## Governance of model on Tableau Cloud

When the semantic model is activated via BI Sync in Tableau, data masking, restrictions, and permissions set by the publisher are automatically applied, ensuring consistent data security and compliance. The behavior of these policies (e.g., masking) may vary based on the Tableau user.

The Tableau management process involves authentication and authorization using the DataOS user ID and API key when accessing synced data models. This ensures that columns redacted by Lens data policies are restricted based on the user's group permissions.

For example, if a user named **iamgroot** in the **Analyst** group is restricted from viewing the 'Annual Salary' column, this column will not be visible in either the Data Product exploration page or Tableau after syncing. Tableau Cloud requires the DataOS user ID and API key for authentication, ensuring that users can access the full model, except for any columns restricted by any data policies. This approach maintains security and guarantees that users only see the data they are authorized to view.
