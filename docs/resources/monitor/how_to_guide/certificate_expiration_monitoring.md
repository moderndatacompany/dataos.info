# How to Generate Incidents for Certificate Expiration

This guide explains how to set up a monitor that generates incidents when an SSL certificate is about to expire, using the Equation Monitor.

## Overview

You can use an Equation Monitor to compare the certificate expiration timestamp with the current time and trigger an incident if the certificate is expiring soon (e.g., within 24 hours).

## Example Equation Monitor YAML

Below is an example configuration for monitoring certificate expiration:

```yaml
# Resource meta section
name: certificate-expiry-monitor
version: v1alpha
type: monitor
tags:
  - dataos:type:resource
description: Monitor for SSL certificates expiring in less than 24 hours
layer: user
runAsUser: ${{iamgroot}} # User ID of User (or use case assignee)
monitor:
  
# Monitor-specific section
  schedule: ${{'*/2 * * * *'}} # Monitor schedule
  properties:
    alert_window: 24h
  incident:
    asset: caretaker-api-cert
    column: expiration_timestamp
    name: Certificate Expiry Alert
    severity: high
    incidentType: field_profiling

  # Equation monitor specification
  type: equation_monitor
  equation:
    # LHS: Time left until certificate expiration (in seconds)
    leftExpression:
      queryCoefficient: 1
      queryConstant: 0
      query:
        type: prom
        cluster: thanos
        description: Get certificate expiration timestamp and subtract current time
        ql: certmanager_certificate_expiration_timestamp_seconds{job="cert-manager-ds", name="caretaker-api-cert"} - time()
        comparisonColumn:
          name: expiration_seconds_left
          dataType: float

    # RHS: Threshold (e.g., 24 hours = 86400 seconds)
    rightExpression:
      queryCoefficient: 1
      queryConstant: 86400
      query:
        type: static
        cluster: none
        ql: ''
        comparisonColumn:
          name: threshold_seconds
          dataType: integer

    # Operator: Trigger incident if time left is less than threshold
    operator: less_than
```
<aside class="callout">
🗣️ Ensure that the metrics you are trying to observe are present in Prometheus and that the query returns valid results before applying the Monitor.
</aside>

## How it Works

- **Schedule:** The monitor runs every 2 minutes.
- **Left Expression:** Calculates how many seconds are left until the certificate expires.
- **Right Expression:** Sets the threshold (e.g., 24 hours = 86400 seconds).
- **Operator:** If the time left is less than the threshold, an incident is generated.

## Customization

- Change the `schedule` to adjust how often the monitor runs.
- Update the `ql` query to match your certificate and Prometheus setup.
- Adjust the `queryConstant` in `rightExpression` to set a different alert window (in seconds).


---

 

