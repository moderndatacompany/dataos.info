# Snowflake

DataOS provides integration with Snowflake, allowing you to seamlessly read data from Snowflake tables using Depots. Snowflake is a cloud-based data storage and analytics data warehouse offered as a Software-as-a-Service (SaaS) solution. It utilizes a new SQL database engine designed specifically for cloud infrastructure, enabling efficient access to Snowflake databases.

## Requirements

To establish a connection to Snowflake and create a Depot, you will need the following information:

- Snowflake Account URL: The URL of your Snowflake account.
- Snowflake Username: Your Snowflake login username.
- Snowflake User Password: The password associated with your Snowflake user account.
- Snowflake Database Name: The name of the Snowflake database you want to connect to.
- Database Schema: The schema in the Snowflake database where your desired table resides.

## Template

To create a Depot of type 'SNOWFLAKE', you can utilize the following YAML template as a starting point:

```yaml
name: {{snowflake-depot}}
version: v1
type: depot
tags:
  - {{tag1}}
  - {{tag2}}
layer: user
depot:
  type: snowflake
  description: {{snowflake-depot-description}}
  spec:
    warehouse: {{warehouse-name}}
    url: {{snowflake-url}}
    database: {{database-name}}
  external: true
  connectionSecret:
    - acl: rw
      type: key-value-properties
      data:
        username: {{snowflake-username}}
        password: {{snowflake-password}}
```
