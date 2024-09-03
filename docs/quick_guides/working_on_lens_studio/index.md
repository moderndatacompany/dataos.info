# Working on Lens Studio

!!! info "Information"
    This guide will help you leverage the Lens Studio features to access the data model and efficiently analyze and visualize your data.


With Lens Studio,  you can access your Lens to examine the same data model from diverse perspectives. Studio makes it easy to analyze data across different dimensions, providing the ability to slice and dice information to uncover insights.

**Key Features** 

- Write queries by selecting dimensions and measures to create tailored views to focus on specific data aspects.
- Examine the data model from multiple angles by using filters and sorting.
- Use segments to apply pre-defined group filters.

## Navigating the Lens Studio

When you first open Lens Studio, you’ll see the following interface, designed for efficient data exploration.

### Exploring your Lens

![lens_studio (1).png](/quick_guides/working_on_lens_studio/lens_studio_(1).png)

1. **Tables and Views**: On the left panel, you can see the list of tables and views.
2. **Selecting Dimensions and Measures**: Click on a table or view to expand and see its dimensions and measures. Select the ones you need for your analysis.
3. **Building Queries**: Select dimensions and measures to create your queries.
4. **Running Queries**: Click the "Run Query" button to execute your query and see the results.
5. **Applying Filters:** Filters help you focus on the data that matters by removing unnecessary details or including specific segments.
6. **Visualizing Data:** Switch between **Table**, **Chart**, and **Pivot** views to visualize your data in different formats.
7. **Perspectives and History:** Navigate through various options in the side menu.
    1. **Business Perspective:**  This view presents the measures and dimensions available across various tables and business views, making it easier to analyze business-specific data.
        
        ![business_user_perspective.png](/quick_guides/working_on_lens_studio/business_user_perspective.png)
        
    2. **Developer Perspective:** Gain insight into the measures and dimensions defined within logical tables and business views. This perspective provides detailed information tailored for developers working on the underlying tables and views.
        
        Developer perspective
        
        ![developer_perspective.png](/quick_guides/working_on_lens_studio/developer_perspective.png)
        
    3. **History**: Review and Reflect with the History Feature. You can keep track of your analytical journey by accessing and replaying past actions.

### Understanding Your Data Model

Go to the **Model** tab to explore the schema and fields.

1. **Accessing Summary of Data Model:** Get a high-level summary of your data model fields and access permissions.
    
    ![model_overview.png](/quick_guides/working_on_lens_studio/model_overview.png)
    
2. **Understanding Schema:** View the details about the model schema- dimensions, measures, and segments defined in the logical table/view. You can also view the SQL snippet, which provides the logic for mapping to the physical table.
    
    ![model_schema.png](/quick_guides/working_on_lens_studio/model_schema.png)
    
3. **Examining Graph View of Data Model:** View logical tables, business views, and their relationships for the data model. Click on any table or business view to see detailed information, such as the fields involved.
    
    
    ![model_graph.png](/quick_guides/working_on_lens_studio/model_graph.png)
    
4. **Viewing Manifest Files:** Here, you will get the information on manifest files defined for logical tables and views.
    
    ![model_files.png](/quick_guides/working_on_lens_studio/model_files.png)
    

## Analyzing Data

### **Building  and Running Queries**

Use dimensions and measures from your data model to create queries.

1. Expand a table or view, then select the dimensions and measures needed for your analysis. Selected fields will be added to members. 
    
    <aside class="callout">
    🗣 You can choose to show or hide a field in the query result by clicking the eye icon next to it in the members’ list.
    
    </aside>
    
2. Click the "Run Query" button to execute and view results.
    
    ![simple_query.png](/quick_guides/working_on_lens_studio/simple_query.png)
    

### **Applying Filters**

Use filters and sorting options to narrow down your data, focusing on specific segments. They help you to identify patterns and reveal relationships and insights. Example: Apply filters based on date ranges, categories, etc.

1. Here’s the query to analyze transaction revenues by product category and payment type. The relevant fields have been selected for the query.
    
    ![query_for_filter.png](/quick_guides/working_on_lens_studio/query_for_filter.png)
    
2. Suppose you want to focus on data for a specific payment method. Click the filter icon next to the relevant field to apply the filter.
    
    ![filter_selected.png](/quick_guides/working_on_lens_studio/filter_selected.png)
    
3. The field will appear in the filter panel, ready for you to apply filter criteria.
    
    ![filter_criterion.png](/quick_guides/working_on_lens_studio/filter_criterion.png)
    
4. Set the criteria and run the query to view the filtered data in the results.
    
    ![filter_criterion_query_run.png](/quick_guides/working_on_lens_studio/filter_criterion_query_run.png)
    

