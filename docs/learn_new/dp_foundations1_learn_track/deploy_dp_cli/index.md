# Deploying your Data Product on DataOS

After setting up the essential YAML files — the Bundle YAML, Data Product Specification YAML, and Lens YAMLs — the final step is to deploy your data product on the Data Product Hub. This process makes your product available for discovery and consumption within your organization. The deployment involves resource instantiation and metadata registration.

## 📘 Scenario

Imagine you've built a source-aligned data product called retaildata that delivers curated customer, product, and sales data. You’ve already created the necessary configuration files—now it’s time to deploy it using the DataOS CLI.

## Deploying Data Product

Ddeployment process has three stages:

- **Instantiate Resources**: Using the Bundle YAML, all referenced resources such as Workflows, Secrets, and Services are created.

- **Register the Data Product**: The Data Product Spec is applied to register the product in the Data Product Hub.

- **Register Metadata**: A Scanner Workflow indexes the product into Metis, making it discoverable and searchable.

## Step 1: Login to DataOS CLI

DataOS CLI is a text-based interface that allows users to interact with the DataOS context via command prompts.

## Step 2: Use the `apply` command on CLI to deploy your Data Product on Data Product Hub successfully.

1. Run the Bundle manifest file created in the previous topic.
    
    ```bash
    ➜ dp_retaildata git:(master) ✗ dataos-ctl apply -f retaildata/bundle/bundle.yml 
    
    INFO[0000] 🛠 apply...                                   
    INFO[0000] 🔧 applying retaildata-bundle:v1beta:bundle... 
    INFO[0001] 🔧 applying retaildata-bundle:v1beta:bundle...created 
    INFO[0001] 🛠 apply...complete 
    ```
    
2. Run the Data Product Spec file (YAML) with **`dataos-ctl product apply`** command.
    
    ```bash
    dataos-ctl product apply -f ${path-to-dp-manifest-file}
    ```
    
    ```bash
    ➜ dp_retaildata git:(master) ✗ dataos-ctl product apply -f retaildata/data_product_spec.yml
     
    INFO[0000] 🛠 product apply...                           
    INFO[0000] 🔧 applying data:v1beta:retaildata...          
    INFO[0001] 🔧 applying data:v1beta:retaildata...created   
    INFO[0001] 🛠 product apply...complete 
    ```
    
3. Run the Scanner YAML, created in the last topic, containing a valid reference to the Data Product. This step is important to make your data  product discoverable in the Data Product Hub or Metis.
    
    ```bash
    ➜ dp_retaildata git:(master) ✗ dataos-ctl apply -f retaildata/scanner.yml 
    INFO[0000] 🛠 apply...                                   
    INFO[0000] 🔧 applying(public) scan-data-product-dp:v1:workflow... 
    INFO[0001] 🔧 applying(public) scan-data-product-dp:v1:workflow...created
    ```
    

## Step 3: Validating the creation of Data Product

To check if you have created a data product, run the following command. It lists all data products created by you:

```bash
➜ dataos-ctl product get
```

**Example Usage**

```bash
dp_retaildata git:(master) dataos-ctl product get
INFO[0000] 🔍 product get...                             
INFO[0000] 🔍 product get...complete                     

  TYPE | VERSION |          NAME          | STATUS |   OWNER    
-------|---------|------------------------|--------|------------
  data | v1beta  | retaildata              | active | nandapage  
```

## Step 4: Exploring Data Product on Data Product Hub

🎯 You're done creating your source-alined data product! Now, check it on Data Product Hub.

1. Log in to the DataOS instance and Navigate to Data Product Hub to search the data product.
    
    ![dp_on_dph.png](/learn_new/dp_foundations1_learn_track/deploy_dp_cli/search_retail_data_dp.png)
    
2. Click on the data product to view its details.
    ![dp_on_dph.png](/learn_new/dp_foundations1_learn_track/deploy_dp_cli/retail_data_dp.png)

<aside class="callout">
Great work completing Track 1: Source-Aligned Data Product Foundations! You've successfully connected your data sources, applied governance and observability, and deployed your first source-aligned Data Product on the Data Product Hub.

</aside>

## 🎯 What's Next?
Now it’s time to advance to Foundations Track- Part 2, where you’ll focus on creating Consumer-Aligned Data Products—tailored, business-ready products built on top of source-aligned foundations.

👉 Head to the next module: [Creating a Consumer-Aligned Data Product]()