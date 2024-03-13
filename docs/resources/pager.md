# Pager

What is a Pager?


Why seperate it from Monitor?


How to create a Pager?


How does a Pager Work?


How to configure a Pager?

```yaml title="pager_advanced_configuration.yaml"
pager:
  conditions: # mandatory
    - valueJqFilter: ${string} # mandatory
      operator: ${equals} # mandatory
      value: string # mandatory
  output: # mandatory
    email: 
      emailTargets: # mandatory
        - <email 1>
        - <email 2>
    msTeams: 
      webHookUrl: # mandatory
    webHook: 
      url: ${webhook-url} # mandatory
      headers:  <object>
      authorization: 
        token: ${token}
        customHeader: ${customHeader}
      verb: GET # mandatory
      bodyTemplate: <string> 
```




How to use a Pager?



A Pager enables users to specify criteria for **identifying an incident** from the incident stream and **delivering it** to a user-specified destination. Here is how it works.

1. A pager constantly reads incident messages from the incident stream.
2. If an incident matches the specific attributes.
3. It delivers the incident as a notification to the specified destination.

## How does a Pager work?

### Functional Operation of a Monitor

The Pager takes in two configurations

1. **The Condition**
    
    This is the condition that the incident must meet to raise a notification. The pager will check for these key-value pairs in the incident message. A notification is shot when the key-value pairs are matched.
    
2. **The Output**
    
    This is where you provide the destinations for the notification.
    

When you apply a Pager YAML file through the CLI, the conditions are converted to rules with a Rules Engine.

## Structure of a Pager manifest

```yaml
name: pager-workflow-runtime-fail-alert
version: v1alpha
type: pager
description: sends alerts to email and teams when a workflow fail to run.
pager:
  conditions:
    - valueJqFilter: .properties.name
      operator: equals
      value: workflowrunfailed
    - valueJqFilter: .properties.severity
      operator: equals
      value: high
  output:
    email:
      emailTargets:
        - nikhil.singh@tmdc.io
    msTeams:
      webHookUrl: https://rubikdatasolutions.webhook.office.com/webhookb2/7c004d4a-6898-4def-bdc9-de2a25273d5b@2e22bdde-3ec2-43f5-bf92-78e9f35a44fb/IncomingWebhook/f2941ebdd68e4ed18e297a9626033dd0/671804a0-c038-4e23-8ddd-f5990f82f548
    webHook: 
      url: https://hooks.slack.com/services/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
      # authorization:
      #   token: 
      #   customHeader: 
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

### Understanding Pager spec

- `conditions` Define the conditions in this section that the pager service will use as input. The service will match these conditions against all active pagers, identifying the one that meets the specified criteria, and then execute it.
    - `valueJqFilter` Define a JQ filter expression that extracts a specific value from the data.
        - `valueJqFilter: .properties.name
        operator: equals
        value: workflowrunfailed`
            
            This condition checks whether the value of the property named "name" in the JSON data (likely within a larger context not provided here) is equal to the string "workflowrunfailed.”
            
        - `valueJqFilter: .properties.severity
        operator: equals
        value: high`
            
            This condition checks whether the value of the property named "severity" in the JSON data is equal to the string "high.”
            
- `output` Define the destination of alert here.
    - `emailTargets` Sends email alerts to the specified email address: in this case email to nikhil.singh@tmdc.io.
    - `msTeams` Sends alerts to Microsoft Teams using a webhook.
    - `webHook` Send pager alerts to any applications using incoming webhook. The current example is of sending alerts to slack using an incoming webhook. Below is the explanation of how to configure a slack message.
        
        Configure, http message under the webHook section, by providing 
        
        1. `url`: A string representing the URL where the webhook will send the POST request.
        2. **`verb`:** A string representing the HTTP method used for the request, which is "post" in this case.
        3. **`headers`:** An object containing additional headers to be included in the request. In this case, it specifies the content type as JSON.
            1. **'content-type':** A string representing the content type of the request, which is "application/json".
        4. **`bodyTemplate`:** A string representing the template for the body of the POST request. This will be sent as JSON to the specified URL. 
            1. The body template in this example includes dynamic content using placeholders like **`{{.Monitor.Name}}`**, **`{{.Properties.Severity}}`**, **`{{.CreateTime}}`**, and **`{{.Monitor.Description}}`** which will be replaced with actual values when the webhook is triggered.
        5. `authorization`: This is an object representing authorization details for the webhook. Which in this example is not needed, since the slack doesn’t require any additional authorization params. All the auth details are contained in its webhook itself. But other applications will require this config.
            - **token:** A string representing an authorization token. e.g ‘an apikey string’
            - **customHeader:** A string representing a custom header for authorization. e.g. ‘apikey’

Create and apply a pager through CLI

1. Create a pager based on the spec defined [here](https://www.notion.so/Pager-2-0-954f5ca4834c419ba490f3ca707d5479?pvs=21).
2. Apply it through CLI

```shell
dataos-ctl apply -f {{yaml-file-path}}
```
eg.

```shell
dataos-ctl apply -f /Users/soumadipde/Downloads/Testing_Monitors/xx_watcher3.yml
```

The CLI shows that the pager has been created

