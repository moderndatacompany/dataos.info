# Redash

Metadata can be retrieved from Redash dashboards using non-depot Scanner workflows. In this document, you'll discover the prerequisites and YAML configurations necessary to establish a connection with Redash and extract metadata from your dashboards.

## Requirements

To scan the metadata from Redash, you need the following:

- Redash API key


## Non-Depot Scan Workflow

Start by entering your source connection details to connect with the dashboard service. Once connected you can provide configuration settings, such as metadata type and filter patterns to include/exclude assets for metadata scanning. 

### **Scanner Configuration Properties**

- **Type**: This depends on the underlying data source; `redash`
- **Source**: Provide source name where the scanned metadata is saved within Metastore. Under the given source name, you can see the information about all the entities scanned for your data source; `redash03`

#### **sourceConnection Properties**

- **Host Port**: URL to the Redash instance: For example, `https://592a-150-129-144-242.ngrok-free.app`
- **API Key**: API key for Redash. 
- **username**: Redash username
   

#### **sourceConfig Properties**
- **Type**: This is type of the source  to be scanned: `dashboardmetadata`
- **Filter Patterns**: To control the metadata scan for the desired entities: `dashboardFilterPattern`, `chartFilterPattern`

**Non-Depot Scan Workflow YAML**

In this example, sample source connection and configuration settings are provided.

```yaml
version: v1
name: redash-scanner-wf
type: workflow
tags:
  - postgres
description: DashboardMetadata
workflow:
  dag:
    - name: wf-scan-redash
      description: DashboardMetadata
      spec:
        tags:
          - scanner
        stack: scanner:2.0
        runAsUser: metis
        compute: runnable-default
        stackSpec:
          source: redash03
          type: redash
          sourceConnection:
            config:
              type: Redash
              # This host port is URL where Redash is hosted.
              hostPort: {{host_port}} # or http://localhost:5001
              apiKey: {{redash_api_key}}
              username: {{redash_username}}
          sourceConfig:
            config:
              type: DashboardMetadata
              dashboardFilterPattern: {}
              chartFilterPattern: {}
```

> After the successful workflow run, you can check the metadata of scanned Tables on Metis UI.
