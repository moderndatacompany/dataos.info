# How to restart and scale the Cluster on a pre-defined schedule?

Cluster maintenance is essential for ensuring optimal performance and reliability in your infrastructure. The `maintenance` section in the Cluster manifest file enables you to automate cluster scaling and restart on a pre-defined schedule. This guide will walk you through setting up `restartCron` and `scalingCrons` for efficient cluster management.

<aside class="callout">
🗣 The <code>maintenance</code> section allows you to upscale, downscale, or restart a Cluster based on a predefined cron schedule. Conditions can only be implemented based on time, and not on other parameters like memory or CPU utilization.

</aside>

## Restarting a Cluster on a pre-defined schedule

The `restartCron` attribute defines a cron schedule for restarting the cluster. Poros, the DataOS orchestrator will restart the Cluster based on the specified schedule, defined using a corn expression. This capability is helpful in resource or memory reclamation, as over time clusters may accumulate unused or inefficiently managed resources or memory. A periodic restart helps reclaim these resources or memory, preventing resource wastage and optimizing resource utilization. 

**Syntax**

```yaml
cluster:
  maintenance:
    restartCron: '13 1 */2 * *'
    timezone: Asia/Kolkata
```

In the above syntax:

- `restartCron`: This specifies that the cluster will restart every other day at 1:13 AM.
- `timezone`: Defines the timezone for the cron schedule. By default, it’s UTC and could be any valid timezone from the [tz database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)

### **Using `restartCron`**

Let’s understand how to utilize the `restartCron` attribute to restart a Cluster, using an example:

Assume that every day at 12:20 AM in the Asia/Kolkata timezone, you want to restart the Cluster. You can configure the manifest file of a Cluster in the following way to accomplish that:

```yaml
name: restartcroncluster
version: v1
type: cluster
description: The cluster restarts at a predefined cron schedule
tags:
  - cluster
  - minerva
  - restart
cluster:
  compute: query-default
  maintenance:
    restartCron: '20 12 * * *'
    timezone: Asia/Kolkata
  minerva:
    replicas: 1
    resources:
      limits:
        cpu: 2000m
        memory: 2Gi
      requests:
        cpu: 3000m
        memory: 3Gi
    debug:
      logLevel: INFO
      trinoLogLevel: ERROR
    depots:
      - address: dataos://bigquerycluster
```

Adjust the `restartCron` attribute according to your desired schedule and timezone.

## Scale Cluster on Predefined Schedules

`scalingCrons` enable you to adjust the cluster's capacity based on predefined schedules. Poros can horizontally and/or vertically scale the Cluster based on the provided configuration. This is particularly useful for optimizing resource allocation during peak and off-peak hours.

<aside class="callout">
🗣 A <code>scalingCron</code> overrides the default <code>replicas</code> and/or <code>resources</code> in a cluster manifest while in an "active" cron window. When a cron schedule is triggered, the supplied replicas and resources are put into effect until another cron schedule occurs. To clear an active scalingCron, clear out the <code>scalingCrons</code> section, update the cluster, or apply it again.

</aside>

**Syntax**

```yaml
scalingCrons:
  - cron: '5/10 * * * *' 
    timezone: Europe/Berlin
    replicas: 2
    resources:
      requests:
        cpu: 800m
        memory: 1Gi
      limits:
        cpu: 1000m
        memory: 2Gi
```

Each entry in `scalingCrons` defines a specific cron schedule and scaling parameters such as replicas, CPU, and memory. In the above example:

- `cron`: Specifies the cron schedule for scaling operations.
- `timezone`: Defines the timezone for the cron schedule. By default, it is UTC and could be any valid timezone from the TZ [database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
- `replicas`: Indicates the desired number of replicas for the cluster. By default, it's 1.
- `resources`: Specifies resource requests and limits for CPU and memory.
- `requests`: specifies the resource limits for CPU and memory for the specific Cluster.
- `limits`:
- `cpu`: specifies cpu units in milliCPU(m) or CPU Core. By default, requests: 100m, limits: 400m.
- `memory`: specifies memory in Mebibytes(Mi) or Gibibytes(Gi). By default, requests: 100Mi, limits: 400Mi.

### **Horizontal Scaling**

To scale the Cluster horizontally every 5 minutes, specify.

```yaml
cluster:
  maintenance:
    scalingCrons:
    - cron: '5/10 * * * *'
      timezone: Europe/Berlin
      replicas: 3
    - cron: '10/10 * * * *'
      timezone: Europe/Berlin
      replicas: 0
```

### **Vertical Scaling**

To scale the Cluster vertically every 5 minutes, specify the following attributes/fields.

```yaml
cluster:
  maintenance:
    scalingCrons:
    - cron: '5/10 * * * *'
      timezone: Europe/Berlin
      resources:
        limits:
          cpu: 1000m
          memory: 2Gi
        requests:
          cpu: 800m
          memory: 1Gi
    - cron: '10/10 * * * *'
      timezone: Europe/Berlin
      resources:
        limits:
          cpu: 3000m
          memory: 7Gi
        requests:
          cpu: 1500m
          memory: 3Gi
```

### **Usage Example**

Let's illustrate how to utilize `scalingCrons` effectively:

- **Peak Hours (e.g., 8 AM to 10 AM, Monday to Friday):**
    - Increase replicas to 7.
    - Set CPU to 15,000m and memory to 6Gi.
- **Off-Peak Hours (e.g., 12 PM to 4 PM, Monday to Friday):**
    - Decrease replicas to 4.
    - Reduce CPU to 5,000m and memory to 4Gi.

**Manifest file**

```yaml
name: restartcroncluster
version: v1
type: cluster
description: the cluster restarts at a pre-defined cron schedule
tags:
  - cluster
  - minerva
  - restart
cluster:
	compute: query-default
	maintenance: 
      scalingCrons:
        - corn: '0 8-10 * * MON-FRI'
          replicas: 7
          resources:
            limits:
              cpu: 3000m
              memory: 3Gi
            requests:
              cpu: 15000m
              memory: 6Gi
        - corn: '0 12-16 * * MON-FRI'
          replicas: 4
          resources:
            limits:
              cpu: 3000m
              memory: 3Gi
            requests:
              cpu: 5000m
              memory: 4Gi
	minerva:
      replicas: 1
      resources:
        limits:
          cpu: 2000m
          memory: 2Gi
        requests: 
          cpu: 3000m
          memory: 3Gi
    debug: 
      logLevel: INFO
      trinoLogLevel: ERROR
    depots:
      - address: dataos://bigquery
```