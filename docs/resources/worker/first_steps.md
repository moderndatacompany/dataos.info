# Worker: First Steps

## Create a Worker

A Worker Resource instance can be deployed by applying the manifest file. But before creating a Worker Resource, ensure you have required use-cases assigned.

### **Get Appropriate Access Permission Use Case**

In DataOS, different actions require specific use cases that grant the necessary permissions to execute a task. You can grant these use cases directly to a user or group them under a tag, which is then assigned to the user. The following table outlines various actions related to Worker Resources and the corresponding use cases required:


| **Action** | **Required Use Cases** |
|------------|------------------------|
| Get        | Read Workspaces, Read Resources in User Specified Workspace / Read Resources in User Workspaces (for public and sandbox workspaces) |
| Create     | Create and Update Resources in User Workspace       |
| Apply      | Create and Update Resources in User Workspace          |
| Delete     | Delete Resources in User Workspace               |
| Log        | Read Resource Logs in User Workspace                 |


To assign use cases, you can either contact the DataOS Operator or create a Grant Request by creating a Grant Resource. The request will be validated by the DataOS Operator.

### **Create a manifest file**

To create a Worker Resource, data developers can define a set of attributes in a manifest file, typically in YAML format, and deploy it using the DataOS Command Line Interface (CLI) or API. Below is a sample manifest file for a Worker Resource:

???tip "Sample Worker manifest"

    ```yaml title="sample_worker.yml"
    --8<-- "examples/resources/worker/sample_worker.yml"
    ```

The manifest file for a Worker Resource consists of three main sections, each requiring specific configuration:

