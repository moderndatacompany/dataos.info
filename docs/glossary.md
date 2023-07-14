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
| Airbyte | An open-source platform that facilitates data integration and replication processes by collecting data from various sources and making it available for analysis and storage. DataOS integrates with it and provides a graphical user interface to leverage its capabilities. |
| [Atlas](./interfaces/atlas.md) | A built-in business intelligence (BI) tool that enables you to generate visualizations, customize reports, and create interactive dashboards. |
| [Audiences](./interfaces/audiences.md) | It is an application derived from Lens that uses the semantic data models created through Lens to identify and categorize specific groups of people who have similar characteristics, traits, or behaviors. These categorized groups are referred to as audiences. |
| [Access Policy](./resources/policy.md#access-policy) | Access policies help ensure that data is handled securely, protecting sensitive information and maintaining data integrity.  |

---

# b

| Term | Description |
| --- | --- |
| [Beacon](./resources/stacks/beacon.md) | Beacon refers to a stack in DataOS. It enables your web and other applications to connect with PostgreSQL databases in DataOS. It allows you to perform essential operations like creating, reading, updating, and deleting data (CRUD operations), searching and filtering data, as well as renaming data assets stored in PostgreSQL.|
| [Benthos](./resources/stacks/benthos.md) | Benthos is a streaming stack within DataOS context. It is used to perform tasks like filtering, hydration, enrichment and transformation within the DataOS context. |
| [Bifrost](./interfaces/bifrost.md) | It is a graphical user interface for creation of policies. This can be accessed by both programmers and Business users. Helps in creating centrally authored but globally enforced policies. |
| [Bloblang](./resources/stacks/benthos/bloblang.md) | It is a programming language designed to extract, modify, and restructure data in various formats such as JSON, CSV, and XML. Bloblang is used in data integration and processing pipelines to perform tasks like data mapping, filtering, and conversion. |

---

# c 
| Term | Description |
| --- | --- |
| [CLI](./interfaces/cli.md) | Command Line Interface is essentially an interface to interact with the DataOS context. |
| Context | Context, environment and instance are used interchangeably by DataOS practioners. However, using the word context while defining an instance of DataOS is recommended. |
| Caretaker | Captures, manages, & exposes information from K8s API and storage buckets and serves it to various API for consumption by different core applications in the system. |

---

# d 

| Term | Description |
| --- | --- |
| [Depot](./resources/depot.md) | Depots can be understood as the connection pipeline enabling data access, exploration, and processing. It also provides references to virtual locations where data from different silos and clouds is fetched and stored. |
| [Data Toolbox](./resources/stacks/data_toolbox.md) | Toolbox allows set_version action on the data stored in Icebase that serves as DataOS internal storage. The data stored here is stored in Iceberg format. Using Toolbox, metadata version can be updated to the latest or specific version. |
| Data Developer | Data developer specializes in designing, building, and maintaining data-centric applications and systems. They work with data infrastructure, data sources, and data pipelines to enable efficient data processing and analysis. |
| [Data policy](./resources/policy.md#data-policy) | Data policy enforces a set of actions that will be taken on data assets when a user matching the policy rule requests access to data. These actions protect sensitive data and help organisations achieve data privacy and meet regulatory compliance expectations. |
| Dropzone | Dropzone is a depot in DataOS referring to an object storage. This storage is used as data lake to easily and securely upload files. |

---

# e 

| Term | Description |
| --- | --- |
| Egress | The process of transferring data from one system or network to another external system or network. Egress typically refers to data leaving a particular system or network. |
|  |  |

---

# f 

| Term | Description |
| --- | --- |
| [Flare](./resources/stacks/flare.md) | Flare stack is used for building end-to-end data pipelines within DataOS. It uses a YAML-based declarative programming paradigm built as an abstraction over Apache Spark. It offers an all-in-one solution for performing diverse data ingestion, transformation, enrichment, and syndication processes on batch and streaming data. |
| [Fastbase](./resources/depot/fastbase.md) | Fastbase is a managed depot type within an instance of DataOS that supports Apache Pulsar format for streaming workloads. Pulsar offers a “unified messaging model”  combining the best features of traditional messaging systems like RabbitMQ and pub-sub event streaming platforms like Apache Kafka. |
| Filebase | It is a managed depot that acts as a sink for all the different types of data on which processes like ELT/ETL are not running. File formats of the kind parquet, csv, pdfs, etc can be stored as itdo not enforce structure. |

---

# g 

| Term | Description |
| --- | --- |
| [GUI](./interfaces.md#graphical-user-interface-gui) | Graphical User Interface is where users can interact with various apps built within the DataOS context for query, exploration, and visualization tasks.|
|  | 

---

# h 

| Term | Description |
| --- | --- |
| Hera| Hera is a source of record for lineage and topology that collates metadata from multiple sources, schedulers and/or data processing frameworks as long as the necessary integration is in place. It can receive lieneage information from workflow orchestration engine like Argo or Airflow, or a Jupyter notebook. |
| [Heimdall](./architecture/heimdall_arch.md) | Heimdall allows authentication and authorization to access data meeting the security, privacy, and compliance requirements. The Heimdall application is responsible for PDP, User, and Policy Tags Management and Token, and Secret Provider. |

---

# i

| Term | Description |
| --- | --- |
| [Icebase](./resources/depot/icebase.md) | High-performance storage which provides necessary tooling and integrations to manage data and metadata in a simple and efficient manner while inherenting interoperability with capabilities spread across the data operating system. |
| Interface | Interfaces in DataOS such as CLI, GUI, API provide points of communication and interaction between different components for efficient data operations,  and control over various activities. interfaces enable self-service data management.  |
| [Ingress](./interfaces/operations.md#ingresses) | Ingress in DataOS exposes HTTP and HTTPS routes from outside the DataOS context to services within a DataOS context. It configures the incoming port for the service to allow access to DataOS resources from external links. |

---

# j 

| Term | Description |
| --- | --- |
| Jupyter Notebook | An interactive data science workspace that integrates and maintains 3rd party tools that also drive efficiencies. |
|  |  |

---

# k 

---

# l 

| Term | Description |
| --- | --- |
| [Lens](./interfaces/lens.md) | It is a modeling layer capable of accessing and modeling data from disparate sources. It supports data-driven decision-making by supporting and connecting to underlying data to the real-world business objects, formulates and delineate measure, KPIs, and relationships between different business concepts. |
|  |  |

---

# m 

| Term | Description |
| --- | --- |
| [Metis](./architecture/metis_arch.md) | Metis is a metadata manager, cataloging service, and database within the DataOS environment assissting with discoverability and observability capabilities for your enterprise data. |
| [Minerva](./architecture/minerva_arch.md) | Minerva is a query engine that enables access to data for business insights. It is an interactive query engine based on Trino that makes it easy to analyze big data using SQL. |

---

# n 
---

# o 

| Term | Description |
| --- | --- |
| [Operations](./interfaces/operations.md) | Operations Center provides administrators a centralized way to understand and govern activity on the DataOS platform and monitor how users optimally utilize available resources. |
| OS | OS means Operating System. It is the medium that sits between the machine and human enabling various operations. |
|  |  |

---

# p

| Term | Description |
| --- | --- |
| [Policy](./resources/policy.md) | Policy in DataOS is a rule that defines what tags are associated with subjects, predicates, or paths associated with objects, and additional conditions on metadata to allow or deny access to DataOS resource. |
| [PDP](./resources/policy/understanding_abac_pdp_and_pep.md) | Policy Desicion Point is the service that evaluates a specific subject-predicate-object-metadata request against the current policies to determine if access to the DataOS resource/ environment is allowed or denied. |
| [PEP](./resources/policy/understanding_abac_pdp_and_pep.md) | Policy Enforcement Point is responsible for execution of the decision returned from PDP. |
| Poros | Poros is a custom controller for K8s implemented using the operator pattern. It orchestrates all the primitives required to run DataOS using Kubernetes by registering them as custome resources. |

---

# q

| Term | Description |
| --- | --- |
| Querybook | Querybook is a Big Data integrated development environment that allows you to discover, create, and share data analyses, queries, and tables. |
|  |  |

---

# r 

| Term | Description |
| --- | --- |
| [Resources](./resources.md) | Resources in DataOS are the lego blocks or the building blocks that can be combined to other resources. Other word for resources with context to DataOS is primitives. |
| Resource-instance | Resource-instance is the instance of resource. A user typically use an instance of a resource while performing an action within DataOS. |
| Resource-type | Resource-type is the type of resource. DataOS resources can be categorized into segments, Workspace resource and platform resources. |

---

# s 

| Term | Description |
| --- | --- |
| [Secret](./resources/secret.md) | Secret is a DataOS resource that acts a vault where all the credentials, and access key are stored. |
| [Service](./resources/service.md) | Service is never ending process that is receiving and/or  serving API. It serves real-time data such as user interface.  |
| [Stack](./resources/stacks.md) | DataOS Stacks are the programming paradigms supporting processing and management of data. It acts as the extension points of runnable resources, Workflow, and Service. |
| Sentinel | Sentinel is a monitoring and logging solution offering centralized observability in the DataOS infrastructure. It gives a bird's eye view, keeping a watchful eye on metrics, alerts, and usage. |
| [Scanner](./resources/stacks/scanner.md) |  Scanner is a stack in DataOS is a Python-based framework for extracting metadata from external source systems and the components within the DataOS environment. |

---

# t 

| Term | Description |
| --- | --- |
| TUI | Terminal User Interface is the interface on the terminal where data practioners can interact with the DataOS context. |
| Themis | Themis provides native JDBC and ODBC connectivity, which makes it easy to connect to Themis from a wide variety of programming languages and tools. Themis is a modern, high-performance, and highly available JDBC server that provides a unified interface to connect with different database management systems (DBMS). Themis stands out from other distributed SQL query engines due to its unique and noteworthy features. |

---

# u 


---

# v 


---

# w 

| Term | Description |
| --- | --- |
| [Workbench](./interfaces/workbench.md) | Workbench is a SQL query engine that allows data explorations from disparate sources on the UI within the DataOS context. |
| [Workflow](./resources/workflow.md) | Workflow is a collection of jobs with directional dependencies that defines a hierarchy based on a dependency mechanism. Multiple jobs or a single job within each DAG. |
| Workspace | There are different environments in the DataOS like development environments, staging environments, and production environments. The whole idea of Workspaces stems from there. So you will have a development Workspace that has its own kind of separation of all the resources from all the other Workspaces. Think of it a sandbox environment. |

---

# x

---

# y 

---

# z
