# Data source connectivity

As an Operator in the DataOS ecosystem, you are the backbone of secure and efficient data operations. Your role goes beyond managing existing workflows—it's about enabling seamless integration of data sources while ensuring that every connection is reliable, secure, and compliant with organizational policies.

This module focuses on Data Source Connectivity, a critical responsibility that involves configuring Depots, establishing secure access to diverse data sources, and maintaining operational efficiency. By the end, you’ll have the tools to ensure workflows remain efficient, data remains protected, and your team can access data sources securely.

## Scenario

A key project in your organization requires real-time data from multiple systems. Every configuration you manage will directly impact the team's ability to work with the data efficiently and securely. As you step into this challenge, you're faced with multiple objectives:

- Establishing secure connections to relational databases, cloud object stores, and other critical data sources.
- Configuring Depots to streamline these integrations.
- Ensuring all credentials are encrypted and security best practices are followed.

You’ve already learnt managing sensitive information through the [Credential security module](learn/operator_learn_track/cred_security/), which gave you the confidence to protect and handle credentials securely. Now, follow the steps given below to integrate a growing number of data sources into DataOS for your team. These connections are essential for powering data products that fuel decision-making across the organization.

Why you’re key to data source connectivity

- **Centralized security control**: You ensure compliance with security protocols, reducing risks and vulnerabilities.
- **Streamlined configuration**: Your efforts simplify the setup process, enabling seamless data access for other teams.
- **Consistency across systems**: Your unified approach ensures reliable and secure connections to all integrated data sources.

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

1. **Check required Permissions**: Some tasks require specific permissions typically assigned to DataOS Operators. Ensure you have access to one of the following permission sets either via use-case or via tags:

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