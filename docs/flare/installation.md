# Flare Standalone Installation

## Requirements
Before proceeding, you will need the following:

- curl utility installed.

- Access permissions for the BitBucket repository to download the .zip file.

## Docker download and set up

1. Run the following command from terminal:
```
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```
The above command is to download docker for **Linux**. For Windows and Mac, visit the following link to download docker desktop.
[Docker desktop download](https://www.docker.com/products/docker-desktop)
2. Log into your docker using the following command and enter the login ID and password.
```
docker login
```
> :material-alert: **Note**: You may need to work with your IT team for this step.

## Run standalone

1. Download the [Flare Standalone zip](https://bitbucket.org/rubik_/flare-standalone/downloads/sample-standalone.zip) file. 

2. Extract the zip file. This file contains the following:  

    - dataos-resource folder with config.yaml
    - datadir containing data files
    - dataout folder for the ouput 
    - README.md containing docker command

3. Navigate to the standalone directory, run the following command (given in the the README.md file) to initiate the spawn process:
   ```yaml
    docker run --rm -it \
    -v $PWD/dataos-resource:/etc/standalone \
    -v $PWD:/datadir \
    -v $PWD/dataout:/dataout \
    -e DATAOS_WORKSPACE=public \
    -e DATAOS_RUN_AS_USER=tmdc \
    rubiklabs/flare:5.6.32-dev start
   ```
   > :material-alert: **Note**: Ensure that Docker commnad refers to the latest image.
4. While running it for the first time, it will download all required files, so it may take a few minutes. You should see the following to indicate a successful start:
```
Flare session is available as flare.
    Welcome to
         ______   _                       
        |  ____| | |                      
        | |__    | |   __ _   _ __    ___ 
        |  __|   | |  / _` | | '__|  / _ \
        | |      | | | (_| | | |    |  __/
        |_|      |_|  \__,_| |_|     \___|  version 1.1.0
        
    Powered by Apache Spark 3.0.1
Using Scala version 2.12.10 (OpenJDK 64-Bit Server VM, Java 1.8.0_262)
Type in expressions to have them evaluated.
Type :help for more information.

scala> 
```
5. You can now run various Flare function commands at the prompt. For instance *'tables'* will give you the list of all tables in the current directory. You should see the *'enriched_product_order_retailer'* listed which is created after the given YAML is successfully run.
```
Flare session is available as flare.
    Welcome to
         ______   _                       
        |  ____| | |                      
        | |__    | |   __ _   _ __    ___ 
        |  __|   | |  / _` | | '__|  / _ \
        | |      | | | (_| | | |    |  __/
        |_|      |_|  \__,_| |_|     \___|  version 1.1.0
        
    Powered by Apache Spark 3.0.1
Using Scala version 2.12.10 (OpenJDK 64-Bit Server VM, Java 1.8.0_262)
Type in expressions to have them evaluated.
Type :help for more information.

scala> tables
+--------+---------------------------------+-----------+
|database|tableName                        |isTemporary|
+--------+---------------------------------+-----------+
|        |enriched_product_order_retailer  |true       |
|        |order_line_item_with_product_info|true       |
|        |product_info                     |true       |
|        |retail_order_line_item           |true       |
|        |retailer_info                    |true       |
+--------+---------------------------------+-----------+
```
 - You can also run a Spark sql query to verify the data, as follows:
```
scala> spark.sql("select product_name, product_id from enriched_product_order_retailer").show(4)
+------------+----------+
|product_name|product_id|
+------------+----------+
|     Colazal|     P1098|
|   Oxycodone|     P1705|
|      Belviq|     P1855|
|  Kenalog-40|     P1079|
+------------+----------+
only showing top 4 rows
```
 
**You have now successfully installed Flare standalone and verified the same by ingesting sample data.**

## Sample YAML

The following yaml file (config.yaml) is given in the dataos-resource folder to run a sample job in standalone. This job joins product, retailer and order datasets and creates the new enriched dataset. 

> :material-alert: **Note**: Make the changes to this YAML as per your requirement.

```yaml
version: v1beta1
name: sample-job-standalone
type: workflow
tags:
  - getting-data
  - product
  - retailer
  - orders
description: This job takes input of product, retailer and order data and joins them all and saves as new dataset.
owner: rubik-ai
workflow:
  dag:
    - name: retail-data-enrichment
      title: retailer orders enriched data
      description: This job takes input of product retailer and order data and joins all
      spec:
        tags:
          - Transformation
        stack: flare:1.0
        tier: connect
        flare:
          driver:
            coreLimit: 1200m
            cores: 1
            memory: 1024m
          executor:
            coreLimit: 1200m
            cores: 1
            instances: 1
            memory: 1024m
          job:
            explain: true
            inputs:
             - name: product_info
               dataset: /datadir/product_info
               format: json
             - name: retailer_info
               dataset: /datadir/retailer_info
               format: json               
             - name: retail_order_line_item
               dataset: /datadir/retail_order_line_item
               format: json

            logLevel: ERROR
            
            outputs:
             - name: output01
               depot: depot: /dataout/enriched_retailer    
              
            steps:
              - sink:
                - sequenceName: enriched_product_order_retailer
                  datasetName: enriched_retailer_01
                  outputName: output01
                  outputType: Iceberg
                  description: retailer enriched data
                  outputOptions:
                    saveMode: append
                  tags:
                    - retailer
                    - product
                    - enriched-data
                  title: Retailer Enriched Data

                sequence:
                  - name: order_line_item_with_product_info # Joinin product info with order
                    sql: select * from retail_order_line_item order_i left join product_info product_i on order_i.product_ids = product_i.product_id

                  - name: enriched_product_order_retailer # enriched data
                    sql: select * from order_line_item_with_product_info opi left join retailer_info retail_i on opi.retailer_id = retail_i.retailer_id
```

