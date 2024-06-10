# `stackSpec`

## Attributes of profile section

### `profile`

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | None  |          - |

**Description:** Mandatory configuration. The profile serves as the overarching container for configuration settings within dbt. It encompasses attributes such as targets and their respective specifications.

**Example Usage:**

```yaml
profile: my_organization
profile: analytics_team
profile: data_engineering
```

**Additional Information:**
A dbt project typically revolves around a single profile, and it is advisable to name the profile in a manner that reflects the organization, adhering to snake_case conventions.

### `outputs`

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mappings | mandatory | None  |          - |

**Description:** A configuration section that includes settings related to various outputs or targets within a dbt project. It encompasses attributes such as `<target-name>`, `type`, and `threads`.

**Example Usage:**

```yaml
outputs:
  dev:
    type: snowflake
    threads: 4
  production:
    type: bigquery
    threads: 8
```

### `<target-name>`

**Description:** A specific target within the outputs section, representing a distinct environment or configuration set within a dbt project.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | None  | dev |

**Example Usage:**

```yaml
outputs:
  dev:
    type: snowflake
    threads: 4
  staging:
    type: redshift
    threads: 6
```

### `type`

**Description:** A parameter within a target or output, specifying the type of data warehouse that the dbt project is connecting to.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | None  | bigquery |

**Example Usage:**

```yaml
type: snowflake
type: bigquery
type: redshift`threads`
```

### `threads`

**Description:** A parameter within a target or output, indicating the number of threads that the dbt project will utilize during execution.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| integer | mandatory | None  | 4 |

**Example Usage:**

```yaml
threads: 4
threads: 8
threads: 6
```

**Additional Information:**
The `threads` attribute influences the parallelization of dbt runs, impacting the efficiency of project execution. The default value is often set to 4 threads in user profiles.

## project section

### Attributes of project section

### `name`

**Description:** Required configuration. The name of a dbt project. Should consist of letters, digits, and underscores only; it cannot start with a digit.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | None  | my_project |

**Example Usage:**

```yaml
name: tmdc
name: candy_shop
name: grootcorp
```

**Additional Information:**
An organization typically has one dbt project, making it sensible to name a project with the organization's name in snake_case.

### `version`

**Description:** Model versions, dbt_project.yml versions, and .yml property file versions are distinct and serve different purposes.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | None  | Semantic version format (e.g., 1.0.0) |

**Additional Information:**

- Model versions facilitate effective governance and data model management, tracking changes and updates over time, while dbt_project.yml versions indicate the compatibility of the dbt project with a specific dbt version,

**Example Usage:**

```yaml
version: 1.0.0
```

### `config-version`

**Description:** Specify your dbt_project.yml as using the v2 structure.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| integer | optional | 1 (if not specified) | 2 |

**Example Usage:**

```yaml
config-version: 2
```

### `profile`

**Description:** The profile your dbt project should use to connect to your data warehouse.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | required | none | (variable, depends on organization and warehouse names) |

**Additional Information:**

- Often an organization has only one data warehouse, so it is sensible to use your organization's name as a profile name, in snake_case.
- The inclusion of the warehouse technology name in the profile is also deemed reasonable, particularly when multiple warehouses are involved. For example:

**Example Usage:**

```yaml
profile: tmdc  
#or 
profile: tmdc_bigquery 
```

### `model-paths`

**Description:** Optionally specify a custom list of directories where models and sources are located.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of strings | mandatory | ["models"] | [directory path] |

**Additional Information:**

- By default, dbt will search for models and sources in the models directory.

**Examples:**

- Use a sub directory named `transformations` instead of models.

```yaml
model-paths: ["transformations"]

#or

model-paths: 
	- transformations
```

