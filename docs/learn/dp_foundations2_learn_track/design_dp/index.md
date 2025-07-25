# Designing a Consumer-Aligned Data Product

!!! info "Overview"
    Designing a consumer-aligned Data Product isn't just about connecting data pipelines—it's about crafting insights that matter to your business. In this module, you’ll dive into a structured, right-to-left approach to design a **consumer-aligned Data Product** that meets real-world business goals with precision.

You’ll learn to translate business needs into well-modeled, high-quality Data Products that are secure, scalable, and insight-driven.

## Learning goals

By the end of this module, you’ll be able to:

- Define meaningful use cases and success metrics  
- Discover and evaluate existing Data Products  
- Plan source-to-consumption design with transformations  
- Design semantic models with governed access  
- Implement quality checks and delivery paths  

---
## 📘 Scenario
Imagine an online retail company aiming to boost its sales next year. The business team has tasked the Product Manager with developing a Data Product that can uncover valuable insights from customer purchase behaviors. The goal is to identify cross-sell opportunities, helping sales and marketing teams fine-tune their strategies to increase revenue.

As a Product Manager, you must design this Data Product, ensuring it captures essential metrics like cross-sell opportunity scores, purchase frequency, and total customer spending. Designing a Data Product requires meticulous planning and a deep understanding of the business needs. To effectively design the Data Product, consider the following key aspects:


## Step 1: Define the use case and metrics

###  **Identify Business Problems**

Anchor your design by answering: What decisions will this Data Product support? Talk to stakeholders, understand their pain points, and define the insight they seek.

**Example:** Unlock customer purchase trends to drive cross-sell strategies.

###  **Define metrics that matter**

Pin down measurable outcomes. These become your Data Product’s north star.

**Key Metrics:**

- Cross-sell Opportunity Score  
- Purchase Frequency  
- Customer Lifetime Value (CLV)  

**Checklist:**

- ✅ Are the metrics trackable using current data?  
- ✅ Do they align with business KPIs?  
- ✅ Are they actionable?  

---

## Step 2: Discover reusable Data Products

Before building anything new, explore the **Data Product Hub** for existing assets.

### **Search & evaluate**

- Use tags, filters, and lineage views  
- Check if any existing product meets your needs partially or fully  

**Evaluation questions:**

- Are the outputs up-to-date and accurate?  
- Do the included dimensions/measures align with your use case?  

---

## Step 3: Design the right data model

Work backwards from your outcome metrics and identify required inputs.

### **Start with key metrics**
In the first step, we have already defined the measurable outcomes in terms of key metrics that align with your business objectives.

Example: Cross-sell opportunity score, purchase frequency, and total spending.

### **Break down metrics**

Identify specific measures (quantitative data points) and dimensions (categorical attributes).

- **Measures:** Sales revenue, frequency, etc.  
- **Dimensions:** Product, customer, time, geography 

**Evaluation questions:**

- What are the measures directly tied to each metric (e.g., revenue, counts, percentages)?

- Which dimensions are critical to segmenting or filtering the data (e.g., customer, product, geography)?

- How do measures and dimensions interact to create actionable insights?


### **Identify source tables**

Identify the data sources containing these dimensions. We require them to build the Data Product. Examples include CRM data, sales transactions, and product inventory data.

- Customer demographic data (customer_info)
- Transaction data (purchase)
- Product information (product)

**Evaluation questions:**

- Which storage system holds the customer /Sales information?
- Which datasets have the necessary measures and dimensions?
- Are there any gaps in the data that need to be addressed?

### **Data exploration and understanding**
Explore and understand the content and structure of your datasets using Metis and Workbench. This will help you understand the raw data.

Use tools like Metis or Workbench to:

- Discover required fields  
- Validate data types and cardinality  
- Note any transformations or joins required  

**Evaluation questions:**

- What are the key transformations needed?
- Are there any missing or outlier values that need to be handled?

## Step 4: Identifying the need for ETL process

