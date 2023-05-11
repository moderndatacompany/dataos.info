# Architecture Overview

In this article, we first discuss the Minerva Clusters to have a general understanding of the way Minerva works. Then we will discuss the high-level architectural components which interact with Minerva during the query execution process.

# About Minerva Cluster

A Minerva cluster consists of a single coordinator node and one or more worker nodes, and Minerva uses its own coordinator within the cluster to schedule queries among its workers. The coordinator is responsible for submitting, parsing, planning, and optimizing queries and query orchestration, and worker nodes are responsible for query processing. Minerva enables you to concurrently run hundreds of memory, I/O, and CPU-intensive queries. For such query load, a single Minerva cluster is not sufficient, and you need to create multiple clusters. It can scale to hundreds of worker nodes while efficiently utilizing cluster resources.

Minerva uses Gateway, a query router that sits in front of single or multiple Minerva clusters and becomes the interface for all the queries executed across the clusters. These queries are submitted from the Workbench, Minerva CLI, Atlas, Blender, JDBC, Lens, or any DataOS app such as the audience/segment app.  Gateway also ensures high availability in case of downtime and balances the load across the clusters.

<img src="Architecture%20Overview/minerava-query-engine2_(1).jpg" 
        alt="minerava-query-engine2"
        style="display: block; margin: auto" />

# Detailed Architecture Overview

<img src="Architecture%20Overview/minerva-overview.png" 
    alt="minerva-overview.png"
    style="display: block; margin: auto" />

<br>

> 💡 Minerva query engine integrates within the DataOS ecosystem to provide the following functionalities:
> - Integration with Heimdall, authentication and authorization system, and credential store.
> - Integration with Poros, resource manager to know about the data policies to mask and filter data.
> - Integration with Metis 2.0 data discovery and cataloging services.
> - Support for Depot service to read data from various data sources.
> - Support for data source connectors for exploring data without bringing it to DataOS.
> - Support for gathering query-level and cluster-level statistics.
> - Integration with in-house tracking, monitoring, and auditing systems.

## Query Execution Workflow

1. The query is submitted by the Minerva client.
2. The gateway acts as an abstraction layer over Minerva clusters. It is responsible for parsing SQL queries and formatting the query.
3. It communicates with Heimdall (Governance engine) for access decisions. 
4. After parsing the received SQL query, Gateway communicates with METIS to fetch metadata of all the datasets being accessed by the said query. 
5. It then forwards the query to a Minerva cluster where the actual execution of the query happens. 
6. After receiving the query, Minerva analyzes it and sends a decision request to Gateway for the required data policies to be applied. 
7. The gateway then reverts with a decision made based on the data policy definition (received from Poros). 
8. As per Gateway’s decision, Minerva makes the appropriate changes (filter, mask) and forwards the final result set to the gateway.
9. The gateway then passes the query result to the actual source from where the query is requested initially.

<img src="Architecture%20Overview/Gateway.png" 
        alt="Gateway.png"
        style="display: block; margin: auto" />

# Components and Responsibilities

Minerva consists of many components that work together to create the whole experience of the query execution process on Minerva. 

## Gateway Service

Gateway Service is home to two servers- The [Proxy server](Architecture%20Overview.md) and the [API server](Architecture%20Overview.md).

### Proxy Server

This service creates a proxy server within the gateway service to handle all interactions from the client to the Minerva clusters.  Every request to the system for a query goes through the proxy server. Whenever a SQL query is fired, it is directed to Gateway, which reads and analyses the query for the type of query and tables it contains before sending it to Minerva clusters for execution. 

This proxy manages all requests to Minerva UI paths, Minerva rest API paths, and query creation requests coming from any client including the Minerva CLI. 

### API Server

This service hosts some API services and is responsible for exposing REST APIs for multiple resources. 

API server provides REST endpoints for the following resources: 

