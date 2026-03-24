# Optimize bundling Resources in Data Product

When developing a Data Product, efficiently bundling Resources is essential for streamlined deployment, management, and scalability. There are multiple approaches to bundling Resources based on their operational characteristics, and selecting the right approach depends on the specific needs of the project. The two common strategies for bundling are:

- **Bundling by lifecycle stages:** Grouping Resources based on the phases of the data product lifecycle, such as Design, Build, Deploy, Activate, and Monitor.
- **Bundling by Resource characteristics:** Grouping Resources based on their frequency of change or operational nature, where Resources that are frequently updated are bundled separately from those that are more static.

## Bundling by data product lifecycle stages

An approach to bundling is to structure Resources according to the lifecycle stages of the Data Product. This method groups Resources based on the stages they belong to, such as Design, Build, Deploy, Activate, and Monitor. This is useful for ensuring that Resources are managed in alignment with the overall lifecycle and may provide better traceability for each phase. 

Here’s an example of how a Data Product can be structured according to these lifecycle stages:

```
├── design
│   ├── mock_data_script/
│   └── mock_semantic_model/
├── build
│   ├── data_processing
│   │   ├── input/
│   │   └── output/
│   ├── semantic_model/
│   ├── quality
│   │   ├── input/
│   │   └── output/
│   ├── access_control
│   │   └── policy/
│   └── build_bundle.yaml
├── monitor
│   ├── pager/
│   ├── monitor/
│   └── monitor_bundle.yaml
├── activation
│   ├── data_apis/
│   ├── notebooks/
│   ├── custom_apps/
│   └── activation_bundle.yaml
├── deploy
│   ├── deploy_bundle.yaml
│   ├── data_product_spec.yaml
│   └── scanner.yaml
└── readme
```
Below are the descriptions for each phase of the Data Product lifecycle:

- **Design phase:** During this phase, Resources are focused on preparing mock data and creating initial semantic models that will serve as the foundation for data processing and analytics. Resources bundled here may include scripts for generating mock data and semantic models.

- **Build phase:** In the build phase, the Resources focus on actual data processing, quality assurance, semantic model development, and setting up necessary policies for data access control. Resources involved in building and validating data processing pipelines, creating quality checks, and defining policies are grouped together in this bundle.

- **Deploy phase:** Resources involved in deployment are primarily responsible for packaging the product, generating deployment configurations, and managing the overall deployment process. This bundle includes Resources for deployment bundles, specifications, and scanners for monitoring the deployment state.

- **Activate phase:** Resources required to activate and expose the Data Product to users (e.g., APIs, notebooks, or custom applications) are bundled here. These Resources ensure that the Data Product becomes available to the end-users for their interactions.

- **Monitor phase:** Once the Data Product is live, continuous monitoring is essential to ensure its operational health and quality. Resources dedicated to monitoring the data and operational processes, such as monitoring services or alert systems, are grouped in this bundle.

## Bundling by Resource characteristics

This approach focuses on grouping Resources by how often they change or are used within the Data Product lifecycle. Resources that are involved in finite tasks, such as data ingestion, transformation, and validation, are grouped together, while those that require continuous updates or interactions are bundled separately. This approach typically involves the following categorization:

Resources in this category are involved in one-time or infrequent tasks and generally do not require updates unless specific changes occur (e.g., data refreshes). These include foundational operations like data ingestion and validation:

- **Depot:** Establishes the connection to the data source.
- **Flare:** Ingests data into the system.
- **Soda:** Performs data validation and quality checks.
- **Scanner:** Validates deployment and operational state.

These Resources are bundled together in a Workflow Bundle, ensuring efficient execution without the need for frequent redeployment. Resources that provide ongoing, real-time functionality require continuous updates and interactions, making them better suited for separate bundling:

- **Lens:** A semantic model that organizes and interprets data, providing continuous access to structured data for business users.


By separating service-oriented Resources, such as Lens into their own bundles, these Resources can operate continuously without interference from finite tasks within the Workflow-based bundle.

<aside class="callout">
🗣️ The separation of Resources into distinct bundles is typically suggested during the development or testing phase. This approach provides greater flexibility and ease of management as components are iterated upon. However, this strategy is highly subjective and depends on the specific needs of the project. Once the Data Product transitions to production, bundling strategies may be adjusted to optimize for stability and performance in a live environment.
</aside>

Consider a scenario where we are developing a Data Product focused on product affinity and cross-sell. For the sake of simplicity, we will concentrate on creating a selected set of Resources, namely Flare, Soda, and Lens. These Resources will be organized into distinct bundles optimized for efficient deployment, management, and scalability, with the assumption that the Depot resource has already been created separately.
In this case, two categories of bundles are created:

- **Ingestion and quality Workflow Bundle:** This Bundle includes Flare for data ingestion and Soda for quality assurance.
- **Service-based Resources Bundle:** This Bundle includes Lens for the semantic model for real-time analytics."


### **Step 1: Create Super DAG for Ingestion Workflow**

The first step involves creating a workflow for ingesting various datasets. Since multiple datasets such as customer, product, and transaction data need to be ingested, a Super DAG (Directed Acyclic Graph) is created to handle the ingestion process in a sequence. The Super DAG will be stored in the `build/data_processing` directory of the data product, specifically within the ingestion folder. This ensures that all the necessary ingestion logic and configurations are kept together and can be easily managed or updated when needed. The following is an example of the Super DAG for data ingestion:

```yaml
--8<-- "examples/resources/bundle/bundling_resources_in_data_product/ingestion_dag.yml"
```

### **Step 2: Quality check Super DAG Workflow**

After data ingestion, the next step is to perform data validation and quality assurance. The Quality DAG will be stored in the `build/quality/` directory of the data product. 

```yaml
--8<-- "examples/resources/bundle/bundling_resources_in_data_product/quality_dag.yml"
```


### **Step 3: Bundle for Flare and Soda Workflow**

Since Flare for data ingestion and Soda for data quality checks are finite Resources, they are bundled together into a single Bundle in the `deploy/` directory of the data product. This Bundle ensures that both data ingestion and quality checks are executed in a sequence and are tightly coordinated. 

```yaml
--8<-- "examples/resources/bundle/bundling_resources_in_data_product/bundle_for_dag.yml"
```

### **Step 4: Bundle for Lens**

Assuming the Resources for Lens (semantic model) are already created and stored in the `build/semantic_model` and  `activation/data_apis` directories respectively. These Resources are then referenced in a bundle, which is created in the `deploy/ ` directory for easy deployment. 

```yaml
--8<-- "examples/resources/bundle/bundling_resources_in_data_product/bundle_for_lens_and_talos.yml"
```

### **Step 5: Referencing Bundles in the Data Product manifest file**

Once the bundles for Lens are created, they need to be referenced within the Data Product's manifest file for deployment. The manifest file is a crucial component in linking these separate bundles to the overall Data Product.

```yaml
--8<-- "examples/resources/bundle/bundling_resources_in_data_product/referncing_bundle.yml"
```

