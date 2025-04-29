# Caching

Caching puts a copy of intermediately transformed dataset into memory, allowing us to repeatedly access it at a much lower cost than running the entire pipeline again.

## Syntax

Provide the following syntax in the `sql` attribute of the `sequence` attribute.

```sql
CACHE TABLE <TABLE_NAME>
```
Replace `<TABLE_NAME>` placeholder with table name you wish to cache.

## Flare workflow manifest for caching the Iceberg table

```yaml hl_lines hl_lines= "46-47", "66-67"
version: v1
name: resource-usage-read-pulsar
type: workflow
description: "Read pod usage from pulsar and write it to iceberg with resource level partition"
workflow:
  dag:
    - name: resource-level-pod-usage
      spec:
        stack: flare:6.0
        compute: runnable-default
        stackSpec:
          job:
            explain: true
            showPreviewLines: 100
            inputs:
              - name: input
                dataset: dataos://lakehouse:event_data/pod_usage
                isStream: false
            logLevel: INFO
            steps:
              - sequence:
                  - name: limited_data
                    sql: SELECT __eventTime as event_timestamp,
                      CAST(__eventTime AS DATE) AS event_date, input.*
                      FROM input WHERE namespace NOT IN ('superset', 'heimdall', 'caretaker', 'juicefs-system',
                      'network-gateway', 'calico-system', 'argo', 'core-apps', 'sentinel', 'cloudnativepg',
                      'user-system', 'system', 'default')
                    functions:
                      - name: generate_uuid
                        asColumn: uid


                  - name: cached_limited_data
                    sql: CACHE TABLE limited_data


                  - name: final_data
                    sql: select co.uid, co.pod_name,
                      co.namespace, co.node, co.phase,
                      co.event_timestamp, co.event_date,
                      co.container_name, co.container_cpu_request, co.container_cpu_limit, co.container_cpu_usage,
                      co.container_memory_request, co.container_memory_limit, co.container_memory_usage,
                      co.init_container_name, co.init_container_cpu_request, co.init_container_cpu_limit,
                      co.init_container_cpu_usage, co.init_container_memory_request,
                      co.init_container_memory_limit, co.init_container_memory_usage,
                      CONCAT_WS(':', pv.resource_type, pv.version, pv.resource_name, pv.namespace) AS resource_id,
                      pv.resource_name, pv.owner, pv.version, pv.workspace, pv.runId, pv.stack, pv.resource_type,
                      pv.app_role, pv.dataplane, co.labels
                      from merged_container_with_init as co JOIN pivot_data as pv on co.uid = pv.uid
                      where pv.resource_type IS NOT NULL ORDER BY co.event_date, pv.resource_type, co.namespace

                  - name: cache_final_data
                    sql: CACHE TABLE final_data

            outputs:
              - name: final_data
                dataset: dataos://icebase:pod_usage/resource_usage?acl=rw
                format: Iceberg
                options:
                  saveMode: append
```

