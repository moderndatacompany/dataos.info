# Deploy and Register Data Product

In the last module you built business-ready tables, views, and a Lens model on top of the source-aligned retail datasets you ingested earlier.
Now it’s time to wrap everything into a single, deployable bundle, publish the Data Product spec, and surface it in the Data Product Hub (DPH) & Metis for your consumers.

## Step 1: Create a Bundle Definition

Group related components—workflows, scripts, models—into a single bundle for easy management. Referencing the bundle in your Data Product manifest ensures all resources are deployed together.

🎯 Your Actions:

1. Create a bundle.yaml file using the template below.

2. Include all relevant resources (Lens, monitors, pagers, etc.) in the resources section. Lens must be deployed through Bundle resource.

3. Organize resources into a dedicated workspace (recommended).

4. Apply the bundle using dataos-ctl apply.

??? example "bundle.yaml"

    ```yaml
    name: productaffinity-bundle-practice
    version: v1beta
    type: bundle
    tags:
    - dataproduct
    description: This bundle resource is for the product affinity data product.
    layer: "user"
    bundle:
    resources:
        - id: lens
        file: build/semantic-model/deployment.yml
        workspace: <workspace_name>
        
        - id: quality_customer
        file: build/slo/input/customer.yml
        workspace: <workspace_name>
        
        # Add other resources (monitors, pagers) you have created
    

        
        # - id: quality_product
        #   file: build/slo/input/product.yml
        #   workspace: <workspace_name>

        # - id: quality_purchase
        #   file: build/slo/input/purchase.yml
        #   workspace: <workspace_name>
        
        # - id: quality_affinity
        #   file: build/slo/output/affinity-matrix.yml
        #   workspace: <workspace_name>

        # - id: quality_cross_sell
        #   file: build/slo/output/cross-sell.yml
        #   workspace: <workspace_name>

    ```
## Step 2: Create the Data Product Specification File

Document key metadata, purpose, and the structure of your data product.

🎯 Your Actions:

1. Create a productaffinity.yaml file using the template below.

2. Describe the product purpose and use cases.

3. Define input and output datasets.

4. Link to your bundle and services (e.g., Lens).

5. Set up ports for services like Lens, Talos, REST APIs, and databases. For this example, we have Lens.

5. Apply using:

```bash
dataos-ctl product apply -f productaffinity.yaml
```
<details><summary>Click here to view Data Product Spec file</summary>

```yaml
name: productaffinity
version: v1beta
type: data
description: Analyzes product affinity to identify cross-sell opportunities.
tags:
  - DPDomain.Marketing
  - DPUsecase.Customer Segmentation
  - DPUsecase.Product Recommendation
  - DPTier.Consumer Aligned
v1beta:
  data:
    meta:
      title: Product Affinity xx
      #sourceCodeUrl: https://bitbucket.org/tmdc/product-affinity-training/src/main/
      #trackerUrl: https://rubikai.atlassian.net/browse/DPRB-65
    collaborators:
      - name: 
        description: owner
      - name: <dataos-id of user>
        description: developer
      - name: <dataos-id of user>
        description: consumer
      - name: <dataos-id of user>
        description: consumer
    resource:
      refType: dataos
      ref: bundle:v1beta:productaffinity-bundle
    inputs:
      - refType: dataos
        ref: dataset:postgresxx:public:customer_data

      - refType: dataos
        ref: dataset:postgresxx:public:purchase_data

      - refType: dataos
        ref: dataset:postgresxx:public:product_data

    outputs:
      - refType: dataos
        ref: dataset:lakehouse:crm_data:product_affinity_matrix

      - refType: dataos
        ref: dataset:lakehouse:crm_data:cross_sell_recommendations

    ports:
      lens:
        ref: lens:v1alpha:productaffinity-xx:public
        refType: dataos

      # talos:
      #   - ref: service:v1:product-affinity-api:public
      #     refType: dataos
```

</details>

## Step 3: Register in the Data Product Hub

To make your product discoverable in the Data Product Hub and Metis, apply a scanner workflow.

🎯 Your Actions:

1. Create a scanner.yaml file using the template.

2. Replace the includes field with your data product name.

3. Apply using:

```bash
dataos-ctl apply -f scanner.yaml
```
<details><summary> Click here to view scanner.yaml</summary>

```yaml
version: v1
name: scan-data-product-xx
type: workflow
description: Registers the data product in the Data Product Hub.
workflow:
  dag:
    - name: scan-data-product-job
      description: Scans and registers the data product.
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
                 - productaffinity # data product details
```

## Step 4: ### Activity 8.4: **Validating the Creation of Data Product**

**🎯 Your Actions:**

1. Run the following command in your terminal to list your data products.
    
    ```bash
    ~ dataos-ctl product get
    INFO[0000] 🔍 product get...                             
    INFO[0000] 🔍 product get...complete                     
    
      TYPE | VERSION |          NAME          | STATUS |   OWNER    
    -------|---------|------------------------|--------|------------
      data | v1beta  |      productaffinity   | active | nandapage  
    ```
    
## Step 4: Exploring Data Product on Data Product Hub

You can also check your data product on Data Product Hub.

1. Log in to the DataOS instance and Navigate to Data Product Hub.
    
    ![dp_on_dph.png](/learn_new/dp_foundations2_learn_track/deploy_dp_cli/product360.png)
    
2. Click on the data product to view its details.
    ![dp_on_dph.png](/learn_new/dp_foundations2_learn_track/deploy_dp_cli/product360_details.png)