# How to deploy the Data Product?

You might have successfully created the data product, but in order to make it discoverable on Metis and Data Product Hub you have to run the Scanner. To deploy your Data Product to the Data Product hub and Metis, you have to create a manifest file for a Data Product Scanner Workflow. You can find the manifest file below.

**Data Product scanner workflow manifest**
    
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
    

To apply the scanner workflow manifest file, run the following command.

```shell

dataos-ctl resource apply -f ${path-to-your-scanner-manifest-file}

```

After executing the above command successfully you’ll be able to search for your Data Product on [Metis UI](https://dataos.info/interfaces/metis/) and Data Product Hub UI. To learn more about the Scanner Workflow, go to [Scanner](https://dataos.info/resources/stacks/scanner/).