1. Clusters: To read information about active/inactive clusters and API to register new clusters.
    
    The Gateway service acts as a Cluster Selection Engine, responsible for managing information of all running clusters behind the gateway. Gateway functions as the load balancer in the DataOS environment. A load balancer essentially allocates a task to all the available clusters. This assists in lowering the time taken to execute and present the result while also significantly impacting the computation and distribution of load.
    
2. Query: To get information about queries and to POST query audit information to the gateway service.
3. Meta Inspect: To get basic information about the list of catalogs, schemas, tables, and table descriptions for connected depots. 
4. Access Policy: To get information about access policy decisions. 
    
    Gateway service interacts with Heimdall for data access policy to validate the authenticity of the user and the access the user has against the user tags and clusters. Based on the decision, it forwards the query for execution. It reports to the users when the query is rejected or exceptions from clusters are encountered. 
    
5. Data Policy: To get information about the policy decision for a query and also for CRUD operations.
    
    Once the access privileges are checked, it communicates with Poros for the Data Policy(Checks and applies data masking and data filtering rules ) and passes on this information to Minerva along with the query to execute. The Gateway service is essentially the decision-making point within the DataOS environment when it comes to applying Governance to the output.
    

### Gateway Service DB

Gateway is a service backed by the Postgres database. This is one of the important functionality built into Gateway service. It stores query audits, cluster information, and data policy audits.

## Important associated workflows and their flow of control

1. Cluster Scanner - This runs as a scheduled job with the gateway service and is responsible for interacting with the Poros APIs through a Poros Client and is responsible for getting and persisting all the information about active clusters into the Gateway Service DB after a delay of  10 seconds. 
2. Cluster Health Checker - This ensures that the gateway service always has an updated list of Minerva clusters and their status. This runs as a scheduled job and is responsible for reading all cluster information from the Gateway Service  DB and then trying and accessing each one to validate if the cluster is still healthy and up and accordingly updating the status in the Gateway Service DB after a delay of 10 seconds. 
3. Policy Fetcher - This job starts with the gateway service, hits Poros to fetch a list of all the data policies and upserts it into the Gateway DB. 
4. Get Policy Decisions - This is one of the prime functionalities of the Gateway Service. It provides the data policy decision to the Minerva Governor plugin about what policy needs to be applied to the data from the query. The policy currently provides two primary pieces of information - 
    - Masking - Which columns of data need to be masked and how they should be masked to selectively hide and obfuscate according to the level of anonymity needed.
    - Filtering - Which rows of data has to be filtered from the result of the query for the user running the query.
5. Fetch Query Info - This job does not start with the gateway service. This is originally queued whenever a query is successfully sent to Minerva from the proxy server.  This job is responsible for fetching the metadata of the query from Minerva once the queued query is run. If the query metadata is not available yet, it persists current state of the query and re-enqueues the job to run after a delay of 30 seconds. 
6. Data Policy - This contains some required internal methods to make the decision on the data policy for the incoming query. It also has all the models for the data policy, including the filter and mask operators. It creates the rule engine that governs the data policy decision-making. 
7. Governor/Access Control Plugin  - This is responsible for the following:
    - Registering the clusters to the Gateway Service. 
    - Enforcing the data policy before querying. It uses the Gateway client to get the data policy decision from the Gateway and then enforces it by applying both the masking and the filtering policy decisions for the user. 
    - Tracking the events for the creation and completion of a query on Minerva and in the case of completion of the query, this plugin uses the Gateway client to hit a gateway endpoint and write the metadata of the query back to the Gateway.  
8. Minerva - UDF plugin - This is responsible for generating some random test data so that we can set up the system and test the system easily. 
9. Minerva CLI - This component provides the Minerva CLI jar and is responsible for creating the Minerva console and management of the interaction(commands and options) of the user with the CLI parsing and executing both IO operations. This sends the request to the proxy server that is started by the Gateway service to further process the query.

## Recommended Reading

- [Creating Minerva Clusters Page](Architecture%20Overview/Creating%20Minerva%20Clusters.md)

- [On-Demand Computing Page](Architecture%20Overview/On-Demand%20Computing.md)