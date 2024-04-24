# How to ensure high data quality in Lakehouse Storage using the Write-Audit-Publish pattern?

Ensuring the highest standard of data quality is imperative for extracting valuable insights. Compromises in data quality at any stage within a data engineering workflow can detrimentally impact downstream analyses, including Business Intelligence (BI) and predictive analytics.

Take, for instance, an Extract, Transform, and Load (ETL) process. This process involves moving data from an operational system, such as a relational database, to an analytical system like DataOS Lakehouse storage (Icebase Depot), for utilization in BI reporting or ad-hoc analysis. If the original data contains duplicates or inconsistencies, or if such issues arise during the ETL process and are not resolved before the data is integrated into the production analytics environment, the integrity of insights derived could be compromised, leading to potentially erroneous decisions. This underscores the paramount importance of maintaining data quality throughout data engineering processes. Ensuring data accuracy, consistency, and reliability is not merely theoretical but a practical imperative.

The **Write-Audit-Publish (WAP) pattern** offers a structured method to guarantee data quality. This approach can be broken down into three key stages:

1. **Write:** Initially, data is extracted from its sources and stored in a designated non-production or staged area. This step serves to protect production data from potential quality issues.
2. **Audit:** In this stage, the staged data is subjected to comprehensive validation checks. These checks may include the examination of null values, identification of duplicates, verification of data types, and ensuring data integrity.
3. **Publish:** Once the data has passed validation, it is seamlessly integrated into production tables. This ensures that end-users either have access to the entire, updated dataset or none of it, preserving data integrity.

Below, we'll explore how to implement this framework within the context of DataOS Lakehouse Storage (alternatively known as Icebase Depot) using Iceberg tables’ branching capability.

## WAP Using Iceberg’s Branching Capability

Although there is more than one way to implement WAP in Iceberg, we will focus on an approach using Iceberg’s table-level branching capabilities. 

Branching in Iceberg works similarly to Git branches where you can create local branches from the production table (`main` branch) to carry out isolated data work on the table. The core Iceberg component behind a branch is the snapshot, which describes the state of an Iceberg table at a certain point in time. Branches are named references to these snapshots. 

## Problem Statement

Let’s imagine that product sales data from an e-commerce company is regularly extracted from an operational systems, such as relational database management systems (Postgres Database, MySQL Database, etc.), and is then loaded into the company’s cloud data lake (AWS S3, GCS, WASBS, ABFSS). The data engineering team is responsible for creating and maintaining Iceberg tables in the data lake, which serves as the base dataset to cater to different production applications such as BI reports and predictive models. 

How can they ensure the quality of the data before pushing it into the production environment? 

## Solution Approach

The solution involves utilizing Iceberg's branching capability to implement the WAP pattern as follows:

1. **Create a New Branch:** Initiate the process by creating a new branch (let’s say `stage`) using the DataOS CLI, off the production Iceberg table (`main` branch). This branch acts as a working area that is isolated from the main production data, ensuring no disruptions to the main data flow.
2. **Ingest New Records:** Load the new or updated records onto this newly created branch using the Flare Stack. This step is crucial for staging the data, allowing for thorough validation before it is considered for production.
3. **Conduct Data Validation:** Perform rigorous data validation checks on the staged data using the Soda Stack. These checks might include verifying data accuracy, consistency, completeness, and ensuring it meets all predefined quality standards.
4. **Publish to Main Branch:** Upon successful validation, merge the new data from the `stage` branch into the main production branch by using the cherrypick-snapshot command of the DataOS CLI. This step ensures that only quality-assured data is added to the production environment.
5. **Handle Validation Failures:** If the data fails any validation checks, the branch can be dropped. You can also set up Monitors and Pagers on these for notification. This allows for the rectification of issues and reattempting of the process without any impact on the production data.


### **Prerequisites**

