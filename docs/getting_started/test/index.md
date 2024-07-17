# Testing


### **Understand DataOS Resources**

In this section, DataOS Resources are categorized to align with traditional data processing and management practices, helping you understand their capabilities.

#### **Source Connectivity and Metadata management**

This category includes DataOS Resources that facilitate the connection to various data sources and manage the associated metadata, ensuring seamless data integration and organization.

<div class= "grid cards" markdown>

-   :resources-depot:{ .lg .middle } [**Depot**](/resources/depot/)

    ---
    To connect various data sources to DataOS, abstracting underlying complexities.   


-   :resources-stack:{ .lg .middle } [**Stacks**](/resources/stacks/)

    ---

    Acts as an execution engine and integrates new programming paradigms. Key Stacks in this category are [Soda](/resources/stacks/soda/) and [Scanner](/resources/stacks/scanner/).

</div>


#### **Data Movement and Processing**

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

    Key Stacks in this category are [Flare](/resources/stacks/flare/), [DBT](/resources/stacks/dbt/), [Data Toolbox](/resources/stacks/data_toolbox/) and [CLI Stack](/resources/stacks/cli_stack/).

</div>



##### **Stream Data**

These DataOS Resources are designed for stream data processing, handling real-time data flows and continuous data ingestion.

<div class= "grid cards" markdown>

-   :resources-workflow:{ .lg .middle } [**Workflow**](/resources/workflow/)

    ---
    Manages stream data processing tasks by running them as micro batches.

-   :resources-service:{ .lg .middle } [**Service**](/resources/service/)

    ---

    Represents a long-running process that acts as a receiver and/or provider of APIs.
    
-   :resources-worker:{ .lg .middle } [**Worker**](/resources/worker/)

    ---

    Represents a long-running process responsible for performing specific tasks or computations indefinitely.

-   :resources-stack:{ .lg .middle } [**Stacks**](/resources/stacks/)

    ---

    Key Stacks in this category are [Flare](/resources/stacks/flare/) and [Benthos](/resources/stacks/benthos/).

</div>


#### **Storage**


This category includes DataOS Resources for providing robust, persistent and scalable data storage to store data efficiently and securely.

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

#### **Observability**

These key DataOS Resources are essential for tracking system performance and managing alerts, providing visibility into the health and status of the data infrastructure.

<div class= "grid cards" markdown>

-   :resources-monitor:{ .lg .middle } [**Monitor**](/resources/monitor/)

    ---
    Ensures system reliability and performance through observability and incident management.

-   :resources-pager:{ .lg .middle } [**Pager**](/resources/pager/)

    ---

    Enables developers to define criteria for identifying incidents from a stream, delivering alerts based on specified conditions.
</div>

#### **Security**

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

#### **Deployement**

These DataOS Resources streamline the deployment process of data products, facilitating the packaging, distribution, and execution of applications and services


<div class= "grid cards" markdown>

-   :resources-bundle:{ .lg .middle } [**Bundle**](/resources/bundle/)

    ---
    Standardizes the deployment of multiple Resources, data products, or applications in one operation.

-   :resources-stack:{ .lg .middle } [**Stacks**](/resources/stacks/)

    ---

    Key Stacks in this category are [Container](/resources/stacks/container/) and [SteamPipe](/resources/stacks/steampipe/).
</div>

#### **Infrastructure Resources**

This category includes DataOS Resources for managing computational power and infrastructure configurations, essential for running your analytics and data processing workloads. They ensure optimal performance and scalability of data processing environments.

<div class= "grid cards" markdown>

-   :resources-cluster:{ .lg .middle } [**Cluster**](/resources/cluster/)


    ---
    Provides the computational resources and configurations for data engineering and analytics tasks.

-   :resources-compute:{ .lg .middle } [**Compute**](/resources/compute/)

    ---

    Streamlines the allocation of processing power for data tasks, acting as an abstraction over node pools of similarly configured VMs.   
</div>