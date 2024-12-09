# Tableau Desktop Integration

## Steps

The following steps outline the process for integrating Tableau Desktop with DataOS:

### **Step 1: Navigate to the Data Product Hub**

Access the **Home Page** of DataOS. From the home page, navigate to the **Data Product Hub** to explore the various Data Products available within the platform.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/image%20(20).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

### **Step 2: Browse and Select a Data Product**

In the Data Product Hub, users can browse through a comprehensive list of available Data Products. To integrate with Tableau, click on a specific Data Product of interest. For instance `Sales360`


<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/image%20(21).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

### **Step 3: Access Integration Options**

After selecting Sales360 Data Product, navigate to the **Access Options** tab. Within this tab, various methods to access and interact with the Data Product can be found, including the **BI Sync** tab, where **Tableau Desktop** is located.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/Screenshot%20from%202024-09-21%2000-14-20.png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

### **Step 4: Download and Extract the `.tds` File**

Download the `.tds` file and extract the zip file into Tableau's default repository, typically located at `My Tableau Repository\Datasources\`.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/image%20(22).png" alt="DPH" style="width:25rem; border: 1px solid black;" />
</center>

### **Step 5: Proceed with Data Product**

Click on the Data Product to continue.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/image%20(23).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>

### **Step 6: Enter Credentials**

Users will be prompted to enter their username and API key.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/image%20(24).png" alt="DPH" style="width:25rem; border: 1px solid black;" />
</center>

### **Step 7: Visualize Data in Tableau Desktop**

Once the connection is established, users can begin visualizing the Data Product in Tableau Desktop.

<center>
<img src="/interfaces/data_product_hub/activation/bi_sync/image%20(25).png" alt="DPH" style="width:40rem; border: 1px solid black;" />
</center>


## Supported data types

| **Category**   | **Data Type**          | **Support Status**                       | **Recommended Approach**                       |
|----------------|------------------------|------------------------------------------|-----------------------------------------------|
| **Dimension**  | `time`                   | Supported                                | NA                                            |
| **Dimension**  | `string`                 | Supported                                | NA                                            |
| **Dimension**  | `number`                 | Supported                                | NA                                            |
| **Dimension**  | `boolean`                | Supported                                | NA                                            |
| **Measure**    | `max`                    | Supported                                | NA                                            |
| **Measure**    | `min`                    | Supported                                | NA                                            |
| **Measure**    | `number`                 | Supported                                | NA                                            |
| **Measure**    | `sum`                    | Supported                                | NA                                            |
| **Measure**    | `count`                  | Supported                                | NA                                            |
| **Measure**    | `boolean`                | Auto-converts to Dimension               | NA                                            |
| **Measure**    | `string`                 | Auto-converts to Dimension               | NA                                            |
| **Measure**    | `time`                   | Auto-converts to Dimension               | NA                                            |
| **Measure**    | `avg`                    | Not Supported                            | Option 1: To use measure of type ‘avg’, define an additional measure of type 'count' in that entity:<br>  <br>name: count<br>type: count<br>sql: '1'<br> <br> Option 2: Use measure of type 'number' and define average logic in SQL:<br>  <br>measures:<br>&nbsp;&nbsp;- name: total_accounts<br> &nbsp;&nbsp;&nbsp; type: number<br> &nbsp;&nbsp;&nbsp; sql: "avg({accounts})”<br> |
| **Measure**    | `count_distinct_approx`       | Not Supported         | NA                                            |
| **Rolling Window** | -                      | Supported                                | NA                                            |


## Important considerations for Tableau Integration

**1. Handling Entities without Relationships:** An error will occur during synchronization if any entity in the data model lacks a defined relationship. To resolve this issue, the entity can be hidden to avoid synchronization errors.

**2. Live connection:** The connection between the Lens semantic layer and Tableau Cloud is live. This means that any changes to the underlying data or measure logic will automatically be reflected in Tableau.

**3. Schema changes:** If there are schema updates, such as adding new dimensions or measures, the integration steps will need to be repeated to incorporate these changes into Tableau.

