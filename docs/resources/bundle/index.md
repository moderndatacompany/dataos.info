---
title: Bundle
search:
  boost: 2
---

# :resources-bundle: Bundle

A Bundle [Resource](/resources/) within DataOS serves as a declarative and standardized mechanism for deploying a collection of Resources, Data Products, or applications in a single operation. It empowers data developers with the capability to programmatically orchestrate the deployment, scheduling, creation, and dismantling of code and infrastructure resources linked to these Data Products and applications in a unified manner. 

As implied by its name, the Bundle Resource aggregates various [DataOS Resources](/resources/) into a flattened directed acyclic graph (DAG). Within this structure, each node represents a distinct DataOS Resource, interconnected through dependency relationships.

<aside class="callout">

🗣 A Bundle is an <a href="/resources/types/#instance-level-resources">Instance-level</a> Resource in DataOS, while the Resources present within the Bundle can be either <a href="/resources/types/#workspace-level-resources">Workspace-level</a> or <a href="/resources/types/#instance-level-resources">Instance-level</a>.

</aside>

## Why use a Bundle?

### **End-to-End Definition**

The manifest file of the Bundle can be used to define the logical quantum for a Data Product - it encompasses the ‘code’ part of a ‘Data Product’. It collectively provides a comprehensive definition of a Data Product or application. This representation simplifies the application of software engineering best practices, including source control, code review, testing, and continuous integration/continuous deployment (CI/CD) processes.

### **Streamlined Deployment**

The Bundle eliminates fragmented deployment and validation procedures, enabling robust configuration management across multiple Workspaces and cloud environments. By referencing a Bundle Resource in the Data Product manifest, all related resources are orchestrated and deployed together, ensuring consistency and efficiency across the entire Data Product lifecycle.

For example, a pipeline of data-related tasks can be created where a Depot (a connection) is established, data is ingested using Flare, and quality checks are performed on the ingested data. All of these Resources, representing different stages of the pipeline, are included in a single Bundle. This Bundle must then be referenced in the Data Product manifest file, ensuring that the entire pipeline—covering data ingestion, quality checks, and connections—is seamlessly orchestrated and deployed as a unified entity.


## Structure of a Bundle YAML manifest

The YAML manifest outlined below details the structure of a Bundle:

```yaml
# Resource meta section
name: ${{my-bundle}}
version: v1alpha 
type: bundle
layer: user 
tags: 
  - ${{dataos:type:resource}}
  - ${{dataos:resource:bundle}}
description: ${{this bundle resource is for a data product}}
owner: ${{iamgroot}}

# Bundle-specific section
bundle:

  # Bundle Schedule section
  schedule:
    initialState: ${{initial state}}
    timezone: ${{time zone}}
    create:
      cron: ${{cron expression}}
    delete:
      cron: ${{cron expression}}

  # Bundle Workspaces section
  workspaces:
    - name: ${{bundlespace}} # Workspace name (mandatory)
      description: ${{this is a bundle workspace}} # Workspace description (optional)
      tags: # Workspace tags (optional)
        - ${{bundle}}
        - ${{myworkspace}}
      labels: # Workspace labels (optional)
        ${{purpose: testing}}
      layer: user # Workspace layer (mandatory)

  # Bundle Resources section
  resources:
    - id: ${{bundle-scanner}} # Resource ID (mandatory)
      workspace: ${{bundlespace}} # Workspace (optional)
      spec: # Resource spec (mandatory) 
        ${{resource spec manifest}}
      file: ${{/home/Desktop/bundle-scanner.yaml}} # Resource spec file (optional)
      dependencies: # Resource dependency (optional)
        - ${{bundle-depot}}
      dependencyConditions: # Resource dependency conditions (optional)
        - resourceId: ${{bundle-depot}} # Resource ID (mandatory)
          status: # Status dependency condition (optional)
            is: # Status is (optional)
              - ${{active}}
            contains: # Status contains (optional)
              - ${{activ}}
          runtime: # Runtime dependency condition (optional)
            is: # Runtime is (optional)
              - ${{running}}
            contains: # Runtime contains (optional)
              - ${{run}}

  # Additional properties section
  properties:
    ${{additional properties}}

  # Manage As User
  manageAsUser: ${{iamgroot}}
```

## How to create a Bundle?

