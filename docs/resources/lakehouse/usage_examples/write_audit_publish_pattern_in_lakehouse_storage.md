# How to ensure high data quality in Lakehouse Storage using the Write-Audit-Publish pattern?

Ensuring the highest standard of data quality is imperative for extracting valuable insights. Compromises in data quality at any stage within a data engineering workflow can detrimentally impact downstream analyses, including Business Intelligence (BI) and predictive analytics.

Take, for instance, an Extract, Transform, and Load (ETL) process. This process involves moving data from an operational system, such as a relational database, to an analytical system like DataOS Lakehouse storage (Icebase Depot), for utilization in BI reporting or ad-hoc analysis. If the original data contains duplicates or inconsistencies, or if such issues arise during the ETL process and are not resolved before the data is integrated into the production analytics environment, the integrity of insights derived could be compromised, leading to potentially erroneous decisions. This underscores the paramount importance of maintaining data quality throughout data engineering processes. Ensuring data accuracy, consistency, and reliability is not merely theoretical but a practical imperative.

The **Write-Audit-Publish (WAP) pattern** offers a structured method to guarantee data quality. This approach can be broken down into three key stages:

1. **Write:** Initially, data is extracted from its sources and stored in a designated non-production area. This step serves to protect production data from potential quality issues.
2. **Audit:** In this stage, the staged data is subjected to comprehensive validation checks. These checks may include the examination of null values, identification of duplicates, verification of data types, and ensuring data integrity.
3. **Publish:** Once the data has passed validation, it is seamlessly integrated into production tables. This ensures that end-users either have access to the entire, updated dataset or none of it, preserving data integrity.

Below, we'll explore how to implement this framework within the context of DataOS Lakehouse Storage (alternatively known as Icebase Depot) using Iceberg tables’ branching capability.

## WAP Using Iceberg’s Branching Capability

Although there is more than one way to implement WAP in Iceberg, we will focus on an approach using Iceberg’s table-level branching capabilities. 

Branching in Iceberg works similarly to Git branches where you can create local branches from the production table (main branch) to carry out isolated data work on the table. The core Iceberg component behind a branch is the snapshot, which describes the state of an Iceberg table at a certain point in time. Branches are named references to these snapshots. 

## Problem Statement

Let’s imagine that product sales data from an e-commerce company is regularly extracted from operational systems, such as relational database management systems (Postgres Database, MySQL Database, etc.), and is then loaded into the company’s cloud data lake (AWS S3, GCS, WASBS, ABFSS). The data engineering team is responsible for creating and maintaining Iceberg tables in the data lake, which serves as the base dataset to cater to different production applications such as BI reports and predictive models. 

How can they ensure the quality of the data before pushing it into the production environment? 

## Solution Approach

The solution involves utilizing Iceberg's branching capability to implement the WAP pattern as follows:

1. **Create a New Branch:** Initiate the process by creating a new branch (let’s say `stage`) using the DataOS CLI, off the production Iceberg table (`main` branch). This branch acts as a working area that is isolated from the main production data, ensuring no disruptions to the main data flow.
2. **Ingest New Records:** Load the new or updated records onto this newly created branch using the Flare Stack. This step is crucial for staging the data, allowing for thorough validation before it is considered for production.
3. **Conduct Data Validation:** Perform rigorous data validation checks on the staged data using the Soda Stack. These checks might include verifying data accuracy, consistency, completeness, and ensuring it meets all predefined quality standards.
4. **Publish to Main Branch:** Upon successful validation, merge the new data from the branch into the main production branch by using the cherrypick-snapshot command of the DataOS CLI. This step ensures that only quality-assured data is added to the production environment.
5. **Handle Validation Failures:** If the data fails any validation checks, the branch can be dropped. You can also set up Monitors and Pagers on these for notification. This allows for the rectification of issues and reattempting of the process without any impact on the production data.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/215a8e78-890f-4ae1-8790-724fad621927/c6db25bd-112b-4033-89c8-e80103079d2a/Untitled.png)

### **Prerequisites**

- Operational Data Source - Postgres Depot
- Analytical Data Source - Lakehouse Storage (Icebase Depot)

