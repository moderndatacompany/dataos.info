# Attributes of Soda Stack YAML

## Structure of YAML

```yaml
stackSpec:
  inputs:
    # Redshift
    - dataset: dataos://redshiftdepot:public/redshift_write_12
      checks:
        - row_count between 10 and 1000:
            attributes:
              category: Accuracy

    # Oracle
    - dataset: dataos://oracledepot:dev/oracle_write_12
      checks:
        - row_count between 10 and 1000:
            attributes:
              category: Accuracy
    # MySql
    - dataset: dataos://mysqldepot:tmdc/mysql_write_csv_12
      checks:
        - row_count between 10 and 1000:
            attributes:
              category: Accuracy
    # MSSQL
    - dataset: dataos://mssqldepot:tmdc/mssql_write_csv_12
      checks:
        - row_count between 10 and 1000:
            attributes:
              category: Accuracy
    # Minerva
    - dataset: dataos://icebase:retail/customer
      options:
        engine: minerva
        clusterName: miniature
        branchName: test
      filter:
        name: filter_on_age
        where: age > 50
      profile:
        columns:
          - customer_index
          - exclude email_id
          - include d*
          - e*
      checks:
        - row_count between 10 and 1000:
            attributes:
              category: Accuracy
        - row_count between (10 and 55):
            attributes:
              category: Accuracy
        - missing_count(birthdate) = 0:
            name: Compelteness of the birthdate column
            attributes:
              title: Completeness of the Birthdate Column
              category: Completeness

        # - invalid_percent(phone_number) < 1 %:
        #     valid format: phone number
        - invalid_count(number_of_children) < 0:
            valid min: 0
            valid max: 6
            attributes:
              category: Validity
        - min(age) > 30:
            filter: marital_status = 'Married'
            attributes:
              category: Accuracy
        - duplicate_count(phone_number) = 0:
            attributes:
              category: Uniqueness
        - row_count same as city:
            name: Cross check customer datasets
            attributes:
              category: Accuracy
        - duplicate_count(customer_index) > 10:
            attributes:
              category: Uniqueness
        - duplicate_percent(customer_index) < 0.10:
            attributes:
              category: Uniqueness
        # - failed rows:
        #     samples limit: 70
        #     fail condition: age < 18  and age >= 50
        # - failed rows:
        #     fail query: |
        #       SELECT DISTINCT customer_index
        #       FROM customer as customer
        - freshness(ts_customer) < 1d:
            name: Freshness01
            attributes:
              title: Freshness of the last commit
              category: Freshness
        - freshness(ts_customer) < 5d:
            name: Freshness02
            attributes:
              category: Freshness
        - max(age) <= 100:
            attributes:
              category: Accuracy
        - max_length(first_name) = 8:
            attributes:
              category: Accuracy
        - values in (occupation) must exist in city (city_name):
            attributes:
              category: Accuracy

        - schema:
            name: Confirm that required columns are present
            warn:
              when required column missing: [first_name, last_name]
            fail:
              when required column missing:
                - age
                - no_phone
            attributes:
              category: Schema
        - schema:
            warn:
              when forbidden column present: [Voldemort]
              when wrong column type:
                first_name: int
            fail:
              when forbidden column present: [Pii*]
              when wrong column type:
                number_of_children: DOUBLE
            attributes:
              category: Schema
    # Postgres
    - dataset: dataos://postgresdepot:public/classification
      checks:
        - row_count between 0 and 1000:
            attributes:
              category: Accuracy
    # Big Query
    - dataset: dataos://bigquerydepot:distribution/dc_info
      checks:
      - row_count between 0 and 1000:
            attributes:
              category: Accuracy
    # Snowflake
    - dataset: dataos://snowflakedepot:TPCH_SF10/CUSTOMER
      options: # this option is default no need to set, added for example.
        engine: default
      checks:
        - row_count between 10 and 1000:
            attributes:
              category: Accuracy      
```

## Configuration Attributes

## **`stackSpec`**

**Description:** Specification for the Soda Stack, including inputs for various datasets and associated checks.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | mandatory | none | none |

**Example Usage:**

```yaml
stackSpec:
  inputs:
    # ... (list of dataset inputs and checks)
```

---

### **`inputs`**

**Description:** Within the `inputs` section users define the datasets or data sources on which data quality assessments will be performed, along with associated checks.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of mappings | mandatory | none | none |

**Example Usage:**

```yaml
stackSpec:
  inputs:
    - dataset: dataos://sanityredshift:public/redshift_write_12
      checks:
        - row_count between 10 and 1000:
            attributes:
              category: Accuracy
    # ... (other dataset inputs)
```

