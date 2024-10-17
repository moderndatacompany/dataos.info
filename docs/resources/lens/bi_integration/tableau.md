# Tableau

## Prerequisites

- **Curl**: Ensure that `curl` is installed on the system. For Windows systems, `curl.exe` may be necessary.
- **Lens API endpoint**: The API endpoint provided by Lens for syncing data with meta endpoint access.
- **Access credentials**: Access credentials such as username, password, project name, etc., are required for Tableau.
- **DATA_OS API key**: Ensure the DATAOS API key is available. Get it by using the following command:

```bash
dataos-ctl user apikey get
```

## Steps

To sync the Lens model with Tableau, follow the steps below:

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

1. **URL:**

   - This endpoint is used to sync a specific Lens model to Tableau for public access.
   - Replace <DATAOS_FQDN> with your Fully Qualified Domain Name (FQDN) where your Lens instance is hosted. Example: - liberal-monkey.dataos.app.
   - Replace <WORKSPACE_NAME> with the name of the workspace your Lens model is deployed in. E.g. `public`, `curriculum`.
   - Replace <LENS_NAME> with the name of the Lens model you wish to sync. Example: `sales360`.

2. **Headers:**

    - **apikey:** User's API key for the current context in Lens.

        The DataOS API key for the user can be obtained by executing the command below.

        ```bash
        dataos-ctl user apikey get
        ```
    - **`Content-Type application/json`:** Specifies that the data being sent is in JSON format.
 
3. **Raw data payload:**

    This section defines the details of user's Tableau credentials and project configuration:

    - **project_name:** The name of the Tableau project where the data will be synced. Replace "sample" with user's actual project name. If the project already don't exist, tableau will create a new project with the given name.

    - **username:** Your Tableau account username.

    - **password:** Your Tableau account password.
    
    - **site_id:** The site ID that you are connected to in Tableau.

    - **server_address:** The URL of user's Tableau server. Replace it with the correct server address (e.g., https://prod-apnortheast-a.online.tableau.com). You can obtain these when you **log in** to Tableau. You’ll see the **URL** like below:

        > https://prod-apnortheast-a.online.tableau.com/#/site/iamgroot1086a891fef336/home

         here: **iamgroot1086a891fef336**  is the **site_id.**

**Step 2 Go to Tableau:** Access the Explore tab on the left side. The required tables and views will be visible in the project. In the screenshot below, there are three sources: one for tables and two for views.

<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/tableau1.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

**Step 3 Explore and create visualizations:** Navigate to the Home tab on the left side and click on 'New'. Under this option, select 'Workbook'.

<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/tableau2.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

**Step 4 Connect to data:** After clicking on 'Workbook', the 'Connect to Data' page will be displayed. Select either views or tables and click on 'Connect'.

<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/tableau3.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

Upon clicking 'Connect', a prompt will request the username and password. Enter the DataOS username and API key.


<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/tableau4.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

**Step 5 Start using the model:** After entering the credentials and clicking on 'Sign In', the model will be ready for visualization purposes.

<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/tableau5.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

## Important considerations for Tableau integration

**1. Handling entities without relationships:** An error will occur during synchronization if any entity in the data model lacks a defined relationship. To resolve this issue, the entity can be hidden to avoid synchronization errors.

**2. Live connection:** The connection between the Lens semantic layer and Tableau Cloud is live. This means that any changes to the underlying data or measure logic will automatically be reflected in Tableau.

**3. Schema changes:** If there are schema updates, such as adding new dimensions or measures, the integration steps will need to be repeated to incorporate these changes into Tableau.

**4. Avoiding cyclic dependencies:** Tableau does not support cyclic dependencies within data models. To prevent integration issues, it is essential to ensure that the data model is free of cyclic dependencies prior to syncing with Tableau.


## Handling Specific Data Types in Tableau

1. **Time data type as measure in Tableau**  

    When syncing the Lens semantic layer with Tableau, note that Tableau does not support the time data type as a measure. While Lens allows time-based measures, Tableau defaults to treating date and time fields as dimensions.As a result, Tableau will not correctly interpret any measure with a **time data type**.


    **Recommended actions**:

    To avoid synchronization issues:

    - Use time or date fields in Tableau only for **dimension-based** filtering or grouping.
    - For time-based calculations, limit aggregations to **MIN()** or **MAX()** functions.

2. **String data type to geographical**

    When connecting a dataset to Tableau, it automatically detects fields such as **City** and **Country** and converts them from string data types to **Geography** types. This enables Tableau to treat these fields as geographical locations, allowing features like map visualizations and geospatial analysis without the need for manual adjustments.

<aside class="callout">
📌 All limitations are specific to Tableau's handling of time data types as measures and does not affect other aspects of the Lens semantic layer's functionality.

</aside>

## Data policies and security

Any data masking, restrictions, or permissions defined by the publisher will automatically be enforced for all viewers of the report, ensuring consistent data security and compliance. However, the behavior of data policies (e.g., masking) depends on who is the user of the PowerBI desktop.

## Error handling 

**Scenario 1: Handling syntactical errors in measures or dimensions** 

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

If the Lens is not active in the environment while working on an existing workbook in Tableau or when attempting to establish a new connection, an error will be encountered. This may prevent access to or querying data from the Lens. Verification that the Lens exists and is active is required before syncing


**Scenario 4: Handling data source errors due to access restrictions**

If the Account table is set to public = false, a data source error will occur in Tableau. The error message will indicate that the "Account table not found," which will prevent querying or using data from that table.

<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/image06.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

To resolve this issue, ensure the Account table is accessible (set to public = true or assign appropriate permissions) and then resync the Lens in Tableau to regain access.
