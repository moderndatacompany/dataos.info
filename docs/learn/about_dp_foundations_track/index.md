# Data Product Foundations Track

!!! info "Overview"
    Your starting point for building smart, reliable Data Products in DataOS. This track is designed for anyone new to DataOS or just getting started with the concept of data product development. It introduces the foundational concepts, tools, and workflows you’ll use to build and manage Data Products with confidence.


## Who should take this track?

The 'Data Product Foundations' course is ideal for the following learner personas:

| Persona & Description | Why It Matters | Level |
|---|---|---|
| **New Data Engineers / Developers**
Beginners in building Data Products or DataOS | Learn the core building blocks without being overwhelmed by deep technical details. | Must-have |
| **Aspiring Data Product Developers & Owners**
Business/tech users moving into product roles | Get foundational knowledge to progress into specialized tracks. | Must-have |
| **Cross-functional Team Members**
Analysts, QA, support involved in data workflows | Understand how Data Products work and fit into end-to-end data operations. | Recommended |
| **Technical Decision Makers / Architects**
Architects, Admins, team leads evaluating DataOS | Gain a high-level overview of key DataOS primitives and workflows for better strategic planning. | Recommended |

✨ Ready to get started? Scroll down to explore the full track structure and dive into each course to begin your Data Product journey.


## Track structure

This learning track is divided into two hands-on courses:

