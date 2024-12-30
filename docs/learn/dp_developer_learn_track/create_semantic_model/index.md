# Build a semantic model 

This guide outlines the end-to-end process for building and deploying a semantic model (Lens) in DataOS. It covers everything from conceptualizing the model to implementing, testing, and deploying it for analytical and business needs.

## Scenario

After you've established data connections and built robust data pipelines to process and transform raw data, the next step is to create a semantic model (Lens) on top of the Product-360 Data Product. Your objective is to transform raw data into a structured model that enables the generation of trusted, consistent metrics and KPIs. These metrics will be accessible through APIs and usable across business intelligence, AI, and embedded analytics tools.

## Quick concepts
Semantic models aim to represent data in a way that is easily understandable by business users.

**Why are semantic models important in data products and management?**

- **Improved Data Accessibility:** Semantic models present data in a understandable way, using a common business language that enables users of all technical levels to access and use data effectively, promoting self-service in data product development.
- **Enhanced Data Discovery:** By organizing data clearly, semantic models simplify the process of discovering and exploring data, especially in large or complex datasets, helping users quickly find relevant information.
- **Easier Data Integration:** Semantic models define common meanings and relationships between data elements, making it easier to integrate and maintain consistency across various data sources and systems.
- **Support for Data Governance:** These models enforce data quality standards, ensuring accuracy and reliability, which is essential for regulatory compliance and maintaining trust in data products.
- **Empowering Business Users:** By simplifying technical complexities, semantic models allow business users to access and analyze data independently, fostering a data-driven culture and reducing reliance on IT teams.

Follow the below steps to build a semantic model:

## Step 1: Defining business objectives and KPIs

Before designing your Lens, establish the business objectives and key performance indicators (KPIs) the model will support to ensure that your semantic model is relevant, actionable, and focused on measurable outcomes.

[Define business objectives and KPIs](/learn/dp_developer_learn_track/create_semantic_model/define_business_objective/)

## Step 2: Understanding key concepts 

Before diving into the technical aspects of building the Lens semantic model, it's crucial to understand the key concepts and elements that make up the Lens framework.

[Key concepts of Lens](/learn/dp_developer_learn_track/create_semantic_model/key_concepts_of_lens/) 

## Step 3: Designing conceptual model

Once you've established your business goals and KPIs, the next step is to design the conceptual model. This involves identifying the core business entities, defining their relationships, and organizing the relevant dimensions and measures for analysis.

[Design conceptual data model](/learn/dp_developer_learn_track/create_semantic_model/design_conceptual_model/)

## Step 4: Creating the semantic model

Once your conceptual model is finalized, the next step is to implement it within the Lens framework. This process involves setting up a clear Lens folder structure, defining SQL scripts for data extraction, organizing tables, and implementing dimensions, measures, and metrics to reflect your business logic.


[Creating semantic model](/learn/dp_developer_learn_track/create_semantic_model/create_lens_folder/) 


## Step 5: Testing the model

After implementing the model, you must test it to ensure the data flows correctly and the relationships work as expected. Testing ensures that the model provides accurate and reliable metrics for decision-making. This is an optional step. However, we recommend testing the Lens in the local or development environment before deploying it on DataOS. 

[Test Lens locally](/learn/dp_developer_learn_track/create_semantic_model/testing_lens/) 


## Step 6: Deploying the model

Once tested, you can deploy the model to production. This phase involves optimizing the model for performance, ensuring it integrates with existing business systems, and making it accessible to users.

[Deploying Lens on DataOS](/learn/dp_developer_learn_track/create_semantic_model/deploy_lens_on_dataos/) 




