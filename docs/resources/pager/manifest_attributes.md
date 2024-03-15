# Attributes of Pager manifest

## Structure of a Pager manifest

```yaml
pager:
  conditions:
    - valueJqFilter: ${value-jq-filter}
      operator: ${operator}
      value: ${value}
  output:
    email:
      emailTargets:
        - ${email}
        - ${email}
    msTeams:
      webHookUrl: ${web-hook-url}
    webHook:
      url: ${web-hook-url}
      headers: 
        ${key}: ${value}
      authorization:
        token: ${token}
        customHeader: ${customHeader}
      verb: ${http-operation}
      bodyTemplate: ${body-template}
```

## Pager-specific section attributes


## `pager`

**Description:** The `pager` attribute is a mapping that encapsulates attributes specific to configuring the functionalities of a Pager, such as defining conditions and specifying output destinations.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | mandatory | none | valid Pager-specific attributes |

**Example Usage:**

```yaml
pager:
  conditions:
    - valueJqFilter: .properties.name
      operator: equals
      value: malfunctiondatatool
    - valueJqFilter: .properties.incident_type
      operator: equals
      value: malfunctionsystem
  output:
    webHook:
      url: https://example.com/webhook
      verb: post
```

---

### **`conditions`**

**Description:**  The `conditions` attribute defines the conditions that the Pager Service utilizes as input for matching against all active Pagers. It identifies the Pager meeting the specified criteria and triggers the associated alert. Each condition declaration involves specifying three attributes: `valueJqFilter`, `operator`, and `value`. Multiple conditions can be added as a list of mappings, and the rule engine evaluates the conditions using AND logic.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of mapping | mandatory | none | none |

**Example Usage:**

Single condition

```yaml
pager:
  conditions:
    - valueJqFilter: .properties.name
      operator: equals
      value: workflowrunfailed
```

This condition checks whether the value of the property named "name" in the JSON data is equal to the string "workflowrunfailed.”

Multiple condition

```yaml
pager:
  conditions:
    - valueJqFilter: .properties.name
      operator: equals
      value: workflowrunfailed
    - valueJqFilter: .properties.severity
      operator: equals
      value: high
```
This condition checks whether the value of the property named "name" in the JSON data is equal to the string "workflowrunfailed”, as well as whether the value of the property named "severity" in the JSON data is equal to the string "high".

---

#### **`valueJqFilter`**

**Description:**  The `valueJqFilter` attribute specifies the JSONPath filter used to extract values from the payload of messages in the incident stream. This filter is applied to the incoming data to retrieve specific fields or properties for evaluation within the Pager Service's condition matching logic.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | valid jq filter |

**Additional Details**: You can utilize the `dataos-ctl jq` command for declaring attributes the appropriate jq filters

**Example Usage:**

Single condition

```yaml
pager:
  conditions:
    - valueJqFilter: .properties.name
      operator: equals
      value: malfunctiondatatool
```

#### **`operator`**

**Description:** The `operator` attribute specifies the comparison operator used to evaluate conditions in a Pager. It defines the type of comparison to be performed between the extracted value (using `valueJqFilter`) and the specified value (`value`).

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | equals |

**Example Usage:**

```yaml
pager:
  conditions:
    - valueJqFilter: .properties.name
      operator: equals
      value: workflowrunfailed
```

#### **`value`**

**Description:** The `value` attribute specifies the value against which the extracted value (using `valueJqFilter`) is compared within the Pager's condition evaluation. It defines the target value for comparison based on the chosen `operator`.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | any valid string |

**Example Usage:**

**Single Condition:**

```yaml
pager:
  conditions:
    - valueJqFilter: .properties.name
      operator: equals
      value: workflowrunfailed
```

In this example, the condition checks whether the value extracted from the property named "name" (using JSONPath .properties.name) is equal to the string "workflowrunfailed.”

### **`output`**

**Description:** The `output` attribute defines the destination where alerts are sent. It allows configuring different output channels for alert notifications.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| mapping | mandatory | none | Valid output destinations |

**Example Usage:**

```yaml
pager:
  output:
    email:
      emailTargets:
        - iamgroot@example.com
    msTeams:
      webHookUrl: https://teams.example.com/webhook
    webHook:
      url: https://slack.example.com/webhook
      verb: post
      headers:
        content-type: application/json
      bodyTemplate: '{"text": "Alert: {{.Monitor.Name}} triggered with severity {{.Properties.Severity}} at {{.CreateTime}}. Description: {{.Monitor.Description}}"}'
```

#### **`email`**

**Description:** The `email` attribute specifies email destinations for Pager alerts. Alerts are sent to the specified list of email addresses using a pre-defined template.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | optional | none | valid email-specific attributes |

**Example Usage:**

```yaml
pager:
  output:
    email:
      emailTargets:
        - maybe@example.com
        - imperfect@sample.com
```

---

##### **`emailTargets`**

