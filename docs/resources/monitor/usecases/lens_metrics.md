# Get alerts when Lens metrics decreased

This guide explains how to set up a Monitor and Pager resources to alert you when a Lens metric, such as `purchase_frequency`, decreases. Lens monitors help you track Lens metrics in real time.

## Define the usecase

```yaml
name: monitor-lens-metric-testing01
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
            name: productaffinity
            workspace: public
            sslmode: 'disable'
        ql: SELECT purchase_frequency FROM purchase
    rightExpression:
      queryCoefficient: 1
      queryConstant: 0
      query:
        type: lens
        lens:
          dataOsInstance:
            name: productaffinity
            workspace: public
            sslmode: 'disable'
        ql: SELECT purchase_frequency FROM purchase
    operator: equals
  incident:
    type: business-metric
    name: lens-customer-analysis
    category: equation
    severity: info
```