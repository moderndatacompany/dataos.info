# **Kafka Depot Scan**

DataOS allows you to create a Depot of type 'KAFKA' to read live topic data. The created Depot enables you to read live streaming data. You can scan metadata from an KAFKA-type depot with Scanner workflows.

# **Requirements**

To scan the KAFKA depot, you need the following:

1. Ensure that the depot is created and you have `read` access for the depot.
2. To connect to Kafka, you need KAFKA broker list. Once you provide the broker list, the Depot enables fetching all the topics in the KAFKA cluster.

# **Scanner Workflow**

Here is an example of YAML configuration to connect to the source and reach the Metis server to save the metadata in Metis DB.

1. Create and apply the Scanner YAML. You can run the Scanner workflow with or without a filter pattern. 
    
    ```yaml
    version: v1
    name: kafka-scanner2
    type: workflow
    tags:
      - kafka-scanner2.0
    description: The job scans schema tables and register metadata
    workflow:
      dag:
        - name: scanner2-kafka
          description: The job scans schema from kafka depot tables and register metadata to metis2
          spec:
            stack: scanner:2.0
            compute: runnable-default
    				runAsUser: metis
            scanner:
              depot: kafka01
              # sourceConfig:
              #   config:
              #     topicFilterPattern:
              #       includes:
              #         - Sanity
              #         - sampel_Json_Kafka
              #         - consumer_offsets
    ```
    

> **Note:** Remove the commented part mentioned under the filter pattern in the Scanner YAML to apply filters for the required topics.
> 
1. After the successful workflow run, you can check the metadata of scanned topics on Metis UI.