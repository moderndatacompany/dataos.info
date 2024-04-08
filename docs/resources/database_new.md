# :resources-database: Database

A Database [Resource](/resources/) in DataOS acts as a repository for storing transaction data, utilizing a managed Postgres relational database. It fulfills the transactional data storage needs of custom data applications developed on top of DataOS. Internal applications like [Lens](/docs/interfaces/lens.md), Metis, etc., also leverage the Database Resource for their transactional data storage. Utilizing a [Service](./service.md) supported by the [Beacon Stack](./stacks/beacon.md) facilitates CRUD operations (Create, Read, Update, Delete) on data assets stored in the Database, ensuring smooth connectivity between the data application and the Database. For analytical operations, users can utilize the [Flare Stack](./stacks/flare.md)to move the data from transactional data storage to other [Depots](./depot.md) or [Lakehouses](./lakehouse.md).

![Check Database](/resources/database/databases.png)
<center><i>Database Resource</i></center>

???info "Info"

    A Database is a Workspace-level Resource-type, implying that its scope is limited to a particular Workspace.


<div class="grid cards" markdown>

-   :material-card-bulleted-settings-outline:{ .lg .middle } **How to create and manage a Database?**

    ---

    Learn how to create and manage a Database in DataOS.

    [:octicons-arrow-right-24: Create and Manage Database](#how-to-create-and-manage-a-database)


-   :material-network-pos:{ .lg .middle } **How to configure a database manifest file?**

    ---

    Discover how to configure a Database manifest file by adjusting its attributes.

    
    [:octicons-arrow-right-24: Database Attributes](./database/yaml_configurations_attributes.md)


-   :material-list-box-outline:{ .lg .middle } **Possible Errors**

    ---

    Explore common errors encountered during configuration and troubleshooting strategies.


    [:octicons-arrow-right-24: Explore possible errors](#possible-errors)


-   :material-content-duplicate:{ .lg .middle } **Database Usage Example**

    ---

    Explore examples showcasing the usage of Database in various scenarios.


    [:octicons-arrow-right-24:  Database Usage Examples](#database-usage-examples)

</div>


## How to Create and Manage a Database?

To create a Database in DataOS, follow the below steps:

 - Create a Database manifest file
 - Apply the Database manifest file
 - Verify Database creation


### **Create a Database manifest file**

A sample Database mainfest file is given below:

???note "Example Database manifest"
 
    === "Embeded migration"

          ```yaml
          # Resource-meta section (1)
          name: product_db   #database name
          version: v1                      
          type: database
          description: product_db database created for testing.
          tags:
              - database
          # Database specific section (2)
          database:
          migrate:
              includes:
                  - migrations/     # all up & down sql files.
              command: up           # in case of drop table, write down.
          ```

        1.  [Resource meta section](#resource-meta-section) within a manifest file comprises metadata attributes universally applicable to all [Resource-types](/resources/types_of_dataos_resources/). To learn more about how to configure attributes within this section, refer to the link: [Attributes of Resource meta section](/resources/resource_attributes/).

        2.  [Database-specific section](#database-specific-section) within a manifest file comprises attributes specific to the Database Resource. To learn more about how to configure attributes of Database-specific section, refer the [Attributes of Database-specific section](./database/database_manifest_attributes.md)


The YAML configuration file for creating a Database has the following sections:

- [Resource meta section](#resource-meta-section)
- [Database-specific Section](#database-specific-section)

#### **Resource meta section**

In DataOS, a Database is categorized as a [Resource-type](./types_of_dataos_resources.md). The Resource meta section within the YAML manifest encompasses attributes universally applicable to all Resource-types. The provided YAML codeblock elucidates the requisite attributes for this section:

=== "Syntax"

    ```yaml
    #mandatory attribtues for Resource
    name: ${resource-name}
    version: v1                           #database_name 
    type: database                        
    description: ${description}
      - ${tag1}
      - ${tag2}
    database: 
      #database specific mapping(mandatory)
    ```
=== "Sample"

    ```yaml
    #mandatory attribtues for Resource
    name: products_db
    version: v1                           #database_name 
    type: database                        
    description: product database created for testing.
    tags:
      - database
    database: #database specific mapping(mandatory)
    ```

For more information about the various attributes in Resource meta section, refer to the [Attributes of Resource meta section.](https://dataos.info/resources/resource_attributes/)

#### **Database-specific section**

The Database-specific section of a Database manifest comprises attributes-specific to the Database Resource.


=== "Syntax"

    ```yaml
    database:                            # Specify the resource type
      migrate:
        includes:
          - {{migration-directory}}     # Address to all migrations (relative path)
        command: {{migration-command}}   # Specify the migration command (e.g., "up" or "drop table")
    ```
=== "Sample"

    ```yaml
    database:                            # Specify the resource type
      migrate:
        includes:
          - migrations/    # Address to all migrations (relative path)
        command: up  # Specify the migration command (e.g., "up" or "drop table")
    ```
The table below describes the various attributes used for defining conditions:

| Attribute          | Data Type | Default Value | Possible Values                 | Requirement |
|--------------------|-----------|---------------|---------------------------------|-------------|
| `database`(./database/database_manifest_attributes.md#database)        | object    | none          | none                            | mandatory   |
| `migrate`(./database/database_manifest_attributes.md#migrate)       | object    | none          | none                            | mandatory   |
| `includes`(./database/database_manifest_attributes.md#includes)         | string    | none          | any valid path                  | mandatory   |
| `includesInline`(./database/database_manifest_attributes.md#includesInline)   | object    | none          | Key-value pairs of strings      | optional    |
| `command`(./database/database_manifest_attributes.md#)          | string    | none          | up/down                         | mandatory   |
| `parameter`(./database/database_manifest_attributes.md#parameter)        | string    | none          | none                            | optional    |


For more information about the below attributes, refer to the link [Attributes of Database](./database/yaml_configurations_attributes.md)


#### **Migrate Configuration**

The migration in Database Resource typically involves defining changes to a Database schema, such as creating or altering tables, adding or modifying columns, or establishing relationships between tables.

???note "Example migration"

    ```sql  title="001_create.up.sql"

        CREATE TABLE user (
        user_id INT PRIMARY KEY,
        username VARCHAR(50),
        email VARCHAR(100),
        created_at TIMESTAMP
        );
    ```
    ```sql title="002_insert.up.sql"
        INSERT INTO user (user_id, username, email, created_at) VALUES
        (1, 'JohnDoe', 'john@example.com', '2024-03-29 10:00:00'),
        (2, 'JaneSmith', 'jane@example.com', '2024-03-29 11:00:00'),
        (3, 'AliceJones', 'alice@example.com', '2024-03-29 12:00:00');

        -- Removing the added column
        ALTER TABLE users
        DROP COLUMN IF EXISTS created_at;
    ```
    ``` sql title="0021_drop.down.sql"
    -- Dropping the new table
        DROP TABLE IF EXISTS users;
    ```

These comprises of two ways to define migrations in migration attribute.

- Embed an external directory for migration.
- Provide the migration within the Database manifest.

===  "External to manifest"

    To embed an external scripts for migration, create a folder with name `migration`. In your migration folder, create a new SQL file, e.g., `001_migration_up.sql`, and write the migration script to define the changes to the Database schema.

    === "Syntax"

          ```yaml
          migrate:
            includes:
              - ${migration_folder_path}  #address to all migrations
          ```
    === "Example"
        
          ```yaml
          migrate:
            includes:
              - migration/
          ```

===  "Embedded within manifest"

      Inline migration involves embedding migration logic directly within the application 
      code or database management tool. While simpler to implement for small projects, it may lead to complexity for long complex migrations.


    === "Syntax"

        ```yaml
        migrate:
          includesInline:
            migration: |
              ${sql script}
        ```

    === "Example"

        ```yaml
        migrate:
          includesInline:
            migration: |
              CREATE TABLE IF NOT EXISTS products(
              sproduct_id SERIAL PRIMARY KEY,
              product_name VARCHAR(100) NOT NULL,
              category VARCHAR(50),
              price NUMERIC(10, 2) NOT NULL,
              stock_quantity INT NOT NULL,
              description TEXT,
              created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
        ```


##### **command**

The migration attribute in Database consists of two commands, one to migrate `up` and another to migrate `down`. The `up` migration is responsible for applying changes to the database schema, facilitating the transition to a newer version. Conversely, the `down` migration serves the purpose of reverting changes made by the `up` migration. This is crucial for scenarios requiring a rollback to a previous version.


=== "Syntax"

      ```yaml hl_lines="5"
      database:                              
        migrate:
          includes:
              - migration/ 
          command: ${up}      # in case of drop table, write `down`
      ```


=== "Example"
      
      ```yaml hl_lines="5"
      database:                               
        migrate:
          includes:
              - migration/ 
          command: up        # in case of drop table, write `down`
      ```                 

![Database migration](/resource/database/migration.png)

#### **Apply the Database manifest**

After successfully creating the Database manifest, it’s time to apply manifest to the resource-workspace in the DataOS environment. To apply the Database manifest, utilize the `apply` command.

=== "Command"

    ```bash
    dataos-ctl resource apply -f ${manifest-file-path} -w ${workspace-name}
    ```

=== "Example"

    ```bash
    dataos-ctl resource apply -f database.yaml -w public
    # Expected Output
    INFO[0000] 🛠 apply...                                   
    INFO[0000] 🔧 applying(public) product_db:v1:database... 
    INFO[0027] 🔧 applying(public) product_db:v1:database...created 
    INFO[0027] 🛠 apply...complete
    ```

#### **Verify Database Creation**

To check the successful creation of database in DataOS use the following two methods:

- **Check Database in a Workspace:** Use the following command to list the  created by you in a specific Workspace:

=== "Command"

    ```bash
    dataos-ctl resource get -t database -w ${workspace-name} 
    ```

=== "Example"

    ```bash
    dataos-ctl resource get -t database -w public 
    # Expected Output
      NAME  | VERSION |   TYPE   | WORKSPACE | STATUS | RUNTIME |     OWNER       
    --------|---------|----------|-----------|--------|---------|-----------------
    product_db | v1      | database | public    | active |         | aayushisolanki  
    ```

If the status is ‘active’, re run or use `-r` to refresh the command to get runtime as ‘succeeded’.

- **Retrieve All Databases in a Workspace:**

To retrieve the list of all Databases created in the Workspace, add the `-a` flag to the command:
 
=== "Command"
     ```shell
     dataos-ctl resource get -t database -w ${workspace-name} -a
     ```

=== "Example"
     ```shell
     dataos-ctl resource get -t database -w public -a
     ```

### **Create a Policy**

We define the policy for allowing the authorized users to access the Database Resources and perform specified operations. For more information refer [Policy Resource](./policy.md)

!!! note "📌 Note" 
    The system level policy can only be applied by user with ‘Operator’ tag.


Policy YAML manifest

```yaml title="policy.yaml"
  --8<-- "examples/resources/policy/database_policy.yaml"
```
For detailed customization options and additional attributes of the Policy Resource Section, refer to the link [Attributes of Policy Section](./policy/yaml_configuration_attributes.md).


#### **Apply Policy manifest**

=== "Command"

    ```bash
    dataos-ctl resource apply -f <copied_relative_path_of_policy.yaml>  -w ${workspace-name}
    ```

=== "Example"

    ```bash
    dataos-ctl resource apply -f policy.yaml  -w public
    ```

### **Create a Service**

Create a Beacon Service to expose the PostgreSQL database on API. The syntax for the Beacon Service YAML is provided below:

```yaml title="service.yaml" hl_lines="14"
    --8<-- "examples/resources/service/database_service.yaml"
```
For detailed customization options and additional attributes of the Resource Section, refer to the link [Attributes of Service Section](./service/yaml_configuration_attributes.md).

#### **Apply the Service manifest**

=== "Command"

    ```bash
    dataos-ctl resource apply -f ${service file name} -w ${workspace-name} 
    ```

=== "Example"

    ```bash
    dataos-ctl resource apply -f beacon_service_up.yaml -w public 
    ```

#### **Verify Service Creation**

To check the successful completion of Service use the following command:

```bash
dataos-ctl resource get -t service -w public 
```

#### **Expected Output**

```bash
  		NAME      | VERSION |  TYPE   | WORKSPACE | STATUS |  RUNTIME  |     OWNER       
----------------|---------|---------|-----------|--------|-----------|-----------------
  employee-test | v1      | service | public    | active | running:1 | iamgroot
  product-test  | v1      | service | public    | active | running:1 | iamgroot  
  products-test | v1      | service | public    | active | running:1 | iamgroot
```

you can now access the PostgreSQL database using the exposed API by

To validate the outcome, execute a request to the designated URL:

=== "Syntax"

    ```shell
    https://${current_enviroment}.dataos.app/${database_path}/{table_name}
    ```

=== "Example"

    ```shells
    https://humorous-adder.dataos.app/products_db/api/v1/products
    ```
    #Expected Output
    ```json
        0
    id              1
    product_name    "Laptop"
    category        "Electronics"
    price           999.99
    stock_quantity  20
    1
    id              2
    product_name    "Smartphone"
    category        "Electronics"
    price           499.99
    stock_quantity  30
    ```

This action will enable verification of the expected result by accessing the provided endpoint.

### **Managing a Database**

#### **Debugging a Database**

When a Database creation or service encounters errors, data developers can employ various tactics to diagnose and resolve issues effectively. Here are the recommended debugging techniques:


- **Check Database and Service Logs**

  ```shell
  dataos-ctl resources get -t database -w public -n product_db -d
  ```
#### **Deleting a Database and Service**

As part of best practices, it is recommended to regularly delete Resources that are no longer in use. This practice offers several benefits, including saving time and reducing costs.

There are 3 ways to delete Database(or any Resource):

=== "Method 1"

    ```shell
    dataos-ctl delete -t ${database} -n ${name of depot}S
    ```

=== "Method 2"

    ```shell
    dataos-ctl delete -i ${name of database in the output table from get status command}
    ```

=== "Method 3"

    ```shell
    dataos-ctl delete -f ${file-path}
    ```

Similarly to delete a Service replace type with Service


## Possible Errors



### Dependency Error

During the deletion of a Database, several errors may arise, particularly when dependencies exist or due to various operational issues.

=== "Error"
        
      ```bash
      Error: Unable to delete the database 'force' as it is a dependency of 'service:v1:force-test:public'.
      ```
        
===  "Solution"

    Identify and eliminate the dependent service prior to Database deletion and delete it
    
      ```bash
      # Get status of services
      dataos-ctl get -t service -w public 

      # Delete the dependent service
      dataos-ctl resource delete -t service -n force-test 
      ```


## Database Usage Examples

- []