Data developers can create a Bundle Resource by creating a YAML manifest and applying it via the [DataOS CLI.](https://dataos.info/interfaces/cli/)

### **Create a Bundle YAML manifest**

A Bundle Resource YAML manifest can be structurally broken down into following sections:

#### **Configure the Resource meta section**

In DataOS, a Bundle is categorized as a [Resource-type](/resources/types/). The Resource meta section within the YAML manifest encompasses attributes universally applicable to all Resource-types. The provided YAML codeblock elucidates the requisite attributes for this section: 

```yaml
# Resource meta section
name: ${{my-bundle}} # Resource name (mandatory)
version: v1beta # Manifest version (mandatory)
type: bundle # Resource-type (mandatory)
tags: # Resource Tags (optional)
  - ${{dataos:type:resource}}
  - ${{dataos:resource:bundle}}
description: ${{This is a bundle yaml manifest}} # Resource Description (optional)
owner: ${{iamgroot}} # Resource Owner (optional)
bundle: # Bundle-specific section mapping(mandatory)
  ${{Attributes of Bundle-specific section}}
```

For more information, refer to the [Attributes of Resource Meta Section.](/resources/manifest_attributes/)

#### **Configure the Bundle-specific section**

The Bundle-specific section contains attributes specific to the Bundle Resource. This section comprises of four high-level sections:

- Schedule
- Workspaces
- Bundle Resources
- Additional Properties

Each of these sections should be appropriately configured when creating a Bundle YAML manifest. The high-level structure of the various separate sections within the Bundle-specific section is provided in the YAML below:

```yaml
bundle:
  schedule: # Bundle schedule section (optional)
    ${{attributes for scheduling the bundle}}
  workspaces: # Bundle workspaces section (optional)
    ${{attributes specific to workspace configuration}}
  resources: # Bundle resources section (mandatory)
    ${{attributes specific to bundle resources}}
  properties: # Addtional Properties (optional)
    ${{additional properties}}
  manageAsUser: ${{iamgroot}} # Manage As User (optional)
```

<center>

| Attribute | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| [`bundle`](/resources/bundle/configurations/#bundle) | mapping | none | none | mandatory |
| [`schedule`](/resources/bundle/configurations/#schedule) | mapping | none | none | optional |
| [`workspaces`](/resources/bundle/configurations/#workspaces)| list of mappings | none | none | optional |
| [`resources`](/resources/bundle/configurations/#resources) | list of mappings | none | none | optional |
| [`properties`](/resources/bundle/configurations/#properties) | mapping | none | none | optional |
| [`manageAsUser`](/resources/bundle/configurations/#manageasuser) | string | UserID of Owner | UserID of use case assignee | optional |

</center>

**Bundle Schedule section**

The Bundle Schedule section allows you to specify scheduling attributes for the Bundle Resource. You can schedule the creation or deletion of a Bundle at specific intervals using a cron-like schedule. The following YAML code block outlines the attributes specified in the Bundle Workspaces section:

```yaml
bundle: # Bundle-specific section (mandatory)
  schedule: # Bundle Schedule section (optional)
    initialState: ${{create}} # Initial State of Bundle (mandatory)
    timezone: ${{Asia/Kolkata}} # Time Zone (mandatory)
    create: # Bundle creation cron (optional)
      - cron: ${{'5 0 24 1 *'}}
    delete: # Bundle deletion cron (optional)
      - cron: ${{'25 0 24 1 *'}}
```

Refer to the table below for a summary of the attributes within the Bundle Workspaces section. For detailed information about each attribute, please refer to the respective links provided in the attribute column.

<center>

| Attribute | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| [`initialState`](/resources/bundle/configurations/#initialState) | string | none | create/delete | mandatory |
| [`timezone`](/resources/bundle/configurations/#timezone) | string | none | valid timezone in the “Area/Location” format | mandatory |
| [`create`](/resources/bundle/configurations/#create) | list of mappings | none | none | optional |
| [`cron`](/resources/bundle/configurations/#cron) | string | none | valid cron expression | mandatory |
| [`delete`](/resources/bundle/configurations/#delete) | list of mappings | none | none | optional |

</center>

**Bundle Workspaces section**

Within a Bundle, you have the option to deploy Workspace-level Resources in a new Workspace. To achieve this, you must declare the specifications of this new Workspace and reference it within the corresponding DataOS Workspace-level Resource within the Bundle Resources section. 

<aside class="callout">

🗣 The Workspaces specified within a Bundle does not dictate the location of Bundle creation. Instead, it pertains to the Workspace designated to encompass all <a href="/resources/types/#workspace-level-resources">Workspace-level Resources</a> (such as <a href="/resources/workflow/">Workflow</a>, <a href="/resources/service/">Service</a>, <a href="/resources/worker/">Worker</a>, <a href="/resources/secret/">Secret</a>, Database, <a href="/resources/lakehouse/">Lakehouse</a> and <a href="/resources/cluster/">Cluster</a>) housed within the Bundle.

It is noteworthy that the Workspace-level Resources present in a Bundle can also be instantiated within other Workspaces, not necessarily that was created using the Bundle. But, the <a href="/resources/types/#instance-level-resources">Instance-level Resources</a>, irrespective of their presence within a Bundle, such as <a href="/resources/depot/">Depot</a>, <a href="/resources/policy/">Policy</a>, <a href="/resources/compute/">Compute</a>, <a href="/resources/stacks/">Stacks</a>, Instance-Secret, <a href="/resources/operator/">Operator</a>, or even another Bundle, maintain their instance-level scope and are not constrained to a specific Workspace.

</aside>

The following YAML code block outlines the attributes specified in the Bundle Workspaces section:

```yaml
bundle: # Bundle-specific section (mandatory)
  workspaces: # Bundle Workspaces section (optional)
    - name: ${{bundlespace}} # Workspace name (mandatory)
      description: ${{this is a bundle workspace}} # Workspace description (optional)
      tags: # Workspace tags (optional)
        - ${{bundle}}
        - ${{myworkspace}}
      labels: # Workspace labels (optional)
        ${{purpose: testing}}
      layer: ${{user}} # Workspace layer (mandatory)
```

Refer to the table below for a summary of the attributes within the Bundle Workspaces section. For detailed information about each attribute, please refer to the respective links provided in the attribute column.

<center>

| Attribute | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| [`name`](/resources/bundle/configurations/#name) | string | none | valid Workspace name | mandatory |
| [`description`](/resources/bundle/configurations/#description) | string | none | any valid string | optional |
| [`tags`](/resources/bundle/configurations/#tags) | list of strings | none | any valid string | optional |
| [`labels`](/resources/bundle/configurations/#labels) | mapping | none | valid key-value pairs | optional |
| [`layer`](/resources/bundle/configurations/#layer) | string | none | user/system | mandatory |

</center>

**Bundle Resources section**

The Bundle Resources section allows you to define the Resources that make up the Data Product/application and their dependencies in the form of a flattened DAG. Each node within this DAG represents a Resource interconnected through a set of dependencies. Using the dependency and dependencyConditions, relationship and conditions can be specified such that resource only instantiates when the right dependency condition is met either the correct status and runtime, else it doesn’t. The following YAML code block outlines the attributes specified in the Bundle Workspaces section:

```yaml
bundle: # Bundle-specific section (mandatory)
  resources:
    - id: ${{bundle-scanner}} # Resource ID (mandatory)
      workspace: ${{bundlespace}} # Workspace (optional)
      spec: # Resource spec (mandatory) 
        ${{resource spec manifest}}
      file: ${{/home/Desktop/bundle-scanner.yaml}} # Resource spec file (optional)
      dependencies: # Resource dependency (optional)
        - ${{bundle-depot}}
      dependencyConditions: # Resource dependency conditions (optional)
        - resourceId: ${{bundle-depot}} # Resource ID (mandatory)
          status: # Status dependency condition (optional)
            is: # Status is (optional)
              - ${{active}}
            contains: # Status contains (optional)
              - ${{activ}}
          runtime: # Runtime dependency condition (optional)
            is: # Runtime is (optional)
              - ${{running}}
            contains: # Runtime contains (optional)
              - ${{run}}
```

Refer to the table below for a summary of the attributes within the Bundle Workspaces section. For detailed information about each attribute, please refer to the respective links provided in the attribute column.

<center>

| Attribute | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| [`id`](/resources/bundle/configurations/#id) | string | none | valid string | mandatory |
| [`workspace`](/resources/bundle/configurations/#workspace) | string | none | valid Workspace name | optional (Mandatory for Workspace-level Resources) |
| [`spec`](/resources/bundle/configurations/#spec) | mapping | none | valid Resource spec | optional |
| [`file`](/resources/bundle/configurations/#file) | string | none | valid Resource config file path | optional |
| [`dependencies`](/resources/bundle/configurations/#dependencies) | list of strings | none | Resource ids within the DAG except the current one | optional |
| [`dependencyConditions`](/resources/bundle/configurations/#dependencyConditions) | list of mappings | none | none | optional |
| [`resourceId`](/resources/bundle/configurations/#resourceId) | string | none | ID of dependent Resource | mandatory |
| [`status`](/resources/bundle/configurations/#status) | mapping | none | none | optional |
| [`is`](/resources/bundle/configurations/#is) | list of strings | none | none | optional |
| [`contains`](/resources/bundle/configurations/#contains) | list of strings | none | none | optional |
| [`runtime`](/resources/bundle/configurations/#runtime) | mapping | none | none | optional |

</center>

**Additional Properties section**

The Additional Properties section lets you include any additional key-value properties relevant to the Bundle Resource. The following YAML code block outlines the attributes specified in the additional properties section:

```yaml
bundle: # Bundle-specific section (mandatory)
	properties: # Additional properties section (optional)
		${{alpha: beta}}
		${{gamma: sigma}}
```

Refer to the table below for a summary of the attributes within the additional properties section. For detailed information about each attribute, please refer to the respective links provided in the attribute column.

<center>

| Attribute | Data Type | Default Value | Possible Value | Requirement |
| --- | --- | --- | --- | --- |
| [`properties`](/resources/bundle/configurations/#properties) | mapping | none | properties in the form of key-value pairs | optional |

</center>

Data developers can alter the customize the behaviour of Bundle Resources by configuring the sections and attributes as needed. For a detailed insights into the description and constraints of the attributes within the Bundle-specific section, please consult the 'Attributes of Bundle-specific Section' documentation page.

???tip "Sample Bundle YAML manifest"

    ```yaml title="monitor_manifest_structure.yml"
    --8<-- "examples/resources/bundle/sample_bundle.yml"
    ```


### **Apply the Bundle YAML**

After creating the Bundle YAML manifest, it's time to apply it to instantiate the Resource-instance in the DataOS environment. To apply the Bundle YAML file, utilize the  `apply`  command.

```shell
dataos-ctl apply -f ${{yaml config file path}}

# Sample
dataos-ctl apply -f /home/Desktop/my-bundle.yaml
```

### **Verify Bundle Creation**

To ensure that your Bundle has been successfully created, you can verify it in two ways:

Check the name of the newly created bundle in the list of bundles created by you:

```shell
dataos-ctl get -t bundle

# Expected Output
INFO[0000] 🔍 get...                                     
INFO[0000] 🔍 get...complete                             

       NAME     | VERSION |  TYPE  | WORKSPACE | STATUS | RUNTIME |  OWNER      
----------------|---------|--------|-----------|--------|---------|----------------
    my-bundle   | v1beta  | bundle |           | active |         | iamgroot 
```

Alternatively, retrieve the list of all bundles created in your organization:

```shell
dataos-ctl get -t bundle -a

# Expected Output
INFO[0000] 🔍 get...                                     
INFO[0000] 🔍 get...complete                             

       NAME     | VERSION |  TYPE  | WORKSPACE | STATUS | RUNTIME | OWNER      
----------------|---------|--------|-----------|--------|---------|----------------
    my-bundle   | v1beta  | bundle |           | active |         | iamgroot 
    bundle101   | v1beta  | bundle |           | active |         | thor
```

You can also access the details of any created Bundle through the DataOS GUI in the [Operations App.](/interfaces/operations/)

### **Deleting Bundles**

When a Bundle Resource is deleted, it triggers the removal of all resources associated with that Bundle, including Workspaces (if there are any specified within the Bundle definition). 

Before deleting the Bundle, you must delete all workloads or resources that are dependent on it. This step ensures that there are no dependencies left that could cause issues during deletion. Once it's done, use the `delete` command to remove the specific Bundle Resource-instance from the DataOS environment:

```shell
# METHOD 1
dataos-ctl delete -t bundle -n ${{name of bundle}}
# Sample
dataos-ctl delete -t bundle -n my-bundle

# METHOD 2
dataos-ctl delete -i "${{identifier string for a resource}}"
# Sample 
dataos-ctl delete -i "my-bundle | v1beta | bundle |      "
```

<aside class="callout">
🗣 When deleting a Bundle Resource, the order of resource deletion is reversed from the order of applying. This is done to ensure that resources with dependencies are not deleted before their dependencies, preventing errors or inconsistencies.

</aside>

## Bundle Templates

The Bundle templates serve as blueprints, defining the structure and configurations for various types of Bundles, making it easier for data developers to consistently deploy resources. To know more, refer to the link: [Bundle Templates](/resources/bundle/bundle_templates/).


## Bundle Command Reference

Here is a reference to the various commands related to managing Bundles in DataOS:

- **Applying a Bundle:** Use the following command to apply a Bundle using a YAML configuration file:
    
    ```shell
    dataos-ctl apply -f ${{yaml config file path}}
    ```
    
- **Get Bundle Status:** To retrieve the status of a specific Bundle, use the following command:
    
    ```shell
    dataos-ctl get -t bundle
    ```
    
- **Get Status of all Bundles:** To get the status of all Bundles within the current context, use this command:
    
    ```shell
    dataos-ctl get -t bundle -a
    ```
    
- **Generate Bundle JSON Schema:** To generate the JSON schema for a Bundle with a specific version (e.g., v1alpha), use the following command:
    
    ```shell
    dataos-ctl develop schema generate -t bundle -v v1alpha
    ```
    
- **Get Bundle JSON Resource Schema:** To retrieve the JSON schema for a Bundle Resource from Poros with a specific version (e.g., v1alpha), use the following command:
    
    ```shell
    dataos-ctl develop get resource -t bundle -v v1alpha
    ```
    
- **Delete Bundles:** To delete a specific bundle, you can use the below command
    
    ```shell
    dataos-ctl delete -t bundle -n ${{name of bundle}}
    ```
    

## Recipe

[Optmize Bundling of Resources in Data Product](/resources/bundle/recipe/bundling_resources_in_data_product/)