# Deploying Lens model on DataOS 

This guide provides instructions for setting up Lens in the DataOS environment, importing an existing Lens project from a local machine using SSH, and integrating it with your database, utilizing version control tools such as Bitbucket or Git for seamless CI/CD integration.

## Pre-requisites

Before initiating the deployment process, please ensure you have the following:

- A directory containing your Lens model.
- Access to a hosted code repository, such as **Bitbucket**, **GitHub**, **AWS CodeCommit**, etc.
- Operator level access permission

>If you are new to setting the Lens model directory refer to the detailed doc [here](/resources/lens/local_setup/).**

## Deployment Process

Follow the steps below to deploy Lens on DataOS:

### **Step 1: Push the Lens model directory to a code repository**

**Pushing to a public code repository**

First, push your local Lens model directory to a hosted code repository. This can be done on hosted code repository like [Bitbucket](https://support.atlassian.com/bitbucket-cloud/docs/push-code-to-bitbucket/), [GitHub](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github), [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/getting-started.html) etc.


<aside class="callout">
🗣 If your code repository is private, you will need to create Instance Secrets with your repository credentials for later use during deployment. Public code repositories do not require Step 2.
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

To get the details of instance-secret created by the user who applies the instance-secret, use the following command:

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
    
To get the details of instance-secret created by all the users within the DataOS Instance, use the above command with `-a` flag:

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
🗣 Ensure that you remember the name of the created **instance secret**, as it will be used in the secrets attribute section of the Lens manifest file. This name is crucial for proper configuration and access within your Lens environment.

</aside>

### **Step 3: Create a Lens Resource manifest file**

A Lens manifest file incorporates the configuration of the Lens Resource. The manifest file for the Lens is composed of several sections which define the configuration of various components associated with the Lens Resource.
The different sections of the Lens manifest file are provided below:

1. **Resource meta section**
2. **Lens-specific section**

```yaml
# RESOURCE META SECTION
name: sales360test # Lens Resource name (mandatory)
version: v1alpha # Lens manifest version (mandatory)
layer: user # DataOS Layer (optional)
type: lens # Type of Resource (mandatory)
tags: # Tags (optional)
  - lens
description: sales360 lens deployment on DataOS # Lens Resource description (optional)

# LENS-SPECIFIC SECTION
lens:
  compute: runnable-default # Compute Resource that Lens should utilize (mandatory)
  secrets: # Referred Instance-secret configuration (**mandatory for private code repository, not required for public repository)
    - name: bitbucket-r # Referred Instance Secret name (mandatory)
      allKeys: true # All keys within the secret are required or not (optional)
  source: # Data Source configuration
    type: minerva # Source type 
    name: system # Source name
    catalog: icebase #in case of minerva or themis
  repo: # Lens
   model code repository configuration (mandatory)
    url: https://bitbucket.org/rubik_/customize-solutions # URL of repository containing the Lens model (mandatory)
    lensBaseDir: customize-solutions/lens/sales360/model # Relative path of the Lens 'model' directory in repository (mandatory)
    syncFlags: # Additional flags used during synchronization, such as specific branch.
      - --ref=lens # Repository Branch 
  api: # API Instances configuration (optional)
    replicas: 1 # Number of API instance replicas (optional)
    logLevel: info  # Logging granularity (optional)
    resources: # CPU and memory configurations for API Instances (optional)
      requests:
        cpu: 100m
        memory: 256Mi
      limits:
        cpu: 2000m
        memory: 2048Mi
  worker: # Worker configuration (optional)
    replicas: 2 # Number of Worker replicas (optional)
    logLevel: info # Logging level (optional)
    resources: # CPU and memory configurations for Worker (optional)
      requests:
        cpu: 100m
        memory: 256Mi
      limits:
        cpu: 6000m
        memory: 6048Mi
  router: # Router configuration (optional)
    logLevel: info  # Level of log detail (optional)
    resources: # CPU and memory resource specifications for the router (optional)
      requests:
        cpu: 100m
        memory: 256Mi
      limits:
        cpu: 6000m
        memory: 6048Mi
  iris:
	  logLevel: info
    resources: # CPU and memory resource specifications for the iris board (optional)
      requests:
        cpu: 100m
        memory: 256Mi
      limits:
        cpu: 6000m
        memory: 6048Mi
```

For more information on how to configure a Lens manifest file, refer to the link: [Configuration Fields of the Deployment Manifest File (YAML) for Lens Resource](/resources/lens/configuration/lens_manifest/)

### **Step 4: Apply the manifest file of Lens Resource using DataOS CLI**

Deploy the Lens model to DataOS using the `apply` command.

<aside class="callout">
🗣 When applying the manifest file from the DataOS CLI, make sure you specify the Workspace as Lens is a [Workspace-level Resource] <a href="https://dataos.info/resources/types/#workspace-level-resources" target="blank"> Workspace-level Resource</a>.

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

[Consumption of Deployed Lens](/resources/lens/consumption_of_deployed_lens/)