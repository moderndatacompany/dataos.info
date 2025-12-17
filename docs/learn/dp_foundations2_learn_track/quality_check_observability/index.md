# Create Monitor and Pager for quality checks 

In this module, you'll learn how to configure Monitor and Pager resources in DataOS to proactively detect data quality check failures and send real-time alerts to your team. This ensures faster incident response and improves the overall reliability of your Data Products.

---

## Scenario



> ⚠️ Important: A workflow must be set up to sink SodaStream incidents into the Lakehouse for this monitor to function correctly. Contact your training team to verify this setup.

## What You'll Do

1. Review and understand a sample Monitor configuration for Soda quality checks.

2. Configure a Pager to send alerts (e.g., via Microsoft Teams webhook).

3. Update the webhook URL and customize identifiers as needed.



1. Review the template to understand how a quality checks monitor is configured.
2. Review the template to understand how a quality checks pager is configured. Ensure you update the webhook URL.

**📜 Templates:**

- **Quality Checks Monitor**
    
    ```yaml
    **# Important:** Replace 'abc' with your initials to personalize and distinguish the resource you’ve created.
    name: quality-checks-alerts-abc
    version: v1alpha
    type: monitor
    tags:
      - dataos:type:resource
      - dataos:layer:user
    description: Alerts ..! recent quality check has resulted in a failure due to a mbiguities found in the data. It appears there are inconsistencies or inaccu racies that require your immediate attention. To ensure the integrity and re liability of the data,Your prompt action in addressing these discrepancies will greatly assist us in maintaining the highest standards of quality.
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
    
- **Quality Checks Pager**
    
    ```yaml
    **# Important:** Replace 'abc' with your initials to personalize and distinguish the resource you’ve created.
    name: pager-checks-alert-abc
    version: v1alpha
    type: pager
    tags:
      - dataos:type:resource
    description: This is for sending Alerts on Microsoft Teams Alert Test chan nel
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
    
    > **Important Note:** This pager is designed to receive alerts triggered by the quality-checks-alerts monitor. Full implementation depends on the SodaStream incident workflow being in place. Contact your training team to confirm it.
    >

## Checklist

- [ ]  Check the schedule defined in the Monitor YAML.
- [ ]  Review the conditions and bodyTemplate in the pager manifest.
- [ ]  Update the URL in the webhook section with the actual webhook URL.

## Next Step

With monitors and pagers in place for quality checks, it's time to bundle all your components, define the Data Product specification, and register it in the Data Product Hub.

👉 Refer to the next topic: [Create a deployment Bundle](/learn/dp_foundations1_learn_track/create_bundle/).