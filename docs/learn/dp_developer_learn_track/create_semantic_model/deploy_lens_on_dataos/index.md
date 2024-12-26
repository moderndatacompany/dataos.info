# Deploy Lens in DataOS 

In this topic, you'll learn how to deploy your semantic model (Lens) in DataOS. This step ensures your model is accessible, reliable, and ready for real-time use, enabling stakeholders to derive insights and make data-driven decisions.

## Scenario

After thorough testing of your semantic model (Lens) in a local environment, the next critical step is to deploy it in DataOS. This process ensures that your model is accessible and reliable for broader usage, enabling stakeholders to leverage it for real-time data insights and decision-making.

## Prerequisites

Before diving into configuring Lens, make sure you have everything ready:

1. **Check required Permissions**: Some tasks require specific permissions typically assigned to DataOS Operators. Ensure you have access to one of the following permission sets either via use-cases or via tags:

    | **Access Permission (via use-cases)**       | **Access Permissions (via tags)**      |
    |--------------------------------------------|---------------------------------------|
    | Read Workspace                             | `roles:id:data-dev `                  |
    |Create Update and Delete Lens in user layer specified workspace| `roles:id:system-dev`  |
    | Read all secrets from Heimdall             |                                      |

2. **Check CLI installation and initialization**: You need this text-based interface that allows you to interact with the DataOS context via command prompts. Click [here](/interfaces/cli/) to learn more.

3. **Manage Credentials Securely**: Use **Instance Secrets** for storing your data source credentials, ensuring sensitive information remains protected.

    > **Important**: To prevent credential exposure, contact DataOS administrator and understand the best practices for handling sensitive data.

4. **Organize Your Code Repository**: Place Lens manifests in a private, permission-controlled repository to maintain security and compliance. 

## Steps

You follow the below steps to deploy Lens on DataOS.


### **Step 1: Prepare the semantic model folder in the Data Product directory**

The semantic model is organized within the `build/semantic_model` directory of the Data Product. You don’t need to push the semantic model individually. Instead, you will push the entire Data Product directory, which includes the semantic model, to a code repository such as [GitHub](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github), [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/getting-started.html), or [Bitbucket](https://support.atlassian.com/bitbucket-cloud/docs/push-code-to-bitbucket/), once all the Data Product Resources are prepared. This ensures that the Lens, along with all Data Product Resources (such as Talos), is included in the overall deployment, with proper synchronization for version tracking and collaboration.

The following structure illustrates how the Lens will be organized within the Data Product directory.

```jsx
build/                          # resources folder in dp
├── semantic_model/                           # Lens  folder
│   ├── deployment.yaml             # Deployment file for Lens
│   ├── model/                      # Lens model folder
│   │   ├── sql/                    # SQL files for the Lens model
│   │   ├── tables/                 # Tables used in the Lens model
│   │   ├── views/                  # Views defined for the Lens model
│   │   └── user_groups.yml         # User groups for access control
```

<aside class="callout">
🗣️ If your code repository is private, you must create Instance Secrets with your repository credentials for later use during deployment. Public code repositories do not require Step 2. However, we recommend keeping your repository private to secure your API Keys.

</aside>

### **Step 2: Create Instance Secrets for code repository credentials**

To secure your code repository credentials, you need to create and configure an Instance Secret. This secret is necessary because the Lens deployment file contains Git/Bitbucket credentials and repo address to fetch all Lens artifacts. To create and configure an Instance Secret follow the below steps:

**a.** **Create an Instance Secret manifest file**

Define the Instance Secret Resource in a YAML file. Below is a template you can use for Bitbucket and Github, substituting `${USERNAME}` and `${PASSWORD}` with your actual credentials of Bitbucket or Github:

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
    GITSYNC_PASSWORD: <GIT_TOKEN>
```

**b.** **Apply the Instance Secret manifest**

Deploy the Instance Secret to DataOS using the `apply` command.

<aside class="callout">
🗣️ When applying the manifest file for Instance-secret from CLI, ensure you don't specify Workspace as Instance Secret is a <a href="/resources/types/#instance-level-resources">Instance-level Resource</a>.

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
🗣️ Make a note of the name of the created `Instance Secret`, as it will be required in the secrets attribute section of the Lens manifest file. This name is essential for ensuring proper configuration and access within your Lens.
</aside>

### **Step 3: Create Lens manifest file**

You  begin by creating a manifest file that holds the configuration details for your Lens. The structure of the Lens manifest file is provided below.

The manifest file of Lens can be broken down into two sections:

1. Resource meta section
2. Lens-specific section

<aside class="callout">
🗣️ In DataOS, Lens is categorized as a Resource type. The YAML configuration file for Lens includes a Resource meta section, which contains attributes shared among all Resource types.
</aside>

The following YAML excerpt illustrates the attributes specified within this section:

To configure Lens, replace `name`, `layer`, `tags`, `description`, and `owner` values with appropriate values. For additional configuration information about the attributes of the Resource meta section, refer to the link: [Attributes of Resource meta section](/resources/manifest_attributes/).

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
  api:  #(optional)
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
  worker:  #(optional)
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

  router:  #(optional)
    logLevel: info # Level of log detail for Router (optional)
    resources: # CPU and memory resource specifications for the router (optional)
      requests:
        cpu: 100m
        memory: 256Mi
      limits:
        cpu: 1000m
        memory: 2548Mi

# Iris configuration 
  iris: #(optional)
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

A typical deployment of Lens includes the following components:

| **Section** | **Description** |
| --- | --- |
| **Source** | Specifies the source configuration from which the Lens will be mapped. The Lens support the depot, themis, minerva and flash as source. |
| **Repo** | Outlines the configuration of the code repository where the model used by Lens resides. |
| **API** | Configures an API service that processes incoming requests, connecting to the database for raw data. A single instance is provisioned by default, but the system can auto-scale to add more instances based on workload demands, with a recommendation of one instance for every 5-10 requests per second. |
| **Worker** | When `LENS2_REFRESH_WORKER` is set to true, a Refresh Worker manages and refreshes the memory cache in the background, keeping refresh keys for all data models up-to-date. It invalidates the in-memory cache but does not populate it, which is done lazily during query execution. |
| **Router** | Configures a Router Service responsible for receiving queries from Lens, managing metadata, and handling query planning and distribution to the workers. Lens communicates only with the Router, not directly with the workers. |
| **Iris** | Manages interaction with Iris dashboards. |
| **Metrics** | Populates the metrics in the metric section of the Data Product Hub. |


For more information on how to configure Lens manifest file, refer to the link: [Configuration Fields of the Deployment Manifest File for Lens](/resources/lens/lens_manifest_attributes/)

### **Step 4: Apply the Lens manifest file**

Apply the Lens manifest file using the `apply` command as shown below, or reference the Lens manifest path in the Bundle Resource along with other Resources.

```shell
dataos-ctl apply -f /home/data_product/resources/lens/deployment.yaml #path
```