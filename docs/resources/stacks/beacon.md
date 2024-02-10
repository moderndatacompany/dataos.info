# Beacon

Beacon is a standalone HTTP server designed to facilitate the exposure of data objects and tables contained within PostgreSQL databases. The server offers a `beacon+rest` [Stack](../stacks.md), which exposes entities within a PostgreSQL database through a RESTful API, enabling simple CRUD Operations such as GET, POST, PUT, DELETE.

<aside class=callout>

While Beacon Stack offers CRUD functionality on top of PostgreSQL databases, it's essential to note that the API endpoints and operations are directly impacted by the structural limitations and permissions set by the database. 

</aside>

## Beacon Service

The Beacon Stack provides a robust solution for exposing a Postgres API endpoint to the external world. However, ensuring secure access, scalability, and seamless integration with other internal and external applications can be complex. This is where the [Service Resource](../service.md) becomes a critical factor.

By utilizing the [Service Resource](../service.md), you can ensure governed access to the endpoint, enable scalability in proportion to data growth and facilitate seamless access to all internal and external components and applications within DataOS. You can further enforce governance [Policies](../policy.md) to ensure secure access to PostgreSQL data, all in a declarative YAMLish manner within DataOS. 

![beacon](./beacon/beacon.png)

<center><i>Beacon Service in DataOS</i></center>

In summary, a Beacon Service enables you to expose an API endpoint for a specific table in a PostgreSQL database, allowing you to send data to be stored and interact with the data in the table by sending HTTP requests to the endpoint. With a Beacon Service, your web and other data-driven applications in DataOS can perform CRUD operations on data assets stored in Postgres.

## Structure of a Beacon YAML

![Beacon YAML Configuration Syntax](./beacon/beacon_syntax.png)

<center><i>Structure of a Beacon YAML configuration</i></center>

## Create a Beacon Service

Creating a Beacon Service is a straightforward process that is accomplished within the DataOS platform using a simple declarative YAMLish syntax. While you need to have a basic understanding of Postgres to define migrations, the rest of the process is declarative and straightforward. 

### **Prerequisites**

#### **Apply the Adequate Access Policy or Assign the Use Case**

Make sure you have an adequate tag or use case to create a [Service](../service.md). If you have have one, refer to the section below.

#### **Required Database exists**

Make sure that you have an active Database within DataOS, as per the schema you require. If you have one, navigate to the next step.

### **Create a YAML file**

#### **Configure the Service Resource Section**

At the core of any Beacon Service lies the Service Resource section, which is responsible for defining a Service Resource through a set of YAML attributes. A Service is a persistent process that either receives or delivers API requests. The Beacon Stack is then invoked within the Service to effectuate the exposition of Postgres API.The YAML syntax for the same is provided below.

```yaml
name: ${{stores-db}}
version: v1 
type: service 
tags: 
  - ${{syndicate}}
  - ${{service}}
service: 
  replicas: ${{2}} 
  ingress: 
    enabled: ${{true}} 
    stripPath: ${{true}} 
    path: ${{/stores/api/v1}} 
    noAuthentication: ${{true}} 
  stack: beacon+rest 
  envs: 
    PGRST_OPENAPI_SERVER_PROXY_URI: https://${{dataos-context}}.dataos.app/${{database-path}} # e.g. https://adapting-spaniel.dataos.app/stores/api/v1/
```

For a deeper understanding of Service Resource and its YAML attributes, please refer to the [Attributes of Service Resource YAML](../service/yaml_configuration_attributes.md) page.

#### **Configure Beacon Stack-specific Section**

The Beacon Stack-specific section, comprises attributes within the YAML configuration file. The YAML configuration is given below:

```yaml
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
        - database # Topology step 2 is dependent on step 1
```

The table below summarizes the various attributes within the Beacon Stack-specific Section.

| Attribute | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| [`source`](./beacon/beacon_yaml_attributes.md#source) | mapping | none | none | mandatory |
| [`type`](./beacon/beacon_yaml_attributes.md#type) | string | none | database | mandatory |
| [`name`](./beacon/beacon_yaml_attributes.md#name) | string | none | any string | mandatory |
| [`workspace`](./beacon/beacon_yaml_attributes.md#workspace) | string | public | any valid workspace name | mandatory |
| [`topology`](./beacon/beacon_yaml_attributes.md#topology) | list of mapping | none | none | mandatory |
| [`name`](./beacon/beacon_yaml_attributes.md#name-1) | string | none | any string | mandatory |
| [`type`](./beacon/beacon_yaml_attributes.md#type-1) | string | none | input/output | mandatory |
| [`doc`](./beacon/beacon_yaml_attributes.md#doc) | string | none | any string | optional |
| [`dependencies`](./beacon/beacon_yaml_attributes.md#dependencies) | list of strings | none | any valid dependent topology name | mandatory |

Each of the attributes in this section has been elaborated in detail on the [Attribute of Beacon Stack](./beacon/beacon_yaml_attributes.md) page.

### **Apply the YAML file**

You can apply the YAML file to create a Beacon Service within the DataOS environment using the command given below:

```shell
dataos-ctl apply -f ${{path-of-the-config-file}} -w ${{workspace}}
```

### **Check Run time**

```shell
dataos-ctl -t service -w ${{workspace}} -n ${{service-name}}  get runtime -r
# Sample
dataos-ctl -t service -w public -n pulsar-random  get runtime -r
```


## Case Scenarios

- [Exposing REST API’s on Database using Beacon](./beacon/exposing_rest_apis_on_database_using_beacon.md)

- [Store APIs on Beacon ](./beacon/store_apis_on_beacon.md)

- [Query Pushdown Streamlit Application ](./beacon/query_pushdown_streamlit_application.md)

- [Query Pushdown SSL Postgres](./beacon/query_pushdown_ssl_postgres.md)

- [Mask Data After Moving from Database to Icebase ](./beacon/mask_data_after_moving_from_database_to_icebase.md)

- [Exposing an API After Creating a Database ](./beacon/exposing_an_api_after_creating_a_database.md)