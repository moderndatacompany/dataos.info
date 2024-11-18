# Build a semantic model 

This guide outlines the end-to-end process for building and deploying a semantic model using Lens in DataOS. It covers everything from conceptualizing the model to implementing, testing, and deploying it for analytical and business needs.

## Scenario

After you've established data connections and built robust data pipelines to process and transform raw data, the next step is to create a semantic data model (Lens) on top of the Product-360 Data Product. Your objective is to transform raw data into a structured model that enables the generation of trusted, consistent metrics and KPIs. These metrics will be accessible through APIs and usable across business intelligence, AI, and embedded analytics tools.


## Step 1: Defining business objectives and KPIs

Before designing your Lens, establish the business objectives and key performance indicators (KPIs) the model will support to ensure that your semantic model is relevant, actionable, and focused on measurable outcomes.

[Define business objectives and KPIs](/learn/dp_developer_learn_track/create_semantic_model/define_business_objective/)


## Step2: Designing conceptual model

Once you've established your business goals and KPIs, the next step is to design the conceptual model. This involves identifying the core business entities, defining their relationships, and organizing the relevant dimensions and measures for analysis.

[Design conceptual data model](/learn/dp_developer_learn_track/create_semantic_model/design_conceptual_model/) 


## Step 3: Key concepts of Lens

Before diving into the technical aspects of building the Lens semantic model, it's crucial to understand the key concepts and elements that make up the Lens framework.

[Key concepts of Lens](/learn/dp_developer_learn_track/create_semantic_model/key_concepts_of_lens/) 

## Step 4: Implementing the model

Once your conceptual model is finalized, the next step is to implement it within the Lens framework. This process involves setting up a clear Lens folder structure, defining SQL scripts for data extraction, organizing tables, and implementing dimensions, measures, and metrics to reflect your business logic.


[Creating Lens folder structure](/learn/dp_developer_learn_track/create_semantic_model/create_lens_folder/) 


## Step 5: Testing the model

After implementing the model, you must test it to ensure the data flows correctly and the relationships work as expected. Testing ensures that the model provides accurate and reliable metrics for decision-making. This is an optional step. However, we recommend testing the lens in the local or development environment before deploying it on DataOS. 

[Test Lens locally](/learn/dp_developer_learn_track/create_semantic_model/testing_lens/) 


## Step 6: Deploying the model

Once tested, you can deploy the model to production. This phase involves optimizing the model for performance, ensuring it integrates with existing business systems, and making it accessible to users.

[Deploying Lens on DataOS](/learn/dp_developer_learn_track/create_semantic_model/deploy_lens_on_dataos/) 




