# FS Accelerator Data Product

FS Accelerator Data Product is designed to provide a unified and persistent set of identifiers and attributes that describe customers within the financial services domain. This data product aims to seamlessly connect customer data across various organizational silos and business units. It serves as a mastered dataset that is continuously updated in real-time, ensuring accuracy and reliability.

## Pre-requisites
To create the Data Product within DataOS, following requirements were needed:

- Necessary permissions to create and manage Data Products.

- Basic understanding of Data Product principles and lifecycle management.

## Define Usecase and Vision

- **Purpose Clarity:** Clearly articulate why the data product is being created. FS Accelerator involves providing a unified and persistent set of customer identifiers and attributes across organizational silos in the financial services domain.

- **Business Goals:** Align the objectives with broader business goals, such as improving customer service, enhancing operational efficiency, and enabling better data-driven decision-making.

## Design
Steps required to design the Data Product:

1. 


## Build

## Deploy


Below is the FS Acceletor Data Product manifest template, that will help Data Product personas in their own Data Product development lifecycle:

```yaml

name: customer-overview-dp
version: v1alpha
type: data
tags:
  - data-product
  - dataos:type:product
  - dataos:product:data
  - dataos:product:data:customer-overview-dp
description: A unified, accurate, and persistent set of identifiers and attributes that describe a customer and that can be used to connect customer data across multiple organizational silos, and business processes and units. This mastered data, that is continuously live and up-to-date, can be fed to operational and analytical systems to drive business.
entity: product
v1alpha:
  data:
    domain: financial-services
    resources:
      - description: Data Product pipeline
        purpose: build the data product's data set
        type: workflow
        version: v1
        refType: dataos
        name: wf-customer-overview-pipeline
        workspace: fs-domain-workspace
    inputs:
      - description: customer_overview
        purpose: source
        refType: dataos
        ref: dataos://twdepot:finance_service/customer_overview
    outputs:
      - description: Data Product Dataset
        purpose: consumption
        refType: dataos_address
        ref: dataos://icebasetw:fs_accelerator/customer_overview_dp

```