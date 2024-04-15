# Utilizing Equation Monitor with a Postgres Data Source

The Equation Monitor's integration with Postgres avoids unnecessary load on the Minerva cluster, enhancing performance and response time for critical metric changes This direct connection not only simplifies the architecture but also significantly boosts performance for monitoring changes in Lens2.0 metrics. 

## Configuring the monitor 

To leverage this improved setup, you can create an Equation Monitor manifest configured to query a Postgres database directly. This sample configuration demonstrates how to set up the Equation Monitor for evaluating conditions between two data sets within a Postgres database.

```yaml
name: db-comparison
version: v1alpha
type: monitor
monitor:
  schedule: '*/5 * * * *'
  type: equation_monitor
  equation:
    leftExpression:
      queryCoefficient: 1
      queryConstant: 0
      query:
        type: postgres
        ql: 'SELECT COUNT(*) FROM changes'
        dsn: 'postgres://USER:PASS@HOSTNAME:5432/DB?sslmode=require'
    rightExpression:
      queryCoefficient: 1
      queryConstant: 0
      query:
        type: postgres
        ql: 'SELECT COUNT(*) FROM collections'
        dsn: 'postgres://USER:PASS@HOSTNAME:5432/DB?sslmode=require'
    operator: greater_than_equals
  incident:
    type: pulsar
    name: monitor-incident
    category: equation
    severity: info
```
