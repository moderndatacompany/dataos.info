
# Database: First Steps

## Create a Database

To create a Database, the first step is to create a Database manifest file. But before creating a Worker Resource, ensure you have required use-cases assigned.

### **Get Appropriate Access Permission Use Case**

In DataOS, different actions require specific use cases that grant the necessary permissions to execute a task. You can grant these use cases directly to a user or group them under a tag, which is then assigned to the user. The following table outlines various actions related to Worker Resources and the corresponding use cases required:

| **Action** | **Required Use Cases** |
|------------|------------------------|
| Get        | Read Workspaces, Read Resources in User Specified Workspace / Read Resources in User Workspaces (for public and sandbox workspaces) |
| Create     | Create and Update Resources in User Workspace       |
| Apply      | Create and Update Resources in User Workspace          |
| Delete     | Delete Resources in User Workspace               |
| Log        | Read Resource Logs in User Workspace                 |

To assign use cases, you can either contact the DataOS Operator or create a Grant Request by creating a Grant Resource. The request will be validated by the DataOS Operator.

### **Create a manifest file**

To create a Database Resource, data developers can define a set of attributes in a manifest file, typically in YAML format, and deploy it using the DataOS Command Line Interface (CLI) or API. Below is a sample manifest file for Database Resource:

???note "Sample Database manifest"

    ```yaml title="sample_worker.yml"
    --8<-- "examples/resources/database/database.yaml"
    ```


The manifest for creating a Database has the following two sections, , each requiring specific configuration:

