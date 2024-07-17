# Data Product Developer Journey

Data Product Developers are responsible for creating and managing data products within DataOS. They design, build, and maintain the data infrastructure and pipelines, ensuring the data is accurate, reliable, and accessible.

A Data product developer is typically responsible for the following activities.

## Understand Data Needs

1. Gather and understand the business requirements and objectives for the data pipeline.

2. Get the required access rights to build and run data movement workflows.


## Understanding Data Assets

Data developers need to identify and evaluate the data sources to be integrated (databases, APIs, flat files, etc.) and determine each source's data formats, structures, and protocols. DataOS Metis can help you understand these details.


1. Login to DataOS and go to Metis app.
    
    ![dataoshome_metis.png](/getting_started/dataoshome_metis.png)
    
2. Go to **Assets** tab. Enter a search string to find your data asset quickly.
    
    ![assets_metis.png](/getting_started/assets_metis.png)
    
3. You can also apply filters to find your data asset.
    
    ![dataset_filtered.png](/getting_started/dataset_filtered.png)
    
4. Click on the dataset for details such as schema and columns.
    
    ![dataset_details.png](/getting_started/dataset_details.png)

5. You can further explore the data asset by looking at its data and writing queries. Metis enables you to open the data asset in Workbench.

## Performing Exploratory Data Analysis (EDA)

1. Open the data asset in the Workbench app.
    
    ![dataoshome_workbench.png](/getting_started/dataoshome_workbench.png)
    
2. Select a Cluster to run your queries.
    
    ![selct_cluster.png](/getting_started/selct_cluster.png)
    
3. Select catalog, schema, and table.
    
    ![select_catalog.png](/getting_started/select_catalog.png)
    
4. Write and run queries. 
    
    ![workbench_query.png](/getting_started/workbench_query.png)
    
    Workbench also provides a Studio feature. Whether you're a seasoned SQL pro or just getting started, Studio's intuitive interface will help you craft powerful SQL statements with ease.
    
## Define Data Architecture

1. Design the overall data architecture, including data flow, storage, and processing.

2. Develop a detailed plan outlining the transformation steps and processes for building the data pipeline.

3. Provision and configure the necessary infrastructure and computing resources.


## Build Pipeline for Data Movement

1. Write YAML for the Data Processing Workflow as per the requirement. In the YAML, you need to specify input and output locations as depot addresses—contact the DataOS operator for this information.

2. Specify the DataOS processing Stack you are using for your Workflow.

The following example YAML code demonstrates the various sections of the Workflow.

```yaml
version: v1
name: wf-sports-test-customer       # Workflow name
type: workflow
tags:  
  - customer
description: Workflow to ingest sports_data customer csv
workflow:  
  title: customer csv 
  dag:    
    - name: sports-test-customer
      title: sports_data Dag
      description: This job ingests customer csv from Azure blob storage into icebase catalog 
        tags:         
          - customer    
        stack: flare:4.0        
        compute: runnable-default
        flare:         
          job:            
            explain: true            
            inputs:                                
              - name: sports_data_customer                                                                                              
                dataset: dataos://azureexternal01:sports_data/customers/
                format: CSV
                options:
                  inferSchema : true
  
            logLevel: INFO

            steps:              
              - sequence:                  
                - name: customer                           # Reading columns from definition files.File names is used to create Survey Ids                    
                  sql: > 
                    SELECT *
                    from sports_data_customer   
                  functions: 
                      - name: cleanse_column_names

                      # - name: change_column_case 
                      #   case: lower

                      - name: find_and_replace 
                        column: annual_income
                        sedExpression: "s/[$]//g"

                      - name: find_and_replace 
                        column: annual_income
                        sedExpression: "s/,//g"

                      - name: set_type 
                        columns: 
                          customer_key: int 
                          annual_income: int
                          total_children: int

                      - name: any_date 
                        column: birth_date
                        asColumn: birth_date

                                                 
            outputs:              
              - name: customer
                dataset: dataos://icebase:sports/sample_customer?acl=rw
                format: Iceberg
                title: sports_data
                description: this dataset contains customer csv from sports_data 
                tags:                                                                     
                  - customer
                options:                  
                  saveMode: overwrite

```
## Run the Workflow 

1. You need to run this Workflow by using the *apply* command on DataOS CLI.

2. Using DataOS CLI commands, you can check the runtime information of this Workflow.

3. Once completed, you can check the output data asset on Metis.

Please note that this workflow will be part of the data product bundle. 

Click [here](/resources/stacks/flare/), to access the comprehensive DataOS Resource specific documentaion on dataos.info. 

Explore the rich set of DataOS resources, which serve as the building blocks for data products and processing stacks. Additionally, refer to the learning assets to master the required proficiency level for the role of data product developer.