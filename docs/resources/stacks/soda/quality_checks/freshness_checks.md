# Freshness checks

Ensuring data freshness is essential for maintaining the reliability and accuracy of datasets. In Soda, freshness checks can be defined to monitor and enforce data timeliness. Below are explanations and sample configurations for various types of freshness checks.


**Basic freshness check:** Ensures that the dataset is not older than a specified duration.

In this example, the `freshness(test) < 10d` condition verifies that the dataset's most recent record is less than 10 days old.

```yaml
- freshness(test) < 10d:
    name: Data should not be older than 10 days
    attributes:
      category: Freshness
      title: Validate dataset recency within 10 days
```


**Example with check name:** Ensures that data freshness meets a defined threshold and includes a descriptive check name for better traceability.

The following check verifies that the most recent record in the dataset is less than 27 hours old.

```yaml
- freshness(start_date) < 27h:
    name: Data is fresh
    attributes:
      category: Freshness
      title: Validate that data is updated within the last 27 hours
```


**Example with alert configuration:** Defines warning and failure thresholds for freshness checks using alert conditions.

The only comparison symbol that can be used with freshness checks that employ an alert configuration is `>`.

```yaml
- freshness(start_date):
    warn: when > 3256d
    fail: when > 3258d
    attributes:
      category: Freshness
      title: Monitor and alert when data exceeds freshness limits

# OR


- freshness(start_date):
    warn:
      when > 3256d
    fail:
      when > 3258d
    attributes:
      category: Freshness
      title: Trigger alerts when data freshness thresholds are exceeded
```


**Example with in-check filter:** Ensures that data freshness is validated only for specific subsets of data using a filter condition.

In this example, the check verifies that the records where `weight = 10` are not older than 27 hours.

```yaml
- freshness(start_date) < 27h:
    filter: weight = 10
    attributes:
      category: Freshness
      title: Validate data freshness for records with weight equal to 10
```


### **List of freshness thresholds**

| **Threshold** | **Example** | **Reads as**          |
| ------------- | ----------- | --------------------- |
| `#d`          | `3d`        | 3 days                |
| `#h`          | `1h`        | 1 hour                |
| `#m`          | `30m`       | 30 minutes            |
| `#d#h`        | `1d6h`      | 1 day and 6 hours     |
| `#h#m`        | `1h30m`     | 1 hour and 30 minutes |


By incorporating these accuracy checks into your workflows, you can proactively monitor and maintain the correctness of your datasets, ensuring they meet your organization's data quality standards. 