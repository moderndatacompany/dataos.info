# Creating a Data Product Spec File

After setting up your Bundle manifest, the next step is to define your Data Product Spec file. This file serves as a blueprint for your Data Product—capturing its purpose, metadata, resources, and integration points—ensuring seamless deployment and discovery within DataOS.

## 📘 Scenario

You're building a source-aligned retail Data Product that curates customer, product, and sales data to power downstream use of this data. To make this product easy to deploy, discover, and reuse, you’ll define a Data Product Spec—a blueprint that links metadata, input/output datasets, collaborators, and a production-ready Bundle containing ingestion workflows, quality checks, monitors, and pagers.

## Step 1: Define general information

Start with the high-level metadata about your Data Product:


- **Name:** `product360`Identifies the Data Product name for purchase behaviour analysis. The name cannot contain underscores (_). Names with multiple words can only be punctuated using hyphens(-).
    
    ```yaml
    #Example 1
    name: retail360
    
    #Example 2
    name: retail-data-sa
    ```
    
- **Version:** `v1beta`Indicates the version of the product.
- **Entity:** `product`Classifies the entity as a Data Product.
- **Type:** `data` Specifies that the product handles data.
- **Purpose:** Defines the objective and impact of the product.
- **Tags:** Tags provide important context for categorizing the Data Product on the DPH (Data Product Hub). These tags are used to populate three important data points on the DPH UI - `Domain`, `Usecase` and `Tier`
- **Description:** Provides an overview of what the Data Product delivers.
- **Refs**: Include reference links in the DP spec file to add any additional context to the DP.  Provide `title` and link `href`.
    
    The following code snippet shows how the above properties come in spec file is for our example.
    
    ```yaml
    name: retaildata
    version: v1beta
    entity: product
    type: data
    tags:   
      - DPDomain.Marketing
      - DPUsecase.retail_data
      - DPTier.Source Aligned
    description: Source-aligned Data Product
    refs:
    - title: 'Workspace Info'
      href: https://dataos.info/interfaces/cli/command_reference/#workspace
    ```
    

## Step 2: Add Data Product-specific attributes

All the specific details related to the Data Product comes under `data` section in spec file.

- **Meta**
    
    Include a `meta` section, nested under the `data` section, to provide additional context and information to DPH.
    - title which is shown for your Data Product
    - The `sourceCodeUrl` key is used to link the associated repository where the DP artefacts are maintained
    - The `trackerUrl` key is used to link the associated JIRA ticket where the DP issues are being managed
        
        ```yaml
        v1beta:
          data:
            meta:
              sourceCodeUrl: https://bitbucket.org/tmdc/cloud-cost-360/src/main/
              title: Retail Data # this appears on the UI | If you want to capitalise and format your DP name's appearance on DPH
              trackerUrl: https://rubikai.atlassian.net/browse/DPRB-19?atlOrigin=eyJpIjoiZDVmMDNmYmYxOWYwNGVjZDlhNDdiYTA4NTZmMjg0NTIiLCJwIjoiaiJ9
        ```
        
- **Collaborators**
    
    User IDs of individuals who are collaborating on this Data Product. You can to add`name` and `description` as additional context to each collaborator under the `data` section in the DP Spec YAML.
    
    ```yaml
    v1beta:
      data:
        meta:
          foo: bar
          sourceCodeUrl: https://github.com/NandaAtModern/dp_product360/tree/master/product360
          trackerUrl: https://rubikai.atlassian.net/browse/DPRB-19?atlOrigin=eyJpIjoiZDVmMDNmYmYxOWYwNGVjZDlhNDdiYTA4NTZmMjg0NTIiLCJwIjoiaiJ9
        collaborators:
          - name: nandapage # dataos id is mandatory
            description: owner # description is optional
          - name: aayushisolanki
            description: consumer
          - name: kanakgupta
            description: developer
    ```
    
## Step 3: Reference the Bundle Resource
    
