# Orchestrating Multiple Workflows from a Single Workflow

This section demonstrates how to orchestrate multiple workflows by referencing separate YAML files in a master Workflow YAML file. By following this approach, you can streamline complex data processing tasks into manageable pieces.

## Code Snippet

The code snippet below shows the master Workflow (`dag.yaml`) that references two separate Workflows (stored in `read-pulsar.yaml` and `write-pulsar.yaml`) by specifying the file path within the `file` attribute. 

<details>
<summary>Click here to view the code snippets</summary>

<b>dag.yaml</b>

```yaml
# Resource Section
name: wf-sample-dag
version: v1
type: workflow
tags:
  - read
  - write
description: This jobs reads data from thirdparty and writes to pulsar

# Workflow-specific Section
workflow:
  dag:
    - name: write
      file: workflows/write-pulsar.yaml 

    - name: read
      file: workflows/read-pulsar.yaml
      dependencies:
        - write
```

<b>write-pulsar.yaml</b>

```yaml
# Resource Section
name: write-pulsar-01
version: v1
type: workflow
tags:
  - pulsar
  - read
description: this jobs reads data from thirdparty and writes to pulsar

# Workflow-specific Section
workflow:
  dag:

# Job-specific Section
    - name: write-pulsar
      title: write avro data to pulsar
      description: write avro data to pulsar
      spec:
        tags:
          - Connect
        stack: flare:4.0
        compute: runnable-default

# Flare Stack-specific Section        
        flare:
          job:
            explain: true

            inputs:
              - name: input
                dataset: dataos://thirdparty01:none/city
                format: csv
                isStream: false
            logLevel: INFO

            outputs:
              - name: finalDf
                dataset: dataos://sanitypulsar01:default/city_pulsar_01?acl=rw
                format: pulsar
                tags:
                  - Connect
                title: City Data Pulsar

            steps:
              - sequence:
                  - name: finalDf
                    sql: SELECT * FROM input
```

<b>read-pulsar.yaml</b>

```yaml
# Resource Section
name: read-pulsar-01
version: v1
type: workflow
tags:
  - pulsar
  - read
description: this jobs reads data from thirdparty and writes to pulsar

# Workflow-specific Section
workflow:
  dag:

# Job 1 specific Section
    - name: read-pulsar-001
      title: write avro data to pulsar
      description: write avro data to pulsar
      spec:
        tags:
          - Connect
        stack: flare:4.0
        compute: runnable-default

# Flare Stack-specific Section
        flare:
          job:
            explain: true
            logLevel: INFO

            inputs:
              - name: input
                dataset: dataos://sanitypulsar:default/city_pulsar_01
                isStream: false
                options:
                  startingOffsets: earliest

            outputs:
              - name: output
                dataset: dataos://icebase:sanity/sanity_pulsar?acl=rw
                format: Iceberg
                options:
                  saveMode: overwrite

            steps:
              - sequence:
                  - name: finalDf
                    sql: SELECT * FROM input

# Job 2 specific Section
    - name: dataos-tool-pulsar
      spec:
        stack: toolbox
        compute: runnable-default

# Toolbox Stack-specific Section
        toolbox:
          dataset: dataos://icebase:sample/sanity_pulsar?acl=rw
          action:
            name: set_version
            value: latest
      dependencies:
        - read-pulsar-001
```

</details>


## Implementation Flow

- Save the above code snippets into separate YAML files.

- Once you do that mention the path (relative or absolute) of the `read-pulsar.yaml` and `write-pulsar.yaml` in the file property of the master file `dag.yaml`.

- Apply the `dag.yaml` command from the CLI.

When you apply the `dag.yaml` file, using CLI, it calls in the `write-pulsar.yaml` file first and the `read-pulsar.yaml` file second as the second file is dependent upon the first. The Workflow within the `write-pulsar.yaml` writes the data from `thirdparty` depot to `sanitypulsar01` depot. Once that is done the second workflow is executed which writes the same data from `sanitypulsar01` depot to the `icebase` depot. This finishes the two processing tasks by applying just one file.


