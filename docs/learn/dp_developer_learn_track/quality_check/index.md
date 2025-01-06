# Implementing quality checks

Ensuring high data quality is critical for delivering reliable insights and maintaining trust in your Data Products. This guide will walk you through implementing using Soda Stack in DataOS. These quality checks help ensure that the data is accurate, complete, and ready for reliable analysis.

## Scenario

As a data engineer, you’re working with datasets and exploring them on Workbench and Metis. Before using this data to create a Data Product, you need to validate its quality. Your task is to set up quality checks that verify the data's accuracy, completeness, and consistency, ensuring it meets the necessary standards for consumer use.

## Define service level objectives (SLOs)

In the build stage, you and other stakeholders must have defined SLOs for your Data Product. These are measurable quality goals for the data that define what 'good quality' means for your Data Product.

Suppose the following are the SLOs you and other stakeholders have decided:

- **Accuracy**: 99% of data points must be accurate.
- **Completeness**: No more than 1% of records can have missing values.
- **Freshness**: Data must be updated within the last 24 hours.
- **Schema**: 100% of records must adhere to the expected schema.
- **Uniqueness**: 0.5% of records should be duplicated at maximum.
- **Validity**: 95% of records must meet all domain-specific rules.

## Setting Up data quality checks

### **Step 1: Define a directory structure**

Once your SLOs are defined, you can organize your quality check workflows. Create a quality directory to ensure that your Data Product's input datasets meets the SLOs' requirements. Inside this folder, you'll organize your quality checks by creating subdirectories named 'input'. Each subdirectory will contain the specific Soda check workflows for each input dataset (e.g., `customer.yml`, `product.yml`, `purchase.yml`).

Here’s an example of how your folder might look:

```bash
quality/
│  ├── input/
│     ├── customer.yml
│     ├── product.yml
│     └── purchase.yml
```

This structure helps you keep your quality checks organized and aligned with the defined SLOs for each input dataset.

### **Step 2: Define quality checks**

With your SLOs in place, the next step is to define the quality checks to ensure your data meets the established standards. These quality checks are essential to monitor and maintain the quality of your data. 

For example, if you’re defining quality checks for a 'customer' dataset, you can specify the following checks:

- **Schema**: The data type of birth year should be an integer.
- **Accuracy**: The average length of a country is more than 6.
- **Completeness**: Customer ID should not be zero.
- **Validity**: Customer ID should not be null.
- **Uniqueness**: Customer ID should be unique.

Quality checks will be implemented using the Soda framework, leveraging SodaCL—a YAML-based language—to define custom data quality checks for each dataset. The Soda Stack allows you to embed these rules directly into your workflow, enabling validation of key metrics such as accuracy, completeness, and uniqueness.


## Configuring quality checks using Soda Stack

Use Soda Stack within DataOS to establish robust data quality checks using 

### **Step 1: Choose the right DataOS Resource for the Job**

The type of DataOS Resource you select depends on the use case:

- Workflow Resource: Ideal for batch workloads and periodic quality checks.

- Worker Resource: Best suited for long-running, continuous monitoring.

For demonstration, we will choose the Workflow Resource to run scheduled data quality checks on a customer dataset.

### **Step 2: Define the Soda Workflow manifest**

Create a Workflow manifest to configure Soda Stack for batch quality checks. Ensure that the metadata and Stack properties are properly defined. You can schedule this workflow to run quality checks automatically at regular intervals.

```yaml
ame: soda-customer-quality
version: v1
type: workflow
tags:
  - workflow
  - soda-checks
description: Applying quality checks for the customer data
workspace: public
workflow:
  # schedule:
  #   cron: '00 08 * * *'
  #  # endOn: '2023-12-12T22:00:00Z'
  #   concurrencyPolicy: Forbid
  dag:
    - name: soda-customer-quality
      spec:
        stack: soda+python:1.0
        compute: runnable-default
        resources:
          requests:
            cpu: 1000m
            memory: 250Mi
          limits:
            cpu: 1000m
            memory: 250Mi
        logLevel: INFO # WARNING, ERROR, DEBUG
        
```
### **Step 3: Declare the Soda stackSpec section**

**Declaring input dataset address**

The dataset attribute allows data developer to specify the data source or dataset that requires data quality evaluations. It is declared in the form of a Uniform Data Link [UDL], in the following format: dataos://[depot]:[collection]/[dataset].

**Profile the dataset (Optional)**

Enable profiling to gather insights into the dataset’s characteristics and data distribution. Specify the columns to be profiled in the manifest. Wildcard Matching: Use "*" to profile all columns in the dataset.

