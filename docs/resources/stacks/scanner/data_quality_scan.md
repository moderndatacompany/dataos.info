# Scanner for Data Quality Checks

Assertions are business-specific validation rules applied to test and evaluate the quality of specific datasets if they are appropriate for the intended purpose. DataOS allows you to define your own assertions with a combination of tests to check the rules. Flare workflows are run for data quality checks on the entire dataset or sample /filtered data. This analysis is stored in Icebase.

> To learn more about data quality (assertions) Flare workflows, click [here](/resources/stacks/flare/job_types/#data-quality-job).
>

Data quality Scanner workflow reads about these quality checks for your data along with their pass/fail status(metadata extraction related to data quality) and stores it in Metis DB. This data helps you validate the captured data to determine whether the data meets business requirements.

<aside class="callout">
🗣️ Before running the Scanner workflow for quality checks metadata, ensure that the data quality and data-tool workflows are run successfully.

</aside>

## Scanner Workflow YAML for Quality Checks 

The following YAML configuration will connect to the Icebase depot and scan the data quality checks-related information.

### **YAML Configuration** 

```yaml
version: v1
name: icebase-depot-quality
type: workflow
tags:
  - icebase-depot-quality
description: The job scans schema tables and registers metadata
workflow:
  dag:
    - name: icebase-depot-quality
      description: The job scans schema from icebase depot tables and registers metadata to metis2
      spec:
        tags:
          - scanner2.0
        stack: scanner:2.0
        compute: runnable-default
        runAsUser: metis
        scanner:
          depot: dataos://icebase
          type: data-quality
          sourceConfig:
            config:
              schemaFilterPattern:
                includes:
                  - emr_healthcare
```

## Metadata on Metis UI

You can view the list of assertions created for the dataset to monitor the data quality and trend charts for each run. The trend charts also show whether the checks are passed or failed.