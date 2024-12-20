# Evaluating input & output datasets 

This topic explains how to access detailed information about input and output datasets. Users can explore these details through two options available in the Data Product Hub: delve into Metis to review metadata, schema, and quality standards, or explore them directly in Workbench for a greater insight into the data.

## Scenario

To gain a deeper understanding of the data you plan to use for the marketing campaign, you thoroughly explore the input and output datasets of the 'Product 360' Data Product. You analyze the schema and metadata for insights, such as identifying missing fields or outdated entries, to better comprehend the data.

On Data Product Hub, open the data product details and follow the below steps:

## Step 1: Start with Data Product details

Begin by reviewing the data product's input and output datasets in the Data Product Hub. This initial overview provides insight into the dataset’s structure and integrity. For deeper details, open the dataset in Metis to explore schema, quality, lineage, and policies.

Click on the Metis option as shown below:

![explore_in_metis.png](/learn/dp_consumer_learn_track/eval_io_datasets/explore_in_metis.png)

## Step 2: Explore metadata of input dataset in Metis

For structured data sources, you will see comprehensive details such as asset type, meta version, last update time, follower count, and various editing options for owner, tier, domain, tags, and description.

You will see the DataOS address for your dataset. Within DataOS, each source system is identified by a unique Uniform Data Link (UDL). This address acts as a consistent reference point, regardless of the source system's internal naming conventions and structure. Leveraging the UDL enables access to datasets and seamless execution of various operations.

You will also get schema details, including table/column names, their descriptions and type, constraints, and sensitive tags, etc. You can suggest some tags if required.

![dataset_metis.png](/learn/dp_consumer_learn_track/eval_io_datasets/dataset_metis.png)

### **1. Assess schema and tags**

In the schema section, you can view tags assigned to each column. You may also request additional tags that align with your use-case and compliance. Tags are invaluable for tracking and categorizing data elements that meet specific requirements, such as regulatory standards or analytical needs.

### **2. Review stats & activity feeds**

Get an overview of the dataset structural information such as, total records, file size, partitions, snapshots, schema updates , etc. Activity feeds gives you an idea about conversations around the dataset and tasks created.

![structure_info.png](/learn/dp_consumer_learn_track/eval_io_datasets/structure_info.png)

### **3. Inspect queries and data profiling**

1. The Queries section provides insights into how frequently the dataset is queried, indicating its utility and relevance in real-world scenarios. 
    
    ![query_on_dataset.png](/learn/dp_consumer_learn_track/eval_io_datasets/query_on_dataset.png)
    
2. Data profiling results on Metis show valuable metrics on data distribution and column profiles, helping you know whether the dataset’s structure aligns with your analytical needs.
    
    ![dataset_profiling.png](/learn/dp_consumer_learn_track/eval_io_datasets/ce85fb16-0137-41dc-b92c-3901bd5832f3.png)
    
3. Column profile helps you find the distribution of values within each field, null values, unique values, etc. This can highlight patterns or outliers, indicating anomalies or irregularities that might require further investigation. Understanding these patterns allows you to validate assumptions about the data. For this dataset, there are no missing values for the column of interest. 
    
    You can further investigate the quality issues if any, by clicking on the number of tests. 
    
    ![col_profile.png](/learn/dp_consumer_learn_track/eval_io_datasets/col_profile.png)
    

### **4. Check Data Quality**

The information includes data validation rules for the customer dataset, organized by type (table-level or column-level) and focus area (Schema, Accuracy, Completeness, Validity). Each rule is paired with recent run statuses ('Last 5 Runs') to monitor ongoing compliance.

This information is critical to assess the dataset’s integrity. Monitoring these checks allows quick identification and correction of data issues, improving reliability for downstream processes.

![dataset_quality.png](/learn/dp_consumer_learn_track/eval_io_datasets/dataset_quality.png)

Based on the provided rules and their descriptions, potential quality issues and the probable action are listed :

| Issue | Rule | Description | Action |
| --- | --- | --- | --- |
| **Data Type Mismatch** | Birth year should be integer | Non-integer values in `birth_year` may cause processing errors. | Convert to integers and enforce integer format validation during entry. |
| **Country Field Accuracy** | Avg. length of country > 6 | Short entries in `country` may indicate incomplete or incorrect names. | Standardize to full names and apply cleaning to correct abbreviations or incomplete data. |
| **Customer ID Completeness** | Customer ID should not be zero | Zero values in `customer_id` may imply missing or placeholder IDs, affecting uniqueness. | Replace zero values with unique IDs; review processes to prevent zero entries. |

### **5. Investigate Data Lineage**

View the lineage of the dataset to understand its source, transformations, and dependencies. By checking lineage, you can see the jobs that created and modified the dataset, helping you confirm that the data is prepared and processed to meet your use case requirements.

