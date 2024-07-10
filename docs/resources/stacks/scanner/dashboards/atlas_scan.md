# Atlas

You can scan metadata from Atlas for a dashboard with non-depot Scanner workflows. In this document, find requirements and YAML configurations to connect to Atlas for extracting metadata for the created dashboards. 

## Requirements

To scan the metadata from Atlas, you need the following:

- Atlas API key

> To obtain an Atlas API key, log in to Atlas. Once logged in, navigate to the <b>Profile</b> section, where you can access and view your generated API key.


## Non-Depot Scan Workflow

First you need to provide source connection details to connect with the dashboard service. Once connected you can provide configuration settings, such as metadata type and filter patterns to include/exclude assets for metadata scanning. 

### **Scanner Configuration Properties**

- **Type**: This depends on the underlying data source; `redash`
- **Source**: Provide source name where the scanned metadata is saved within Metastore. Under the given source name, you can see the information about all the entities scanned for your data source; `atlas`

#### **sourceConnection Properties**

- **Host Port**: dataOS Atlas url (provide the fully qualified domain name of the DataOS® instance): For example, `https://whole-locust.dataos.app/atlas`
- **API Key**: API key for Atlas. 
- **username**: DataOS username
   

#### **sourceConfig Properties**
- **Type**: This is type of the source  to be scanned: `dashboardmetadata`
- **Filter Patterns**: To control the metadata scan for the desired entities: `dashboardFilterPattern`, `chartFilterPattern`

**Non-Depot Scan Workflow YAML**

In this example, sample source connection and configuration settings are provided.

```yaml
version: v1
name: atlas-scanner-wf
type: workflow
description: Scanner workflow to scan Dashboard Metadata
workflow:
  dag:
    - name: scan-atlas-wf
      description: Job to perform non-depot scan for Dashboard Metadata
      spec:
        tags:
          - scanner
        stack: scanner:2.0
        runAsUser: metis
        compute: runnable-default
        stackSpec:
          source: atlas
          type: redash
          sourceConnection:
            config:
              type: Redash
              hostPort: https://{{DataOS instance}}/atlas
              apiKey: {{atlas_api_key}}          # atlas api key
              username: {{user-name}}          # dataos username
          sourceConfig:
            config:
              type: DashboardMetadata
              dashboardFilterPattern: {}
              chartFilterPattern: {}
```

> After the successful workflow run, you can check the metadata of scanned dashboards on Metis UI.
