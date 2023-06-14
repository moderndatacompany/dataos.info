# BigQuery

You can scan metadata from BigQuery with depot/non depot Scanner workflows. In this document, find requirements and YAML configurations to connect to BigQuery for extracting entity metadata. 

## Requirements

To scan the metadata from BigQuery, you need the following:

1. Ensure that the BigQuery project is created.
2. BigQuery user must have`viewer` privilege on the warehouse. 
3. You should have enough access to fetch the required metadata. The following list describes the minimum required permissions.

|  | GCP Permission | GCP Role | Required For |
| --- | --- | --- | --- |
| 1 | bigquery.datasets.get | BigQuery Data Viewer | Metadata Ingestion |
| 2 | bigquery.tables.get | BigQuery Data Viewer | Metadata Ingestion |
| 3 | bigquery.tables.getData | BigQuery Data Viewer | Metadata Ingestion |
| 4 | bigquery.tables.list | BigQuery Data Viewer | Metadata Ingestion |
| 5 | resourcemanager.projects.get | BigQuery Data Viewer | Metadata Ingestion |
| 6 | bigquery.jobs.create | BigQuery Job User | Metadata Ingestion |
| 7 | bigquery.jobs.listAll | BigQuery Job User | Metadata Ingestion |

## Depot Scan Workflow

DataOS allows you to create a depot of type 'BIGQUERY' to read the data stored in the BigQuery projects. You can create several depots, each pointing to a different project. The following YAML scans metadata from a BigQuery-type depot. 

<aside>
🗣 Ensure that the depot is created and you have `read` access for the depot.

</aside>

### Depot Scan Workflow YAML

```yaml
version: v1
name: wf-bigquery-depot
type: workflow
tags:
  - bigquery-depot
description: The workflow scans schema tables and register data
workflow:
  dag:
    - name: bigquery-depot
      description: The job scans schema from bigquery-depot tables and register data to metis2
      spec:
        tags:
          - scanner
        stack: scanner:2.0
        compute: runnable-default
        runAsUser: metis
        scanner:
          depot: demoprepbq           
          sourceConfig:           
            config:
              markDeletedTables: false
              includeTables: true
              includeViews: true
              databaseFilterPattern:
                includes:
                  - <databasename> 
                excludes:
                  - <databasename> 
              schemaFilterPattern:
                includes:
                  - <schemaname>
                excludes:
                  - <schemaname>
              tableFilterPattern:
                includes:
                  - <schemaname>
                excludes:
                  - <schemaname>

```

## Non-Depot Scan Workflow

You need to provide source connection details and configuration settings, such as metadata type and filter patterns to include/exclude assets for metadata scanning. 

### Scanner Configuration **Properties**

- **Type**: This is type of the source  to be scanned; `bigquery`
- **Source**: Provide source name where the scanned metadata is saved within Metastore. Under the given source name, you can see the information about all the entities scanned for your data source; `BigQuerySource_ND`

### Source **Connection Properties**

**hostPort**: BigQuery APIs URL. By default the API URL is `bigquery.googleapis.com` you can modify this if you have custom implementation of BigQuery.

**credentials**: You can authenticate with your bigquery instance using either `GCS Credentials Path` where you can specify the file path of the service account key or you can pass the values directly by choosing the `GCS Credentials Values` from the service account key file.

You can checkout **[this](https://cloud.google.com/iam/docs/keys-create-delete#iam-service-account-keys-create-console)** documentation on how to create the service account keys and download it.

**gcsConfig:**

**1.** Passing the raw credential values provided by BigQuery. This requires us to provide the following information, all provided by BigQuery. You can fetch the associated values for each of them from the BigQuery account files.

- **type**: Credentials Type is the type of the account.
- **projectId**: A project ID is a unique string used to differentiate your project from all others in Google Cloud. You can also pass multiple project id to ingest metadata from different BigQuery projects into one service.
- **privateKeyId**: This is a unique identifier for the private key associated with the BigQuery account.
- **privateKey**: This is the private key associated with the service account that is used to authenticate and authorize access to BigQuery.
    
    <aside>
    🗣 While providing private key, divide every \n to new line  between BEGIN & END PRIVATE KEY as shown in the example below.
    
    </aside>
    
- **clientEmail**: This is the email address associated with the service account.
- **clientId**: This is a unique identifier for the service account.
- **authUri**: This is the URI for the authorization server. To fetch this key, look for the value associated with the `auth_uri` key in the service account key file. The default value to Auth URI is https://accounts.google.com/o/oauth2/auth.
- **tokenUri**: The Google Cloud Token URI is a specific endpoint used to obtain an OAuth 2.0 access token from the Google Cloud IAM service. This token allows you to authenticate and access various Google Cloud resources and APIs that require authorization. To fetch this key, look for the value associated with the `token_uri` key in the service account credentials file. Default Value to Token URI is https://oauth2.googleapis.com/token.
- **authProviderX509CertUrl**: This is the URL of the certificate that verifies the authenticity of the authorization server. To fetch this key, look for the value associated with the `auth_provider_x509_cert_url` key in the BigQuery account key file. The Default value for Auth Provider X509Cert URL is https://www.googleapis.com/oauth2/v1/certs
- **clientX509CertUrl**: This is the URL of the certificate that verifies the authenticity of the service account.

**2.** Passing a local file path that contains the credentials:

- **gcsCredentialsPath**
    
    If you prefer to pass the credentials file, you can do so as follows:
    
    ```yaml
    credentials:
      gcsConfig: <path to file>
    ```
    

### Non-Depot Scan Workflow YAML

In this example, sample source connection and configuration settings are provided.

```yaml
version: v1
name: bigquery-scanner2
type: workflow
tags:
  - bigquery-non-depot
description: The workflow scans schema tables and registers metadata
workflow:
  dag:
    - name: bigquery-scanner2
      description: The job scans schema from bigquery via Non-depot tables and register metadata to metis
      spec:
        tags:
          - scanner2.0
        stack: scanner:2.0
        compute: runnable-default
				runAsUser: metis
        scanner:
          type: bigquery
          source: BigQuerySource_ND
          sourceConnection:
            config:
              type: BigQuery
              credentials:
                gcsConfig:
                  type: <account type>
                  projectId: project ID # ["project-id-1", "project-id-2"]
                  privateKeyId: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                  privateKey: |                              # divide every \n to new line  between BEGIN & END PRIVATE KEY
                          -----BEGIN PRIVATE KEY-----
                          xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
													xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                          xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
													xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
													xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
													xxxxxxxxxxxxxxxxxxxx
                          -----END PRIVATE KEY-----
                  clientEmail: client@mail.com
                  clientId: 123456
                  # authUri: https://accounts.google.com/o/oauth2/auth (default)
                  # tokenUri: https://oauth2.googleapis.com/token (default)
                  # authProviderX509CertUrl: https://www.googleapis.com/oauth2/v1/certs (default)
                  clientX509CertUrl: https://cert.url
          sourceConfig:
            config:             # Use them as per requirement
              markDeletedTables: false
              includeTables: true
              includeViews: true
              databaseFilterPattern:
                includes:
                  - <databasename> 
                excludes:
                  - <databasename> 
              schemaFilterPattern:
                includes:
                  - <schemaname>
                excludes:
                  - <schemaname>
              tableFilterPattern:
                includes:
                  - <schemaname>
                excludes:
                  - <schemaname>
```

> After the successful workflow run, you can check the metadata of scanned Tables on Metis UI.
>