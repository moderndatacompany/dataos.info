# How to build a Data Product?

Data Product is build by the Data Product Developers. This section involves the building phase of the Data Product right from data connection to defining SLOs. DataOS provides flexible ways to build the Data Product. You can create the Data Product from scratch or reuse the existing one as per requirements. You can explore the Data Products in the [Data Product Hub](/interfaces/data_product_hub/), an interface that lists all the existing Data Product information.

Let’s see the steps for building a Data Product:

## Pre-requisites

Before proceeding with the Data Product creation, ensure that you have the necessary tags or use cases to be assigned. To know more about use cases, go to [Bifrost](https://dataos.info/interfaces/bifrost/).

<aside class="callout">
🗣 To acquire the necessary tags and use cases, please contact your organization's DataOS Operator.

</aside>

## Steps to Create a Data Product

From the design phase, it is clear which DataOS resources we require to build the Data Product, and these are [Instance Secret](/resources/instance_secret/), [Depot](/resources/depot/), [Cluster](/resources/cluster/), [Scanner](/resources/stack/), [Flare](/resources/stack/), [Policy](/resources/policy/), [SODA Checks](/resources/stack/), [Monitor](/resources/monitor/), [Pager](/resources/pager/), and [Bundle](/resources/bundle/). Let’s see how to create each one step by step. As we already created the Depot and ran the Depot scanner, we’ll directly jump into the data transformation step using Flare.

<aside class="callout">
🗣 Depending upon the use case more resources can be added or removed, to know more about the DataOS resources refer to <a href="https://dataos.info/resources/">DataOS Resources</a>.
</aside>


### **Create the Flare Job for data transformation**

[Flare](/resources/stack/) is a stack orchestrated by the [Workflow](/resources/workflow/) that abstracts Apache Spark for large-scale data processing, including ingestion, transformation, enrichment, profiling, quality assessment, and syndication for both batch and streaming data.

Let’s see how you can utilize Flare for various transformations, we are taking the same example of Google Analytics here, to ingest raw data as is from S3, with the only transformation being the conversion of the date column to date_time since it's initially in varchar format.

The code snippet below demonstrates a Workflow involving a single Flare batch job that reads the input dataset from the S3 depot, performs transformation using Flare Stack, and stores the output dataset in the Icebase Depot. 

```yaml
version: v1
name: wf-ga-sessions-daily-raw
type: workflow
tags:
  - GA-Sessions-Daily-Data-Raw
description: This job ingests Google Analytics Sessions Daily Data from S3 bucket to DataOS. This workflow will run everyday and will keep appending the raw google analytics data on a daily basis
workflow:
  title: GA Sessions Daily Data Raw
  dag:
    - name: dg-ga-sessions-daily-raw
      title: GA Sessions Daily Data Raw
      description: This job ingests GA Sessions Daily Data from S3 bucket to DataOS
      spec:
        tags:
          - GA-Sessions-Daily-Data-Raw
        stack: flare:5.0
        compute: runnable-default
        stackSpec:
          driver:
            coreLimit: 6000m
            cores: 2
            memory: 8000m
          executor:
            coreLimit: 6000m
            cores: 3
            instances: 2
            memory: 10000m
          job:
            explain: true
            streaming:
              forEachBatchMode: true
              triggerMode: Once
              checkpointLocation: dataos://icebase:sys01/checkpoints/ga-sessions-daily-data-raw/ga-1001?acl=rw
            inputs:
              - name: ga_sessions_daily_data
                dataset: dataos://s3depot:none/ga_data/
                format: parquet
                isStream: true
            logLevel: INFO
            outputs:
              - name: ga_sessions_daily_data_raw_v
                dataset: dataos://icebase:google_analytics/ga_sessions_daily_data_raw?acl=rw
                format: Iceberg
                title: GA Sessions Daily Data
                description: Ingests GA Sessions Data daily
                options:
                  saveMode: append
                  sort:
                    mode: partition
                    columns:
                      - name: date_time
                        order: asc
                  iceberg:
                    properties:
                      write.format.default: parquet
                      write.metadata.compression-codec: gzip
                    partitionSpec:
                      - type: day
                        column: date_time
                        name: day
            steps:
              - sequence:
                  - name: ga_sessions_daily_data_raw_v
                    sql: >
                      select *, cast(to_date(date, 'yyyyMMdd') as timestamp) as date_time
                      FROM ga_sessions_daily_data

          sparkConfig:
            - spark.sql.files.maxPartitionBytes: 10MB
            - spark.sql.shuffle.partitions: 400
            - spark.default.parallelism: 400
            - spark.dynamicAllocation.enabled: true
            - spark.sql.adaptive.enabled: true
            - spark.dynamicAllocation.executorIdleTimeout: 60s
            - spark.dynamicAllocation.initialExecutors: 1
            - spark.dynamicAllocation.minExecutors: 2
            - spark.dynamicAllocation.maxExecutors: 5
            - spark.dynamicAllocation.shuffleTracking.enabled: true
    - name: dt-ga-sessions-daily-raw
      spec:
        stack: toolbox
        compute: runnable-default
        stackSpec:
          dataset: dataos://icebase:google_analytics/ga_sessions_daily_data_raw?acl=rw
          action:
            name: set_version
            value: latest
      dependencies:
        - dg-ga-sessions-daily-raw
```

Note that the above provided manifest file is just an example of how you can create a Flare job. To know more about the Flare, [refer to this](https://dataos.info/resources/stacks/flare/). 

### **Create the Monitor for observability**

The [Monitor Resource](/resources/monitor/) in DataOS's Observability System triggers incidents based on events or metrics alongside the [Pager](/resources/pager/) Resource, enabling comprehensive observability and proactive incident management for high system reliability and performance.

Let’s see how you can set up the Monitor for Workflow status.

Create a manifest file for the Monitor as follows:

```yaml
name: runtime-monitor
version: v1alpha
type: monitor
tags:
  - dataos:type:resource
  - dataos:layer:user
description: Attention! workflow run has failed.
layer: user
monitor:
  schedule: '*/10 * * * *'
  incident:
    name: workflowrunning
    severity: high
    incidentType: workflowruntime
    
  type: report_monitor
  report:
    source:
      dataOsInstance:
         path: /collated/api/v1/reports/resources/status?id=workflow:v1:wf-ga-sessions-daily-raw:public
    conditions:
      - valueComparison:
          observationType: status
          valueJqFilter: '.value'
          operator: equals
          value: failed
```

The above sample configuration demonstrates how to set up the Equation Monitor to raise the incident whenever the Workflow fails.

To know more about Monitor, [refer to this](https://dataos.info/resources/monitor/).

### **Create the Pager for managing incidents**

A Pager in DataOS evaluates incident data against predefined conditions, triggering alerts to specified destinations upon identifying a match, forming the backbone of DataOS Observability, and enabling proactive alerting with the Monitor Resource.

Let’s see how you can set up a Pager to get an alert on MS Teams and Email on the incident raised by the Monitor whenever the Workflow fails.

To create a Pager in DataOS, simply compose a manifest file for a Pager as shown below:

```yaml
name: wf-failed-pager
version: v1alpha
type: pager
tags:
  - dataos:type:resource
  - workflow-failed-pager
description: This is for sending Alerts on the Microsoft Teams Channel and Outlook.
workspace: public
pager:
  conditions:
    - valueJqFilter: .properties.name
      operator: equals
      value: workflowrunning

  output:
    email:
      emailTargets:
        - iam.groot@tmdc.io
        - thisis.loki@tmdc.io

    msTeams:
      webHookUrl: https://rubikdatasolutions.webhook.com/webhookb2/e6b48e18-bdb1-4ffc-98d5-cf4a3819fdb4@2e22bdde-3ec2-43f5-bf92-78e9f35a44fb/IncomingWebhook/20413c453ac149db9

```

The above configurations demonstrate, how to create a Pager for MS Team and Outlook notifications.

To know more about Pager, [refer to this](https://dataos.info/resources/pager/).

### **Create the Bundle for applying all the resources**

With the help of Bundle, users can perform the deployment and management of multiple Resources in a single operation, organized as a flattened DAG with interconnected dependency nodes.

Let’s see, how you can create the Bundle resource to apply all the resources based on their dependencies. To create a Bundle in DataOS, simply compose a manifest file for a Bundle as shown below:

```yaml
# Resource meta section
name: dp-bundle
version: v1beta
type: bundle
layer: user 
tags: 
  - dataos:type:resource
description: this bundle resource is for a data product

# Bundle-specific section
bundle:

  # Bundle Workspaces section
  workspaces:
    - name: bundlespace1 # Workspace name (mandatory)
      description: this is a bundle workspace # Workspace description (optional)
      tags: # Workspace tags (optional)
        - bundle
        - myworkspace
      labels: # Workspace labels (optional)
        purpose: testing
      layer: user # Workspace layer (mandatory)

  # Bundle Resources section
  resources:
    - id: flare-job
      file: /home/office/data_products/flare.yaml

    - id: policy
      file: /home/office/data_products/policy.yaml
      dependencies:
        - flare-job
      
    - id: soda checks
      file: /home/office/data_products/checks.yaml
      dependencies:
        - flare-job    
        
    - id: monitor
      file: /home/office/data_products/monitor.yaml
      dependencies:
        - flare-job

    - id: pager
      file: /home/office/data_products/pager.yaml
      dependencies:
        - flare-job
                    
  # Manage As User
  manageAsUser: iamgroot
```

replace the placeholder with the actual values and apply it using the following command on the DataOS [Command Line Interface (CLI)](https://dataos.info/interfaces/cli/).

```bash
dataos-ctl apply -f ${{yamlfilepath}}
```

After executing the above command, all the resources will be applied per the dependencies.

To learn more about the Bundle, [refer to this](https://dataos.info/resources/bundle/).


### **Create a Policy to secure the data**

The Policy Resource in DataOS enforces a "never trust, always verify" ethos with ABAC, dynamically evaluating and granting access permissions only if explicitly requested and authorized at each action attempt.

Let’s see how you can create a Data Policy for data masking:

```yaml
name: email-masking-policy
version: v1
type: policy
tags:
  - dataos:type:resource
description: data policy to mask user's email ID
owner: iamgroot
layer: user
policy:
  data:
    dataset: ga_sessions_daily_data_raw
    collection: google_analytics
    depot: icebase
    priority: 40
    type: mask
    mask:
      operator: hash
      hash:
        algo: sha256
    selector:
      column:
        tags:
          - PII.Email
      user:
        match: any
        tags:
          - roles:id:user
```

The above manifest file illustrates data masking for masking the email ID of users having tag `roles:id:user`. Apply the following command on the DataOS [Command Line Interface (CLI)](/interfaces/cli/).

```bash
dataos-ctl apply -f ${{yamlfilepath}}
```

After executing the above command, the Policy will be applied.

To know more about Policy, [refer to this](https://dataos.info/resources/policy/).

Now the Data Product is ready. You can explore the Data Product on [Data Product Hub](/interfaces/data_product_hub).