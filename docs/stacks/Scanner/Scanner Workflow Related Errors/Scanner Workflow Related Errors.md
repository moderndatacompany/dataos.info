# Scanner Workflow Related Errors

When you run a Scanner workflow, you may see errors that can affect the metadata scan. Here is a list of commonly encountered errors and their solutions.

## Error #1

Sometimes a user might get an ERROR 403 (Example Below) while running the Scanner Jobs.
 
<center>

![Picture](./Untitled_(5).png)

</center>

### Suggested Solution

To overcome this issue, we need to run the job as Metis user  `runAsUser: metis`

The following YAML displays the section where you need to add this information.

```yaml
version: v1
name: wf-bigquery-depot
type: workflow
tags:
  - bigquery-depot
description: The job scans schema tables and register data
workflow:
  dag:
    - name: bigquery-depot
      description: The job scans schema from bigquery-depot tables and register data to metis2
      spec:
        tags:
          - scanner
        stack: scanner:2.0
        compute: runnable-default
        runAsUser: metis                #run as Metis user
        scanner:
          depot: demoprepbq
          
```

## Error #2

While scanning PostgreSQL database metadata, If the user doesn't have login access for the underlying database, this error will be shown.

```bash

psycopg2.OperationalError: connection to server at "mebash.postgres.database.azure.com" (20.81.106.165), port 5432 failed: FATAL:  password authentication failed for user "ashish"
connection to server at "mebash.postgres.database.azure.com" (20.81.106.165), port 5432 failed: FATAL:  no pg_hba.conf entry for host "20.219.178.198", user "ashish", database "postgres", no encryption
```

### Suggested Solution

The user needs to have both `CONNECT` and `SELECT`  privileges on the database.

To check privileges:

```sql
SELECT table_catalog, table_schema, table_name, privilege_type
FROM   information_schema.table_privileges 
WHERE  grantee = 'MY_USER_Name'
```

## Error #3

If the user doesn't have access to the Database, then such an error will be thrown.

```bash
psycopg2.OperationalError: connection to server at "mebash.postgres.database.azure.com" (20.81.106.165), port 5432 failed: FATAL:  permission denied for database "ashish_access"
DETAIL:  User does not have CONNECT privilege.
```

### Suggested Solution

The user needs to have both `CONNECT` and `SELECT`  privileges on the database.

To check Privileges:

```sql
SELECT table_catalog, table_schema, table_name, privilege_type
FROM   information_schema.table_privileges 
WHERE  grantee = 'MY_USER_Name'
```

> 🗣 The errors thrown in the case of Redshift and PostgresSQL databases are mostly the same. Please check if you have enough permissions to scan the metadata from the underlying sources.

To learn more, refer to:

- [PostgreSQL Depot Scan](../Templates%20for%20Depot%20Scan/PostgreSQL%20Depot%20Scan.md) 

- [Redshift Depot Scan](../Templates%20for%20Depot%20Scan/Redshift%20Depot%20Scan.md) 

## Error #4

You may get the following error for value is not a valid enumeration member or extra fields not permitted.
 
<center>

![Picture](./MicrosoftTeams-image_(113).png)

</center>

### Suggested Solution

Check the `scanner` section of your YAML file. You have mistyped the property name or mentioned a property that does not exist. For example, if you enter `service` for the property `source`, you will get this error. Similarly, if you type depo instead of  `depot`, your Scanner workflow will not run and throw this error.

## Error #5

In case of Snowflake, you may get the following error while scanning data for warehouse is not configured for this depot.
 
<center>

![Picture](./MicrosoftTeams-image_(112).png)

</center>

### Suggested Solution

You encounter the above error when Snowflake depot is configured with a database name instead of a warehouse name. Please contact the DataOS administrator to fix this with the depot. You need the warehouse name in the Depot configuration YAML file for scanning metadata.

## Error #6

You will encounter this error when you try to scan unstructured data stored in File/blob storage.
 
<center>

![Picture](./MicrosoftTeams-image_(116).png)

</center>

> Note: At present, scanning the metadata of File Systems/Blob storage(Unstructured data) is not supported.