```yaml
stackSpec:
  inputs:
    - dataset: dataos://lakehouse:customer_relationship_management/customer_data
      options:
        engine: minerva
        clusterName: miniature
      profile:
        columns:
          - include *
```

### **Step 4: Define Soda checks**
Tailor the checks to address issues identified by your team.

```yaml
stackSpec:
  inputs:
    - dataset: dataos://lakehouse:customer_relationship_management/customer_data
      options:
        engine: minerva
        clusterName: miniature
      profile:
        columns:
          - include *
      checks:  
        - schema:
            name: Data type of birth year should be integer
            fail:
              when wrong column type:
                birth_year: bigint
            attributes:
              category: Schema

        - freshness(created_at) < 7d:
            name: If data is older than 7 days 
            attributes:
              category: Freshness

        - invalid_count(customer_id) = 1 :
            name: Customer Id  should not be zero
            valid min: 1
            attributes:
              category: Validity

        - missing_count(customer_id) = 0:
            name:  Customer Id should not be zero
            attributes:
              category: Completeness

        - duplicate_count(customer_id) = 0:
            name:  Customer Id should not be duplicated
            attributes:
              category: Uniqueness

        - avg_length(country) > 2:
            name:  Average length of country more than 2
            attributes:
              category: Accuracy
```

<aside class="callout">
🗣️ In Soda, you can define a title for the check. If none is specified, the system automatically uses the check's name as title.

</aside>


### **Step 5: Apply the manifest**
Once the manifest is complete, apply it using the DataOS CLI:

```bash
dataos-ctl apply -f /path/to/soda-workflow.yaml -w public
```
??? "Click here to view the complete manifest file"
    ```yaml
    name: soda-customer-quality
    version: v1
    type: workflow
    tags:
      - workflow
      - soda-checks
    description: Applying quality checks for the customer data
    workspace: public
    workflow:
      # schedule:
      #   cron: '00 08 * * *'
      #  # endOn: '2023-12-12T22:00:00Z'
      #   concurrencyPolicy: Forbid
      dag:
        - name: soda-customer-quality
          spec:
            stack: soda+python:1.0
            compute: runnable-default
            resources:
              requests:
                cpu: 1000m
                memory: 250Mi
              limits:
                cpu: 1000m
                memory: 250Mi
            logLevel: INFO # WARNING, ERROR, DEBUG
            stackSpec:
              inputs:
                - dataset: dataos://lakehouse:customer_relationship_management/customer_data
                  options:
                    engine: minerva
                    clusterName: miniature
                  profile:
                    columns:
                      - include *
                  checks:  
                    - schema:
                        name: Data type of birth year should be integer
                        fail:
                          when wrong column type:
                            birth_year: bigint
                        attributes:
                          category: Schema

                    - freshness(created_at) < 7d:
                        name: If data is older than 7 days 
                        attributes:
                          category: Freshness
    
                    - invalid_count(customer_id) = 1 :
                        name: Customer Id  should not be zero
                        valid min: 1
                        attributes:
                          category: Validity
    
                    - missing_count(customer_id) = 0:
                        name:  Customer Id should not be zero
                        attributes:
                          category: Completeness

                    - duplicate_count(customer_id) = 0:
                        name:  Customer Id should not be duplicated
                        attributes:
                          category: Uniqueness
    
                    - avg_length(country) > 2:
                        name:  Average length of country more than 2
                        attributes:
                          category: Accuracy
    
    ``` 

    
## Monitoring results 
    
Once these checks are applied, their results will be displayed on Metis. Here, you can monitor the status of the quality checks and ensure they align with your analytical requirements. Each check is categorized as:

- Accuracy: Green checkmark for passed validations.

- Completeness: Alerts for missing values.

- Uniqueness: Warnings for duplicate records.

Click on a specific check to view detailed trend charts, allowing you to analyze data quality metrics over time.


The quality checks displayed in Metis as defined in the Soda YAML manifest file, including their descriptions, as shown in the image below.

![soda_checks_metis.png](/learn/dp_developer_learn_track/quality_check/soda_checks_metis.png)

<aside class="callout">
🗣️ Similarly, define the quality checks for all other input and output datasets. Ensure your folder structure includes an 'output' directory to organize these checks effectively.
</aside>

## Next Step
Once you’ve ensured the quality of your datasets, you can proceed to build the semantic model. If you choose not to include a semantic model in your data product, you can move directly to deploying the data product. Refer to the following links for detailed guidance:

[Building a Semantic Model](/learn/dp_developer_learn_track/create_semantic_model/)

[Deploying a Data Product](/learn/dp_developer_learn_track/create_bundle/)

