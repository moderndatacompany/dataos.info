# Steampipe

Steampipe is a declarative [Stack](../stacks.md) integrated within the DataOS that exposes APIs and services as a high performance relational database, enabling data querying and analysis upon these dynamic data interfaces and cloud platforms using SQL-based queries. Leveraging the open-source [Steampipe](https://steampipe.io/docs), it provides an array of plugins for diverse data sources, enabling streamlined data retrieval.

## How to start using Steampipe Stack: Connecting to CSV

The below points outline the high-level steps involved in establishing a connection to a CSV data source and commencing query operations using the Steampipe Stack. 

- [Prerequisites](#prerequisites)
    - [Steampipe Stack within the DataOS instance](#ensure-the-presence-of-a-steampipe-stack-within-the-dataos-instance)
- [Steps](#steps)
    - [Create a Service orchestrating the Steampipe Stack](#create-a-service-that-orchestrates-the-steampipe-stack)
    - [Establish a Depot atop the Database Service](#create-a-depot-on-the-hosted-database-service)
    - [Validate the Depot using port-forward and USQL](#validate-the-depot-using-port-forward-and-usql)
    - [Target a Cluster on the Depot](#cluster-manifest-creation-and-depot-targeting)

### **Prerequisites**

#### **Ensure the presence of a Steampipe Stack within the DataOS instance**

Before commencing, ascertain the existence of a Steampipe Stack within the DataOS instance. Utilize the [`get`](../../interfaces/cli/command_reference.md#get) command to list all available the Stacks within the DataOS instance:

```shell
dataos-ctl get -t stack -a
```

<details>
<summary>Sample</summary>
    
```shell
dataos-ctl get -t stack -a          
# Expected Output
INFO[0000] 🔍 get...                                     
INFO[0000] 🔍 get...complete                             

            NAME            | VERSION | TYPE  | WORKSPACE | STATUS | RUNTIME |       OWNER        
----------------------------|---------|-------|-----------|--------|---------|--------------------
    alpha-v1                  | v1alpha | stack |           | active |         | dataos-manager     
    beacon-graphql-v1         | v1alpha | stack |           | active |         | dataos-manager     
    beacon-rest-v1            | v1alpha | stack |           | active |         | dataos-manager     
    benthos-v3                | v1alpha | stack |           | active |         | dataos-manager     
    dataos-ctl-v1             | v1alpha | stack |           | active |         | dataos-manager     
    dataos-resource-apply-v1  | v1alpha | stack |           | active |         | dataos-manager     
    dataos-resource-delete-v1 | v1alpha | stack |           | active |         | dataos-manager     
    dataos-resource-run-v1    | v1alpha | stack |           | active |         | dataos-manager         
    flare-v4                  | v1alpha | stack |           | active |         | dataos-manager      
    scanner-v1                | v1alpha | stack |           | active |         | dataos-manager     
    scanner-v2                | v1alpha | stack |           | active |         | dataos-manager     
    soda                      | v1alpha | stack |           | active |         | dataos-manager     
    steampipe-v1              | v1alpha | stack |           | active |         | iamgroot
    toolbox-v1                | v1alpha | stack |           | active |         | dataos-manager
```
</details>

If the Steampipe Stack is not available within the DataOS instance, initiate the creation of a new Steampipe Stack. For detailed guidance on crafting a custom Stack within DataOS, consult the following resource: [How to create a custom Stack within DataOS?](./custom_stacks.md)

### **Steps**

#### **Create a Service that orchestrates the Steampipe Stack**

**Create a Service Manifest**

A [Service](../service.md) is a long-running process designed to handle and respond to API requests, serves as the orchestrator for the Steampipe Stack. By applying the Service manifest from the DataOS CLI, a Service Resource instance can be created that orchestrates the Steampipe Stack. For the orchestration of the Steampipe Stack, certain attributes necessitate specific configurations

- `servicePort`: Set the `servicePort` to 9193 for the Steampipe Stack. Any deviation from this port number will result in errors.
    
    ```yaml
    servicePort: 9193
    ```
    
- `stack`: Utilize the following stack name and version: `steampipestack:1.0`. Retrieve the Stack name and version from the YAML of the specific Steampipe Stack definition.
    
    ```yaml
    stack: steampipestack:1.0
    ```
    
- `envs`: Furnish the Steampipe Database password through the `STEAMPIPE_DATABASE_PASSWORD` environmental variable. Alternatively, create a separate Secret Resource, create a Secret Resource instance for the same by applying it from the CLI and reference the Secret using the `dataosSecrets` attribute within the Steampipe Service. For further details on this scenario, consult the documentation on [Referring Secrets in a Service Resource.](/resources/secret/#how-to-refer-secrets-in-other-dataos-resources)
    
    ```yaml
    # For Referring Secrets from a pre-created Secret Resource
      dataosSecrets: 
        - name: ${{secret resource name}}
          workspace: ${{workspace name}}
          allKeys: true
          consumptionType: envVars
    
    # For Supplying Secrets as Environment Variables
      envs:
        STEAMPIPE_DATABASE_PASSWORD: ${{steampipe database password}}
    ```
    
- `configs`: Steampipe relies on the `.spc` file for configuration specifications. The filename varies based on the plugin, such as `csv.spc` for CSV or `snowflake.spc` for Snowflake. As a data developer, specify the file name along with the path in the value. Upon applying the YAML, the DataOS orchestrator, Poros, interpolates information from the `.spc` file and encrypts it using the base64 encryption algorithm within the YAML definition. You can verify this process by linting the YAML before applying. For additional configuration rules related to the .spc file, refer to the official Steampipe documentation and search for the specific plugin.
    
    ```yaml
    configs:
    	csv.spc: "/home/iamgroot/stack/dataos_steampipe/steampipe_csv/config/csv.spc"
    ```
    
    The configuration for the `csv.spc` is provided below:
    
    ```shell
    connection "csv" {
      plugin = "csv"
    
      # Paths is a list of locations to search for CSV files
      # Paths can be configured with a remote Git repository URL, or an S3 bucket URL, etc.
      # Refer https://hub.steampipe.io/plugins/turbot/csv#supported-path-formats for more information
      # All paths are resolved relative to the current working directory (CWD)
      # Wildcard based searches are supported, including recursive searches
    
      # For example:
      #  - "*.csv" matches all CSV files in the CWD
      #  - "*.csv.gz" matches all gzipped CSV files in the CWD
      #  - "**/*.csv" matches all CSV files in the CWD and all sub-directories
      #  - "../*.csv" matches all CSV files in the CWD's parent directory
      #  - "steampipe*.csv" matches all CSV files starting with "steampipe" in the CWD
      #  - "/path/to/dir/*.csv" matches all CSV files in a specific directory
      #  - "/path/to/dir/custom.csv" matches a specific file
    
      # If paths includes "*", all files (including non-CSV files) in
      # the CWD will be matched, which may cause errors if incompatible file types exist
    
      # Defaults to CWD
      paths = [ "bitbucket.org/ved_misra/sample-csv//*.csv" ] 
    
      # The field delimiter character when parsing CSV files. Must be a single
      # character. Defaults to comma.
      # separator = ","
    
      # If set, then lines beginning with the comment character without preceding
      # whitespace are ignored. Disabled by default.
      # comment = "#"
    
      # Determine whether to use the first row as the header row when creating column names.
      # Valid values are "auto", "on", "off":
      #   - "auto": If there are no empty or duplicate values use the first row as the header; else, use the first row as a data row and use generic column names, e.g., "a", "b".
      #   - "on": Use the first row as the header. If there are empty or duplicate values, the tables will fail to load.
      #   - "off": Do not use the first row as the header. All column names will be generic.
      # Defaults to "auto".
      # header = "auto"
    }
    ```
    
    For more details, refer to the official [CSV+Steampipe plugin documentation.](https://hub.steampipe.io/plugins/turbot/csv#configuration)
    
- `stackSpec`: Keep the `stackSpec` attribute empty by utilizing **`{}`** after a space.
    
    ```yaml
    stackSpec: {}
    ```
    

For details on the remaining attributes, consult the documentation on [Attributes of the Service Manifest.](../service/yaml_configuration_attributes.md)

<details>
<summary>Sample Service Resource manifest</summary>
    
```yaml
# Resource meta section
name: steampipe-csv
version: v1
type: service
tags:
    - service
    - steampipe
description: Steampipe CSV Service

# Service-specific section
service:
    servicePort: 9193 # Mandatory value: 9193
    replicas: 1
    stack: steampipestack:1.0 # Stack name and version
    logLevel: INFO
    compute: runnable-default

# Uncomment the relevant section based on secret handling preference

# For Referring Secrets from a pre-created Secret Resource
    # dataosSecrets: 
    #   - name: steampipedb
    #     workspace: steampipe
    #     allKeys: true
    #     consumptionType: envVars

# For Supplying Secrets as Environment Variables
    envs:
    STEAMPIPE_DATABASE_PASSWORD: "${{steampipe database password}}"

    configs:
    csv.spc: "/home/iamgroot/modern_office/stack/dataos_steampipe/steampipe_csv/config/csv.spc"

# Stack-Specific Section
    stackSpec: {}
```
</details>

**Apply the Service Resource manifest**

Once you have created the Service manifest, [`apply`](../../interfaces/cli/command_reference.md#apply) it using the DataOS Command Line Interface (CLI) to instantiate a Service Resource instance. Execute the following command:

```shell
dataos-ctl apply -f ${{file-path}} -w ${{workspace-name}}
```

**Verification and Status Confirmation**

Validate the Service Resource instance creation by utilizing the [`get`](../../interfaces/cli/command_reference.md#get) command:

```shell
dataos-ctl get -t service -w ${{workspace-name}}
```

#### **Create a Depot on the hosted Database Service**

**Create a Depot Manifest** 

Once you have the Steampipe Service up and running, the next step involves creating a Depot on the Postgres Database associated with that Service. This necessitates the formulation of a Postgres Depot Manifest. Detailed configuration specifications are available on the [PostgreSQL Depot config templates](../depot/depot_config_templates/postgresql.md). In this specific context, certain attributes demand precise configuration, as outlined below:

- `host`: Configure the host using the format given below:
    
    ```yaml
    # Format
    host: ${{name of the steampipe service}}.${{workspace of the service}}.svc.cluster.local
    
    # Sample 
    host: steampipe-csv.public.svc.cluster.local
    ```
    
- `port`: Set the port number to 9193.
    
    ```yaml
    port: 9193
    ```
    
- `database`: Specify the database name as `steampipe`.
    
    ```yaml
    database: steampipe
    ```
    

The remaining attributes can be adjusted in accordance with the information provided in the link: [PostgreSQL Depot Configuration.](../depot/depot_config_templates/postgresql.md)

<details>
<summary>Sample Depot Resource manifest</summary>
    
```yaml
# Resource meta section
name: steampipecsvdepot
version: v1
type: depot
layer: user

# Depot-specific section
depot:
    type: JDBC                                # Depot type
    description: To write data to retaildb postgresql database
    external: true
    connectionSecret:                               # Data source specific configurations
    - acl: r
        type: key-value-properties
        data:
        username: "steampipe"
        password: "${{steampipe depot password}}"
    spec:                                           # Data source specific configurations
    host: steampipe-csv.public.svc.cluster.local
    port: 9193
    database: steampipe
    subprotocol: postgresql
```
</details>

**Apply the Depot manifest**

To create Depot Resource instance within the DataOS environment, use the [`apply`](../../interfaces/cli/command_reference.md#apply) command as shown below:

```shell
dataos-ctl apply -f ${{depot manifest file path}}
```

**Verify Depot Creation**

Use the [`get`](../../interfaces/cli/command_reference.md#get) command to verify whether the depot is in an active state or not.

```shell
dataos-ctl get -t depot
```

#### **Validate the Depot using port-forward and USQL**

Prior to directing queries towards a [Cluster](../cluster.md) through the Depot, it is advisable to validate the Depot's functionality. The DataOS CLI facilitates this validation.

**Port Forwarding for Service Port**

Execute the following command on the DataOS CLI to port forward the servicePort to a locally designated listenPort:

```shell
dataos-ctl -t service -w public -n ${{service name}} tcp-stream --servicePort 9193 --listenPort ${{valid localhost port number}}
```

**Query the Database using the DataOS CLI USQL**

Utilize the DataOS `usql` command to query the Database:

```shell
dataos-ctl usql "postgres://localhost:${{username}}@${{password}}"

# Sample Command
dataos-ctl usql "postgres://localhost:steampipe@alphabeta"
```

Execute a series of Postgres commands to confirm successful database querying:

```sql
\dt # to list all the database tables

select * from locations limit 10;
```

#### **Cluster manifest Creation and Depot Targeting**

Upon successful validation of querying through DataOS usql, the subsequent step involves creating a Cluster and directing it towards the designated depot.

**Create a Cluster manifest**

Create a new Cluster manifest or incorporate the depot address into an existing Cluster and update the YAML definition. A sample Cluster manifest is provided below.

```yaml
# Resource meta section
name: steampipecsvcluster
version: v1
type: cluster

# Cluster-specific section
cluster:
  compute: runnable-default
  minerva:
    replicas: 1
    resources:
      requests:
        cpu: 2000m
        memory: 2Gi
      limits:
        cpu: 2000m
        memory: 2Gi

# Target depot
    depots:
      - address: dataos://steampipecsvdepot:default
    debug:
      logLevel: DEBUG
      trinoLogLevel: DEBUG
    selector:
      users:
        - '**'
      tags: []
      sources:
        - '**'
      match: ""
      priority: ""
```

**Apply the Cluster manifest**

To create Cluster Resource instance within the DataOS environment, use the [`apply`](../../interfaces/cli/command_reference.md#apply) command as shown below:

```shell
dataos-ctl apply -f ${{cluster manifest file path}} -w ${{workspace name}}
```

**Verification and Status Confirmation**

Validate the Cluster Resource instance creation by utilizing the [`get`](../../interfaces/cli/command_reference.md#get) command:

```shell
dataos-ctl get -t cluster -w ${{workspace-name}}
```

**Query Data on Workbench**

Navigate to the Workbench application on the DataOS and choose the above steampipedepot Cluster and the catalog, schema choose as csv

```sql
SELECT * FROM csv_locations LIMIT 10;
```

## Steampipe Plugins

Steampipe employs a Postgres Foreign Data Wrapper (FDW) to present external system and service data as database tables. The Steampipe Foreign Data Wrapper serves as a Postgres extension, enabling Postgres to establish connections with external data sources in a standardized manner. It's important to note that the Steampipe FDW does not directly interact with external systems. Instead, it relies on plugins to implement API/provider-specific code, delivering it in a standardized format through gRPC.

This architectural choice streamlines the extension of Steampipe, as the Postgres-specific logic is encapsulated within the FDW. API and service-specific code are exclusively housed within the plugins, ensuring a modular and maintainable structure.

### **Default Plugins**

The Steampipe Stack in the DataOS relies on a predefined set of plugins installed within the Steampipe Stack image. The default plugins are summarized in the table below.

<center>

| Plugin Name | Description |
| --- | --- |
| `csv` | Steampipe plugin designed for querying CSV files. |
| `aws` | Steampipe plugin tailored for querying instances, buckets, databases, and more from the AWS Public Cloud. |
| `salesforce` | Steampipe plugin enabling the querying of accounts, opportunities, users, and more from Salesforce instances. |
| `config` | Steampipe plugin facilitating the querying of data from various file types, including INI, JSON, YML, and more. |
| `googlesheets` | Capability to query data stored in Google Sheets. |
| `francois2metz/airtable` | https://airtable.com/ integration, providing the ability to query data from this user-friendly database platform. |
| `finance` | Financial data retrieval from multiple sources, including https://finance.yahoo.com/ and https://www.sec.gov/edgar.shtml service. |
| `exec` | Execution of commands locally or on remote Linux and Windows hosts through SSH or WinRM. |

</center>

### **Installing additional plugins from Steampipe Hub**

In cases where a data developer aims to connect to a source not covered by the plugins listed above, the developer must install the desired Steampipe plugin from the [Steampipe Plugin Hub](https://hub.steampipe.io/plugins) within the Steampipe image. Following the installation, a new image must be built, and the Stack within the new image should be updated or a new Stack created. Subsequently, this updated or new Stack can be employed to establish a connection to the desired source. Detailed steps for this process are available on the link: [Installing additional plugins within the Steampipe Stack.](./steampipe/installing_additional_plugins.md)