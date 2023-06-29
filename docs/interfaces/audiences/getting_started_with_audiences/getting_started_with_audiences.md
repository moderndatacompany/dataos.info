# Getting Started with Audiences

## Pre-Requisites

### Name of the Lens should be `c360`

A Lens with the designated name `c360` must be established. It should be noted that any other name chosen for the Lens will not be reflected within the Audience App. The Audience App provides a comprehensive view of audience information using the default Lens Query, and the name `c360` is a critical component in this regard.

### `customer` entity with a `customer_id` field

In the Audience App, the `customer` entity of the `c360` Lens must consistently feature a `customer_id` column, encompassing dimensions such as `email`, `phone_number`, and `address`. The absence of the `customer` entity with the `customer_id` will result in the failure of the workflow.

So without any further ado, let’s get right into building audiences within the Audience App.

> 📖 Best Practice: Assigning a string data type to the `customer_id` field is recommended to improve query performance. Even if a different data type is provided, we have handled it in the query-building process, so there's no need to worry.

## Building Audiences

### Step 1: Create a Lens

Ensure that the Lens YAML is created with the prerequisites satisfied. For demonstration purpose, As a demonstration, a `c360` lens sample has been provided below:

```yaml
name: c360
description: Data Model to answer any questions around a customer. It follows Activity Schema specifications.
contract: c360
owner: iamgroot
tags:
  - c360
entities:
  - name: customer
    sql:
      query: >
        SELECT * FROM icebase.audience.customers_large_data_02
      columns:
        - name: customer_id
        - name: customer_name
        - name: email
        - name: phone_number
        - name: address
      verified: true
      tables:
        - icebase.audience.customers_large_data
    fields:
      - name: customer_id
        type: string
        description: unique identifier of the customer
        primary: true
        sql_snippet: customer_id
      - name: customer_name
        type: string
        description: Business name the customer operates under
        sql_snippet: customer_name
      - name: email
        type: string
        description: email address of the customer
        sql_snippet: email
      - name: phone_number
        type: string
        description: contact number of the customer
        sql_snippet: phone_number
      - name: address
        type: string
        description: postal address of the customer
        sql_snippet: address
    dimensions:
      - name: customer_no
        type: string
        description: customer identifier only unique within the site
        sql_snippet: customer_no
      - name: site
        type: string
        description: site number
        sql_snippet: site
      - name: state
        type: string
        description: state code where the customer physical address is located
        sql_snippet: state
      - name: county_name
        type: string
        description: name of the county
        sql_snippet: county_name
      - name: zip
        type: string
        description: ZIP code associate with the customer physical address
        sql_snippet: zip
      - name: premise_code
        type: string
        description: premise code - on prem, off prem
        sql_snippet: premise_code
      - name: status
        type: string
        description: customer status - active, inactive, suspended
        sql_snippet: status
      - name: license_classification
        type: string
        description: used to identify customer tier
        sql_snippet: license_classification
      - name: license_type
        type: string
        description: type of license
        sql_snippet: license_type
      - name: channel_code
        type: string
        description: indicates whether chain is a grocery, hotel etc
        sql_snippet: channel_code
      - name: channel_name
        type: string
        description: channel description
        sql_snippet: channel_name
      - name: selling_division_name
        type: string
        description: internal division responsible for the order
        sql_snippet: selling_division_name
    measures:
      - name: total_customers
        sql_snippet: ${customer.customer_id}
        type: count
        description: count of total customers
    relationships:
      - type: 1:N
        field: customer_id
        target:
          name: activity_stream
          field: entity_id
        verified: true
  - name: activity_stream
    sql:
      query: >
        select * from icebase.audience.activity_streams_large_data_02
      columns:
        - name: activity_uuid
        - name: entity_id
      verified: true
      tables:
        - icebase.audience.activity_streams_large_data
    fields:
      - name: activity_uuid
        type: string
        description: unique identifier of the activity event
        primary: true
        sql_snippet: activity_uuid
      - name: entity_id
        type: string
        description: customer identifier
        sql_snippet: entity_id
    dimensions:
      - name: activity_ts
        type: date
        description: timestamp of the moment when activity_occured
        sql_snippet: activity_ts
      - name: activity
        type: string
        description: name of the activity associated with the customer
        sql_snippet: activity
      - name: feature1
        type: string
        description: activity specific features
        sql_snippet: feature1
      - name: feature2
        type: string
        description: activity specific features
        sql_snippet: feature2
      - name: feature3
        type: string
        description: activity specific features
        sql_snippet: feature3
      - name: feature4
        type: string
        description: activity specific features
        sql_snippet: feature4
      - name: feature5
        type: string
        description: activity specific features
        sql_snippet: feature5
      - name: feature6
        type: string
        description: activity specific features
        sql_snippet: feature6
      - name: feature7
        type: string
        description: activity specific features
        sql_snippet: feature7
      - name: feature8
        type: string
        description: activity specific features
        sql_snippet: feature8
      - name: feature9
        type: string
        description: activity specific features
        sql_snippet: feature9
      - name: feature10
        type: string
        description: activity specific features
        sql_snippet: feature10
      - name: activity_occurence
        type: number
        description: how many times has this activity happened to this customer
        sql_snippet: activity_occurence
      - name: activity_repeated_at
        type: date
        description: The date of the next instance of this activity for this customer
        sql_snippet: activity_repeated_at
    measures:
      - name: total_activities
        sql_snippet: activity_uuid
        type: count
        description: count of total activities
```

