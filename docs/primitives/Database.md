# Database

A Database is another important primitive in the DataOS ecosystem for the use cases where output is to be saved in a specific format in a relational database.

We added a feature to have a way to create a relational database. So, we actually have a database construct that you can create by providing a set of schema. Once the database construct is created in the DataOS ecosystem, you can create a [Depot](./Depot/Create%20Depot/Create%20Depot.md) on top of it. This Database primitive can be used in all the scenarios where you need to syndicate structured data. It fits perfectly into PostgreSQL- part of DataOS storage.; Once you create a database, then you can put a service on top of it to serve the data right from this Database. This is made possible by the [Beacon service](../Stacks/Beacon/Beacon.md) by exposing an API endpoint to the created table in which you can send the data to be stored. 

For example, let’s say we want to read data incrementally using python and want to store the state of the last read data. To implement this, we can create a Stores DB database [table structure](./Database.md) is given in the next section) to keep the state of incremental keys.  A Beacon service will help you to send a response to store the state and get the last state details of your incremental keys.

Database primitive allows you to syndicate the output internally in the DataOS, which is like creating a mart with the data in a structured format. We have many different options such as OLAP form in the Icebase or heap. But here, a database resource is created because we wanted a backing relational database for this service. Since it has a depot, you can address it the same way as anything else in DataOS and manage the schema through a resource/primitive in our system.

## Creating Database Primitive

1. Writing migrations- SQL statements to create schema.
2. Creating a database primitive YAML.
3. Applying it to DataOS CLI to create the resource in DataOS.
4. Creating and running a [Beacon](../Stacks/Beacon/Beacon.md) service to expose the PostgreSQL database.
5. Creating a policy in DataOS against which a CRUD operation will be performed by authorized users.

## Writing Migrations

Create a table `stores` to save incremental states.

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

## Creating a Database Primitive

The above migration is used while creating a database. Below is the YAML for creating a database within DataOS.

> Note: This database requires the path of a folder where all migrations are saved.
> 

```yaml
version: v1beta1
name: storesdb
type: database
description: Stores DB
tags:
  - database
database:
  migrate:
    includes:
      - ./services/metis-table-store/migrations_poc
    command: up
```

## Run the *'apply’* command to create a Resource

After creating the database yaml, you can create the database resource using the following command on DataOS CLI.

```
dataos-ctl apply -f <yamlfilepath> 
```

Once the above three steps are done successfully, you can create a Beacon service to expose this PostgreSQL database on API. You can read more about  [Beacon Stack in DataOS](../Stacks/Beacon/Beacon.md).