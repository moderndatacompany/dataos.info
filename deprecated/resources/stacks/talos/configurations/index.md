# Talos Configurations

Talos configurations consist of various manifest files, let’s see each one in detail to help you configure Talos efficiently.

## `config.yaml`

The config.yaml file serves as the primary configuration file for a Talos project. It specifies essential settings and parameters required to configure the Talos application. For a detailed explanation of each attribute, refer to [this section](/resources/stacks/talos/configurations/config/).

## `apis`

The `apis` directory contains:

- **SQL Files:** Define the queries used by the API.
- **Manifest Files:** Contain the API endpoint path, description, data source, and access control settings for user groups.

For more details, refer to [this section](/resources/stacks/talos/configurations/apis/).

## `service.yaml`

The service.yaml file is a service manifest used for configuring Talos within DataOS. It includes service definitions, dependencies, and environment configurations. For a complete attribute reference, refer to [this section](/resources/stacks/talos/configurations/service/).

## Additional Links

- [Talos for Lens](/resources/stacks/talos/recipes/lens_setup/)
- [Talos for Flash](/resources/stacks/talos/recipes/flash_setup/)
- [Talos for Redshift](/resources/stacks/talos/recipes/redshift/)
- [Talos for Postgres](/resources/stacks/talos/recipes/postgres/)
- [Talos for Mysql](/resources/stacks/talos/recipes/mysql/)
