# Tableau

<aside class="callout">
💡 For a streamlined and user-friendly integration with Tableau, use the Data Product Hub interface. This approach eliminates the need for manually working with `curl` commands, providing an easy way to connect to your Lens semantic model.

To get started with Tableau integration through Data Product Hub, refer to the link below:

<a href="/interfaces/data_product_hub/activation/bi_sync/tableau_cloud/">Access the Tableau integration guide</a>.
</aside>

<!-- ## Tableau desktop
## Tableau cloud  -->

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
    <img src="/resources/lens/bi_integration/tableau1.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

**Step 3: Explore and create visualizations** Navigate to the Home tab on the left side and click on 'New'. Under this option, select 'Workbook'.

<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/tableau2.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

**Step 4: Connect to data** After clicking on 'Workbook', the 'Connect to Data' page will be displayed. Select either views or tables and click on 'Connect'.

<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/tableau3.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

Upon clicking 'Connect', a prompt will request the username and password. Enter the DataOS username and API key.


<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/tableau4.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

**Step 5: Start using the semantic model** After entering the credentials and clicking on 'Sign In', the model will be ready for visualization purposes.

<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/tableau5.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>




## Important considerations for Tableau integration

**1. Handling entities without relationships:** An error will occur during synchronization if any entity in the semantic model lacks a defined relationship. To resolve this issue, the entity can be hidden to avoid synchronization errors.

**2. Live connection:** The connection between the semantic layer and Tableau Cloud is live. This means that any changes to the underlying data will automatically be reflected in Tableau.

**3. Schema changes:** If there are schema updates, such as adding new dimensions or measures, the integration steps will need to be repeated to incorporate these changes into Tableau.

**4. Avoiding cyclic dependencies:** Tableau does not support cyclic dependencies within semantic models. To prevent integration issues, it is essential to ensure that the semantic model is free of cyclic dependencies prior to syncing with Tableau.

## Data policies and security

Any data masking, restrictions, or permissions defined by the publisher will automatically be enforced for all viewers of the report, ensuring consistent data security and compliance. However, the behavior of data policies (e.g., masking) depends on who is the user of the PowerBI desktop.

## Error handling 

**Scenario 1: Handling syntactical errors in measures or dimensions** 

If a measure or dimension contains a syntactical error (and is also not functioning in Lens Studio), the following error will appear when attempting to select it:

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