- [Resource meta section](#resource-meta-section)
- [Database-specific Section](#database-specific-section)

#### **Resource meta section**

In DataOS, a Database is categorized as a Resource-type. The Resource meta section within the manifest file encompasses attributes applicable to all Resource-types. The provided manifest file elucidates the requisite attributes for this section:

=== "Syntax"

    ```yaml
    #Attribtues for Resource
    name: ${resource-name}                #database_name 
    version: v1                           
    type: database                        
    description: ${description}
    tags:
      - ${tag1}
      - ${tag2}
    owner: ${iamgroot}
    layer: ${user}
    database: 
      #database specific mapping(mandatory)
    ```
=== "Sample"

    ```yaml
    #Attribtues for Resource
    name: products_db
    version: v1                           #database_name 
    type: database                        
    description: product database created for testing.
    tags:
      - database
    database: #database specific mapping(mandatory)
    owner: iamgroot
    layer: user 
    ```

To configure a Database Resource, replace the values of `name`, `layer`, `tags`, `description`, and `owner` with appropriate values. For additional configuration information about the attributes of the Resource meta section, refer to the link: [Attributes of Resource meta section](/resources/resource_attributes/).

#### **Database-specific section**

The Database-specific section of a Database manifest comprises attributes-specific to the Database Resource.


=== "Syntax"

    ```yaml
    database:                            # Specify the resource type
      migrate:
        includes:
          - ${migration-directory}     # Address to all migrations (relative path)
        includesInline:
          migration: |
            ${migration_script}

        command: ${migration-command}   # ("up" or "down")
      compute: runnable-default
    ```
=== "Sample"

    ```yaml
    database:                            # Specify the resource type
      migrate:
        includes:
          - migrations/  
        includesInline:
          migration: |                    # Address to all migrations (relative path)
            CREATE TABLE Product (
            id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(100),
            price DECIMAL(10, 2),
            description TEXT);
        command: up  # Specify the migration command (e.g., "up" or "drop table")
      compute: runnable-default
    ```


**Migrate Configuration**

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

There are two ways to define migrations: .

- Embed an external directory for migration.
- Provide the migration within the Database manifest.

===  "External to manifest"

    To embed an external scripts for migration, create a folder with name say `migration`. In your migration folder, create a new SQL file, e.g., `001_migration_up.sql`, and write the migration script to define the changes to the Database schema.

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

      Inline migration involves embedding migration logic directly within the manifest file. While simpler to implement for small projects, it may lead to complexity for long complex migrations.


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

!!!info "📖 Best Practice"

      - Numeric Prefixing:
          Prefix filenames with a numeric sequence for a clear execution order.
      - File Naming Format:
          Use `<anything>.up.sql` and `<anything>.down.sql` for migration files.

      - Example:

      ```sql
      001_initialize.up.sql
      001_initialize.down.sql
      002_add_column.up.sql
      002_add_column.down.sql
      003_update_data.up.sql
      003_update_data.down.sql
      ```          
<center>![Database migration](/resources/database/migration.png)</center>
<center><i>Database Migration </i></center>

### **Apply the Database manifest**

After successfully creating the Database manifest, it’s time to apply manifest. To apply the Database manifest, utilize the `apply` command.

=== "Command"

    ```bash
    dataos-ctl resource apply -f ${manifest-file-path} -w ${workspace-name}
    ```

=== "Example"

    ```bash
    dataos-ctl resource apply -f database.yaml -w curriculum
    # Expected Output
    INFO[0000] 🛠 apply...                                   
    INFO[0000] 🔧 applying(curriculum) products_db:v1:database... 
    INFO[0027] 🔧 applying(curriculum) products_db:v1:database...created 
    INFO[0027] 🛠 apply...complete
    ```

## Manage a Database

### **Verify Database creation**

To check the successful creation of Database in DataOS Workspace use the following two methods:

- **Check the Database in a Workspace:** Use the following command to list the created Database in a specific Workspace:

=== "Command"

    ```bash
    dataos-ctl resource get -t database -w ${workspace-name} 
    ```

=== "Example"

    ```bash
    dataos-ctl resource get -t database -w curriculum

    # Expected Output
    |    NAME     | VERSION |   TYPE    |  WORKSPACE  | STATUS | RUNTIME |     OWNER       |
    |-------------|---------|-----------|-------------|--------|---------|-----------------|
    | products_db  |   v1    | database  | curriculum  | active |         | iamgroot |
    ```
If the status is ‘active’, re run or use `-r` to refresh the command to get runtime as ‘succeeded’.

- **Retrieve all Databases in a Workspace:**

To retrieve the list of all Databases created in the Workspace, add the `-a` flag to the command:
 
=== "Command"
     ```shell
     dataos-ctl resource get -t database -w ${workspace-name} -a
     ```

=== "Example"
     ```shell
     dataos-ctl resource get -t database -w curriculum -a
     ```

### **Getting Database logs**

  ```shell
  dataos-ctl resource get -t database -w curriculum -n products_db -d
  ```

### **Deleting a Database**

As part of best practices, it is recommended to regularly delete Resources that are no longer in use. This practice offers several benefits, including saving time and reducing costs.

There are 3 ways to delete Database(or any Resource):



There are 3 ways to delete Service(or any Resource):

=== "Method 1"

    === "Command"

        ```shell
        dataos-ctl delete -t ${database} -n ${name of database} -w ${name of workspace}
        ```
    === "Example"

        ```shell
        dataos-ctl delete -t service -n products_db -w curriculum
        ```

=== "Method 2"

    === "Command"

        ```shell
        dataos-ctl delete -i ${name of database in the output table from get status command}
        ```
    === "Example"

        ```shell
        dataos-ctl delete -i "products_db  | v1 | database | curriculum"
        ```

=== "Method 3"

    
    === "Command"

        ```shell
        dataos-ctl delete -f ${file-path}
        ```
    === "Example"

        ```shell
        dataos-ctl delete -f home/iamgroot/database/database_product.yml
        ```

## **Create a Beacon Service**

Create a [Beacon](/resources/stacks/beacon) Service to expose the PostgreSQL database on API. The syntax for the Beacon Service manifest file is provided below:

```yaml title="service.yaml" hl_lines="14"
--8<-- "examples/resources/database/service.yaml"
```
For detailed customization options and additional attributes of the Service Resource Section, refer to the link [Attributes of Service Section](/resources/service/configuration).

### **Apply the Service manifest**

=== "Command"

    ```bash
    dataos-ctl resource apply -f ${service file name} -w ${workspace-name} 
    ```

=== "Example"

    ```bash
    dataos-ctl resource apply -f products-service.yaml -w curriculum
    ```

### **Verify Service creation**

To check the successful completion of Service use the following command:

```bash
dataos-ctl resource get -t service -w curriculum
```
Expected output

```bash
  		NAME      | VERSION |  TYPE   | WORKSPACE | STATUS |  RUNTIME  |     OWNER       
----------------|---------|---------|-----------|--------|-----------|-----------------
  employee-test | v1      | service | curriculum   | active | running:1 | iamgroot
  product-test  | v1      | service | curriculum   | active | running:1 | iamgroot  
  products-test | v1      | service | curriculum   | active | running:1 | iamgroot
```

you can now access the PostgreSQL database using the exposed API by

To validate the outcome, execute a request to the designated URL:

=== "Syntax"

    ```shell
    https://<dataos_fqdn>/<database_path>/<table_name>
    ```

=== "Example"

    ```shell
    https://liberal-donkey.dataos.app/products_db/api/v1/products
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

### **Deleting a Service**

As part of best practices, it is recommended to regularly delete Resources that are no longer in use. This practice offers several benefits, including saving time and reducing costs.

There are 3 ways to delete Service(or any Resource):

=== "Method 1"

    === "Command"

        ```shell
        dataos-ctl delete -t ${service} -n ${name of service} -w{workspace}
        ```
    === "Example"

        ```shell
        dataos-ctl delete -t service -n products-service -w curriculum
        ```

=== "Method 2"

    === "Command"

        ```shell
        dataos-ctl delete -i ${name of service in the output table from get status command}
        ```
    === "Example"

        ```shell
        dataos-ctl delete -i "products-service  | v1 | service | curriculum"
        ```

=== "Method 3"

    
    === "Command"

        ```shell
        dataos-ctl delete -f ${file-path}
        ```
    === "Example"

        ```shell
        dataos-ctl delete -f home/iamgroot/database/service.yml
        ```

## Next Steps

Database Resource is used to store data on the fly. Your next steps depend upon whether you want to learn about what you can do with the database,  here are some how to guides to help you with that process:

- [How to query database data using workbench?](/resources/database/how_to_guide/query_database)

