# Scanner for Users Info
Heimdall, in DataOS, is the security engine managing user access. It ensures only authorized users can access DataOS resources. This Scanner workflow connects with Heimdall to To scan and retrieve information about users in the DataOS environment, including their descriptions and profile images and stores it in Metis DB. 

## Scanner Workflow YAML 

The given YAML will scan the user-related information from Heimdall.

### **YAML Configuration**

```yaml
name: heimdall-users-sync
version: v1
type: workflow
tags:
  - users
  - scanner
description: Heimdall users sync workflow
owner: metis
workspace: system
workflow:
  title: Heimdall Users Sync
  schedule:
    cron: '*/10 * * * *'
    timezone: UTC
    concurrencyPolicy: Forbid
  dag:
    - name: users-sync
      description: The job scans and publishes all users heimdall to metis.
      spec:
        stack: scanner:2.0
        stackSpec:
          type: users
        logLevel: INFO
        compute: runnable-default
        runAsUser: metis
        resources:
          requests:
            cpu: 250m
            memory: 512Mi
          limits:
            cpu: 1100m
            memory: 2048Mi
        runAsApiKey: >-
          ****************************************************************************
```
## Metadata on Metis UI

On a successful run, you can view the users information on Metis UI.