### Step 2: Deploy the Lens using Postman

With the YAML for the Lens being created, the next step is to deploy it. Postman will be used as the deployment tool. Ensure that you have installed Postman and followed all necessary steps to deploy the Lens.

### Step 3: Exploring the Audience App

Once the Lens is deployed on the DataOS environment, access the Audience [Application](../audiences.md) from the DataOS Homepage and navigate to the [Builder](../audiences.md) section. As soon as you deploy a lens by the name `c360` that satisfies all the prerequisites, it automatically showcases in the Audience Builder. Here now, you can check out all the entities that are there in the c360 model, various fields and measures that are available within them, and also take a look at the visual representation of relationships between them. The below image depicts the various steps to be executed while building audiences:
 
<center>

![Picture](./aud.svg)

</center>

The following is a comprehensive procedure that outlines the steps depicted in the aforementioned diagram:

#### Step 3.1: Provide a Name and Description for the Audience

As a primary step, it is essential to supply the name and description to the audience. The provision of the name is a mandatory requirement, while the description is optional.

> 📖 Best Practice: Providing an appropriate description for the audience is part of the best practices so that people within the organization can easily find out what the saved audiences (or cohorts) represent.

#### Step 3.2: Select a Cluster

In this step, select a cluster if it has not been pre-selected. If the desired cluster has already been pre-selected, proceed to the next step.

Upon selecting a cluster, you will be presented with a summary of all available data. The bar graph in the block displays the percentage of the selected cohort's audience, taking into consideration that no filter conditions or parameters have been applied at this time.
 
<center>

![Picture](./untitled_4.png)

</center>

The summary statistics reveal that out of the total data set, only 61.97% of individuals have email information available, 98.45% have phone numbers on record, and 99.74% have address information. These statistics are essential in determining the appropriate marketing channel to use.

#### Step 3.3: Set Filter Conditions

The filter capabilities provide you with the ability to segment your target audience based on specific criteria and traits. For example, by implementing a filter on the metric of total activities, to evaluate the number of target audience members who have completed more than 5 activities, simply navigate to the "Activity Stream" section within Filters and select the "+ Add rule" button. Configure the operator to ">=" and set the value to "5," as illustrated below.
 
<center>

![Picture](./untitled_5.png)

</center>

To access the values and frequency information for a specific column, click on the `i` icon located adjacent to the column name. This will bring up a pop-up window displaying the detailed information for that column.
 
<center>

![Picture](./untitled_6.png)

</center>

#### Step 3.4: Update

Upon clicking the "Update" button, the Summary Statistics for the selected cohort of individuals who meet the filter criteria will be displayed. The Percentage Bar within the Summary Statistics shows the proportion of individuals who satisfy the criteria. The text panes below indicate the percentage of the audience that possess email addresses, phone numbers, and physical addresses. Once you have confirmed that this is the desired audience, you may proceed to save them.

#### Step 3.5: Saving the Targeted Audience

The audience whose activity meets or exceeds the threshold of 5 has now been acquired. The summary reveals that 85.3% of the 100% of the audience satisfies the criteria. Within this group, 60.24% have email addresses, 98.63% have phone numbers, and 100% have physical addresses.
 
<center>

![Picture](./untitled_7.png)

</center>

Once you save the Audiences, they are saved in the [Audiences](../audience_ui/audience_ui.md) by the name you provided earlier, and you can still make changes to them, but you cannot schedule them or query them using Workbench until you Publish them. 

#### Step 3.6: Publish the Audiences

You can click the eye-like icon near the Save button to Publish the Audiences. Only when the audiences are Published, you can schedule them. You can Clone the Published Audiences to create new ones using the Clone button.

#### Step 3.7: Schedule the Audiences

Schedule the Audiences using the feature available in the Audiences App. You can choose the cadence interval, whether it's every minute, hour, day, etc. 

> 🗣️ The Audience workflow will only commence another iteration once the previous one has been successfully concluded. If an error occurs prior to the next scheduled iteration, the workflow will initiate at the designated cron time.
 
<center>

![Picture](./untitled_8.png)

</center>

#### Step 3.8: Saving the Audiences. Again!!!

As soon as you save the audiences again after scheduling, a workflow will be triggered to write the audience data to the DataOS internal storage, Icebase. 

#### Step 3.9: Utilizing the Generated Audience Information

Once the Audience data has been saved to the Icebase, it can be accessed using the Workbench for marketing campaigns targeting these specific audiences. To access the data, select the `icebase` depot and the `audience_segment` catalog in the Workbench, where you have two datasets available, `segment_stream` and `max_occurence_state`. Both these datasets can be queried to provide answers to various questions. An example query is provided below:

```sql
SELECT * FROM "icebase"."audience_segment".segment_stream LIMIT 10;
```