# Data Product Owner Journey

Data product owners are in charge of creating and managing data products, making sure they match the organizational objectives and deliver real value. They work with business stakeholders to set the data strategy and vision, aligning company goals with data initiatives and identifying key success metrics. They coolaborate with stakeholders to priritize requirements, define the specifications and quality expectations with clear roadmaps for actionable solutions.

After setting clear goals and objectives for the data product, including identifying the business problems it will solve, the value it will provide, and how it will be used, data owners perform the following activities on DataOS:

Following are the activities carried out by data product owner on DataOS.

## Introspect Existing Data Ecosystem 

This step identifies data assets that adhere to the expectations

1. Login to DataOS and go to Metis app.
    
    ![dataoshome_metis.png](/getting_started/dataoshome_metis.png)
    
2. Go to **Assets** tab. 
    
    ![assets_metis.png](/getting_started/assets_metis.png)
    
3. Enter a search string to find your data asset quickly.
    
    ![dataset_filtered.png](/getting_started/dataset_filtered.png)
    
4. Click on the dataset for details such as schema and columns. 
    
    ![dataset_details.png](/getting_started/dataset_details.png)
   
5. Metis lets you trace the lineage of your data to understand its journey. You can also access profiling information to assess data quality.
   
   ![dataset_details.png](/getting_started/data_product_owner/lineage.png)

## Explore Data

Now for data exploration, you can query the data using the Workbench. DataOS enables you to examine your data without moving it. 

1. You can launch the Workbench app from the Metis interface to explore the specific data asset.

   ![dataset_details.png](/getting_started/data_product_owner/explore_workbench.png)

2. Run the queries to understand data.

   ![dataset_details.png](/getting_started/data_product_owner/query_workbench.png)


## Create Data Product Specifications

The Data Product specification can be divided into four aspects: Input, Transformations, SLOs, and Output. These specifications are given in the data product manifest file (YAML format).

1. **Input**: The input aspect of a data product focuses on the technical mechanisms for data access or ingestion, such as APIs, streaming, connectors, and batch processes. These components enable the Data Product to acquire data from various sources, ensuring seamless and reliable data flow into the system for further processing and analysis.

2. **Transformation**: The transformation aspect of a data product involves processing and manipulating data within the product, which may include data cleansing, enrichment, aggregation, normalization, or any other data transformations required to make valuable data for analysis and consumption that meets the desired format, structure, and quality. Transformation is defined as DataOS Resources like Workflows, Services, and Workers using DataOS Flare, Bento, Lens, and Container Stacks.     

3. **SLOs**: SLOs define the performance, availability, accessibility, and quality targets a Data Product aims to achieve. These objectives ensure that the Data Product meets the required service levels regarding quality and governance. SLOs may include success metrics defined based on business, metadata, and operations data. Monitoring and managing SLOs help ensure that the Data Product performs optimally and meets the expectations of its consumers. SLOs are defined using DataOS Resources like Policy, Monitor, and Pager.
 
4. **Output**: The output aspect of a data product refers to the results or outcomes generated from the data analysis and processing, which includes the table, stream, APIs, visualizations, or web app delivered to the data consumers. Define the logical representation of the outcome. DataOS Depots, Lens, APIs, Streamlit App, JDBC ports, etc., are supported. 

The following example illustrates the manifest file for a data product created for Website Performance Analysis, marketing Campaign Optimization, and Personalized Customer Experience. Based on this specification, the data product developer will create the DataOS Resources mentioned in the spec file.

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