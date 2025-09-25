# Freshness checks

Ensuring data freshness is essential for maintaining the reliability and accuracy of datasets. In Soda, freshness checks can be defined to monitor and enforce data timeliness. Below are explanations and sample configurations for various types of freshness checks.

**1. Basic freshness check:** This check ensures that the dataset is not older than a specified duration.

In this example, the `freshness(test) < 10d` condition verifies that the dataset's most recent record is less than 10 days old.

```yaml
- freshness(test) < 10d:
    name: Data should not be older than 10 days
    attributes:
      category: Freshness
      title: Data should not be older than 10 days
```