- Operational Data Source - Postgres Depot
- Analytical Data Source - Lakehouse Storage (Icebase Depot)
- Dataset - `dataos://icebase:retail/customer`

### **Create a branch**

First, let’s create a new branch named `stage` from the existing Iceberg dataset. This branch will act as the staging area for the new data.

Use the create-branch command to create a new branch within a dataset at a specified location within DataOS Lakehouse Storage (Icebase):

```shell
# Create a Branch on the dataset called 'stage'
dataos-ctl dataset create-branch -a dataos://icebase:retail/customer -b stage
```

### **List Branch**

```shell
# List all Table References
dataos-ctl dataset list-branch -a dataos://icebase:retail/customer
```

### **List Branch Snapshots**

This command lists all snapshots associated with a specific branch within a dataset at a specified location in DataOS.

```bash
dataos-ctl dataset snapshots -a dataos://icebase:retail/customer -b stage
```

### **Write the data**

For ETL, we will be using the Flare Stack. A couple of preparatory steps are required before we begin using the WAP method for ingesting new data. 

#### **Flare job configuration**

The configuration of the Flare job involves specifying input sources and customizing output settings to direct the data specifically to the desired branch. Here is a detailed breakdown of how to configure and run an ETL job using the Flare Stack:

- **Input Configuration:** Start by configuring the input to read data from a Postgres Depot. To know more about the configuation, refer to the link: Flare Postgres Read configuration.
- **Output Configuration:** The output needs special attention to ensure data is written to the correct branch. Set the branch attribute in the Flare configuration to direct the writing action to the `stage` branch specifically.

Below is a sample manifest file for an ETL job that ingests new records into a specific staging branch of an Iceberg dataset:

```yaml
name: lakehouse-storage-write
version: v1
type: workflow
tags:
  - lakehouse
  - storage
  - icebase
  - depot
  - write
description: The job ingests data from operational source depots to DataOS Lakehouse storage (or Icebase depot) in the staging branch
workflow:
  dag:
    - name: source-read-lakehouse-write
      title: Write to Lakehouse Storage from source Depot
      description: The job ingests city data from dropzone into raw zone
      spec:
        tags:
          - Connect
          - City
        stack: flare:5.0
        compute: runnable-default
        stackSpec:
          job:
            explain: true
            inputs:
              - name: source_data
                dataset: dataos://postgresdepot:retail/customer
                format: postgres
                options:
                  driver: org.postgres.driver
            logLevel: INFO
            outputs:
              - name: output01
                dataset: dataos://icebase:retail/customer
                format: ICEBERG
                options:
                  extraOptions:
                    branch: stage
                  saveMode: append
            steps:
              - sequence:
                  - name: output01
                    sql: SELECT * FROM source_data
```

Remember that this branch acts as a standalone variant of the production data. Any action taken on this branch affects only this dataset, not the main one. You can validate your production table by querying the record count on the main branch. You should see that this query returns the same count we had originally, telling us the main branch is unchanged:

```sql
--- Count of Records on the Main Branch
SELECT COUNT(*) as total_records FROM catalog.db.table VERSION AS OF 'main'
```

### **Audit the data**

After writing the new data into the isolated branch, stage, it is essential to ensure that this new dataset stands up to the organization’s quality standards. The audit phase acts as a checkpoint where we subject our data to rigorous evaluation, ensuring its fitness for purpose. We will perform a few basic data quality checks for this exercise using the DataOS Soda Stack. 

