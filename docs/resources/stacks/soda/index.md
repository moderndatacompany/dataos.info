---
title: Soda Stack
search:
  boost: 2
---

# Soda Stack

Soda is a declarative [Stack](/resources/stacks/) for data quality testing within and beyond data pipelines, extending its capabilities, enhancing data observability and reliability across one or more datasets. It enables you to use the [Soda Checks Language (SodaCL)](https://docs.soda.io/soda-cl/soda-cl-overview.html) to turn user-defined inputs into aggregated SQL queries.

## How to run Soda checks?

### **Create a Workflow/Worker manifest**

Soda operates as a Stack that can be orchestrated through various [Resources](/resources/), such as a [Workflow](/resources/workflow/), or a [Worker](/resources/worker/) Resource. The choice of orchestrator-type is contingent upon the specific use case being addressed.

- When dealing with batch workloads for executing quality checks and profiling, opt for the [Workflow](/resources/workflow/) Resource.
- For long-running, continuous workloads, the recommended choice is the [Worker](/resources/worker/) Resource.

For detailed insights into the selection and utilization of the appropriate Resource, please refer to the dedicated documentation for [Workflow](/resources/workflow/) and [Worker](/resources/worker/) Resources.

<details><summary>Code Snippet for Workflow and Worker manifest</summary>

<h3><b>Code Snippet for Workflow</b></h3>

```yaml
# Configuration for Resource meta section

name: soda-workflow         # Resource name (mandatory, default: none, possible: any string confirming the regex [a-z0-9]([-a-z0-9]*[a-z0-9]) and length less than or equal to 48 characters)
version: v1                 # Manifest version (mandatory, default: none, possible: v1)
type: workflow              # Resource-type (mandatory, default: none, possible: workflow)
tags:                       # Tags (optional, default: none, possible: list of strings)
  - workflow
  - soda-checks
description: Soda workflow  # Resource description (optional, default: none, possible: any string)
workspace: public           # Workspace name (optional, default: public, possible: any DataOS Workspace name)

# Configuration for Workflow-specific section

workflow:
  dag:
    - name: soda-job-v1           # Job name (mandatory, default: none, possible: any string confirming the regex [a-z0-9]([-a-z0-9]*[a-z0-9]) and length less than or equal to 48 characters)
      title: Soda checks job      # Job title (optional, default: none, possible: any string)
      description: Soda job       # Job description (optional, default: none, possible: any string)
      spec:                       # Job spec (mandatory)
        stack: soda+python:1.0    # Stack name, flavor, and version (mandatory, default: none, value: for soda use soda+python:1.0. Here soda is the stack, python is flavor, and 1.0 is version)
        compute: runnable-default # Compute name (mandatory, default: none, possible: runnable-default or any other runnable-type Compute Resource name)
        resources:                # CPU and memory resources (optional)
          requests:               # Requested resources (optional)
            cpu: 1000m            # Requested CPU resources (optional, default: 100m, possible: cpu units in milliCPU(m) or cpu core)
            memory: 100Mi         # Requested memory resources (optional, default: 100Mi, possible: memory in Mebibytes(Mi) or Gibibytes(Gi))
          limits:                 # Resource limits (optional)
            cpu: 400m             # CPU resource limits (optional, default: 400m, possible: cpu units in milliCPU(m) or cpu core)
            memory: 400Mi         # Memory resource limits (optional, default: 400Mi, possible: cpu units in milliCPU(m) or cpu core)
        logLevel: INFO            # Logging level (optional, default: INFO, possible: INFO / WARNING / ERROR / DEBUG)

# Configuration for Soda Stack-specific section
        stackSpec:
          # ... attributes specific to Soda Stack are specified here.
```
<center><i>Configuration for a Workflow YAML manifest</i></center>

To learn more about the attributes of <a href="/resources/workflow/">Workflow</a> Resource, refer to the link: <a href="/resources/workflow/configurations/">Attributes of Workflow YAML</a>.

<h3><b>Code Snippet for Worker</b></h3>

```yaml

# Configuration for Resource meta section

name: soda-worker           # Resource name (mandatory, default: none, possible: any string confirming the regex [a-z0-9]([-a-z0-9]*[a-z0-9]) and length less than or equal to 48 characters)
version: v1beta             # Manifest version (mandatory, default: none, possible: v1beta)
type: worker                # Resource-type (mandatory, default: none, possible: worker)
tags:                       # Tags (optional, default: none, possible: list of strings)
  - worker
  - soda-checks
description: Soda worker    # Resource description (optional, default: none, possible: any string)
workspace: public           # Workspace name (optional, default: public, possible: any DataOS Workspace name)

# Configuration for Worker-specific section

worker:
  replicas: 1                        # Number of worker replicas (optional, default: 1, possible: any positive integer)
  tags:                              # Tags (optional, default: none, possible: list of strings)
    - sodaworker
  stack: soda+python:1.0             # Stack name, flavor, and version (mandatory, default: none, value: for soda use sodaworker+python:1.0. Here sodaworker is the stack, python is flavor, and 1.0 is version)
  logLevel: INFO                     # Logging level (optional, default: INFO, possible: INFO / WARNING / ERROR / DEBUG)
  compute: runnable-default          # Compute name (mandatory, default: none, possible: runnable-default or any other runnable-type Compute Resource name)
  resources:                # CPU and memory resources (optional)
    requests:               # Requested resources (optional)
      cpu: 1000m            # Requested CPU resources (optional, default: 100m, possible: cpu units in milliCPU(m) or cpu core)
      memory: 100Mi         # Requested memory resources (optional, default: 100Mi, possible: memory in Mebibytes(Mi) or Gibibytes(Gi))
    limits:                 # Resource limits (optional)
      cpu: 400m             # CPU resource limits (optional, default: 400m, possible: cpu units in milliCPU(m) or cpu core)
      memory: 400Mi         # Memory resource limits (optional, default: 400Mi, possible: cpu units in milliCPU(m) or cpu core)

# Configuration for Soda Stack-specific section

  stackSpec: 
    # ... attributes specific to Soda Stack are specified here.
```
<center><i>Configuration for a Worker YAML manifest</i></center>

To learn more about the attributes of <a href="/resources/worker/">Worker</a> Resource, refer to the link: <a href="/resources/worker/configurations/">Attributes of Worker YAML</a>.

</details>


### **Declare the configuration for Soda `stackSpec` section**

The [Workflow](/resources/workflow/) and [Worker](/resources/worker/) Resource comprise of a [`stackSpec`](/resources/stacks/soda/configurations/#stackspec) section (or a mapping) that comprises the attributes of the Stack to be orchestrated. In the context of Soda Stack, the StackSpec defines diverse datasets and their associated Soda checks. 

The YAML snippet below shows a sample structure of the Soda [`stackSpec`](/resources/stacks/soda/configurations/#stackspec) section:

```yaml
stackSpec:
  inputs:
    - dataset: dataos://icebase:retail/customer
      options:
        engine: minerva
        clusterName: miniature
        branchName: test
      filter:
        name: filter_on_age
        where: age > 50
      checks:
        - missing_count(snapshot_id) = 0:
            name: Completeness of the Snapshot ID Column #add the name
            attributes:
              title: Completeness of the Snapshot ID Column
              category: Completeness
      profile:
        columns:
          - "*"
```

This involves the declaration of following parts:

1. [Declare Input Dataset Address](#declaring-input-dataset-address)
2. [Define columns to be profiled (optional)](#defining-columns-to-be-profiled-optional)
3. [Define filters](#define-filters)
4. [Define Soda Checks](#defining-soda-checks)
5. [Define Optional configuration](#define-optional-configuration)

#### **Declaring Input Dataset Address**

The [`dataset`](/resources/stacks/soda/configurations/#dataset) attribute allows data developer to specify the data source or dataset that requires data quality evaluations. It is declared in the form of a [Uniform Data Link [UDL]](/resources/depot/), in the following format: `dataos://[depot]:[collection]/[dataset]`.

```yaml
stackSpec:
  inputs:
    - dataset: dataos://icebase:retail/customer
      # ...other input attributes
    - dataset: dataos://postgresdb:state/city
      # ...other input attributes
```


#### **Defining Soda Checks**

Soda Stack utilzies SodaCL, a YAML-based, low-code, human-readable, domain-specific language for data reliability and data quality management. SodaCL enables data developers to write checks for data quality, then run a scan of the data in the data source to execute those checks.

<div style="text-align: center;">
  <img src="/resources/stacks/soda/soda_check.png" alt="SODA" style="border:1px solid black; width: 80%; height: auto;">
  <figcaption><i>Anatomy of a regular check in Soda. The dataset identifier is the name of the dataset on which you want to run the check. A metric is a property of the dataset that you wish to evaluate. The threshold is the metric value you want to check for during a scan.</i></figcaption>
</div>

The [`checks`](/resources/stacks/soda/configurations/#checks) section allows users to specify a list of specific data quality checks or tests that will be performed on the designated dataset. These checks can be tailored to suit the unique requirements of the dataset and the data quality objectives.

```yaml
# Checks for basic validations would be named in `Validity` category

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
        - invalid_percent(customer_name) < 1%:
            valid max length: 27
            filter: site_number > 0
            attributes:
              category: Validity     
        # - invalid_percent(phone) < 1 %:
        #     valid format: phone number
        - invalid_count(number_cars_owned) = 0:
            valid min: 1
            valid max: 6
            attributes:
              category: Validity
        - duplicate_count(phone) = 0:
            attributes:
              category: Uniqueness
        - invalid_count(site_number) < 0:
            valid min: 5
            valid max: 98
            attributes:
              category: Validity
      # ...other inputs attributes

stackSpec:
  inputs:
    - dataset: dataos://icebase:retail/customer
      checks:
      - avg(safety_stock_level) > 50:
          attributes:
            category: Accuracy
      # ...other inputs attributes

---

# Check for Freshness would be categorised in `Freshness` category 

stackSpec:
  inputs:
    - dataset: dataos://icebase:retail/customer
      checks:
        - freshness(test) < 551d:
            name: Freshness01
            attributes:
              category: Freshness
      # ...other inputs attributes

---

# Check for Accuracy Category

stackSpec:
  inputs:
    - dataset: dataos://icebase:retail/customer
      checks:
        - values in (city_name) must exist in city (city_name):
            samples limit: 20
            attributes:
              category: Accuracy
      # ...other inputs attributes
```

<details>

<summary>Sample Soda checks</summary>

```yaml
name: soda-customer-checks
version: v1
type: workflow
tags:
  - workflow
  - soda-checks
description: Empowering sales360 dp.
workspace: public
workflow:
  dag:
    - name: soda-job-v1
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
            - dataset: dataos://icebase:sales_360/account
              options:
                engine: minerva
                clusterName: system
              profile:
                columns:
                  - site_number
                  - customer_no
                  - city
              checks:

                - schema:
                    name: Confirm that required columns are present
                    warn:
                      when required column missing: [customer_name,premise_code]
                    fail:
                      when required column missing: 
                        - city
                      when wrong column type:
                        site_number: integer

                - invalid_count(customer_name) = 0 :
                    valid min length: 5
                    name: First name has 5 or more characters
                    warn: when between 5 and 27
                    fail: when > 27  

                - invalid_percent(customer_name) < 1%:
                    valid max length: 27
                    filter: site_number > 0

                - invalid_count(site_number) < 0:
                    valid min: 5
                    valid max: 98

                - missing_percent("phone_number") = 0

                - duplicate_percent(customer_no) < 1%

                - row_count between 1 and 170
                - avg_length(address) > 16
                - min(customer_no) > 0:
                    filter: site_number = 3
    # ...other inputs attributes
```

</details>

[Data Product Hub](/interfaces/data_product_hub/) consolidates the status of all your data quality checks under the **Quality** tab, giving a comprehensive view of the health of your data assets.   There are two ways for a check and its latest result to appear on the dashboard:

**Manual Scans with Scanner:** When you define checks in a YAML file and run a scanner using the Soda Library, the checks and their results are displayed in the Checks dashboard.

**Scheduled Scans by Soda Workflow:** When Soda runs a scheduled workflow, the checks and their latest results automatically appear on the Checks dashboard.

Each check result on the dashboard indicates whether it has passed or failed based on the specific quality dimension it is assessing. For Instance, in the below provided image, we can see the status of various data quality checks:

- Accuracy: Passed, as indicated by the green checkmark.
- Completeness: Passed, with a green checkmark.
- Freshness: Flagged with a warning (⚠), suggesting the data might not be up-to-date.
- Schema: Also flagged (⚠), which could mean there are schema mismatches or other issues with the data structure.
- Uniqueness: Passed successfully.
- Validity: Passed, indicating the data adheres to the expected validation rules.

<div style="text-align: center;">
  <img src="/resources/stacks/soda/soda_checks_01.png" alt="SODA" style="border:1px solid black; width: 80%; height: auto;">
  <figcaption><i>Checks Symbol</i></figcaption>
</div>

When you click on any of the check, a detailed trend chart appears, displaying the specific times the check was executed along with the percentage of SLO compliance over time. The chart includes a graphical representation of how the data met the predefined quality standards, with 100% indicating full compliance. Any dips in the line graph highlight potential issues during specific check runs. Additionally, the dashboard may show more information like dataset details and error messages, offering a comprehensive view of the data quality trends over time. For instance, here you can see that the Trend Chart of the Validity check which indicates the time checks were ran against the percentage of SLOs.

<div style="text-align: center;">
  <img src="/resources/stacks/soda/image.png" alt="SODA" style="border:1px solid black; width: 80%; height: auto;">
  <figcaption><i>Checks Symbol</i></figcaption>
</div>

The detailed trend chart shows that the data quality check was consistently run at 8:05 AM on several specific dates, including September 25, 26, 28, and daily from October 1 to 9. This regular cadence indicates the check was scheduled to run at the same time on these dates, ensuring continuous monitoring. The trend line remains at 100%, meaning the data met all SLO criteria during each check. For more details on the Quality tab refer [this link](/interfaces/data_product_hub/discovery/#data-product-tab) and scroll to Quality tab.

You can refer to the Soda documentation for the grammar of check definitions: [Soda CL Reference](https://docs.soda.io/soda-cl/soda-cl-overview.html).

#### **Defining Columns to be Profiled (Optional)**

The [`profile`](/resources/stacks/soda/configurations/#profile) section enables you to specify a list of columns that require profiling. Profiling involves analysing and collecting information about the characteristics and data distribution in these columns. The profile section is especially beneficial for gaining insights into the data and comprehending it’s patterns.

```yaml
stackSpec:
  inputs:
    - dataset: dataos://distribution:distribution/dc_info
      profile:
        columns:
          - "*"
```

**Columns Specification**

The [`columns`](/resources/stacks/soda/configurations/#columns) attribute under the profile section is where you specify the list of columns you want to profile. Each column is represented as a string item in the list. 

You can provide the exact column name, or you can use special patterns to match multiple columns. The column matching patterns are provided in the list below:

<table>
    <tr>
        <th>Column Patterns</th>
        <th>Description</th>
        <th>Example</th>
    </tr>
    <tr>
        <td>Exact Column Matching</td>
        <td>If you provide an exact column name, the profiling will focus only on that specific column.</td>
        <td>
            <pre>profile:<br>  columns:<br>    - customer_index</pre>
        </td>
    </tr>
    <tr>
        <td>Wildcard Matching</td>
        <td>If you want to profile multiple columns that share a common pattern, you can use the "*" wildcard character. This wildcard matches any sequence of characters within a column name.</td>
        <td>
            <pre>profile:<br>  columns:<br>    - include d*</pre>
        </td>
    </tr>
    <tr>
        <td>Wildcard for all Columns</td>
        <td>To profile all columns in the dataset, you can use the "*" wildcard without any prefix.</td>
        <td>
            <pre>profile:<br>  columns:<br>    - "*"</pre>
        </td>
    </tr>
    <tr>
        <td>Excluding Columns</td>
        <td>To exclude specific columns from the profiling process, you can use the "exclude" keyword followed by the column names.</td>
        <td>
            <pre>profile:<br>  columns:<br>    - "*"<br>    - exclude email_id</pre>
        </td>
    </tr>
    <tr>
        <td>Combining Patterns</td>
        <td>You can combine different patterns to create more refined selections.</td>
        <td>
            <pre>profile:<br>  columns:<br>   - customer_index<br>   - exclude email_id<br>   - include d*<br>   - e*</pre>
        </td>
    </tr>
</table>

#### **Define Filters**

The [`filter`](/resources/stacks/soda/configurations/#filter) attribute or section works as a global filter for all checks specified within a dataset. 

<aside class="callout">

🗣️ This global filter functionality differs from the filter applied within the <a href="/resources/stacks/soda/#defining-soda-checks"><code>checks</code></a> section.

</aside>

The following YAML sample demonstrates how the [`filter`](/resources/stacks/soda/configurations/#filter) section can be employed to apply a global filter on all checks specified within the [`checks`](/resources/stacks/soda/configurations/#checks) section.

```yaml
stackSpec:
  inputs:
    - dataset: dataos://icebase:retail/customer
      filter:
        name: filter_on_age
        where: age > 50
```


#### **Define Optional configuration**

The [`options`](/resources/stacks/soda/configurations/#options) section provides users with the flexibility to configure various attributes for connecting to data sources or data source options. These options encompass:

**Engine**

The [`engine`](/resources/stacks/soda/configurations/#engine) attribute can assume two values: `minerva` and `default`. 

- The `default` value executes queries on the data source.
- The `minerva` option utilizes the DataOS query engine (Minerva) to execute queries on the depot connected to the cluster. When opting for `minerva`, specifying the [`clusterName`](/resources/stacks/soda/configurations/#clustername) becomes mandatory.

<aside class="callout">
🗣 For sources like <b>Icebase</b>, engine must be <code>minerva</code>. For more information, refer to the list of sources and supported engines provided below.

<details>
<summary>List of Sources and Supported Engine</summary>

<center>

<table>
    <tr>
        <th><strong>Source Name/Engine</strong></th>
        <th><strong>Default</strong></th>
        <th><strong>Minerva</strong></th>
    </tr>
    <tr>
        <td>Snowflake</td>
        <td>Yes</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>Oracle</td>
        <td>Yes</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>Trino</td>
        <td>Yes</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>Minerva</td>
        <td>No</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>BigQuery</td>
        <td>Yes</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>Postgres</td>
        <td>Yes</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>MySQL</td>
        <td>Yes</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>MSSQL</td>
        <td>Yes</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>Redshift</td>
        <td>Yes</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>Elastic Search</td>
        <td>No</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>MongoDB</td>
        <td>No</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>Kafka</td>
        <td>No</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>Azure File System</td>
        <td>No</td>
        <td>No</td>
    </tr>
    <tr>
        <td>Eventhub</td>
        <td>No</td>
        <td>No</td>
    </tr>
    <tr>
        <td>GCS</td>
        <td>No</td>
        <td>No</td>
    </tr>
    <tr>
        <td>OpenSearch</td>
        <td>No</td>
        <td>No</td>
    </tr>
    <tr>
        <td>S3</td>
        <td>No</td>
        <td>No</td>
    </tr>
</table>

</center>

</details>

</aside>

**Cluster Name**

If applicable, users can provide the [`clusterName`](/resources/stacks/soda/configurations/#clustername) on which queries will run. This is a mandatory field in the case of the Minerva engine. You can check the cluster on which your depot is mounted in Workbench or check the cluster definition in the [Operations](/interfaces/operations/) App.

<aside class="callout">

🗣 You can use all source-supported properties that the <a href="https://github.com/sodadata/soda-core/blob/main/docs/overview-main">Soda Core</a> library supports as well.

</aside>

```yaml
stackSpec:
  inputs:
    - dataset: dataos://icebase:retail/customer
      options:
        engine: minerva
        clusterName: miniature
```

The following table provides a comprehensive overview of the various attributes within the Soda-specific Section:

| Attribute | Data Type | Default Value | Possible Values | Requirement |
| --- | --- | --- | --- | --- |
| [`stackSpec`](/resources/stacks/soda/configurations/#stackspec) | mapping | none | none | mandatory |
| [`inputs`](/resources/stacks/soda/configurations/#inputs) | list of mappings | none | any valid iceberg<br>dataset UDL address | mandatory |
| [`dataset`](/resources/stacks/soda/configurations/#dataset) | string | none | none | mandatory |
| [`options`](/resources/stacks/soda/configurations/#options) | mapping | none | set_version | optional |
| [`engine`](/resources/stacks/soda/configurations/#engine) | string | none | default / minerva | optional |
| [`clusterName`](/resources/stacks/soda/configurations/#clustername) | string | none | valid cluster name | optional |
| [`branchName`](/resources/stacks/soda/configurations/#branchname) | string | main | valid branch name in string format | optional |
| [`filter`](/resources/stacks/soda/configurations/#filter) | mapping | none | none | optional |
| [`name`](/resources/stacks/soda/configurations/#name) | string | none | valid filter name | optional |
| [`where`](/resources/stacks/soda/configurations/#where) | string | none | valid filter condition | optional |
| [`profile`](/resources/stacks/soda/configurations/#profile) | mapping | none | none | optional |
| [`columns`](/resources/stacks/soda/configurations/#columns) | list of strings | none | dataset column names | optional |
| [`checks`](/resources/stacks/soda/configurations/#checks) | list of mappings | none | valid SodaCL checks | mandatory |

For further details regarding the Soda Stack-specific attributes, you can refer to the link: [Attributes of Soda Stack YAML](/resources/stacks/soda/configurations/).

**Branch Name Configuration for Lakehouse storage or Icebase type Depots**

In DataOS, Soda facilitates the execution of checks on different branches within a Lakehouse storage or Icebase-type Depot. By default, if no branch name is specified, Soda automatically targets the `main` branch. However, users have the option to direct the checks towards a specific branch by providing the branch name.

To specify a branch name when running a check in a Depot that supports the Iceberg table format, follow the sample configuration below. This capability ensures checks are performed on the desired branch, enhancing the flexibility and accuracy of data management.

```yaml
stackSpec:
  inputs:
    - dataset: dataos://icebase:retail/customer
      options:
        engine: minerva
        clusterName: miniature
        branchName: test
```

This configuration illustrates how to set the `branchName` to "test". Adjust the `branchName` parameter to match the branch you intend to assess.

### **Code Samples**

<details>
<summary>Sample manifest for Soda Stack orchestrated using a Workflow</summary>

```yaml
name: soda-workflow-v01
version: v1
type: workflow
tags:
  - workflow
  - soda-checks
description: Random User Console
workspace: public
workflow:
  dag:
    - name: soda-job-v1
      title: soda Sample Test Job
      description: This is sample job for soda dataos sdk
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
            # Redshift
            - dataset: dataos://sanityredshift:public/redshift_write_12
              checks:
                - row_count between 10 and 1000:
                    attributes:
                      category: Accuracy
              
            # Oracle
            - dataset: dataos://sanityoracle:dev/oracle_write_12
              checks:
                - row_count between 10 and 1000:
                    attributes:
                      category: Accuracy
            # MySql
            - dataset: dataos://sanitymysql:tmdc/mysql_write_csv_12
              checks:
                - row_count between 10 and 1000:
                    attributes:
                      category: Accuracy
            # MSSQL
            - dataset: dataos://sanitymssql:tmdc/mssql_write_csv_12
              checks:
                - row_count between 10 and 1000:
                    attributes:
                      category: Accuracy
            # Minerva
            - dataset: dataos://icebase:retail/customer
              options:
                engine: minerva
                clusterName: miniature
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
                    attributes:
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
                      category: Freshness
                - freshness(ts_customer) < 5d:
                    name: Freshness02
                    attributes:
                      category: Freshness
                - max(age) <= 100:
                    attributes:
                      category: Accuracy
                # - max_length(first_name) = 8:
                #     attributes:
                #       category: Accuracy
                - values in (occupation) must exist in city (city_name):
                    samples limit: 20
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
            - dataset: dataos://metisdb:public/classification
              checks:
                - row_count between 0 and 1000:
                    attributes:
                      category: Accuracy
            # Big Query
            - dataset: dataos://distribution:distribution/dc_info
              checks:
              - row_count between 0 and 1000:

            # Snowflake
            - dataset: dataos://sodasnowflake:TPCH_SF10/CUSTOMER
              options: # this option is default no need to set, added for example.
                engine: default
              checks:
                - row_count between 10 and 1000:
                    attributes:
                      category: Accuracy

```
</details>

<details>
<summary>Sample manifest for Soda Stack orchestrated using a Worker</summary>

```yaml
name: soda-worker-sample-v01
version: v1beta
type: worker
tags:
  - worker
  - soda-checks
description: Soda Sample Worker
workspace: public
worker:
  replicas: 1
  tags:
    - worker
    - soda-checks
  stack: sodaworker+python:1.0
  logLevel: INFO
  compute: runnable-default
  resources:
    requests:
      cpu: 100m
      memory: 128Mi
    limits:
      cpu: 1000m
      memory: 1024Mi
  stackSpec:
    inputs:
      # Minerva
      - dataset: dataos://icebase:retail/customer
        options:
          engine: minerva
          clusterName: miniature
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
              attributes:
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
                category: Freshness
          - freshness(ts_customer) < 5d:
              name: Freshness02
              attributes:
                category: Freshness
               
          - max(age) <= 100:
              attributes:
                category: Accuracy
          # - max_length(first_name) = 8:
          #     attributes:
          #       category: Accuracy
          - values in (occupation) must exist in city (city_name):
              samples limit: 20
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
              attributes:
                category: Schema
```
</details>


### **Apply the manifest using CLI**

Use the apply command to apply the workflow using CLI.

```shell
dataos-ctl apply -f ${{path/file-name}} -w ${{workspace}} # By default the workspace is public
```

## Querying Profiling and Checks data

Soda check results and profiling information are stored in Iceberg tables, and querying this information can be accomplished through [Workbench](/interfaces/workbench/) App. 

To do so, Workflows can be executed to sink the information related to Checks and Profiles into the [Icebase](/resources/depot/#icebase) depot. The YAML for both Workflows is provided below.

<details>
<summary>Workflow for sinking Soda Check information</summary>

```yaml
name: soda-check-metrics-data
version: v1
type: workflow
workflow:
  dag:
    - name: soda-cm-data
      spec:
        stack: flare:5.0
        compute: runnable-default
        stackSpec:
          job:
            explain: true
            inputs:
              - name: soda
                dataset: dataos://systemstreams:soda/quality_profile_results_01
                isStream: false
                options:
                  startingOffsets: earliest
            logLevel: INFO
            outputs:
              - name: joined_checks_metrics
                dataset: dataos://icebase:soda/soda_check_metrics_01?acl=rw
                format: Iceberg
                options:
                  saveMode: append
                  checkpointLocation: dataos://icebase:sys01/checkpoints/soda-checks-data/v001?acl=rw
                  sort:
                    mode: partition
                    columns:
                        - name: depot
                          order: desc
                        - name: collection
                          order: desc
                        - name: dataset
                          order: desc
                  iceberg:
                    partitionSpec:
                      - type: identity
                        column: depot
                      - type: identity
                        column: collection
                      - type: identity
                        column: dataset
            steps:
              - sequence:
                  - name: dropped_columns
                    sql: SELECT * from soda
                    functions:
                      - name: drop
                        columns:
                          - __eventTime
                          - __key
                          - __producer_name
                          - __messageProperties
                          - __publishTime
                          - __topic
                          - automatedMonitoringChecks
                          - clusterName
                          - dataosResourceId
                          - defaultDataSource
                          - definitionName
                          - engine
                          - hasFailures
                          - hasErrors
                          - hasWarnings
                          - logs
                          - metadata
                          - profiling
                          - queries
                          - runId
                      - name: cleanse_column_names
                  - name: checks_extracted
                    sql: select * from dropped_columns
                    functions:
                      - name: unfurl 
                        expression: explode(checks) as checks_
                      - name: drop
                        columns:
                          - checks
                      - name: rename_all
                        columns:
                          metrics: metrics_value
                      - name: unfurl 
                        expression: checks_.*
                      - name: drop
                        columns:
                          - checks_
                      - name: unfurl
                        expression: explode(metrics) as metrics_
                      - name: drop
                        columns:
                          - metrics
                  - name: metrics_extracted
                    sql: select dataos_run_id, metrics_value from checks_extracted
                    functions:
                      - name: unfurl 
                        expression: explode(metrics_value) as metrics_value_
                      - name: drop
                        columns:
                          - metrics_value
                      - name: unfurl 
                        expression: metrics_value_.*
                      - name: drop
                        columns:
                          - metrics_value_

                  - name: joined_checks_metrics
                    sql: select 
                          ce.dataos_run_id, ce.job_name, ce.scan_start_timestamp as timestamp, ce.user_name, ce.depot, ce.collection, ce.dataset, ce.column, ce.name as check_definition, me.metric_name, me.value as metric_value, ce.outcome as check_outcome
                          from checks_extracted ce
                          left join metrics_extracted me on ce.dataos_run_id = me.dataos_run_id and ce.metrics_ = me.identity

    - name: soda-check-data
      spec:
        stack: toolbox
        compute: runnable-default
        stackSpec:
          dataset: dataos://icebase:soda/soda_check_metrics_01?acl=rw
          action:
            name: set_version
            value: latest
      dependencies:
        - soda-cm-data
```
</details>

<details>
<summary>Workflow for sinking Soda Profiling information</summary>

```yaml
version: v1
name: soda-profile-data
type: workflow
workflow:
  dag:
    - name: soda-prf-data
      spec:
        stack: flare:5.0
        compute: runnable-default
        stackSpec:
          job:
            explain: true
            inputs:
              - name: soda
                dataset: dataos://systemstreams:soda/quality_profile_results_01
                isStream: false
                options:
                  startingOffsets: earliest
            logLevel: INFO
            outputs:
              - name: changed_datatype
                dataset: dataos://icebase:soda/soda_profiles_01?acl=rw
                format: Iceberg
                options:
                  saveMode: append
                  checkpointLocation: dataos://icebase:sys01/checkpoints/soda-profiles-data/v001?acl=rw
                  sort:
                    mode: partition
                    columns:
                        - name: depot
                          order: desc
                        - name: collection
                          order: desc
                        - name: dataset
                          order: desc
                  iceberg:
                    partitionSpec:
                      - type: identity
                        column: depot
                      - type: identity
                        column: collection
                      - type: identity
                        column: dataset
            steps:
              - sequence:
                  - name: dropped_columns
                    sql: SELECT * from soda
                    functions:
                      - name: drop
                        columns:
                          - __eventTime
                          - __key
                          - __producer_name
                          - __messageProperties
                          - __publishTime
                          - __topic
                          - automatedMonitoringChecks
                          - clusterName
                          - dataosResourceId
                          - defaultDataSource
                          - definitionName
                          - engine
                          - hasFailures
                          - hasErrors
                          - hasWarnings
                          - logs
                          - metadata
                          - checks
                          - queries
                          - metrics
                      - name: cleanse_column_names
                      - name: unfurl
                        expression: explode(profiling) as profiling_
                      - name: unfurl
                        expression: profiling_.*
                      - name: drop
                        columns:
                          - profiling
                          - profiling_
                      - name: unfurl
                        expression: explode(column_profiles) as column_profiles_
                      - name: unfurl
                        expression: column_profiles_.*
                      - name: unfurl
                        expression: profile.*
                      - name: drop
                        columns:
                          - column_profiles
                          - column_profiles_
                          - profile
                      - name: cleanse_column_names
                  - name: changed_datatype
                    sql: |
                      SELECT
                        collection,
                        dataset,
                        depot,
                        job_name,
                        user_name,
                        scan_end_timestamp as created_at,
                        row_count,
                        table,
                        column_name,
                        run_id,
                        cast(avg AS STRING) AS avg,
                        cast(avg_length AS STRING) AS avg_length,
                        cast(distinct AS STRING) AS distinct,
                        cast(frequent_values AS STRING) AS frequent_values,
                        cast(histogram AS STRING) AS histogram,
                        cast(max AS STRING) AS max,
                        cast(max_length AS STRING) AS max_length,
                        cast(maxs AS STRING) maxs,
                        cast(min AS STRING) AS min,
                        cast(min_length AS STRING) AS min_length,
                        cast(mins AS STRING) AS mins,
                        cast(missing_count AS STRING) AS missing_count,
                        cast(stddev AS STRING) AS stddev,
                        cast(sum AS STRING) AS sum,
                        cast(variance AS STRING) AS variance
                      FROM
                        dropped_columns
                    functions:
                      - name: unpivot 
                        columns:
                          - avg
                          - avg_length
                          - distinct
                          - frequent_values
                          - histogram
                          - max
                          - max_length
                          - maxs
                          - min
                          - min_length
                          - mins
                          - missing_count
                          - stddev
                          - sum
                          - variance
                        pivotColumns:
                          - run_id
                          - created_at
                          - depot
                          - collection
                          - dataset
                          - user_name
                          - job_name
                          - row_count
                          - table
                          - column_name
                        keyColumnName: analyzer_name
                        valueColumnName: result

    - name: soda-prf-tool
      spec:
        stack: toolbox
        compute: runnable-default
        stackSpec:
          dataset: dataos://icebase:soda/soda_profiles_01?acl=rw
          action:
            name: set_version
            value: latest
      dependencies:
        - soda-prf-data
```
</details>

Once executed, the information can be queried from the Icebase tables using the Workbench App.

- For checks information, query the `dataos://icebase:soda/soda_check_metrics_01` table.
- For profiling information, query the `dataos://icebase:soda/soda_profiles_01` table.

**Sample Query**

```sql
SELECT * FROM icebase.soda.soda_check_metrics_01 LIMIT 10
```

## Case Scenarios

<!-- - [How to run Soda checks for data quality evaluation using Soda Stack in DataOS?](/resources/stacks/soda/how_to_run_soda_checks_using_soda_stack) -->

- [How to run profiling using Soda Stack in DataOS?](/resources/stacks/soda/how_to_run_profiling_using_soda_stack/)
- [How to run Soda checks on a specific branch of Iceberg dataset?](/resources/stacks/soda/how_to_run_soda_checks_on_a_specific_branch_of_iceberg_dataset/)



