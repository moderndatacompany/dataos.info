# Store APIs on Beacon

## Incremental Key Store

Store DB is created to store the state of incremental keys. For example, let’s say you want to read data incrementally using python and want to store state of till when you have read data or for which categories you have read data. 

To implement this you can create a database (with below mentioned table structure) and store the state by sending state detail with store name (name) and key’s you want to store.

And, in next iterations, whenever you need to read the last state you can get the last state stored for above created database.

This is made possible by beacon service by exposing an API end point to created table on which you can send response to store the state and get the last state details of your incremental keys.

You can achieve this by following below steps - 

Steps - 

1. Writing migrations
2. Creating a database
3. Running a service to expose database (**`Beacon`**)

**Writing migration -** 

created a table `stores` to store all states of incremental states.

```sql
CREATE TABLE IF NOT EXISTS stores (
    uuid                              uuid NOT NULL,
    name                              character varying(500) NOT NULL,
    key                               character varying(500) NOT NULL,
    value                             jsonb NOT NULL,
    created_at                        timestamp without time zone NOT NULL,
    updated_at                        timestamp without time zone NOT NULL,
    partition_key                     character varying(200),
    expire_on                         timestamp without time zone NULL,
    UNIQUE (name, partition_key, key),
    PRIMARY KEY (uuid)
);
```

**Creating a database -**

Above written migration is used while creating a database. Below is yaml for creating a database within dataos.

This database requires path of a folder where all migrations are saved.

```yaml
version: v1beta1
name: storesdb
type: database
description: Stores DB
owner: rakeshvishvakarma
tags:
  - database
database:
  migrate:
    includes:
      - ./services/metis-table-store/migrations_poc
    command: up
```

After creating this database yaml, you can apply using `dataos-cli`

Once above two steps are done successfully, you can run beacon yaml to expose this posgres database on API.

**Running a `Beacon Service`**

To expose `storesdb` on api, create a below yaml and run. 

```yaml
version: v1beta1
name: stores-db
type: service
tags:
  - syndicate
  - service
service:
  replicas: 2
  ingress:
    enabled: true
    stripPath: true
    path: /stores/api/v1
    noAuthentication: true
  stack: beacon+rest
  envs:
    PGRST_OPENAPI_SERVER_PROXY_URI: https://flexible-buffalo.dataos.app/stores/api/v1
  beacon:
    source:
      type: database
      name: storesdb
      workspace: public
  topology:
  - name: database
    type: input
    doc: stores database connection
  - name: rest-api
    type: output
    doc: serves up the stores database as a RESTful API
    dependencies:
    - database
```

Running this service will expose database on give `PGRST_OPENAPI_SERVER_PROXY_URI` and you can pass table names at end of URL and get request will give you table results.

To store state in created table you can post data using below command - 

```bash
curl --location --request POST 'https://flexible-buffalo.dataos.app/stores/api/v1/stores' \
--header 'Content-Type: application/json' \
--data-raw '{
        "uuid": "ebf335fa-45c8-4691-9253-18fbcdc87a3a",
        "name": "flareincr31032022",
        "key": "incremental_order_002",
        "value": "{\"start\": 10}",
        "created_at": "2022-07-12T19:00:00",
        "updated_at": "2022-07-13T19:00:00",
        "partition_key": "default",
        "expire_on": "2022-07-20T19:00:00"
    }'
```

**curl and API url for filtering rows and columns (to get state of your interest)**

1. To select one column from store table get request  or you can run curl command - 
    
    ```powershell
    [https://flexible-buffalo.dataos.app/stores/api/v1/stores](https://flexible-buffalo.dataos.app/stores/api/v1/stores)
    ```
    
    ```powershell
    curl --location --request GET 'https://flexible-buffalo.dataos.app/stores/api/v1/stores'
    ```
    
2. To select a column from stores table 
    
    ```powershell
    [https://flexible-buffalo.dataos.app/stores/api/v1/stores](https://flexible-buffalo.dataos.app/stores/api/v1/stores)?select=name
    ```
    
    ```powershell
    curl --location --request GET 'https://flexible-buffalo.dataos.app/stores/api/v1/stores?select=name'
    ```
    

1. To select column and filter row wise data
    
    ```powershell
    https://flexible-buffalo.dataos.app/stores/api/v1/stores?select=*name=eq.flareincr31032021
    ```
    
    ```powershell
    curl --location --request GET 'https://flexible-buffalo.dataos.app/stores/api/v1/stores?select=*name=eq.flareincr31032021'
    ```