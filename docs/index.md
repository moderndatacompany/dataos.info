# DataOS Documentation

In the rapidly evolving world of data, the need for robust, scalable, and efficient data products has never been more critical. DataOS is a platform that transforms how businesses create, manage, and leverage data products. DataOS empowers business teams to innovate by providing the tools and autonomy for data product development.

DataOS is an enterprise-grade data product platform that enables organizations to build, manage, and share data products. It provides the essential building blocks, data developers require to create powerful data products that drive significant business outcomes. 

DataOS development is driven by core principles tailored to address specific user needs and challenges:

- **Consumption Ready Layer**: DataOS streamlines data product consumption with context-aware discovery, secure exploration, reliable quality, and multi-interface activation through its self-serve architecture.

- **Data Product Lifecycle Management**: DataOS is built to serve data product consumers, including data analysts/scientists and data app developers. It aims to capture the entire data product lifecycle, integrating data product consumers, owners, developers, and administrators under one roof. This holistic approach ensures seamless integration with tools that users are already familiar with.

- **Faster Time to Value**: DataOS accelerates the development process, enabling enterprises to gain insights quickly. This reduces the time to value substantially, fueling targeted campaigns, personalizing customer journeys, and enhancing profits faster.

- **AI Ready**: Leveraging AI agents, DataOS enhances the user experience by providing heuristic assistance that evolves based on user feedback and needs.

- **FinOps**: DataOS provides real-time insights into resource utilization, enabling organizations to monitor and control cloud spending effectively. This strategic approach promotes shared responsibility across teams, drives significant cost savings, improves operational efficiency, and facilitates informed financial decisions.

DataOS continuously evolves to meet the real-world needs of data professionals. It significantly lowers the total cost of ownership by streamlining data operations through task automation, minimizing data movement, and simplifying maintenance.

## Navigating Documentation

If you are new to DataOS, dataos.info is your go-to place for getting started with key technical concepts. Understanding these will help you develop data products efficiently with DataOS. For experienced developers looking to build solutions, how-to guides and reference docs are available to get you up to speed with data product creation. You'll find everything you need right here, whether starting or diving deep.

The documentation website features the top menu bar with the options like Getting Started, Data Products, Glossary, and Videos. A multi-level index is displayed on the left menu, allowing users to easily explore and dive deeper into specific topics within each category. 

### **First Steps**

The following sections in the top menu bar of the documentation will help you get started with DataOS.

<div class= "grid cards" markdown>

-   :material-content-duplicate:{ .lg .middle } **Getting Started**

    ---

    Get hands-on and up to speed with DataOS, and familiarize yourself with its capabilities.

    [:octicons-arrow-right-24:  Learn more](/getting_started/)


-   :material-network-pos:{ .lg .middle } **Data Product**

    ---

    Learn to create, deploy & manage domain-specific data products at scale.

    
    [:octicons-arrow-right-24: Explore more](/products/data_product/)


</div>

### **Core Aspects**

The following sections of the documentation, located on the left menu, provide detailed insights into the DataOS philosophy and its architecture.

<div class= "grid cards" markdown>

-   :material-card-bulleted-settings-outline:{ .lg .middle } **Philosophy**

    ---

    Understand the philosophy behind DataOS, designed to simplify and abstract the complexities of traditional data infrastructure.

    [:octicons-arrow-right-24: Read more](/philosophy/)


-   :material-list-box-outline:{ .lg .middle } **Architecture**

    ---

    Learn about the architecture of DataOS, built to democratize data, and accelerate data product creation.

    [:octicons-arrow-right-24: See more](/architecture/)

</div>

### **Understand Interfaces**

The Interfaces section in the documentation introduces various ways to interact with DataOS services and components.

<div class= "grid cards" markdown>

