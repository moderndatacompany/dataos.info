# Optimize bundling Resources in Data Product

When developing a Data Product, efficiently bundling Resources is essential for streamlined deployment, management, and scalability. This process involves grouping Resources into distinct Bundles based on their operational characteristics. The rationale for bundling is to group Resources whose frequency of change is high together, while those that are applied once or infrequently should be bundled separately for better efficiency and management. Resources such as Depot, Flare, Soda, and Scanner are primarily involved in finite tasks, such as data ingestion, transformation, and validation. These operations are typically one-time or infrequent actions within the broader Data Product lifecycle and generally do not require frequent changes. For example:

- **Depot:** Establishes the connection to the data source.
- **Flare:** Ingests data into the system.
- **Soda:** Performs data validation and quality checks.

Once these tasks are completed, there is typically no need to re-run them unless there are specific updates.(e.g., data refreshes). As these Resources are foundational to the Data Product; they are often bundled together in a Workflow, ensuring efficient execution.

In contrast, Service-oriented Resources, such as Lens and Talos, provide continuous, real-time functionality. These Resources are often consumer-driven and require regular updates or interactions. For instance:

- **Lens:** A semantic model that organizes and interprets data for business users. It remains active to provide consistent access to organized data.
- **Talos:** Offers real-time analytics and API services, responding to queries and updates as data changes.

These Resources must remain active and responsive to changing data demands and user interactions. Due to their ongoing nature, they are better suited for a separate Bundle that manages their continuous operation. By separating these service-oriented Resources into their own bundle, you ensure that they can operate continuously without being affected by the finite tasks within the Workflow-based bundle.

<aside class="callout">
🗣️ The separation of Resources into distinct bundles is typically suggested during the development or testing phase. This approach provides greater flexibility and ease of management as components are iterated upon. However, this strategy is highly subjective and depends on the specific needs of the project. Once the Data Product transitions to production, bundling strategies may be adjusted to optimize for stability and performance in a live environment.
</aside>

Consider a scenario where we are developing a Data Product focused on product affinity and cross-sell. For the sake of simplicity, we will concentrate on creating a selected set of Resources, namely Flare, Soda, Lens, and Talos. These Resources will be organized into distinct bundles optimized for efficient deployment, management, and scalability, with the assumption that the Depot resource has already been created separately.
In this case, two categories of bundles are created:

- **Ingestion and quality Workflow Bundle:** This Bundle includes Flare for data ingestion and Soda for quality assurance.
- **Service-based Resources Bundle:** This Bundle includes Lens for the semantic model and Talos for real-time analytics."


### **Step 1: Create Super DAG for Ingestion Workflow**

The first step involves creating a workflow for ingesting various datasets. Since multiple datasets such as customer, product, and transaction data need to be ingested, a Super DAG (Directed Acyclic Graph) is created to handle the ingestion process in a sequence. The Super DAG will be stored in the `build/data_processing` directory of the data product, specifically within the ingestion folder. This ensures that all the necessary ingestion logic and configurations are kept together and can be easily managed or updated when needed. The following is an example of the Super DAG for data ingestion:

```yaml
--8<-- "examples/resources/bundle/bundling_resources_in_data_product/ingestion_dag.yml"
```

### **Step 2: Quality Check Super DAG Workflow**

After data ingestion, the next step is to perform data validation and quality assurance. The Quality DAG will be stored in the `build/quality/` directory of the data product. 

```yaml
--8<-- "examples/resources/bundle/bundling_resources_in_data_product/quality_dag.yml"
```


### **Step 3: Bundle for Flare and Soda Workflow**

Since Flare for data ingestion and Soda for data quality checks are finite resources, they are bundled together into a single Bundle in the `deploy/` directory of the data product. This Bundle ensures that both data ingestion and quality checks are executed in a sequence and are tightly coordinated. 

```yaml
--8<-- "examples/resources/bundle/bundling_resources_in_data_product/bundle_for_dag.yml"
```

### **Step 4: Bundle for Lens and Talos**

Assuming the Resources for Lens (semantic model) and Talos (real-time analytics and API services) are already created and stored in the `build/semantic_model` and  `activation/data_apis` directories respectively. These Resources are then referenced in a bundle, which is created in the `deploy/ ` directory for easy deployment. 

```yaml
--8<-- "examples/resources/bundle/bundling_resources_in_data_product/bundle_for_lens_and_talos.yml"
```

### **Step 5: Referencing Bundles in the Data Product manifest file**

Once the bundles for Lens and Talos are created, they need to be referenced within the Data Product's manifest file for deployment. The manifest file is a crucial component in linking these separate bundles to the overall Data Product.

```yaml
--8<-- "examples/resources/bundle/bundling_resources_in_data_product/referncing_bundle.yml"
```

