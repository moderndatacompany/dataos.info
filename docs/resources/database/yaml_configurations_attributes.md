# Attributes of Database manifest

**Structure of Database YAML configuration**

**Attributes configuration**

`database` 

**Description:** The `database` attribute is used to define a Database Resource in YAML. This mapping defines the configuration for a Database within the DataOS environment.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| mapping | mandatory | none | none |

**Example Usage:**

```yaml
database:
    {} # database attributes go here
```

`migrate`

**Description:** Configures database migration settings, allowing the application of changes to the database schema over time for seamless updates as the application evolves. It specifies the directory and command for managing migrations.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| list of mapping | mandatory | none | none |

**Example Usage:**

```yaml
migration:
	include:
	command:
```

`includes`

**Description:** Points to the directory (`products_migration/`) containing all migration files. These files provide instructions for modifying the database schema, enabling organized management of database changes and versioning.

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | any valid path |

**Example usage:**

```yaml
includes:
	- {{ my_migrations/}}
```

`includesInline`

**Description:** It is an object property that uses a pattern property to allow keys of any string and values that must be strings. It is used to represent inline or embedded migration scripts directly within the configuration.

| Property | Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- | --- |
| includesInline | object | optional | none | Key-value pairs of strings |

**Example usage:**

```yaml
includesInline:
  script1: "CREATE TABLE users (id SERIAL PRIMARY KEY, name VARCHAR(255));"
  script2: "ALTER TABLE users ADD COLUMN email VARCHAR(255);"
```

`command`

**Description:** Specifies the type of migration operation to be performed. In this case, "up" signifies applying migrations. Adjust accordingly for rollback operations, such as "down".

| Data Type | Requirement | Default Value | Possible Value |
| --- | --- | --- | --- |
| string | mandatory | none | up/down |

**Example usage:**

```yaml
migrate:
	command:up/down
```