# How to create a custom body template for Pager?

Custom body templates in Pager allow you to define personalized message formats for notifications sent via webhooks and email. This enables you to tailor the appearance and content of alerts sent to various destinations like Microsoft Teams, Slack, email, or any other webhook-supported application. By default, Pager sends alerts using predefined templates. However, custom body templates provide the flexibility to:

- Customize message formatting and appearance
- Include specific incident data fields
- Adapt messages for different notification platforms
- Create rich, interactive notifications (like Adaptive Cards for MS Teams)

## Template types

Pager supports two custom template engines for both email and webhook templates:

- **Liquid templating** (recommended)
- **Go text templates**

## Manifest configuration structure

Custom body templates can be used in two different output configurations:

=== "For email templates"

    ```yaml
    pager:
      output:
        email:
          emailTargets:
            - user@example.com
          templateType: liquid  # Recommended - or "go" (fully supported)
          bodyTemplate: |
            # Your custom HTML or plain text email template here
    ```

=== "For webhook templates (including MS Teams)"

    ```yaml
    pager:
      output:
        webHook:
          url: ${webhook-url}
          verb: post
          contentType: application/json
          templateType: liquid  # Recommended 
          bodyTemplate: |
            # Your custom JSON webhook payload template here
    ```

<aside class="callout">
🗣️ Going forward, please use `Liquid` instead of `Go` when configuring the `bodyTemplate` in Pager for MS Teams webhook. While both template engines are supported, `Go` templates for MS Teams webhook are in legacy support mode.
</aside>

## Examples

=== "Microsoft Teams examples"

    Below are examples for sending Pager notifications to Microsoft Teams using custom body templates. Using Adaptive Cards and Message Cards (legacy).

    <details>
      <summary>Adaptive card template (liquid)</summary>

      ```yaml
      # Resource meta section 
      name: testalerts                   # mandatory
      version: v1alpha                              # mandatory
      type: pager                                   # mandatory
      description: testing pager                    # mandatory

      # Pager-specific section 
      pager: 
        conditions:                                 # mandatory
          - valueJqFilter: .properties.severity
            operator: equals
            value: high

        # Output 
        output:                                     # mandatory
          email:
            emailTargets:                           # mandatory
              - iamgroot@tmdc.io 
              - thisisthor@tmdc.io

          webHook: 
            url: https://rubikdatasolutions.webhook.office.com/webhookb2/09239cd8-92a8-4d59-9621-92175bf6bdde-3ec2-43f5-bf92-78e9f35a44fb/IncomingWebhook/fb6f86b6b36aa2f25634531ea65c/631bd149-c89d-4d3b-8-8ef62b419/V2GRmwzBgUEv2Ymj7BFOFNLg7dk5AlFT9fl2KM1                   # mandatory
            verb: post                              # mandatory
            contentType: application/json  # mandatory
            templateType: liquid          # optional
            bodyTemplate: |
            {
                "@type": "AdaptiveCard",
                "summary": Service has Failed",
                "themeColor": "0076D7",
                "sections": [
                  {
                    "activityTitle": "Sending this alert,",
                    "activitySubtitle": "⚠️ Our system detected an issue with the service and was unable to complete the process as expected.",
                    "facts": [
                      {
                        "name": "service:",
                        {% assign id_parts = reportContext.resourceId | split: ':' %}
                        {% assign type = id_parts[0] %}
                        {% assign version = id_parts[1] %}
                        {% assign name = id_parts[2] %}
                        {% assign workspace = id_parts[3] %}
                        "value": "{{ name }}"
                      },
                      {
                        "name": "Failure Time:",
                        "value": "{{ createTime }}"
                      },
                      {
                        "name": "Severity:",
                        "value": "{{ properties.severity }}"
                      },
                      {
                        "name": "Run Details:",
                        "value": "[View Run Details](https://liberal-katydid.dataos.app/operations/user-space/resources/resource-runtime?name={{ name }}&type=service&workspace={{ workspace }})"
                      },
                      {
                        "name": "Logs:",
                        "value": "[View Logs](https://liberal-katydid.dataos.app/metis/resources/service/dataos.{{ workspace }}.{{ name }}/run_history)"
                      }
                    ]
                  },
                  {
                    "text": "We understand the importance of timely and accurate data processing, and our team is actively working to resolve the issue and get the pipeline back up and running as soon as possible.\n\nIf you have any questions or concerns, please reach out to us on our [support portal](https://support.yourcompany.com)."
                  },
                  {
                    "text": "Best regards,\n\nThe Modern Data Company"
                  }
                ]
              }
      ```
      </details>


    <details>
      <summary>Message card template (liquid)</summary>

      For organizations still using Message card format (legacy):

      ```yaml
      # Resource meta section 
      name: testalerts                   # mandatory
      version: v1alpha                              # mandatory
      type: pager                                   # mandatory
      description: testing pager                    # mandatory

      # Pager-specific section 
      pager: 
        conditions:                                 # mandatory
          - valueJqFilter: .properties.severity
            operator: equals
            value: high

        # Output 
        output:                                     # mandatory
          email:
            emailTargets:                           # mandatory
              - iamgroot@tmdc.io 
              - thisisthor@tmdc.io

          webHook: 
            url: https://rubikdatasolutions.webhook.office.com/webhookb2/09239cd8-92a8-4d59-9621-9217bf6ed2bdde-3ec2-43f5-bf92-78e9f35a44fb/IncomingWebhook/fb6f86b662aa2f254531ea65c/631bd149-c89d-4d3b-8979-8e3f62b419/V2GRmwzBgUEv2Ymj7BFO5KLbFJpI75AlFT9fl2KM1                   # mandatory
            verb: post                              # mandatory
            contentType: application/json  # mandatory
            # authorization:                          # optional
            #   token: ${{webhook-token}}                       # mandatory
            #   customHeader: ${{webhook-custom-header}}        # optional
            templateType: liquid          # optional
            # headers:                                          # optional
            #   'content-type': '${{webhook-content-type}}'     # mandatory
            bodyTemplate: |
            {
                "@type": "MessageCard",
                "summary": "Service has Failed",
                "themeColor": "0076D7",
                "sections": [
                  {
                    "activityTitle": "Sending this alert,",
                    "activitySubtitle": "⚠️ Our system detected an issue with the service and was unable to complete the process as expected.",
                    "facts": [
                      {
                        "name": "service:",
                        {% assign id_parts = reportContext.resourceId | split: ':' %}
                        {% assign type = id_parts[0] %}
                        {% assign version = id_parts[1] %}
                        {% assign name = id_parts[2] %}
                        {% assign workspace = id_parts[3] %}
                        "value": "{{ name }}"
                      },
                      {
                        "name": "Failure Time:",
                        "value": "{{ createTime }}"
                      },
                      {
                        "name": "Severity:",
                        "value": "{{ properties.severity }}"
                      },
                      {
                        "name": "Run Details:",
                        "value": "[View Run Details](https://liberal-katydid.dataos.app/operations/user-space/resources/resource-runtime?name={{ name }}&type=service&workspace={{ workspace }})"
                      },
                      {
                        "name": "Logs:",
                        "value": "[View Logs](https://liberal-katydid.dataos.app/metis/resources/service/dataos.{{ workspace }}.{{ name }}/run_history)"
                      }
                    ]
                  },
                  {
                    "text": "We understand the importance of timely and accurate data processing, and our team is actively working to resolve the issue and get the pipeline back up and running as soon as possible.\n\nIf you have any questions or concerns, please reach out to us on our [support portal](https://support.yourcompany.com)."
                  },
                  {
                    "text": "Best regards,\n\nThe Modern Data Company"
                  }
                ]
              }
      ```

