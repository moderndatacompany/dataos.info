---
search:
  exclude: true
---

# Beacon

Beacon is a standalone HTTP server designed to facilitate the exposure of data objects and tables contained within PostgreSQL databases. The server offers two distinct flavors (or types) of HTTP APIs, including REST, which leverages the `beacon+rest` stack, and GraphQL, which utilizes the `beacon+graphql` stack.

While both flavors of the Beacon stack are designed to offer functionality on top of PostgreSQL databases, it's essential to note that the API endpoints and operations are directly impacted by the structural limitations and permissions set by the database. Each flavor of the stack offers its unique and intuitive capabilities, which are detailed in the table below.

| Parameter | beacon+rest stack | beacon+graphql stack |
| --- | --- | --- |
| Function | Exposes entities within a PostgreSQL database through a RESTful API. | Exposes entities within a PostgreSQL database through a GraphQL API. |
| Protocol | REST | GraphQL |
| Querying | Simple CRUD operations using HTTP verbs (GET, POST, PUT, DELETE). | Advanced querying and filtering using GraphQL queries, mutations, and subscriptions. |
| Relationships | Supports basic foreign key relationships between tables. | Supports complex nested relationships and connections between tables. |
| Schema Generation | Uses PostgreSQL metadata to automatically generate a RESTful API. | Uses PostgreSQL metadata to automatically generate a GraphQL schema. |
| Use Cases | Well-suited for simple use cases where you need a quick and easy way to expose your database data through a RESTful API. | Designed to handle complex use cases where you need to perform complex queries on your database or work with related data in a flexible and efficient manner. |

## Beacon Service

The Beacon stack provides a robust solution for exposing a Postgres API endpoint to the external world. However, ensuring secure access, scalability, and seamless integration with other internal and external applications in DataOS can be complex. This is where the Service Primitive/resource becomes a critical factor.

By utilizing the Service Primitive/resource, you can ensure governed access to the endpoint, enable scalability in proportion to data growth and facilitate seamless access to all internal and external components and applications within DataOS. You can further enforce governance Policies to ensure secure access to PostgreSQL data, all in a declarative YAMLish manner within DataOS. 

![beacon]

In summary, a Beacon Service enables you to expose an API endpoint for a specific table in a PostgreSQL database, allowing you to send data to be stored and interact with the data in the table by sending HTTP requests to the endpoint. With a Beacon Service, your web and other data-driven applications in DataOS can perform CRUD operations, search, filter, and rename data assets stored in Postgres (the native relational database of DataOS).

## Syntax of Beacon YAML Configuration

![Beacon YAML Configuration Syntax]

<center><i>Beacon YAML configuration syntax</i></center>

## Create a Beacon Service

Creating a Beacon Service is a straightforward process that is accomplished within the DataOS platform using a simple declarative YAMLish syntax. While you need to have a basic understanding of Postgres to define migrations, the rest of the process is declarative and straightforward. Click on the link below to learn more.

[Creating Beacon Service ]

## Sections of a Beacon YAML Configuration

Let's take a closer look at each section of the YAML configuration and understand their importance in configuring your Beacon Service. For a detailed breakdown of each section and how to configure them, please visit the Beacon YAML configuration page.

[Beacon YAML Configurations]

## Recipes

[Exposing GraphQL API’s on Database using Beacon ]

[Exposing REST API’s on Database using Beacon]

[Store APIs on Beacon ]

[Query Pushdown Streamlit Application ]

[Query Pushdown SSL Postgres]

[Mask Data After Moving from Database to Icebase ]

[Exposing an API After Creating a Database ]