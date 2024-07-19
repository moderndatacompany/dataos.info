# Getting Started with Audiences

## Pre-Requisites

### **Name your Lens `c360`**

A Lens with the designated name `c360` must be established. It should be noted that any other name chosen for the Lens will not be reflected within the Audiences App. The Audiences App provides a comprehensive view of audience information using the default Lens Query, and the name `c360` is a critical component in this regard.

### **`customer` entity with a `customer_id` field**

In the Audiences App, the `customer` entity of the `c360` Lens must consistently feature a `customer_id` column, encompassing dimensions such as `email`, `phone_number`, and `address`. The absence of the `customer` entity with the `customer_id` will result in the failure of the backend Audiences workflow.

<aside class="best-practice"> 📖 <b>Best Practice:</b> Assigning a string data type to the `customer_id` field is recommended to improve query performance. However, even if a different data type is specified, the query-building process has been designed to handle it seamlessly.</aside>

Let’s get right into building audiences within the Audiences App.

## Building Audiences

### **Step 1: Create a Lens**

Ensure that the Lens manifest file is created with the prerequisites satisfied. If you want to learn more about the process of creating a Lens, refer to [Building Lens](/interfaces/lens/building_lens/) documentation for detailed instructions.

For the demonstration purpose, a `c360` Lens sample has been created. The Lens manifest file outlines the entities, fields, measures, and relationships, providing a structured data model for the Audiences app.

???tip "Example manifest for the 'c360' Lens"

    ```yaml
    --8<-- "examples/interfaces/audiences/c360.yml"
    ```
### **Step 2: Deploy the Lens using Postman**

With the manifest file for the Lens being created, the next step is to deploy it. Postman will be used as the deployment tool. Ensure that you have installed Postman and followed all necessary steps to deploy the Lens.

### **Step 3: Access the Audiences App**

Once the Lens is deployed in the DataOS environment, go to the Audiences application on the DataOS Homepage and navigate to the Builder section. When you deploy a Lens named "c360" that meets all the prerequisites, it instantly appears in the Audiences Builder. From there, you can explore the entities in the c360 model, review the different fields and measures associated with them, and visually examine the relationships between them. The below image depicts the various steps to be executed while building audiences:
 
<center>
  <div style="text-align: center;">
    <img src="/interfaces/audiences/getting_started/audiences_builder.svg" alt="Audiences Builder" style="width: 60rem; border: 1px solid black;">
    <figcaption>Audiences Builder</figcaption>
  </div>
</center>


The following is a comprehensive procedure that outlines the steps depicted in the aforementioned diagram:

#### **3.1: Provide Name and Description for the Audiences**

As a primary step, it is essential to supply the name and description to the audience. The provision of the name is a mandatory requirement, while the description is optional.

<aside class="best-practice"> 📖 <b>Best Practice:</b> Providing an appropriate description for the audience is part of the best practices so that people within the organization can easily find out what the saved audience (or cohort) represent.</aside>

#### **3.2: Select a Cluster**

In this step, select a Cluster if it has not been pre-selected. If the desired cluster has already been pre-selected, proceed to the next step.

Upon selecting a Cluster, you will be presented with a summary of all available data. The bar graph in the block displays the percentage of the selected cohort's audience, taking into consideration that no filter conditions or parameters have been applied at this time.
 
<center>
  <div style="text-align: center;">
    <img src="/interfaces/audiences/getting_started/summary_statistics.png" alt="Summary statistics" style="width: 60rem; border: 1px solid black;">
    <figcaption>Summary statistics</figcaption>
  </div>
</center>


The summary statistics reveal that out of the total data set, only 61.97% of individuals have email information available, 98.45% have phone numbers on record, and 99.74% have address information. These statistics are essential in determining the appropriate marketing channel to use.

#### **3.3: Set Filter Conditions**

The filter capabilities provide you with the ability to segment your target audience based on specific criteria and traits. For example, by implementing a filter on the metric of total activities, to evaluate the number of target audience members who have completed more than 5 activities, simply navigate to the "Activity Stream" section within Filters and select the "+ Add rule" button. Configure the operator to ">=" and set the value to "5," as illustrated below.
 
<center>
  <div style="text-align: center;">
    <img src="/interfaces/audiences/getting_started/filter_conditions.png" alt="Filter conditions" style="width: 60rem; border: 1px solid black;">
    <figcaption>Filter conditions</figcaption>
  </div>
</center>

To access the values and frequency information for a specific column, click on the <code>i</code> icon located adjacent to the column name. This will bring up a pop-up window displaying the detailed information for that column.

<center>
  <div style="text-align: center;">
    <img src="/interfaces/audiences/getting_started/detailed_column_information.png" alt="Detailed Column Information" style="width: 60rem; border: 1px solid black;">
    <figcaption>Detailed column information</figcaption>
  </div>
</center>


#### **3.4: Update**

Upon clicking the "Update" button, the Summary Statistics for the selected cohort of individuals who meet the filter criteria will be displayed. The Percentage Bar within the Summary Statistics shows the proportion of individuals who satisfy the criteria. The text panes below indicate the percentage of the audience that possess email addresses, phone numbers, and physical addresses. Once you have confirmed that this is the desired audience, you may proceed to save them.

#### **3.5: Save the Targeted Audience**

The audience whose activity meets or exceeds the threshold of 5 has now been acquired. The summary reveals that 85.3% of the 100% of the audience satisfies the criteria. Within this group, 60.24% have email addresses, 98.63% have phone numbers, and 100% have physical addresses.
 
<center>
  <div style="text-align: center;">
    <img src="/interfaces/audiences/getting_started/summary.png" alt="Summary" style="width: 60rem; border: 1px solid black;">
    <figcaption>Summary</figcaption>
  </div>
</center>


Once you save the Audiences, they are saved in the [Audiences](/interfaces/audiences/audiences_ui/) by the name you provided earlier, and you can still make changes to them, but you cannot schedule them or query them using Workbench until you Publish them. 

#### **3.6: Publish the Audiences**

You can click the eye-like icon near the Save button to Publish the Audiences. Only when the audiences are Published, you can schedule them. You can Clone the Published Audiences to create new ones using the Clone button.

#### **3.7: Schedule the Audiences**

Schedule the Audiences using the feature available in the Audiences App. You can choose the cadence interval, whether it's every minute, hour, day, etc. 

<aside class="callout"> 🗣️ The Audience workflow will only commence another iteration once the previous one has been successfully concluded. If an error occurs prior to the next scheduled iteration, the workflow will initiate at the designated cron time.</aside>
 
<center>
  <div style="text-align: center;">
    <img src="/interfaces/audiences/getting_started/scheduling_options.png" alt="Scheduling Options" style="width: 60rem; border: 1px solid black;">
    <figcaption>Scheduling options</figcaption>
  </div>
</center>


#### **3.8: Save the Audiences. Again!!!**

As soon as you save the audiences again after scheduling, a workflow will be triggered to write the audience data to the DataOS internal storage, Icebase. 

## Leveraging the Generated Audience Insights

Once the Audience data has been saved to the Icebase, it can be accessed using the Workbench for marketing campaigns targeting these specific audiences. To access the data, select the `icebase` depot and the `audience_segment` catalog in the Workbench, where you have two datasets available, `segment_stream` and `max_occurence_state`. Both these datasets can be queried to provide answers to various questions. An example query is provided below:

```sql
SELECT * FROM "icebase"."audience_segment".segment_stream LIMIT 10;
```