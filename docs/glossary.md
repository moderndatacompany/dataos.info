---
hide:
  - navigation
#   - toc
---
  [a](./glossary.md#a) &nbsp;&nbsp;   [b](./glossary.md#b) &nbsp;&nbsp;    [c](./glossary.md#c)  &nbsp;&nbsp;     [d](./glossary.md#d) &nbsp;&nbsp;    [e](./glossary.md#e) &nbsp;&nbsp;   [f](./glossary.md#f) &nbsp;&nbsp;    [g](./glossary.md#g)  &nbsp;&nbsp;   [h](./glossary.md#h) &nbsp;&nbsp;    [i](./glossary.md#i) &nbsp;&nbsp;     [j](./glossary.md#j) &nbsp;&nbsp;    [k](./glossary.md#k) &nbsp;&nbsp;     [l](./glossary.md#l) &nbsp;&nbsp;     [m](./glossary.md#m) &nbsp;&nbsp;     [n](./glossary.md#n) &nbsp;&nbsp;    [o](./glossary.md#o) &nbsp;&nbsp;    [p](./glossary.md#p) &nbsp;&nbsp;     [q](./glossary.md#q) &nbsp;&nbsp;     [r](./glossary.md#r) &nbsp;&nbsp;     [s](./glossary.md#s) &nbsp;&nbsp;    [t](./glossary.md#t) &nbsp;&nbsp;     [u](./glossary.md#u) &nbsp;&nbsp;    [v](./glossary.md#v) &nbsp;&nbsp;     [w](./glossary.md#w) &nbsp;&nbsp;     [x](./glossary.md#x) &nbsp;&nbsp;     [y](./glossary.md#y) &nbsp;&nbsp;     [z](./glossary.md#z) 
---

# a

| Term | Description |
| --- | --- |
| [Access Policy](./resources/policy.md#access-policy) | An access policy in DataOS serves as a regulatory mechanism that governs user authorizations by defining rules for granting or denying access to specific actions. These policies determine whether a user, referred to as the subject, is authorized to perform a particular action, known as the predicate, on a given dataset, API path, or other resources, referred to as objects. Read about [Bifrost](interfaces/bifrost.md) to establish access control via a Graphical User Interface.  |
| [Airbyte](/resources/depot/list_of_connectors/) | Airbyte is a modern ELT data pipeline tool that streamlines data integration and replication by efficiently collecting data from diverse sources and making it available for analysis and storage. DataOS seamlessly integrates with Airbyte and provides a graphical user interface to enable access to Airbyte connectors. This integration empowers users to leverage Airbyte's functionalities effortlessly within the DataOS ecosystem. |
| [Alerts](/interfaces/atlas/#set-up-alerts) | DataOS allows you to monitor & setup alerts at different stages of the data product journey. For example, you can setup Metrics Alerts in DataOS to serve a notification that informs you when a specific field returned by a query meets a predefined threshold or set of criteria; you can setup Workflow Alerts to get notified of breaks in the data pipelines; you can also setup alerts for quality checks, data changes, and a lot more. |
| [Assertions]() | Assertions are custom validation rules tailored to a specific business domain. They are essential in evaluating the suitability of datasets for their intended purpose. By implementing assertions, datasets can undergo additional validation checks, leading to enhanced data quality.  |
| [Atlas](./interfaces/atlas.md) | A built-in business intelligence (BI) tool that enables you to generate visualizations, and create interactive dashboards. |
| [Audiences](./interfaces/audiences.md) | It is an application derived from Lens that uses the semantic data models created through Lens to identify and categorize specific groups of people who have similar characteristics, traits, or behaviors. These categorized groups are referred to as audiences. |
| [Authorization Atoms](./interfaces/bifrost.md) | Each predicate and object in an Access Policy is an Authorization Atom. This allows us to use them in a composable manner to create modular use cases or policies. |


# b

| Term | Description |
| --- | --- |
| [Beacon](./resources/stacks/beacon.md) | Beacon is a stack in DataOS that facilitates connections between web and other applications with PostgreSQL databases. It enables essential operations such as CRUD operations, data searching, filtering, and renaming.|
| [Benthos](./resources/stacks/benthos.md) | Benthos is a robust and efficient stream processing stack within DataOS. It offers a user-friendly declarative YAML programming approach, enabling seamless execution of essential data engineering tasks like data transformation, mapping, schema validation, filtering, and enrichment.|
| [Bifrost](./interfaces/bifrost.md) | Bifrost is a Graphical User Interface (GUI) that empowers users to effortlessly create and manage access policies for applications, services, people, and datasets. Bifrost leverages the governance engine of DataOS, Heimdall, to ensure secure and compliant data access through ABAC policies, giving users fine-grained control over the data and resources.|
| [Bloblang](./resources/stacks/benthos/bloblang.md) | Benthos incorporates Bloblang, a built-in mapping language designed to extract, modify, and restructure data in formats like JSON, CSV, and XML. Bloblang is used in data integration and processing pipelines to perform tasks like data mapping, filtering, and conversion. With Bloblang, users can efficiently manipulate and transform data within Benthos, enhancing their data processing capabilities.  |


# c 
| Term | Description |
| --- | --- |
| [Caretaker](/architecture/#caretaker) | Caretaker is a component within DataOS that captures, stores, and provides information related to pods, including their states and aggregates. It maintains historical data in blob storage while serving real-time information about running pods through the Operations app. |
| [CLI](./interfaces/cli.md) | Command Line Interface is  a text-based interface to interact with the DataOS context. It offers quick access to system functionality with flexibility and control making it ideal for data engineers or system administrators. |
| [Cloud Kernel](/architecture/#cloud-kernel)  | Cloud Kernel is an abstraction layer over the cloud APIs of cloud providers like AWS, GCP & Azure that facilitates interactions with cloud-based services and resources. It makes DataOS cloud-agnostic. |
| Collection | The collection represents a logical container that holds related data entities, and it plays a key role in establishing the data hierarchy. Once a mapping is established between a depot and a collection, it generates a Uniform Data Link (UDL) that can be utilized throughout DataOS to access the dataset. |
| Context | DataOS Context refers to the environment or instance where DataOS is deployed and operates.   |
| [Core Kernel](/architecture/#core-kernel) | Core Kernel serves as the traditional operating system kernel, responsible for OS functionalities that are independent of cloud-specific features. It incorporates drivers to enable communications between services, enforces access controls for both ingress & egress, and manages creation, scheduling & termination of various DataOS Resources & applications.   |


# d 

| Term | Description |
| --- | --- |
| Data Developer | Data developer in DataOS, specializes in designing, building, and maintaining data-centric applications and systems. They work with data infrastructure, data sources, and data pipelines to enable efficient data processing and analysis. |
| [Data Policy](./resources/policy.md#data-policy) | Data Policy serves as an additional layer of control in regulating the visibility and interaction with specific data after access has been granted. It employs techniques like data masking or filtering to  restrict the visibility of sensitive or restricted data based on predefined rules or conditions. By enforcing these policies, organizations can ensure data privacy and regulatory compliance, minimizing the risk of unauthorized access to sensitive information. |
| [Data Toolbox](./resources/stacks/data_toolbox.md) | The Data Toolbox Stack is used to update metadata for the data that is ingested into Icebase using Flare Stack. The metadata of the ingested datasets needs to be registered with Metis before it can be queried using Workbench.|
| [Depot](./resources/depot.md) | Depot is a Dataos Resource that simplifies connectivity to different data sources by abstracting the complexities of the underlying systems.  Depots handle protocols, credentials, and connection schemas, making it easier for users to access and utilize data from diverse sources, including file systems, data lake systems, database systems, and event systems |
| Dropzone | Dropzone is a depot in DataOS referring to an object storage. This storage is used as data lake to easily and securely upload files. |


# e 

| Term | Description |
| --- | --- |
| Egress | In DataOS, egress refers to the process of transferring data from a particular system or network to an external system or network. Egress can occur when data is retrieved, exported, or transmitted from DataOS to another system, allowing data to be utilized outside of the DataOS ecosystem. |


# f 

| Term | Description |
| --- | --- |
| [Flare](./resources/stacks/flare.md) | Flare stack is used for building end-to-end data pipelines within DataOS. It uses a YAML-based declarative programming paradigm built as an abstraction over Apache Spark. It offers an all-in-one solution for performing diverse data ingestion, transformation, enrichment, and syndication processes on batch and streaming data. |
| [Fastbase](./resources/depot/fastbase.md) | Fastbase is a managed depot type in DataOS specifically designed to support Apache Pulsar format for streaming workloads. With Fastbase depots, users can seamlessly leverage the power of streaming and real-time data processing within the DataOS ecosystem. |
| Filebase | It is a depot that is configured during the DataOS installation and serves as a destination for storing various types of data in file formats like parquet, csv, pdfs, and more. |

# g 

| Term | Description |
| --- | --- |
| Grafana | Grafana is a powerful tool that allows the creation of  dashboards and provides capabilities for querying, visualizing, and exploring metrics, logs, and traces within the DataOS environment. It empowers administrators to effectively assess health of Kubernetes clusters. |
| [GUI](./interfaces.md#graphical-user-interface-gui) | The Graphical User Interface (GUI) in DataOS provides a user-friendly and visually appealing interface for interacting with DataOS and its components. |


# h 

| Term | Description |
| --- | --- |
| Hera| Hera is a source of record for lineage and topology that collates metadata from multiple sources, schedulers and/or data processing frameworks as long as the necessary integration is in place. It can receive lieneage information from workflow orchestration engine like Argo or Airflow, or a Jupyter notebook. |
| [Heimdall](./architecture/heimdall_arch.md) | Heimdall is the authentication, authorization, and governance engine in DataOS, responsible for implementing a robust security strategy. It ensures that only authorized users have access to DataOS resources. |


# i

| Term | Description |
| --- | --- |
| [Icebase](./resources/depot/icebase.md) | Icebase is a depot in DataOS that utilizes the Apache Iceberg table format. It seamlessly integrates with popular object storage systems like Azure Data Lake, Google Cloud Storage, and Amazon S3, following the Lakehouse pattern. Icebase offers a powerful OLAP (Online Analytical Processing) system that simplifies access to data lakes.|
| Indexer | It is a continuous running service within the DataOS environment that keeps track of newly created or updated datasets/topics/pipelines(workflows). With the information about the changed entity, a reconciliation Scanner YAML is created with filters to scan the metadata of the affected entity. |
| [Ingress](./interfaces/operations.md#ingresses) | Ingress in DataOS exposes HTTP and HTTPS routes from outside the DataOS context to services within a DataOS context. It configures the incoming port for the service to allow access to DataOS resources from external links. |
| [Interface](/interfaces/) | Interfaces in DataOS such as CLI, GUI, API provide points of communication and interaction between different components for efficient data operations,  and control over various activities. Interfaces enable self-service data management.  |


# j 

| Term | Description |
| --- | --- |
| Jupyter Notebook | Jupyter Notebook is an interface that enables interactive computing and data analysis. DataOS is configured to leverage the Jupyter ecosystem. This integration allows users to seamlessly utilize Jupyter Notebook within the DataOS environment, empowering them to explore and analyze data. |


# k 
| Term | Description |
| --- | --- |
| kubectl | In DataOS, kubectl provides a powerful interface for administrators and developers to interact with the underlying Kubernetes infrastructure of DataOS, enabling efficient management and operation of containerized applications and services. It allows to manage and control various aspects of the DataOS environment, such as deploying and scaling applications, inspecting cluster resources, accessing logs, etc.|


# l 

| Term | Description |
| --- | --- |
| [Lens](./interfaces/lens.md) | It is a modeling layer capable of accessing and modeling data from disparate sources. It supports data-driven decision-making by supporting and connecting to underlying data to the real-world business objects, formulates and delineate measure, KPIs, and relationships between different business concepts. |
| [Lens Explorer](/interfaces/lens/#lens-explorer) | Lens Explorer is an intuitive graphical user interface that allows users to discover and analyze data within the Ontology layer. Users can utilize Lens Explorer to query the semantic model(lens) and obtain answers to complex data questions in an exploratory manner.|

# m 

| Term | Description |
| --- | --- |
| [Metis](./architecture/metis_arch.md) | Metis is a metadata manager, cataloging service, and database within the DataOS environment assissting with discoverability and observability capabilities for your enterprise data. |
| [Minerva](./architecture/minerva_arch.md) | Minerva is a query engine that enables access to data for business insights. It is an interactive query engine based on Trino that makes it easy to analyze big data using SQL. |


# n 
| Term | Description |
| --- | --- |
| Network Gateway | In DataOS, a Network Gateway is a component that enables secure communication and connectivity between different networks or systems within the DataOS infrastructure. It serves as a bridge or interface that facilitates the exchange of data and information between networks while enforcing security measures such as access control and data encryption.  |
| Node Pool | A Node pool refers to a groups of virtual machines (VMs) with similar configurations (CPU, RAM, Storage Capacity, Network Protocal, and Storage Drive Types). Nodepools are made available to DataOS as a Compute Resource.  |



# o 

| Term | Description |
| --- | --- |
| Odin | DataOS Odin is a comprehensive knowledge graph that incorporates a semantic network of entities and their relationships within a system. It offers a queryable interface supporting SQL and Cypher query languages, allowing users discover data and surface underlying connections between data points. |
| OpenID | OpenID Connect is an identity layer built on top of the OAuth protocol, providing a streamlined mechanism for Clients to verify the identity of End-Users. It utilizes an Authorization Server to authenticate the user and retrieve basic profile information through exposed REST APIs. In DataOS, Heimdall leverages OpenID Connect for authentication and authorization when processing sign-in requests from users. |
| [Operations](./interfaces/operations.md) | Operations app provides administrators a centralized way to understand and govern activity on the DataOS platform and monitor how users optimally utilize available resources. |


# p

| Term | Description |
| --- | --- |
| [PDP](./resources/policy/understanding_abac_pdp_and_pep.md) | Policy Desicion Point is the service that evaluates a specific subject-predicate-object-metadata request against the current policies to determine if access to the DataOS resource/ environment is allowed or denied. |
| [PEP](./resources/policy/understanding_abac_pdp_and_pep.md) | Policy Enforcement Point is responsible for execution of the decision returned from PDP. |
| Poros | DataOS Poros is an orchestration engine for managing workflows, which are run for data transformation and movement. Working in coordination with Kubernetes, Poros efficiently allocates resources to various running jobs and services for data processing.  |
| [Policy](./resources/policy.md) | Policy is a in DataOS Resource to define rules to allow or deny access to DataOS resources. Policies are enforced using Attribute Based Access Control (ABAC) and define what actions(predicates), a user (a subject) can perform on a dataset, API Path, or a Resource (an object). |
| [Profiling](/resources/stacks/flare/case_scenario/data_profiling_jobs/#data-profiling-jobs) | Data profiling is a process that involves examining data to gain insights into its structure, quality, and characteristics. In DataOS,  data profiling workflow aims to analyze data for valid formats, null values, and inconsistencies to enhance data quality. By utilizing basic statistics, it uncovers anomalies, redundancies, and provides insights into the validity of the data. |


# q

| Term | Description |
| --- | --- |
| Querybook | Querybook is an integrated interface to run SQL queries on any datasets and explore.|


# r 

| Term | Description |
| --- | --- |
| [Resource](./resources.md) | Resources in DataOS are the lego blocks or the building blocks of the system that can be composed together. Each Resource in DataOS is a logical atomic unit with specific purpose, and is defined using a particular set of attributes. |
| Resource-instance | The instance of a DataOS Resource which is deployed and orchestrated as a 'record of intent'. Every resource-instance in a Workspace, will have a unique name.  |
| Resource-type | Resource-type refers to each of the different kinds of Resources which are available in DataOS. So, Workflow, Compute, Policy - each of them is a resource-type. |

# s 

| Term | Description |
| --- | --- |
| [Scanner](./resources/stacks/scanner.md) |  Scanner is a Stack in DataOS, a Python-based framework for extracting metadata from external source systems and the components within the DataOS environment. |
| [Secret](./resources/secret.md) | Secret is a DataOS Resource to store sensitive information such as passwords, tokens or keys in the internal vault of DataOS. |
| [Service](./resources/service.md) | Service is a DataOS Resource for long running process that is receiving and/or serving API. It is used for scenarios that need a continuous flow of real-time data, such as event processing, streaming IoT and more.   |
| [Stack](./resources/stacks.md) | DataOS Stacks are the programming paradigms supporting processing and management of data. They acts as the extension points of runnable resources, Workflow, and Service. |
| Sentinel | Sentinel is a monitoring and logging solution offering centralized observability in the DataOS infrastructure. |


# t 

| Term | Description |
| --- | --- |
| TUI | Terminal User Interface is the interface on the terminal where data practioners can interact with the DataOS context. |
| Themis | Themis provides native JDBC and ODBC connectivity, which makes it easy to connect to Themis from a wide variety of programming languages and tools. Themis is a modern, high-performance, and highly available JDBC server that provides a unified interface to connect with different database management systems (DBMS). Themis stands out from other distributed SQL query engines due to its unique and noteworthy features. |


# u
| Term | Description |
| --- | --- | 
| Unified Architecture | The unified architecture of DataOS refers to the cohesive and integrated design approach that combines various components, services, and technologies into a unified system. It enables data management, processing, and analysis, ensuring seamless interoperability and consistent user experience across different functionalities and applications within DataOS.|
| [Uniform Data Link](/resources/depot/#depot) | The Depot serves as the registration of data locations to be made accessible to DataOS. Once the Depot is created, each source system is assigned a unique address, referred to as a Uniform Data Link (UDL). Regardless of the source system's internal naming conventions and structure, the UDL ensures consistency in referencing data.  |
| [User Space](/interfaces/operations/#user-kernel) | User Space represents the domain of the operating system where data developers work and create resources such as workflows, services, secrets, depots, clusters, compute, etc for data processing jobs, services, and analytics workloads. Operations UI provides a way for users to observe and monitor these resources and their runtimes to debug if any issues.|


# v 

---

# w 

| Term | Description |
| --- | --- |
| [Workbench](./interfaces/workbench.md) | Workbench is a query interface within DataOS that provides functionality for editing, running, and saving SQL scripts, viewing query results and more. It serves as a versatile tool for running both simple and complex SQL queries on diverse data sources, enabling efficient data exploration.  |
| [Workflow](./resources/workflow.md) | The Workflow is a DataOS Resource for orchestrating data processing tasks with dependencies. It defines a pipeline involving a sequence of jobs, each utilizing stacks behind the scenes to accomplish various tasks. Within a Workflow, a job encompasses a sequence of processing tasks that need to be executed in a specific order to achieve desired outcomes.  |
| Workspace | In DataOS, a Workspace is a separate work environment for individuals or teams, providing logical separation and control over resources. Each Workspace functions like a tenant, allowing the creation and management of resources in an isolated context. By default, resources are created in the public Workspace, serving as a shared environment. |


# x

---

# y 

---

# z
