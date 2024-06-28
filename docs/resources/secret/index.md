---
title: Secret
search:
  boost: 2
---

# :resources-secret: Secret

In DataOS, Secrets are [Resources](/resources/) designed for the secure storage of sensitive information, including usernames, passwords, certificates, tokens, or keys within the confines of a specific [DataOS Workspace](/resources/). 

To mitigate the risk of exposing confidential data, Secrets in DataOS separate sensitive information from application code or configuration files. This practice minimizes the chance of accidental exposure during resource management phases like creation, viewing, or editing. By leveraging Secrets, data developers safeguard sensitive information, thus reducing security vulnerabilities in their data workflows.

Operators can exercise precise control over who can retrieve credentials from Secrets, if in your organisation any data developer need access to secrets you can assign them a 'read secret' use case using [Bifrost](/interfaces/bifrost/).

!!!tip "Secret in the Data Product Lifecycle"

    In the Data Product Lifecycle, Secrets play a crucial role in securely managing credentials and sensitive information. They are particularly useful when your data product requires:

    - **Secure Credential Management**: Storing and managing sensitive information such as usernames, passwords, API keys, or certificates securely within a spcific workspace. For example, a Secret can securely store the credentials needed to access the private repository, ensuring that these credentials are not exposed in the codebase or configuration files.

    - **Access Control**: Ensuring that only authorized components and services within the workspace can access the credentials. For instance, a secret can be used to provide a web application with the credentials to access a third-party service without exposing those credentials to the broader environment.

    - **Auditing and Compliance**: Maintaining a secure and auditable method of handling sensitive data, complying with security policies and regulatory requirements. Secrets ensure that credential usage is logged and can be monitored for compliance purposes.

    By using Secrets, you can manage sensitive information securely and efficiently, mitigating the risk of exposing credentials while enabling seamless access for your applications and services.

<aside class="callout">

🗣️ Each Secret in DataOS is linked to a specific <a href="https://dataos.info/resources/types_of_dataos_resources/#workspace-level-resources">Workspace</a>, confining its accessibility and application within that Workspace. This reinforces data security measures by ensuring that Secrets are only accessible within their designated Workspace. However, it's important to note that <a href="https://dataos.info/resources/instance_secret/">Instance-secret</a> have a broader scope, spanning across the entirety of the <a href="https://dataos.info/resources/types_of_dataos_resources/#instance-level-resources">DataOS instance</a> .

</aside>

## First Steps

Secret Resource in DataOS can be created by applying the manifest file using the DataOS CLI. To learn more about this process, navigate to the link: [First steps](/resources/secret/first_steps/).

## Configuration

Secret can be configured to secure the credentials infromation in the form of key value pairs. For a detailed breakdown of the configuration options and attributes, please refer to the documentation: [Attributes of Secret manifest](/resources/secret/configuration/).

## Recipes

Below are some recipes to help you configure and utilize Secret effectively:

[How to refer Secret in other DataOS Resources?](/resources/secret/how_to_guide/recipe1/)

[How to set up secrets to pull images from a private container registry for Docker credentials?](/resources/secret/how_to_guide/recipe2/)