# Implementing quality checks to maintain data integrity

In this section, you’ll learn how to implement quality checks for input data before building a data product. These checks help ensure that the data is accurate, complete, and ready for reliable analysis.

## Scenario

As a data engineer, you’re working with datasets and exploring them on Workbench and Metis. Before using this data to create a data product, you need to validate its quality. Your task is to set up checks that verify the data's accuracy, completeness, and consistency, ensuring it meets the necessary standards for consumer use.

### **Define service level objectives (SLOs)**

In the build stage, you and other stakeholders must have defined SLOs for your data product. These are measurable quality goals for the data that define what "good quality" means for your data product.

Suppose the following are the SLOs you and other stakeholders have decided:

- **Accuracy**: 99% of data points must be accurate.
- **Completeness**: No more than 1% of records can have missing values.
- **Freshness**: Data must be updated within the last 24 hours.
- **Schema**: 100% of records must adhere to the expected schema.
- **Uniqueness**: 0.5% of records should be duplicated at maximum.
- **Validity**: 95% of records must meet all domain-specific rules.

### **Create a quality directory structure**

Once your **SLOs** are defined, you can organize your quality check workflows. Create a quality directory to ensure that your data product's input meets the SLOs' requirements. Inside this folder, you'll organize your checks by creating subdirectories named **input**. Each subdirectory will contain the specific **SODA** check workflows for each input dataset (e.g., `customer.yml`, `product.yml`, `purchase.yml`).

Here’s an example of how your folder might look:

```bash
quality/
│  ├── input/
│     ├── customer.yml
│     ├── product.yml
│     └── purchase.yml

```

This structure helps you keep your quality checks organized and aligned with the defined SLOs for each input dataset.

### **Define quality checks with SODA**

With your **SLOs** in place, the next step is to define the quality checks to ensure your data meets the established standards. These quality checks are essential to monitor and maintain the quality of your data. Below are the key quality checks available to you:

- **Accuracy**: Ensures the data values are correct and fall within expected ranges.
- **Completeness**: Checks for missing values or incomplete records, ensuring no critical data is omitted.
- **Freshness**: Verifies that the dataset is up to date, maintaining the reliability and timeliness of the data.
- **Schema**: Ensures the data's structure matches the expected formats, such as correct data types and column names.
- **Uniqueness**: Checks for duplicate records, ensuring each data point is unique within the dataset.
- **Validity**: Ensures the data meets business rules or domain-specific constraints, confirming that it aligns with predefined logic.

Each rule will accompany the status of the **last five runs**, allowing you to monitor recent check results and track ongoing compliance with your SLOs.

These checks will be implemented using the **SODA** framework and defined in YAML files for each dataset. Once these checks are specified, they will be populated on platforms like **Metis** and **Data Product Hub**, where data consumers can view the status of the data quality checks and align them with their analytical needs.

For example, if you’re defining quality checks for a **customer dataset**, your YAML file might include the following checks:

- **Schema**: The data type of birth year should be an integer.
- **Accuracy**: The average length of a country is more than 6.
- **Completeness**: Customer ID should not be zero.
- **Validity**: Customer ID should not be null.
- **Uniqueness**: Customer ID should be unique.

For the above checks, the SODA workflow yaml manifest will look like as follows:

- **customer.yml**
    
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
                - dataset: dataos://icebase:customer_relationship_management/customer
                  options:
                    engine: minerva
                    clusterName: system
                  profile:
                    columns:
                      - include *
                  checks:  
                    - schema:
                        name: Data type of birth year should be integer
                        fail:
                          when wrong column type:
                            birth_year: string
                        attributes:
                          category: Schema
     
                    - invalid_count(customer_id) = 0 :
                        name: Customer Id  should not be null
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
     
                    - avg_length(country) > 6:
                        name:  Average length of country more than 6
                        attributes:
                          category: Accuracy
     
    ```
    

Each quality check is displayed in **Metis** as defined in the **SODA** YAML manifest file. The description of the check, as specified in the YAML file, is shown on the platform, as illustrated in the image below.

![soda_checks_metis.png](/learn/dp_developer_learn_track/quality_check/soda_checks_metis.png)

Similarly, these checks are also populated on the **Data Products Hub**, as shown in the example below.

*The Quality checks populating in the Quality tab of the Data Product Hub*

![quality_tab.png](/learn/dp_developer_learn_track/data_api/quality_tab.png)

<aside class="callout">
🗣️ In SODA, you have an attribute to define the title, but if a title is not explicitly defined in the YAML file, the system will automatically use the check's name as the title. This name will then appear in the **Check** section.

</aside>

Similarly, you decide to define the following checks for the Purchase table:

- **Freshness**: This check ensures the **purchase_date** is within the last 2 days. If the data is older than 2 days, this check will fail, indicating that the dataset is stale and may need to be refreshed.
- **Schema**: The schema check verifies that the **recency** column has the correct data type. Specifically, it should be an integer; if the column is mistakenly typed as a string, the check will fail, highlighting the issue.
- **Validity**: This check ensures that the count of invalid entries in the **mntwines** column is within a specified range (between 0 and 1). The check will flag the dataset as invalid if the count falls outside this range.
- **Purchase.yml**
    
    ```yaml
    name: soda-purchase-quality
    version: v1
    type: workflow
    tags:
      - workflow
      - soda-checks
    description: Applying quality checks for the purchase data
    workspace: public
    workflow:
      dag:
        - name: soda-purchase-quality-job
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
                - dataset: dataos://icebase:customer_relationship_management/purchase
                  options:
                    engine: minerva
                    clusterName: system
                  profile:
                    columns:
                      - include *
                  checks:  
                    - freshness(purchase_date) < 2d:
                        name: If data is older than 2 days 
                        attributes:
                          category: Freshness
    
                    - schema:
                        name: Data type of recency should be integer
                        fail:
                          when wrong column type:
                            recency: string
                        attributes:
                          category: Schema
     
                    - invalid_count(mntwines) < 0:
                        valid min: 0
                        valid max: 1
                        attributes:
                          category: Validity
                        title: Invalid count of mntwines
    ```