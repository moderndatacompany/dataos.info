---
title: Supported Data Quality Checks
search: 
  exclude: true
---

# Supported Data Quality Checks

```yaml

 # Volume
  - row_count > 0
  - row_count between 10 and 20000

  # Freshness check
  - freshness < 3

  # Missing Metrics
  - missing_count = 0
  - missing_percent < 5%

  # Check for valid values
  - invalid_percent = 0:
      valid length: 14
  - invalid_percent <= 2:
      valid max: 7
  - invalid_percent = 0:
      valid max length: 14
  - invalid_count = 0:
      valid min: 1
  - invalid_percent = 0:
      valid min length: 12
  - invalid_count = 0:
      valid values: [t, f]
  - invalid_count = 0:
      invalid values: [PO522145787]
  - invalid_count = 0:
      invalid values: [0, 8]

  # Numeric Metrics
  - avg between 100 and 1000
  - avg_length > 12
  - duplicate_count = 0
  - duplicate_percent = 0%
  - max <= 100
  - max_length >= 13
  - min >= 50
  - min_length = 10
  - sum < 120

------------------------------------------------------------
 
 # Checks Attribute (to give additional information about a check)
  - avg_length >= 10:
		  name: {name}
      attributes:
        description: {description about the check}
        tags: [event_campaign, webinar]
```