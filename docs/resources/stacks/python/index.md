---
title: Python Stack
search:
  boost: 4
tags: 
    - Python
    - Python stack
    - Python Application Deployment
    - Containerized Python
---

# Python Stack

Python Stack provides an environment for executing Python applications and scripts within DataOS. It handles containerization, automatically installs dependencies from the repository, synchronizes the code from Git, and injects secrets securely, so the application runs the same way every time. Key features include:

- **Ready Python environment:** lightweight Python 3.12 image with pip, optimized for production.
- **Dependency management:** installs packages from `requirements.txt` automatically.
- **Code synchronization:** pulls the latest code from Git at runtime using git-sync.
- **Secure secret handling:** injects secrets as environment variables during execution.
- **Reproducibility:** ensures consistent execution across environments, reducing setup issues.

## Prerequisites

Before using the Python Stack, ensure the following requirements are met:

- The Python Stack must be deployed and registered as a Stack within the DataOS environment. To verify the availability of  Python Stack within DataOS, execute the following command.
    
    ```bash
    dataos-ctl get -t stack -a

    #expected output:
                NAME            | VERSION | TYPE  | WORKSPACE | STATUS | RUNTIME |       OWNER        
    ----------------------------|---------|-------|-----------|--------|---------|--------------------
      beacon-graphql-v1         | v1alpha | stack |           | active |         | dataos-manager     
      bento-v4                  | v1alpha | stack |           | active |         | dataos-manager     
      flare-v7                  | v1alpha | stack |           | active |         | dataos-manager     
      lakesearch-v2             | v1alpha | stack |           | active |         | iamloki         
      python-3-12               | v1alpha | stack |           | active |         | iamgroot           
    ```
    
    <aside class="callout">
    🗣 If Python Stack is not available, deploy the Stack by following the steps given in the link below.<br>
    <a href="/resources/stacks/python/stack_deployment/">Deploy Python as a Stack</a>
    </aside>

- A Compute Resource must be configured and accessible for running Python workloads. To configure the Compute Resource, please [refer to this link.](/resources/compute/)

- Persistent Volume Resource should be provisioned for data processing use cases. To configure Volume Resource,  please [refer to this link.](/resources/volume/)

- A valid Git repository (GitHub or Bitbucket) that will contain the Python application or script code.

- Access to the target DataOS workspace where the application will be deployed. To create a new workspace, execute the command below.
    
    ```bash
    dataos-ctl workspace create -n ${{workspace-name}}
    ```
    
- Permissions to create and manage DataOS Resources, such as Services and Instance Secrets.

- Application code must be compatible with Python 3.12.

## Getting started with Python Stack

This section guides you through the complete flow, from securing repository access to structuring the code and finally deploying it as a managed Service within DataOS.

### **Build the Python application**

The application code or script must be structured in a Git repository with a clear base directory containing `main.py` (entry point) and `requirements.txt` (dependencies). This step involves preparing the codebase with proper configuration, logging, and dependency management so it runs reliably in the DataOS environment. To do so,  please refer to the link below.

[Build a Python application/script](/resources/stacks/python/repo_setup/)

### **Deploy the Python application**

Once your code and repository credentials are ready, you can define and apply a Python Service manifest to run the Python code using Python Stack. The manifest specifies details such as repository URL, base directory, resource limits, environment variables, and secrets. To do so, please refer to the following link. 

[Configure a Python Service](/resources/stacks/python/python_service/)

## Configurations

This section provides a comprehensive overview of the configuration attributes available for the Python Service manifest files.

[Python Service manifest configuration](/resources/stacks/python/configurations/)

## Governance

This section explains how authentication and access control work when deploying and running Python applications on the Python Stack. These mechanisms ensure that only authorized users can access or manage the Python Service and applications.

### **Authentication**

Authentication ensures that only authorized users can access Python applications. To authenticate the Python application with a valid user, please refer to the link below.

[Authentication](/resources/stacks/python/authentication/)

### **Access control**

Access control defines what authenticated users are allowed to do. For Python applications, this involves regulating who can access the Python Application. Policies, roles, use cases, and tags are applied to enforce permissions, ensuring that users interact only with approved Python applications.

[Access Control](/resources/stacks/python/access/)

## Recipes

This section provides examples for deploying common Python use cases on the Python Stack. Each recipe demonstrates how to structure your code, configure required dependencies, and define service manifests to deploy and run applications in DataOS successfully.

### **Frameworks**

This section includes step-by-step implementation guides for common Python scenarios. It demonstrates how to prepare code, configure manifests, and deploy interactive or visualization-based applications on the Python Stack.

#### Streamlit

Streamlit is an open-source Python framework to deliver data apps with only a few lines of code. This subsection explains how to deploy a Streamlit application on the Python Stack. It covers repository setup, dependency configuration, service definition, and how to expose the application through ports and ingress.

[Implement the Streamlit Framework](/resources/stacks/python/streamlit/)

#### Vizro

Vizro is an open-source, Python-based toolkit designed to simplify the creation of data visualization applications and dashboards. This subsection explains how to deploy a Vizro dashboard application. It focuses on structuring the repository, managing required dependencies, defining the Service manifest, and enabling external access through ingress settings.

[Implement the Vizro Framework](/resources/stacks/python/vizro/)

### **Utilities**

This section provides  Python scripts that help developers automate common tasks and interact with DataOS resources more efficiently. These examples are designed to illustrate how simple automation logic can be integrated into applications running on the Python Stack.

#### Retrieve data insights

This example demonstrates how to use a Python script to query the Semantic Model and extract insights.

[Retrieve insights from the Semantic Model](/resources/stacks/python/insights/)

## Best practices

This section includes recommended approaches for using the Python Stack effectively. It highlights how to organize repositories, manage dependencies, configure applications with environment variables, and implement proper logging and error handling.

[Best practices](/resources/stacks/python/bestpractices/)

## Troubleshooting

This section guides on resolving common issues that arise when deploying and running Python applications or scripts.

[Troubleshooting](/resources/stacks/python/troubleshooting/)