---

### **`dataset`**

**Description:** Dataset specification, including the source and path. Specify the data source or dataset on which you want to run data quality checks.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | dataset UDL path |

**Example Usage:**

```yaml
stackSpec:
  inputs:
    - dataset: dataos://sanityredshift:public/redshift_write_12
      # ...
```

---

### **`checks`**

**Description:** List of checks associated with the dataset input. Here you will specify a list of specific data quality checks or tests that will be performed on the designated dataset. These checks can be tailored to suit the unique requirements of the dataset and the data quality objectives. 

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of mappings | mandatory | none | none |

**Example Usage:**

```yaml
stackSpec:
  inputs:
    - dataset: dataos://sanityredshift:public/redshift_write_12
      checks:
        - row_count between 10 and 1000:
            attributes:
              category: Accuracy
    # ... (other checks for the dataset)
```

---




### **`name`**

**Description:**  Name of the check.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
|  string | mandatory | none | none |

```yaml
stackSpec:
  inputs:
    - dataset: dataos://sanityredshift:public/redshift_write_12
      checks:
        - row_count between 10 and 1000:
            name: row count 
            attributes:
              category: Accuracy
    # ... (other checks for the dataset)
```

---

### **`attributes`**

**Description:**  Additional metadata that describes or categorizes the check, such as accuracy, completeness, or consistency.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of mappings | mandatory | none | none |

```yaml
stackSpec:
  inputs:
    - dataset: dataos://sanityredshift:public/redshift_write_12
      checks:
        - row_count between 10 and 1000:
            attributes:
              category: Accuracy
    # ... (other checks for the dataset)
```

---

### **`title`**

**Description:**  A descriptive title for the specific check being applied. It is used to give a human-readable name to the check, as the check itself may have a technical name or underscores (e.g., row_count).

| Data Type | Requirement | Default Value | Possible Value |
| --------- | ----------- | ------------- | -------------- |
|   string  |   optional  |     none      |     none       |

```yaml
stackSpec:
  inputs:
    - dataset: dataos://sanityredshift:public/redshift_write_12
      checks:
        - row_count between 10 and 1000:
            attributes:
              title: Row Count between 10 and 1000
              category: Accuracy
    # ... (other checks for the dataset)
```

**Additional Information:**

The system takes the `title` attribute as the first priority for Display Name. If the title is not present, the `name` attribute is displayed. 

---



### **`category`**

**Description:**  The category under which the check falls, such as Freshness, Accuracy, etc.	


| Data Type | Requirement | Default Value | Possible Value |
| --------- | ----------- | ------------- | -------------- |
|   string  |   optional  |     none      |     none       |


```yaml
stackSpec:
  inputs:
    - dataset: dataos://sanityredshift:public/redshift_write_12
      checks:
        - row_count between 10 and 1000:
            attributes:
              title: Row Count between 10 and 1000
              category: Accuracy
    # ... (other checks for the dataset)
```

**Additional Information**

It is necessary to add the category of the checks, as this allows the category to be populated in the [Data Product Hub (DPH)](/interfaces/data_product_hub/). By specifying a category, checks are better organized and easily searchable, ensuring that users can quickly understand the type of validation being applied. There are total six types of categories of check:

  - Freshness
  - Schema
  - Validity
  - Completeness
  - Uniqueness
  - Accuracy

---

### **`options`**

**Description:** Options associated with the dataset input, such as the engine or cluster name. Here, you can configure how you want to connect to the data source and run the check. Pass the following information - 


| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | optional | none | mapping containing options in key-value pairs |

**Example Usage:**

```yaml
stackSpec:
  inputs:
    - dataset: dataos://icebase:retail/customer
      options:
        engine: minerva
        clusterName: miniature
      # ...other inputs attributes
```

---

### **`engine`**

**Description:** Engine option for the dataset input. The engine key can have two values: "minerva" and "default". The "default" value executes queries on the native engine of the data source, while "minerva" uses the DataOS query engine to run queries. 

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | default/minerva |

**Additional Information:** 

- Why and when do we need to connect to Minerva?
    - When the source’s engine is not supported
    - When the source doesn’t have a native engine

To run checks on such a source, we must first connect it to a depot.

- **Available engines for different sources**
    
    
    | Source Name/Engine | Default | Minerva |
    | --- | --- | --- |
    | Snowflake | Yes | Yes |
    | Oracle | Yes | Yes |
    | Trino | Yes | Yes |
    | Minerva | No | Yes |
    | BigQuery | Yes | Yes |
    | Postgres | Yes | Yes |
    | MySQL | Yes | Yes |
    | MSSQL | Yes | Yes |
    | Redshift | Yes | Yes |
    | Elastic Search | No | Yes |
    | MongoDB | No | Yes |
    | Kafka | No | Yes |
    | Azure File System | No | No |
    | Eventhub | No | No |
    | GCS | No | No |
    | OpenSearch | No | No |
    | S3 | No | No |

