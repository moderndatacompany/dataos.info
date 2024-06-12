---
title: Instance Secret
search:
  boost: 2
---

# Instance Secret

An Instance Secret is a [DataOS Resource](/resources/) designed for securely storing sensitive information at the DataOS instance level. This encompasses sensitive information like usernames, passwords, certificates, tokens, and keys. The primary purpose of Instance Secret is to address the inherent exposure risk associated with directly embedding such confidential data within application code or manifest file (YAML configuration files).

Instance secrets establish a critical segregation between sensitive data and Resource definitions. This division minimizes the chances of inadvertent exposure during various Resource management phases, including creation, viewing, or editing. By leveraging Instance Secrets, data developers ensure the safeguarding of sensitive information, thereby mitigating security vulnerabilities inherent in their data workflows. To understand the key characteristics and what differentiates an Instance Secret from a Secret refer to the following link: [Core Concepts](/resources/worker/core_concepts/).

<aside class="callout">

🗣️ In the DataOS ecosystem, there are two specialized Resources designed to protect sensitive information: Instance Secret and <a href="/resources/secret/">Secret</a>. The Instance Secret offers a wider scope, extending across the entirety of the <a href="/resources/types_of_dataos_resources/#instance-level-resources">DataOS Instance</a>. Resources within any Workspace can utilize Instance Secrets for securely retrieving sensitive data. In contrast, Secrets are limited to the <a href="/resources/types_of_dataos_resources/#workspace-level-resources">Workspace level</a>, accessible exclusively within a specific Workspace and only by Resources associated with that Workspace.
</aside>

## First Steps

Instance-secret Resource in DataOS can be created by applying the manifest file using the DataOS CLI. To learn more about this process, navigate to the link: [First steps](/resources/instance_secret/first_steps/).

## Configuration

Instance-secret can be configured to secure the credentials infromation in the form of key value pairs. For a detailed breakdown of the configuration options and attributes, please refer to the documentation: [Attributes of Instance Secret manifest](/resources/instance_secret/configuration/).

## Recipes

Below are some recipes to help you configure and utilize Instance Secret effectively:

[How to refer Instance Secret in other DataOS Resources?](/resources/instance_secret/how_to_guide/recipe1/)

[Templates for Instance Secret of different source systems](/resources/instance_secret/how_to_guide/recipe2/)
