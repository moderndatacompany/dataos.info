# Cluster Maintenance

> Available in DataOS CLI Version 2.8.2 and DataOS Version 1.10.41
> 

A `maintenance` section has been added to the Cluster resource type. This section provides a set of features to assist with various operator activities that need to be simplified and automated by Poros. The maintenance features are invoked on a corn schedule which triggers a restart or a scale that is very specific to the cluster in purview.

### `restartCron`

By providing a cron string in this field, Poros will restart the cluster on this schedule.

**Sample**

Will restart at 1:13am every other day.

```yaml
cluster:
  maintenance:
    restartCron: '13 1 */2 * *'
```

### `scalingCrons`

By providing a list of `cron`, `replicas`, and/or `resources`, Poros will scale horizontally and/or vertically according to the provided schedules.

A `scalingCron` overrides the default provided `replicas` and/or `resources` in a cluster like Minerva while in an "active" cron window. 

When a cron schedule is triggered, the supplied replicas and resources are put into effect until another cron schedule occurs. To clear an active scalingCron, clear out the `scalingCrons` section and apply the resource again.

**Examples**

Will scale horizontally every 5 minutes.

```yaml
# Horizontal Scaling
cluster:
  maintenance:
    scalingCrons:
    - cron: '5/10 * * * *'
      replicas: 3
    - cron: '10/10 * * * *'
      replicas: 0
```

Will scale vertically every 5 minutes

```yaml
# Vertical Scaling
cluster:
  maintenance:
    scalingCrons:
    - cron: '5/10 * * * *'
      resources:
        limits:
          cpu: 1000m
          memory: 2Gi
        requests:
          cpu: 800m
          memory: 1Gi
    - cron: '10/10 * * * *'
      resources:
        limits:
          cpu: 3000m
          memory: 7Gi
        requests:
          cpu: 1500m
          memory: 3Gi
```