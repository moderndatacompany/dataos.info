
# Source data connectivity

Connecting to data sources is the first step in building Data Products with DataOS. Now, it's time to set up connections to various data sources. In this topic, you'll learn how to configure **Depots** in DataOS, allowing seamless and secure access to a range of real-world data sources without moving the data.

## Scenario

Your team is expanding its use of DataOS and needs to integrate multiple data sources into the platform. Using **Depots**, you can establish secure connections to these data sources, enhancing data interoperability while keeping the data securely in place. This approach not only preserves data security but also facilitates interaction with various DataOS Resources.

## Quick concepts

The **Depot Resource** in DataOS provides a standardized way to connect to a variety of enterprise data sources, such as:

- Cloud-based object stores
- Databases
- Data warehouses
- NoSQL data stores

This versatility allows you to integrate structured, semi-structured, and unstructured data seamlessly. Using Depots, you can set up data sources to:

- Create high-quality data pipelines for building robust data products.
- Utilize query clusters for efficient data querying.
- Develop comprehensive semantic models.

## Prerequisites

Before diving into configuring data source connections, make sure you have everything ready:

1. **Check required Permissions**: Some tasks require specific permissions typically assigned to DataOS Operators. Ensure you have access to one of the following permission sets:

    | **Access Permission (via use-cases)**       | **Access Permissions (via tags)**      |
    |--------------------------------------------|---------------------------------------|
    | Read Workspace                             | `roles:id:data-dev `                  |
    | Manage All Depot                           | `roles:id:system-dev`                   |
    | Read All Dataset                           | `roles:id:user`                      |
    | Read all secrets from Heimdall             |                                |

2. **Check CLI installation and initialization**: You need this text-based interface that allows you to interact with the DataOS context via command prompts. Click [here](/interfaces/cli/) to learn more.

3. **Manage Credentials Securely**: Use **Instance Secrets** for storing your data source credentials, ensuring sensitive information remains protected.

    > **Important**: To prevent credential exposure, contact DataOS administrator and understand the best practices for handling sensitive data.

4. **Organize Your Code Repository**: Place Depot manifests in a private, permission-controlled repository to maintain security and compliance. 

## Data source connection - PostgreSQL
For demonstration purposes, we'll use a PostgreSQL database in this example. However, the same process applies to any database that supports the JDBC protocol, such as MySQL, MariaDB, and MSSQL-Server.

With permissions set up, the next step is to establish a connection from DataOS to your hosted PostgreSQL database. This connection is vital for seamless data retrieval, enabling you to access and work with PostgreSQL datasets directly in DataOS. It lays the foundation for building data pipelines, executing queries, and developing valuable data products using your PostgreSQL data source.

Refer to the next topic: [Data Source Connection - PostgreSQL](/learn/dp_developer_learn_track/data_source_connectivity/postgres/)
