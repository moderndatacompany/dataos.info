# How to deploy the Data Product using the CI/CD pipeline?

This section walks you through deploying a data product using a Continuous Integration/Continuous Deployment (CI/CD) pipeline. Follow these steps to set up and execute the deployment process seamlessly.

Make sure to follow the steps given in [this section](/products/data_product/recipes/cookiecutter/) before moving on to the below steps.

## Add Data Product configuration files

After creating the template, you can now update the template with required configuration files to create the Data Product.

## Update User Information

- Open `username_mapping.py`  in your code editor.
    
    <div style="text-align: center;">
    <img src="/products/data_product/recipes/Untitled%20(12).png" alt="username_mapping" />
    </div>

- Add your Git username, Bitbucket username, and DataOS user ID in the specified order as shown below:
    
    ```python
    
    'git_username':'dataos userID'
    'bitbucket_username':'dataos userID'
    ```
    
- You can obtain the DataOS user ID by executing the command:
    
    ```bash
    dataos-ctl user get
    ```
        

## Update Pipeline Configuration

- Open `bitbucket-pipelines.yml` in your code editor.
- Replace occurrences of the branch name `main` with your actual Bitbucket repository branch name.
- Adjust workspace and schema names as per your requirements.
- Update the context environment to reflect your actual working context environment (e.g. emerging-hawk).

## Set Repository Variables

- Navigate to your Bitbucket repository settings.
- Go to `Repository Settings` > `Repository variables`.
- Add repository variables as shown in the image provided, ensuring to input the correct credentials obtained from your DataOS specialist.
    <div style="text-align: center;">
    <img src="/products/data_product/recipes/Untitled%20(13).png" alt="username_mapping" />
    </div>

## Push Changes

- In your code editor terminal, push the changes to the main branch using an app password.
- Pushing the changes will trigger the CI/CD pipeline to start deploying automatically. Alternatively, you can manually initiate the deployment by clicking on the `Run pipeline` option in the Pipelines section of your Bitbucket repository as shown below.
    
    <div style="text-align: center;">
    <img src="/products/data_product/recipes/image1.png" alt="username_mapping" />
    </div>    

    

By following the above steps, you'll successfully deploy your data product using the CI/CD pipeline. If you encounter any issues or need further assistance, don't hesitate to reach out to your DataOS specialist.