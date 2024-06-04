# Getting started: Worker

## Create a Worker

A Worker Resource instance can be deployed by applying the manifest file. But before creating a Worker Resource, ensure you have the following:

### **Appropriate Access Permission Use Case**

In DataOS, different actions require specific use cases that grant the necessary permissions to execute a task. You can grant these use cases directly to a user or group them under a tag, which is then assigned to the user. The following table outlines various actions related to Worker Resources and the corresponding use cases required:

| **Action** | **Required Use Cases** |
|------------|------------------------|
| Create     | Read Workspace         |
| Apply      | Read Workspace         |
| Get        | Read Workspaces, Read Resources in User Specified Workspace / Read Resources in User Workspaces (for public and sandbox workspaces) |
| Delete     | Update                 |
| Log        | Update                 |

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

#### **Configuring the Resource meta section**

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
      owner: ${{resource_owner}} # Owner of the Resource (optional, default to user-id of user deploying the resource)
      layer: ${{resource_layer}} # DataOS Layer 
      ```
=== "Example"

      ```yaml
      name: my-first-worker # Name of the Resource
      version: v1beta # Manifest version of the Resource
      type: worker # Type of Resource
      tags: # Tags for categorizing the Resource
        - dataos:worker # Tags 
        - worker # Additional tags
      description: Common attributes applicable to all DataOS Resources
      owner: iamgroot
      layer: user
      ```

To configure a Worker Resource, replace the values of `name`, `layer`, `tags`, `description`, and `owner` with appropriate values. For additional configuration information about the attributes of the Resource meta section, refer to the link: [Attributes of Resource meta section](/resources/resource_attributes/)

#### **Configuring the Worker-specific section**

The Worker-specific section of a manifest file encompasses attributes specific to the Worker Resource.


=== "Basic configuration"

    === "Syntax"

          ```yaml
          name: my-first-worker # Name of the Resource
          version: v1beta # Manifest version of the Resource
          type: worker # Type of Resource
          tags: # Tags for categorizing the Resource
            - dataos:worker # Tags 
            - worker # Additional tags
          description: Common attributes applicable to all DataOS Resources
          owner: iamgroot
          layer: user
          ```

    === "Example"

          ```yaml
          name: my-first-worker # Name of the Resource
          version: v1beta # Manifest version of the Resource
          type: worker # Type of Resource
          tags: # Tags for categorizing the Resource
            - dataos:worker # Tags 
            - worker # Additional tags
          description: Common attributes applicable to all DataOS Resources
          owner: iamgroot
          layer: user
          ```

=== "Advanced configuration"

    === "Syntax"

          ```yaml
          name: my-first-worker # Name of the Resource
          version: v1beta # Manifest version of the Resource
          type: worker # Type of Resource
          tags: # Tags for categorizing the Resource
            - dataos:worker # Tags 
            - worker # Additional tags
          description: Common attributes applicable to all DataOS Resources
          owner: iamgroot
          layer: user
          ```

    === "Example"

          ```yaml
          name: my-first-worker # Name of the Resource
          version: v1beta # Manifest version of the Resource
          type: worker # Type of Resource
          tags: # Tags for categorizing the Resource
            - dataos:worker # Tags 
            - worker # Additional tags
          description: Common attributes applicable to all DataOS Resources
          owner: iamgroot
          layer: user
          ```

#### **Configuring the Stack-specific section**

The Stack-specific section of a manifest file encompasses attributes specific to the Stack orchestrated by the Worker. A Stack Resource within DataOS enables data developers to bring custom programming paradigms to the platform and leverage all native guarantees provided by DataOS.

Although users retain the autonomy to bring any Stack of their choice that supports long-running orchestration, Stacks such as Benthos and Fast Fun that come out-of-the-box with DataOS are compatible with Worker.


=== "Benthos Stack"

      ```yaml
      name: ${{resource_name}} # Name of the Resource (mandatory)
      version: v1beta # Manifest version of the Resource (mandatory)
      type: worker # Type of Resource (mandatory)
      tags: # Tags for categorizing the Resource (optional)
        - ${{tag_example_1}} 
        - ${{tag_example_2}} 
      description: ${{resource_description}} # Description (optional)
      owner: ${{resource_owner}} # Owner of the Resource (optional, default to user-id of user deploying the resource)
      layer: ${{resource_layer}} # DataOS Layer 
      ```
=== "Fast Fun Stack"

      ```yaml
      name: my-first-worker # Name of the Resource
      version: v1beta # Manifest version of the Resource
      type: worker # Type of Resource
      tags: # Tags for categorizing the Resource
        - dataos:worker # Tags 
        - worker # Additional tags
      description: Common attributes applicable to all DataOS Resources
      owner: iamgroot
      layer: user
      ```

=== "Custom Stack"

      ```yaml
      name: my-first-worker # Name of the Resource
      version: v1beta # Manifest version of the Resource
      type: worker # Type of Resource
      tags: # Tags for categorizing the Resource
        - dataos:worker # Tags 
        - worker # Additional tags
      description: Common attributes applicable to all DataOS Resources
      owner: iamgroot
      layer: user
      ```