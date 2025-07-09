# Introduction to DataOS

!!! info "Overview"
    This topic introduces DataOS, a data product platform that transforms how organizations work with data. You will learn about its key components that enable technical and business users to turn raw data into powerful, governed, and production-ready data assets.

DataOS is an enterprise-grade data product platform that enables organizations to build, manage, and share data products. It provides the essential building blocks data developers require to create powerful data products that drive significant business outcomes.

## Key Benefits

DataOS empowers organizations to build faster, collaborate smarter, and scale confidently. It provides a modular, composable, and interoperable data infrastructure built on open standards, making it extensible and flexible for integration with existing tools and infrastructure.

- **Modularity**: Facilitates flexible integration and scalability, allowing components to be independently developed, deployed, and managed.

- **Composability**: Enables building complex data workflows from simple, reusable components.

- **Interoperability**: Ensures seamless interaction with various data tools and platforms.

- **Governance and Security**: Provides robust access controls and compliance features, ensuring data integrity and adherence to regulatory standards.

- **Self-Service Enablement**: Empowers users, including data analysts and business stakeholders, to independently discover, access, and utilize data products through intuitive interfaces such as the Data Product Hub and Lens Studio. This reduces reliance on IT teams and accelerates time-to-insight.

## Developing Data Products with DataOS

The development of a data product in **DataOS** follows a structured lifecycle:

1. **Design**: Define business goals and translate them into a solution architecture.

2. **Develop**: Build and test the data product based on the design.

3. **Deploy**: Release the product to users and ensure it operates effectively in a production environment.

4. **Iterate**: Continuously improve the product through feedback and performance analysis.

## Key Components in Data Product Development

### **Depots**  
Serve as data connectors between external systems and DataOS without requiring data movement. Depots enable secure and consistent access to raw data while maintaining it in place, enhancing both efficiency and governance. :contentReference[oaicite:1]{index=1}

---

### **Stacks**

Stacks acts as an execution engine and integrates new programming paradigms. Key Stacks in this category are Flare, Bento, Soda and Scanner.  

**Flare**: DataOS’s declarative engine built atop Apache Spark, designed for scalable batch and streaming data processing. 
Flare supports various job types:

- **Batch jobs** for full-data loads  
- **Incremental jobs** for efficient updates  
- **Streaming jobs** for real-time processing  

**Bento:** DataOS’s lightweight, stateless engine designed for real-time stream processing. It utilizes a declarative YAML-based configuration, enabling efficient data transformations such as mapping, validation, filtering, and enrichment. Bento is ideal for scenarios requiring low-latency processing, like IoT data ingestion or real-time analytics.

Supported Job Types:

- **Streaming Jobs** for continuous processing of real-time data streams.

**Soda**:  Data quality validation Stack for implementing data quality checks within and beyond data pipelines. Utilizing the Soda Checks Language (SodaCL), it allows users to define validation rules to monitor metrics like accuracy, completeness, and uniqueness. 

Supported Job Types:

- **Batch Jobs** for scheduled data quality checks on datasets.

- **Continuous Monitoring** for ongoing validation processes for real-time data quality assurance.

**Scanner:** DataOS’s stack designed for extracting metadata from external source systems and internal DataOS resources. It facilitates the discovery and understanding of data assets by collecting metadata such as schemas, column details, and data lineage. Scanner supports metadata ingestion from databases, dashboards, messaging services, and more.

Supported Job Types:

**Batch Jobs** for scheduled metadata extraction tasks.

**Reactive Jobs** for event-driven metadata updates based on resource lifecycle events.

---

### **Lens**  
The semantic modeling layer that translates technical data into business-friendly terms. Lens empowers users to define and expose metrics, dimensions, and business logic, making data consumable for BI tools, APIs, or direct consumers.

---

### **Monitors & Pagers**
Tools to track data quality, pipelines, and system health.

- **Monitors** observe performance, quality, and SLA compliance.

- **Pagers** trigger alerts and incident management workflows to quickly address failures 

---

### **Policies**

DataOS enables Attribute‑Based Access Control (ABAC)—tagging tables, rows, or columns with access rules and automatically enforcing them across all access channels (API, BI, queries, etc.). Data policies in DataOS help ensure that sensitive data is accessed only by the right users, keeping it secure and compliant across the entire ecosystem.

---

### **Bundles**  
A declarative packaging mechanism for deploying and managing entire data products. Bundles encapsulate Depots, Flare jobs, Lens models, and pipelines into a single deployable unit—ensuring consistency, version control, and testability within CI/CD workflows.

To learn more about all the Resources, refer to [DataOS Resources](/resources/)

---

## Governance, Security, and Observability

### **Governance and Security**
DataOS incorporates robust security measures to protect data confidentiality, integrity, and availability. It implements access controls, encryption mechanisms, and privacy safeguards, ensuring data is safeguarded from unauthorized access or breaches .
dataos.info

### **Observability**
Observability in DataOS involves systematically monitoring the health and performance of data products to ensure continuous operation and enhance data reliability. This includes tracking key metrics such as data availability, latency, and throughput, as well as detecting and alerting on anomalies.
