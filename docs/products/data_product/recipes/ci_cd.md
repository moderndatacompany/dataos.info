# How to deploy Data Product through a CI/CD pipeline?

This documentation outlines the process for deploying a Data Product through a [CI/CD pipeline](https://support.atlassian.com/bitbucket-cloud/docs/get-started-with-bitbucket-pipelines/). A **CI/CD pipeline** (Continuous Integration/Continuous Deployment) automates building, testing, and deploying code using Bitbucket, significantly reducing the time required for Data Product deployment.

The following steps are provided to guide you through the successful setup of a CI/CD Data Product pipeline:

- Creating a repository in Bitbucket.
- Cloning the repository.
- Making specific modifications to the folder/directory.
- Adding repository variables in Bitbucket.
- Deploying the pipeline.
- Verifying the deployment.

## Pre-requisites

To begin building the pipeline, ensure the following prerequisites are met:

- Have a blueprint of the [Data Product](/products/data_product/) you plan to build. For example, if creating a Data Product like `sales-360`, identify the necessary [Resources](/resources/), such as [Depot](/resources/depot/), [Services](/resources/service/), [Workflows](/resources/workflow/), or [Lens](/resources/lens/).
- Obtain the following DataOS environment variables:
    - **License organization ID, license key, Docker username & password, and DataOS prime API key:** These details can be provided by the DataOS operator or admin.
    - **API key**: Generate the DataOS API key in the DataOS profile section.
    - **Client secret, access token, and refresh token:** These can be obtained from the `.dataos` folder within your home directory.
        
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/c2f9e419-742a-4d3b-96f7-8cd08ea09bd0/image.png)
        

## Steps to build a CI/CD pipeline

To begin building the CI/CD pipeline for your Data Product, follow these steps.

### **1. Create a Bit bucket repository**

Begin by creating a Bitbucket repository. Follow these steps to set up the repository in Bitbucket:

a. Log in to your Bitbucket account.
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/e6a7eb17-81ec-4e20-afa0-8fc55a15edfe/image.png)
    
 Select the “Create” drop-down menu and choose “Repository.”

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/c4fb625f-2c60-49e3-888a-df5b1c892484/image.png)

b. Enter the project, repository name, and default branch name. If you want the repository to be public, uncheck the private repository option. Then, click on “Create repository.”
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/00e98480-a634-46d4-87a9-01ed7f41fc6d/image.png)
    
c. The repository creation can be verified by navigating to the Repositories tab.
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/5f1d672a-c9b0-45bb-b0b4-f3dbcbad4847/image.png)
    

### **2. Clone the repository**

Follow these steps to clone the repository:

a. Open the repository and click the "Clone" button.
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/54d9d35d-0a16-4e3e-945f-9ca731ec4ede/image.png)
    
b. Copy the provided URL, paste it into your terminal, and press Enter.
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/abb11048-b9bb-4fc8-b4e8-3a0df87746a2/image.png)
    
c. The repository can now be found in your home/root directory.
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/c3e51f0b-3c1f-477d-bbfb-607ec0a35527/f731e9a8-07f0-4e1f-bfd6-9297331d54a4.png)
    

### **3. Start building the Data Product**

This section presents a use case where data is being ingested from BigQuery to start building the Data Product. To accomplish this, various Resources must be created, including a Depot, Scanner, Flare job, Bundle, and Data Product deployment manifest. Additional Resources such as Policies, Talos, or Lenses can be created as required.

a. Open the cloned repository using your preferred code editor (e.g., VS Code).
b. Inside the repository, create a folder named `data_product` to store all related Resources.
    
```sql
data-product-deployment
└── data_product
```
    
c. Inside the `data_product` folder, create a subfolder called `depot`. Following the depot documentation, create a depot manifest file.
    
```sql
data-product-deployment
└── data_product
    └── depot
        └── depot.yaml
```
    
d. For the BigQuery Depot, add a JSON file inside the `depot` folder. Provide the correct path to this JSON file in the `depot manifest` file. While it is not mandatory to store the JSON file in the same folder, it is recommended as best practice.
    
```sql
data-product-deployment
└──data_product
    └── depot
        ├── depot.yaml
        └── key.json
```
    
e. Inside the `data_product` folder, create a subfolder named `scanner`. Place the scanner manifest file for both the Depot and the Data Product inside this folder.
    
```sql
data-product-deployment
└── data_product
    ├── depot
    │   ├── depot.yaml
    │   └── key.json
    └── scanner
        ├── depot_scanner.yaml
        └── dp_scanner.yaml
```
    
