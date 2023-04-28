# Core Concepts of DataOS [Overview]
## What is DataOS?
## DataOS Capabilities

One Platform for all your data activities  

Data Management 

The DataOS seamlessly connects to all your source and sink systems and transform and curate data with our model-based low-code declarative artifacts. ACID-compliant data lake enables teams to store structured, unstructured and streaming data. Out-of-the-box data quality and profiling functionality lets you get quality and trusted data without additional processing. Leverage our observability principles to create robust alerts across the data lifecycle.  

Data Exploration - 

DataOS’s Datanet creates a connective tissue between all your data systems continuously adding usage-based intelligence to your data. Easily Discover, search and find trusted and context-aware data. Understand the journey, relationships and impact of your datasets and make decisions with confidence. DataOS also has powerful workbench that lets you query datasets with simple SQL queries.   

Data Activation 

Activate your data and share it across your enterprise. DataOS lets you create customized reports on any datasets in minutes, share and collaborate on them securely. Build trigger alerts and notifications to 10+ destinations including ServiceNow, Jira, Pager Duty, Slack, MS teams etc. Consume your shared data from SaaS systems like salesforce, zendesk, google ads etc 

Data Products 

Build and launch new data products faster.  DataOS handles all the infrastructure needed  - Run,host,store,process,sync,serve  to build your data application so teams can focus on innvoation. 

Governance & Security 

DataOS’s Tag-based governance enables flexible and granular policy creation that gives teams an automated and scalable way to ensure governance and compliance for data within your ecosystem. Attribute-based access control future-proofs your org and lets it adapts to changing and new compliance regulations. Easy-to-create access and Data policies let you control, track and audit access to data. Row-level filtering and column masking give you granular control of what data authenticated users can access. Advanced primitives like data masking, data abstraction and differential privacy ensure your teams are working with trusted data at all times.  

Data Sharing 

Share data easily across your business ecosystem without copying or moving data. DataOS’s best in class governance enables you to control access in a secured and auditable environment. Share data and collaborate with customers, internal and external partners to unlock newer and richer insights. 

Data Modeling 

DataOS’s foundational MML(Map-Model) architecture brings a declarative model-first approach to pipeline creation. It abstracts away the complexity of pipeline building.  MML makes it easy to build and manage data pipelines helping data engineering teams to streamline and simplify their ETL processes.  



## High-level conceptual working
The general activities involved with big data processing with DataOS:
1. Ingesting data into the system
2. Persisting the data in storage
3. Computing and analyzing data
4. Visualizing the results
5. Sharing and collaboration
## DataOS components [Overview]
### Depots
Depot is  a  resource type and core primitive within the dataOS ecosystem. Depot provides a reference to the Data source/sink and abstracts the details of their configurations and storage formats. It helps you to easily understand the data source/sink and connect with it. You can use these Depots for accessing, processing and exploring data within DataOS.

Depot contains the data location information along with any credentials and secrets that are required to access data from an external source. Once the Depot is created, you can use it in your Flare jobs, services and in other tools within the DataOS system.


### Datanet
DataOS’s Datanet creates a connective tissue between all your data systems continuously adding usage-based intelligence to your data. You can get a holistic view of all the data and understand the journey, relationships and impact of your datasets. You can easily search and find trusted and context-aware data. 

Datanet application consists of majorly five components -

- Search

- Fabric

- Policies

- Depots

- Tag Manager

Search 
this component helps us to search across different entities like- dataset, job, workflow, service, function, query, dashboard etc. This search page is built using Elasticsearch. Elasticsearch is a search engine based on the Lucene library. It provides a distributed, multitenant-capable full-text search engine with an HTTP web interface and schema-free JSON documents. It gives us the ability to filter out the result as well facets based on the search criteria. The user also has the option to navigate the respective detail page.

Fabric
Fabric component provides the capability to search among different nodes like- job, dataset, depot, workflow, service, function, query and dashboard. It is a graphical representation of a search page. It also helps us to know the relationship among different nodes. We can also get primary information related to the node. Fabric component provides the capability to search among different nodes like- job, dataset, depot, workflow, service, function, query and dashboard. It is a graphical representation of a search page. It also helps us to know the relationship among different nodes. We can also get primary information related to the node. G6 graph library is used to build this component.

Policies
This component contains two things

Access Policy 
Access policy helps to identify the list of access level policies that are available in the system. We can get the info about which policy tags have what level of access with respect to the subject and predicates.

Mask Policies 
These policies are global policies available in the system which contains all the column level policy. This will helps to get the info about applied tags, priority and masking strategy.

Depots
This component shows the list of depots available in the system. This shows high level info about a depot like- name, type, description, catalog etc.

Tag Manager
This component displays list of tags available in the system. We have the functionality to create a new tag and also we can update an existing tag also in the system.
#### Catalog
#### Dataset
#### Schema/tables
#### Dictionary

### Linage
You need to know the origin of data you are handling or interpreting.
### Impact
Engineering teams in yoiur organization depend on this information to analyse the impact of change
on all downstream processes and products and choose the appropriate strategy for implementing the change.

## Measures

## Fingerprinting
Metrics and Checks
Flare
Minerva
Workbench
Atlas
Basic Concepts and Terminology [Overview]
AI
Machine Learning
Fingerprinting
Data Profiling
Cluster Computing
Stream Data vs Batch Data
Data Pipelines
Data Ingestion/Exploration
ELT vs ETL
Data Lake vs Data Warehouse
Data Sources


A dataset in DataOS is a structured collection of data that you import or connect to. These datasets can be created while ingesting stream or batch data into DataOS. You can also create new datasets by joining existing datasets. You use these datasets while crteating reports and dashboards or doing descriptive analysis. 