# Apache Pulsar

DataOS provides the capability to create a Depot of type 'PULSAR' for reading topics and messages stored in Pulsar. This Depot facilitates the consumption of published topics and processing of incoming streams of messages.

## Requirements

To establish a connection with Pulsar, the following information is required:

- Admin URL
- Service URL

## Template

To create a Depot of type 'PULSAR,' utilize the following template:

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
  type: PULSAR       
  description: {{description}}
  external: {{true}}
  spec:              
    adminUrl: {{admin-url}}
    serviceUrl: {{service-url}}
    tenant: {{system}}
# Ensure to obtain the correct tenant name and other specifications from your organization.
```