f. Create another folder named `transformation` inside the `data_product` folder. Inside this folder, add the flare job manifest files for data transformation.
    
```sql
data-product-deployment
└── data_product
    ├── depot
    │   ├── depot.yaml
    │   └── key.json
    ├── scanner
    │   ├── depot_scanner.yaml
    │   └── dp_scanner.yaml
    └── transformation
        ├── flare1.yaml
        └── flare2.yaml
        
```
    
g. Create a folder named `bundle` inside the `data_product` folder. Inside the `bundle` folder, create a bundle manifest file that will apply the Depot, Depot Scanner, and Flare jobs at once.
    
```sql
data-product-deployment
└── data_product
    ├── depot
    │   ├── depot.yaml
    │   └── key.json
    ├── scanner
    │   ├── depot_scanner.yaml
    │   └── dp_scanner.yaml
    ├── transformation
    │   ├── flare1.yaml
    │   └── flare2.yaml
    └── bundle
        └── bundle.yaml   
        
```
    
h. Inside the `data_product` folder, create a Data Product deployment manifest file.
    
```sql
data-product-deployment
├── data_product
    ├── depot
    │   ├── depot.yaml
    │   └── key.json
    ├── scanner
    │   ├── depot_scanner.yaml
    │   └── dp_scanner.yaml
    ├── transformation
    │   ├── flare1.yaml
    │   └── flare2.yaml
    ├── bundle
    │   └── bundle.yaml   
    └── deployment.yaml 
```
    
i. Double-check all files and paths to ensure everything is provided correctly and that the manifest files are properly set up.
j. You can add configuration files of more resources as per your requirements, such as Policy, Talos, Lens, etc.

### **4. Configure the pipeline**

Configure the pipeline by following the below steps. 

a. In your home directory, locate the `.dataos` folder containing the current DataOS context configuration files. Copy the folder and paste it into your cloned repository.
    
```sql
data-product-deployment
├── data_product
└── .dataos    
```
    
b. Create a manifest file named `bitbucket-pipelines.yaml` and include the following code. This file will contain the DataOS ctl commands to apply the manifest files along with their dependencies. Additionally, update the default branch name in the file. In this case, the default branch is `main`, but it can be any name, such as `master`, depending on the branch defined when creating the Bitbucket repository.
    
```sql
data-product-deployment
├── data_product
├── .dataos  
└── bitbucket-pipelines.yaml  
```
    


```yaml
image: atlassian/default-image:2
pipelines:
    branches:
    main:  # your default branch name
        - step:
            name: "Setup DataOS Data Product Self Service CLI Runtime"
            script:
            # Login Docker and pull dataos docker image
            - echo "$DOCKER_PASSWORD" | docker login --username "$DOCKER_USERNAME" --password-stdin 
            - docker pull rubiklabs/dataos-ctl:2.26.17-dev
            - docker run rubiklabs/dataos-ctl:2.26.17-dev

            services: 
            - docker 
            caches:
            - docker 
    
        - step:
            name: "Deploy Data Product"
            script:
            # Define common environment variables for Docker run
            - DOCKER_ENV_VARS="-e DATAOS_CONFIG_DIRECTORY=/dataos -e USER_ID=${{iamgroot}} DATAOS_PRIME_APIKEY=$DATAOS_PRIME_APIKEY -e LICENSE_KEY=$LICENSE_KEY -e LICENSE_ORGANIZATION_ID=$LICENSE_ORGANIZATION_ID -e DATAOS_FQDN=${{splendid-shrew.dataos.app}} -e APIKEY=$API_KEY
            
            # Apply the Bundle Resource
            - docker run --rm -i -v $BITBUCKET_CLONE_DIR/.dataos:/dataos -v $BITBUCKET_CLONE_DIR:/jobsfolder $DOCKER_ENV_VARS rubiklabs/dataos-ctl:2.26.17-dev apply -f /jobsfolder/data-product-deployment/ci_cd/slb/bundle/bundle.yaml
            
            # Apply the Data Product manifest file
            - docker run --rm -i -v $BITBUCKET_CLONE_DIR/.dataos:/dataos -v $BITBUCKET_CLONE_DIR:/jobsfolder $DOCKER_ENV_VARS rubiklabs/dataos-ctl:2.26.17-dev product apply -f /jobsfolder/data-product-deployment/ci_cd/data_product_spec.yml
            
            # Apply the Data Product Dcanner
            - docker run --rm -i -v $BITBUCKET_CLONE_DIR/.dataos:/dataos -v $BITBUCKET_CLONE_DIR:/jobsfolder $DOCKER_ENV_VARS rubiklabs/dataos-ctl:2.26.17-dev apply -f /jobsfolder/data-product-deployment/ci_cd/slb/scanner/data-product/scanner.yml
            
            
            # - sleep 20

            services: 
            - docker 
            caches:
            - docker
```
    