The ETL process is critical for converting raw data into a usable format. It involves extracting data, transforming it based on business logic, and loading it into a storage system. This process enables the creation of source-aligned Data Products, which represent data in its original form with minimal transformation. These source-aligned products can then be used to create consumer-aligned Data Products.

> If your data is already in a usable, structured format, you can skip this step.

### **Create ETL or Flare workflows to:**

- Clean and normalize fields  
- Join multiple sources  
- Maintain lineage  

**ETL essentials:**

Design an ETL pipeline to process raw data into structured datasets.

- **Extract**: Retrieve data from various sources.
- **Transform**: Clean and aggregate data for analysis.
- **Load**: Store processed data in a central data warehouse.

**Evaluation questions:**

- What transformations are essential for data preparation?
- How often should the ETL process run to maintain data freshness?

### **Define data quality checks**

Embed quality checks to validate data integrity during the ETL process.

Quality checks include:

- **Completeness**: Ensure no missing values.
- **Uniqueness**: Avoid duplicate records.
- **Consistency**: Validate data types and formats.

**Evaluation questions:**

- Which quality checks are most critical for this product?
- How will issues be detected and resolved?

---

## Step 5: Define the semantic model

The semantic model acts as the business-facing lens into your data. It simplifies exploration and enforces structure.

> ### **When to create a semantic model**
> 
> Creating a semantic model can be particularly beneficial in situations such as:
> 
> - **When data needs to be accessible to a wide range of users with varying levels of technical expertise**  
>   For example, a marketing team can easily view customer data through simplified metrics like **"Total Sales"** instead of raw database fields.
> 
> - **When there is a need for a single, consistent view of data across different departments or systems**  
>   For instance, different departments like finance and sales may define *revenue* differently. A semantic model standardizes the definition of revenue across systems.
> 
> - **When complex data needs to be made more understandable and usable for business decision-making**  
>   For example, renaming column names to more business-friendly terms can help stakeholders make better decisions.
> 
> - **When building applications to answer data-related questions using large language models (LLMs)**  
>   Semantic models help structure and clarify data, making it easier for LLMs to generate accurate and context-aware answers.


### **Model components**

- **Tables:** Purchase, Product, Customer  
- **Measures:** Purchase frequency, total spend  
- **Dimensions:** Region, age group, product category  
- **Relationships:** Customer → Purchases → Products  


**Evaluation questions:**

- Identify entities to define logical tables  
- What are the critical dimensions and measures?  
- How will relationships between entities be represented?  
- Does the model capture all necessary metrics?
 

---

## Step 6: Ensure data security and compliance

Design with **data governance** and **privacy** in mind.

### **Define Policies**

- Who gets access to which fields or rows?  
- Use RBAC and ABAC models  

### **Apply masking**

Mask sensitive PII like emails or phone numbers.

**Evaluation questions:**

- Have we classified sensitive data?  
- Are access controls reviewed regularly?  

---

## Step 7: Define SLOs and quality gates

Great Data Products are reliable. Define **Service Level Objectives (SLOs)** to maintain trust.

### **SLO categories**

- **Architecture:** Performance, uptime  
- **Quality:** Completeness, freshness, validity  
- **Governance:** Masking, lineage, access audits, compliance with regulations like GDPR, HIPAA, etc.  

### **Quality checks**

- Validate schemas  
- Ensure uniqueness (e.g., `customer_id` is unique)  
- Track nulls and outliers  

---

## Step 8: Enable output and delivery

Identify how end users will consume the Data Product and the methods used for data delivery, such as APIs or connecting with BI tools.


###  **APIs and BI tools**

- Use Lens to expose datasets  
- Define API contracts (GraphQL, REST)  
 

**Evaluation questions:**

- Do APIs meet downstream tool requirements?  
- Are outputs discoverable and documented?  

---

## Next step

You’ve sketched a complete design blueprint. Now it's time to bring it to life.

Each next module will guide you through building this design into a working consumer-aligned Data Product. Let’s build it—one module at a time!

👉 [Start with configuring source connectivity](/learn/dp_foundations2_learn_track/data_source_connectivity/)