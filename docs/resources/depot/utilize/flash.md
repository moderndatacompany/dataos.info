# Accelerating queries

For enhancing the query performance, a user can cache the data using [Flash Stack.](/resources/stacks/flash/)

**For example:**

A user wants to reduce the time it takes to get query results, so they cache the dataset in the lakehouse Depot using Flash Service. This ensures faster query results whenever the dataset is queried. The below manifest file defines a Service named `flashtest`. The Service caches a dataset named `city`, stored in `dataos://lakehouse:retail/city`, and initializes a table `mycity` by selecting data from `retail.city`.

```yaml
name: flashtest
version: v1
type: service
tags:
    - service
description: Flash service
workspace: public
service:
    servicePort: 8080
    servicePorts:
    - name: backup
        servicePort: 5433  
    ingress:
    enabled: true
    stripPath: false
    path: /flash/public:flashtest
    noAuthentication: true
    replicas: 1
    logLevel: info
    compute: runnable-default
    envs:
    APP_BASE_PATH: 'dataos-basepath'
    FLASH_BASE_PATH: /flash/public:flashtest
    resources:
    requests:
        cpu: 1000m
        memory: 1024Mi
    stack: flash+python:2.0
    stackSpec:
# Datasets
    datasets:
        - name: city
        address: dataos://lakehouse:retail/city

    init:
        - create table mycity as (select * from retail.city)

    # schedule:
    #   - expression: "*/2 * * * *"
    #     sql: INSERT INTO mycustomer BY NAME (select * from customer);
```