c. Update the username and current DataOS context in the placeholders within the script section of the `bitbucket-pipelines.yaml` file.
d. To apply the bundle manifest file, copy the relative path of your bundle manifest file and paste it into the script, as shown below. The path should be pasted after the `/jobsfolder` in this case.
    
```yaml
# Apply the Bundle Resource
- docker run --rm -i -v $BITBUCKET_CLONE_DIR/.dataos:/dataos -v $BITBUCKET_CLONE_DIR:/jobsfolder $DOCKER_ENV_VARS rubiklabs/dataos-ctl:2.26.17-dev delete -f /jobsfolder/data-product-deployment/ci_cd/slb/bundle/bundle.yaml
```
    
e. Repeat the previous step to apply the Data Product deployment and Scanner manifest files. For these specific manifest files, the commands need to be updated accordingly. In this case, to apply the Data Product manifest file, the command should be provided along with the path, as shown: `product apply -f /jobsfolder/data-product-deployment/ci_cd/data_product_spec.yml`. Similarly, if you want to delete any existing resource, use the delete command along with the corresponding path.
    
```yaml
# Apply the Data Product manifest file
- docker run --rm -i -v $BITBUCKET_CLONE_DIR/.dataos:/dataos -v $BITBUCKET_CLONE_DIR:/jobsfolder $DOCKER_ENV_VARS rubiklabs/dataos-ctl:2.26.17-dev product apply -f /jobsfolder/data-product-deployment/ci_cd/data_product_spec.yml
```
    
f. In the same manner, any number of Resources, Stacks, and Products can be applied or deleted as needed.

<aside class="callout">
🗣 Remember that a Resource or Product may have dependencies on other Resources or Products, so the apply commands should be provided accordingly. For example, the Data Product Scanner has a dependency on the Data Product manifest file, so the apply command for the Data Product manifest file should be added first, followed by the Depot Scanner.
</aside>

### **5. Add repository variables**

Add repository variables to the Bit Bucket repository settings by following the below steps.

a. In the Bit Bucket repository, navigate to the repository settings.
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/785c5826-2f1a-48a0-9ae8-bb2cb5efe8a2/d6d84d91-f397-4ce7-a92d-9b4a28ae1a4c.png)
    
b. In the repository variables section, add key-value pairs mentioned in the pre-requisites section as shown below.
    
    <aside class="callout">
    🗣 Before adding the repository variables make sure the pipeline deployment is enabled in your Bit Bucket settings.
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/49e26105-570c-4a25-a3bc-d6f839dbf60f/image.png)
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/d0e67218-99bc-462d-af55-b385b42899a5/image.png)
    
    </aside>
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/d27de6c1-85be-4190-b81a-dfd73bdfa0b3/image.png)
    

### **6. Deploy the pipeline**

Deploy the pipeline by following the below steps.

a. Open the terminal of your repository, and add the changes by applying the following command.
    
```bash
git add .
```
    
b. Commit the changes.
    
```bash
git commit -m "Added data product configurations"
```
    
c. Push the changes by providing the Bit Bucket app password which can be created from the personal Bit Bucket settings.

```bash
git push 
```
    
d. By pushing the changes in Bit Bucket, the pipeline will automatically start deploying which can be tracked on the commits section of the Bit Bucket repository.
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/6c776bdb-0289-4a29-895a-103748878612/image.png)
    
e. A successful deployment will look like the following.
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/c5c0053e-d74f-47de-a39e-24d5cf9bc95d/image.png)
    

### **8. Error fixes**

Fix the possible errors by following the below steps.

- If an error occurs during the push due to a large file size, navigate to your repository settings. Under **Repository details**, open the **Advanced** dropdown, uncheck the “Block pushes with files over 100MB” option, and save the changes. Then push again.
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/8838fdce-1941-4f67-94e5-c137295a5eda/image.png)
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/266a517b-512f-4093-89d1-ef2985753d7e/image.png)
    
- If the pipeline fails for any reason, you can make the necessary updates, push the changes, and rerun the failed part of the pipeline based on the error received.
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/ff04fb87-b596-435a-8376-c3af7c120f34/image.png)
    

Good to go!