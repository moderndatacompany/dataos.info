# Data Product Owner Journey

Data product owners are responsible for managing stakeholder expectations, and ensuring alignment with business goals through clear roadmaps for actionable solution. They coolaborate with stakeholders to priritize requirements, define the specifications and quality expectations. They understand both the business and the technology landscape.

Once clear goals and objectives for the data product are established, including identifying the business problems it will address, the value it will provide, and how it will be consumed, data owners carry out the following activities on DataOS:

Following are the activities carried out by Data product owner on DataOS.

## Introspect Existing Data Ecosystem 

This is to identify data assets adhering to the expectations.

1. Login to DataOS and go to Metis app.
    
    ![dataoshome_metis.png](/getting_started/dataoshome_metis.png)
    
2. Go to **Assets** tab. Enter search string to quickly find your data asset.
    
    ![assets_metis.png](/getting_started/assets_metis.png)
    
3. Find your data asset.
    
    ![dataset_filtered.png](/getting_started/dataset_filtered.png)
    
4. Click on the dataset to see its details such as schema, columns. 
    
    ![dataset_details.png](/getting_started/dataset_details.png)
   
5. Metis allows to explore its lineage to understand its data journey. You can also view its profiling information and know the quality. 
   
   ![dataset_details.png](/getting_started/data_product_owner/lineage.png)

## Explore Data

1. You can launch Workbench app from Metis interface to explore the specofic data asset.

   ![dataset_details.png](/getting_started/data_product_owner/explore_workbench.png)

2. Run the queries to understand data.

   ![dataset_details.png](/getting_started/data_product_owner/query_workbench.png)


## Create Data Product Specifications

Broadly, Data Product specification can be broken down into four aspects - Input, Transformation, SLOs and Output. These specifications are given in the Data Product manifest file (YAML format).

1. **Input**: The input aspect of a Data Product focuses on the technical mechanisms for data access or ingestion, such as APIs, streaming, connectors, and batch processes. These components enable the Data Product to acquire data from various sources, ensuring seamless and reliable data flow into the system for further processing and analysis.

2. **Transformation**: The transformation aspect of a Data Product involves the processing and manipulating of data within the product. This may include data cleansing, enrichment, aggregation, normalisation, or any other data transformations required to make the valuable data for analysis and consumption, which meets the desired format, structure, and quality. Transformation is defined as resources using DataOS Flare, Benthos, Lens and Alpha stacks.  

3. **SLOs**: SLOs define the performance, availability, accessibility, and quality targets a Data Product aims to achieve. These objectives ensure that the Data Product meets the required service levels regarding quality and governance. SLOs may include success metrics defined on business, metadata and operations data.  Monitoring and managing SLOs help ensure that the Data Product performs optimally and meets the expectations of its consumers. SLOs are defined using DataOS resources like Policy, Monitor and Pager.
 
4. **Output**: The output aspect of a Data Product refers to the results or outcomes generated from the data analysis and processing. This includes the table, stream, APIs, visualisations, or web app delivered to the data consumers. Define the logical representation of the outcome. DataOS Depots, Lens, APIs, Streamlit App, JDBC ports etc., are supported. 

The following example illustrates the manifest file for a data product created for Website Performance Analysis, marketing Campaign Optimization and Personalized Customer Experience. On the basis of this specification, data product developer will create the resources which are mentioned in the spec file.


```yaml
name: google-analytics
version: v1alpha
entity: product
type: data
tags:
  - data-product
  - Type.3rd Party Data Product
  - Domain.Customer Service
description: This Data Product contains Google Analytics data that cater to Website Performance Analysis, marketing Campaign Optimization and Personalized Customer Experience.
purpose: This data product is intended to provide insights into the google analytics sample data.
collaborators:
  - loki
refs:
  - title: 'Data Product Hub'
    href: https://liberal-donkey.dataos.app/dph/data-products/all

v1alpha:
  data:
    useCases:
      - analysis

    resources:
      - description: 'Depot for establishing data source connection with snowflake'
        purpose: connect with snowflake
        refType: dataos
        type: depot
        version: v1
        name: snowflake09

      - description: 'Scan metadata from snowflake depot'
        purpose: to check metadata in metis 
        refType: dataos
        type: workflow
        version: v1
        name: scanner-newdepot09
        workspace: public

      - description: 'Flare job to write data from snowflake to icebase'
        purpose: to write data from snowflake to icebase 
        refType: dataos
        type: workflow
        version: v1
        name: wf-sample-data-testing09
        workspace: public

      - description: 'Data quality checks to determine whether the output data mets the quality checks or not'
        purpose: to know about the quality of output data 
        refType: dataos
        type: workflow
        version: v1
        name: soda-workflow09
        workspace: public

      - description: 'Masking monetoryrownumber column'
        purpose: to mask a column
        refType: dataos
        type: policy
        version: v1
        name: bucketage09
        workspace: public    

    inputs:
      - description: Snowflake contains google analytics data 
        purpose: source
        refType: dataos
        ref: dataos://snowflake01:PUBLIC/GA

    outputs:
      - description: Processed data
        purpose: consumption
        refType: dataos_address
        ref: dataos://icebase:sandbox/google_analytics09
```