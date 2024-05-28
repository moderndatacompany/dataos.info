# Exposing GraphQL API’s on Database using Beacon

This recipe/case scenario exposes a GraphQL API using the `beacon+graphql` stack on `retail101` database.

## Code Snippet

```yaml
version: v1
name: retail
type: service
tags:
  - syndicate
  - retail
  - service
service:
  replicas: 2
  ingress:
    enabled: true
    stripPath: false
    path: /retail/api/v1
    noAuthentication: true
  stack: beacon+graphql
  beacon:
    source:
      type: database
      name: retail01
      workspace: public
	  topology:
	  - name: database
	    type: input
	    doc: retail database connection
	  - name: graphql-api
	    type: output
	    doc: serves up the retail database as a GraphQL API
	    dependencies:
	    - database
```