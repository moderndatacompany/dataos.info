## Steps for Integrating Data Products with Tableau Cloud

This document outlines the steps required to integrate Data Products from DataOS with Tableau Cloud.

### **Step 1: Navigate to the Data Product Hub**

Access the **Home Page** of DataOS. From the home page, navigate to the **Data Product Hub** to explore the various Data Products available.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/image%20(6).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

### **Step 2: Browse and select a Data Product**

Browse through the list of available Data Products. Select a specific Data Product to integrate with Tableau. For instance, **Product 360** can be chosen to explore the Data Product on Tableau for data visualisation and getting  insights.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/Tableau/Tableau0.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

### **Step 3: Navigate to the Access Options**

After selecting a Data Product, navigate to the **BI Sync** option in the **Access Options** tab. Scroll through the BI Sync and locate the **Tableau Cloud** option. Now, Click on the **Add Connection** button

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/Tableau/Tableau1.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

### **Step 4: Enter connection details and click Activate button**

A connection window will open, prompting the entry of the necessary connection details. There are following two ways to pass the connection details:

1. [Connection details for connecting using Tableau username and password](#connection-details-for-connecting-via-tableau-username-and-password)
2. [Connection details for connecting using Tableau PAT](#connection-details-for-connecting-using-tableau-pat)


#### Connection details for connecting using Tableau username and password

- **Project Name**: Enter the Tableau project name. If a project with that name does not already exist, it will be created automatically. If you do not specify a name, the project will default to the name of the Data Product, which will register all associated data sources under that project.

For optimal organization within Tableau, we recommend providing a custom project name it facilitates easier navigation of your data sources.

- **Server Name**: The address of the Tableau server (e.g., `https://prod-apnortheast-a.online.tableau.com`).
- **Site ID**: The site ID (e.g., `tableausuer@123`).
- **Username**: The Tableau username.(e.g., `labs@tmdc.io`)
- **Password**: The password associated with the Tableau account.

These details can be obtained upon logging into Tableau. The URL format will appear as follows:

[https://prod-apnortheast-a.online.tableau.com/#/site/site_id](https://prod-apnortheast-a.online.tableau.com/#/site/tableauuser@123)

**Sample URL**: 

[https://prod-apnortheast-a.online.tableau.com/#/site/tableauuser@123/home](https://prod-apnortheast-a.online.tableau.com/#/site/tableauuser@123/home)

In this example, `tableuuser@123` represents the **site_id**.

After entering the required credentials, click the **Activate** button to establish the connection. A confirmation message will appear upon successful connection.  

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/Tableau/Tableau3.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

#### Connection details for connecting using Tableau PAT

In addition to using standard Tableau credentials, users can also opt to use Personal Access Tokens (PAT) for authentication. To create a PAT in the Tableau follow the instructions given on [this link](https://help.tableau.com/current/online/en-us/security_personal_access_tokens.htm).

After successfully creating the PAT, follow the same steps as of connection details for the Tableau username and password and enter the connection details:

- **Project Name:** The designated name for the project within Tableau. (E.g.  Product Analysis)
- **Server Name:** The URL or address of the Tableau Server hosting the cloud instance.
- **Site ID:** The identifier for the specific site on Tableau Cloud.
- **Username**: Tableau PAT Name. (e.g., `iamgroot`, `test_token`)
- **Password**: Personal Access Token.

After filling all details, click on the Acitvate button. A confirmation message will appear upon successful connection.  

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/Tableau/Tableau4.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

## Exploring the Data Product on Tableau Cloud

### **Step 1: Log in to Tableau Cloud**

Users should log in to Tableau Cloud using the same credentials of Tableau. This will redirect to the Tableau Cloud home page.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/Tableau/Tableau5.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

### **Step 2: Manage Projects**

Click on the **Manage Projects** option on the home page.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/image%20(13).png" alt="DPH" style="width:25rem; border: 1px solid black;" />
</center>

### **Step 3: Access the Project interface**

This will open an interface displaying all projects, including the newly created project titled **Product Analysis**.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/Tableau/Tableau5.1.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

### **Step 4: Select the Project**

Click on the  project to view the available data sources for dashboard creation. This project will contains semantic model and all it's views (entities and metrics).

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/Tableau/Tableau5.2.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

### **Step 5: Create a new workbook**

Click on the menu option in the upper right corner of the data source and select the **New Workbook** option.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/Tableau/Tableau6.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

### **Step 6: Provide credentials**

To create a new workbook where dashboard creation can commence, users will be prompted to provide their DataOS username and API key as the password to access the data source. The API can be retrieved by navigating to the profile page in the bottom left corner of the Data Product Hub.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/Tableau/Tabelau7.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

### **Step 7: Start creating the dashboard**

Now, users can create dashboard and extract relevant insights

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/Tableau/tableau8.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
<figcaption><i>Happy dashboarding!</i></figcaption>
</center>


## Important Considerations for Tableau Integration

**1. Handling Entities without Relationships:** An error will occur during synchronization if any entity in the data model lacks a defined relationship. To resolve this issue, the entity can be hidden to avoid synchronization errors.

**2. Live connection:** The connection between the Lens semantic layer and Tableau Cloud is live meaning that any changes to the underlying data or measure logic will automatically be reflected in Tableau.

**3. Schema changes:** If there are schema updates, such as adding new dimensions or measures, the integration steps will need to be repeated to incorporate these changes into Tableau.

**4. Avoiding cyclic dependencies:** Tableau does not support cyclic dependencies within data models. To prevent integration issues, it is essential to ensure that the data model is free of cyclic dependencies prior to syncing with Tableau.


## Handling specific data types in Tableau

1. **Time data type as measure in Tableau**  

    When syncing the Lens semantic layer with Tableau, note that Tableau does not support the time data type as a measure. While Lens allows time-based measures, Tableau defaults to treating date and time fields as dimensions.As a result, Tableau will not correctly interpret any measure with a **time data type**.


    **Recommended actions**:

    To avoid synchronization issues:

    - Use time or date fields in Tableau only for **dimension-based** filtering or grouping.
    - For time-based calculations, limit aggregations to **MIN()** or **MAX()** functions.

2. **String data type to geographical**

    When connecting a dataset to Tableau, it automatically detects fields such as **City** and **Country** and converts it from string to **Geography** types. This enables Tableau to treat these fields as geographical locations, allowing features like map visualizations and geospatial analysis without the need for manual adjustments.

<aside class="callout">
📌 All limitations are specific to Tableau's handling of time data types as measures and does not affect other aspects of the Lens semantic layer functionality.

</aside>

## Error handling 

**Scenario 1: Handling syntactical errors in Measures or Dimensions** 

If a measure or dimension contains a syntactical error (and is also not functioning in Lens Studio), the following error will appear when attempting to select such a measure or dimension:

<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/image02.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

After correcting the syntactical error in the measure or dimension within Lens, the error will no longer appear. To reflect the changes in Tableau, refreshing the data source and re-selecting the measure or dimension will be necessary to display it in the chart.


<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/image03.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>


**Scenario 2: Reflecting logical changes in measures or dimensions**

If logical changes are made to a measure or dimension, for example adjusting how the sum is calculated, the changes will not be reflected in Tableau immediately.

<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/image04.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

Before the change, the sum calculation may appear as shown below:

<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/image05.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>


**Scenario 3: Handling inactive Lens in the environment** 

If the Lens is not active in the environment while working on an existing workbook in Tableau or when attempting to establish a new connection, an error will be encountered. This may prevent access to or querying data from the Lens. Hence, verification that the Lens exists and is active is required before syncing.


**Scenario 4: Handling data source errors due to access restrictions**

If the `Account` table is set to public = false, a data source error will occur in Tableau. The error message will indicate that the "Account table not found," which will prevent querying or using data from that table.

<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/image06.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

To resolve this issue, ensure the `Account` table is accessible (set to public = true or assign appropriate permissions) and then resync the Lens in Tableau to regain access.

---

## Governance of model on Tableau Cloud

When the Lens Model is activated via BI Sync on Tableau,data masking, restrictions, or permissions defined by the publisher will automatically be enforced for all viewers of the report from Lens are automatically applied to Tableau ensuring consistent data security and compliance. However, the behavior of data policies (e.g., masking) depends on who is the user of Tableau.

The Tableau management process involves authentication and authorization using the DataOS user ID and API key when accessing synced data models. This ensures that columns redacted by Lens data policies are restricted based on the user's group permissions.

For example, if a user named **iamgroot** in the "**Analyst**" group is restricted from viewing the "Annual Salary" column, this column will not be visible in either the Data Product exploration page or Tableau after syncing. Tableau Cloud requires the DataOS user ID and API key for authentication, ensuring that users can access the full model, except for any columns restricted by any data policies. This approach maintains security and guarantees that users only see the data they are authorized to view.
