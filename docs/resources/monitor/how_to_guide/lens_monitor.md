# Equation Monitor to observe Lens metrics

Equation Monitor can observe the Lens metrics to generate the incidents when the condition met.

**Configuring Equation Monitor**

This sample configuration demonstrates how to set up the Equation Monitor for observing the Lens. An incident will be generated if the calculated value of the left expression is less than the calculated value of the right expression.
```yaml
name: monitor-lens-metric
version: v1alpha
type: monitor
runAsUser: iamgroot
monitor:
  schedule: '*/2 * * * *'
  type: equation_monitor
  equation:
    leftExpression:
      queryCoefficient: 1
      queryConstant: 0
      query:
        type: lens
        lens:
          dataOsInstance:
            name: sales-ops
            workspace: public
            sslmode: 'disable'
        ql: SELECT deal_momentum, deal_name FROM deal_momemtum_analysis where deal_momentum is not null and deal_momentum != 0
        comparisonColumn: {
            name: deal_momentum,
            dataType: int64
        }
    rightExpression:
      queryCoefficient: 0
      queryConstant: 50
      query:
    operator: less_than_equals
  incident:
    type: business-metric
    name: low-deal-momentum
    category: equation
    severity: info
```
To know more about the specific attributes, [refer to this](/resources/monitor/configurations/).