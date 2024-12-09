# Optimize bundling Resources in Data Product

When developing a Data Product, efficiently bundling Resources is essential for streamlined deployment, management, and scalability. This process involves grouping Resources into a single bundle based on their operational characteristics.

Resources such as Depot, Flare, SODA, Lens, and Talos are involved in various tasks across the Data Product lifecycle, from data ingestion and transformation to validation and real-time analytics. Instead of separating them into multiple bundles, we now propose bundling all these Resources into a single, comprehensive bundle for the entire data pipeline. For example:

**Depot:** Establishes the connection to the data store.
**Flare:** Ingests data into the system.
**SODA:** Performs data validation and quality checks.
**Lens:** Organizes and interprets data for business users, ensuring ongoing accessibility.
**Talos:** Provides real-time analytics and API services, responding to queries and updates as data changes.
By grouping these Resources together in a unified bundle, the data pipeline can be managed more efficiently, with streamlined deployment and consistent operation throughout its lifecycle. This single bundle approach ensures that all tasks, whether finite (such as data ingestion and validation) or ongoing (such as analytics and real-time data services), are executed in a cohesive manner.

This approach simplifies both the deployment and management processes, allowing for better scalability as the Data Product evolves. Bundling all Resources together ensures that updates and changes can be managed in one place, ensuring consistency across the entire data product without the need for separate workflows or bundles.

