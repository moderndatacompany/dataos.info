# Gateway Service

Gateway is one of the core components and primitives that comes with DataOS out-of-the-box. This component is backed by a Postgres DB (Gateway DB).

By default, Gateway hits [Metis](../../Ontology/Metis.md) for fetching the metadata of all the datasets and [Poros](../../About%20DataOS.md) for cluster information every 10 seconds. It stores this information locally for faster processing.  Gateway stores data policies in Gateway DB.

Whenever a SQL query is fired from any sources (viz Workbench, Atlas, Trino-CLI, Blender, JDBC, Lens, or Trino-python-client) Gateway parses and formats the query. The query is then forwarded to the [Minerva](../../Analytics/Minerva.md) cluster where execution takes place.

After receiving the query, Minerva analyses it and sends a decision request to Gateway for the governance to be applied. Gateway reverts with a decision based on user tags (received from Heimdall) and data-policy definition (received from Gateway DB).

Based on the decision, Minerva applies appropriate governance policy changes like filtering and/or masking (depending on the dataset) and sends the final result set to Gateway. The final output is then passed to the source from where the query was initially requested.

Additionally, Gateway functions as the load balancer in the DataOS architecture, which means it is responsible for equally distributing incoming requests among the available clusters to make sure minimum queue time.

Let us understand the mechanism with the help of the following diagram:

<img src="Gateway%20Service/MicrosoftTeams-image_(4).png"
        alt="Caption"
        style="display: block; margin: auto" />

Note: For a detailed description of [Metis](../../Ontology/Metis.md), [Minerva](../../Analytics/Minerva.md), [Heimdall](../Heimdall%20Capabilities.md), or [Poros](../../About%20DataOS.md) please refer to the respective documentation from these links.