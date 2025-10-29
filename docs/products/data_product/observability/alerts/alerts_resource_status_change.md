# Alerts for Resource Status Change

This section outlines how to configure a Monitor Resource that watches for a change in the status of a DataOS Resource (e.g., from `active` to `deleted`) and a Pager Resource that sends alerts when such a change is detected. This allows teams to respond quickly to unexpected state transitions, such as accidental deletions or misconfigurations.

1. Create a Monitor Resource manifest file. This manifest uses a Report Monitor to detect when a specific Resource’s status changes from `active` to `deleted`.
    
    ```yaml
    # Resource meta sectionname: runtime-monitor
    version: v1alpha
    type: monitor
    tags:
      - dataos:type:resource
      - dataos:layer:user
    description: Attention! instance secret is deleted
    layer: user
    monitor:
    
    # Monitor-specific sectionschedule: '*/2 - - - *'
      incident:
        name: depotincident
        severity: high
        incidentType: depotincident
    
      type: report_monitor
    # Report Monitor specificationreport:
        source:
          dataOsInstance:
             path: /collated/api/v1/reports/resources/status?id=depot:v2alpha:bigquery-depot
        conditions:
          - valueComparison:
              observationType: state
              valueJqFilter: '.value'
              operator: equals
              value: deleted
    ```
    
    <aside class="callout">
    🗣️ Before applying the Monitor manifest, make sure to replace the placeholder resource path or id in the monitor with the actual resource you want to track.
    </aside>

2. Validate the monitor logic by testing the condition before applying the resource.
    
    ```bash
    dataos-ctl develop observability monitor report -f /office/monitor/status_change_monitor.yaml
    ```
    
    **Expected output when the condition is not met:**
    
    ```bash
    bash
    CopyEdit
    INFO[0000] 🔮 develop observability...
    INFO[0000] 🔮 develop observability...monitor tcp-stream...starting
    INFO[0001] 🔮 develop observability...monitor tcp-stream...running
    INFO[0002] 🔮 develop observability...monitor tcp-stream...stopping
    INFO[0002] 🔮 context cancelled, monitor tcp-stream is closing.
    INFO[0003] 🔮 develop observability...complete
    
    RESULT (maxRows: 10, totalRows:0): 🟧 monitor condition not me
    ```
    
    The status remains `active`, so no incident is triggered.
    
    **Expected output when the condition is met:**
    
    ```bash
    INFO[0000] 🔮 develop observability...
    INFO[0000] 🔮 develop observability...monitor tcp-stream...starting
    INFO[0001] 🔮 develop observability...monitor tcp-stream...running
    INFO[0001] 🔮 develop observability...monitor tcp-stream...stopping
    INFO[0001] 🔮 context cancelled, monitor tcp-stream is closing.
    INFO[0002] 🔮 develop observability...complete
    
    RESULT (maxRows: 10, totalRows:1): 🟩 monitor condition met
    ```
    
    A status change (e.g., to `deleted`) is detected, triggering the incident.
    
3. Apply the Monitor Resource using the following command.
    
    ```bash
    dataos-ctl resource apply -f status-change-monitor.yaml
    ```
    
4. Verify the Monitor runtime to confirm that the monitor is running and scheduled correctly.
    
    ```bash
    dataos-ctl get runtime -t monitor -w <your-workspace> -n status-change-monitor -r
    ```
    
5. Create a Pager Resource manifest file. This file defines how and where alerts will be sent when a Resource status change is detected.
    
    ```yaml
    name: status-alert-pager
    version: v1alpha
    type: pager
    description: Alert, Resource is deleted! 
    workspace: <your-workspace>
    pager:
      conditions:
        - valueJqFilter: .properties.name
          operator: equals
          value: resource-status-alert
      output:
        msTeams:
          webHookUrl: https://rubikdatasolutions.webhook.office.com/webhookb2/09239cd8-92a8--9621-9217305bf6eec2-43f5-bf92-78e9f35a44fb/IncomingWebhook/92dcd2acdaee4e6cac125ac4a729e48f/631bd149-c89d--8979-8e364f62b419/V23AwNxCZx9JkwfToWpqDSYeRkDZ-cPn74p0HTqg1
    ```
    
6. Apply the Pager Resource using the command below.
    
    ```bash
    dataos-ctl resource apply -f status-alert-pager.yaml
    ```
    
7. Get notified! When the Resource status changes from `active` to any other value, the Monitor triggers an incident, and the Pager sends a notification to the configured destination, as shown below.
    
    <div style="text-align: center;">
    <img src="/products/data_product/observability/alerts/alerts_notified_posts_files_notes_reply.png" style="border:1px solid black; width: 70%; height: auto">
    </div>