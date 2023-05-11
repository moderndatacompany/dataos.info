# Glossary

This page is dedicated to giving you reference of the terms that we use as part of the DataOS product description. This will enable us to remain on the same page while we discuss several aspects of the product.

| Term | Definition | Category |
| --- | --- | --- |
| Alpha | Helps to deploy & connect with web-server-based application images developed on top of DataOS.  | Stack |
| Atlas | An in-built BI solutions tool that allows you to create visualizations, custom reports & dashboards. | App |
| Audiences | Native app to easily segment customers according to key variables, and get deeper insights into their behaviour and value. | App |
| Beacon | A service that allows your web & other applications access to PostgreSQL databases within DataOS. It can be used to perform CRUD operations, Search, Filtering & Renaming of data assets stored in Postgres. | Stack |
| Customer 360 | Native app to connect your customer data from any source and power your use cases. | App |
| Compute | These are groups of Virtual Machines registered with DataOS. By default, you get two compute resources with DataOS installation. One for runnable resource and the other for queries. | Primitive |
| CLI | DataOS CLI is our Command Line Terminal/Interface to enable you to interact with DataOS context. | Interface |
| Cluster | A cluster is a collection of computation resources and configurations on which you run your data engineering, data science, and analytics workloads. By default, DataOS installation, creates two types of clusters, one for data processing needs (Job cluster) and the other for query-related workload (Minerva cluster).  | Primitive |
| Data Toolbox | Supports additional functionality to manage datasets; such as, list metadata, update columns, get snapshots, etc. | Stack |
| DataOS Context | Refers to the entire DataOS platform environment. | DataOS Term |
| Database | We have Database present as a primitive/resource within DataOS. You can use it to syndicate structured data.  | Primitive |
| Depot | Depots can be understood as the central data repository. Data stored here can be accessed, explored, and processed. It also provides references to virtual locations where data from different silos and clouds is fetched and stored. | Primitive |
| Fastbase | DataOS provides a default stream storage to support real-time and pub-sub use cases with the help of <span style="color:green">apache pulsar</span>. We call it `fastbase`. In a way, it is just another depot | Storage |
| Flare | A declarative stack that has been built as an abstraction over Spark. It allows the user to carry out data transformation & build entire data pipelines by writing batch jobs. | Stack |
| Gateway | Gateway is a connection service that functions as an abstraction layer over Minerva Clusters. | Service |
| Heimdall | Heimdall is the authentication, authorization, and governance engine component of DataOS. It also acts as a vault for secrets.  | Component |
| Hera | Hera refers to the lineage capability within DataOS context.  | App |
| Icebase | DataOS provides a default table storage backed by iceberg table format on underlying blob storage(azure datalake/gcs/s3). We call it `icebase`. In a way, it is just another depot | Storage |
| Lens | A semantic-ontological layer which is capable of accessing & modelling data from disparate sources. It allows you to define a data contract which expresses a business concept via entities, measures & dimensions. |  |
| Metis | A centralized metadata repository to discover all the data assets within your organisation, and follow their evolution/change in real time. It is also our Data Catalog. | Component |
| Minerva | Query engine to process & analyse big data from a variety of heterogeneous data sources. It is built on top of Trino (Presto). | Component |
| Notebook | Allows you to create and share documents that contain live code, equations, visualizations, and narrative text for data science and analytic needs. | App |
| Observability | Includes both data observability & observability around DataOps. | Core pillar |
| Odin | Odin refers to knowledge graph in the DataOS context. | App |
| Ontology | A defined model that organizes structured and unstructured information through entities, their properties, and the way they relate to one another. [Ontology + Data = Knowledge Graph] | DataOS Term |
| Operations Center | Operation Center enables monitoring resources, users, and data operations (DataOps) in DataOS for the deployed components and applications. It helps you know what happens in data ingestion, processing, and storage during the operations and provides actionable insights for troubleshooting. | App |
| Policy | A DataOS Policy is a set of rules that help safeguard data and establish standards for its access, use, and integrity. | Primitive |
| Poros | Poros is our orchestration engine & resource manager. | Component |
| Primitives | In the DataOS context, primitives are the core components that frame the entire foundation structure of the DataOS platform. However, the platform is developed in such a way that it remains composable and can function with equal efficiency with or without some of the core components. | DataOS Term |
| Query Book |  | App |
| Scanner | Stack to enable Metadata registration & indexing in Metis. It captures schema details such as table names, constraints, primary keys, etc. Once done, you can view the scanned data assets in Metis, and then undertake processes such as transformations, quality checks, etc. | Stack |
| Service | Service allows you to collect, process and analyze a continuous flow of data (stream).A service has a port and a socket open to receive data.  | Primitive |
| Secret | This Resource helps you to store sensitive data such as passwords, token or keys which are required to access your data sources or use services. | Primitive |
| Security |  | Core Pillar |
| UDL | It is called Universal Data Link. As the name suggests, it is an address to access your data and can be used by you throughout the DataOS system. | DataOS Term |
| Workbench | A data exploration tool to write and run SQL queries. It is designed to be usable by both technical and business users. In other words, Workbench is our SQL editor that connects you to Minerva query engine. | App |
| Workflow | Workflow is a DAG(Directed Acyclic Graphs) of jobs. It is a way to define data pipelines(end-to-end) and run jobs in a hierarchical manner. | Primitive |
| Workspace | Workspace is to implement multi-tenant system that provides a way to segregate your private work from the rest of the organisation’s. | Primitive |