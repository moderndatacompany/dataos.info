# DataOS<sup>®</sup> DEPOT

This document talks about DataOS® Depots and how to create them.


## What is a Depot?

 Depot is a resource which helps you to easily understand the data source/sink within DataOS®. The concept of a depot is to provide the information of data source/sink in an abstract manner.


## Table of contents

* [Types of depot](#types-of-depot)
* [How to create a depot](#how-to-create-a-depot)
* [Config Detail for each depot type.](#config-detail-for-each-depot-type)



### Types of depot

   - [FILE](#file)
   - [PULSAR](#pulsar)
   - [GCS](#gcs)
   - [BIGQUERY](#bigquery)
   - [ABFSS](#abfss)
   - [KAFKA](#kafka)
   - [S3](#s3)
   - [MYSQL](#mysql)
   - [POSTGRESQL](#postgresql)
   - [JDBC](#jdbc)
   - [ELASTICSEARCH](#elasticsearch)
   - [PRESTO](#presto)
   - [REDIS](#redis)
   

### How to create a depot
 1. Create a yaml with below content.
    ```
    version: v1beta1
    name: "raw01"                                 #(REQUIRED) 
    type: depot                                   #(REQUIRED) 
    tags:                                         #(OPTIONAL) 
      - google-cloud
    owner: bob_tmdc_io                            #(OPTIONAL) 
    description: "Default Raw Zone Depot"         #(OPTIONAL) 
    depot:                                        #(REQUIRED) corresponding section for the type
      spec:                                       #(REQUIRED) depot connection specification
        bucket: <bucket-name>,
        relativePath: "raw"
      connectionSecret:                           #(OPTIONAL) secrets to access the depot
        - acl: r                                  #(OPTIONAL) secret that gives reader permissions
          type: key-value-properties
        - acl: rw                                 #(OPTIONAL) secret that gives read & write permissions
          type: key-value-properties
      external: true
      hiveSync: false
      type: <depot-type>                         #(REQUIRED) depot type
    ```
2. Run
   ```
    dataos-ctl apply -f <filepath> -n <workspace>
   ```

## Config Detail for each depot type.
### FILE
```
    version: v1beta1
    name: "raw01"
    type: depot
    tags:
      - raw01
    owner: bob_tmdc_io
    description: "Default Raw Zone Depot"
    depot:
      spec:
        path: "tmp/dataos"
      external: true
      hiveSync: false
      type: FILE
```

### PULSAR
```
    version: v1beta1
    name: "raw01"
    type: depot
    tags:
      - raw01
    owner: bob_tmdc_io
    description: "Default Raw Zone Depot"
    depot:
      spec:
        adminUrl: <admin-url>
        serviceUrl: <service-url>
      external: true
      hiveSync: false
      type: PULSAR
```
### BIGQUERY
```
  version: v1beta1
    name: "raw01"
    type: depot
    tags:
      - raw01
    owner: bob_tmdc_io
    description: "Default Raw Zone Depot"
    depot:
      spec:
        project: "aerobik-dataos"
        dataset : "dataset01"
        params: 
           key: "value"
      connectionSecret:
        - acl: rw
          values:
            bucket: <bucket-name>
            json_keyfile: <json-file-path>
        - acl: r
          values:
            json_keyfile: <json-file-path>
      external: true
      hiveSync: false
      type: BIGQUERY
```

### GCS
```
   version: v1beta1
    name: "raw01"
    type: depot
    tags:
      - raw01
    owner: bob_tmdc_io
    description: "Default Raw Zone Depot"
    depot:
      spec:
        bucket: <bucket-name>
        relativePath: "raw"
      connectionSecret:
        - acl: rw
          values:
            email: <service-accounnt-email>
            gcskey_json: <json-file-path>
            projectid: <project-id>
        - acl: r
          values:
            email: <service-accounnt-email>
            gcskey_json: <json-file-path>
            projectid: <project-id>
      external: true
      hiveSync: false
      type: GCS
```
### ABFSS
```
   version: v1beta1
    name: "raw01"
    type: depot
    tags:
      - raw01
    owner: bob_tmdc_io
    description: "Default Raw Zone Depot"
    depot:
      spec:
        account: "aerobik-dataos"
        container: "container01"
      connectionSecret:
        - acl: rw
          values:
             azurestorageaccountname: <azure-storage-account-name>
             azurestorageaccountkey: <azure-storage-account-key>
        - acl: r
          values:
            azurestorageaccountname: <azure-storage-account-name>
            azurestorageaccountkey: <azure-storage-account-key>
      external: true
      hiveSync: false
      type: ABFSS
```
### KAFKA
```
   version: v1beta1
    name: "raw01"
    type: depot
    tags:
      - raw01
    owner: bob_tmdc_io
    description: "Default Raw Zone Depot"
    depot:
      spec:
        brokers: ["localhost:9092", "localhost:9093"]
      external: true
      hiveSync: false
      type: KAFKA
```
### S3
```
   version: v1beta1
    name: "raw01"
    type: depot
    tags:
      - raw01
    owner: bob_tmdc_io
    description: "Default Raw Zone Depot"
    depot:
      spec:
        bucket: <bucket-name>
        relativePath: "raw"
      connectionSecret:
        - acl: rw
          values:
            accesskeyid: <access-key-id>
            secretkey: <secret-key>
        - acl: r
          values:
            accesskeyid: <access-key-id>
            secretkey: <secret-key>
      external: true
      hiveSync: false
      type: S3
```
### MYSQL
```
   version: v1beta1
    name: "raw01"
    type: depot
    tags:
      - raw01
    owner: bob_tmdc_io
    description: "Default Raw Zone Depot"
    depot:
      spec:
         host: "localhost",
         port: "3306",
         database: "mysql"
      connectionSecret:
        - acl: rw
          values:
            username: <username>
            password: <password>
        - acl: r
          values:
            username: <username>
            password: <password>
      external: true
      hiveSync: false
      type: MYSQL
```
### POSTGRESQL
```
   version: v1beta1
    name: "raw01"
    type: depot
    tags:
      - raw01
    owner: bob_tmdc_io
    description: "Default Raw Zone Depot"
    depot:
      spec:
        host: "localhost"
        port: "3306"
        database: "mysql"
      connectionSecret:
        - acl: rw
          values:
            username: <username>
            password: <password>
        - acl: r
          values:
            username: <username>
            password: <password>
      external: true
      hiveSync: false
      type: POSTGRESQL
```
### JDBC
```
   version: v1beta1
    name: "raw01"
    type: depot
    tags:
      - raw01
    owner: bob_tmdc_io
    description: "Default Raw Zone Depot"
    depot:
      spec:
        subprotocol: "mysql"
        host: "localhost"
        port: "3306"
        database: "mysql"
      connectionSecret:
        - acl: rw
          values:
            username: <username>
            password: <password>
        - acl: r
          values:
            username: <username>
            password: <password>
      external: true
      hiveSync: false
      type: JDBC
```
### ELASTICSEARCH
```
  version: v1beta1
    name: "raw01"
    type: depot
    tags:
      - raw01
    owner: bob_tmdc_io
    description: "Default Raw Zone Depot"
    depot:
      spec:
        nodes: ["localhost:9092", "localhost:9093"]
      connectionSecret:
        - acl: rw
          values:
            username: <username>
            password: <password>
        - acl: r
          values:
            username: <username>
            password: <password>
      external: true
      hiveSync: false
      type: ELASTICSEARCH
```
### PRESTO
```
   version: v1beta1
    name: "raw01"
    type: depot
    tags:
      - raw01
    owner: bob_tmdc_io
    description: "Default Raw Zone Depot"
    depot:
      spec:
         host: "localhost"
         port: "5432"
         catalog: "postgres"
      connectionSecret:
        - acl: rw
          values:
            username: <username>
            password: <password>
        - acl: r
          values:
            username: <username>
            password: <password>
      external: true
      hiveSync: false
      type: PRESTO
```
### REDIS
```
   version: v1beta1
    name: "raw01"
    type: depot
    tags:
      - raw01
    owner: bob_tmdc_io
    description: "Default Raw Zone Depot"
    depot:
      spec:
         host: "localhost"
         port: 5432
         db: 10
         table: "user"
      connectionSecret:
        - acl: rw
          values:
            password: <password>
        - acl: r
          values:
            password: <password>
      external: true
      hiveSync: false
      type: REDIS
```
***