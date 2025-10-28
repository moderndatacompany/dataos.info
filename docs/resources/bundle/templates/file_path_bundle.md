# File Path Bundle Template

This YAML template defines a DataOS Bundle Resource that demonstrates the **modular file-based approach** using the `file` attribute. Instead of embedding complete Resource specifications inline, this template references external YAML manifest files, promoting separation of concerns, reusability, and maintainability across complex deployments.

## Use Case

This template is ideal for:

- **Large-scale deployments** with many Resources (5+ Resources)
- **Enterprise environments** where different teams manage different Resources
- **Resource reusability** scenarios where the same Depot, Cluster, or Service is used across multiple Bundles
- **Complex Data Products** with multiple interconnected components
- **CI/CD pipelines** where Resource files are generated or templated separately
- **Multi-environment deployments** where Resource files are environment-specific

## Template


```yaml
name: cross-sell-bundle-pipeline
version: v1beta
type: bundle
tags:
  - dataproduct
description: This bundle Resource is for the cross-sell data product.
layer: "user"
bundle:
  workspaces:
    - name: tester
      description: "This workspace runs bundle Resources"
      tags:
        - dataproduct
        - bundleResource
      labels:
        name: "dataproductBundleResources"
      layer: "user"
  Resources:
    - id: ingestion_dag
      file: build/super_dag_ingestion.yml  #local file path
      workspace: public

    - id: quality_dag
      file: build/super_dag_quality.yml #local file path
      workspace: public
      dependencies:
        - ingestion_dag
      dependencyConditions:
        - ResourceId: ingestion_dag
          status:
            is:
              - active
          runtime:
            is:
              - succeeded
```


## When to Use File-Based vs. Direct Bundles

**Use File-Based Bundle (this template) when:**

- Managing 5+ Resources in a single Bundle
- Resources are reused across multiple Bundles or Data Products
- Different teams or individuals manage different Resources
- Resource configurations are large (>50 lines each)
- You need to test or validate Resources independently
- Working with CI/CD pipelines that generate Resource files

**Use Direct Bundle (Template 1) when:**

- You have 2-4 simple Resources
- All configurations fit in one file (<500 lines total)
- Maximum portability with a single file is desired
- Resources are always deployed together and never reused