### **Create a branch**

First, let’s create a new branch named `stage` from the existing Iceberg table. This branch will act as the staging area for the new data.

Use the create-branch command to create a new branch within a dataset at a specified location within DataOS Lakehouse Storage (Icebase):

```yaml
# Create a Branch on the Table called 'stage'
dataos-ctl dataset create-branch -a dataos://icebase:retail/customer -b stage
```

### **List Branch**

```python
# List all Table References
dataos-ctl dataset list-branch -a dataos://icebase:retail/customer
```

### **List Branch Snapshots**

This command lists all snapshots associated with a specific branch within a dataset at a specified location in DataOS.

```bash
dataos-ctl dataset snapshots -a dataos://icebase:retail/customer -b stage
```

**Flags:**

- `-a` or `--address`: Specifies the dataset location.
- `-b` or `--branch`: Specifies the name of the new branch to be created

### **Write the data**

For ETL, we will be using the Flare Stack. A couple of preparatory steps are required before we begin using the WAP method for ingesting new data. 

<aside>
🗣 To be completed!!

</aside>

#### **Flare Job configuration**

- Within the Flare Job, while we can configure the inputs for Postgres Database from the following link. The output section need some special configuration as shown below.
    - add the iceberg table property `write.wap.enabled=true` . This step prepares our Iceberg table to follow the WAP pattern.
    - After that to make sure that the writing action target this specific branch directly, we use the branch attribute and set to assign the Branch identifier `stage` to the Flare configuration

```yaml
outputs:
  - name: cities
    dataset: dataos://icebase:retail/customer
    format: ICEBERG
    options:
      iceberg:
        write.wap.enabled: true
      extraOptions:
        branch: stage
      saveMode: append
```

Now we are ready to run the ETL job to ingest new records to this specific branch of the table. The manifest file for the same is provided below.

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
	                iceberg:
		                write.wap.enabled: true
                  extraOptions:
                    branch: stage
                  saveMode: append
            steps:
              - sequence:
                  - name: output01
                    sql: SELECT * FROM source_data limit 20