=== "Email examples"

    For custom email notifications with HTML formatting:
    <details>
      <summary>HTML email template (liquid)</summary>

      ```yaml
      name: custom-email-pager
      version: v1alpha
      type: pager
      description: Email pager with custom HTML template

      pager:
        conditions:
          - valueJqFilter: .properties.severity
            operator: equals
            value: high
        
        output:
          email:
            emailTargets:
              - admin@company.com
              - devops@company.com
            templateType: liquid
            bodyTemplate: |
              <!DOCTYPE html>
              <html>
              <head>
                <meta charset="utf-8">
                <title>DataOS Alert - {{ properties.severity | capitalize }} Severity</title>
                <style>
                  body { font-family: Arial, sans-serif; margin: 20px; }
                  .alert-container { max-width: 600px; margin: 0 auto; }
                  .header { background-color: {% if properties.severity == 'critical' %}#dc3545{% elsif properties.severity == 'high' %}#fd7e14{% else %}#28a745{% endif %}; color: white; padding: 20px; border-radius: 5px 5px 0 0; }
                  .content { border: 1px solid #ddd; padding: 20px; border-radius: 0 0 5px 5px; }
                  .info-table { width: 100%; border-collapse: collapse; margin: 20px 0; }
                  .info-table th, .info-table td { padding: 10px; text-align: left; border-bottom: 1px solid #ddd; }
                  .info-table th { background-color: #f8f9fa; font-weight: bold; }
                  .action-buttons { text-align: center; margin: 20px 0; }
                  .btn { display: inline-block; padding: 10px 20px; background-color: #007bff; color: white; text-decoration: none; border-radius: 5px; margin: 0 10px; }
                  .footer { text-align: center; margin: 20px 0; color: #666; font-size: 12px; }
                </style>
              </head>
              <body>
                <div class="alert-container">
                  <div class="header">
                    <h1>🚨 DataOS Alert: {{ properties.severity | capitalize }} Severity</h1>
                    <p>{{ createTime | date: '%B %d, %Y at %I:%M %p UTC' }}</p>
                  </div>
                  
                  <div class="content">
                    {% assign id_parts = reportContext.resourceId | split: ':' %}
                    {% assign resource_type = id_parts[0] %}
                    {% assign version = id_parts[1] %}
                    {% assign name = id_parts[2] %}
                    {% assign workspace = id_parts[3] %}
                    
                    <p><strong>Alert Summary:</strong> An incident has been detected in your DataOS environment that requires attention.</p>
                    
                    <table class="info-table">
                      <tr>
                        <th>Service Name</th>
                        <td>{{ name | default: 'Unknown' }}</td>
                      </tr>
                      <tr>
                        <th>Workspace</th>
                        <td>{{ workspace | default: 'Unknown' }}</td>
                      </tr>
                      <tr>
                        <th>Resource Type</th>
                        <td>{{ resource_type | default: 'Unknown' }}</td>
                      </tr>
                      <tr>
                        <th>Severity</th>
                        <td><span style="color: {% if properties.severity == 'critical' %}#dc3545{% elsif properties.severity == 'high' %}#fd7e14{% else %}#28a745{% endif %}; font-weight: bold;">{{ properties.severity | capitalize | default: 'Unknown' }}</span></td>
                      </tr>
                      <tr>
                        <th>Incident Type</th>
                        <td>{{ properties.incident_type | default: 'Service Issue' }}</td>
                      </tr>
                      <tr>
                        <th>Monitor</th>
                        <td>{{ monitor.name | default: 'System Monitor' }}</td>
                      </tr>
                      {% if monitor.description %}
                      <tr>
                        <th>Description</th>
                        <td>{{ monitor.description }}</td>
                      </tr>
                      {% endif %}
                      <tr>
                        <th>Incident ID</th>
                        <td>{{ reportContext.incidentId | default: 'N/A' }}</td>
                      </tr>
                    </table>
                    
                    <div class="action-buttons">
                      <a href="https://liberal-katydid.dataos.app/operations/user-space/resources/resource-runtime?name={{ name }}&type={{ resource_type }}&workspace={{ workspace }}" class="btn">View Resource Details</a>
                      <a href="https://liberal-katydid.dataos.app/metis/resources/{{ resource_type }}/dataos.{{ workspace }}.{{ name }}/run_history" class="btn">View Logs</a>
                    </div>
                    
                    <p><em>Please investigate this issue promptly. If you need assistance, contact the DataOS support team.</em></p>
                  </div>
                  
                  <div class="footer">
                    <p>This alert was generated by DataOS Pager Service</p>
                    <p>Time: {{ createTime }}</p>
                  </div>
                </div>
              </body>
              </html>
      ```
    </details>
 
    For simple plain text email notifications using Go templates: 
      
    <details>
      <summary>Plain text email template (Go)</summary>

      ```yaml
      name: plaintext-email-pager
      version: v1alpha
      type: pager
      description: Plain text email pager using Go templates

      pager:
        conditions:
          - valueJqFilter: .properties.severity
            operator: equals
            value: medium
        
        output:
          email:
            emailTargets:
              - alerts@company.com
            templateType: go
            bodyTemplate: |
              DataOS Alert Notification
              ========================
              
              Alert Time: {{ .CreateTime }}
              Severity: {{ .Properties.severity | upper }}
              
              {{ $resourceParts := split .ReportContext.ResourceId ":" }}
              Service Details:
              - Name: {{ index $resourceParts 2 }}
              - Type: {{ index $resourceParts 0 }}
              - Workspace: {{ index $resourceParts 3 }}
              - Version: {{ index $resourceParts 1 }}
              
              Incident Information:
              - ID: {{ .ReportContext.IncidentId }}
              - Type: {{ .Properties.incident_type }}
              - Monitor: {{ .Monitor.Name }}
              {{ if .Monitor.Description }}- Description: {{ .Monitor.Description }}{{ end }}
              
              Action Required:
              Please investigate this {{ .Properties.severity }} severity incident immediately.
              
              Quick Links:
              - Resource Details: https://liberal-katydid.dataos.app/operations/user-space/resources/resource-runtime?name={{ index $resourceParts 2 }}&type={{ index $resourceParts 0 }}&workspace={{ index $resourceParts 3 }}
              - Logs: https://liberal-katydid.dataos.app/metis/resources/{{ index $resourceParts 0 }}/dataos.{{ index $resourceParts 3 }}.{{ index $resourceParts 2 }}/run_history
              
              ---
              This is an automated message from DataOS Pager Service.
              Please do not reply to this email.
      ```
    </details>