**Example Usage:**

```yaml
stackSpec:
  inputs:
    - dataset: dataos://icebase:retail/customer
      options:
        engine: minerva
      # ...other inputs attributes
```

---

### **`clusterName`**

**Description:** Here, the users can specify the cluster name on which the queries will run. If the engine is Minerva, this is a mandatory field. You can check the cluster on which your depot is mounted in Workbench or check the cluster definition in Operations.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | valid Cluster Name |

**Example Usage:**

```yaml
stackSpec:
  inputs:
    - dataset: dataos://icebase:retail/customer
      options:
        clusterName: miniature
      # ...other inputs attributes
```

---

### **`branchName`**

**Description:** This attribute allows users to specify the branch of an Iceberg dataset on which the checks should be executed. If the branch name is omitted, Soda defaults to running checks on the `main` branch. For targeted operations on specific branches, providing the branch name is essential.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | main | any valid branch name |

**Example Usage:**

```yaml
stackSpec:
  inputs:
    - dataset: dataos://icebase:retail/customer
      options:
        branchName: test
      # ...other inputs attributes
```

---

### **`filter`**

**Description:** The `filter` attribute mapping or filter section serves as a global filter for all checks specified within a dataset. It is essential to note that this global filter functionality differs from the filter applied within the check section.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | optional | none | none |

**Example Usage:**

```yaml
stackSpec:
  inputs:
    - dataset: dataos://icebase:retail/customer
      filter:
          name: filter_on_age
          where: age > 50
      # ...other inputs attributes
```

---

### **`name`**

**Description:** The `name` attribute provides a unique name to the filter.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | any valid string |

**Example Usage:**

```yaml
stackSpec:
  inputs:
    - dataset: dataos://icebase:retail/customer
      filter:
          name: filter_on_age
        # ...other filter attributes
```

---

### **`where`**

**Description:** The `where` attribute is used to specify the filter condition.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | valid filter condition |

**Example Usage:**

```yaml
stackSpec:
  inputs:
    - dataset: dataos://icebase:retail/customer
      filter:
          where: age < 60
        # ...other filter attributes
```

---

### **`profile`**

**Description:** Profile specification for the dataset input, including column selections. Here you can specify a list of columns that require profiling. Column profile information is used to understand the characteristics and data distribution in the specified columns, such as the calculated mean value of data in a column, the maximum and minimum values in a column, and the number of rows with missing data. 

It can help you to gain insight into the type of checks you can prepare to test for data quality. However, it can be resource-heavy, so carefully consider the datasets for which you truly need column profile information.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | optional | none | none |

**Example Usage:**

```yaml
stackSpec:
  inputs:
    - dataset: dataos://icebase:retail/customer
      profile:
        columns:
          - customer_index
          - exclude email_id
          - include d*
          - e*
      # ...
```

---

### **`columns`**

**Description:** List of column specifications for profiling the dataset.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of strings | optional | - | List of column names or patterns. |

**Additional Information:** In this section, specify the columns for which you need profiling information. You can do so in the following ways -

- Exact Column Name:
    
    If you provide an exact column name, the profiling will focus only on that specific column. 
    
    ```yaml
    profile:
      columns:
        - customer_index
    ```
    
- Wildcard Matching:
    
    If you want to profile multiple columns that share a common pattern, you can use the "*" wildcard character. This wildcard matches any sequence of characters within a column name. 
    
    ```yaml
    profile:
      columns:
        - include d*
    ```
    
- Wildcard for All Columns:
    
    To profile all columns in the dataset, you can use the "*" wildcard without any prefix. 
    
    ```yaml
    profile:
      columns:
        - "*"
    ```
    
- Excluding Columns:
    
    Exclude specific columns from the profiling process, by using the "exclude" keyword followed by the column names.
    
    ```yaml
    profile:
      columns:
    		- "*"
        - exclude email_id
    ```
    
- Combining Patterns
    
    Combine different patterns to create more refined selections. 
    
    ```yaml
    profile:
      columns:
        - customer_index
        - exclude email_id
        - include d*
        - e*
    ```
    

**Example Usage:**

```yaml
stackSpec:
  inputs:
    - dataset: dataos://icebase:retail/customer
      profile:
        columns:
          - customer_index
          - exclude email_id
          - include d*
          - e*
      # ...
```

---
