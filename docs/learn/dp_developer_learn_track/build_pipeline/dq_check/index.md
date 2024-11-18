# Data quality checks with SODA Stack

Maintaining high data quality is crucial for delivering reliable insights and making informed business decisions. As a Data Product developer, you often encounter issues like missing values, incorrect data formats, or unexpected data inconsistencies. Identifying and resolving these problems proactively is essential to ensure the accuracy and trustworthiness of your data products.

In this module, you'll learn how to leverage Soda Stack within DataOS to implement robust data quality checks. Soda Stack, using Soda Checks Language (SodaCL), allows you to define rules for validating data directly in your workflow, helping you monitor key metrics such as accuracy, completeness, and uniqueness. By the end of this module, you'll be equipped with the skills to set up and automate these checks, ensuring consistent data quality across your datasets.

## Scenario
Imagine you’ve just rolled out a new customer data product, and feedback from the analytics team highlights some discrepancies in the dataset. There are missing customer IDs, duplicate phone numbers, and unexpected fluctuations in row counts, causing concerns about the quality and reliability of the data.

To address these issues, you decide to implement a systematic approach to monitor and enforce data quality checks. You turn to Soda Stack in DataOS, a tool that allows you to define quality checks declaratively using SodaCL. You will set up a workflow to automatically validate key aspects of your customer data, such as ensuring no missing customer numbers and checking for duplicate phone records. This automated solution will help you catch data issues early and maintain the integrity of your data product over time.

Get ready to enhance your data quality process with Soda Stack and streamline your quality checks using DataOS!

## Steps to configure Soda Stack

### **Step 1: Choose the Right Resource for the Job**
The type of DataOS Resource you select depends on the use case:

- **Workflow Resource**: Ideal for batch workloads and periodic quality checks.
- **Worker Resource**: Best suited for long-running, continuous monitoring.

For your initial setup, choose the **Workflow Resource** to run scheduled data quality checks on a dataset.


### **Step 2: Define the Workflow manifest**
Create a Workflow manifest to configure Soda Stack for batch quality checks. Ensure that the metadata and workflow-specific sections are properly defined.

```yaml
# Resource meta section
name: soda-workflow
version: v1
type: workflow
tags:
  - workflow
  - soda-checks
description: Soda workflow
workspace: public

# Workflow-specific section
workflow:
  dag:
    - name: soda-job-v1
      title: Soda checks job
      description: Run data quality checks using Soda Stack
      spec:
        stack: soda+python:1.0
        compute: runnable-default
        resources:
          requests:
            cpu: 1000m
            memory: 100Mi
          limits:
            cpu: 400m
            memory: 400Mi
        logLevel: INFO

        stackSpec:
          inputs:
            - dataset: dataos://icebase:retail/customer
              options:
                engine: minerva
                clusterName: miniature
              checks:
                - row_count between 1 and 170:
                    attributes:
                      title: Row Count Between 1 and 170
                      category: Accuracy
                - missing_count(customer_no) = 0:
                    attributes:
                      category: Completeness
```

### **Step 3: Define Soda checks**

Use **SodaCL**, a YAML-based language, to define custom checks for data quality. Tailor the checks to address issues identified by your team:

- **Accuracy**: Ensures row counts fall within an acceptable range.
- **Completeness**: Verifies that critical fields have no missing values.
- **Uniqueness**: Checks for duplicate records in specific columns.

```yaml
stackSpec:
  inputs:
    - dataset: dataos://icebase:retail/customer
      checks:
        - row_count between 1 and 170:
            attributes:
              title: Row Count Between 1 and 170
              category: Accuracy
        - missing_count(customer_no) = 0:
            attributes:
              category: Completeness
        - duplicate_count(phone) = 0:
            attributes:
              category: Uniqueness
```
### **Step 4: Configure profiling (Optional)**

Enable profiling to gather insights into the dataset’s characteristics and data distribution. Specify the columns to be profiled in the manifest. Wildcard Matching: Use "*" to profile all columns in the dataset.

```yaml
stackSpec:
  inputs:
    - dataset: dataos://distribution:distribution/dc_info
      profile:
        columns:
          - "*"
```

### **Step 5: Apply the manifest**
Once the manifest is complete, apply it using the DataOS CLI:

```bash

dataos-ctl apply -f /path/to/soda-workflow.yaml -w public
```
Verify the configuration in the Data Product Hub’s **Quality** tab, where the status of Soda checks is displayed.

## Monitoring results in the Quality tab

After applying the configuration, use the Quality tab in Metis to monitor the results of your checks. Each check is categorized as:

**Accuracy**: Green checkmark for passed validations.

**Completeness**: Alerts for missing values.

**Uniqueness**: Warnings for duplicate records.


Click on a specific check to view detailed trend charts, allowing you to analyze data quality metrics over time.