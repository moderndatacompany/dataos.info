# Viewing Data Product details

In this topic, you'll learn to explore the details of a Data Product in the Data Product Hub.

## Scenario

During your initial exploration, you discovered the 'Product 360' Data Product. Now, you’ll delve into its detailed information such as data contributors, tier classification, linked GitHub repositories, semantic model, quality, etc. This helps you gauge its reliability and relevance for your analysis, such as product affinity analysis.

## Quick concepts

Before we dive in, let’s review a few essential terms:

- **Inputs:** The raw data that feed into a Data Product or analysis.
- **Outputs:** The insights or processed data generated from a Data product.
- **Semantic Model:** A framework that defines and organizes data relationships to ensure clarity and consistency.
- **Metric:** A quantifiable measure used to track and evaluate the performance of a Data Product.
- **Data Quality:** The degree to which data is accurate, complete, consistent, and reliable for its intended use.

## What do you need to get started?

To make the most out of this guide, you should be familiar with:

- Basic data quality concepts and semantic modeling.

## Steps to view Data Product details

After discovering the “Product 360” Data Product, follow these steps to explore its details.

1. **Access the Data Product details page:** From the Data Product Hub, select the 'Product 360' Data Product. This action will redirect you to the Data Product details page.
    
    ![view_access.png](/learn/dp_consumer_learn_track/view_dp_info/view_access.png)
    
2. **Review the details:** On the Data Product details page, you get the description, Git link, Jira link, tier, use cases, collaborators, quality checks applied on the Data Product, and an overview tab that shows the data flow.

3. **Get the details on inputs and outputs:** On navigating to the inputs tab you get the details on the input datasets that are fed into the Data Product. The details include the customer, product, and purchase table, in the customer table you get the details of the columns, their type, and the Data Product reference that has the same dataset used for its development.
    
    ![view_input.png](/learn/dp_consumer_learn_track/view_dp_info/view_input.png)
    
    - Similarly, you get the details of output datasets by navigating to the outputs tab.
    
    ![view_output.png](/learn/dp_consumer_learn_track/view_dp_info/view_output.png)
    
4. **Understanding the semantic model and Metrics:**
    - On the semantic model tab, you get to understand the data model built on top of the Data Product that is populating the key metrics of the Data Product.
        
        Notable metrics include:
        
        - **Cross Sell Opportunity Score**
        - **Purchase Frequency**
        - **Total Spending**
        
        ![view_model.png](/learn/dp_consumer_learn_track/view_dp_info/view_model.png)
        
    - **Metrics Details**: On the Metrics tab, you’ll see how each metric is calculated from the input datasets. For example, the “Cross Sell Opportunity Score” metric is derived from the product and purchase datasets.
        
        ![view_metrics.png](/learn/dp_consumer_learn_track/view_dp_info/view_metrics.png)
        
5. **Review quality checks and access options:** 
    - On navigating to the quality tab, you get the details on the quality of the Data Product categorized by accuracy, completeness, freshness, schema, uniqueness, and validity.
        
        ![view_quality.png](/learn/dp_consumer_learn_track/view_dp_info/view_quality.png)
        
    - On the access options tab, you can see the ways to consume the Data Product via various tools:
        - Power BI and MS Excel
        - Jupyter Notebook
        - Data APIs
        - Postgres
        - GraphQL

## Best practices

- **Review metadata for insights**: Always check metadata for the Data Product description, quality checks, and ownership to ensure it aligns with your requirements.

- **Evaluate Suitability of Data Products**: Check linked resources, like Git repositories or Jira tickets, to understand its development and governance history.

- **Check inputs and outputs**: Ensure they align with your analysis requirements.


## Next step

You can further examine input and output datasets for their metadata, schema, and quality related details.

[Exploring Input and Output Data](/learn/dp_consumer_learn_track/eval_io_datasets/)