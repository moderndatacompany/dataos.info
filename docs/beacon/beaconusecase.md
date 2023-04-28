# Create a Beacon service

This article describes the steps to create a Beacon service in DataOS to access tables in PostgreSQL.

**Step 1: [Create SQL Files](#create-sql-files)**

**Step 2: [Create Database YAML](#create-database-yaml)**

**Step 3: [Create Beacon Service YAML](#create-beacon-service-yaml)** 

**Step 4: [Create Policy YAML](#create-policy-yaml)**

## Create SQL files 

1. Create a migration folder.
2. Create Up and Down SQL files.

      a. In up.sql, write the code to create tables, alter tables, create functions & triggers.

      b. In down.sql, we drop tables, functions & triggers.

3. Test your SQL commands on local Postgre instance.
  
> :material-alert: **Note**: Naming of SQL files must be 00001.initial.up.sql & 00001.initial.down.sql format.

## Create Database YAML
1. Provide database name, the full path of the migration folder containing sql files.
```yaml
version: v1beta1
name: citybase                                         # database name 
type: database
description: citybase database for storing city sample data.
tags:
  - database
database:
  migrate:
    includes:
      - /home/user/postgres_beacon/migrations         # all up & down sql files.
    command: up                                       # in case of drop table, write down.
```
2. After creating database YAML, run *apply* command on DataOS CLI to create **database** resource in DataOS.
```
dataos-ctl apply -f database.yaml
```
   To learn more about *apply* command, refer to [CLI](../cli/tutorials.md) section.
   
## Create Beacon Service YAML
While defining a service, you have to define the following properties:

- **replicas**: Create multiple replicated services.
- **ingress**: Configure the incoming port for the service to allow access to DataOS resources from external links.
  Provide the following properties.
     - enable ingress port
     - enable the stripPath to strip the specified path and then forward the request to the upstream service.
     - provide path
     - Set noAuthentication to false if authentication is needed 
- **environment**: configure destination url and path
- **source**: about the data source
- **topology**: provide objects and their input/output types

```yaml
version: v1beta1
name: scitydatabase-rest    #service name
type: service
tags:
  - syndicate
  - segments
  - service
service:
  replicas: 2
  ingress:
    enabled: true
    stripPath: true
    path: /citybase/api/v1   # how your url going to be appeared.
    noAuthentication: true
  stack: beacon+rest
  envs:
    PGRST_OPENAPI_SERVER_PROXY_URI: https://lively-neutral-akita.dataos.io/citybase/api/v1
                                    # environment url + path: /citybase/api/v1
  beacon:
    source:
      type: database
      name: citybase
      workspace: public
  topology:
  - name: database
    type: input
    doc: citybase database connection
  - name: rest-api
    type: output
    doc: serves up the citybase database as a RESTful API
    dependencies:
    - database
```
2. Run the *apply* command on DataOS CLI to create the **service** resource for the database.
   
   To learn more about *apply* command, refer to [CLI](../cli/tutorials.md) section. 

## Create Policy YAML
A policy in DataOS should be created against which a CRUD operation will be performed by authorized users.

1. Define policy for allowing users to access the database resource and perform specified operations.
```yaml
name: "city-search-app-demo"
version: v1beta1
type: policy
layer: system
description: "Allow user to access citybase app rest apis"
policy:
  access:
    subjects:
      tags:
        - - "dataos:u:user"    # user operator can access API
    predicates:
      - "GET"
      - "POST"
      - "PUT"
      - "OPTIONS"              # user can use all CRUD operation if we allow them.
    objects:
      paths:
        - "/citybase/api/v1"   
    allow: true
```
2. Run the *apply* command on DataOS CLI to create the **policy** resource for the database.

   To learn more about *apply* command, refer to [CLI](../cli/tutorials.md) section.

  > :material-alert: **Note**: The user who has operator tag can only apply policy.


   Now you are ready to access the PostgreSQL database with the exposed API.

   For example, the following URL is to carry out full-text search on a column:


   https://lively-neutral-akita.dataos.io/citybase/api/v1/place_search_ts?document_with_weights=phfts(english).kasganj


|**Property**| **Value** | 
| ------ | -------- |
| environment name | https://lively-neutral-akita.dataos.io/ |
| database path | citybase/api/v1/ |
| table name    | place_search_ts |
| column name on which you created ts vector | document_with_weights |