-   :material-card-bulleted-settings-outline:{ .lg .middle } **Command Line Interface (CLI)**

    ---

    The DataOS CLI enables efficient data operations, providing quick, flexible access to system functions for data engineers and administrators.

    [:octicons-arrow-right-24: Learn more](/interfaces/#command-line-interface-cli)


-   :material-list-box-outline:{ .lg .middle } **Graphical User Interface (GUI)**

    ---

    The Graphical User Interface provides an intuitive and visually appealing method for interacting with DataOS and its components.

    [:octicons-arrow-right-24: Learn more](/interfaces/#graphical-user-interface-gui)

-   :material-content-duplicate:{ .lg .middle } **Application Programming Interface (API & SDK)**

    ---

    The Application Programming Interface in DataOS enables seamless interaction with its core components and libraries, enabling the creation of diverse applications and services.

    [:octicons-arrow-right-24:  Learn more](/api_docs/)

</div>


### **Understand DataOS Resources**

Resources section of the documentation will help you understand the primitives of DataOS that power the core functionalities necessary in any data stack. We have mapped these DataOS Resources to their functional role in the data stack:

#### Source Connectivity and Metadata management

This category includes DataOS Resources that facilitate the connection to various data sources, scan the metadata, and run quality checks & data profiling.

<div class= "grid cards" markdown>

-   :resources-depot:{ .lg .middle } [**Depot**](/resources/depot/)

    ---
    Connects various data sources to DataOS, abstracting underlying complexities.   


-   :resources-stack:{ .lg .middle } [**Stacks**](/resources/stacks/)

    ---

    Acts as an execution engine and integrates new programming paradigms. Key Stacks in this category are [Soda](/resources/stacks/soda/) and [Scanner](/resources/stacks/scanner/).

</div>


#### Data Movement and Processing

This category includes DataOS Resources that facilitate the movement and transformation of data.

##### **Batch Data**

These DataOS Resources support batch data processing, enabling scheduled, large-scale data transformations and movements.

<div class= "grid cards" markdown>

-   :resources-workflow:{ .lg .middle } [**Workflow**](/resources/workflow/)

    ---
    Manages batch data processing tasks with dependencies.

-   :resources-operator:{ .lg .middle } [**Operator**](/resources/operator/)

    ---

    Standardizes orchestration of external resources, enabling programmatic actions from DataOS interfaces.
    

-   :resources-stack:{ .lg .middle } [**Stacks**](/resources/stacks/)

    ---

    Key Stacks in this category are [Flare](/resources/stacks/flare/), [DBT](/resources/stacks/dbt/)
</div>



##### **Streaming Data**

These DataOS Resources are designed for stream data processing, handling real-time data flows and continuous data ingestion.

<div class= "grid cards" markdown>

-   :resources-workflow:{ .lg .middle } [**Workflow**](/resources/workflow/)

    ---
    Manages stream data processing tasks by running them as micro-batches.

-   :resources-service:{ .lg .middle } [**Service**](/resources/service/)

    ---

    Represents a long-running process that acts as a receiver and/or provider of APIs.
    
-   :resources-worker:{ .lg .middle } [**Worker**](/resources/worker/)

    ---

    Represents a long-running process responsible for performing specific tasks or computations indefinitely.

-   :resources-stack:{ .lg .middle } [**Stacks**](/resources/stacks/)

    ---

    Key Stacks in this category are [Flare](/resources/stacks/flare/) and [Bento](/resources/stacks/bento/).

</div>


#### Storage


This category includes DataOS Resources for providing efficient & scalable data storage.

<div class= "grid cards" markdown>

-   :resources-volume:{ .lg .middle } [**Volume**](/resources/volume/)

    ---
    Provides persistent shared storage for Pod containers.

-   :resources-lakehouse:{ .lg .middle } [**Lakehouse**](/resources/lakehouse/)
    
    ---

    A fully managed storage architecture that blends the strengths of data lakes and data warehouses.

-    :resources-database:{ .lg .middle } [**Database**](/resources/database/)

    ---

    Acts as a repository for storing transaction data, utilizing a managed Postgres relational database.

-   :resources-stack:{ .lg .middle } [**Stacks**](/resources/stacks/)

    ---

    Key Stack in this category is [Beacon](/resources/stacks/beacon/).
</div>

#### Observability

These key DataOS Resources are essential for tracking system performance and managing alerts, providing visibility into the health and status of the data infrastructure.

<div class= "grid cards" markdown>

-   :resources-monitor:{ .lg .middle } [**Monitor**](/resources/monitor/)

    ---
    Ensures system reliability and performance through observability and incident management.

-   :resources-pager:{ .lg .middle } [**Pager**](/resources/pager/)

    ---

    Enables developers to define criteria for identifying incidents from a stream, delivering alerts based on specified conditions.
</div>

#### Security

These DataOS Resources ensure data security and access control, managing sensitive information and enforcing policies for data protection.

<div class= "grid cards" markdown>

-   :resources-instancesecret:{ .lg .middle } [**Instance-Secret**](/resources/instance_secret/)

    ---
    Designed for securely storing sensitive information at the DataOS instance level, reducing exposure risks in application code or manifest files.

-   :resources-secret:{ .lg .middle } [**Secret**](/resources/secret/)

    ---

    Designed for secure storage of sensitive information like passwords, certificates, tokens, or keys within a DataOS Workspace.
    
-   :resources-policy:{ .lg .middle } [**Policy**](/resources/policy/)

    ---

    Defines rules governing user/application behavior, enforced through Attribute-Based Access Control. 

-   :resources-worker:{ .lg .middle } [**Grant**](/resources/grant/)

    ---

    Links the Subject-Predicate-Object relationship to create access policies, granting specific system or data access.
</div>

#### Deployment

These DataOS Resources streamline the deployment process of data products, facilitate the packaging, distribution, and execution of applications and services.


<div class= "grid cards" markdown>

-   :resources-bundle:{ .lg .middle } [**Bundle**](/resources/bundle/)

    ---
    Standardizes the deployment of multiple Resources, data products, or applications in one operation.

-   :resources-stack:{ .lg .middle } [**Stacks**](/resources/stacks/)

    ---

    Key Stacks in this category are [Container](/resources/stacks/container/) and [SteamPipe](/resources/stacks/steampipe/).
</div>

#### Infrastructure Resources

This category includes DataOS Resources for managing computational power and infrastructure configurations, essential for running your analytics and data processing workloads. They ensure optimal performance and scalability of data processing environments.

<div class= "grid cards" markdown>

-   :resources-cluster:{ .lg .middle } [**Cluster**](/resources/cluster/)


    ---
    Provides the computational resources and configurations for data engineering and analytics tasks.

-   :resources-compute:{ .lg .middle } [**Compute**](/resources/compute/)

    ---

    Streamlines the allocation of processing power for data tasks, acting as an abstraction over node pools of similarly configured VMs.   
</div>

### **Learning Tracks**

Explore role-based learning tracks to master essential DataOS capabilities to create, manage and consume Data Products. These paths enable you to focus on the training and knowledge areas most relevant to your specific role. With practical insights, and step-by-step guidance, these learning tracks streamline your journey, empowering you to unlock the full potential of Data Products.

<div class= "grid cards" markdown>

-   :fontawesome-solid-user-tag:{ .lg .middle } **Data Product Consumer**

    ---

    [:octicons-arrow-right-24: Learn more](/learn/#data-product-consumer)


-   :fontawesome-solid-user-gear:{ .lg .middle } **Data Product Developer**

    ---

    [:octicons-arrow-right-24:  Learn more](/learn/#data-product-developer)

-   :fontawesome-solid-user-check:{ .lg .middle } **DataOS Operator**

    ---

    [:octicons-arrow-right-24: Learn more](/learn/#dataos-operator)

</div>


### **Learning Assets**

To further support your journey, the following sections in the documentation help you understand various aspects of DataOS, which are essential for building Data Products using DataOS.

<div class= "grid cards" markdown>

-   :material-network-pos:{ .lg .middle } **Glossary**

    ---

    [:octicons-arrow-right-24: Learn more](/glossary/)


-   :material-content-duplicate:{ .lg .middle } **Quick Start Guides**

    ---

    [:octicons-arrow-right-24:  Learn more](/quick_guides/)

-   :material-list-box-outline:{ .lg .middle } **Video Tutorials**

    ---

    [:octicons-arrow-right-24: Learn more](/videos/)

</div>
