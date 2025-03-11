# How to add context column to the Monitors?

Monitor provides the capability to use SQL in the monitor query to return multiple columns, allowing for greater flexibility in monitoring and incident management. Among these columns, one can be designated as the "comparison column," which serves the specific purpose of triggering incidents when a predefined threshold is met. The other columns, known as "context columns," are used to provide additional context to the results, enhancing the understanding and analysis of the data when an incident is triggered. This setup enables users to customize their monitoring and incident response strategies effectively. Below is the manifest file of the Equation Monitor with the context column.

```yaml
name: longer-avg-query-system-minerva
version: v1alpha
type: monitor
description: checks if queries are longer than average
monitor:
  schedule: '*/2 * * * *'
  type: equation_monitor
  equation:
    leftExpression:
      queryCoefficient: 1
      queryConstant: 0
      query:
        type: trino
        cluster: system
        ql: | 
          SELECT query_id, date_diff('millisecond', created, last_heartbeat) AS exec_time, user 
          FROM "system"."runtime".queries 
          WHERE state = 'FINISHED' 
          ORDER BY 'end' desc 
          LIMIT 100
        comparisonColumn:
          name: exec_time
          dataType: float64
    rightExpression:
      queryCoefficient: 1.75
      queryConstant: 0
      query:
        type: trino
        cluster: system
        ql: SELECT avg(date_diff('millisecond', created, last_heartbeat)) AS avg_exec_time FROM "system"."runtime".queries WHERE state = 'FINISHED'
    operator: greater_than
  incident:
    type: query-exec-time-exceeded
    name: longer-avg-query-system-minerva
    category: equation
    severity: warning
```
The above Equation Monitor will generate the following incident:

```json
{
  "id": "djw4bftzve2o",
  "createTime": "2024-04-26T10:52:00.612351887Z",
  "properties": {
    "category": "equation",
    "name": "longer-avg-query-system-minerva",
    "severity": "warning",
    "type": "query-exec-time-exceeded"
  },
  "equationContext": {
    "queryExpressions": [
      {
        "leftExpressionValue": "69763.00",
        "rightExpressionValue": "4547.20",
        "leftRow": {
          "comparisonColumn": {
            "name": "exec_time",
            "value": "69763.00"
          },
          "contextColumns": [
            {
              "name": "query_id",
              "value": "20240426_103616_03485_ryzfm"
            },
            {
              "name": "user",
              "value": "iamgroot"
            }
          ]
        },
        "rightRow": {
          "comparisonColumn": {
            "name": "avg_exec_time",
            "value": "2598.40"
          }
        }
      }
    ]
  },
  "monitor": {
    "id": "longer_avg_query_system_minerva_public",
    "name": "longer-avg-query-system-minerva",
    "description": "checks if queries are longer than average",
    "schedule": "*/2 * * * *",
    "timezone": "UTC",
    "type": "equation_monitor",
    "equationMonitor": {
      "leftExpression": {
        "queryCoefficient": 1,
        "queryConstant": 0,
        "query": {
          "type": "trino",
          "cluster": "system",
          "ql": "SELECT query_id, date_diff('millisecond', created, last_heartbeat) AS exec_time, user \nFROM \"system\".\"runtime\".queries \nWHERE state = 'FINISHED' \nORDER BY 'end' desc \nLIMIT 100\n",
          "comparisonColumn": {
            "name": "exec_time",
            "dataType": "float64"
          }
        }
      },
      "rightExpression": {
        "queryCoefficient": 1.75,
        "queryConstant": 0,
        "query": {
          "type": "trino",
          "cluster": "system",
          "ql": "SELECT avg(date_diff('millisecond', created, last_heartbeat)) AS avg_exec_time FROM \"system\".\"runtime\".queries WHERE state = 'FINISHED'"
        }
      },
      "operator": "greater_than"
    }
  }
}
```