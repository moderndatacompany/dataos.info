# Linter Command Validation and Errors


## Command

```yaml
dataos-ctl apply -f <manifest-file-path> -l
```

## Validations

The Linter Command (-l flag) validates the command on following checks

| Category | Parameter | Check/ Validation Rule |
| --- | --- | --- |
| Workflow Information | owner | should not be empty |
|  | workspace | should not be empty |
|  | version | should not be empty |
|  | type | should not be empty |
|  | name | should not be empty and a valid DNS name |
|  | workflow | should not be nil |
|  | dag | should not be nil |
|  | length of workflow dag | should be greater than 0 (there should be at least 1 job within a DAG) |
| For cron workflows | cron | For cron type workflow, cron information should be accurate |
|  | schedule.EndOn | RFC3339 format |
| Flare Job | name | should not be empty and a valid DNS name |
|  | spec | should not be nil |
|  | spec.Stack | should not be nil |
|  | spec.Compute | should not be nil |
|  | spec.Stackspec | should not be nil |
|  | spec.Topology | should be valid if its supplied |


### **Name containing characters other than Alphanumeric characters and ‘-’**

**Error Message**

```yaml
⚠️ Invalid Parameter - failure validating resource : job name is invalid sample-$, must be less than 48 chars and conform to the following regex: [a-z]([-a-z0-9]*[a-z0-9])?
```

**What went wrong?**

The DNS name of the workflow/service/job contains non-alphanumeric characters.

**Solution**

The DNS Name must confirm to the regex `[a-z]([-a-z0-9]*[a-z0-9])`

The regex implies

- Match a single character present in the list below [a-z]
    - a-z matches a single character in the range between a (index 97) and z (index 122) (case sensitive)
- 1st Capturing Group ([-a-z0-9]*[a-z0-9])
    - Match a single character present in the list below [-a-z0-9]
        - matches the previous token between zero and unlimited times, as many times as possible, giving back as needed (greedy)
        - matches the character - with index 45 literally (case sensitive)
            - a-z matches a single character in the range between a (index 97) and z (index 122) (case sensitive)
            - 0-9 matches a single character in the range between 0 (index 48) and 9 (index 57) (case sensitive)
    - Match a single character present in the list below [a-z0-9]
        - a-z matches a single character in the range between a (index 97) and z (index 122) (case sensitive)
        - 0-9 matches a single character in the range between 0 (index 48) and 9 (index 57) (case sensitive)

## Associated Errors

### **DNS Name Errors**

**Error Message: DNS name length should be less than 48**

```yaml
2022-11-17 12:32:12,901 ERROR [kubernetes-executor-snapshots-subscribers-0] o.a.s.s.c.k.ExecutorPodsSnapshotsStoreImpl: Going to stop due to IllegalArgumentException
java.lang.IllegalArgumentException: **'sample-12345678998765432112345678-d606d38485934408'** in spark.kubernetes.executor.podNamePrefix is invalid. must conform https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-label-names and the value length <= 47
```

**What went wrong?**

The DNS name length of workflow/job/service should be less than 48. But in the majority of the cases, a Unique ID generated by the orchestration engine gets appended to the name increasing its size, making it cross the threshold limit.

**Solution**

In majority of the cases the length of the Unique ID is 17 characters. So its advised to keep the name length less than less than or equal to 30.

### **Invalid input UDL name**

**Error Message**

```yaml
Exception in thread "main" com.fasterxml.jackson.databind.etc.ValueInstantiationException: Cannot construct instance of `io.dataos.flare.configurations.job.input.Input`, problem: Invalid dataset found: dataos:////thirdparty01:analytics/survey_unpivot/unpivot_data.csv
```

**What went wrong?**

The UDL of the input dataset is invalid

**Solution**

The UDL should conform to the format `dataos://[depot]:[collection]/[dataset]`

### **Invalid file format**

```yaml
2022-11-18 07:57:27,726 ERROR [main] i.d.f.Flare$: =>Flare: Job finished with error build version: 6.0.91-dev; workspace name: public; workflow name: test-03-dataset; workflow run id: 3bdc1dcb-5130-49a5-97e9-e332e238396a; run as user: iamgroot; job name: sample-123; job run id: 3b0c3db5-ea06-4727-96ff-8f493ff80257; 
java.lang.ClassNotFoundException: 
Failed to find data source: csvbb. 
```

**What went wrong?**

The input file format is not compatible or its wrong 

**Solution**

Choose the correct file format. 