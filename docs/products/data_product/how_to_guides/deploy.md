# How to deploy the Data Product?

You might have successfully created the data product, but in order to make it discoverable on [Metis](/interfaces/metis/) and [Data Product Hub](/interfaces/data_product_hub/), you have to run the [Scanner](/resources/stacks/scanner/). To deploy your Data Product to the Data Product hub and Metis, you have to create a manifest file for a Data Product Scanner Workflow. You can find the manifest file below.

**Data Product Scanner Workflow manifest**
    
```yaml
version: v1
name: scan-data-product2
type: workflow
tags:
    - scanner
    - data-product
description: The job scans data product from poros
workflow:
    # schedule:
    #   cron: '*/20 * * * *'
    #   concurrencyPolicy: Forbid
    dag:
    - name: scan-data-product-job2
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
                # dataProductFilterPattern:
                #   includes:
                #     - customer-360-all$
```
    

To apply the Scanner Workflow manifest file, run the following command.

```shell

dataos-ctl resource apply -f ${path-to-your-scanner-manifest-file}

```

After executing the above command successfully you’ll be able to search for your Data Product on [Metis UI](/interfaces/metis/) and Data Product Hub UI. To learn more about the Scanner Workflow, go to [Scanner](/resources/stacks/scanner/).

After successfully deploying the Data Product, it’s time to observe the results if the Data Product incorporates with your use-case or not, If the Data Product does not match the goal then you can iterate the process until your goal is achieved. 

### **Validate the Data Product**

To check if you have created a Data Product run the following command. It will list all the data products created by you.

```bash
dataos-ctl product get
```

**Example usage:**

```bash
dataos-ctl product get
# expected output
product get...                             
product get...complete                     

  TYPE | VERSION |     NAME      | STATUS |    OWNER     
-------|---------|---------------|--------|--------------
  data | v1alpha |     dp-test   | active | iamgroot  
  

```
## Deprecate the Data Product
If a Data Product is no longer in use we can delete the Data Product. To delete a Data Product please follow the below steps.

### **Delete the Data Product**

To delete the Data Product execute the following command.

```bash
dataos-ctl product delete -f ${path-to-dp-manifest-file}
```

**Example usage:**

```bash
dataos-ctl product delete -f /home/iamgroot/office/data_products/firstdp.yaml
# Expected Output
INFO[0000] 🗑 product delete...                          
INFO[0000] 🗑 deleting data:v1alpha:dp-test... 
INFO[0000] 🗑 deleting data:v1alpha:dp-test...deleted 
INFO[0000] 🗑 product delete...complete 
```

**Alternative commands to delete the Data Product:**

- using `-i` identifier.
    
    ```bash
    dataos-ctl product delete -i TYPE:VERSION:NAME
    ```
    
    **Example usage:**
    
    ```bash
    dataos-ctl product delete -i data:v1alpha:dp-test
    # Expected Output
    INFO[0000] 🗑 product delete...                          
    INFO[0000] 🗑 deleting data:v1alpha:dp-test... 
    INFO[0000] 🗑 deleting data:v1alpha:dp-test...deleted 
    INFO[0000] 🗑 product delete...complete 
    ```
    
- using `-t` type.
    
    ```bash
    dataos-ctl product delete -t data -n name -v version
    ```
    
    **Example usage:**
    
    ```bash
    dataos-ctl product delete -t data -n dataproduct -v v1alpha
    # Expected Output
    INFO[0000] 🗑 product delete...                          
    INFO[0000] 🗑 deleting data:v1alpha:dp-test... 
    INFO[0000] 🗑 deleting data:v1alpha:dp-test...deleted 
    INFO[0000] 🗑 product delete...complete 
    ```
    

### **Delete the metadata of the Data Product from Metis:**

When clicking on your Data Product on Metis, clicking on the menu of the right-corner you will have the option to delete the metadata from Metis as you can see below:

![delete](/products/data_product/how_to_guides/delete.png)
