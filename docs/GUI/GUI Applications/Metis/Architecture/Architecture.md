# Architecture

Metis Metadata Architecture enables you to set up a metadata API server, create a metadata repository, and write scanner and integration applications that store, use, or manage the metadata. 

## Components

The following components are part of the metadata architecture:

Metis API Server: Metis is an API server and exposes API through which all other components interact with Metis for Governance and Observability.

Metadata Ingestion Framework: Various connectors and workflows to extract metadata from the data sources. It also fetches information about profiling and quality as well as lineage and ingests into Metis DB. This metadata is consumed by various components for governance and observability, so you have increased visibility and trust in the data. Metis gives you the flexibility to use different ingestion/consumption interfaces.

Metis DB: To store metadata. It keeps updated information about the state of all the Entities of your data ecosystem and their Relationships. This metadata is consumed by various components for observability and governance, so you have increased visibility and trust in the data.

Metis UI: Metis UI comes with an evolving set of features facilitating business users in exploring and keeping track of all the data assets created within the DataOS environment. Metis UI also provides you with a powerful interface for examining lineage, managing ownership, governing with tags, and much more. For a complete overview of the capabilities currently supported, please refer to [Metis Features](../Metis%20Features/Metis%20Features.md).

Metis Search Engine: Powered by ElasticSearch is the UI's indexing system to help users discover the metadata.

Changed Event Handler: To Keep track of events happening around your data assets and update metadata storage so that you have the latest and fresh metadata.

Heimdall: To manage granular policies with various user roles to govern the metadata.
 
<center>

![Picture](./MicrosoftTeams-image_(117).png)

</center>

## Metadata Ingestion

Integrate your database, dashboard, messaging, and pipeline services with DataOS Poros as a workflow engine to run metadata ingestion jobs. Metis supports both pull-based metadata ingestion.

Metadata capturing is accomplished by the DataOS Scanner stack. The Scanner-based Ingestion Framework is a Python-based library for extracting Metadata from external source systems (e.g., Snowflake, Looker, MySQL, Kafka), transforming and writing it into Metis DB (Postgres database)using the Metis server REST APIs. The Scanner stack for metadata ingestion comes with a host of capabilities. It supports entity metadata extraction and schema extraction from an extensive list of sources such as databases, data warehouses, dashboards, messaging services, etc. 

The Scanner stack also supports connecting with various DataOS apps/components and getting the information surfaced by the individual apps.

This Metadata is available on Metis UI so that data teams can see all the information about the data loaded, trace data sources, explore lineage, and understand the importance and criticality of the data.

> 🗣 DataOS Scanner is a flexible and extensible framework, you can easily integrate it with new sources.

## Scanner Workflows

Metis Admins can configure the following workflows to run these pipelines and add a schedule to kick off the ingestion jobs automatically. 

Getting started with the Ingestion Framework is as simple: just define a YAML file using Scanner stack and apply the workflows using dataOS CLI.

To learn more about how to configure and run these workflows, refer to
[Scanner](../../../../Stacks/Scanner/Scanner.md).

## Metadata Consumption

Metis supports REST APIs for pulling and pushing data out of the metadata storage system. Metis acts as a REST server backed by the Postgres database and exposes API endpoints.  Any DataOS component/external application can talk to Metis using exposed API. The stored metadata is used by various DataOS components for discoverability, governance, and observability. External apps running on top of DataOS can also fetch this metadata via Metis server APIs.

It also powers its UI by making the metadata available for users to explore and discover assets.
 
<center>

![Picture](./MicrosoftTeams-image_(105).png)

</center>

## End User through Metis UI

Metadata consumption is through Metis UI, where users can explore, discover, and collaborate on all data. The Metis API server powers the Metis UI and populates the metadata information to
make it readily available to all users. Metis UI gives users various options to enrich the captured metadata by adding descriptions, glossary terms, and announcements. To know more, refer to [Metis Features](../Metis%20Features/Metis%20Features.md).

## Components and Applications through HTTP Requests

Metis API server also serves the metadata requests from internal components as well as external applications through HTTP requests. When these requests are made to the backend Metis API server, Metadata API lets you specify the kind of object to be retrieved from the metadata server. The JSON Schema is used to model the entities across all the APIs and schemas in Metis. This helps the components and stacks to use the API calls to deal with standard metadata format.

## Metadata Governance

All metadata operations in Metis are performed through well-defined roles and policies.

To learn more, refer to
[Pre-defined Roles and Policies](./Pre-defined%20Roles%20and%20Policies.md).

## Metadata Change Events

Metadata changes generate events that indicate which entity changed, who changed it, and how it changed. 

The Change Event Handler identifies and captures metadata changes, delivering them in real time to a downstream process or system. Its responsibility is to capture changes made to metadata; it notifies and registers the change with the Metis search engine and eventually gets stored in metis DB.

This process ensures that data teams have access to the latest and freshest metadata, enhancing visibility and trust in the data. You can view a summary of change events in the Activity Feed for all data or for data you are the owner of.