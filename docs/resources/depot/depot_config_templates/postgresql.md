# PostgreSQL


DataOS allows you to connect to a PostgreSQL database and read data from tables using Depots. A Depot provides access to all schemas visible to the specified user in the configured database.

## Requirements

To create a Depot and connect to a PostgreSQL database, you need the following information:

- Database name: The name of the PostgreSQL database.
- Hostname/URL of the server: The hostname or URL of the PostgreSQL server.
- Parameters: Additional parameters for the connection, if required.
- Username: The username for authentication.
- Password: The password for authentication.

## Template

To create a Depot of type ‘POSTGRESQL‘, use the following template:

**Use this template, if self-signed certificate is enabled.**

=== "v1"

    ```yaml
    name: {{postgresdb}}
    version: v1
    type: depot
    layer: user
    depot:
      type: JDBC                  
      description: {{To write data to postgresql database}}
      external: {{true}}
      connectionSecret:           
        - acl: rw
          type: key-value-properties
          data:
            username: {{username}}
            password: {{password}}
      spec:                        
        subprotocol: "postgresql"
        host: {{host}}
        port: {{port}}
        database: {{postgres}}
        params: #Required 
          sslmode: {{disable}}
    ```

=== "v2alpha"

    ```yaml
    name: {{postgresdb}}
    version: v2alpha
    type: depot
    layer: user
    depot:
      type: JDBC                  
      description: {{To write data to postgresql database}}
      external: {{true}}
      connectionSecret:           
        - acl: rw
          type: key-value-properties
          data:
            username: {{username}}
            password: {{password}}
      postgresql:                        
        subprotocol: "postgresql"
        host: {{host}}
        port: {{port}}
        database: {{postgres}}
        params: #Required 
          sslmode: {{disable}}
    ```

**If self-signed certificates are not being used** by your organization, for connection to these storage systems, then you do not need to write additional parameters within the spec section.

=== "v1"

    ```yaml
    name: {{depot-name}}
    version: v1
    type: depot
    tags:
      - {{tag1}}
    owner: {{owner-name}}
    layer: user
    depot:
      type: POSTGRESQL
      description: {{description}}
      external: true
      connectionSecret:                               
        - acl: rw
          type: key-value-properties
          data:
            username: {{posgresql-username}}
            password: {{posgresql-password}}
        - acl: r
          type: key-value-properties
          data:
            username: {{posgresql-username}}
            password: {{posgresql-password}}
      spec:                                          
        host: {{host}}
        port: {{port}}
        database: {{database-name}}
        params: # Optional
          {{"key1": "value1"}}
          {{"key2": "value2"}}
    ```

=== "v2alpha"

    ```yaml
    name: {{depot-name}}
    version: v2alpha
    type: depot
    tags:
      - {{tag1}}
    owner: {{owner-name}}
    layer: user
    depot:
      type: POSTGRESQL
      description: {{description}}
      external: true
      connectionSecret:                               
        - acl: rw
          type: key-value-properties
          data:
            username: {{posgresql-username}}
            password: {{posgresql-password}}
        - acl: r
          type: key-value-properties
          data:
            username: {{posgresql-username}}
            password: {{posgresql-password}}
      postgresql:                                          
        host: {{host}}
        port: {{port}}
        database: {{database-name}}
        params: # Optional
          {{"key1": "value1"}}
          {{"key2": "value2"}}
    ```