# Designing Data Products

This module dives into the detailed process of designing data products tailored to meet specific business needs. It covers every aspect from defining use cases, and discovering existing resources, to creating a robust design and ensuring quality, security, and compliance.

Whether you're a Product Manager, Data Scientist, or Developer, this guide will help you systematically build a data product that provides actionable insights and meets organizational goals. By the end of this module, you will be able to:

- Identify key use cases for a data product
- Evaluate and leverage existing data products
- Design input data sources and plan ETL processes
- Define a semantic model and validate its accuracy
- Ensure data quality and security
- Plan for compliance with data regulations

## Scenario

Imagine an online retail company aiming to boost its sales next year. The business team has tasked the Product Manager with developing a data product that can uncover valuable insights from customer purchase behaviors. The goal is to identify cross-sell opportunities, helping sales and marketing teams fine-tune their strategies to increase revenue.

As a Product Manager, you must design this data product, ensuring it captures essential metrics like cross-sell opportunity scores, purchase frequency, and total customer spending. 

Designing a data product requires meticulous planning and a deep understanding of the business needs. To effectively design the data product, consider the following key aspects:

## Step 1. Defining use cases

Defining clear use cases is the foundation of any successful data product. It involves understanding business needs, identifying key problems, and determining the metrics that will help solve them.

### **a. Identify and validate use cases**

Start by defining the specific business problems your data product aims to solve. Use cases often focus on providing actionable insights for stakeholders like sales teams, marketing analysts, or data science teams.

**Example Use case:** Analyze **Customer Purchase Behavior** to understand product affinity and identify cross-sell opportunities.

**Questions to ask:**

- What business problems are we solving with this data product?
- Who are the key stakeholders, and what insights do they need?
- How will this data product support decision-making processes?

### **b. Define business Metrics**

Identify key performance metrics that align with your use case goals. These metrics will drive the analysis and provide value to the stakeholders.

**Key Metrics:**

- **Cross-sell opportunity score:** Likelihood of customers purchasing additional product categories.
- **Purchase frequency:** Number of purchases made over a specific period.
- **Total spending:** Total expenditure of a customer on products.

**Questions to ask:**

- Which metrics are most valuable for our stakeholders?
- How will these metrics be utilized in business strategies?

## Step 2. Discovering Existing Data Products

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

After defining the use case and key metrics, you proceed to the design phase of the Data Product. by identifying input data sources, defining data transformations, and creating a semantic model.

### **a. Identify input data sources**

Identify the data sources required to build the product. Examples include CRM data, sales transactions, and product inventory data. You need to create Depots for the source connectivity.

- Customer demographic data (`customer_info`)
- Transactional data (`sales_transactions`)
- Product catalog (`product_inventory`)

**Questions to ask:**

- Which storage system holds the customer /Sales information?
- Which datasets have the necessary measures and dimensions?
- Are there any gaps in the data that need to be addressed?

### **b. Data exploration and understanding**

Explore and understand the content and structure of your datasets using Metis and Workbench. This will help you understand the raw data.

**Questions to ask:**

- What are the key transformations needed?
- Are there any missing or outlier values that need to be handled?

## Step 4. Identifying the need for ETL process

The ETL process is critical for converting raw data into a usable format. It involves extracting data, transforming it based on business logic, and loading it into a storage system. 

### **a. Define ETL processes**

Design an ETL pipeline to process raw data into structured datasets.

- **Extract:** Retrieve data from various sources.
- **Transform:** Clean and aggregate data for analysis.
- **Load:** Store processed data in a central data warehouse.

**Questions to ask:**

- What transformations are essential for data preparation?
- How often should the ETL process run to maintain data freshness?

### **b. Implement data quality checks**

Embed quality checks to validate data integrity during the ETL process.

**Quality checks include:**

- **Completeness:** Ensure no missing values.
- **Uniqueness:** Avoid duplicate records.
- **Consistency:** Validate data types and formats.

**Questions to ask:**

- Which quality checks are most critical for this product?
- How will issues be detected and resolved?

## Step 5. Defining the Semantic Model

The semantic model provides a logical structure for the data, defining key entities and relationships, making it easy for end users to query and understand.

Organize the transformed data into a structured logical model (Lens) that represents key customer and product relationships. Users can explore data through this logical model.

### **a. Define logical tables**

The data model is defined in collaboration with the development team. It incorporates three key metrics derived from the customer, product, and purchase tables: cross-sell opportunity score, purchase frequency, and total spending.

**Components of Semantic Model:**

- **Dimensions:** Customer demographics, product details.
- **Measures:** Sales revenue, purchase frequency.
- **Relationships:** Link customer purchases to products.

**Questions to ask:**

- What are the critical dimensions and measures?
- How will relationships between entities be represented?
- Does the model capture all necessary metrics?

## Step 6. Ensuring data security and compliance

Ensuring data security and compliance with regulations is crucial to protecting sensitive data throughout its lifecycle.

### **a. Define data access and security policies**

Implement attribute/role-based access control and data masking to secure sensitive data.

**Questions to ask:**

- Who should have access to this data product?
- Are there sensitive data elements that require masking?
- How will we maintain compliance with privacy regulations?

### **b. Defining quality checks**

Several quality checks are need to be established to ensure adherence to data quality standards:

- **Completeness:** No missing (null or blank) values are allowed in the `customer_id` column, and every row must contain a valid, non-null `customer_id`.
- **Schema:** The schema must be validated to ensure that column data types align with the defined structure.
- **Freshness:** Purchase data must be kept up to date.
- **Uniqueness:** Each `customer_id` must be unique, with no duplicates permitted.
- **Validity:** The `mntwines` attribute must conform to specified criteria, ensuring the data falls within a valid range of 0 to 1. Any occurrence where the invalid count (`invalid_count(mntwines)`) exceeds 0 highlights a data quality issue that requires attention.

### **Step 7: Output and delivery**

Identify how end users will consume the data product and the methods used for data delivery, such as APIs or connecting with BI tools.

### **a. Define the API interfaces needed to deliver data insights to users**

**Questions to ask:**

- How will users access the data product?
- What API specifications are required for seamless integration?

In this module, we explored the complete process of designing a data product—from defining clear use cases to implementing data quality checks, and ensuring robust security and compliance. By addressing the key questions provided throughout, you can effectively identify the necessary requirements and design a data product that meets your organization's needs and drives business value.

## Next step

Now that you have a solid understanding of the design process, the next step is to move into implementation. This involves translating your data product design into an actionable plan and beginning the actual development starting with establishing the data connections.

[Establishing data connections](/learn/dp_developer_learn_track/data_source_connectivity/)