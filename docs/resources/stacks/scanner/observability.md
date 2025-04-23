# Observability in Scanner Stack

The Monitor Resource is an integral part of DataOS’ Observability system,. It is designed to trigger incidents based on specific events or metrics. By leveraging the Monitor Resource alongside the Pager Resource for sending alerts, users can achieve comprehensive observability and proactive incident management over Scanner which ensure high Scanner reliability and performance.

User can easily track the status or runtime of a Scanner whether it is active, running, failed or deleted using the Monitor Resource and Metis UI. Additionally, Pager Resource is also configure to receive notifications if a Scanner is failed, deleted or succeed. Following are the steps to create the Monitor and Pager for the Scanner:


## Step 1: Create a Monitor manifest file for Scanner

User can create a Monitor with the help of sample manifest file that contains the different configurations as shown below:

```yaml
# Resource meta section
name: ${{runtime-monitor}} 
version: ${{v1alpha}}
type: monitor
tags: 
  - ${{dataos:type:resource}}
  - ${{dataos:layer:user}}
description: ${{Attention! workflow run is succeeded.}}
layer: ${{user}}
monitor: 

# Monitor-specific section
  schedule: ${{'*/3 * * * *'}} 
  incident: 
    name: ${{workflowrunning}}
    severity: ${{high}}
    incidentType: ${{workflowruntime}}

  type: {{report_monitor}}
# Report Monitor specification
  report: 
    source: 
      dataOsInstance: 
        path: ${{/collated/api/v1/reports/resources/runtime?id=workflow:v1:scan-data-product-test:public}}
    conditions: 
      - valueComparison: 
          observationType: ${{runtime}}
          valueJqFilter: ${{'.value'}
          operator: ${{equals}}
          value: ${{succeeded}}}
```

Before applying the Monitor Resource file, it is recommended to check the response of the API endpoint and configure the attributes of the manifest file.


## Step 2: Apply the Monitor manifest file

After configuring the attribute and validating the API endpoint, the next step is to apply the Monitor manifest file by executing the code below.

```bash
dataos-ctl resource apply -f ${{path-of-your-manifest-file}} -w ${{workspace_name}}
```


## Step 3: Validate runtime of the Monitor

Validate or check the runtime of the Monitor by executing the below command.

```bash
dataos-ctl get runtime -t monitor -w ${{workspace_name}} -n ${{monitor_name}} -r
```

Now whenever the Monitor condition is met, it will trigger an incident.


## Step 4: Create a Pager manifest file for Scanner

This incident is delivered to a user specified destination (like web-hook, email, etc). It operates by evaluating pre-defined conditions against incoming incident data from the incident stream. It triggers an alert and delivers it to the specified destination on getting a match. Following is the sample manifest file for the pager:

```yaml
# Resource meta section 
name: pager-workflow-runtime-fail-alert
version: v1alpha
type: pager
description: sends alerts to email and teams when a workflow fail to run.

# Pager-specific section 
pager: 

  # Conditions 
  conditions: 
    - valueJqFilter: .properties.name
      operator: equals
      value: workflowrunfailed
    - valueJqFilter: .properties.severity
      operator: equals
      value: high

  # Output 
  output: 
    email: 
      emailTargets: 
        - thor@example.com
        - ironman@example.com
    msTeams: 
      webHookUrl: https://example.com/webhook
    webHook:  
      url: https://example.com/webhook
      verb: post
      headers: 
        'content-type': 'application/json'
      bodyTemplate: |
        {
          "blocks": [
            {
              "type": "header",
              "text": {
                "type": "plain_text",
                "text": ":warning: Incident detected by, {{.Monitor.Name}}!"
              }
            },
            {
              "type": "section",
              "text": {
                "type": "mrkdwn",
                "text": "*Incident Type* - {{.Properties.Severity}} was observed at *Publish Time* - {{.CreateTime}}"
              }
            },
            {
              "type": "section",
              "text": {
                "type": "mrkdwn",
                "text": "{{.Monitor.Description}}"
              }
            }
          ]
        }
```


## Step 5: Apply the Pager

After configuring the attributes of the Pager, user can execute the manifest file by using the code below:

```bash
dataos-ctl resource apply -f ${{path-of-your-manifest-file}} -w ${{workspace_name}}
```

This will generate a notification on the specified user channel or emails whenever the conditions of the incident are met.
