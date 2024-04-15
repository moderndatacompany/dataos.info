# Attributes of Database manifest

**Structure of Database manifest**
```yaml
database:
  migrate:                  #mandatory
    includes: 
      - migrations/     # all up & down sql files.
    includesInline: |
      "CREATE TABLE users (
      id SERIAL PRIMARY KEY,
      username VARCHAR(50) NOT NULL,
      email VARCHAR(100) NOT NULL"
    command: up           # in case of drop table, write down.  
    parameter: example
  manageAsUser: iamgroot        #string       
```

**Database-specific section Attributes**

## `database` 

**Description:** The database attributes is a mapping that defines the configuration for a Database within the DataOS environment.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| mapping | mandatory | none | none |

**Example Usage:**

```yaml
database:
  migrate:                  #mandatory
    includes: 
      - migrations/     # all up & down sql files.
    command: up           # in case of drop table, write down.  
   # database attributes go here
```

#### **`migrate`**

**Description:** Configures database migration settings, allowing the application of changes to the database schema over time for seamless updates as the application evolves. It specifies the directory and command for managing migrations.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| mapping | mandatory | none | none |

**Example Usage:**

```yaml
migrate:
	includes:
    	- ${ my_migrations/}
	command: up
```

##### **`includes`**

**Description:** Points to the directory (`products_migration/`) containing all migration files. These files provide instructions for modifying the database schema, enabling organized management of database changes and versioning.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| list of string | optional | none | valid migration file path |

**Example usage:**

```yaml
includes:
	- ${ my_migrations/}
```

##### **`includesInline`**

**Description:** It is an object property that uses a pattern property to allow keys of any string and values that must be strings. It is used to represent inline or embedded migration scripts directly within the configuration.

It is used to represent inline or embeed migration scripts directly within the configuration in the form of key-value pairs, where key represent the name of the migration and value is the migration script

| Property | Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- | --- |
| includesInline | mapping | optional | none | Key-value pairs  |

**Example usage:**

```yaml
includesInline:
  script1: "CREATE TABLE users (id SERIAL PRIMARY KEY, name VARCHAR(255));"
  script2: "ALTER TABLE users ADD COLUMN email VARCHAR(255);"
```

##### **`command`**

**Description:** The command attribute in databases involves up and down commands. up applies schema changes for version transition, while down reverts changes, crucial for rollbacks to previous versions.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | up/down |

**Example usage:**

```yaml
migrate:
  command: down
```

##### **`parameter`**

**Description:** 


| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | optional | none | none |


**Example usage:**

```yaml
migrate:
	parameter: 3
```

#### **`manageAsUser`**

**Description:** When the manageAsUser attribute is configured with the UserID of the use-case assignee, it grants the authority to perform operations on behalf of that user. 

| Data Type | Requirement | Default Value | Possible Value                  |
|-----------|-------------|---------------|---------------------------------|
| string    | optional    | none          | userID of the Use Case Assignee |

**Example usage:**

```yaml
manageAsUser: iamgroot
```