## Output

Below is an example of how a custom body template notification appears in Microsoft Teams.

<div style="text-align: center;">
  <img src="/resources/pager/usage_examples/custom_body_template.png" alt="Custom Body Template Outputr" style="border:1px solid black; width: 60%; height: auto;">
  <figcaption><i>Custom Body Template Output</i></figcaption>
</div>

## Template syntax guide

When creating custom body templates, you have access to the following common variables from the incident data:

**Core variables**

| Variable | Description | Example Value |
|----------|-------------|---------------|
| `createTime` | Timestamp when the incident was created | `2024-01-15T10:30:00Z` |
| `properties.severity` | Severity level of the incident | `high`, `medium`, `low`, `critical` |
| `properties.incident_type` | Type of incident | `service_failure`, `data_quality_issue` |
| `properties.name` | Name of the affected resource | `user-service` |
| `monitor.name` | Name of the monitor that triggered | `service-health-monitor` |
| `monitor.description` | Description of the monitor | `Monitors service availability` |
| `reportContext.resourceId` | Full resource identifier | `service:v1:user-service:public` |
| `reportContext.incidentId` | Unique incident identifier | `inc-123456789` |

**Resource ID components (when using split)**

The `reportContext.resourceId` follows the pattern: `type:version:name:workspace`