```yaml
name: soda-workflow-sample-v01
version: v1
type: workflow
tags:
  - workflow
  - soda-checks
description: Customer
workspace: public
workflow:
  dag:
    - name: soda-job-v1
      description: This is sample job for soda dataos sdk
      title: soda Sample Test Job
      spec:
        stack: soda:1.0
        logLevel: INFO
        compute: runnable-default
        resources:
          requests:
            cpu: 1000m
            memory: 250Mi
          limits:
            cpu: 1000m
            memory: 250Mi
        stackSpec:
          inputs:
            - dataset: dataos://icebase:retail/customer
              options:
                engine: minerva
                clusterName: miniature
                branchName: stage
              checks:
                - row_count between 10 and 1000
                - row_count between (10 and 55)
                - missing_count(birthdate) = 0
                - invalid_percent(phone_number) < 1 %:
                    valid format: phone number
                - invalid_count(number_of_children) < 0:
                    valid min: 0
                    valid max: 6
                - min(age) > 30:
                    filter: marital_status = 'Married'
                - duplicate_count(phone_number) = 0
                - row_count same as city
                - duplicate_count(customer_index) > 10
                - duplicate_percent(customer_index) < 0.10
                - failed rows:
                    samples limit: 70
                    fail condition: age < 18  and age >= 50
                - failed rows:
                    fail query: |
                      SELECT DISTINCT customer_index
                      FROM customer as customer
                - freshness(ts_customer) < 1d
                - freshness(ts_customer) < 5d
                - max(age) <= 100
                - max_length(first_name) = 8
                - values in (occupation) must exist in city (city_name)
                - schema:
                    name: Confirm that required columns are present
                    warn:
                      when required column missing: [first_name, last_name]
                    fail:
                      when required column missing:
                        - age
                        - no_phone
```

### **Applying fixes.** 

At this stage, you can take a couple of actions, such as communicating about the anomalies with the required stakeholders, reviewing the ETL job, determining the origin of the anomalies, and applying some quick fixes. 

Now our branch has new validated records, and we’ve shipped off the invalid records to our stakeholders, who can fix them for later backfilling.


### **Publish the changes**

The final operation in the WAP pattern is to publish the changes and make the data available to the production environment so that downstream applications can use it. The publish operation in Iceberg is made possible by the cherry-pick procedure. In DataOS, the `cherrypick-snapshot` procedure produces a new snapshot based on a previous one, all the while preserving the original without any changes or deletions. For our use case, we can select a specific snapshot, the branch (stage), to form a new snapshot. What sets cherry-picking apart is that it is a metadata-only operation. This implies that the actual datafiles remain untouched and only the metadata references are altered. As a result, we’re essentially making the new data available in the production table without the need to relocate any datafiles. One limitation to note is that cherry-picking caters to a single commit. To run this procedure, we will need to provide the snapshot ID as an argument to the method. Let’s find out the snapshot ID associated with `stage` by querying a metadata table called refs, meaning references:

List branch snapshots

```shell
dataos-ctl dataset snapshots -a dataos://icebase:retail/city -b stage
```

or you can query the 'refs' metadata table from the DataOS Workbench app.

```sql
--- Query The List of References for the Table
SELECT * FROM catalog.db.table.refs
```

This will return our list of references (branches and tags), and we can see the current snapshot ID for each branch, which is the information we need. Now let’s execute the cherry_pick() procedure:

```shell
dataos-ctl dataset cherrypick-snapshot -a dataos://icebase:retail/city -sid 8018697
```

Once the operation runs successfully, our main branch’s current snapshot will be made the same snapshot at the current `stage` snapshot. This means we have made the newly inserted records in `stage` available to the `main` branch for production usage. If we now query the record count on `main` and `stage`, we should see they are identical:

```sql
--- Record count on the 'main' branch
SELECT count(*) FROM catalog.db.table VERSION AS OF 'main'
```

```sql
--- Record count on the 'stage' branch
SELECT count(*) FROM catalog.db.table VERSION AS OF 'stage'
```

In this use case, we reviewed how to leverage the WAP data quality pattern in Apache Iceberg to address the challenges of dealing with data quality at scale. With WAP, before committing data to the production environment, there’s a structured mechanism to write, assess for quality concerns, and finalize or discard the data. This method preserves the reliability of the data, ensuring that what drives business decisions is accurate, consistent, and free from anomalies. 