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

**2. Freshness check with alerting:** Configure alerts to notify stakeholders when the data freshness check fails to meet the specified criteria.

The following manifest file checks that the `ingestion_time` column indicates data ingested within the last 12 hours and sends alerts via email and Slack if the condition is not met.

```yaml
- freshness(test) < 12h:
    column: ingestion_time
    name: Data ingestion should occur within the last 12 hours
    attributes:
      category: Freshness
      title: Data ingestion should occur within the last 12 hours
    alert:
      email: data-team@example.com
      slack: '#data-alerts'
```

Integrating freshness checks ensures proactive monitoring and maintenance of dataset timeliness, supporting compliance with organizational data quality standards.

