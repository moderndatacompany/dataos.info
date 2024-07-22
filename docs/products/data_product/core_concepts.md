# Core Concepts
## Key Facets of the Data Products

### **Input**

The input aspect of a Data Product encompasses the technical mechanisms responsible for data access and ingestion. These mechanisms include APIs, streaming services, connectors, and batch processes, all of which facilitate the acquisition of data from diverse sources. By ensuring seamless and reliable data flow into the system, these components play a crucial role in preparing data for subsequent processing and analysis.

### **Output**

The output aspect of a Data Product pertains to the results generated from data analysis and processing. This includes tables, streams, APIs, visualizations, and web applications delivered to data consumers. The outputs can be experiential or serve as programmatic interfaces to other Data Products, providing valuable insights and enabling further data-driven decision-making.

### **SLO**

SLOs (Service Level Objectives) define the targets for performance, availability, accessibility, and quality that a Data Product aims to achieve. These objectives ensure that the Data Product adheres to the required service levels concerning quality and governance. SLOs may encompass metrics based on business data, metadata, and operational data. By monitoring and managing these SLOs, it is possible to ensure that the Data Product performs optimally and meets the expectations of its consumers.

### **Governance**

Governance includes robust access controls to manage permissions at various levels, such as tables, rows, columns, and other relevant dimensions. This involves setting and enforcing policies that regulate data access, usage, and handling, ensuring data integrity, privacy, and security throughout the data product's lifecycle. Additionally, governance encompasses auditing, monitoring, and compliance reporting to maintain transparency and accountability in data management practices.

### **Transformation**

The transformation aspect of a Data Product involves processing and manipulating data within the product. This may include data cleansing, enrichment, aggregation, normalization, or other necessary transformations. These processes ensure that the data is valuable for analysis and consumption, meeting the desired format, structure, and quality standards.

### **Observability**

Observability in data products involves systematically monitoring their health and performance to ensure continuous operation and enhance data reliability. This includes proactively tracking key metrics such as data availability, latency, and throughput, as well as detecting and alerting on anomalies or deviations from expected behaviors.
Data profiling is a crucial component of observability, enabling a thorough examination, analysis, and summarization of data characteristics. This process helps identify and understand the structure, quality, and patterns within datasets. By profiling data, organizations gain insights into data distribution, completeness, and consistency, which are essential for ensuring data reliability and suitability for use.

## Characteristics of the Data Products
The core principles of Data Products guide their design and development, ensuring they meet business goals, maintain high quality, and are user-centric. Here are the key principles:

### **Discoverable**

A Data Product is designed to be easily discovered by users. It includes appropriate metadata, tags, and descriptions, enabling users to find and understand its purpose and contents quickly.

### **Addressable**

A Data Product is assigned a unique identifier, making it easily referencable and accessible within a data ecosystem. This ensures that users can reliably access and work with the data product without ambiguity.

### **Understandable**

A Data Product is presented in a manner that is easily understandable to users. It employs clear and intuitive visualizations, documentation, and explanations, facilitating users' understanding of the data and its implications.

### **Natively Accessible**

A Data Product is made available in its native format, ensuring seamless integration with different tools and systems commonly used by data consumers. This eliminates the need for complex conversions or transformations, allowing for direct access and utilization.

### **Trustworthy and Truthful**

A Data Product adheres to rigorous quality assurance processes and data governance principles. It ensures that the data is accurate, reliable, and transparently sourced, instilling trust and confidence in the insights or outputs it provides.

### **Interoperable and Composable**

A Data Product is designed to integrate and interact with other Data Products and systems seamlessly. It follows standardized protocols and interfaces, enabling interoperability and composability, thus allowing users to combine and leverage multiple data products for comprehensive analysis.

### **Valuable on Its Own**

A Data Product provides users with intrinsic value without further processing or integration. It delivers meaningful insights, actionable information, or standalone functionalities that can be used to support decision-making and drive desired outcomes.

### **Secure**

A Data Product incorporates robust security measures to protect the data's confidentiality, integrity, and availability. It implements access controls, encryption mechanisms, and privacy safeguards, ensuring the data is safeguarded from unauthorized access or breaches.

### **Purpose Driven**

A Data Product have a clear purpose and be aligned with specific business objectives. It is designed to solve particular problems or provide distinct value to its users, ensuring that its development and deployment are goal-oriented and impactful.

### **Responsive**

A Data Product is responsive to user needs and environmental changes. It has mechanisms for receiving feedback, adapting to new requirements, and evolving based on user interactions and external factors, ensuring it remains relevant and useful over time.

### **Reactive**

A Data Product is capable of reacting to real-time data and events. It is designed to process and respond to new information dynamically, allowing users to make timely decisions based on the most current data available.

## Data Product Persona

In the realm of Data Products, understanding the different personas is crucial for crafting an effective Data Product. These personas represent the various stakeholders who interact with the data product throughout its lifecycle. Each persona has unique requirements, goals, and perspectives, which should be addressed in the Data Product development to ensure that it is useful and accessible to everyone involved. Here, we outline the primary personas typically associated with Data Products.

### **Data Product Owner**

Data Product Owners are responsible for defining the strategic direction and success metrics of the Data Product. They prioritize features, manage stakeholder expectations, and ensure alignment with business goals through clear roadmaps and effective communication. Within the Data Product Owner role, various divisions include strategic leaders who define the vision and goals, stakeholders who prioritize requirements and outline development milestones, and business analysts who analyze market trends and user feedback.

### **Data Product Developer**

Data Product Developers designs, builds, and maintains the technical infrastructure of the Data Product. They implement data pipelines, ensure data quality and security, observe and optimize performance. Collaboration with other teams ensures that the product meets technical requirements and integrates seamlessly. As for the Data Product Developer, roles include data engineers who design and implement pipelines, software developers who create functionality and interfaces, database administrators who manage data storage, and DevOps engineers who automate deployment processes.

### **Data Product Consumer**

Data Product Cosumers utilizes the Data Product to derive insights and make data-driven decisions. They explore output data, generate reports, and leverage visualizations for strategic planning and operational improvements. For Data Product Consumers, divisions encompass business analysts who derive insights, operational managers who optimize processes, executive stakeholders who rely on strategic insights, and data scientists, and data analysts who use advanced analytics and models. Data consumers utilize the Data Product Hub to explore and obtain the Data products that align with their business requirements. They can review descriptions of the Data Products to determine suitability. Through an intuitive interface, data consumers can efficiently access the appropriate data they need.

## Types of Data Product

Data Products can be categorized based on their design and structure. The main types are described below:

### **Entity First Data Product**

Entity-first Data Products are organized and structured based on the characteristics and origins of the underlying data sources themselves. There is emphasis on ensuring data quality, governance, and compliance with organizational standards and policies.​ They often aligning closely with the data domains of the organization.​ At times, they are also referred to as Source-aligned Data Products. Examples include Data Warehouses, which centralize and integrate data across an organization, and Master Data Management Systems, which ensure consistency and accuracy of key data entities like customers or products.

### **Model First Data Product**

Model-first Data Products are designed and structured primarily around the needs, preferences, and use cases of the end-users or consumers of the data. There is emphasis on understanding the semantics and context in which users will interact with the data.​This essentially means modeling the outcome first (prototyping) and then putting the parts together to bring the product vision to life. ​At times, they are also referred to as Consumer-aligned Data Products.​ Examples include Business Intelligence Dashboards that provide visual analytics for decision-making, Predictive Analytics Models that forecast future trends based on historical data, and Recommendation Systems that suggest items based on user behavior and preferences.
