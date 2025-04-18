# Using an Instance Secret for secure database connection in a Data Product
This section involves a real-life use case of an Instance Secret.

## Scenario

A Customer Insights Data Product development requires access to a PostgreSQL database that stores customer transaction data. An Instance Secret is used to securely store and retrieve the credentials of PostgreSQL to set up the connection.

## Steps to implement

1. **Create an Instance Secret manifest file:**



Create an Instance Secret to store the database connection credentials of PostgreSQL securely:

=== "Read-only Instance Secret"

  ```yaml 
  # PostgresSQL Read Instance-secret Manifest
  name: postgresdb-r # Unique identifier for Resource, replace ${postgres-depot-name} with depot name
  version: v1 # Manifest version
  type: instance-secret # Type of the Resource
  description: an instance secret for storing PostgreSQL credentails # Purpose of the Instance-secret
  layer: user # DataOS layer
  instance-secret:
    type: key-value-properties # Secret type
    acl: r # Access control: 'r' for read-only
    data:
      username: db_user
      password: 45678
  ```
=== "Read-write Instance Secret"

  ```yaml 
  # PostgresSQL Read Write Instance-secret Manifest
  name: postgresdb-rw 
  version: v1 # Manifest version
  type: instance-secret # Type of the Resource
  description: an instance secret for storing PostgreSQL credentails # Purpose of the Instance-secret
  layer: user # DataOS layer
  instance-secret:
    type: key-value-properties # Secret type
    acl: rw # Access control: 'rw' for read-write
    data:
      username: db_user
      password: 45678
  ```


2. **Apply the Instance Secret using the DataOS CLI**

```bash
dataos resource apply -f db-secret.yaml
```

3. **Refer to the Instance Secret in the Depot Manifest**



Now that the secret is stored securely, reference it in the Depot Manifest. The Depot Manifest defines the PostgreSQL connection for the Data Product development.

```yaml
name: postgresdb
version: v2alpha
type: depot
layer: user
depot:
  type: JDBC                  
  description: postgresql database connection
  external: true
  secrets:
    - name: postgresdb-r
      allkeys: true

    - name: postgresdb-rw
      allkeys: true
  postgresql:                        
    subprotocol: "postgresql"
    host: host
    port: port
    database: postgres
    params: #Required 
      sslmode: disable
```