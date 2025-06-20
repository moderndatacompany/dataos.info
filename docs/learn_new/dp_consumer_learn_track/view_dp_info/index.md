# Viewing Data Product details

In this topic, you'll learn to explore the details of a Data Product in the Data Product Hub.

## Scenario

During your initial exploration, you discovered the 'Product Affinity' Data Product. Now, you’ll delve into its detailed information such as data contributors, tier classification, linked GitHub repositories, semantic model, quality, etc. This helps you gauge its reliability and relevance for your analysis, such as product affinity analysis.

## Quick concepts


As we understand that Data Product is a ready-to-use, reliable, and governed data solution designed to provide meaningful and actionable insights to meet specific business needs. It is a self-contained entity that delivers analytical data through predefined inputs, outputs, and APIs. Let's understand more about its components.

### **Components of a Data Product**

- **Inputs**: Inputs refer to the raw data that feeds into a Data Product or analysis. These datasets serve as the foundation for all processing and transformations that the Data Product performs.

- **Outputs**: Outputs are the insights or processed data generated from a Data Product. A Data Product may have one or more outputs, or in some cases, none. These outputs might include processed datasets which are cleaned and transformed data, ready for analysis.

- **Semantic model**: A Semantic Model maps physical data to logical tables by defining relationships between data entities and creating meaningful metrics. It simplifies the underlying data structure into familiar business terms.

    1. **Abstracting complexity**:  It abstract representations of the data designed for ease of use.
    2. **Providing insights**: Enables easy understanding of key metrics and relationships. 
       - A Metric is a quantifiable measure used to track and evaluate the product performance or customer behaviour. Metrics are  derived from the Semantic Model and represent key business indicators.
    3. **Facilitating Interaction**: Serves as a user-friendly interface for data exploration.

- **Data Quality**: The degree to which data is accurate, complete, consistent, and reliable for its intended use.

- **Access options**: These are consumption portsfor exposing data through APIs or BI tools for downstream applications.

## What do you need to get started?

To make the most out of this guide, you should be familiar with:

- Basic data quality concepts and semantic modeling.

## Steps to view Data Product details

After discovering the 'Product Affinity' Data Product, follow these steps to explore its details.

1. **Access the Data Product details page:** From the Data Product Hub, select the 'Product Affinity' Data Product. This action will redirect you to the Data Product details page.
    
    ![view_access.png](/learn/dp_consumer_learn_track/view_dp_info/view_access.png)
    
2. **Review the details:** On the Data Product details page, you get the description, Git link, Jira link, tier, use cases, collaborators, quality checks applied on the Data Product, and an overview tab that shows the data flow.

3. **Get the details on inputs and outputs:** On navigating to the inputs tab you get the details on the input datasets that are fed into the Data Product. The details include the customer, product, and purchase table, in the customer table you get the details of the columns, their type, and the Data Product reference that has the same dataset used for its development.
    
    ![view_input.png](/learn/dp_consumer_learn_track/view_dp_info/view_input.png)
    
    - Similarly, you get the details of output datasets by navigating to the outputs tab.
    
    ![view_output.png](/learn/dp_consumer_learn_track/view_dp_info/view_output.png)
    
4. **Understanding the semantic model and Metrics:**
    - On the 'Semantic Model' tab, you get to understand the data model built on top of the Data Product that is populating the key metrics of the Data Product. Here, you can view the relations between logical tables and derived metrics and views.
        
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
        
6. **Access options:**
    You can explored the semantic model associated with your data Product using tools like Studio or integrated with various BI tools, AI/ML platforms, or applications using DataOS APIs. If a Data Product includes a Semantic Model, then the following consumption ports are available on  the access options tab:

    - Power BI and MS Excel
    - Jupyter Notebook
    - Data APIs
    - Postgres
    - GraphQL

    Output datasets are generally consumed via Talos APIs. As well as these outputs can become inputs for some other Data Products.


## Best practices

- **Review metadata for insights**: Always check metadata for the Data Product description, quality checks, and ownership to ensure it aligns with your requirements.

- **Evaluate Suitability of Data Products**: Check linked resources, like Git repositories or Jira tickets, to understand its development and governance history.

- **Check inputs and outputs**: Ensure they align with your analysis requirements.

## FAQs

**Q1: How can Semantic Models be consumed?**  
Semantic Models can be explored using tools like Studio or integrated with BI tools and GraphQL APIs. Their versatility makes them suitable for a wide range of consumption layers.

**Q2: What are Metrics in a Semantic Model?**  
Metrics are quantifiable measures used to track and evaluate the performance of a Data Product or user behavior. Derived from the Semantic Model, they represent key business indicators.

**Q3: How are Outputs consumed in a Data Product?**  
Outputs are generally consumed through Talos APIs for direct integration with systems. However, they can be input for other Data Products to enable seamless data processing across multiple Data Products.

**Q4: What are consumption ports?**  
Consumption ports are the methods or interfaces to expose data from a Data Product. Examples include APIs, BI tools, and GraphQL APIs.

**Q5: What happens if a Data Product has no semantic model?**  
If a Data Product lacks a Semantic Model, its outputs are typically limited to processed output datasets that are consumed using Talos APIs. "Talos" is a service within DataOS that provides APIs for interacting with data.


## Next step

You can further examine input and output datasets for their metadata, schema, and quality related details.

[Exploring Input and Output Data](/learn/dp_consumer_learn_track/eval_io_datasets/)