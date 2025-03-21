---
search:
  exclude: true
---

# Smart Home Data Product
The Smarthome Data Product (smarthome-dp) is designed to monitor air quality index and environmental conditions continuously by capturing data from embedded smart IoT devices. These devices measure various parameters such as temperature, carbon dioxide, light, and smoke levels to ensure optimal living conditions over time.

Below is the Smart Home Data Product manifest template, that will help Data Product personas in their own Data Product development lifecycle:

```yaml

name: smarthome-dp
version: v1alpha
type: data
tags:
  - data-product
  - Readiness.Ready to use
  - Type.External Data Product
  - Tier.Gold
  - Domain.Operations
description: Smarthomes have embedded smart IoT devices that captures various data points such as temperature, carbon dioxide, light and smoke levels, so that over tiime 
purpose: The purpose of the data product is to monitor the air quality index and environmental conditions continuously and monitor temperature and humiditiy.
owner: ironman
collaborators:
  - iamgroot
refs:
  - title: Smart Home Data API Service
    href: https://liberal-donkey.dataos.app/smarthome-api

tags:
  - Tier.Gold
entity: product
v1alpha:
  data:
    useCases:
      - air_quality_monitoring
      - temperature_monitoring
      - humiditiy_monitoring
    resources:
      - description: Smart Home Data API Service
        purpose: API Service
        type: service
        version: v1
        refType: dataos
        name: smarthome-api
        workspace: public
      - description: Smart Home Data Stream processing pipeline
        purpose: Stream Processing Pipeline
        type: service
        version: v1
        refType: dataos
        name: smarthome-data-ingest
        workspace: public
      - description: Smart Home Stream Worker Sync
        purpose: Sync data from Fastbase to Icebase
        type: worker
        version: v1
        refType: dataos
        name: smarthome-data-sync
        workspace: public
      - description: Smart Home Dataset Scanner
        purpose: Scans the ingested dataset
        type: workflow
        version: v1
        refType: dataos
        name: wf-icebase-depot-scanner
        workspace: public
      - description: Smart Home Dataset quality checks
        purpose: Runs quality checks on top of dataset
        type: workflow
        version: v1
        refType: dataos
        name: smarthome-data-quality-checks
        workspace: public
    inputs:
      - description: Fastbase topic of smarthome data
        purpose: source
        refType: dataos
        ref: dataos://fastbase:default/smarthome_data

    outputs:
      - description: By transforming streaming data from Fastbase, the output is created
        purpose: consumption
        refType: dataos_address
        ref: dataos://icebase:smarthome/dataset

```