# How to Generate incidents for certificate expiration?

You can generate incidents for whenever the certificate is about to expire using Equation Monitor. Let's see how you can do so.

``` yaml
# Resource meta section
name: ${{certificateexpirymonitornew}} # Resource name
version: v1alpha
type: monitor
tags:
  - ${{dataos:type:resource}} # Tags
description: ${{SSL certificate is about to expire less then 24 hrs}} # Resource description
layer: user
runAsUser: ${{iamgroot}} # User ID of User (or use case assignee)
monitor:
  
# Monitor-specific section
  schedule: ${{'*/2 * * * *'}} # Monitor schedule
  properties:
    ${{alpha: beta}}
  incident: # mandatory
    asset: ${{output_1}}
    column: ${{column_2}}
    name: ${{CertificateExpirydata}}
    severity: ${{high}}
    incidentType: ${{field_profiling}}

# Equation monitor specification
  type: equation_monitor # mandatory
  equation: 
    # LHS
    leftExpression: 
      queryCoefficient: ${{1}} # mandatory
      queryConstant: ${{0}} # mandatory
      query: # mandatory
        type: ${{prom}} # mandatory
        cluster: ${{thanos}}
        description: ${{query description}}
        dsnSecretRef:
          name: ${{secret}} # mandatory
          workspace: ${{sandbox}}
          key: ${{username}}
          keys:
            - ${{username}}
            - ${{password}}
          allkeys: ${{true}}
          consumptionType: ${{string}}
        ql: certmanager_certificate_expiration_timestamp_seconds{container="cert-manager-controller", endpoint="9402", exported_namespace="caretaker", instance="10.212.4.9:9402", issuer_group="cert-manager.io", issuer_kind="ClusterIssuer", issuer_name="ca", job="cert-manager-ds", name="caretaker-api-cert", namespace="cert-manager", pod="cert-manager-ds-7d8cc489dd-d46sb", service="cert-manager-ds"} - time() # mandatory
        comparisonColumn:  
          name: ${{column1}}
          dataType: ${{string}}

    # RHS
    rightExpression: # mandatory
      queryCoefficient: ${{1}} # mandatory
      queryConstant: ${{7766092}} # mandatory
      query: # mandatory
        type: ${{trino}} # mandatory
        cluster: ${{themis}} # mandatory
        dsn: ${{integer}} 
        dsnSecretRef: 
          name: ${{secret}} # mandatory
          workspace: ${{sandbox}}
          key: ${{username}}
          keys:
            - ${{username}}
            - ${{password}}
          allkeys: ${{true}}
          consumptionType: ${{string}}       
        ql: ${{SELECT metric_value FROM icebase.soda.soda_check_metrics_01 WHERE metric_name = 'missing_count' ORDER BY timestamp DESC LIMIT 1;}} # mandatory
        comparisonColumn: 
          name: ${{column1}} # mandatory
          dataType: ${{integer}} # mandatory      
    # Operator
    operator: ${{less_than}}
```

