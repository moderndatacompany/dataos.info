# How to observe an Instance Secret?

Track the status of an Instance Secret—whether it is active or deleted—using the Monitor Resource and Metis UI. Additionally, configure Pager Resource to receive notifications if an Instance Secret is deleted.

## Metric monitoring

### **How to monitor the status using Metis UI?**

Users can track the status of an Instance Secret, whether active or deleted, along with the total count of active and deleted Instance Secrets through the Metis UI. Simply navigate to `Resources → Instance Secret `to check the status of any Instance Secret within the environment. Additionally, users can quickly find a specific Instance Secret by searching for its name in the Metis UI search bar.

<center>
<img src="/resources/instance_secret/metis_is.png" alt="Bifrost Governance" style="width:55rem; border: 1px solid black; padding: 5px;" />
<figcaption><i>Metis UI</i></figcaption>
</center>


### **How to monitor the status using DataOS CLI?**

Users can check whether an Instance Secret is active or deleted by running the command `dataos-ctl resource get -t instance-secret -n ${{instance-secret-name}}` in the DataOS CLI. The output will appear as follows:

```bash
dataos-ctl resource get -t instance-secret -n metalh-r
INFO[0000] 🔍 get...                                     
INFO[0000] 🔍 get...complete                             

    NAME   | VERSION |      TYPE       | WORKSPACE | STATUS | RUNTIME |     OWNER       
-----------|---------|-----------------|-----------|--------|---------|-----------------
  metalh-r | v1      | instance-secret |           | active |         | dataos-manager 
```

### **How to get notified whenever the status of an Instance Secret changes?**

Users can configure a Monitor Resource to define the conditions for triggering an alert. They can then set up a Pager Resource to specify the alert path and the text schema format in which the alert will be delivered. The alert path can be a webhook URL, email ID, or any other designated endpoint.

This section outlines the steps to create a Monitor Resource that triggers an incident when the state of an Instance Secret changes from active to deleted. Make sure you have the permission to create a Monitor Resource.

**Step 1: Create a manifest file for Monitor Resource**

Begin by creating a manifest file that contains the configurations of the Monitor as shown below in template. Replace the Instance Secret name with your actual Instance Secret.

```yaml
# Resource meta section
name: runtime-monitor
version: v1alpha
type: monitor
tags:
  - dataos:type:resource
  - dataos:layer:user
description: Attention! instance secret is deleted
layer: user
monitor:

# Monitor-specific section
  schedule: '*/2 * * * *'
  incident:
    name: instancesecret
    severity: high
    incidentType: instancesecret
    
  type: report_monitor
# Report Monitor specification
  report:
    source:
      dataOsInstance:
         path: /collated/api/v1/reports/resources/status?id=instance-secret:v1:modern-docker-secret
    conditions:
      - valueComparison:
          observationType: state
          valueJqFilter: '.value'
          operator: equals
          value: deleted
```

**Step 2: Validate the  DataOS instance API path**

Before applying the Monitor Resource file, it is recommended to check the response of the API endpoint.

**Step 3: Apply the Monitor manifest file**

After validating the API endpoint, the next step is to apply the Monitor manifest file by executing the code below.

```bash
dataos-ctl resource apply -f ${{path-of-your-manifest-file}}
```

**step 4: Validate the Monitor**

Validate or check the runtime of the Monitor by executing the below command.

=== "Command"

    ```bash 
    dataos-ctl get runtime -t monitor -w public -n runtime-monitor1 -r 
    ```
=== "Expected output"

    ```bash 
    dataos-ctl get runtime -t monitor -w public -n runtime-monitor1 -r         
    INFO[0000] 🔍 monitor...                                 
    INFO[0000] 🔍 monitor...complete                         

            NAME       | VERSION |  TYPE   | WORKSPACE |    OWNER     
    -------------------|---------|---------|-----------|--------------
      runtime-monitor1 | v1alpha | monitor | public    | iamgroot  

            NAME       | VERSION |  TYPE   | WORKSPACE |    OWNER     
    -------------------|---------|---------|-----------|--------------
      runtime-monitor1 | v1alpha | monitor | public    | iamgroot  


      STATUS |            RUNTIME              
    ---------|---------------------------------
      active | next:2025-01-28T18:38:00+05:30  


        RUN ID    |          STARTED          |         FINISHED          | RUN STATUS |                                                                     RESULT                                                                      
    ---------------|---------------------------|---------------------------|------------|-------------------------------------------------------------------------------------------------------------------------------------------------
      ebctzh4krmro | 2025-01-28T18:30:00+05:30 | 2025-01-28T18:30:00+05:30 | completed  | 🟧 monitor condition not met for monitor: 'runtime_monitor1_public'  
    ---------------|---------------------------|---------------------------|------------|----------------------------------------------------------------------
      ebctt1wkmsxv | 2025-01-28T18:28:00+05:30 | 2025-01-28T18:28:00+05:30 | completed  | 🟧 monitor condition not met for monitor: 'runtime_monitor1_public'  
    ---------------|---------------------------|---------------------------|------------|----------------------------------------------------------------------
      ebctmmokhz42 | 2025-01-28T18:26:00+05:30 | 2025-01-28T18:26:00+05:30 | completed  | 🟧 monitor condition not met for monitor: 'runtime_monitor1_public'  
    ---------------|---------------------------|---------------------------|------------|----------------------------------------------------------------------
      ebcuiqs8omis | 2025-01-28T18:36:00+05:30 | 2025-01-28T18:36:00+05:30 | completed  | 🟩 monitor condition met for monitor: 'runtime_monitor1_public', 'instance-secret:v1:modern-docker-secret', created incident id 'ebcuird1u680'  
    ---------------|---------------------------|---------------------------|------------|-------------------------------------------------------------------------------------------------------------------------------------------------

    ```


