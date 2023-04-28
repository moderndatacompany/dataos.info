# **Snowflake**

DataOS allows you to connect to Snowflake to read data from Snowflake tables using Depots.
Snowflake database is a purely cloud-based data storage and analytics data warehouse provided as a Software-as-a-Service (SaaS). An entirely new SQL database engine (similar to ANSI SQL syntax and features) is designed to work with cloud infrastructure to access the Snowflake database.

## **Requirements**

To connect to Snowflake, you need:

- URL of your Snowflake account
- Snowflake username, typically your login username
- Snowflake user password
- Snowflake Database name
- Database schema where your table belongs

## **Template**

To create a Depot of type ‘SNOWFLAKE‘, use the following template:

```yaml
version: v1
name: <depot-name>
type: depot
tags:
  - dropzone
  - snowflake
layer: user
depot:
  type: SNOWFLAKE                                  **# Depot type**
  description: "Snowflake Sample data"
  spec:                                            **# Data Source Specific Configurations**
    url: MUA15126.snowflakecomputing.com
    database: "SF_TUTS"
  external: true
  connectionSecret:
    - acl: rw
      type: key-value-properties
      data:
        username: <get hold of it>
        password: <you have to earn it>
```