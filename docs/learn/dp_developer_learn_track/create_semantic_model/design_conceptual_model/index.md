# Designing the conceptual model


This topic explores how a Data Engineer conceptualizes a semantic model, transforming business needs into the model. This enables them to create and monitor key business metrics to ensure the model meets their analytical and business needs.

## Scenario

With clear business objectives and measurable KPIs defined, you're now ready to move to the designing the conceptual data model. At this point, the business has given you valuable insights into what they want to achieve, but it’s your job as a Data Engineer to translate those objectives into a structured, actionable model that will drive insights.

The conceptual data model serves as the blueprint for the entire data structure. It defines the core entities, their relationships, and the data points needed to analyze the KPIs and meet the business goals. This model forms the foundation for everything that will follow—so it’s crucial to get it right.

## Identifying core business entities

At this stage, you need to determine the primary business entities your data model will need to include. These entities are essentially the objects your data will describe, and each plays a crucial role in measuring the business’s performance.

In consultation with stakeholders, you identify the following key entities for your model:

- **Customer**
- **Product**
- **Purchase**

These core entities will allow you to analyze the business’s most critical issues. It’s now time to start defining relationships between them.

## Defining relationships between entities

Once you’ve identified your core entities, the next step is to define how they are related to one another

For instance:

- **Customer to Purchase**: A `one-to-many` relationship. Each customer can have multiple purchases, but each purchase is associated with only one customer.
- **Purchase to Product**: A `many-to-many` relationship. A single purchase can include multiple products, and each product may be part of many purchases.

These relationships allow you to ask insightful questions, such as:

- How do customer purchase behaviors differ across different product categories?
- What are the most common products bought together by customers from different segments?
- How can changes in product offerings influence customer purchasing patterns?

By clearly defining these relationships, you set the stage for the next phase—where you’ll begin organizing the data around these entities and relationships, building the actual schema that will enable your KPIs to be tracked.

## Conceptual model design

At this point, you’ll start creating the conceptual model. Here’s a simplified diagram of how the entities and relationships might look:

```jsx
+------------------+                +------------------+                +------------------+
|     Customer     |  One-to-Many   |     Purchase     |  Many-to-Many  |     Product      |
+------------------+  -------------> +------------------+ -------------> +------------------+
|                  |                |                  |                |                  |
|                  |                |                  |                |                  |
|                  |                |                  |                |                  |
+------------------+                +------------------+                +------------------+

```

---

## Measures and dimensions

Once the relationships are established, it’s time to define the dimensions and measures for each entity. Dimensions provide context, while measures quantify key business metrics. For example:

| **Entity** | **Related To** | **Relationship** | **Fields and Dimensions** | **Measures** |
| --- | --- | --- | --- | --- |
| Customer | Purchase | One-to-Many | `customer_id`, `birth_year`, `education`, `marital_status`, `income`, `country`, `customer_segments` | `total_customers` |
| Product | Purchase | Many-to-One | `product_customer_id`, `product_id`, `product_category`, `product_name`, `price`, `product_affinity_score`, `purchase_channel` | `total_products` |
| Purchase | Customer | Many-to-One | `p_customer_id`, `purchase_date`, `recency_in_days`, `mntwines`, `mntmeatproducts`, `mntfishproducts`, `mntsweetproducts`, `mntgoldprods`, `mntfruits`, `numdealspurchases`, `numwebpurchases`, `numcatalogpurchases`, `numstorepurchases`, `numwebvisitsmont`, `purchases`, `spend`, `country_name` | `recency`, `purchase_frequency`, `total_spend`, `average_spend`, `churn_probability`, `cross_sell_opportunity_score` |

## Logical model

After you establish your goals, value objectives, drivers, measures, and dimensions, This is how your logical semantic model looks like 

```jsx
+------------------+
|     Customer     |
+------------------+
| customer_id      | (PK)
| birth_year       |
| education        |
| marital_status   |
| income           |
| country          |
+------------------+
        |
        |  One-to-Many
        |
        v
+------------------+
|   Purchase       |
+------------------+
| purchase_id      | (PK)
| purchase_date    |
| p_customer_id    | (FK) -----> references Customer(customer_id)
| mntwines         |
| mntmeatproducts  |
| mntfishproducts  |
| mntsweetproducts  |
| mntgoldprods    |
| mntfruits        |
| numdealspurchases |
| numwebpurchases  |
| numcatalogpurchases |
| numstorepurchases |
| numwebvisitsmont |
| purchases        |
| spend            |
| country_name     |
+------------------+
        |
        |  Many-to-One
        |
        v
+------------------+
|     Product      |
+------------------+
| product_id       | (PK)
| product_customer_id |
| product_category  |
| product_name     |
| price            | |
+------------------+

```

## Next steps

The next step is implementing the data model. This involves conceptually representing business objects, their relationships, and the rules governing them within the DataOS Lens framework. Before implementing you must be well aware of the key concepts and elements of Lens essential to build the semantic model

[Key concepts of Lens](/learn/dp_developer_learn_track/create_semantic_model/key_concepts_of_lens/)