```

Remember that this branch acts as a standalone variant of the production data. Any action taken on this branch affects only this dataset, not the main one. You can validate your production table by querying the record count on the main branch. You should see that this query returns the same count we had originally, telling us the main branch is unchanged:

```bash
# Count of Records on the Main Branch
spark.sql("SELECT COUNT(*) as total_records FROM catalog.db.table VERSION AS OF
'main'").show()
```

## Audit the data

After writing the new data into the isolated local branch, etl_branch, it is essential to ensure that this new dataset stands up to the organization’s quality standards. The audit phase acts as a checkpoint where we subject our data to rigorous evaluation, ensuring its fitness for purpose. The audit process offers the flexibility to write native code or incorporate third-party tools tailored to validate data quality checks. We will perform a few basic data quality checks for this exercise. 

### NULL values.

First let’s use PySpark to see if there are any null values in the table:

### Date consistency.

The final data quality validation we want to perform on this new dataset is date consistency. When dealing with time-series data or records with timestamped entries, it is critical to ensure that every date in the dataset is valid and falls within a predefined, acceptable range. For example, let’s assume that the data we ingested represents the period of January 2024. The number of records whose `date_column` values are in this period should equal the number of records added. Let’s quickly write some code to do this:

```bash
# df = dataframe with our "catalog.db.table" table
# Define your date range
start_date = datetime(2024, 1, 1) # for example, Jan 1, 2024
end_date = datetime(2024, 1, 31) # for example, Jan 31, 2024
# Convert the date column to date type if it's not already
df = df.withColumn("date_column", col("date_column").cast("date"))
# Filter the DataFrame to find records within the date range
within_range = df.filter((col("date_column") >= start_date) & (col("date_col
umn") <= end_date))
# Count the records that fall within the desired date range
count_within_range = within_range.count()
```

We compare this count to the difference between the count of the records on the main branch and the count on etl_branch. If they don’t match, we can inspect whether any records have incorrect dates or null dates causing the inconsistency. 

We have gone through three examples of data quality checks we can run on an isolated branch. During these checks, the yet-to-be validated data was not being scanned by incoming queries that would query the main branch, which will only have validated data. The ability to perform these quality checks flexibly in an isolated branch without impacting anything in production is a critical capability in Apache Iceberg.
By using this approach, we end up with a couple of benefits:
**Enhanced data quality**
Production environments are not exposed to unverified data, preventing incorrect results and decisions. This eliminates the rush to correct data errors, reducing the risk of additional mistakes during the fixing process.
**Efficient data handling**

Compared to the traditional way of using a staging table for quality checks, the need for data copies is eliminated, saving resources and ensuring efficiency. This enables the easy identification of issues, such as duplicate data, that are often missed when just checking new data.
**Applying fixes.** 

At this stage, you can take a couple of actions, such as communicating about the anomalies with the required stakeholders, reviewing the ETL job, determining the origin of the anomalies, and applying some quick fixes. As a basic remediation step, let’s create two DataFrames—one with records needing remediation, which we can save to another table or write to a file to give to stakeholders, and another comprising validated records that we can overwrite the table with so that it only has validated records:

Now our branch has new validated records, and we’ve shipped off the invalid records to our stakeholders, who can fix them for later backfilling.

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

### Publish the changes

The final operation in the WAP pattern is to publish the changes and make the data available to the production environment so that downstream applications can use it. The publish operation in Iceberg is made possible by the cherry-pick procedure. In Spark, the cherrypick_snapshot() procedure produces a new snapshot based on a previous one, all the while preserving the original without any changes or deletions.
For our use case, we can select a specific snapshot, the branch (ETL_branch), to form a new snapshot. What sets cherry-picking apart is that it is a metadata-only operation. This implies that the actual datafiles remain untouched and only the metadata references are altered. As a result, we’re essentially making the new data available in the production table without the need to relocate any datafiles. One limitation to note is that cherry-picking caters to a single commit. To run this procedure, we will need to provide the snapshot ID as an argument to the method. Let’s find out the snapshot ID associated with etl_branch by querying a metadata table called refs, meaning references:

```bash
#Query The List of References for the Table
spark.sql("SELECT * FROM catalog.db.table.refs")
```

This will return our list of references (branches and tags), and we can see the current snapshot ID for each branch, which is the information we need. Now let’s execute the cherry_pick() procedure:

```bash
#Cherry-picking the snapshot from 'etl_branch' over to 'main'
spark.sql("CALL catalog.system.cherrypick_snapshot('db.table',
2668401536062194692)").show()
```

Once the operation runs successfully, our main branch’s current snapshot will be made the same snapshot at the current etl_branch snapshot. This means we have made the newly inserted records in etl_branch available to the main branch for production usage. If we now query the record count on main and etl_branch, we should see they are identical:

```bash
# Record count on the 'main' branch
spark.sql("SELECT count(*) FROM catalog.db.table VERSION AS OF 'main'").show();
# Record count on the 'etl_branch' branch
spark.sql("SELECT count(*) FROM catalog.db.table VERSION AS OF 'etl_bran
ch'").show();
```

To conclude this particular WAP session associated with the branch, we’ll remove the specific Spark configuration property, spark.wap.branch. This ensures that all the subsequent reads and writes don’t explicitly happen from this branch but from the main branch of the table:

```bash
#Turn off the WAP feature
spark.conf.unset('spark.wap.branch')
```

In this use case, we reviewed how to leverage the WAP data quality pattern in Apache Iceberg to address the challenges of dealing with data quality at scale. With WAP, before committing data to the production environment, there’s a structured mechanism to write, assess for quality concerns, and finalize or discard the data. This method preserves the reliability of the data, ensuring that what drives business decisions is accurate, consistent, and free from anomalies. If you need to isolate changes across multiple tables, catalog-level branches can be created for a similar pattern using the Nessie catalog.

List branch snapshots

```yaml
dataos-ctl dataset snapshots -a dataos://icebase:retail/city -b stage
```

Cherry Pick 

```yaml
dataos-ctl dataset cherrypick-snapshot -a dataos://icebase:retail/city -sid 8018697
```