| Course | Title | Description |
|--------|-------|-------------|
| 1 | [Creating a Source-Aligned Data Product](/learn/about_dp_foundations_track/#course-1-create-a-source-aligned-data-product) | Learn to build a foundational data product directly from raw source systems—starting from connectivity to monitoring and packaging. |
| 2 | [Creating a Consumer-Aligned Data Product](/learn/about_dp_foundations_track/#course-2-create-a-consumer-aligned-data-product) | Take your product further with transformations, semantic modeling, and governed delivery of metrics tailored for business users. |


<aside class="callout">
🗣 To fully engage with the hands-on components of this learning track, access to a dedicated DataOS training instance is required. Please contact your training team to obtain the necessary credentials.

</aside>

## 📚 Track details
Find the details of the two courses—each structured and designed to walk you through the lifecycle of a Data Product. Each module within these courses covers key topics through step-by-step guidance, hands-on examples, and best practices—ensuring a clear and practical learning experience. This Foundations track keeps the content streamlined, emphasizing core concepts and guiding learners through one complete end-to-end example.

<aside class="callout">
🗣 This track features hands-on modules utilizing both the DataOS CLI and GUI. You'll use the CLI to apply YAML configurations and execute workflows. Concurrently, you'll navigate key DataOS graphical interfaces—such as Workbench for querying data, Metis for metadata management, and the Data Product Hub (DPH) for overseeing Data Products—to gain comprehensive insights into the platform's capabilities.
</aside>

### **Course 1: Create a Source-Aligned Data Product**

Build your first Data Product using raw source system data. Learn how to connect, ingest, transform, and monitor datasets using DataOS primitives.

<div style="text-align: left; padding-left: 1em;">
<img src="/learn/about_dp_foundations_track/foundations1_track1.png" alt="infographics">
</div>

### 🌟 **Outcome: What you’ll build**

By the end of this course, you will have a fully deployed Source-Aligned Data Product in DataOS that takes raw source datasets as input and publishes curated output datasets—ready for discovery and consumption.

<img src="/learn/about_dp_foundations_track/outcome_sa.png" alt="infographics">


### 📚 **Core modules**

| No. | Module                                | Objective/Description                                                                                                                                                                  | Key Topics                                                                                                                                         |
|-----|----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| 1   | **Understanding Source-Aligned Data Product** | Understand what are source-aligned Data Products | - Features & Importance |
| 2   | **Connect with Source Systems**       | Learn how to connect existing external data sources to DataOS without moving the data, and inspect the structure using Workbench.                                                       | - DataOS Primitives: Instance Secrets, Depots, Stacks<br>- Configuring and applying Secrets & Depots                                               |
| 3   | **Scan Metadata and Explore Data**     | Use a Scanner workflow to fetch metadata from structured source systems and preview data in Metis and Workbench—without ingesting.                                                     | - Creating Scanner Workflows<br>- Viewing scanned metadata in Metis<br>- Exploring external data via Workbench                                    |
| 4   | **Build Workflows for Data Transformation & Ingestion** | Understand when and how to bring source data into DataOS and apply transformations using Flare workflows.                                          | - DataOS Primitives: Workflows, Services<br>- Writing Flare Workflows<br>- Ingesting and verifying data                                            |
| 5   | **Add Quality Checks**               | Add basic profiling and validation checks to ensure data trustworthiness.                                                                                                              | - Defining SLOs (Service Level Objectives)<br>- Using Soda Stack for quality checks<br>- Running profiling                                         |
| 6   | **Set Up Monitors & Pagers**         | Set up monitoring and alerting to track failures and ensure visibility into data issues.                                                                                               | - Creating Monitors for workflow and Soda failures<br>- Setting up Pagers with email/webhook alerts<br>- Validating alerts                        |
| 7   | **Build and Deploy Your First Source-aligned Data Product** | Package and deploy your Data Product by bundling all resources, defining the spec, and registering it in the Data Product Hub and Metis.                 | - Creating a bundle.yaml<br>- Writing the Data Product specification<br>- Deploying and registering the Data Product                              |

### ✅ **Start learning** 
!!! abstract "Ready to Dive In?" 
    :rocket: [Start this course here](/learn/dp_foundations1_learn_track/) 

### **Course 2: Create a Consumer-Aligned Data Product**

Take it further by designing a Data Product tailored for business consumption—featuring semantic modeling, governed access, and metric delivery.

<div style="text-align: left; padding-left: 1em;">
<img src="/learn/about_dp_foundations_track/foundations2_track1.jpg" alt="infographics">
</div>

### 🌟 **Outcome: What you’ll build**

By the end of this course, you will have a fully deployed Consumer-Aligned Data Product in DataOS designed for business consumption—complete with transformations, semantic modeling, governed access, and reusable metrics.

<img src="/learn/about_dp_foundations_track/outcome_ca.png" alt="infographics">

### 📚 **Core modules**

| No. | Module                               | Objective/Description                                                                                                                                  | Key Topics                                                                                                                                               |
|-----|--------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1   | **Define Business Requirements**     | Clearly define the business problem or opportunity the Data Product will address, aligning with measurable success criteria.                           | - Define objectives and KPIs<br>- Collaborate with business teams<br>- Identify metrics tied to outcomes                                                 |
| 2   | **Design Semantic Model**            | Design a logical schema to represent key business entities, relationships, and metrics. Identify data security needs for governed access.             | - Identify business objects<br>- Define dimensions and measures<br>- Model relationships<br>- Create business views<br>- Address data security           |
| 3   | **Create a Repo for Versioning**     | Set up a version-controlled repository to manage changes and enable collaboration across teams.                                                        | - Initialize a code repository<br>- Set up clear folder structure                                                                                         |
| 4   | **Connect with Source Systems**      | Configure depots to connect with both source and destination systems for reading and writing data.                                                     | - Create and apply Instance Secrets<br>- Configure Depots for read/write access                                                                          |
| 5   | **Transform & Ingest**               | Apply complex data transformations to create refined output datasets that meet business use case requirements.                                         | - Design transformation logic<br>- Create and deploy Flare workflows<br>- Ingest and validate output data                                                |
| 6   | **Create Semantic Model**            | Organize key metrics and relationships into a semantic layer for business users to easily explore via tools like Lens.                                 | - Set up semantic model folders<br>- Define SQL scripts & manifest files<br>- Configure business views and access control     |
| 7   | **Deploy and Register Data Product** | Package and register the complete Data Product so it’s discoverable in Data Product Hub and Metis.                                                     | - Create bundle.yaml<br>- Write the product spec<br>- Deploy and register the Data Product                                                               |

### ✅ **Start learning** 

!!! abstract "Ready to Dive In?" 
    :rocket: [Start this course here](/learn/dp_foundations2_learn_track/)
 