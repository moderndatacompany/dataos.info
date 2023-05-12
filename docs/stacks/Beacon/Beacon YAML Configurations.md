# Beacon YAML Configurations

## Structure of a Beacon Service YAML

```yaml
# PRIMITIVE/RESOURCE SECTION

version: v1 # Version
name: beacon-service # Name of the Service (Resource)
type: service # Type of Resource (Here its a Service)
service:
	# ...
	# ...
	# ... 
  stack: beacon+rest/beacon+graphql   # Stack (Here it's Beacon)
	envs:
    PGRST_OPENAPI_SERVER_PROXY_URI: https://<dataos-context>/sampledb/api/v2

# BEACON STACK SECTION
  beacon:
    source: # Database
      type: database # Resource Type (Database)
      name: retail01 # Name should match the Database resource name
      workspace: public # Workspace name
	  topology: # Topology
	  - name: database # What's this?
	    type: input
	    doc: retail database connection
	  - name: graphql-api
	    type: output
	    doc: serves up the retail database as a GraphQL API
	    dependencies:
	    - database
```

## Primitive/Resource Section

At the core of any Beacon Service lies the Service Primitive/Resource Section, which is responsible for defining a Service Primitive/Resource through a set of YAML fields and configurations. The Service component defines a persistent process that either receives or delivers API requests. The Beacon stack is then invoked within the Service to effectuate the exposition of Postgres API. For a deeper understanding of Services and their associated YAML configurations, please refer to the following page:
[Service](./../../Primitives/Service/Service.md)

### Environment Variables

While creating a Beacon Service with a `beacon+rest` stack, you need to specify the environment variable `PGRST_OPENAPI_SERVER_PROXY_URI` given below:

```yaml
envs:
  PGRST_OPENAPI_SERVER_PROXY_URI: https://<dataos-context>/sampledb/api/v2
# Replace the <dataos-context> with your DataOS Full Context Name
```

## Beacon Stack Section

### `source`

The Source section contains fields for the data source

```yaml
source:
  type: database
  name: retail01 # Name of the source
  workspace: public # Name of the workspace
```

`type`

The type of source. This field is mandatory.

Default Value: ‘’

Possible Value: database

Field Type: Mandatory

---

`name`

The name of the data source.

Default Value: ‘’

Possible Value: Any name that follows the regex.

Field Type: Mandatory

---

`workspace`

The DataOS workspace where the source exists.

Default Value: public

Possible Value: Any available workspace within DataOS

Field Type: Mandatory

---

### `topology`

Topology refers to the physical or logical arrangement of the different components of a PostgreSQL system, such as inputs, outputs, etc.

```yaml
topology:
- name: database # Topology Name
  type: input # Type
  doc: retail database connection # Doc 
- name: graphql-api # Topology Name
  type: output # What are the possible values within the type section
  doc: serves up the retail database as a GraphQL API # Doc
  dependencies: # Dependencies
  - database
```

`name`

Name of a particular topology.

Type: String

Default Value: ‘’

Possible Value: Any string

---

`type`

Type of topology.

Type: String

Default Value: ‘’

Possible Value: input/output 

---

`doc`

This field is to document the steps done in this step

Type: String

Default Value: ‘’

Possible Value: Any string

---

`dependencies`

This field is used to define the dependencies between steps.

Type: String

Default Value: ‘’

Possible Value: Any step name within the topology