# How to integrate Volume with Flash?

In DataOS, Flash enhances query performance with in-memory caching. However, when dealing with large datasets, Flash’s memory can become overloaded, leading to system crashes. Volume Storage is attached to Flash to address these challenges by offering persistent and scalable storage. Volume storage extends Flash’s capacity to handle large datasets, ensuring stable performance and preventing crashes.  

Follow the below steps:

## Volume manifest file

```yaml
name: email-attribution-vol # Name of the Resource
version: v1beta # Manifest version of the Resource
type: volume # Type of Resource
tags: # Tags for categorizing the Resource
  - dataos:volume # Tags
  - volume # Additional tags
  - ad-attribution
description: Storage Volume for ad-attribution lens
# owner: sgws
layer: user
volume:
  size: 225Gi  #100Gi, 50Mi, 10Ti, 500Mi
  accessMode: ReadWriteMany  #ReadWriteOnce, ReadOnlyMany.
  type: temp
```

## Flash Service manifest file

Refernce the Volume created in the `persistanceVolume` attribute of the Flash Service.

```yaml
name: flash-email-attribution-service
version: v1
type: service
tags:
  - service
description: flash service for email_campaign_attribution
workspace: public
service:
  servicePort: 5433
  replicas: 1
  stack: flash+python:1.0
  logLevel: info
  # compute: runnable-default           # (16/64)
  # compute: advancedminerva-compute    # (16/128)
  compute: navigator-compute          # (64/512)


  persistentVolume:
    name: email-attribution-vol
    directory: p_volume_temp

  resources:
    requests:
      cpu: 250m
      memory: 2Gi

    limits:
      cpu: 58000m
      memory: 450Gi

  envs:
    INIT_SQLS: "set azure_transport_option_type = 'curl'"


  stackSpec:
    datasets:

      - address: dataos://icebase:sandbox/sfmc_email_activity
        name: email_campaign

      - address: dataos://icebase:sandbox/efdp_sales_v2
        name: sales

      - address: dataos://icebase:sandbox/efdp_product_v2
        name: product

      - address: dataos://icebase:sandbox/efdp_customer_v2
        name: customer

    init:

      -  SET temp_directory = '/var/dataos/persistent_data/p_volume_temp/main.duckdb.tmp';
          SET allocator_flush_threshold = '64MiB';
          SET checkpoint_threshold = '128MiB';
          set threads=10;
          set external_threads=8;
          SET preserve_insertion_order = false;
          SET memory_limit = '420GiB';

      - >
        select
         *
        from duckdb_settings() where name in ('external_threads','memory_limit','threads','worker_threads','checkpoint_threshold')


      - >
        CREATE TABLE IF NOT EXISTS email_campaign as
        (
        select * from email_campaign
        )


      - >
        CREATE TABLE IF NOT EXISTS sales as
        (
          select * from sales
        )

      - >
        CREATE TABLE IF NOT EXISTS product as
        (
          select * from product
        )

      - >
        CREATE TABLE IF NOT EXISTS customer as
        (
          select * from customer
        )
```

