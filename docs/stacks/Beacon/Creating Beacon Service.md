# Creating Beacon Service

## Prerequisites

### Apply the Adequate Access Policy or Assign the Use Case

Make sure you have an adequate access policy to create a Service. If you don’t have one, refer to the section below:

> 🗣 To apply the access policy, you will require operator-level access or `roles:id:operator`. Contact the administrator within your organization to get the requisite access.


### Required Database exists

Make sure that you have an active Database Primitive/Resource within DataOS, as per the schema you require, in case you don’t have it, navigate to the link below to create one. If you have one, navigate to the next step.

## Let’s Begin!

### Step 1: Create a Benthos Service YAML

To commence the process, we will be creating a Beacon Service YAML that will encompass several essential components. Each of these sections has been elaborated in detail on the various configurations page. The YAML Configuration is provided below:

```yaml
# PRIMITIVE/RESOURCE SECTION
version: v1 # Manifest Version
name: stores-db # Name of the Resource/Primitive
type: service # Type of Resource (Here its a Service)
tags: # Tags for the Resource
  - syndicate
  - service
service: # Service Section
  replicas: 2 # Replicas
  ingress: # Ingress Section
    enabled: true # Enables Ingress Port
    stripPath: true # Strip Path and then forward the request to the upstream service.
    path: /stores/api/v1 # Path. How your URL is going to appear?
    noAuthentication: true # If true, there is no Authentication
  stack: beacon+rest # Stack (here the flavor is rest)
  envs: # Environment Variable
    PGRST_OPENAPI_SERVER_PROXY_URI: https://<dataos-context>.dataos.app/<database-path> # e.g. https://adapting-spaniel.dataos.app/citybase/api/v1/

# BEACON STACK SECTION
  beacon: 
    source: # Source Section
      type: database # Source Type
      name: storesdb # Source Name
      workspace: public # Workspace
  topology: # Topology Section
  - name: database # Topology Name
    type: input # Topology Type
    doc: stores database connection # Document of the Topology step
  - name: rest-api # Toplogy Name
    type: output # Topology Type
    doc: serves up the stores database as a RESTful API # Document of the Topology step
    dependencies: # Dependency
    - database # Topology step 2 is dependent on step 1
```

### Step 2: Apply the YAML file

You can apply the YAML file to create a Service resource within the DataOS environment using the command given below:

```bash
dataos-ctl apply -f <path-of-the-config-file> -w <workspace>
```

### Step 3: Check Run time

```bash
dataos-ctl -t service -w <workspace> -n <service-name>  get runtime -r
# Sample
dataos-ctl -t service -w public -n pulsar-random  get runtime -r
```