```liquid
{% assign id_parts = reportContext.resourceId | split: ':' %}
{% assign resource_type = id_parts[0] %}     <!-- service -->
{% assign version = id_parts[1] %}           <!-- v1 -->
{% assign name = id_parts[2] %}              <!-- user-service -->
{% assign workspace = id_parts[3] %}         <!-- public -->
```

**Liquid template syntax**

Liquid templates use `{{ }}` for output and `{% %}` for logic:

```liquid
<!-- Output variables -->
{{ properties.severity }}
{{ createTime }}

<!-- String manipulation -->
{{ properties.name | capitalize }}
{{ createTime | date: '%Y-%m-%d %H:%M:%S' }}

<!-- Conditionals -->
{% if properties.severity == 'critical' %}
  "color": "#ff0000"
{% elsif properties.severity == 'high' %}
  "color": "#ff9900"
{% else %}
  "color": "#00ff00"
{% endif %}

<!-- Loops (if working with arrays) -->
{% for tag in properties.tags %}
  "{{ tag }}"
{% endfor %}

<!-- Variable assignment -->
{% assign id_parts = reportContext.resourceId | split: ':' %}
{{ id_parts[2] }}  <!-- Outputs the service name -->
```

**Go template syntax**

Go templates use `{{ }}` for both output and logic:

```go
<!-- Output variables -->
{{ .Properties.severity }}
{{ .CreateTime }}

<!-- String functions -->
{{ .Properties.name | title }}

<!-- Conditionals -->
{{ if eq .Properties.severity "critical" }}
  "color": "#ff0000"
{{ else if eq .Properties.severity "high" }}
  "color": "#ff9900"
{{ else }}
  "color": "#00ff00"
{{ end }}

<!-- String splitting -->
{{ index (split .ReportContext.ResourceId ":") 2 }}
```

## Best practices

To ensure the custom body templates are working as expected across notification channels, follow these best practices when implementing templates.

- Always validate your JSON structure using online JSON validators.

- Provide default values for variables that might be missing:

    ```liquid
    {{ properties.name | default: 'Unknown Service' }}
    ```

- Use conditional checks for optional fields:

    ```liquid
    {% if monitor.description %}
      "description": "{{ monitor.description }}"
    {% endif %}
    ```

- Avoid exposing sensitive information in templates.

- Use Adaptive Cards for rich, interactive notifications:

    - Follow Microsoft's [Adaptive Card schema](https://adaptivecards.io/explorer/)
    - Test cards using the [Adaptive Card Designer](https://adaptivecards.io/designer/)

- Check Pager service logs for template parsing errors in Operations app.

    <div style="text-align: center;">
      <img src="/resources/pager/ops.png" alt="Operations app" style="border:1px solid black; width: 80%; height: auto;">
      <figcaption><i>Operations app</i></figcaption>
    </div>


## Troubleshooting

If the custom body template does not render as expected or Pager notifications fail to deliver, use the following checklist to diagnose and resolve common issues.

- Check for missing quotes or commas in JSON.

- Ensure proper escaping of special characters.

- Validate template syntax for your chosen engine.

- Verify variable names match the incident data structure.

- Check Pager service logs for undefined variable warnings.

- Verify webhook URL is accessible.

- Check authentication headers and tokens.

- Ensure content-type matches the expected format.

