# Tableau Cloud

This topic covers how to integrate the semantic model of the Data Product with Tableau Cloud. By the end of this guide, you will be able to independently set up this integration and utilize the semantic model effectively.

## Scenario

Here, we will demonstrate how to seamlessly integrate the 'Product360' data product with Tableau Cloud, enabling you to build compelling dashboards that drive strategic business outcomes.

## Establishing the data connection

You initiate the process by configuring the connection between *Product-360* and your organization’s selected BI platform, Tableau Cloud. To successfully set up the integration, you need to enable BI-Sync.

### 1. **Navigate to Access Options**
    
Go to the **Access Options** tab for your Data product in Data Product Hub. Under the **BI Sync** section, locate the **Tableau Cloud** option.

![tableau_cloud_conn.png](/learn/dp_consumer_learn_track/integrate_bi_tools/tab_cloud/tableau_cloud_conn.png)

This action opens a setup window where you’ll enter the credentials required to connect your DataOS instance to Tableau Cloud.

### 2. **Enter Tableau Cloud Credentials**
    
In the subsequent setup window, input the required Tableau Cloud credentials:

![tableau_access_options_bisync.png](/learn/dp_consumer_learn_track/integrate_bi_tools/tab_cloud/tableau_access_options_bisync.png)

In the setup window, fill in the required credentials:

- **Project Name**: Specify the name of the project within Tableau (e.g., "Product 360 Analysis").
- **Server Name**: Provide the URL or address of the Tableau Server hosting your cloud instance.
- **Site ID**: Input the Site ID for your specific Tableau Cloud site.
- **Username**: Your Tableau account username.
- **Password**: Your Tableau account password.

![tableau_username_and_pw.png](/learn/dp_consumer_learn_track/integrate_bi_tools/tab_cloud/tableau_username_and_pw.png)

In addition to using standard Tableau credentials, you can also opt to use **Personal Access Tokens (PAT)** for authentication:

1. To create a PAT, log in to your Tableau Cloud account.
2. Click your avatar in the top-right corner.
3. Select **Personal Access Tokens** from the menu.
4. If available, click **Create a New Token**.
5. Name your token and click **Create**.
6. Copy the token and store it securely.
7. Enter the necessary Tableau details.
    - **Project Name:** The designated name for the project within Tableau. [E.g.  Projec
    - **Server Name:** The URL or address of the Tableau Server hosting the cloud instance.
    - **Site ID:** The identifier for the specific site on Tableau Cloud.
    - **Username**: Your Tableau PAT Name.
    - **Password**: Personal Access Token.

![tableau_pat.png](/learn/dp_consumer_learn_track/integrate_bi_tools/tab_cloud/tableau_pat.png)

After entering the credentials, click **Activate** to complete the setup. The *Product 360* data product will now be integrated into Tableau Cloud. If the project isn’t created already, a new project, **‘Product Analysis,’** will automatically be established.
    
### 3. **Consuming the Data Product on Tableau Cloud**
    
Once the *Product-360* Data Product has been successfully activated, you can proceed to create a dashboard in Tableau Cloud by following these steps:

1. **Login to Tableau Cloud**: Log into Tableau Cloud using the credentials; this action redirects you to the home page.

![tableau_ui.png](/learn/dp_consumer_learn_track/integrate_bi_tools/tab_cloud/tableau_ui.png)

2. **Accessing Manage Projects**: Select the **Manage Projects** option from the home page. This opens an interface displaying all existing projects within your Tableau environment, including the newly created **‘Product Analysis’** project.
    
    ![tableau_projects.png](/learn/dp_consumer_learn_track/integrate_bi_tools/tab_cloud/tableau_projects.png)
    
3. **Selecting the Project**: Locate and select the **‘Product Analysis** project. The project contains the newly synced semantic model (Lens) cross-sell-affinity and all it’s metrics.

![tableau_projectlens.png](/learn/dp_consumer_learn_track/integrate_bi_tools/tab_cloud/tableau_projectlens.png)

4. **Creating a New Workbook**: In the top-right corner of the data source interface, select the menu option and click on **New Workbook**.

![tableau_workbook.png](/learn/dp_consumer_learn_track/integrate_bi_tools/tab_cloud/tableau_workbook.png)

5. **Authenticate with DataOS:** This process prompts you to enter your **DataOS Username** and **API key** as the password. The API Key can be generated via clicking on the profile in the bottom left corner.

![tab_desk_api.png](/learn/dp_consumer_learn_track/integrate_bi_tools/tab_cloud/tab_desk_api.png)

6. **Creating the Dashboard**: After successful authentication, you are redirected to the new workbook interface, where you can begin visualizing and developing dashboards with insights derived from *Product 360*.

![tableau_dashboard.png](/learn/dp_consumer_learn_track/integrate_bi_tools/tab_cloud/tableau_dashboard.png)

## Important Considerations for Tableau Integration

When integrating your *Product 360* data model with Tableau Cloud, consider the following tips to ensure smooth functionality and avoid potential issues:

- **Handling Entities without Relationships**:  If you encounter entities with no defined relationships in your data model, they may cause errors during synchronization. To prevent this, consider hiding these entities before syncing with Tableau.
- **Live Connection**: You benefit from a live connection between the Lens semantic layer and Tableau Cloud; any changes made to the underlying data or measure logic will automatically be updated in Tableau, ensuring you always have access to the latest insights.
- **Schema Changes**: If you make schema updates, such as adding new dimensions or measures, remember that you will need to repeat the integration steps to incorporate these changes into Tableau.
- **Avoiding Cyclic Dependencies**: Before syncing with Tableau, ensure your data model is free of cyclic dependencies, as Tableau does not support them. This will help prevent integration issues.

### Handling Specific Data Types in Tableau

When working with the Lens semantic model in Tableau, understanding how Tableau handles specific data types will ensure accurate analysis and visualization:

- **Time Data Type as Measure**: Tableau does not treat time as a measure; instead, it recognizes date and time fields as dimensions. To avoid issues, use date and time fields for filtering or grouping and limit calculations to `MIN()` or `MAX()` functions.
- **String Data Type to Geographical**: When syncing data that contains location information (e.g., City or Country), Tableau automatically converts string fields to Geography types. This enables map visualizations and spatial analysis without needing additional manual adjustments.

<aside class="callout">
🗣 These limitations specifically pertain to how Tableau handles time data types as measures and do not impact other functionalities of the Lens semantic layer.

</aside>