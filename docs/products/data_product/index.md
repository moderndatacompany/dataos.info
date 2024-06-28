# Data Product

A Data Product is a self-contained unit designed for handling and sharing analytical data, managed by a dedicated team. It includes data transformation code, input and output definitions, discovery and observability APIs, documentation, service level objectives (SLOs), access control mechanisms, and platform dependencies such as compute and storage resources. This design ensures that the Data Product can be developed, maintained, and deployed independently, providing a comprehensive and autonomous solution for data processing within a larger system.

## Key Concepts of Data Product

**Input**

Input refers to all the data received by a data product from various sources, which is then processed and utilized to generate outputs.

**Output**

Output refers to the data produced by a data product after processing the inputs, which then can be used by data consumers to generate insights.

## Data Product Lifecycle

The development of the Data Product lifecycle consists of four key phases: design, build, deploy, and manage/iterate. In the design phase, the focus is on defining requirements, creating architectural plans, and specifying data inputs, outputs, and performance targets. The build phase involves developing the data transformation code, setting up necessary APIs, and implementing security and access controls. During the deployment phase, the Data Product is moved to a production environment, ensuring it integrates smoothly with existing systems and meets SLOs. Finally, in the manage/iterate phase, the Data Product is monitored for performance and reliability, with continuous improvements and updates being made based on user feedback and changing requirements. This lifecycle ensures the Data Product remains effective, reliable, and up-to-date. In the later sections of this documentation, you will have more detailed information on each phase.

## Structure of Data Product Manifest


```yaml
# Product meta section
name: {{dp-test}} # Product name (mandatory)
version: {{v1alpha}} # Manifest version (mandatory)
type: {{data}} # Product-type (mandatory)
tags: # Tags (Optional)
  - {{data-product}}
  - {{dataos:type:product}}
  - {{dataos:product:data}}
description: {{the customer 360 view of the world}} # Descripton of the product (Optional)
Purpose: {{This data product is intended to provide insights into the customer for strategic decisions on cross-selling additional products.}} # purpose (Optional)
collaborators: # collaborators User ID (Optional)
  - {{thor}}
  - {{blackwidow}}
  - {{loki}}
owner: {{iamgroot}} # Owner (Optional)
refs: # Reference (Optional)
  - title: {{Bundle Info}} # Reference title (Mandatory if adding reference)
    href: {{https://dataos.info/resources/bundle/}} # Reference link (Mandatory if adding reference)
entity: {{product}} # Entity (Mandatory)
# Data Product-specific section (Mandatory)
v1alpha: # Data Product version
  data:
    resources: # Resource specific section(Mandatory)
      - name: {{bundle-dp}} # Resource name (Mandatory)
        type: {{bundle}} # Resource type (Mandatory)
        version: {{v1beta}} # Resource version (Mandatory)
        refType: {{dataos}} # Resource reference type (Mandatory)
        workspace: {{public}} # Workspace (Requirement depends on the resource type)
        description: {{this bundle resource is for a data product}} # Resource description (Optional)
        purpose: {{deployment of data product resources}} # Purpose of the required resource (Optional)   
    
    inputs:
      - description: Sales 360
        purpose: source
        refType: dataos
        ref: dataos://bigquery:PUBLIC/MYTABLE
    
    outputs:
      - description: Customer
        purpose: consumption
        refType: dataos_address
        ref: dataos://icebase:sandbox/sales?acl=rw     
```

## Templates