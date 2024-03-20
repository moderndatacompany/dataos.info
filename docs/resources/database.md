# :resources-database: Database

A Database Resource [Resource](/resources/) in DataOS ct as a repository for storing transaction data, utilizing a managed Postgres relational database. It fulfills the transactional data storage needs of custom data applications developed on top of DataOS. Internal applications like Lens, Metis, etc., also leverage the Database Resource for their transactional data storage. Utilizing a [Service](./service.md) supported by the [Beacon Stack](./stacks/beacon.md)facilitates CRUD operations (Create, Read, Update, Delete) on data assets stored in the Database, ensuring smooth connectivity between the data application and the Database. For analytical operations, users can utilize the [Flare Stack](./stacks/flare.md)to move the data from transactional data storage to other [Depots](./depot.md) or [Lakehouses](./lakehouse.md).

<aside class=”callout”>

A Database is a Workspace-level Resource-type, implying that its scope is limited to a particular Workspace.

</aside>


<div class="grid cards" markdown>

-   :material-card-bulleted-settings-outline:{ .lg .middle } **How to create and manage a Database?**

    ---

    Learn how to create and manage a Database in DataOS.

    [:octicons-arrow-right-24: Create and Manage Database](#how-to-create-and-manage-a-database)


-   :material-list-box-outline:{ .lg .middle } **How to create and manage a Database?**

    ---

    Learn how to create a database yaml specific to PostgreSQL.

    [:octicons-arrow-right-24: Create a Database](#how-to-create-a-database)

-   :material-network-pos:{ .lg .middle } **Possible Errors**

    ---

    Discover potential errors and solutions for each

    
    [:octicons-arrow-right-24: Possible Errors](#possible-errors)

-   :material-content-duplicate:{ .lg .middle } **Case Scenarios**

    ---

    Understand a end to end use case of using a database

    [:octicons-arrow-right-24:  Possible errors](#case-scenarios)

</div>



## Key Features of Database

### **Transactional Data Storage**

A Database serves as a Resource, guaranteeing systematic storage of data generated and consumed by various applications within DataOS. The Beacon Service, through its exposed API endpoints, facilitates a seamless connection between applications and the Database, fostering a resourceful data storage hub.

### **CRUD Operations for Data Assets**

The Beacon Service enables CRUD operations (Create, Read, Update, Delete) on data assets stored in the PostgreSQL database. This functionality is pivotal for applications within DataOS to manipulate and interact with the underlying data efficiently.

To learn more about the Beacon refer [Becon Resource](/resources/stacks/beacon/#configure-beacon-stack-specific-section)


## How to Create and Manage a Database?

To create a Database Resource specific to PostgreSQL define a YAML configuration file create a dedicated folder `migration` to store all Database migration files.

### **Create a Migration File**

Creating a migration in SQL typically involves defining changes to a Database schema, such as creating or altering tables, adding or modifying columns, or establishing relationships between tables.

In your migration folder, create a new SQL file, e.g., `001_migration_up.sql`, and write the migration script to define the changes to the Database schema.

**Database Migrations**

=== "Up Migration"

    The "up" migration is responsible for applying changes to the database schema, facilitating the transition to a newer version. 

    ```sql
    -- Creating a new table
    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        email VARCHAR(100) NOT NULL
    );

    -- Adding a new column to an existing table
    ALTER TABLE users
    ADD COLUMN published_at TIMESTAMP;
    ```
=== "Down Migration"

    Conversely, the "down" migration serves the purpose of reverting changes made by the "up" migration. This is crucial for scenarios requiring a rollback to a previous version. 

    ```sql
    -- Dropping the new table
    DROP TABLE IF EXISTS users;

    -- Removing the added column
    ALTER TABLE users
    DROP COLUMN IF EXISTS published_at;
    ```

???note "Example Database migration"

    ```sql  title="initial.up.sql"
    CREATE TABLE IF NOT EXISTS products(

        sproduct_id SERIAL PRIMARY KEY,
        product_name VARCHAR(100) NOT NULL,
        category VARCHAR(50),
        price NUMERIC(10, 2) NOT NULL,
        stock_quantity INT NOT NULL,
        description TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    ```
    ```sql title="insert.up.sql"
    INSERT INTO products (id, product_name, category, price, stock_quantity)
    VALUES
      (1, 'Laptop', 'Electronics', 999.99, 20),
      (2, 'Smartphone', 'Electronics', 499.99, 30),
      (3, 'Coffee Maker', 'Appliances', 79.99, 15),
      (4, 'Running Shoes', 'Apparel', 59.99, 25),
      (5, 'Backpack', 'Accessories', 39.99, 40);
    ```


!!!info "📖 Best Practice"

    - Numeric Prefixing:
        Prefix filenames with a numeric sequence for a clear execution order.
    - File Naming Format:
        Use `<anything>.up.sql` and `<anything>.down.sql` for migration files.
    - Serialization for Multiple Operations:
        Serialize filenames when multiple operations are needed for the same update.

    - Example:

    ```sql
    001_initialize.up.sql
    001_initialize.down.sql
    002_add_column.up.sql
    002_add_column.down.sql
    003_update_data.up.sql
    003_update_data.down.sql
    ```


### **Create a manifest file**

A sample Database mainfest file is given below:

???note "Example Database manifest"

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

    2.  [Database-specific section](#database-specific-section) within a manifest file comprises attributes specific to the Database Resource. To learn more about how to configure attributes of Database-specific section, refer the 



The YAML configuration file for creating a Database has the following sections:

- [Resource meta section](#resource-meta-section)
- [Database-specific Section](#database-specific-section)


<!-- **Configuring the Resource meta section** -->

Resource meta section is common for declaring all kinds of resources in DataOS however the version, name and type change according to resource type but are mandatory fields

#### **Resource meta section**

Resource meta section is common for declaring all kinds of resources in DataOS however the version, name and type change according to resource type but are mandatory fields. The provided codeblock elucidates the requisite attributes for this section:

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

This section is intended for defining database migration settings within the resource section of DataOS. Crucial fields like migrate, includes are mandatory. The configuration allows you to specify the migration directory and command (e.g., "up" or "drop table") for effective management of database schema changes.

The below YAML provides a high-level structure for the Database-specific section:

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

| Attribute   | Data Type | Default Value                             | Possible Value                  | Requirement |
|-------------|-----------|-------------------------------------------|---------------------------------|-------------|
| `database`  | object  | none                                      | none                            | mandatory   |
| `migrate`   | object  | none                                      | none                            | mandatory   |
| `includes`  | string  | none                                      | none                            | mandatory   |
| `command`   | string  | none                                      | none                            | mandatory   |
| `description` | string | none                                      | none                            | optional    |
| `owner`     | string  | ID of the user who deploys the Resource  |                                 | optional    |
| `layer`     | string  | user                                      |                                 | optional    |

For more information about the below attributes, refer to the link [Attributes of Database](./database/yaml_configurations_attributes.md)

#### **Apply the Database manifest**

After successfully creating the Database YAML file, it’s time to apply manifest to the resource-workspace in the DataOS environment. To apply the Database YAML file, utilize the `apply` command.

=== "Command"

    ```bash
    dataos-ctl apply -f ${yaml-file-path} -w ${workspace-name}
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

- **Retrieve All Databases in a Workspace:** To retrieve the list of all Databases created in the Workspace, add the `-a` flag to the command:
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

#### **Verify Creation**

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

#### **Validate the outcome**

To validate the outcome, execute a request to the designated URL:

=== "Syntax"

    ```shell
    https://${current_enviroment}.dataos.app/${table_name}/api/v1
    ```

=== "Example"

    ```shells
    https://humorous-adder.dataos.app/product/api/v1
    ```

This action will enable verification of the expected result by accessing the provided endpoint.


#### **Accessing Data**

To view the contents of the newly established database, simply extend the API endpoint with /tablename in browser.

=== "Syntax"

    ```shell
    https://humorous-adder.dataos.app/${database_name}/api/v1/${tablename}
    ```
=== "Example"

    ```shell
    https://humorous-adder.dataos.app/product_db/api/v1/products
    ```
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

To delete a Service replace type with Service

## Possible Errors


## Case Scenarios

- []