**4. Avoiding cyclic dependencies:** Tableau does not support cyclic dependencies within data models. To prevent integration issues, it is essential to ensure that the data model is free of cyclic dependencies prior to syncing with Tableau.

**5. Visualization with multiple data sources:** You cannot build a visualization that incorporates data from multiple data sources. For live connections, Tableau does not support data blending. Only a single data source can be used to create a visualization.
<!-- 
**6. Calculated Fields on Dimensions/Measures:** Any calculated field defined on top of a dimension or measure that is part of the semantic model is not supported. This means you cannot create custom calculations based on these predefined dimensions or measures within the semantic model. -->

**6. Centralized management:** All data sources should be managed and published by the admin on the server, with everyone else using this source.

**7. Single authority for Desktop publications:** If data sources are published via Tableau Desktop, ensure that all sources are published by a single authority to avoid multiple data source conflicts on the server.

**8. Row Limit:** The Lens API has a maximum return limit of 50,000 rows per request. To obtain additional data, it is necessary to set an offset. This row limit is in place to manage resources efficiently and ensure optimal performance.

**9. Selection:** It is important to select fields from tables that are directly related or logically joined, as the system does not automatically identify relationships between tables through transitive joins. Selecting fields from unrelated tables may result in incorrect or incomplete results.

<aside class="callout">
🗣️ Be aware that custom calculations or fields (measures/dimensions) created in BI tools may be lost during re-sync. It is preferable to create custom logic directly in Tableau's Lens.
</aside>

<!-- 
## Handling specific data types in Tableau

1. **Time data type as measure in Tableau**  

    When syncing the Lens semantic layer with Tableau, note that Tableau does not support the time data type as a measure. While Lens allows time-based measures, Tableau defaults to treating date and time fields as dimensions.As a result, Tableau will not correctly interpret any measure with a **time data type**.


    **Recommended actions**:

    To avoid synchronization issues:

    - Use time or date fields in Tableau only for **dimension-based** filtering or grouping.
    - For time-based calculations, limit aggregations to **MIN()** or **MAX()** functions.

2. **String data type to geographical**

    When connecting a dataset to Tableau, it automatically detects fields such as **City** and **Country** and converts them from string data types to **Geography** types. This enables Tableau to treat these fields as geographical locations, allowing features like map visualizations and geospatial analysis without the need for manual adjustments. -->

<!-- <aside class="callout">
🗣️ All limitations are specific to Tableau's handling of time data types as measures and does not affect other aspects of the Lens semantic layer's functionality.

</aside> -->


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

If the Account table is set to `public = false`, a data source error will occur in Tableau. The error message will indicate that the "Account table not found," which will prevent querying or using data from that table.

<div style="text-align: center;">
    <img src="/resources/lens/bi_integration/image06.png" alt="Superset Configuration" style="max-width: 80%; height: auto; border: 1px solid #000;">
</div>

To resolve this issue, ensure the Account table is accessible (set to public = true or assign appropriate permissions) and then resync the Lens in Tableau to regain access.

## Governance of Model on Tableau Desktop

When the Lens semantic model is activated via BI Sync on Tableau,data masking, restrictions, or permissions defined by the publisher will automatically be enforced for all viewers of the report from Lens are automatically applied to Tableau ensuring consistent data security and compliance. However, the behavior of data policies (e.g., masking) depends on who is the user of Tableau.

The Tableau management process involves authentication and authorization using the DataOS user ID and API key when accessing synced data models. This ensures that columns redacted by Lens data policies are restricted based on the user's group permissions.

For example, if a user named **iamgroot** in the **Analyst** group is restricted from viewing the 'Annual Salary' column, this column will not be visible in either the Data Product exploration page or Tableau after syncing. Tableau Cloud requires the DataOS user ID and API key for authentication, ensuring that users can access the full model, except for any columns restricted by any data policies. This approach maintains security and guarantees that users only see the data they are authorized to view.
