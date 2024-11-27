# Creating a Data Product Spec file

After setting up your Bundle manifest, the next step is to define your Data Product Spec file. This file serves as a blueprint for your data product, specifying all the necessary configurations and metadata to ensure smooth deployment and management within DataOS.

## Scenario

Imagine you are building a data product called product360 to analyze purchase behavior, revenue trends, and customer insights. To get started, you need a Data Product Spec file that captures all the essential configurations like inputs, outputs, collaborators, and associated resources. This file will help structure your data product and provide a comprehensive guide for its lifecycle management.

## Step 1: Define general information

This section includes basic details about your data product:


- **Name:** `product360`Identifies the data product name for purchase behaviour analysis. The name cannot contain underscores (_). Names with multiple words can only be punctuated using hyphens(-).
    
    ```yaml
    #Example 1
    name: product360
    
    #Example 2
    name: purchase-behaviour-insights
    ```
    
- **Version:** `v1beta`Indicates the version of the product.
- **Entity:** `product`Classifies the entity as a data product.
- **Type:** `data` Specifies that the product handles data.
- **Purpose:** Defines the objective and impact of the product.
- **Tags:** Tags provide important context for categorizing the data product on the DPH (Data Product Hub). These tags are used to populate three important data points on the DPH UI - `Domain`, `Usecase` and `Tier`
- **Description:** Provides an overview of what the Data Product delivers.
- **Refs**: Include reference links in the DP spec file to add any additional context to the DP.  Provide `title` and link `href`.
    
    The following code snippet shows how the above properties come in spec file is for our example.
    
    ```yaml
    version: v1beta
    entity: product
    type: data
    tags:   
      - DPDomain.product OPS
      - DPUsecase.Purchasing Behaviour Analysis
      - DPTier.Consumer Aligned
    description: Get a comprehensive analysis of important business metrics, including purchase behavior, revenue trends, and customer insights. This analysis helps identify patterns, preferences, and purchasing trends, providing insights into customer segmentation, and personalized marketing strategies.
    refs:
    - title: 'Workspace Info'
      href: https://dataos.info/interfaces/cli/command_reference/#workspace
    ```
    

## Step 2: Add Data Product-specific attributes

This section outlines data product-specific attributes such as Bundle resource, inputs, outputs, and references. All the specific details related to the data product comes under `data` section in spec file.

- **Meta**
    
    Include a `meta` section, nested under the `data` section, to provide additional context and information to DPH.
    
    - The `sourceCodeUrl` key is used to link the associated repository where the DP artefacts are maintained
    - The `trackerUrl` key is used to link the associated JIRA ticket where the DP issues are being managed
        
        ```yaml
        v1beta:
          data:
            meta:
              sourceCodeUrl: https://bitbucket.org/tmdc/cloud-cost-360/src/main/
              title: Cloud Cost 360 # this appears on the UI | If you want to capitalise and format your DP name's appearance on DPH
              trackerUrl: https://rubikai.atlassian.net/browse/DPRB-19?atlOrigin=eyJpIjoiZDVmMDNmYmYxOWYwNGVjZDlhNDdiYTA4NTZmMjg0NTIiLCJwIjoiaiJ9
        ```
        
- **Collaborators**
    
    User IDs of individuals who are collaborating on this data product. You can to add`name` and `description` as additional context to each collaborator under the `data` section in the DP Spec YAML.
    
    ```yaml
    v1beta:
      data:
        meta:
          foo: bar
          sourceCodeUrl: https://github.com/NandaAtModern/dp_product360/tree/master/product360
          trackerUrl: https://rubikai.atlassian.net/browse/DPRB-19?atlOrigin=eyJpIjoiZDVmMDNmYmYxOWYwNGVjZDlhNDdiYTA4NTZmMjg0NTIiLCJwIjoiaiJ9
        collaborators:
          - name: nandapage # name is mandatory
            description: owner # description is optional
          - name: Shraddha
            description: consumer
          - name: kanakgupta
            description: developer
    ```
    
## Step 3: Specify Resource references
    
With a `resource` section, you give a reference to a single **Bundle Resource** which is expected to contain all the DataOS Resources which are part of Data Product. For example, Workflows, Services, Secrets, Policies etc.

This section is crucial to bring every workspace-level resource needed for the DP under one umbrella for lifecycle management and context comprehensive context sharing of the Data Product.

```yaml
resource:
    description: 'Resources associated with product360 Data Product'
    purpose: 'DP Life Cyle Management'
    refType: dataos.                     # mandatory
    ref: bundle:v1beta:product360-bundle. # mandatory | referred Bundle must exist
```
    
## tep 4: Define inputs and outputs
Set up datasets that the data product will consume and produce:
    
There are two types of dataset references - 

- **dataos**: this is used when your dataset is stored in DataOS and has a DataOS address
- **depot**: this can be used when your dataset is stored on a third party system

