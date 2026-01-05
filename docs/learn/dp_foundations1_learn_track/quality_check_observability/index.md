# Create Monitor and Pager for quality checks 

!!! info "Overview"
    In this module, you'll learn how to configure Monitor and Pager resources in DataOS to proactively detect data quality check failures and send real-time alerts to your team. This ensures faster incident response and improves the overall reliability of your Data Products.

---

## 📘 Scenario

You are working with customer data from your CRM system. This data powers applications and dashboards used by your sales and marketing teams. Recently, some quality issues—like missing values and invalid formats—went unnoticed and caused problems in reporting. To avoid this in the future, you need to:

- Set up a Monitor that checks for failed quality checks in the crm_data collection.

- Create a Pager that sends an alert to your team on Microsoft Teams when a failure happens.

In this exercise, you’ll configure both the Monitor and Pager using the templates provided. 

## What you'll do

1. Review and understand a sample Monitor configuration for Soda quality checks.

2. Configure a Pager to send alerts (e.g., via Microsoft Teams webhook/mail).

3. Update the webhook URL and customize identifiers as needed.

**📜 Templates:**

- **Quality Checks Monitor**
    
    ```yaml
    # Important: Replace 'abc' with your initials to personalize and distinguish the resource you’ve created.
    name: quality-checks-alerts-abc
    version: v1alpha
    type: monitor
    tags:
      - dataos:type:resource
      - dataos:layer:user
    description: Alerts ..! recent quality check has resulted in a failure due to ambiguities found in the data. It appears there are inconsistencies or inaccu racies that require your immediate attention. To ensure the integrity and re liability of the data,Your prompt action in addressing these discrepancies will greatly assist us in maintaining the highest standards of quality.
    layer: user
    monitor:
      schedule: '30 9 * * 1-5'
      type: equation_monitor
      equation:
        leftExpression:
          queryCoefficient: 1
          queryConstant: 0
          query:
            type: trino
            cluster: system
            ql: |
              WITH checks AS (
                  SELECT
                    CASE
                      WHEN check_outcome = 'fail' THEN 0
                      ELSE 1
                    END AS result,
                    check_definition
                  FROM
                    lakehouse.sys01.soda_quality_checks
                  WHERE
                    collection = 'crm_data'
                )
                SELECT check_definition ,
                  result
                FROM checks
        comparisonColumn:
          name: result
          dataType: int64
        rightExpression:
          queryCoefficient: 0
          queryConstant: 0
      operator: equals
      incident:
        name: checkfailsoda
        severity: high
        incident_type: sodaquality
    
    ```
> ⚠️ Important: A workflow must be set up to sink SodaStream incidents into the Lakehouse for this monitor to function correctly. Contact your training team to verify this setup.
    
