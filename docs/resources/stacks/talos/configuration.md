# Talos Configurations

Talos configurations consist of various manifest files, let’s see each one in detail to help you configure Talos efficiently.

## `config.yaml`

The `config.yaml` file is the main configuration file for a Talos project. It defines the essential settings and parameters to configure your Talos application. To understand each attribute in detail please refer to [this section](/resources/stacks/talos/configurations/config/).

## `docker-compose.yaml`

Docker compose manifest file is used to configure the docker image of Talos. To understand each attribute of the docker-compose manifest file, please refer to [this section](/resources/stacks/talos/configurations/docker_compose/).

## `apis`

While configuring Talos, the `apis` folder contains an SQL file and a manifest file, an SQL file is where you write your queries, and the manifest file contains the endpoint path, description, source, and allowed user groups. To know more in detail please refer to [this section](/resources/stacks/talos/configurations/apis/).

## `service.yaml`

`service.yaml` is a Service manifest file configured when setting up Talos within DataOS. To understand each attribute of this manifest file, please refer to [this section](/resources/stacks/talos/configurations/service/).

<aside class="callout">
🗣 Note that you do not need to configure the `service.yaml` file while setting up Talos Locally.

</aside>

## `Makefile`

The `Makefile` simplifies and automates the process of managing Docker Compose services, making it easier to start and stop services with predefined commands.