![dataset_lineage.png](/learn/dp_consumer_learn_track/eval_io_datasets/dataset_lineage.png)

### **6. Confirm compliance policies**

Finally, review policies associated with the dataset to ensure compliance with necessary governance and security standards. This ensures the dataset aligns with legal and regulatory requirements, safeguarding sensitive data. If required, you can suggest tags for columns to apply default policies

![policies_on_metis.png](/learn/dp_consumer_learn_track/eval_io_datasets/policies_on_metis.png)

<aside class="callout">
🗣 If the dataset does not contain any default policies, you can request related tags on Metis UI on Dataset details page. Or you can contact your team to implement policies at the semantic model level.

</aside>

By following these steps, you gain a comprehensive understanding of the dataset’s quality, structure, and usage, ensuring it aligns with your specific analytical and business needs.

## Step 3: Performing exploratory data analysis using Workbench

After understanding the schema, structure, and quality of your dataset, you’re ready to dive into exploratory data analysis on DataOS Workbench. This web-based data exploration tool lets you run both simple and complex queries across a variety of relational databases, storage systems, and lakehouses. By doing this, you can examine the actual data and assess its suitability for your specific use case.

### **1.  Open Workbench app**

On Data Product Hub, go to 'Workbench' option.

![workbench_on_dph.png](/learn/dp_consumer_learn_track/eval_io_datasets/workbench_on_dph.png)

### **2. Select a Cluster**

When you open the Workbench app, the first step is to select a cluster for your analytics workload. This cluster will handle the execution of your SQL scripts, and you should choose it based on your specific computing requirements.

![select_cluster.png](/learn/dp_consumer_learn_track/eval_io_datasets/select_cluster.png)

<aside class="callout">
🗣 To ensure your query runs successfully, please select a cluster that you are authorized to access. If you encounter an error after selecting a cluster, try choosing a different one. If the problem persists, please reach out to your administrator for assistance.

</aside>

### **3. Write and run your query**

Determine what information you need and use a query language like SQL to write commands that retrieve and process your data. Here’s how:

**Selecting Data**: Use `SELECT` statements to specify which columns and rows to retrieve, helping you focus on relevant details.

**Filtering Data**: Add `WHERE` clauses to narrow down results based on specific conditions, making your data more targeted.

**Joining Tables**: Combine data across multiple tables with `JOIN` operations to get a complete view.

**Aggregating Data**: Apply functions like `SUM`, `AVG`, `COUNT`, `MAX`, and `MIN` to perform calculations and summarize insights.

**Sorting and Grouping**: Organize results with `ORDER BY` for sorting and `GROUP BY` for grouping, enabling easy comparison and summarization.

Run your query.

![query_result.png](/learn/dp_consumer_learn_track/eval_io_datasets/query_result.png)

### **4. View results and policies**

Check the results of your query and review any applied governance policies. The details of the query can be seen after it has run. A cautionary red triangle will appear in the result bar If a governance policy has been applied to the table being queried. Click on it to see the details.

![policy_details.png](/learn/dp_consumer_learn_track/eval_io_datasets/policy_details.png)

<aside class="callout">
🗣 For a closer look at the metadata structure or to see sample data for the Outputs datasets, generated by the data product, simply navigate to Metis and Workbench, following the instructions provided above.

</aside>

## Best practices

- **Assess metadata thoroughly**: Check for accurate descriptions of datasets and columns.

- **Evaluate data profiling metrics**: Inspect column profiles for null values, unique counts, and patterns. Use this to detect outliers or anomalies early.

- **Investigate lineage and dependencies**: Understand data transformations and sources. This information will help you understand whether the dataset meets the use-case requirements.

- **Check governance policies**: Know about compliance with regulatory and security standards, especially for sensitive data fields. You can 

## Guidelines: Do's and Don'ts

**Do's**

- Ask for missing column descriptions, as they provide essential context and help you fully understand the data.

- Use the 'Last 5 Runs' feature to track data quality trends over time and identify recurring issues.


**Don'ts**

- Don't rely on datasets with unresolved quality issues or failed validation checks, as these can propagate errors into downstream processes.

- Don't overlook untagged or misclassified columns, as they can create governance and compliance gaps.
    For instance, the email and phone columns in the following dataset lack tags to identify them as sensitive data, you can request the addition of appropriate tags to ensure their protection. 

    ![image](/learn/dp_consumer_learn_track/eval_io_datasets/col_missing_tags_metis.png)

## Next step

To further understand relationships between data entities and improve data comprehension, refer to the next module:

[Explore Semantic Model](/learn/dp_consumer_learn_track/explore_sm/)