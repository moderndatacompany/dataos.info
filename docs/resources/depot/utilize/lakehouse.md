# Depot as Lakehouse

Whenever a user ingests the data, it gets stored in the DataOS Lakehouse. To know more about the Lakehouse, please refer [to this link.](/resources/lakehouse/)

**For example:**

A company in the e-commerce sector looking to analyze user behavior data across multiple platforms. The company collects large volumes of raw, unstructured user interaction data (clicks, browsing history, and purchase patterns) in a data lake. However, the marketing team requires structured, real-time insights for personalized advertising and targeting. To meet this need, the company implements the DataOS Lakehouse. They store the raw data in a cloud-based object storage system like AWS S3, but instead of working directly with the unstructured data, the team uses Apache Iceberg as a unified data format that allows both structured and unstructured data to be queried efficiently. The data is structured through a metastore, which ensures consistency and fast access for analysis. The team can now run complex queries and data processing pipelines for machine learning models to predict future customer behavior, while still being able to handle large-scale data storage and data processing in a scalable, efficient manner. This setup allows the business to have real-time analytics and long-term insights from the same data store.

The below manifest file defines the `alphaomega` Lakehouse, which operates on the `Iceberg` format and is hosted on `Azure`. The storage layer is managed through an `S3`-based lakehouse Depot, utilizing the `dataos-lakehouse` bucket with a relative path of `/test`. Access control is configured via secrets for read (`alphaomega-r`) and read-write (`alphaomega-rw`) permissions. The Lakehouse employs an `Iceberg REST Catalog` as its metastore for data management and utilizes `Themis` as the query engine.

```yaml
# Resource-meta section 
name: alphaomega
version: v1alpha
type: lakehouse
tags:
    - Iceberg
    - Azure
description: lakehouse depot of storage-type S3
owner: iamgroot
layer: user

# Lakehouse-specific section 
lakehouse:
    type: iceberg
    compute: runnable-default
    iceberg:

    # Storage section 
    storage:
        depotName: alphaomega
        type: s3
        s3:
        bucket: dataos-lakehouse   
        relativePath: /test
        secrets:
        - name: alphaomega-r
            keys:
            - alphaomega-r
            allkeys: true 
        - name: alphaomega-rw
            keys:
            - alphaomega-rw
            allkeys: true  

    # Metastore section 
    metastore:
        type: "iceberg-rest-catalog"

    # Query engine section 
    queryEngine:
        type: themis
```
