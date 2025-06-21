# Designing Data Products

This module dives into the detailed process of designing data products tailored to meet specific business needs. It covers every aspect from defining use cases, and discovering existing resources, to creating a robust design and ensuring quality, security, and compliance.

Whether you're a Product Manager, Data Scientist, or Developer, this guide will help you systematically build a data product that provides actionable insights and meets organizational goals. By the end of this module, you will be able to:

- Identify key use cases for a data product
- Evaluate and leverage existing data products
- Identify input data sources and plan ETL processes
- Understand the semantic models 
- Understand the data quality and security requirements
- Plan for compliance with data regulations

## Scenario

Imagine an online retail company aiming to boost its sales next year. The business team has tasked the Product Manager with developing a data product that can uncover valuable insights from customer purchase behaviors. The goal is to identify cross-sell opportunities, helping sales and marketing teams fine-tune their strategies to increase revenue.

As a Product Manager, you must design this data product, ensuring it captures essential metrics like cross-sell opportunity scores, purchase frequency, and total customer spending. 

Designing a data product requires meticulous planning and a deep understanding of the business needs. To effectively design the data product, consider the following key aspects:

## Step 1. Defining use cases and metrics

Defining clear use cases is the foundation of any successful data product. It involves understanding business needs, identifying key problems, and determining the metrics that will help solve them.

### **a. Identify and validate use cases**

Start by defining the specific business problems your data product aims to solve. Use cases often focus on providing actionable insights for stakeholders like sales teams, marketing analysts, or data science teams.

**Example Use case:** Analyze **Customer Purchase Behavior** to understand product affinity and identify cross-sell opportunities.

**Questions to ask:**

- What business problems are we solving with this data product?
- Who are the key stakeholders, and what insights do they need?
- How will this data product support decision-making processes?

### **b. Define business metrics**

Identify key performance metrics that align with your use case goals. These metrics will drive the analysis and provide value to the stakeholders.

**Key Metrics:**

- **Cross-sell opportunity score:** Likelihood of customers purchasing additional product categories.
- **Purchase frequency:** Number of purchases made over a specific period.
- **Total spending:** Total expenditure of a customer on products.

**Questions to ask:**

- Which metrics are most valuable for our stakeholders?
- How will these metrics be utilized in business strategies?
- Are there any dependencies or limitations affecting these metrics?
- Can these metrics be tracked with the existing data, or do new data sources need to be integrated?

## Step 2. Discovering existing Data Products

Before building a new data product, explore if similar products already exist within your organization to avoid duplication and leverage available resources.

### **a. Conduct a search in the Data Product Hub**

On the Data Product Hub, using search and filters, identify existing data products that might meet your use case requirements.

**Questions to ask:**

- Is there an existing data product that can be adapted for this use case?
- What existing products offer similar metrics or features that can be reused?

### **b. Evaluate existing Data Products**

Analyze the quality and relevance of existing data products, considering their metrics, data freshness, and structure.

**Questions to ask:**

- Does the data quality meet our required standards?
- Are the metrics aligned with our use case goals?

## Step 3. Designing the Data Product

If existing data products do not meet the desired outcomes, it's time to consider designing a new Data Product. To ensure alignment with business objectives, follow a right-to-left approach— start from the defined goals and work backward to structure the Data Product effectively.

### **a. Start with key metrics**
In the first step, we have already defined the measurable outcomes in terms of key metrics that align with your business objectives.

Example: Cross-sell opportunity score, purchase frequency, and total spending.

### **b. Identify measures and dimensions**

Break down key metrics into specific measures (quantitative data points) and dimensions (categorical attributes).

**Questions to ask:**

- What are the measures directly tied to each metric (e.g., revenue, counts, percentages)?
- Which dimensions are critical to segmenting or filtering the data (e.g., customer, product, geography)?
- How do measures and dimensions interact to create actionable insights?
- Are there existing standards or definitions for these measures and dimensions, or do they need to be defined?
- Are there any additional dimensions that might enrich the analysis or provide deeper insights?

Measures: Sales revenue, purchase frequency.
Dimensions: Customer demographics, product categories.

### **c. Identify input data sources**

Identify the data sources containing these dimensions. We require them to build the Data Product. Examples include CRM data, sales transactions, and product inventory data. You need to create Depots for the source connectivity.

- Customer demographic data (`customer_info`)
- Transaction data (`purchase`)
- Product information (`product`)

**Questions to ask:**

- Which storage system holds the customer /Sales information?
- Which datasets have the necessary measures and dimensions?
- Are there any gaps in the data that need to be addressed?

### **d. Data exploration and understanding**

Explore and understand the content and structure of your datasets using Metis and Workbench. This will help you understand the raw data.

**Questions to ask:**

- What are the key transformations needed?
- Are there any missing or outlier values that need to be handled?

## Step 4. Identifying the need for ETL process

The ETL process is critical for converting raw data into a usable format. It involves extracting data, transforming it based on business logic, and loading it into a storage system.  This process enables the creation of source-aligned data products, which represent data in its original form with minimal transformation. These source-aligned products can then be used to create consumer-aligned data products.

