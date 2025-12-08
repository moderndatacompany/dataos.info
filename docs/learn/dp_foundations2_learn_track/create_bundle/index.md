# Creating a Deployable Bundle Resource

After creating and testing all necessary components, it's time to assemble them into a single, deployable unit using a Bundle Resource in DataOS. This bundle acts as the foundation of your Data Product, packaging all production ready Resources, ensuring consistent and scalable deployments across environments.

## Scenario

In our source-aligned retail Data Product, a bundle in DataOS packages ingestion, quality checks, monitors, and pagers into a single deployable unit. It keeps everything connected and consistent, making it easy to deploy the product across environments with minimal setup.

## Quick concepts

- A Bundle Resource in DataOS is a standardized way to deploy multiple resources, Data Products, or applications at once. It lets data developers easily manage the deployment, scheduling, and creation of related resources in a single step.

- The Bundle acts like a flattened DAG (directed acyclic graph) where each node is a DataOS Resource, linked by dependencies.

## Step 1: Creating required DataOS Resources

Ensure you have created all necessary Resources, such as Worker, Workflow, Service, Depot, Cluster, Policy, Secret, Instance Secret, Monitor, Pager, etc.

The following DataOS Resources are required for the example scenarios:

1. Instance-Secret to store credentials safely
2. Depot to connect to the source system (e.g., BigQuery)
3. Flare Workflow to ingest raw data from Bigquery to DataOS Lakehouse
4. Soda Workflows to check the quality of data
5. Monitors and Pagers to observe Workflow and Quality failures

## Step 2: Creating a Bundle Resource

The Bundle manifest defines all related resources and their interdependencies. It ensures they are packaged and deployed together.

Create a Bundle resource with the above mentioned Resources. The Bundle links all relevant artifacts to your Data Product, allowing both producers and consumers to view all required workspace-level resources in one place.

In the below example, the bundle contains:

- Ingestion Workflow
- Soda Quality workflows
- Monitors and pagers



```yaml
name: retaildata-bundle-abc
version: v1beta
type: bundle
description: Source-aligned Data Product Bundle
layer: user
bundle:
  resources:
    - id: quality_customer
      file: build/slo/input/customer.yml    # Example path - update as needed
      workspace: <workspace_name>
      
    - id: quality_product
      file: build/slo/input/product.yml
      workspace: public

    - id: quality_purchase
      file: build/slo/input/purchase.yml
      workspace: <workspace_name>
      
    - id: quality_monitor
      file: <actual_path>
      workspace: <workspace_name>
      
    - id: workflow_monitor
      file: 
      workspace: <workspace_name>
      
    - id: quality_pager
      file: 
      workspace: <workspace_name>
      dependencies:
        - quality_monitor
      
    - id: workflow_pager
      file: 
      workspace: <workspace_name>
      dependencies:
        - workflow_monitor
    
    # Add other resources you have created
    # - id: filter_policy
    #   file: policy/filter-policy.yml
    #   workspace: public
    #   dependencies:
    #     - api # Provide id 
```

> Tip: Make sure all referenced files and paths are correct and that you’ve tested each resource individually before bundling.

## Next step

With your Bundle defined, you're ready to create the Data Product Spec file, which captures metadata, purpose, input/output datasets, and links to this bundle.

👉 Continue to:[Creating Data Product Spec file](/learn/dp_foundations1_learn_track/create_dp_spec/)