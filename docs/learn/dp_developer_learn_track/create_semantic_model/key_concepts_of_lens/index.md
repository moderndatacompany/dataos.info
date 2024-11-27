# Key concepts of Lens

Before delving into the technicalities of building a Lens semantic model, it’s essential to grasp the fundamental components and concepts that form the backbone of the Lens framework. Understanding these key elements will allow you to design and work with data models effectively. In this section, we'll cover the main aspects of the Lens framework: Tables, Views, Joins, Dimensions, Measures, and Segments.

## Elements of Lens

Let’s explore each of these elements in detail

### **Table**

Tables are logical constructs that define core entities in your semantic model, such as 'Customer', 'Product', or 'Sales'. They define the structure of your data, including dimensions (descriptive attributes) and measures (aggregated values), and specify relationships (joins) with other entities.

**Key Table components:**

- **Joins:** Define relationships between tables (e.g., linking 'customer' to 'product').
- **Dimensions:** Descriptive attributes like `owner_id` or `owner_name` that add context to your data.
- **Measures:** Quantifiable data points such as `count`, `sum`, or `average`, typically used in analytical calculations.
- **Segments:** Filters that categorize data into groups based on specific criteria (e.g., active vs. inactive users).

Following is the brief description of each component:

#### **1. Joins**

Joins define the relationships between different tables within the data model. Lens supports left joins by default and allows you to specify the nature of the relationship: one-to-one, one-to-many, or many-to-one. When you define a join in a table, the base table is always positioned on the left-hand side of the join.

**Key Join attributes:**

- **name:** The name of the table to join.
- **relationship:** The type of relationship, e.g., one-to-many or many-to-one.
- **sql:** The SQL condition that defines the join (e.g., `table1.id = table2.table1_id`).

#### **2. Dimensions**

Dimensions are descriptive fields that give context to your data. They help organize and filter data, making analyzing different aspects of an entity easier. Examples include `owner_name`, `city`, or `contact_email`. Dimensions are the building blocks for slicing and dicing your data into valuable insights.

**Key Dimension attributes:**

- **name:** A unique identifier for the dimension (e.g., `owner_id`).
- **type:** The data type of the dimension (e.g., string, number, time).
- **description:** A detailed explanation of the dimension's role and significance.
- **primary_key:** The dimension’s primary key, used for establishing relationships.
- **public:** Controls whether the dimension is visible to all users.

#### **3. Measures**

Measures are quantifiable metrics that provide valuable business insights, such as the total revenue, number of sales, or customer count. These are typically used for aggregation or statistical operations.

**Key Measure attributes:**

- **name:** A unique identifier for the measure (e.g., `total_sales`).
- **sql:** The SQL expression that defines how the measure is calculated (e.g., `SUM(order_total)`).
- **type:** The type of measure (e.g., `sum`, `avg`, `count`).
- **description:** A concise explanation of the measure’s purpose.
- **filters:** SQL conditions that apply filters to the measure (e.g., limit to a specific date range).
- **rollingWindow:** Defines time-based measures like a trailing 7-day sum.
- **format:** Specifies the format for presenting the measure (e.g., number with two decimal places).

#### **4. Segments**

Segments allow you to categorize your data based on predefined filters, which are often used to group data into meaningful subsets, such as 'active users' or 'high-value customers'.

**Key Segment Attributes:**

- **name:** A unique name for the segment (e.g., `active_owners`).
- **sql:** The filter criteria used to define the segment (e.g., `{TABLE}.status = 'active'`).
- **public:** Controls visibility of the segment.
- **Meta:** Metadata provides additional context for the segment, such as security levels or custom tags.

### **Working with Views**

Views abstract away the underlying complexity of your data model, providing users with a simplified interface for querying key metrics. 

For example, a view might include details from the 'customer' and 'purchase' tables, aggregating relevant data such as `customer_id`, `product_name`, and `contact_email`, making it easier for end-users to understand and interact with the data.

#### **When to define Views?**
You define Views in the following scenarios:

1. **Defining Metrics**:
Views allow you to combine measures and dimensions from different tables, providing a consolidated data model tailored for specific use cases. For example, a view could give you all the necessary dimensions and measures to understand 'Weekly Spirits Sales in Florida' in a unified view.
2. **Providing a simplified interface**:
By exposing only the relevant measures and dimensions for a given use case, views help reduce the complexity of the underlying data model, making it easier for business users to access actionable insights without wading through raw data.

#### **Types of Views**

There are two primary types of Views in Lens: Entity-First Views and Metric-First Views. Each type is designed to meet different business needs.

##### **1. Entity-first View**

An Entity-First View is structured around a specific entity or object of interest, such as a `customer`, `product`, or `transaction`. It aims to provide users with a comprehensive, detailed view of an entity's attributes and relationships without focusing on aggregated metrics. To define an Entity-First View, you combine measures and dimensions from multiple tables that comprehensively describe an entity. 

##### **2. Metric-first View**

A Metric-first View is centered around a specific measure and typically includes time dimensions. The primary focus is providing clear, actionable metrics for business decision-making.

The Metric-first View enables users to track a single metric consistently, making it easier to answer questions like:

- What happened?
- Why did it happen?
- What will happen next?
- What should we do in response?

Defining a Metric-First View focuses on tracking a specific measure, such as `conversion rate` or `quarter-to-date`, `revenue`. The view will include related time dimensions and additional attributes necessary to analyze that metric effectively.

## Next step

After familiarizing yourself with the key concepts of Lens, the next step is to begin implementing a Lens by creating the Lens semantic model in your code editor.

[Creating the Lens semantic model in your code editor](/learn/dp_developer_learn_track/create_semantic_model/create_lens_folder/)