```yaml
inputs:
    - description: Fetching sales data from the S3 bucket, for comprehensive analysis of sales metrics, providing insights into revenue trends, performance tracking, and decision-making support.
    refType: dataos
    ref: dataset:icebase:sales360mockdb:f_sales

    - description: Pulling customer data from the S3 bucket, for understanding customer demographics, behaviors, preferences and customer segmentation.
    refType: dataos
    ref: dataset:icebase:sales360mockdb:customer_data_master

    - description: Fetching product data from the S3 bucket,to get a full view of the product portfolio, product performance analysis, and market positioning strategies.
    refType: dataos 
    ref: dataset:icebase:sales360mockdb:product_data_master

outputs:
    - description: The objective is to expose this sales data to facilitate the creation of data APIs to enable seamless access to sales data, allowing integration with external systems, real-time data consumption, and enhanced analytical capabilities.
    refType: dataos
    ref: dataset:icebase:sales360mockdb:f_sales
```
        
## Step 5: Configure ports for integration
Set up ports for services like Lens, Talos, REST APIs, and databases:
    
The **Ports** section lets you set up links to various services and tools tied to your Data Product, such as **Lens**, **Talos**, **REST APIs**, and **Postgres** databases. While it's optional for creating a Data Product, adding ports significantly enhances functionality.

Adding a **Lens** port enables direct access to data models in the **Model** tab of the Data Product details page, making data exploration seamless.

**Talos, REST, and Postgres** ports enable integration with external services, APIs, and databases that the data product may interact with.

```yaml
ports:
    lens:
    ref: lens:v1alpha:product360-lens:public
    refType: dataos

    talos:
    - ref: service:v1:service-product360-api:public
    refType: dataos

    rest: 
    - url: https://liberal-donkey.dataos.app/lens2/api/public:cloud-cost-analysis/v2/rest
    
    postgres: 
    - host: tcp.liberal-donkey.dataos.app
    port: 5432
    params:
        ssl: true
```
    
## Data Product Spec (YAML) file
<details>
<summary>Click here to view the complete Data Product Spec file</summary>

```yaml
name: product-360
version: v1beta
entity: product
type: data
tags:   
  - DPDomain.Sales
  - DPDomain.Marketing
  - DPUsecase.Customer Segmentation
  - DPUsecase.Product Recommendation
  - DPTier.DataCOE Approved
description: Leverages product affinity analysis to identify cross-sell opportunities, enabling businesses to enhance customer recommendations and drive additional sales by understanding the relationships between products purchased together
refs:
- title: 'Workspace Info'
  href: https://dataos.info/interfaces/cli/command_reference/#workspace

v1beta:
  data:
    meta:
      title: Product 360
      sourceCodeUrl: https://bitbucket.org/mywork15/talos/src/main/
      trackerUrl: https://rubikai.atlassian.net/browse/DPRB-65
 
    collaborators:
      - name: shraddhaade
        description: developer
      - name: aayushisolanki
        description: consumer

    resource:
      refType: dataos
      ref: bundle:v1beta:product-360-bundle

    inputs:
      - refType: dataos
        ref: dataset:icebase:customer_relationship_management:customer

      - refType: dataos
        ref: dataset:icebase:customer_relationship_management:purchase

      - refType: dataos
        ref: dataset:icebase:customer_relationship_management:product

    outputs:
      - refType: dataos
        ref: dataset:icebase:customer_relationship_management:product_affinity_matrix

      - refType: dataos
        ref: dataset:icebase:customer_relationship_management:cross_sell_recommendations

    ports:
      lens:
        ref: lens:v1alpha:cross-sell-affinity:public
        refType: dataos

      talos:
        - ref: service:v1:affinity-cross-sell-api:public
          refType: dataos

         
```
</details>

The Data Product Spec file acts as the backbone of your data product in DataOS, enabling seamless deployment, management, and integration with other services. By defining all these sections, you create a comprehensive and efficient configuration for your data product, making it easier to manage and evolve over time.

## Data Product Scanner manifest file
The Scanner Workflow is required to register your data product on the Data Product Hub, making it discoverable and ready for consumption.

```yaml
version: v1
name: scan-data-product-dp
type: workflow
tags:
  - scanner
  - data-product
description: The job scans data product from poros
workflow:
  dag:
    - name: scan-data-product-job
      description: The job scans data-product from poros and register data to metis
      spec:
        tags:
          - scanner2
        stack: scanner:2.0
        compute: runnable-default
        stackSpec:
          type: data-product
          sourceConfig:
            config:
              type: DataProduct
              markDeletedDataProducts: true
              dataProductFilterPattern:
                includes:
                 - product-360
```

## Next step

Now that you have prepared all the necessary components — Bundle Resource, Data Product Spec file, and Scanner Workflow YAML — it’s time to bring your data product to life in the DataOS environment.

Refer to [Deploying Your Data Product on DataOS](/learn/dp_developer_learn_track/deploy_dp_cli/).
