# Connecting to snowflake Depot

## Prerequisite

CLI Version should be `dataos-cli 2.26.39-dev` or greater.


## Step 1: Create the snowflake Depot

If the Depot is not active, you need to create one using the provided template.

```yaml
name: snowflake-depot
version: v2alpha
type: depot
tags:
  - Snowflake depot
  - user data
layer: user
depot:
  name: sftest
  type: snowflake
  description: Depot to fetch data from Snowflake datasource
  secrets:
    - name: sftest-r
      keys:
        - sftest-r
      allKeys: true
    - name: sftest-rw
      keys:
        - sftest-rw
      allKeys: true
  external: true
  snowflake:
    database: TMDC_V1
    url: ABCD23-XYZ8932.snowflakecomputing.com
    warehouse: COMPUTE_WH
    account: ABCD23-XYZ8932
  source: sftest
```

## Step 2: Prepare the Lens model folder

Organize the Lens model folder with the following structure to define tables, views, and governance policies:

```
model
├── sqls
│   └── sample.sql  # SQL script for table dimensions
├── tables
│   └── sample_table.yml  # Logical table definition (joins, dimensions, measures, segments)
├── views
│   └── sample_view.yml  # Logical views referencing tables
└── user_groups.yml  # User group policies for governance
```

1. **SQL Scripts (`model/sqls`):** Add SQL files defining table structures and transformations. Ensure the SQL dialect matches snowflake syntax. Format table names as:
     `schema.table`.

2. **Tables (`model/tables`):** Define logical tables in separate YAML files. Include dimensions, measures, segments, and joins.

3. **Views (`model/views`):** Define views in YAML files, referencing the logical tables.

4. **User Groups (`user_groups.yml`):** Define access control by creating user groups and assigning permissions.

## Step 3: Deployment manifest file

After setting up the Lens model folder, the next step is to configure the deployment manifest. Below is the YAML template for configuring a Lens deployment.

```yaml
# RESOURCE META SECTION
version: v1alpha # Lens manifest version (mandatory)
name: "snowflake-lens" # Lens Resource name (mandatory)
layer: user # DataOS Layer (optional)
type: lens # Type of Resource (mandatory)
tags: # Tags (optional)
  - lens
description: snowflake depot lens deployment on lens2 # Lens Resource description (optional)

# LENS-SPECIFIC SECTION
lens:
  compute: runnable-default # Compute Resource that Lens should utilize (mandatory)
  secrets: # Referred Instance-secret configuration (**mandatory for private code repository, not required for public repository)
    - name: bitbucket-cred # Referred Instance Secret name (mandatory)
      allKeys: true # All keys within the secret are required or not (optional)

  source: # Data Source configuration
    type: depot # Source type is depot here
    name: snowflake-depot # Name of the snowflake depot

  repo: # Lens model code repository configuration (mandatory)
    url: https://bitbucket.org/tmdc/sample # URL of repository containing the Lens model (mandatory)
    lensBaseDir: sample/lens/source/depot/snowflake/model # Relative path of the Lens 'model' directory in the repository (mandatory)
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
    logLevel: debug # Logging level (optional)
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
    logLevel: info # Level of log detail (optional)
    resources: # CPU and memory resource specifications for the iris board (optional)
      requests:
        cpu: 100m
        memory: 256Mi
      limits:
        cpu: 6000m
        memory: 6048Mi

  metric:    #optional
    logLevel: info
```

Each section of the YAML template defines key aspects of the Lens deployment. Below is a detailed explanation of its components:

* **Defining the Source:**

      * **Source type:**  The `type` attribute in the `source` section must be explicitly set to `depot`.

      * **Source name:** The `name` attribute in the `source` section should specify the name of the snowflake Depot created.

* **Setting Up Compute and Secrets:**

      * Define the compute settings, such as which engine (e.g., `runnable-default`) will process the data.

      * Include any necessary secrets (e.g., credentials for Bitbucket or AWS) for secure access to data and repositories.

* **Defining Repository:**

      * **`url`** The `url` attribute in the repo section specifies the Git repository where the Lens model files are stored. For instance, if your repo name is lensTutorial then the repo `url` will be  [https://bitbucket.org/tmdc/lensTutorial](https://bitbucket.org/tmdc/lensTutorial)

      * **`lensBaseDir`:**  The `lensBaseDir` attribute refers to the directory in the repository containing the Lens model. Example: `sample/lens/source/depot/snowflake/model`.

      * **`secretId`:**  The `secretId` attribute is used to access private repositories (e.g., Bitbucket, GitHub) . It specifies the secret needed to securely authenticate and access the repository.

      * **`syncFlags`**:  Specifies additional flags to control repository synchronization. Example: `--ref=dev` specifies that the Lens model rsides in the dev branch.

* **Configuring API, Worker and Metric Settings (Optional):** Set up replicas, logging levels, and resource allocations for APIs, workers, routers, and other components.

## Step 4: Apply the Lens deployment manifest file

After configuring the deployment file with the necessary settings and specifications, apply the manifest using the following command:

=== "Command"

    ```bash 
    dataos-ctl resource apply -f ${manifest-file-path}
    ```
=== "Alternative command"

    ```bash 
    dataos-ctl apply -f ${manifest-file-path}
    ```
=== "Example usage"

    ```bash 
    dataos-ctl apply -f /lens/lens_deployment.yml -w curriculum
    # Expected output
    INFO[0000] 🛠 apply...                                   
    INFO[0000] 🔧 applying(curriculum) sales360:v1alpha:lens... 
    INFO[0001] 🔧 applying(curriculum) sales360:v1alpha:lens...created 
    INFO[0001] 🛠 apply...complete
    ```
