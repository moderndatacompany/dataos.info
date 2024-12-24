# Scanning Metadata 

!!! info "Information"
    Scanning metadata allows for a comprehensive understanding of the source data's structure, which helps in designing and optimizing ETL processes that meet desired use cases and ensure data quality. This guide explains the different ways to scan metadata and provides detailed instructions to perform the metadata scan.

The Scanner stack in DataOS is  designed for developers to extract metadata from external source systems (such as RDBMS, Data Warehouses, Messaging services, Dashboards, etc.) and the components/services within the DataOS environment to extract information about Data products and DataOS Resources. 

## Metadata Extraction Workflows

Within DataOS, different workflows can be deployed and scheduled, which will connect to the data sources to extract metadata.

<div class= "grid cards" markdown>

-   [Depot Scan Workflow](/quick_guides/scan_metadata/depot/)

    ---
    With this type of Scanner workflow, depots are used to get connected to the metadata source to extract Entities’ metadata. It enables you to scan all the datasets referred by a Depot. You need to provide the depot name or address, which will connect to the data source. 
    
-   [Non-Depot Scan Workflow](/quick_guides/scan_metadata/non_depot/)

    ---
    With this type of Scanner workflow, you must provide the connection details and credentials for the underlying metadata source in the YAML file. These connection details depend on the underlying source and may include details such as host URL, project ID, email, etc.

</div>

<aside class="callout">

🗣 The non-Depot scan can help extract metadata from sources where Depot creation is not supported or when you do not have an already created Depot.
</aside>