- **Quality Checks Pager**
<details><summary>Click here to view the complete manifest file for email notification</summary>
```
# Important: Replace 'abc' with your initials to personalize and distinguish the resource you’ve created.
name: pager-checks-alert-abc
version: v1alpha
type: pager
tags:
  - dataos:type:resource
description: This is for sending Alerts on Microsoft Teams Alert Test channel
workspace: public
pager:
  conditions:
    - valueJqFilter: .properties.name
      operator: equals
      value: Soda Fail Checks
    - valueJqFilter: .properties.incident_type
      operator: equals
      value: Soda Quality Checks
  output:
    email:
      emailTargets:
        - deepak.jaiswal@tmdc.io
      templateType: liquid
      template: |
        <p><strong>Dear Team,</strong></p>

        <p>⚠️ Alerts: Data quality check failed due to inconsistencies and inaccuracies; immediate action required to maintain integrity and reliability.</p>

        <div style="font-family: Arial, sans-serif;">
          <table border="0" cellspacing="0" cellpadding="8" style="font-family: Arial, sans-serif; font-size: 14px; width: 100%; border-collapse: collapse;">
            <tbody>
              <tr style="border-top: 2px solid #000; border-bottom: 1px solid #ccc;">
                <td style="font-weight: bold;">Incident Name</td>
                <td>{{ incidentProperties.name }}</td>
              </tr>
              <tr style="border-bottom: 1px solid #ccc;">
                <td style="font-weight: bold;">Severity</td>
                <td>{{ incidentProperties.severity }}</td>
              </tr>
              <tr style="border-bottom: 1px solid #ccc;">
                <td style="font-weight: bold;">Failure Time</td>
                <td>{{ incidentCreated }}</td>
              </tr>
              <tr style="border-bottom: 2px solid #000;">
                <td style="font-weight: bold;">Failed Checks</td>
                <td>
                  <table style="width: 100%; border-collapse: collapse; margin-top: 10px;">
                    <thead>
                      <tr style="border-bottom: 2px solid #000;">
                        <th style="text-align: left; padding: 5px; font-weight: bold;">Check Definition</th>
                        <th style="text-align: left; padding: 5px; font-weight: bold;">Metric Name</th>
                      </tr>
                    </thead>
                    <tbody>
                      {% for check in incidentContext.data %}
                        <tr>
                          <td style="padding: 5px;">{{ check.leftRow.contextColumns[0].value }}</td>
                          <td style="padding: 5px;">{{ check.leftRow.contextColumns[1].value }}</td>
                        </tr>
                      {% endfor %}
                    </tbody>
                  </table>
                </td>
              </tr>
            </tbody>
          </table>
        </div>

        <p>Best regards,</p>

        <p>The Modern Data Company</p>


```
</details>

<details><summary>Click here to view the complete manifest file for webhook notification</summary>
    
  ```yaml
  # Important: Replace 'abc' with your initials to personalize and distinguish the resource you’ve created.
  name: pager-checks-alert-abc
  version: v1alpha
  type: pager
  tags:
    - dataos:type:resource
  description: This is for sending Alerts to Microsoft Teams Alert Test chan nel
  workspace: public
  pager:
    conditions:
      - valueJqFilter: .properties.name
        operator: equals
        value: manishsodaincident
      - valueJqFilter: .properties.incident_type
        operator: equals
        value: sodaquality
    output:
      webHook:
        url: <Your webhook url>
        verb: post
        headers:
          'content-type': 'application/json'
        bodyTemplate: |
          {
            "@type": "MessageCard",
            "summary": "Alert on Quality Check failure",
            "themeColor": "FF0000",
            "sections": [
              {
                "activityTitle": "Dear Team,",
                "activitySubtitle": "⚠ Quality check has been failed. Please revi ew this.",
                "facts": [
                  {
                    "name": "Failure Time:",
                    "value": "{{ .CreateTime }}"
                  },
                  {
                    "name": "Severity:",
                    "value": "{{ .Properties.severity }}"
                  } ,
                  {
                    "name": "Alert:",
                    "value": "{{range .EquationContext.QueryExpressions}}{{range .LeftRow.ContextColumns}}{{if eq .Name \"check_definition\"}} {{.Value}}, {{end}}{{end}}{{end}}"
                  }
                ]
              }
            ]
          }
  
  ```
  </details>
    
  > **Important Note:** This pager is designed to receive alerts triggered by the quality-checks-alerts monitor. Full implementation depends on the SodaStream incident workflow being in place. Contact your training team to confirm it.
  >

## Checklist

- ✅  Check the schedule defined in the Monitor YAML.
- ✅  Review the conditions and bodyTemplate in the pager manifest.
- ✅  Update the URL in the webhook section with the actual webhook URL.

## Next step

With monitors and pagers in place for quality checks, it's time to bundle all your components, define the Data Product specification, and register it in the Data Product Hub.

👉 Refer to the next topic: [Create a deployment Bundle](/learn/dp_foundations1_learn_track/create_bundle/).