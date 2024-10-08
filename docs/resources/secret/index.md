---
title: Secret
search:
  boost: 3
---

# :resources-secret: Secret

In DataOS, Secrets are [Resources](/resources/) designed for the secure storage of sensitive information, including usernames, passwords, certificates, tokens, or keys within the confines of a specific [DataOS Workspace](/resources/). 

To mitigate the risk of exposing confidential data, Secrets in DataOS separate sensitive information from application code or configuration files. This practice minimizes the chance of accidental exposure during resource management phases like creation, viewing, or editing. By leveraging Secrets, data developers safeguard sensitive information, thus reducing security vulnerabilities in their data workflows.

Operators can exercise precise control over who can retrieve credentials from Secrets, if in your organisation any data developer need access to secrets you can assign them a 'read secret' use case using [Bifrost](/interfaces/bifrost/).

<aside class="callout">

🗣️ Each Secret in DataOS is linked to a specific <a href="/resources/types/#workspace-level-resources">Workspace</a>, confining its accessibility and application within that Workspace. This reinforces data security measures by ensuring that Secrets are only accessible within their designated Workspace. However, it's important to note that <a href="/resources/instance_secret/">Instance-secret</a> have a broader scope, spanning across the entirety of the <a href="/resources/types/#instance-level-resources">DataOS instance</a> .

</aside>

## First Steps

Secret Resource in DataOS can be created by applying the manifest file using the DataOS CLI. To learn more about this process, navigate to the link: [First steps](/resources/secret/first_steps/).

## Configuration

Secret can be configured to secure the credentials infromation in the form of key value pairs. For a detailed breakdown of the configuration options and attributes, please refer to the documentation: [Attributes of Secret manifest](/resources/secret/configurations/).

## Recipes

Below are some recipes to help you configure and utilize Secret effectively:

[How to refer Secret in other DataOS Resources?](/resources/secret/how_to_guide/recipe1/)

[How to set up secrets to pull images from a private container registry for Docker credentials?](/resources/secret/how_to_guide/recipe2/)