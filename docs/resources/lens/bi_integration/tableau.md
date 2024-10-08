
# Tableau

## Prerequisites

- **Curl**: Ensure you have `curl` installed on your system. For Windows users, you may need to use `curl.exe`. 
- **Lens API Endpoint**: The API endpoint provided by Lens to sync the data with meta endpoint access.
- **Access Credentials**: For Tableau you will need access credentials such as username, password, project name, etc..
- **DATA_OS API KEY:** : Ensure you have your DATAOS APIKEY.

## Steps

To sync your Lens model with Tableau, follow the below  steps:

**Step 1: Run the curl command**

```bash
curl --location --request POST 'http://DATAOS_FQDN/lens2/sync/api/v1/tableau/<WORKSPACE_NAME>:<LENS_NAME>' \
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
1. **URL:**

   - This endpoint is used to sync a specific Lens model to Tableau for public access.
   - Replace <DATAOS_FQDN> with your Fully Qualified Domain Name (FQDN) where your Lens instance is hosted. Example: - liberal-monkey.dataos.app.
   - Replace <WORKSPACE_NAME> with the name of the workspace your Lens model is deployed in. E.g. `public`, `curriculum`.
   - Replace <LENS_NAME> with the name of the Lens model you wish to sync. Example: `sales360`.

2. **Headers:**

    - **apikey:** Your API key for the current context in Lens.

        The DataOS API key for the user can be obtained by executing the command below.

        ```bash
        dataos-ctl user apikey get
        ```
    - **`Content-Type application/json`:** Specifies that the data being sent is in JSON format.
 
3. **Raw Data Payload:**

    This section defines the details of your Tableau credentials and project configuration:

    - **project_name:** The name of the Tableau project where the data will be synced. Replace "sample" with your actual project name. If the project already don't exist, tableau will create a new project with the given name.

    - **username:** Your Tableau account username.

    - **password:** Your Tableau account password.
    
    - **site_id:** The site ID that you are connected to in Tableau.

    - **server_address:** The URL of your Tableau server. Replace it with the correct server address (e.g., https://prod-apnortheast-a.online.tableau.com). You can obtain these when you **log in** to Tableau. You’ll see the **URL** like below:

        > https://prod-apnortheast-a.online.tableau.com/#/site/iamgroot1086a891fef336/home

         here: **iamgroot1086a891fef336**  is your **site_id.**

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

## Important Considerations for Tableau Integration

1. **Building Connections Twice**: For views and tables, you need to establish the connection twice to ensure proper integration with Tableau.

2. **Handling Entities Without Relationships**: If any entity in the data model lacks a defined relationship, an error will occur during synchronization. To resolve this, you can hide the entity to avoid errors.

3. **Live Connection**: The connection between the Lens semantic layer and Tableau Cloud is live, meaning any changes to the underlying data or measure logic will automatically reflect in Tableau.

4. **Schema Changes**: If there are any schema updates, such as the addition of new dimensions or measures, you will need to repeat the integration steps to incorporate these changes into Tableau.

5. **Avoiding Cyclic Dependencies**: Tableau does not support cyclic dependencies within data models. Before syncing with Tableau, ensure that your data model is free of any cyclic dependencies to avoid integration issues.


## Handling Specific Data Types in Tableau

1. **Time Data Type as Measure in Tableau**  

    When syncing the Lens semantic layer with Tableau, note that Tableau does not support the time data type as a measure. While Lens allows time-based measures, Tableau defaults to treating date and time fields as dimensions.As a result, Tableau will not correctly interpret any measure with a **time data type**.


    **Recommended Actions**:

    To avoid synchronization issues:

    - Use time or date fields in Tableau only for **dimension-based** filtering or grouping.
    - For time-based calculations, limit aggregations to **MIN()** or **MAX()** functions.

2. **String Data Type to Geographical**

    When connecting a dataset to Tableau, it automatically detects fields such as **City** and **Country** and converts them from string data types to **Geography** types. This enables Tableau to treat these fields as geographical locations, allowing features like map visualizations and geospatial analysis without the need for manual adjustments.

<aside class="callout">
📌 All limitations are specific to Tableau's handling of time data types as measures and does not affect other aspects of the Lens semantic layer's functionality.

</aside>



## Data Policies and Security

Any data masking, restrictions, or permissions defined by the publisher will automatically be enforced for all viewers of the report, ensuring consistent data security and compliance. However, the behavior of data policies (e.g., masking) depends on who is the user of the PowerBI desktop.

## Error Handling 

**Scenario 1: Handling Syntactical Errors in Measures or Dimensions** 

If a measure or dimension contains a syntactical error (and is also not working in Lens Studio), the following error will appear when you try to select such a measure or dimension:

<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/image02.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

After correcting the syntactical error in the measure or dimension within Lens, the error will no longer appear. To reflect the changes in Tableau, you must refresh the data source and re-select the measure or dimension to display it in the chart.

<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/image03.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>


**Scenario 2: Reflecting Logical Changes in Measures or Dimensions**

If logical changes are made to a measure or dimension, for example adjusting how the sum is calculated, the changes will not be reflected in Tableau immediately.

<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/image04.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

Before the change, the sum calculation may appear as shown below:

<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/image05.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>


**Scenario 3: Handling Inactive Lens in the Environment** 

If the Lens is not active in the environment while working on an existing workbook in Tableau or when trying to establish a new connection, you will encounter an error. This could prevent you from accessing or querying data from the Lens. Make sure the lens exists and is active before syncing.

**Scenario 4: Handling Data Source Errors Due to Access Restrictions**

If the Account table is made public = false, you will encounter a data source error in Tableau. The error message will indicate that the "Account table not found," preventing you from querying or using data from that table.

<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/image06.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

To resolve this issue, ensure the Account table is accessible (set to public = true or with appropriate permissions) and then resync the Lens in Tableau to regain access.