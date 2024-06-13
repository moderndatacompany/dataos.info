# Opensearch

DataOS provides the capability to connect to Opensearch data using Depot. The Depot facilitates access to all documents that are visible to the specified user, allowing for text queries and analytics.

## Requirements

To establish a connection with Opensearch, the following information is required:

- Username
- Password
- Nodes (Hostname/URL of the server and ports)

## Template

To create a Depot of Opensearch, in the type field you will have to specify type ‘ELASTICSEARCH‘, and utilize the following template:

=== "v1"

    ```yaml
    name: {{depot-name}}
    version: v1
    type: depot
    tags:
      - {{tag1}}
      - {{tag2}}
    owner: {{owner-name}}
    layer: user
    depot:
      type: ELASTICSEARCH              
      description: {{description}}
      external: {{true}}
      connectionSecret:                
        - acl: rw
          values:
            username: {{username}}
            password: {{password}}
        - acl: r
          values:
            username: {{opensearch-username}}
            password: {{opensearch-password}}
      spec:                           
        nodes:
          - {{nodes}}
    ```
=== "v2alpha"

    ```yaml
    name: {{depot-name}}
    version: v2alpha
    type: depot
    tags:
      - {{tag1}}
      - {{tag2}}
    owner: {{owner-name}}
    layer: user
    depot:
      type: ELASTICSEARCH              
      description: {{description}}
      external: {{true}}
      connectionSecret:                
        - acl: rw
          values:
            username: {{username}}
            password: {{password}}
        - acl: r
          values:
            username: {{opensearch-username}}
            password: {{opensearch-password}}
      elasticesearch:                           
        nodes:
          - {{nodes}}
    ```