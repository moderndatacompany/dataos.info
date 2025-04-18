# Best Practices for Scanner Stack

## 1. Use Specific Filter Patterns

Filter patterns help limit the scope of scanned data. By using specific patterns, user can avoid scanning unnecessary databases, schemas, or tables, improving performance and security.

### **Correct Approach**

```yaml
databaseFilterPattern: 
  includes:
    - ^SNOWFLAKE.*
```

- This pattern ensures that only databases starting with **"SNOWFLAKE"** are scanned.

- Using anchored regex ( `^SNOWFLAKE.*` ) prevents unintentional matches.

**Avoid:**
Overly broad patterns that match unintended databases.

## 2. Avoid Using Wildcards at the End of Patterns

Wildcards (`.*`) at the end of filter patterns may match more than expected, leading to performance issues and unexpected results.

### **Correct Approach**

```yaml
databaseFilterPattern: 
  includes: 
    - ^SNOWFLAKE$
```

This ensures that **only** the database **SNOWFLAKE** is included, preventing unintended matches like `SNOWFLAKE_TEST` or `SNOWFLAKE_OLD`.

**Avoid:**

- Avoid specifying the exact names of databases, schemas, or tables without using regex. Any provided name will automatically be converted into a regex pattern with a wildcard appended, meaning that "SNOWFLAKE" will be interpreted as `^SNOWFLAKE.*.`

- `^SNOWFLAKE.*` could match `SNOWFLAKE_TEST`, `SNOWFLAKE_OLD`, etc., leading to unintended scans.

## 3. Exclude Specific Schemas and Tables

To prevent unnecessary scanning of known irrelevant schemas or tables, use **excludes** to filter them out.

### **Correct Approach**

```yaml
schemaFilterPattern: 
  excludes:
    - ^TPCH_SF100$
```

Excludes the `TPCH_SF100` schema from scanning, reducing processing overhead and avoiding unnecessary data collection.

**Avoid:**
Forgetting to exclude temporary, test, or irrelevant schemas.

## 4. Use Include and Exclude Properties with Caution

The `includes` and `excludes` properties are evaluated as an **OR** condition. Using both together can lead to unpredictable results.

Incorrect:

```yaml
tableFilterPattern: 
  includes: 
    - ^CUSTOMER.*
  excludes: 
    - ^CUSTOMER_JAN$
    - ^CUSTOMER_FEB$
```

This configuration includes **all tables starting with "CUSTOMER"**, but exclusions of CUSTOMER\_JAN and CUSTOMER\_JAN table do not override inclusions, leading to unintended behavior.

### **Correct Approach 1: Use only `includes`**

```yaml
tableFilterPattern: 
  includes: 
    - ^CUSTOMER.*
```

### **Correct Approach 2: Use only `excludes`**

```yaml
tableFilterPattern: 
  excludes: 
    - ^CUSTOMER_JAN$
    - ^CUSTOMER_FEB$
```

By following these best practices, users can:

- Improve **performance** by reducing unnecessary scans.

- Enhance **security** by filtering out sensitive or irrelevant data.

- Increase **accuracy** by avoiding unintended matches.