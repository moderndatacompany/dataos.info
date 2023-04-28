# **BigQuery**

DataOS allows you to create a Depot of type 'BIGQUERY' to read the data stored in the BigQuery projects. You can create several Depots, each pointing to a different project.

## **Requirements**

To connect to BigQuery, you need:

- Project id
- Email id
- Credential properties in JSON file
- Additional parameters

## **Template**

To create a Depot of type 'BIGQUERY', use the following template:

```yaml
version: v1
name: <depot-name>
type: depot
tags:
  - dropzone
  - bigquery
owner: <owner-name>
layer: user
depot:
  type: BIGQUERY                  **# Depot type**
  description: <description>
  external: true
  connectionSecret:               **# Data source specific configurations**
    - acl: rw
      type: key-value-properties
      data:
        projectid: <project-name>
        email: <email-id>
      files:
        json_keyfile: <json-file-path>
    - acl: r
      type: key-value-properties
      data:
        projectid: <project-name>
        email: <email-id>
      files:
        json_keyfile: <json-file-path>
  spec:                            **# Data source specific configurations**
    project: <project-name>
    params:
      "key1": "value1"
      "key2": "value2"
```

The json file should contain the following details:

```json
#fill up all the blanks within quotes
{
    "type": " ", 
    "project_id": " ",
    "private_key_id": " ",
    "private_key": " ",
    "client_email": " ",
    "client_id": " ",
    "auth_uri": " ",
    "token_uri": " ",
    "auth_provider_x509_cert_url": " ",
    "client_x509_cert_url": " "
  }
```