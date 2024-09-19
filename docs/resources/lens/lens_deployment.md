# Deploying Lens model on DataOS 

!!! abstract "Quick Guide"
    To quickly get started with lens deployment follow the [quick guide on deploying your Lens model](/quick_guides/deploy_data_model/) to walk through the process. This guide ensures a smooth and secure deployment, helping you get your Lens Resource up and running quickly.

This guide provides instructions for setting up Lens in the DataOS environment, importing an existing Lens project from a local machine using SSH, utilizing version control tools such as Bitbucket or Git for seamless CI/CD integration.

## Pre-requisites

Before initiating the deployment process, please ensure you have the following:

- A directory containing Lens model.
- Access to a hosted code repository, such as **Bitbucket**, **GitHub**, **AWS CodeCommit**, etc.
- Operator level access permission

>If you are new to setting the Lens model directory refer to the detailed doc [here](/resources/lens/lens_setup/).

## Deployment Process

Follow the steps below to deploy Lens on DataOS:

### **Step 1: Push the Lens model directory to a code repository**

**Pushing to a public code repository**

First, push your Lens model directory to a hosted code repository. This can be done on hosted code repository like [Bitbucket](https://support.atlassian.com/bitbucket-cloud/docs/push-code-to-bitbucket/), [GitHub](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github), [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/getting-started.html) etc.


<aside class="callout">
🗣 If your code repository is private, you will need to create <b>Instance Secrets</b> with your repository credentials for later use during deployment. Public code repositories do not require Step 2.
</aside>

### **Step 2: Create Instance Secrets for Code Repository Credentials**

Create and configure an Instance Secret to secure your code repository credentials. This involves the following steps:

**Create an Instance Secret manifest file**

Define the Instance Secret Resource in a YAML file. Below is a template you can use for Bitbucket, substituting `${USERNAME}` and `${PASSWORD}` with your actual Bitbucket credentials:

=== "Syntax"

    ```yaml
    # RESOURCE META SECTION
    name: ${bitbucket-r }# Secret Resource name (mandatory)
    version: v1 # Secret manifest version (mandatory)
    type: instance-secret # Type of Resource (mandatory)
    description: Bitbucket read secrets for code repository # Secret Resource description (optional)
    layer: user # DataOS Layer (optional)

    # INSTANCE SECRET-SPECIFIC SECTION
    instance-secret: 
      type: key-value # Type of Instance-secret (mandatory)
      acl: r # Access control list (mandatory)
      data: # Data (mandatory)
        GITSYNC_USERNAME: ${USERNAME}
        GITSYNC_PASSWORD: ${PASSWORD}
    ```

=== "Example"

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

Deploy the Instance Secret to DataOS using the `apply` command.

<aside class="callout">
🗣 When applying the manifest file for Instance-secret from CLI, make sure you don't specify Workspace as Instance Secrets are <a href="https://dataos.info/resources/types/#instance-level-resources" target="_blank">Instance-level Resource</a>.
</aside>


The `apply` command is as follows:

=== "Command"

    ```bash
    dataos-ctl resource apply -f ${manifest-file-path}
    ```

    Alternatively, you can also use the below command:

    ```bash
    dataos-ctl apply -f ${manifest-file-path}
    ```

    Replace `${manifest-file-path}` with the path to your YAML file.

=== "Example"

    ```bash
    dataos-ctl resource apply -f ./lens/instance_secret.yml
    # Expected output
    INFO[0000] 🛠 apply...                                   
    INFO[0000] 🔧 applying bitbucket-r:v1:instance-secret... 
    INFO[0001] 🔧 applying bitbucket-r:v1:instance-secret...created 
    INFO[0001] 🛠 apply...complete 
    ```

**Verify Instance-secret creation**

To validate the proper creation of the Instance Secret Resource within the DataOS environment, employ the `get` command. Execute the following commands to ascertain the existence of the Instance Secret Resource:

To get the details of Instance-secret created by the user who applies the Instance-secret, use the following command:

=== "Command"
      
    ```bash
    dataos-ctl resource get -t instance-secret
    ```
      
    Alternatively, you can also use the below command.
      
    ```bash
    dataos-ctl get -t instance-secret
    ```
    
=== "Example"
    
    ```bash
    dataos-ctl get -t instance-secret
    # Expected Output
    INFO[0000] 🔍 get...                                     
    INFO[0000] 🔍 get...complete                             
    
                NAME           | VERSION |      TYPE       | WORKSPACE | STATUS | RUNTIME |   OWNER          
    ---------------------------|---------|-----------------|-----------|--------|---------|-----------------------
      bitbucket-r              | v1      | instance-secret |           | active |         | iamgroot  
    ```
    
To get the details of Instance-secret created by all the users within the DataOS Instance, use the above command with `-a` flag:

=== "Command"
    
    ```bash
    dataos-ctl resource get -t instance-secret -a
    ```
    
    Alternatively, you can use the following command:
    
    ```bash
    dataos-ctl get -t instance-secret -a
    ```
    
=== "Example"

    ```shell
    dataos-ctl get -t instance-secret -a

    # Expected Output
    INFO[0000] 🔍 get...                                     
    INFO[0000] 🔍 get...complete                             

                NAME           | VERSION |      TYPE       | WORKSPACE | STATUS | RUNTIME |        OWNER          
    ---------------------------|---------|-----------------|-----------|--------|---------|-----------------------
      abfss-r                  | v1      | instance-secret |           | active |         | thor          
      gcsdepot-r               | v1      | instance-secret |           | active |         | ironman            
      bitbucket-r              | v1      | instance-secret |           | active |         | iamgroot  
    ```

<aside class="callout">
🗣 Ensure that you remember the name of the created <b>Instance secret</b>, as it will be used in the secrets attribute section of the Lens manifest file. This name is crucial for proper configuration and access within your Lens environment.

</aside>

### **Step 3: Create a Lens Resource manifest file**

Begin by creating a manifest file that will hold the configuration details for your Lens Resource. The structure of the Lens manifest file is provided below.

???tip "Sample Lens manifest"

    ```yaml
    --8<-- "/examples/lens/sample_lens_manifest.yml"
    ```

The manifest file of a Lens can be broken down into two sections:

1. Resource meta section
2. Lens-specific section

### **Resource-meta Section**

In DataOS, a Lens is categorized as a Resource type. The YAML configuration file for a Lens Resource includes a Resource meta section, which contains attributes shared among all Resource types.

The following YAML excerpt illustrates the attributes specified within this section:


=== "Syntax"

      ```yaml
      name: ${{resource_name}} # Name of the Resource (mandatory)
      version: v1alpha # Manifest version of the Resource (mandatory)
      type: lens # Type of Resource (mandatory)
      tags: # Tags for categorizing the Resource (optional)
        - ${{tag_example_1}} 
        - ${{tag_example_2}} 
      description: ${{resource_description}} # Description (optional)
      owner: ${{resource_owner}} # Owner of the Resource (optional, default value: user-id of user deploying the resource)
      layer: ${{resource_layer}} # DataOS Layer (optional, default value: user)
      lens: # lens-specific Section
        ${{Attributes of lens-specific Section}}
      ```
=== "Example"

      ```yaml
      name: my-first-lens # Name of the Resource
      version: v1alpha # Manifest version of the Resource
      type: lens # Type of Resource
      tags: # Tags for categorizing the Resource
        - dataos:lens 
        - lens 
      description: Common attributes applicable to all DataOS Resources # Description
      owner: iamgroot # Owner of the Resource
      layer: user # DataOS Layer
      lens: 
        # .... 
      ```

To configure a lens Resource, replace the values of `name`, `layer`, `tags`, `description`, and `owner` with appropriate values. For additional configuration information about the attributes of the Resource meta section, refer to the link: [Attributes of Resource meta section](/resources/manifest_attributes/).

### **Lens-specific section**

A typical deployment of a Lens Resource includes the following components:

| Section  | Description |
|----------|-------------|
| **Source** | Defines the configuration of the data source for data processing and querying. |
| **Repo**   | Outlines the configuration of the code repository where the model used by Lens resides. |
| **API**    | Configures an API service that processes incoming requests, connecting to the database for raw data. A single instance is provisioned by default, but the system can auto-scale to add more instances based on workload demands, with a recommendation of one instance for every 5-10 requests per second. |
| **Worker** | When `LENS2_REFRESH_WORKER` is set to true, a Refresh Worker manages and refreshes the memory cache in the background, keeping refresh keys for all data models up-to-date. It invalidates the in-memory cache but does not populate it, which is done lazily during query execution. |
| **Router**  | Configures a Router Service responsible for receiving queries from Lens, managing metadata, and handling query planning and distribution to the workers. Lens communicates only with the Router, not directly with the workers. |

For more information on how to configure a Lens manifest file, refer to the link: [Configuration Fields of the Deployment Manifest File (YAML) for Lens Resource](/resources/lens/lens_manifest_attributes/)

### **Step 4: Apply the manifest file of Lens Resource using DataOS CLI**

Deploy the Lens model to DataOS using the `apply` command.

<aside class="callout"> 

When applying the manifest file from the DataOS CLI, make sure you specify the Workspace as Lens is a <a href="https://dataos.info/resources/types/#workspace-level-resources" target="blank"> Workspace-level Resource</a>.

</aside>

The `apply` command is as follows:

=== "Command"

    ```bash
    dataos-ctl resource apply -f ${manifest-file-path} -w ${workspace}
    ```
    
    Alternatively, you can also use the below command:
    
    ```bash
    dataos-ctl apply -f ${manifest-file-path} -w ${workspace}
    ```
    
    Replace `${manifest-file-path}` with the path to your Lens manifest file, and `${workspace}` with the name of the Workspace.

=== "Example"
 
    ```bash
    dataos-ctl resource apply -f ./lens/lens.yml -w curriculum
    # Expected output
    INFO[0000] 🛠 apply...                                   
    INFO[0000] 🔧 applying(curriculum) sales360:v1alpha:lens... 
    INFO[0001] 🔧 applying(curriculum) sales360:v1alpha:lens...created 
    INFO[0001] 🛠 apply...complete 
    ```


### **Step 5: Validate Lens Resource creation**

To validate the proper creation of the Lens Resource within the DataOS environment, employ the `get` command. Execute the following commands to ascertain the existence of the Lens Resource:
 
 - To get the details of the Lens created by the user who applies the Lens, use the following command:
     
     ```bash
     dataos-ctl resource get -t lens -w ${workspace}
     ```
     
     Alternatively, you can also use the below command.
     
     ```bash
     dataos-ctl get -t lens -w ${workspace}
     ```
     
     Example
     
     ```bash
     dataos-ctl get -t lens -w curriculum
     # Expected Output
     INFO[0000] 🔍 get...                                     
     INFO[0000] 🔍 get...complete                             
     
           NAME     | VERSION | TYPE | WORKSPACE  | STATUS | RUNTIME |    OWNER     
     ---------------|---------|------|------------|--------|---------|--------------
         sales360   | v1alpha | lens | curriculum | active |         |  iamgroot
     ```
     
 - To get the details of Lens created by all the users within the DataOS Instance, use the above command with `-a` flag:
     
     ```bash
     dataos-ctl resource get -t lens -w ${workspace} -a
     ```
     
     Alternatively, you can use the following command:
     
     ```bash
     dataos-ctl get -t lens -w ${workspace} -a
     ```
     
     Example
     
     ```bash
     dataos-ctl get -t lens -w curriculum -a
     # Expected Output
     INFO[0000] 🔍 get...                                     
     INFO[0000] 🔍 get...complete                             
     
           NAME      | VERSION | TYPE | WORKSPACE  | STATUS | RUNTIME |    OWNER     
     ----------------|---------|------|------------|--------|---------|--------------
         sales360    | v1alpha | lens | curriculum | active |         |  iamgroot
         customer360 | v1alpha | lens | curriculum | active |         |  thor
     ```

## Next Step

Exploration of Deployed Lens:

- [Exploration of deployed Lens using SQL APIs](/resources/lens/exploration_of_deployed_lens_using_sql_apis/)
- [Exploration of deployed Lens using Python](/resources/lens/exploration_of_deployed_lens_using_python/)
- [Exploration of deployed Lens using REST APIs](/resources/lens/exploration_of_deployed_lens_using_rest_apis/)
- [Exploration of deployed Lens using GraphQL](/resources/lens/exploration_of_deployed_lens_using_graphql/)