### Segments for Targeted Data Analysis.

Segments are pre-defined groups of filters. Segments are created while defining the business object's manifest file, such as Segment by demographics, purchase behavior, etc.

1. Suppose we're focusing on data for loyal customers, and we've already defined a loyal customer segment with the relevant filter criteria. You can apply this segment to filter the data. For demonstration, the query lists customers along with their loyalty status. 
    
    ![query_loyal_customer.png](/quick_guides/working_on_lens_studio/query_loyal_customer.png)
    
2. The loyal customers segment is defined in the Customer table. Drag and drop the segment to the members’ list.
3. Applying the loyal customer segment will filter the results to show only those customers. Simply Select segments to apply a predefined group filter. 
    
    ![segment_applied.png](/quick_guides/working_on_lens_studio/segment_applied.png)
    

### **Visualizing Data**

Switch between different views such as **Table**, **Chart**, and **Pivot** to visualize your data effectively.

1. Once you run a query and select the Chart option, a default chart will be generated for your data.
2. You can select the chart type that best represents your data for analysis. For date-wise revenue analysis, a line graph is more suitable for visualizing trends over time.
    
    ![timeline_chart.png](/quick_guides/working_on_lens_studio/timeline_chart.png)
    
3. You can configure the chart to meet your analysis requirements. In this example, additional fields are included for more granular level analysis. Data is grouped for the payment method.
    
    ![configure_chart.png](/quick_guides/working_on_lens_studio/configure_chart.png)
    

### Data Aggregation and Rearrangement with Pivot Feature

The Pivot feature helps you transform and simplify your data dynamically. It turns complex datasets into clear, insightful summaries, making it easier to spot trends and patterns.

1. After running a query, switch to the **Pivot** view from the visualization options. The data grid will adjust to allow for pivoting, where you can drag and drop different dimensions and measures.
2. Choose which dimensions and measures to display as rows and columns. For example, you might place "Product Categories" in rows and "Transaction revenue" in columns.
    
    ![lens_studio_pivot.png](/quick_guides/working_on_lens_studio/lens_studio_pivot.png)
    

<aside class="callout">
🗣 Use filters to refine the data in your pivot table and sorting to arrange it in ascending or descending order by specific measures.

</aside>

### Accessing and Replaying Past Analyses

The **History** feature in Lens Studio allows you to track and revisit your past data exploration. Whether you want to review the steps you took to reach a particular insight or need to retrace your work, the History feature provides a chronological log of all your actions within the studio.

1. To access History, **n**avigate to the History tab from the side menu. The History panel will display a list of recent actions, queries, and data visualizations.
2. Click on any item in the history list to see the details of that action, including the specific filters, dimensions, and measures you used.
    
    ![history.png](/quick_guides/working_on_lens_studio/history.png)
    
3. Run the query to ****restore your workspace to any previous state by selecting the desired entry in the history. This allows you to continue working from that point without having to manually redo your steps.

<aside class="callout">
🗣 This feature is especially useful if you want to replicate or refine a previous analysis. It saves time by letting you quickly revisit and validate past analysis states, as all steps are tracked.

</aside>

### Data Protection **Policies** and Viewing User Groups

In the Lens model, data is safeguarded by robust policies that ensure sensitive information remains secure. These policies govern access control, determining who can view, or interact with specific data. They also define how data should be masked to prevent unauthorized access to sensitive details.

**Masked Data**

Data masking policies can be defined on dimensions and measures to protect sensitive information. Masked data is partially or fully hidden, depending on the policies in place:

- Masked fields often appear with asterisks (e.g., ***1234) or other placeholders like redact.
- Only users with the appropriate permissions can view the full data.

**Viewing User Groups**

User groups are a way to organize users for managing access to various API scopes and easier application of data policies for different categories of users. Each user group specifies a set of users and their access controls. API scopes manage access to specific functionalities and endpoints. You can view the API scopes that user group members are permitted to access, with each scope representing particular endpoints or functionalities.

To control data visibility based on user groups, row filter policies can also be applied. When creating a Lens model,  these policies are configured to regulate access to specific data.

In Lens Studio, go to **Model tab**. you can easily check the permissions associated with your Lens model and its data:

![Model_overview.png](/quick_guides/working_on_lens_studio/Model_overview.png)

**Masking Applied for the Data**

With a masking policy applied to fields like income, the corresponding data in the query results will be redacted. You can notice the red triangle to denote that the masking policy applied.

![redact_income.png](/quick_guides/working_on_lens_studio/redact_income.png)

Click on the **Inspect** button. This is what the query looks like:

![redact_segment_payload.png](/quick_guides/working_on_lens_studio/redact_segment_payload.png)