### **a. Define ETL processes**

Design an ETL pipeline to process raw data into structured datasets.

- **Extract:** Retrieve data from various sources.
- **Transform:** Clean and aggregate data for analysis.
- **Load:** Store processed data in a central data warehouse.

**Questions to ask:**

- What transformations are essential for data preparation?
- How often should the ETL process run to maintain data freshness?

### **b. Define data quality checks**

Embed quality checks to validate data integrity during the ETL process.

Quality checks include:

- **Completeness:** Ensure no missing values.
- **Uniqueness:** Avoid duplicate records.
- **Consistency:** Validate data types and formats.

**Questions to ask:**

- Which quality checks are most critical for this product?
- How will issues be detected and resolved?

## Step 5. Defining the semantic model

The semantic model provides a logical structure for the data, defining key entities and relationships, making it easy for end users to query and understand.

Creating a semantic model can be particularly beneficial in situations such as:

- When data needs to be accessible to a wide range of users with varying levels of technical expertise. Such as, a marketing team can easily view customer data through simplified metrics like "Total Sales" instead of raw database fields.
- When there is a need for a single, consistent view of data across different departments or systems. For instance, different departments like finance and sales may have different ways of defining 'revenue'. But a semantic model standardizes the definition of revenue across systems.
- When complex data needs to be made more understandable and usable for business decision-making. For example, when column names need to be changed to more business-friendly terms for decision-making.
- When building applications to answer data-related questions using large language models (LLMs).

Organize the transformed data into a structured logical model (Lens) that represents key customer and product relationships. Users can explore data through this logical model.

**Components of semantic model:**

- **Tables**: Customer, Product, or Sales.
- **Dimensions:** Customer demographics, product details.
- **Measures:** Sales revenue, purchase frequency.
- **Relationships/joins:** Link customer purchases to products.

**Questions to ask:**

- Identify entities to define logical tables
- What are the critical dimensions and measures?
- How will relationships between entities be represented?
- Does the model capture all necessary metrics?

### **a. Define logical tables, dimensions, measures**

The data model is defined in collaboration with the development team. Create the logical tables containing dimensions and measures incorporates three key metrics derived from the customer, product, and purchase tables: cross-sell opportunity score, purchase frequency, and total spending.

<aside class="callout">
🗣️ Logical tables are beneficial in scenarios where organizations prefer not to replicate data or wish to directly access data from source systems. They do not persist, making them ideal when you want to avoid duplication or store data in a Lakehouse-type storage. In such cases, semantic models offer significant advantages by providing structured access to the data. </aside>

## Step 6. Ensuring data security and compliance

Ensuring data security and compliance with regulations is crucial to protecting sensitive data throughout its lifecycle. Define governance right there for semantic model. It includes defining rules for access control, and compliance, ensuring that the data remains safe and trustworthy.

### **a. Define data access and security policies**

Implement attribute/role-based access control and data masking to secure sensitive data.

**Questions to ask:**

- Who should have access to this data product?
- Are there sensitive data elements that require masking?
- How will we maintain compliance with privacy regulations?

## Step 7: Defining SLOs

SLOs or service level objectives are quantitative measurement of a service’s performance or reliability, measured over time. SLOs guide/ support architecture, operations and observability decisions.

**Questions to ask:**

- What are the relevant architecture target metrics for the DP?
- What are the relevant data quality target metrics for the DP?
- What are the relevant data governance target metrics for the DP?

### **Key Metrics:**

- **Architecture**: Performance, scalability, and reliability.
- **Data Quality**: Completeness, freshness, and accuracy.
- **Governance**: Compliance with regulations like GDPR, HIPAA, etc.

Several quality checks are need to be established to ensure adherence to data quality standards:

- **Completeness:** No missing (null or blank) values are allowed in the `customer_id` column, and every row must contain a valid, non-null `customer_id`.
- **Schema:** The schema must be validated to ensure that column data types align with the defined structure.
- **Freshness:** Purchase data must be kept up to date.
- **Uniqueness:** Each `customer_id` must be unique, with no duplicates permitted.
- **Validity:** Any occurrence where the invalid count (`invalid_count(mntwines)`) exceeds 0 highlights a data quality issue that requires attention.

## Step 8: Output and delivery

Identify how end users will consume the data product and the methods used for data delivery, such as APIs or connecting with BI tools.

### **a. Define the API interfaces needed to deliver data insights to users**

**Questions to ask:**

- How will users access the data product?
- What API specifications are required for seamless integration?

In this module, we explored the complete process of designing a data product—from defining clear use cases to implementing data quality checks, and ensuring robust security and compliance. By addressing the key questions provided throughout, you can effectively identify the necessary requirements and design a data product that meets your organization's needs and drives business value.

## Next step

Now that you have a solid understanding of the design process, the next step is to move into implementation phase. This involves translating your data product design into an actionable plan and beginning the actual development starting with establishing the data connections.

[Establishing data connections](/learn/dp_developer_learn_track/data_source_connectivity/)