With a `resource` section, you give a reference to a single Bundle Resource which is expected to contain all the DataOS Resources which are part of Data Product. For example, Workflows, Services, Secrets, Policies etc.

This section is crucial to bring every workspace-level resource needed for the DP under one umbrella for lifecycle management and context comprehensive context sharing of the Data Product.

```yaml
resource:
    description: 'Resources associated with retaildata Data Product'
    purpose: 'DP Life Cycle Management'
    refType: dataos                     # mandatory
    ref: bundle:v1beta:product360-bundle. # mandatory | referred Bundle must exist
```
    
## Step 4: Define inputs and outputs
Set up datasets that the Data Product will consume and produce:
    
There are two types of dataset references - 

- **dataos**: this is used when your dataset is stored in DataOS and has a DataOS address
- **depot**: this can be used when your dataset is stored on a third party system

```yaml
inputs:
  - refType: dataos
    ref: dataset:postgresxx:public:customer_data

  - refType: dataos
    ref: dataset:postgresxx:public:purchase_data

  - refType: dataos
    ref: dataset:postgresxx:public:product_data

outputs:
  - refType: dataos
    ref: dataset:postgresxx:public:customer_data

  - refType: dataos
    ref: dataset:postgresxx:public:purchase_data

  - refType: dataos
    ref: dataset:postgresxx:public:product_data
```
        
## Step 5: Configure ports for integration
Set up Ports to connect the Data Product to Lens, Talos APIs, REST endpoints, and more:
    
The Ports section lets you set up links to various services and tools tied to consumption of your Data Product. While it's **optional** for creating a Data Product, adding ports significantly enhances functionality.

```yaml
ports:
    lens:
      ref: lens:v1alpha:product360-lens:public
      refType: dataos

    talos:
      - ref: service:v1:service-product360-api:public
        refType: dataos
```
    
## Data Product Spec (YAML) file

Here is the comprehensive and efficient configuration for your Data Product, which makes it easier to manage and evolve over time.
<details>
<summary>Click here to view the complete Data Product Spec file</summary>

```yaml
name: retaildata
version: v1beta
type: data
description: Source-aligned Data Product
tags:
  - DPDomain.Marketing
  - DPUsecase.retail_data
  - DPTier.Source Aligned
v1beta:
  data:
    meta:
      title: Retail Data
      #sourceCodeUrl: https://bitbucket.org/tmdc/product-affinity-training/src/main/
      #trackerUrl: https://rubikai.atlassian.net/browse/DPRB-65
    
    collaborators:
      - name: manishagrawal      #Provide dataos id 
        description: owner
      - name: deepakjaiswal
        description: developer
      - name: nandapage
        description: consumer
      - name: aayushisolanki
        description: consumer
    resource:
      refType: dataos
      ref: bundle:v1beta:retaildata-bundle-xx
    inputs:
      - refType: dataos
        ref: dataset:postgresxx:public:customer_data

      - refType: dataos
        ref: dataset:postgresxx:public:purchase_data

      - refType: dataos
        ref: dataset:postgresxx:public:product_data

    outputs:
      - refType: dataos
        ref: dataset:postgresxx:public:customer_data

      - refType: dataos
        ref: dataset:postgresxx:public:purchase_data

      - refType: dataos
        ref: dataset:postgresxx:public:product_data

    ports:
             
```
</details>

## Data Product Scanner manifest file
The Scanner Workflow is required to register your Data Product on the Data Product Hub, making it discoverable and ready for consumption.

```yaml
version: v1
name: scan-data-product-dp
type: workflow
tags:
  - scanner
  - data-product
description: The job scans Data Product from poros
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
                 - retaildata
```

## Next step

You now have all the components in place—Bundle, Data Product Spec, and Scanner Workflow— it’s time to bring your Data Product to life in the DataOS environment.

👉 Continue to the next module: [Deploying Your Data Product on DataOS](/learn/dp_developer_learn_track/deploy_dp_cli/).
