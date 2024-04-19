# Exposing REST API’s on Database using Beacon

## Code Snippet 1

This recipe exposes a REST API using a Beacon Service on top of `retail101` database.

```yaml
version: v1
name: retail-rest
type: service
tags:
  - syndicate
  - retail
  - service
service:
  replicas: 2
  ingress:
    enabled: true
    stripPath: true
    path: /retail/api/rest
    noAuthentication: true
  stack: beacon+rest
  beacon:
    source:
      type: database
      name: retail001
      workspace: public
  topology:
  - name: database
    type: input
    doc: retail database connection
  - name: rest-api
    type: output
    doc: serves up the retail database as a RESTful API
    dependencies:
    - database
```

## Code Snippet 2

This recipe exposes a REST API using a Beacon Service on top of `searchapppoc` database.

```yaml
version: v1
name: searchapppoc-rest-01
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
    path: /searchapppoc/api/v1
    noAuthentication: true
  stack: beacon+rest
  envs:
    PGRST_OPENAPI_SERVER_PROXY_URI: https://newly-uncommon-goat.dataos.io/searchapppoc/api/v1
  beacon:
    source:
      type: database
      name: searchapppoc
      workspace: public
  topology:
  - name: database
    type: input
    doc: searchapppoc database connection
  - name: rest-api
    type: output
    doc: serves up the searchapppoc database as a RESTful API
    dependencies:
    - database
```

## Code Snippet 3

This recipe exposes a REST API using a Beacon Service on top of `partsearchdb` database.

```yaml
version: v1
name: part-search-data
type: service
tags:
  - syndicate
  - service
service:
  replicas: 2
  ingress:
    enabled: true
    stripPath: true
    path: /partsearch/api/v1
    noAuthentication: true
  stack: beacon+rest
  envs:
    PGRST_OPENAPI_SERVER_PROXY_URI: https://af-grh.dataos.io/partsearch/api/v1
  beacon:
    source:
      type: database
      name: partsearchdb
      workspace: public
  topology:
  - name: database
    type: input
    doc: part search database connection
  - name: rest-api
    type: output
    doc: serves up the part search database as a RESTFUL API
    dependencies:
    - database
```

## Code Snippet 4

This recipe exposes a REST API using a Beacon Service on top of `segmentsearchapp` database.

```yaml
version: v1
name: searchsegmentapp-rest
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
    path: /searchsegmentapp/api/v1
    noAuthentication: true
  stack: beacon+rest
  envs:
    PGRST_OPENAPI_SERVER_PROXY_URI: https://newly-uncommon-goat.dataos.io/searchsegmentapp/api/v1
  beacon:
    source:
      type: database
      name: segmentsearchapp
      workspace: public
  topology:
  - name: database
    type: input
    doc: segmentsearchapp database connection
  - name: rest-api
    type: output
    doc: serves up the segmentsearchapp database as a RESTful API
    dependencies:
    - database
```

## Code Snippet 5

This recipe exposes a REST API using a Beacon Service on top of `storesdb` database.

```yaml
version: v1
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

## Code Snippet 6

This recipe exposes a REST API using a Beacon Service on top of `segmentapp` database.

```yaml
version: v1
name: segmentapp-rest
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
    path: /segmentapp/api/v1
    noAuthentication: true
  stack: beacon+rest
  envs:
    PGRST_OPENAPI_SERVER_PROXY_URI: https://{{.CloudKernel.PublicFqdn.Value}}/segmentapp/api/v1
  beacon:
    source:
      type: database
      name: segmentapp
      workspace: public
  topology:
  - name: database
    type: input
    doc: segmentapp database connection
  - name: rest-api
    type: output
    doc: serves up the segmentapp database as a RESTful API
    dependencies:
    - database
```