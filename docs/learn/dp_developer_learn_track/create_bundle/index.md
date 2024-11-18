# Creating a deployable Bundle Resource

After completing the creation of required Resources, it's time to assemble them for building your data product. This involves setting up data ingestion and transformation processes, managing credentials, enforcing quality rules, and more. 

**Scenario:** 

We will create a Data Product that provides a comprehensive view of the customer landscape with understand buying patterns and downstream applications such as targeted marketing campaigns and loyalty programs. We will also include the data model which can help experiment with understanding key business drivers and metrics.

## Quick concepts

A Bundle Resource in DataOS is a standardized way to deploy multiple resources, data products, or applications at once. It lets data developers easily manage the deployment, scheduling, and creation of related resources in a single step.

The Bundle acts like a flattened DAG (directed acyclic graph) where each node is a DataOS Resource, linked by dependencies.

## Step 1: Creating Required DataOS Resources

Ensure you have created all necessary Resources, such as Worker, Workflow, Service, Depot, Cluster, Policy, Secret, Instance Secret, Monitor, Pager, etc.

The following DataOS Resources are required for the example scenarios:

1. Instance-Secret to store credentials safely
2. Depot to connect to the source system.(e.g., bigquery)
3. Flare Workflow to ingest raw data from Bigquery to DataOS Lakehouse
4. Soda Workflows to check the quality of data
5. Policy to enable accessing certain columns of data which is masked by default DataOS policies.

## Step 2: Creating a Bundle Resource

The Bundle Resources section allows you to define the Resources that make up the data product/application and their dependencies in the form of a flattened DAG.

Create a Bundle resource with the above mentioned Resources. Along with all other Resources, Lens is also deployed through Bundle. The Bundle is necessary to link all relevant artifacts to your DP. This enables both data producers and consumers to view all workspace-level resources needed for the DP under one umbrella.

In the below example, the bundle contains:

- The ingestion Workflow
- The Lens model and deployment YAMLs
- The Soda Quality workflows
- The Talos API service YAML


```yaml
name: product360-01-bundle
version: v1beta
type: bundle
tags:
  - dataproduct
description: This bundle resource is for the cross-sell data product.
layer: "user"
bundle:
  resources:
    - id: lens
      file: resources/lens2/deployement.yaml
      workspace: public

    - id: api
      file: consumption_ports/dataApi/service.yaml
      workspace: public
      dependencies:
        - lens

    - id: quality_customer
      file: product-affinity-cross-sell/bundle/quality/customer.yml
      workspace: public

    - id: quality_marketing
      file: product-affinity-cross-sell/bundle/quality/marketing.yml
      workspace: public

    - id: quality_purchase
      file: product-affinity-cross-sell/bundle/quality/purchase.yml
      workspace: public
      
    - id: customer
      file: product-affinity-cross-sell/bundle/ingestion/flare-customer.yml
      workspace: public

    - id: marketing
      file: product-affinity-cross-sell/bundle/ingestion/flare-marketing.yml
      workspace: public
      dependencies:
        - customer

    - id: product
      file: product-affinity-cross-sell/bundle/ingestion/flare-product.yml
      workspace: public
      dependencies:
        - marketing
```

## Next step

After creating your Bundle manifest YAML file, the next step is to create the Data Product Spec file. Check out the following section for details.
[Creating Data Product Spec file](/learn/dp_developer_learn_track/create_dp_spec/)