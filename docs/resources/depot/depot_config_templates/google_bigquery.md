# BigQuery

DataOS enables the creation of a Depot of type 'BIGQUERY' to read data stored in BigQuery projects. Multiple Depots can be created, each pointing to a different project.

## Requirements

To establish a connection with BigQuery, the following information is required:

- Project ID: The identifier of the BigQuery project.
- Email ID: The email address associated with the BigQuery project.
- Credential properties in JSON file: A JSON file containing the necessary credential properties.
- Additional parameters: Any additional parameters required for the connection.

## Template

To create a Depot of type 'BIGQUERY', utilize the following template:

```yaml
name: {{depot-name}}
version: v1
type: depot
tags:
  - {{dropzone}}
  - {{bigquery}}
owner: {{owner-name}}
layer: user
depot:
  type: BIGQUERY                 
  description: {{description}}
  external: {{true}}
  connectionSecret:            
    - acl: rw
      type: key-value-properties
      data:
        projectid: {{project-name}}
        email: {{email-id}}
      files:
        json_keyfile: {{json-file-path}}
    - acl: r
      type: key-value-properties
      data:
        projectid: {{project-name}}
        email: {{email-id}}
      files:
        json_keyfile: {{json-file-path}}
  spec:                           
    project: {{project-name}}
    params:
      {{"key1": "value1"}}
      {{"key2": "value2"}}
```

Ensure that the JSON file used for the credential properties includes the necessary details as specified in the template below.

```json
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