**Description:** The `emailTargets` attribute specifies the email addresses to which Pager alerts will be sent. 

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| list of string | mandatory | none | valid email addresses in string format |

**Example Usage:**

```yaml
pager:
  output:
    email:
      emailTargets:
        - thor@avengers.com
```

---


#### **`msTeams`**

**Description:** The `msTeams` attribute specifies the Microsoft Teams webhook URL for Pager alerts.  Alerts are sent to the specified Microsoft Teams webhook URL using a pre-defined body template. To configure the body template, use the `webHook` attribute and configure the template using the `bodyTemplate` attribute.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | optional | none | none |

**Example Usage:**

```yaml
pager:
  output:
    msTeams:
      webHookUrl: https://teams.example.com/webhook
```

---

##### **`webHookUrl`**

**Description:** The `webHook` attribute configures Pager alerts to be sent to Microsoft Teams using an incoming webhook. Alerts sent using the `msTeams` and `webHookUrl` use a pre-defined body template. To configure the body template, use the `webHook` attribute and configure the template using the `bodyTemplate` attribute.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| mapping | mandatory | none | valid MS Teams incoming webhook url |

**Example Usage:**

```yaml
pager:
  output:
    msTeams:
      webHookUrl: https://teams.example.com/webhook
```

#### **`webHook`**

**Description:** The `webHook` attribute configures Pager alerts to be sent to any applications using an incoming webhook. It provides attributes to configure URL, HTTP method (verb), headers, and body template for the webhook request.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| mapping | optional | none | valid webhook configurations |

**Example Usage:**

```yaml
pager:
  output:
    webHook:
      url: https://slack.example.com/webhook
      verb: post
      headers:
        content-type: application/json
      bodyTemplate: '{"text": "Alert: {{.Monitor.Name}} triggered with severity {{.Properties.Severity}} at {{.CreateTime}}. Description: {{.Monitor.Description}}"}'
      authorization:
        token: "an apikey string"
        customHeader: "apikey"
```

---

##### **`url`**

**Description:** The `url` attribute specifies the URL of the webhook destination for Pager alerts.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | valid URL |

**Example Usage:**

```yaml
pager:
  output:
    webHook:
      url: https://slack.example.com/webhook
```

---

##### **`verb`**

**Description:** The `verb` attribute specifies the HTTP verb to be used in the webhook request (e.g., GET, POST, PUT, DELETE).

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | GET, POST, PUT, DELETE, PATCH |

**Example Usage:**

```yaml
pager:
  output:
    webHook:
      verb: POST
```

---

##### **`headers`**

**Description:** The `headers` attribute specifies any additional headers to be included in the webhook request. For specififying authorization headers like apikey tokens, use the `authorization` attribute for secured authorization.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| object | optional | none | valid HTTP headers |

**Example Usage:**

```yaml
pager:
  output:
    webHook:
      headers: 
        'Content-Type': 'application/json'
```

---

##### **`authorization`**

**Description:** The `authorization` attribute specifies the authorization details for accessing the webhook URL.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | optional | none | none |

**Example Usage:**

```yaml
pager:
  output:
    webHook:
      authorization:
        token: abcdefghijklmnopqrstuvwxyz
        customHeader: apikey
```

---

###### **`token`**

**Description:** The `token` attribute specifies the authorization token for accessing the webhook URL.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | valid authorization token |

**Example Usage:**

```yaml
pager:
  output:
    webHook:
      authorization:
        token: abcdefghijklmnopqrstuvwxyz
```

---

###### **`customHeader`**

**Description:** The `customHeader` attribute specifies any custom header to be included in the webhook request for authorization purposes.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | valid HTTP header |

**Example Usage:**

```yaml
pager:
  output:
    webHook:
      authorization:
        customHeader: apikey
```
##### **`bodyTemplate`**

**Description:** The `bodyTemplate` attribute specifies the template to be used for the body of the webhook request. It allows customization of the content sent in the webhook payload. Refer to the documentation of the respective application for guidance on crafting the template. 

For example, for Microsoft Teams, refer to the [Message Card Reference](https://learn.microsoft.com/en-us/outlook/actionable-messages/message-card-reference). You can also use a user interface to craft body templates for MS Teams visit [this link](https://amdesigner.azurewebsites.net/). Similarly, for Slack, visit [Slack webhooks](https://api.slack.com/messaging/webhooks).

The body template can also incorporate dynamic content using go text templates placeholders. For example, in the example provided below `{{.Monitor.Name}}`, `{{.Monitor.Description}}`, etc. will be replaced with actual values when the webhook is triggered. To learn more about them, consult the [Sprig Function Documentation](https://masterminds.github.io/sprig/).

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | optional | none | valid template string |

**Example Usage:**

```yaml
pager:
  output:
    webHook:
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
                "text": "*Incident Type* - {{get .Properties "severity"}} was observed at *Publish Time* - {{.CreateTime}}"
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