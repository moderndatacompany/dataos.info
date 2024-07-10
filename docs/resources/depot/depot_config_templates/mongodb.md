# MongoDB

DataOS allows you to connect to MongoDB using Depot, enabling you to interact with your MongoDB database and perform various data operations. You can create a MongoDB Depot in DataOS by providing specific configurations.

## Requirements

To connect to MongoDB using DataOS and create a MongoDB Depot, the following information is required:

- Subprotocol: The Subprotocol of the MongoDB Server
- Nodes: Node
- Username: The username for authentication.
- Password: The password for authentication.

## Template

To create a Depot of type 'MONGODB', use the following template:

=== "v1"

    ```yaml
    name: {{depot-name}}
    version: v1
    type: depot
    tags:
      - {{tag1}}
      - {{tag2}}
    layer: user
    depot:
      type: MONGODB                                 
      description: {{description}}
      compute: {{runnable-default}}
      spec:                                          
        subprotocol: {{"mongodb+srv"}}
        nodes: {{["clusterabc.ezlggfy.mongodb.net"]}}
      external: {{true}}
      connectionSecret:                              
        - acl: rw
          type: key-value-properties
          data:
            username: {{username}}
            password: {{password}}
    ```

=== "v2alpha"

    ```yaml
    name: {{depot-name}}
    version: v2alpha
    type: depot
    tags:
      - {{tag1}}
      - {{tag2}}
    layer: user
    depot:
      type: MONGODB                                 
      description: {{description}}
      compute: {{runnable-default}}
      mongodb:                                          
        subprotocol: {{"mongodb+srv"}}
        nodes: {{["clusterabc.ezlggfy.mongodb.net"]}}
      external: {{true}}
      connectionSecret:                              
        - acl: rw
          type: key-value-properties
          data:
            username: {{username}}
            password: {{password}}
    ```