- [Resource Meta Section](#configuring-the-resource-meta-section): Contains attributes shared among all types of Resources.
- [Worker-Specific Section](#configuring-the-worker-specific-section): Includes attributes unique to the Worker Resource.
- [Stack-Specific Section](#configuring-the-stack-specific-section): Encompasses attributes specific to the Stack orchestrated by the Worker, which can vary depending on the Stack.

#### **Resource meta section**

In DataOS, a Worker is categorized as a Resource type. The YAML configuration file for a Worker Resource includes a Resource meta section, which contains attributes shared among all Resource types.

The following YAML excerpt illustrates the attributes specified within this section:

=== "Syntax"

      ```yaml
      name: ${{resource_name}} # Name of the Resource (mandatory)
      version: v1beta # Manifest version of the Resource (mandatory)
      type: worker # Type of Resource (mandatory)
      tags: # Tags for categorizing the Resource (optional)
        - ${{tag_example_1}} 
        - ${{tag_example_2}} 
      description: ${{resource_description}} # Description (optional)
      owner: ${{resource_owner}} # Owner of the Resource (optional, default value: user-id of user deploying the resource)
      layer: ${{resource_layer}} # DataOS Layer (optional, default value: user)
      ```
=== "Example"

      ```yaml
      name: my-first-worker # Name of the Resource
      version: v1beta # Manifest version of the Resource
      type: worker # Type of Resource
      tags: # Tags for categorizing the Resource
        - dataos:worker 
        - worker 
      description: Common attributes applicable to all DataOS Resources # Description
      owner: iamgroot # Owner of the Resource
      layer: user # DataOS Layer
      ```

To configure a Worker Resource, replace the values of `name`, `layer`, `tags`, `description`, and `owner` with appropriate values. For additional configuration information about the attributes of the Resource meta section, refer to the link: [Attributes of Resource meta section](/resources/resource_attributes/).

#### **Worker-specific section**

The Worker-specific section of a manifest file encompasses attributes specific to the Worker Resource.


=== "Basic configuration"

    === "Syntax"

        ```yaml
        worker:
          stack: ${{worker_stack}} # Stack used (mandatory) 
          compute: ${{compute_resource_name}} # Compute configuration (mandatory)
          stackSpec: # Stack-specific section
            # Attributes specific to the choosen Stack are declared here
        ```
    === "Example"

        ```yaml
        worker:
          stack: benthos # Stack used (mandatory) 
          compute: runnable-default # Compute configuration (mandatory)
          stackSpec: # Stack-specific section (mandatory)
            # Attributes specific to the choosen stack are declared here
        ```

=== "Advanced configuration"

    === "Syntax"

        ```yaml
        worker: # Worker-specific configuration
          title: ${{worker_title}} # Title of the worker 
          tags:
            - ${{worker_tag1}} # Tags for the worker 
            - ${{worker_tag2}} # Additional tags (
          replicas: ${{worker_replicas}} # Number of replicas 
          autoscaling: # Autoscaling configuration
            enabled: ${{autoscaling_enabled}} # Enable or disable autoscaling 
            minReplicas: ${{min_replicas}} # Minimum number of replicas 
            maxReplicas: ${{max_replicas}} # Maximum number of replicas 
            targetMemoryUtilizationPercentage: ${{memory_utilization}} # Target memory utilization percentage 
            targetCPUUtilizationPercentage: ${{cpu_utilization}} # Target CPU utilization percentage 
          stack: ${{worker_stack}} # Stack used (mandatory) 
          logLevel: ${{log_level}} # Logging level 
          configs: # Configuration settings
            ${{config_key1}}: ${{config_value1}} # Example configuration 
            ${{config_key2}}: ${{config_value2}} # Additional configuration 
          envs: # Environment variables
            ${{env_key1}}: ${{env_value1}} # Example environment variable 
            ${{env_key2}}: ${{env_value2}} # Additional environment variable 
          secrets: 
            - ${{secret_name}} # List of secrets 
          dataosSecrets: # DataOS secrets configuration
            - name: ${{secret_name}} # Name of the secret 
              workspace: ${{secret_workspace}} # Workspace 
              key: ${{secret_key}} # Key 
              keys: 
                - ${{secret_key1}} # List of keys 
                - ${{secret_key2}} # Additional key 
              allKeys: ${{all_keys_flag}} # Include all keys or not 
              consumptionType: ${{consumption_type}} # Type of consumption 
          dataosVolumes: # DataOS volumes configuration
            - name: ${{volume_name}} # Name of the volume 
              directory: ${{volume_directory}} # Directory 
              readOnly: ${{read_only_flag}} # Read-only flag 
              subPath: ${{volume_subpath}} # Sub-path 
          tempVolume: ${{temp_volume_name}} # Temporary volume 
          persistentVolume: # Persistent volume configuration
            name: ${{persistent_volume_name}} # Name of the volume 
            directory: ${{persistent_volume_directory}} # Directory 
            readOnly: ${{persistent_volume_read_only}} # Read-only flag 
            subPath: ${{persistent_volume_subpath}} # Sub-path 
          compute: ${{compute_resource_name}} # Compute configuration 
          resources: # Resource requests and limits
            requests:
              cpu: ${{cpu_request}} # CPU request 
              memory: ${{memory_request}} # Memory request 
            limits:
              cpu: ${{cpu_limit}} # CPU limit 
              memory: ${{memory_limit}} # Memory limit 
          dryRun: ${{dry_run_flag}} # Dry run flag 
          runAsApiKey: ${{api_key}} # API key for running the worker 
          runAsUser: ${{run_as_user}} # User to run the worker as 
          topology: # Topology configuration
            - name: ${{topology_name}} # Name of the topology 
              type: ${{topology_type}} # Type of the topology 
              doc: ${{topology_doc}} # Documentation link or description 
              properties:
                ${{property_key}}: ${{property_value}} # Example property 
              dependencies: # List of dependencies
                - ${{dependency1}} # Example dependency 
                - ${{dependency2}} # Additional dependency
          stackSpec: 
            # Attributes specific to the choosen Stack
        ```

#### **Stack-specific section**

The Stack-specific section of a manifest file includes attributes unique to the Stack orchestrated by the Worker. A Stack Resource within DataOS allows data developers to integrate custom programming paradigms into the platform while utilizing all the native guarantees provided by DataOS.

While users have the flexibility to bring any Stack that supports long-running orchestration, Stacks such as Benthos and Fast Fun, which come out-of-the-box with DataOS, are compatible with Workers.

| Stack | Purpose of Worker orchestrated by the Stack |
| --- | --- |
| Benthos | Benthos Stack enables stream data processing. When orchestrated using a Worker Resource, Benthos Stack facilitates long-running processes that continuously process stream data and write to a sink of choice. |
| Fast Fun | Fast Fun is a declarative Stack that enables data sinking from Pulsar-type depots such as Fastbase and systemstream to DataOS Lakehouse storage (or depots supporting the Iceberg file format). While Benthos Workers support processing, Fast Fun sinks data as-is without transformation. |

The attributes within the `stackSpec` section vary between Stacks and are determined by the `workerConfig` attribute within the definition of that specific Stack. Below are sample stackSpec sections for the respective Stacks.


=== "Benthos Stack"

    Below is a sample stack specification for a Benthos Worker, where an end user wants to read data from a specific URL and provide a standard output:

    ```yaml 
    stackSpec:
      input:
        http_client:
          headers:
            Content-Type: ${{content_type}}
          url: ${{http_url}}
          verb: ${{http_verb}}
      output:
        stdout:
          codec: ${{codec}}
    ```
    To get templates for Benthos Workers, click on this link. For details about the information of the Benthos Stack, refer to the link: Benthos

=== "Fast Fun Stack"

    ```yaml
    stackSpec:
      input:
        datasets:
          - ${{input_dataset_udl_address}}
        options:
          cleanupSubscription: ${{cleanup_subscription_or_not}}
          processingGuarantees: ${{processing_guarantees}}
          subscriptionPosition: ${{subscription_position}} 
      output:
        datasets:
          - ${{output_dataset_udl_address}}
        options:
          commitInterval: ${{commit_interval}}
          iceberg:
            properties:
              write.format.default: ${{write_file_format}}
              write.metadata.compression-codec: ${{write_metadata_compression_codec}}
          recordsPerCommit: ${{number_of_records_per_commit}}
    ```

    To look at a few examples related to the Fast Fun Stack

## Manage a Worker

### **Verifying Worker creation**

To ensure that your Worker has been successfully created, you can verify it in two ways:

Check the name of the newly created Worker in the list of workers created by you in a particular Workspace:

```shell
dataos-ctl get -t worker - w <workspace-name>
```

```shell
dataos-ctl get -t worker - w <workspace-name>
```

Sample

```shell
dataos-ctl get -t worker -w curriculum
```

Alternatively, retrieve the list of all Workers created in the Workspace by appending `-a` flag:

```shell
dataos-ctl get -t worker -w <workspace-name> -a
# Sample
dataos-ctl get -t worker -w curriculum -a
```

You can also access the details of any created Lakehouse through the DataOS GUI in the Resource tab of the  [Operations](/interfaces/operations/) app.

### **Getting Worker logs**

### **Deleting a Worker**

Use the [`delete`](/interfaces/cli/command_reference/#delete) command to remove the Worker from the DataOS environment. As shown below, there are three ways to delete a Worker.

**Method 1:** Copy the Worker name, version, Resource-type and Workspace name from the output of the [`get`](/interfaces/cli/command_reference/#get) command seperated by '|' enclosed within quotes and use it as a string in the delete command.

Command

```shell
dataos-ctl delete -i "${identifier string}"
```

Example

```shell
dataos-ctl delete -i "demo-01 | v1beta | worker | public"
```

Output

```shell
INFO[0000] 🗑 delete...
INFO[0001] 🗑 deleting(public) demo-01:v1beta:worker...
INFO[0003] 🗑 deleting(public) demo-01:v1beta:worker...deleted
INFO[0003] 🗑 delete...complete
```

**Method 2:** Specify the path of the YAML file and use the [`delete`](/interfaces/cli/command_reference/#delete) command.

Command

```shell
dataos-ctl delete -f ${manifest-file-path}
```

Example

```shell
dataos-ctl delete -f /home/desktop/connect-city/config_v1alpha.yaml
```

Output

```shell
INFO[0000] 🗑 delete...
INFO[0001] 🗑 deleting(public) demo-01:v1beta:worker...
INFO[0003] 🗑 deleting(public) demo-01:v1beta:worker...deleted
INFO[0003] 🗑 delete...complete
```

**Method 3:** Specify the Workspace, Resource-type, and Worker name in the [`delete`](/interfaces/cli/command_reference/#delete) command.

Command

```shell
dataos-ctl delete -w ${workspace} -t worker -n ${worker name}
```

Example

```shell
dataos-ctl delete -w public -t worker -n demo-01
```

Output

```shell
INFO[0000] 🗑 delete...
INFO[0001] 🗑 deleting(public) demo-01:v1beta:worker...
INFO[0003] 🗑 deleting(public) demo-01:v1beta:worker...deleted
INFO[0003] 🗑 delete...complete
```



## Next steps

Your next steps depend upon whether you want to learn about what you want to do, or want to configure a specific Worker further, here are some how to guides to help you with that process:

- Learn how to configure the manifest file of a Worker. See [Worker: Configuration]()
- Set up workers to sync data from Fastbase topics to Icebase dataset. See [How to Create a Report Monitor]()
- Set up workers to transform stream data. See [How to create a Stream Monitor]()
