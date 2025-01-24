# Data Product Developer Learning Track

This track is designed to equip you with the skills needed to develop robust and scalable Data Products using DataOS. 

By the end of this course, you'll be able to:

- **Understand business needs**: Align Data Products with business goals and define quality and security requirements.

- **Design effective data models**: Use DataOS Metis and Workbench to analyze and refine data assets.

- **Build and implement Data Products**: Develop logical semantic models, data pipelines, and apply access control.

- **Deploy and manage Data Products**: Utilize CI/CD practices for seamless deployment and updates.

## Module 1: Understanding data needs

To create a successful Data Product, it’s crucial to first understand the business context and requirements. This module focuses on capturing key needs and expectations for Data Products for your organization based on Righ to Left approach:

<div class= "grid cards" markdown>

- [Understanding business goals](/learn/dp_developer_learn_track/understand_business_goals/)

</div>

## Module 2: Designing Data Products

This module dives into the detailed process of designing Data Products tailored to meet specific business needs. It covers every aspect from defining use cases, and discovering existing resources, to creating a robust design and ensuring quality, security, and compliance.

<div class= "grid cards" markdown>

- [Designing Data Products](/learn/dp_developer_learn_track/design_dp/)  

</div>

## Module 3: Building Data Products

In the previous module, we explored the essential steps for designing a Data Product. We started by defining the use case of Customer Purchase Behavior for an online retail company. This use case focuses on analyzing customer buying patterns to identify cross-sell opportunities and enhance marketing strategies.

Now that we have a clear design plan, it’s time to move into the development phase. In this module, we will build the Data Product step by step, setting up the necessary components within DataOS. You should follow the different topics in the given order to ensure a smooth and systematic approach to building the Data Product.

<div class= "grid cards" markdown>

- [#1 Establishing data connections](/learn/dp_developer_learn_track/data_source_connectivity/)

- [#2 Building data pipelines](/learn/dp_developer_learn_track/build_pipeline/)

- [#3 Implementing quality checks to maintain data integrity](/learn/dp_developer_learn_track/quality_check/)

- [#4 Creating semantic models](/learn/dp_developer_learn_track/create_semantic_model/)

- [#5 Implementing Data Policies that govern access and security](/learn/dp_developer_learn_track/data_policy/)

- [#6 Creating APIs to expose data for consumption by other systems](/learn/dp_developer_learn_track/data_api/)

</div>

## Module 4: Deploying Data Products

The final step is to deploy the Data Product, making it available for consumption and ensuring it can be easily managed and updated.

<div class= "grid cards" markdown>

- [#1 Packaging the Data Product and related Resources into a deployment Bundle](/learn/dp_developer_learn_track/create_bundle/)
 
- [#2 Defining Data Product spec file](/learn/dp_developer_learn_track/create_dp_spec/)

- [#3 Deploying Bundle and Data Product specifications using CLI](/learn/dp_developer_learn_track/deploy_dp_cli/)

- [#4 Implementing CI/CD integration to automate updates for reliable Data Products](/learn/dp_developer_learn_track/ci_cd/)

</div>

## Checklist for success

To complete the Data Product Developer learning track, ensure you accomplish the following tasks using DataOS components:

1. :white_check_mark: Verify DataOS CLI installation and initialization.  
2. :white_check_mark: Create Depot manifests using Instance Secrets to store credentials securely.  
3. :white_check_mark: Explore Data on Workbench and Access Metis for Quality and Lineage to ensure suitability with the use case.  
4. :white_check_mark: Create pipelines (Workflows) for data ingestion (if the use case requires), ensuring desired schedule and observability.  
5. :white_check_mark: Define and implement SLOs for accuracy, freshness, completeness, uniqueness, schema, and validity using Soda Workflow using SodaCL.  
6. :white_check_mark: Monitor Quality Checks in Metis with SLO-based results and trend analysis via detailed metrics and charts.  
7. :white_check_mark: Write SQL Scripts to extract necessary columns and define logical table manifests along with metrics.  
9. :white_check_mark: Define segments and manage access controls with user groups.  
10. :white_check_mark: Build Data APIs to create data applications.  
11. :white_check_mark: Deploy the Data Product and verify that it is visible and accessible to intended users.  
