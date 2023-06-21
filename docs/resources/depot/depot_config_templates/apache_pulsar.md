# Apache Pulsar


DataOS allows you to create a Depot of type 'PULSAR' to read the topics/messages stored in Pulsar. The created Depot enables you to read the published topics and process incoming stream of messages.

## Requirements

To connect to Pulsar, you need:

- Admin URL
- Service URL

## Template

To create a Depot of type ‘PULSAR‘, use the following template:

```yaml
version: v1
name: <depot-name>
type: depot
tags:
  - <tag1>
  - <tag2>
owner: <owner-name>
layer: user
depot:
  type: PULSAR       **# Depot type**
  description: <description>
  external: true
  spec:              **# Data source specific configurations**
    adminUrl: <admin-url>
    serviceUrl: <service-url>
    tenant: <system> 
#you can get the tenant name and other specifications from your organisation
```