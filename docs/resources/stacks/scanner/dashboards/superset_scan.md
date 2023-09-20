# Superset

Metadata can be retrieved from Superset dashboards using non-depot Scanner workflows. In this document, you'll discover the prerequisites and YAML configurations necessary to establish a connection with Superset and extract metadata from your dashboards.


## Requirements

To scan the metadata from Superset, you need the following:

- Database Connection: To extract metadata from Superset via MySQL or Postgres database, database user must have at least SELECT priviledge on dashboards & slices tables within of superset schema.

> The metadata extraction also works with Superset 2.0.0 🎉

## Non-Depot Scan Workflow

First, you need to provide source connection details to connect with the dashboard service. Once connected, you can provide configuration settings, such as metadata type and filter patterns to include/exclude assets for metadata scanning. 

### **Scanner Configuration Properties**

- **Type**: Data source type; `superset`
- **Source**: Provide source name where the scanned metadata is saved within Metastore. Under the given source name, you can see the information about all the entities scanned for your data source; `superset08`

#### **sourceConnection Properties**

**For Superset connection**:
- **Host and Port**: Host and port of the Superset instance. 

**For Postgres Connection**
- **Type**: This depends on the underlying data source;`Postgres`
- **Username**: Postgres user name. It can be seen from .env-non-dev;`superset`                    
- **Password**: Postgres password;`superset`                   
- **Host and Port**: Fully qualified hostname and port number for your Postgres deployment (postgres is hosted using ngrok); `0.tcp.in.ngrok.io:10672`      
- **Database**: Name of database associated with Superset instance


#### **sourceConfig Properties**
- **Type**: This is type of the source  to be scanned: `dashboardmetadata`
- **Filter Patterns**: To control the metadata scan for the desired entities: `dashboardFilterPattern`, `chartFilterPattern`

**Non-Depot Scan Workflow YAML**

In this example, sample source connection and configuration settings are provided.

```yaml
version: v1
name: superset-scanner-wf
type: workflow
tags:
  - postgres
description: DashboardMetadata
workflow:
  dag:
    - name: wf-scan-superset
      description: DashboardMetadata
      spec:
        tags:
          - scanner
        stack: scanner:2.0
        runAsUser: metis
        compute: runnable-default
        scanner:
          type: superset
          source: superset08     # can be given anything by your choice
          sourceConnection:
            config:
              type: Superset
              hostPort: {{host_url}}          # This is where Superset is hosted
              connection:
                type: Postgres
                username: superset                    # postgres db name. can be seen from .env-non-dev
                password: superset                    # postgres password
                hostPort: 0.tcp.in.ngrok.io:10672     # postgres is hosted using ngrok 
                database: superset                    # postgres database
          sourceConfig:
            config:
              type: DashboardMetadata 
              chartFilterPattern: {}
              dashboardFilterPattern: {}
```

> After the successful workflow run, you can check the metadata of scanned dashboards on Metis UI.
