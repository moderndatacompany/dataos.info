# Lens Ecosystem

The Lens Ecosystem consists of the following components:

1. **Lens Query**:  enables end users to query Lens using the lens grammar.
2. **Lens Service**: facilitates the execution of lens queries, providing the necessary infrastructure and resources for efficient data processing.

Collectively, they form a robust platform that supports a wide range of data-related tasks and scenarios.


## Lens Query
The Lens can be queried by the end-user using Lens Queries which are essentially abstracted SQL queries. These queries can be executed from various interfaces like Lens Explorer, Workbench, Atlas, Tableau, Power BI, etc., The query API exposes the Lens, enabling the end-user to query it. Upon defining and deploying a data model, you can start querying the model. Users with limited SQL proficiency can explore the model using Lens Explorer - a low code, intuitive, drag-and-drop data exploration utility. To know more about Lens queries and Grammar, refer to the [Lens Query Language(LQL)](lql.md) document.

## Lens Service

Lens Service is a transpiler. It converts Lens Query to SQL Query. Currently, the Lens serviceis accessed via Gateway. Gateway analyses each incoming query and sends the query text to Lens Service, and the transpiler within the Lens Service will return the expanded SQL query to the Gateway. After receiving the expanded SQL query, Gateway sends it to Minerva query engine for execution. Query results are returned to Gateway with the data governance policies implemented. 

