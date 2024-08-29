# Getting started: Volume

## Create a Volume

A Volume Resource instance can be deployed by applying the manifest file. But before creating a Volume Resource, ensure you have the following:

### **Appropriate Access Permission Use Case**

In DataOS, different actions require specific use cases that grant the necessary permissions to execute a task. You can grant these use cases directly to a user or group them under a tag, which is then assigned to the user. The following table outlines various actions related to Volume Resources and the corresponding use cases required:

| **Action** | **Required Use Cases** |
|------------|------------------------|
| Get        | Read Workspaces, Read Resources in User Specified Workspace / Read Resources in User Workspaces (for public and sandbox workspaces) |
| Create     | Create and Update Resources in User Workspace       |
| Apply      | Create and Update Resources in User Workspace          |
| Delete     | Delete Resources in User Workspace               |
| Log        | Read Resource Logs in User Workspace                 |

To assign use cases, you can either contact the DataOS Operator or create a Grant Request by creating a Grant Resource. The request will be validated by the DataOS Operator.

### **Create a manifest file**

To create a Volume Resource, data developers can define a set of attributes in a manifest file, typically in YAML format, and deploy it using the DataOS Command Line Interface (CLI) or API. Below is a sample manifest file for a Volume Resource:

???tip "Sample Volume manifest"

    ```yaml title="sample_volume.yml"
    --8<-- "examples/resources/volume/sample_volume.yml"
    ```

The manifest file for a Volume Resource consists of three main sections, each requiring specific configuration:

- [Resource Meta Section](#configuring-the-resource-meta-section): Contains attributes shared among all types of Resources.
- [Volume-Specific Section](#configuring-the-volume-specific-section): Includes attributes unique to the Volume Resource.

#### **Configuring the Resource meta section**

In DataOS, a Volume is categorized as a Resource type. The YAML configuration file for a Volume Resource includes a Resource meta section, which contains attributes shared among all Resource types.

The following YAML excerpt illustrates the attributes specified within this section:

=== "Syntax"

      ```yaml
      name: ${{resource_name}} # Name of the Resource (mandatory)
      version: v1beta # Manifest version of the Resource (mandatory)
      type: volume # Type of Resource (mandatory)
      tags: # Tags for categorizing the Resource (optional)
        - ${{tag_example_1}}
        - ${{tag_example_2}}
      description: ${{resource_description}} # Description (optional)
      owner: ${{resource_owner}} # Owner of the Resource (optional, default to user-id of user deploying the resource)
      layer: ${{resource_layer}} # DataOS Layer 
      ```
=== "Example"

      ```yaml
      name: my-first-volume # Name of the Resource
      version: v1beta # Manifest version of the Resource
      type: volume # Type of Resource
      tags: # Tags for categorizing the Resource
        - dataos:volume # Tags 
        - volume # Additional tags
      description: Common attributes applicable to all DataOS Resources
      owner: iamgroot
      layer: user
      ```

To configure a volume Resource, replace the values of `name`, `layer`, `tags`, `description`, and `owner` with appropriate values. For additional configuration information about the attributes of the Resource meta section, refer to the link: [Attributes of Resource meta section](/resources/manifest_attributes/).

#### **Configuring the Volume-specific section**

The Volume-specific section of a manifest file encompasses attributes specific to the Volume Resource.


=== "Configuration"

    === "Syntax"

          ```yaml
          volume:
            size: ${{size}}  #100Gi, 50Mi, 10Ti, 500Mi
            accessMode: ${{access_mode}}  #ReadWriteOnce, ReadOnlyMany.
            type: ${{type}}
          ```

    === "Example"

          ```yaml
          volume:
            size: 1Gi  #100Gi, 50Mi, 10Ti, 500Mi
            accessMode: ReadWriteMany  #ReadWriteOnce, ReadOnlyMany.
            type: temp
          ```


### **Apply the Volume manifest**

After creating the Volume manifest file, it's time to apply it to instantiate the Resource-instance in the DataOS environment. To apply the manifest file, utilize the  `apply`  command.

```shell
dataos-ctl resource apply -f ${{yaml config file path}} -w ${{workspace}}

# Sample
dataos-ctl resource apply -f /home/Desktop/my-volume.yaml -w curriculum
```

### **Verify Volume Creation**

To ensure that your Volume has been successfully created, you can verify it in two ways:

Check the name of the newly created Volume in the list of volumes created by you in a specific Workspace:

```shell
dataos-ctl get -t volume -w ${{workspace}}
```

Alternatively, retrieve the list of all volumes created in your organization:

```shell
dataos-ctl get -t volume -w ${{workspace}} -a
```

You can also access the details of any created Volume through the DataOS GUI in the [Operations App.](/interfaces/operations/)

### **Deleting Volumes**

Use the `delete` command to remove the specific Volume Resource-instance from the DataOS environment:

```shell
# METHOD 1
dataos-ctl delete -t volume -n ${{name of Volume}}
# Sample
dataos-ctl delete -t volume -n my-volume

# METHOD 2
dataos-ctl delete -i "${{identifier string for a resource}}"
# Sample 
dataos-ctl delete -i "my-volume | v1beta | volume | curriculum "
```


