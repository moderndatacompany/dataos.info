# **From Testing to Production**

Once you have successfully tested the Job on Standalone, now it's time to take it into production by submitting it to Poros, the Resource Manager for DataOS. But before doing so there are a couple of tweaks that you need to make in the YAML. The below sections give details for these configurations.

## **Replace the IO Data Source Configs with IO Depot Configs**

When we run a Flare Job, one of the necessary conditions is that the data should reside within a depot. Once a depot is created it removes the need for specifying the credentials separately. So when we move from Flare Standalone to writing an actual Flare Job that uses depots, we need to remove all the source configurations and replace them with corresponding depot configurations.

### **Input Section**

Replace the Input Data Source Properties with Dataset Properties in UDL. The below blocks show a sample `inputs` section  is given below

```yaml
# Data Source Input Configuration
inputs:
  - name: oms_transactions_data
    inputType: file
    file:
      path: /data/examples/default/transactions/
      format: json
```

```yaml
# Dataset Input Configuration 
inputs:
  - name: oms_transactions_data
    dataset: dataos://thirdparty:default/transactions
    format: json

```

### **Outputs Section**

```yaml
# Data Source Output Configuration
outputs:
  - name: finalDf
    outputType: pulsar
    pulsar:
      serviceUrl: pulsar+ssl://<protocol>.<dataos-context>:<port>
      adminUrl: https://<protocol>.<dataos-context>:<port>
      topic: <topic-name>
```

```yaml
# Dataset Output Configuration 
outputs:
  - name: finalDf
    dataset: dataos://pulsar01:default?acl=rw
    format: pulsar

```

## **Remove the Environment Variables**

Remove the Data Source Environment Variables while submitting a Flare Job. Depots abstract the need to define the source environment variables hence additional variables need not be defined

```yaml
# Data Source Environment Variables
envs:
  PULSAR_SSL: true
  ENABLE_PULSAR_AUTH: true
  DATAOS_RUN_AS_APIKEY: <prime-api-key>
```

```yaml
# This is what removal means 

```

## **Remove the Spark Configuration (only Data Source Connection ones)**

Remove all Spark Configuration that was required for connection to the Data Source in Standalone. Though, you can keep the ones that are required for optimizing your Job.

```yaml
# Spark Configuration for Flare Standalone
sparkConf:
  - spark.sql.adaptive.autoBroadcastJoinThreshold: 20m # (Configuration For Job Optimization)
  - spark.sql.shuffle.partitions: 450 # (Configuration For Job Optimization)
  - spark.sql.optimizer.dynamicPartitionPruning.enabled: true # (Configuration For Job Optimization)
  - spark.serializer: org.apache.spark.serializer.KryoSerializer # (Configuration For Job Optimization)
  - spark.default.parallelism: 300 # (Configuration For Job Optimization)
  - spark.sql.broadcastTimeout: 200 # (Configuration For Job Optimization)
	- 'spark.hadoop.fs.s3a.bucket.<bucket-name>.access.key': '<access-key>' # (Configuration For Data Source Connection)
	- 'spark.hadoop.fs.s3a.bucket.<bucket-name>.secret.key': '<secret-key>' # (Configuration For Data Source Connection)
```

```yaml
# Spark Configuration for Flare
sparkConf:
  - spark.sql.adaptive.autoBroadcastJoinThreshold: 20m # (Configuration For Job Optimization)
  - spark.sql.shuffle.partitions: 450 # (Configuration For Job Optimization)
  - spark.sql.optimizer.dynamicPartitionPruning.enabled: true # (Configuration For Job Optimization)
  - spark.serializer: org.apache.spark.serializer.KryoSerializer # (Configuration For Job Optimization)
  - spark.default.parallelism: 300 # (Configuration For Job Optimization)
  - spark.sql.broadcastTimeout: 200 # (Configuration For Job Optimization)

```

Once you have made the above changes you can move over to submitting the Flare Job to production.