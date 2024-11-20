# Deploy Lens in DataOS 

In this topic, you'll learn how to deploy your semantic model(Lens) in DataOS. This step ensures your model is accessible, reliable, and ready for real-time use, enabling stakeholders to derive insights and make data-driven decisions.

## Scenario

After thorough testing of your Lens model in a local environment, the next critical step is to deploy it to a production setting within DataOS. This process ensures that your model is accessible and reliable for broader usage, enabling stakeholders to leverage it for real-time data insights and decision-making.

## Prerequisites

Before diving into configuring Lens, make sure you have everything ready:

1. **Check required Permissions**: Some tasks require specific permissions typically assigned to DataOS Operators. Ensure you have access to one of the following permission sets either via use-cases or via tags:

    | **Access Permission (via use-cases)**       | **Access Permissions (via tags)**      |
    |--------------------------------------------|---------------------------------------|
    | Read Workspace                             | `roles:id:data-dev `                  |
    |Create Update and Delete Lens in user layer specified workspace| `roles:id:system-dev`  |
    | Read all secrets from Heimdall             |  `roles:id:operator`                                    |

2. **Check CLI installation and initialization**: You need this text-based interface that allows you to interact with the DataOS context via command prompts. Click [here](/interfaces/cli/) to learn more.

3. **Manage Credentials Securely**: Use **Instance Secrets** for storing your data source credentials, ensuring sensitive information remains protected.

    > **Important**: To prevent credential exposure, contact DataOS administrator and understand the best practices for handling sensitive data.

4. **Organize Your Code Repository**: Place Lens manifests in a private, permission-controlled repository to maintain security and compliance. 

## Steps

You follow the below steps to deploy a Lens on DataOS.


### **Step 1: Push the Lens model directory to a code repository**

