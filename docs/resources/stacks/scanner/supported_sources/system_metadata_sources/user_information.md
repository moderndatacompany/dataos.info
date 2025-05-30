# Scanner for User Information 

Heimdall, in DataOS, is the security engine managing user access. It ensures only authorized users can access DataOS Resources. This Scanner Workflow connects with Heimdall to scan and retrieve information about users in the DataOS environment, including their descriptions and profile images and stores it in Metis DB.

This Scanner Workflow will scan the information about the users in DataOS. This is a scheduled Workflow that connects with Heimdall on a given cadence to fetch information about users as shown below: 

```yaml
name: heimdall-users-sync
version: v1
type: workflow
tags: 
  - users
  - scanner
description: Heimdall users sync workflow
owner: metis
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
        runAsApiKey: 
	        ${{"API-KEY"}}
```

On a successful run, user can view the users information on Metis UI. The above sample manifest file is deployed using the following command:

```bash
dataos-ctl resource apply -f ${{path to the Scanner YAML}}
```

**Updating the Scanner Workflow**:

If the Depot or Scanner configurations are updated, the Scanner must be redeployed after deleting the previous instance. Use the following command to delete the existing Scanner:

```bash 
  dataos-ctl delete -f ${{path-to-Scanner-YAML}}]
```

**OR**

```bash
  dataos-ctl delete -t workflow -n ${{name of Scanner}} -w ${{name of workspace}}
```


!!! info "**Best Practice**"

    As part of best practices, it is recommended to regularly delete Resources that are no longer in use. This practice offers several benefits, including saving time and reducing costs.