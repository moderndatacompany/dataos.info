# Implementing Masking Data Policy


When a Data Policy is implemented in DataOS, there are two primary options available:

**Using exisitng Data Masking Policies:** Predefined policies in DataOS can be applied to column data by assigning tags to the relevant columns via Metis. For example, if the goal is to mask an age column using a predefined policy such as age bucketing, the appropriate tag (e.g., PII.Age) should be applied to the column, and the pre-existing policy will be automatically enforced.

**Creating Custom Data Masking Policies:** If the predefined Data policies do not meet specific requirements, a custom policy can be created. This involves defining both a custom tag and a custom Data Policy. For instance, if the default age bucketing policy is unsuitable, a new policy can be created to group ages according to the desired preferences.


## How to implement Data Policy using exisitng Data Masking Policies?

The initial step in applying a Data Policy involves assigning tags to columns. Tags serve as identifiers, facilitating the categorization and management of data based on its sensitivity and regulatory requirements.

To illustrate, consider a scenario where we aim to categorize the `Age` column within the customer table 

Let's first examine the state of our Age column data before implementing the policy:

<div style="text-align: center;">
  <img src="/resources/policy/how_to_guide/maskingbefore.png" alt="Sample inaccessible dataset" style="border:1px solid black; width: 80%; height: auto;">
  <figcaption> Before: The Age column presents individual ages without any grouping</ficaption>
</div>

### **Assign tags to columns**

1. Access **Metis** and navigate to the **Assets** section.

    <div style="text-align: center;">
    <img src="/resources/policy/how_to_guide/dataoshomepage.png" alt="Sample inaccessible dataset" style="border:1px solid black; width: 80%; height: auto;">
    <figcaption>Metis</ficaption>
    </div>

2. Search for the specific table containing the data to be masked, e.g.,**`icebase.retail.customer`**.

    <div style="text-align: center;">
    <img src="/resources/policy/how_to_guide/metis.png" alt="Sample inaccessible dataset" style="border:1px solid black; width: 80%; height: auto;">
    <figcaption>Metis</ficaption>
    </div>

3. Select the relevant table from the search results to display all associated columns.
    
    <div style="text-align: center;">
    <img src="/resources/policy/how_to_guide/customertable.png" alt="Sample inaccessible dataset" style="border:1px solid black; width: 80%; height: auto;">
    <figcaption>Metis - customer table</ficaption>
    </div>

4. Within the **Schema** section, click on the search box to search specific columns intended for grouping or redaction. e.g., to categorize the Age column using the bucket_number masking policy, locate the Age column within the table.
    
    <div style="text-align: center;">
    <img src="/resources/policy/how_to_guide/customertable.png" alt="Sample inaccessible dataset" style="border:1px solid black; width: 80%; height: auto;">
    <figcaption>Metis - customer table Schema section</ficaption>
    </div>

5. In the Tag column, click on the **Add** button and select the appropriate tag, such as **`PII.Age`**, to apply to the column.

    <div style="text-align: center;">
    <img src="/resources/policy/how_to_guide/customertable.png" alt="Sample inaccessible dataset" style="border:1px solid black; width: 80%; height: auto;">
    <figcaption> Applying PII.Age tag on Age column in customer table</ficaption>
    </div>

*You have now successfully applied a tag to the Age column.*

## How to implement Data Policy using custom Data Masking Policies?

### **Create a custom tag via Metis**

To create a new tag within Metis, follow these steps:

**Access Metis:** Log in to the Metis platform using your credentials.

**Navigate to Governance:**

Click on the Govern button located in the top right corner of the page.

**Access Tag Groups:**

Choose the appropriate tag group like `PII` where you want to create a new tag, or create a new tag group if needed.

**Add a New Tag:**

Click on the Add Tag button in the top right corner to initiate the creation of a new tag. for instance, `mycustomtag`.

**Define Tag Details:**

Provide a Name and Description for the new tag to clearly identify its purpose and usage.


### **Create a Data Policy manifest file**

After creating the tag, the next step is to define the policy associated with it. For example, if you need to customize an age bucket data masking policy for the tag PII.mycustomtag, the policy structure will be as follows:


???tip "Filter Policy for city not equals to Verbena"

    ```yaml
    --8<-- "/examples/resources/policy/sample_mask_data_policy.yml"
    ```

### **Assign tag to the appropriate column of the dataset
**
Once the tag has been created and its associated policy defined, the next step is to apply this tag to the appropriate column within the dataset. This ensures that the policy is enforced on the specified data. Follow these steps to apply the tag:

**Navigate to the Dataset:** Open the Metis platform and locate the dataset you want to modify.

**Select the Dataset:** Click on the dataset to view its schema and details.

**Identify the Column:** Browse through the dataset schema to find the column that requires the tag application.

### **Apply the Tag:**

Apply the tag using the same process as in first method.