You first push your Lens model directory to a hosted code repository such as [Bitbucket](https://support.atlassian.com/bitbucket-cloud/docs/push-code-to-bitbucket/), [GitHub](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github), [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/getting-started.html), etc.

<aside class="callout">
🗣️ If your code repository is private, you must create Instance Secrets with your repository credentials for later use during deployment. Public code repositories do not require Step 2. However, we recommend keeping your repository private to secure your API Keys.

</aside>

### **Step 2: Create Instance Secrets for code repository credentials**

Create and configure an Instance Secret to secure your code repository credentials. This involves the following steps:

**Create an Instance Secret manifest file**

Define the Instance Secret Resource in a YAML file. Below is a template you can use for Bitbucket, substituting `${USERNAME}` and `${PASSWORD}` with your actual Bitbucket credentials:

```yaml
# RESOURCE META SECTION
name: bitbucket-r # Secret Resource name (mandatory)
version: v1 # Secret manifest version (mandatory)
type: instance-secret # Type of Resource (mandatory)
description: Bitbucket read secrets for code repository # Secret Resource description (optional)
layer: user # DataOS Layer (optional)

# INSTANCE SECRET-SPECIFIC SECTION
instance-secret: 
  type: key-value # Type of Instance-secret (mandatory)
  acl: r # Access control list (mandatory)
  data: # Data (mandatory)
    GITSYNC_USERNAME: iamgroot
    GITSYNC_PASSWORD: <git_token>
```

**Apply the Instance Secret manifest**

Deploy the Instance Secret to DataOS using the `apply` command.

<aside class="callout">
🗣️ When applying the manifest file for Instance-secret from CLI, ensure you don't specify Workspace as Instance Secret is a [Instance-level Resource](/resources/types/#instance-level-resources).

</aside>

You apply the manifest file as follows:

```bash
dataos-ctl apply -f ./lens/instance_secret.yml
# Expected output
INFO[0000] 🛠 apply...                                   
INFO[0000] 🔧 applying bitbucket-r:v1:instance-secret... 
INFO[0001] 🔧 applying bitbucket-r:v1:instance-secret...created 
INFO[0001] 🛠 apply...complete
```

<aside class="callout">
🗣️ Make a note of the name of the created `Instance Secret`, as it will be required in the secrets attribute section of the Lens manifest file. This name is essential for ensuring proper configuration and access within your Lens environment.
</aside>

### **Step 3: Create a Lens Resource manifest file**

You  begin by creating a manifest file that holds the configuration details for your Lens Resource. The structure of the Lens manifest file is provided below.

The manifest file of a Lens can be broken down into two sections:

1. Resource meta section
2. Lens-specific section

<aside class="callout">
🗣️ In DataOS, a Lens is categorized as a Resource type. The YAML configuration file for a Lens Resource includes a Resource meta section, which contains attributes shared among all Resource types.
</aside>

The following YAML excerpt illustrates the attributes specified within this section:

To configure a lens Resource, replace `name`, `layer`, `tags`, `description`, and `owner` values with appropriate values. For additional configuration information about the attributes of the Resource meta section, refer to the link: [Attributes of Resource meta section](/resources/manifest_attributes/).

**Lens manifest file**

```yaml
# RESOURCE META SECTION
name: cross-sell-affinity # Lens Resource name (mandatory)
version: v1alpha # Lens manifest version (mandatory)
layer: user # DataOS Layer (optional)
type: lens # Type of Resource (mandatory)
tags: # Tags (optional)
  - lens
description: This data model provides comprehensive insights for cross-sell and product affinity analysis. # Lens Resource description (optional)

# LENS-SPECIFIC SECTION
lens:
  compute: runnable-default # Compute Resource that Lens should utilize (mandatory)
  secrets: # Referred Instance-secret configuration (**mandatory for private code repository, not required for public repository)
    - name: bitbucket-cred # Referred Instance Secret name (mandatory)
      allKeys: true # All keys within the secret are required or not (optional)
      
# Data Source configuration      
  source: 
    type: minerva # Source type (optional)
    name: system # Source name (optional)
    catalog: icebase # Catalog name for Minerva or Themis (optional)
  repo: # Lens model code repository configuration (mandatory)
    url: https://bitbucket.org/tmdc/dataproducts # URL of repository containing the Lens model (mandatory)
    lensBaseDir: dataproducts/setup/resources/lens2/model # Relative path of the Lens 'model' directory in repository (mandatory)
    syncFlags: # Additional flags used during synchronization (optional)
      - --ref=main # Repository Branch (optional)

# API Instances configuration
  api:  (optional)
    replicas: 1 # Number of API instance replicas (optional)
    logLevel: info # Logging granularity (optional)
    resources: # CPU and memory configurations for API Instances (optional)
      requests:
        cpu: 100m
        memory: 256Mi
      limits:
        cpu: 1000m
        memory: 1048Mi

# Worker configuration
  worker:  (optional)
    replicas: 1 # Number of Worker replicas (optional)
    logLevel: debug # Logging level for Worker (optional)
    resources: # CPU and memory configurations for Worker (optional)
      requests:
        cpu: 100m
        memory: 256Mi
      limits:
        cpu: 1000m
        memory: 1248Mi

# Router configuration

  router:  (optional)
    logLevel: info # Level of log detail for Router (optional)
    resources: # CPU and memory resource specifications for the router (optional)
      requests:
        cpu: 100m
        memory: 256Mi
      limits:
        cpu: 1000m
        memory: 2548Mi

# Iris configuration 
  iris: (optional)
    logLevel: info # Log level for Iris (optional)
    resources: # CPU and memory resource specifications for the iris board (optional)
      requests:
        cpu: 200m
        memory: 256Mi
      limits:
        cpu: 1600m
        memory: 2240Mi
# Metric configuration 
  metric: (optional)
    logLevel: info # Log level for metrics (optional)
```

A typical deployment of a Lens Resource includes the following components:

| **Section** | **Description** |
| --- | --- |
| **Source** | Defines the configuration of the data source for data processing and querying. |
| **Repo** | Outlines the configuration of the code repository where the model used by Lens resides. |
| **API** | Configures an API service that processes incoming requests, connecting to the database for raw data. A single instance is provisioned by default, but the system can auto-scale to add more instances based on workload demands, with a recommendation of one instance for every 5-10 requests per second. |
| **Worker** | When `LENS2_REFRESH_WORKER` is set to true, a Refresh Worker manages and refreshes the memory cache in the background, keeping refresh keys for all data models up-to-date. It invalidates the in-memory cache but does not populate it, which is done lazily during query execution. |
| **Router** | Configures a Router Service responsible for receiving queries from Lens, managing metadata, and handling query planning and distribution to the workers. Lens communicates only with the Router, not directly with the workers. |
| **Iris** | Manages interaction with Iris dashboards. |
| **Metrics** | Populates the metrics in the metric section of the Data Product Hub. |

For more information on how to configure a Lens manifest file, refer to the link: [Configuration Fields of the Deployment Manifest File for Lens Resource](/resources/lens/lens_manifest_attributes/)

### **Step 4: Apply the Lens Resource manifest file**

Apply the Lens manifest file using the `apply` command as shownn below, or reference the Lens manifest path in the Bundle Resource along with other Resources.

```shell
dataos-ctl apply -f /home/data_product/resources/lens/deployment.yaml #path
```