Now whenever the Monitor condition is met, it will trigger an incident.

### **How to create a Pager Resource to get notified whenever an Instance Secret gets deleted?**

Through Monitor whenever the condition is met it will trigger an incident, we will use that incident to get notified on the desired platform such as Microsoft Teams, Outlook, etc. by creating a Pager Resource. This section involves the steps to create a Pager Resource.

**Step 1: Create a manifest file for Pager**

Begin by creating a manifest file that contains the configurations of Pager as shown below in template. Replace the given values with your actual values and edit the notification template as required.

```yaml

name: instancesecrpager
version: v1alpha
type: pager
tags:
  - dataos:type:resource
  - workflow-failed-pager
description: This is for sending Alerts on Microsoft Teams Channel.
workspace: public
pager:
  conditions:
    - valueJqFilter: .properties.name
      operator: equals
      value: instancesecret

  output:
    webHook:
      url: https://rubikdatasolutions.webhook.office.com/webhookb2/e6b48e18-bdb1-4ffc-98d5-cf4a3890lkh4@2e22bdde-3ec2-43f5-bf92-78e9f35a44fb/IncomingWebhook/d23792bec444445gg8bb7193145dfae985/631bd149-c89d-4d3b-8979-8e364f62b419/V2ZJfUrl5d8I5xPhM80JyeE9LqKHU53gPsJQX9H8I2fOs1
      verb: post
      headers:
        'content-type': 'application/json'
      bodyTemplate: |
          {
            "@type": "MessageCard",
            "summary": "Instance Secret is deleted",
            "themeColor": "0076D7",
            "sections": [
              {
                "activityTitle": "Dear Team,",
                "activitySubtitle": "Instance Secret is deleted",
                "activityImage": "https://adaptivecards.io/content/cats/3.png",
                "facts": [
                  {
                    "name": "Following Instance Secret is deleted",
                    "value": "{{ index (splitn ":" 4 .ReportContext.ResourceId) "_2" }}"
                  },
                  {
                    "name": "Failure Time:",
                    "value": "{{ .CreateTime }}"
                  },
                  {
                    "name": "Severity:",
                    "value": "{{ .Properties.severity }}"
                  },
                  {
                    "name": "Run Details:",
                    "value": "<a href=\"https://${dataos-fqdn}/operations/user-space/resources/resource-runtime?name={{ index (splitn ":" 4 .ReportContext.ResourceId) "_2" }}&type=workflow&workspace=public\">Operation</a>"
                  },
                  {
                    "name": "Logs:",
                    "value": "<a href=\"https://${dataos-fqdn}/metis/resources/workflow/dataos.public.{{ index (splitn ":" 4 .ReportContext.ResourceId) "_2" }}/run_history\">Metis</a>"
                  }
                ]
              },
              {
                "title": "Disclaimer",
                "text": "{{ .Monitor.Description }}"
              }
            ]
          }
```

**Step 2: Apply the manifest file of the Pager Resource**

After validating the API endpoint, the next step is to apply the Monitor manifest file by executing the code below.

```bash
dataos-ctl resource apply -f ${{path-of-your-manifest-file}}
```

**Step 3:** **Get Notification!**

You will get a notification on the team's channel whenever the conditions of the incident are met.

<center>
<img src="/resources/instance_secret/pager_noti.png" alt="Bifrost Governance" style="width:60rem; border: 1px solid black; padding: 5px;" />
<figcaption><i>Pager Notification</i></figcaption>
</center>

## Operational monitoring

Using the Operations App, users can monitor the operational logs of an Instance Secret. In addition to tracking its status, they can also view details such as the builder stage, Cloud Kernel Resource Count, WebService Resource Count, and, if applicable, the Operator Runtime Resource Count.

<center>
<img src="/resources/instance_secret/pager_noti.png" alt="Bifrost Governance" style="width:60rem; border: 1px solid black; padding: 5px;" />
<figcaption><i>Operations App</i></figcaption>
</center>