- **optional paths like seed, analyses, tests:**
    
    ### `seed-paths`
    
    **Description:** Optionally specify a custom list of directories where seed files are located.
    
    | Data Type | Requirement | Default Value | Possible Value |
    | --- | --- | --- | --- |
    | list of strings | optional | ["seeds"] | [directory path] |
    
    **Additional Information:**
    
    - By default, dbt expects seeds to be located in the seeds directory.
    - Co-locate your models and seeds in the models directory (Note: this works because dbt is looking for different file types for seeds (.csv files) and models (.sql files)).
    
    **Examples:**
    
    - Use a subdirectory named `custom_seeds` instead of seeds.
    
    ```yaml
    seed-paths: ["custom_seeds"]
    ```
    
    - Split your seeds across two directories (Note: We recommend that you instead use two subdirectories within the seeds/ directory to achieve a similar effect).
    
    ```yaml
    seed-paths: ["seeds", "custom_seeds"]
    ```
    
    ### `test-paths`
    
    **Description:** Optionally specify a custom list of directories where singular tests are located.
    
    | Data Type | Requirement | Default Value | Possible Value |
    | --- | --- | --- | --- |
    | list of strings | optional | ["tests"] | [directory-path] |
    
    **Additional Information:**
    
    - Without specifying this config, dbt will search for tests in the tests directory. Specifically, it will look for .sql files containing:
        - Generic test definitions in the tests/generic sub directory.
        - Singular tests (all other files).
    
    **Examples:**
    
    - Use a sub directory named `custom_tests` instead of tests for data tests.
    
    ```yaml
    test-paths: ["custom_tests"]
    ```
    
    ### `analysis-paths`
    
    **Description:** Specify a custom list of directories where analyses are located.
    
    | Data Type | Requirement | Default Value | Possible Value |
    | --- | --- | --- | --- |
    | list of strings | optional | [analyses] | [directorypath] |
    
    **Additional Information:**
    
    - Without specifying this config, dbt will not compile any `.sql` files as analyses.
    
    **Examples:**
    
    - Use a subdirectory named `analyses` (This is the value populated by the dbt init command).
    
    ### `macro-paths`
    
    **Description:** Optionally specify a custom list of directories where macros are located. Note that you cannot co-locate models and macros.
    
    | Data Type | Requirement | Default Value | Possible Value |
    | --- | --- | --- | --- |
    | list of directory paths | optional | ["macros"] | [directorypath] |
    
    **Additional Information:**
    
    - By default, dbt will search for macros in a directory named `macros`.
    
    **Examples:**
    
    - Use a subdirectory named `custom_macros` instead of `macros`.
    
    ```yaml
    macro-paths: ["custom_macros"]
    ```
    
    ### `snapshot-paths`
    
    **Description:** Optionally specify a custom list of directories where snapshots are located. Note that you cannot co-locate models and snapshots.
    
    | Data Type | Requirement | Default Value | Possible Value |
    | --- | --- | --- | --- |
    | list of strings | optional | ["snapshots"] | [directorypath] |
    
    **Examples:**
    
    - Use a subdirectory named `archives` instead of `snapshots`.
    
    ```yaml
    snapshot-paths: ["archives"]
    ```
    
    ### `docs-paths`
    
    **Description:** Optionally specify a custom list of directories where docs blocks are located.
    
    | Data Type | Requirement | Default Value | Possible Value |
    | --- | --- | --- | --- |
    | list of strings | optional | [”docs”] | [directory path] |
    
    **Additional Information:**
    
    - By default, dbt will search in all resource paths for docs blocks (i.e. the combined list of `model-paths`, `seed-paths`, `analysis-paths`, `macro-paths`, and `snapshot-paths`). If this option is configured, dbt will only look in the specified directory for docs blocks.
    
    **Example:**
    
    - Use a sub directory named `docs` for docs blocks:
    
    ```yaml
    docs-paths: ["docs"]
    ```
    
    ### `target-path`
    
    **Description:** Optionally specify a custom directory where compiled files (e.g., compiled models and tests) will be written .
    
    | Data Type | Requirement | Default Value | Possible Value |
    | --- | --- | --- | --- |
    | list of strings | optional | "target" | [directorypath] |
    
    **Examples:**
    
    - Specify a sub directory using the project config file.
    
    ```yaml
    target-path: "compiled_files"s
    ```
    

## dbt_package section:

### `packages`

**Description**: define dbt project to run as a dbt package

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| mapping | mandatory | "target" | [directorypath] |

### `git`

**Description:** A attribute within the `packages.yml` configuration file for dbt projects, specifying the Git repository URL. It plays a key role in defining the source for dbt packages

```yaml
dbt_packages:
	packages:
	  - git: "https://github.com/dbt-labs/dbt-utils.git" # git URL
	    revision: dev # tag or branch name ( to be tested)
```
