# Session information

Functions providing information about the query execution environment.

### **`current_user`**

| Function         | Description                          | Return Value    |
| ---------------- | ------------------------------------ | --------------- |
| `current_user`  | Returns the current user running the query. | User Name       |

### **`current_groups()`**

| Function           | Description                                   | Return Value    |
| ------------------ | --------------------------------------------- | --------------- |
| `current_groups()` | Returns the list of groups for the current user running the query. | List of Groups  |

### **`current_catalog`**

| Function         | Description                                        | Return Value    |
| ---------------- | -------------------------------------------------- | --------------- |
| `current_catalog`| Returns a character string representing the current catalog name. | Catalog Name    |

### **`currrent_schema`**

| Function         | Description                                        | Return Value    |
| ---------------- | -------------------------------------------------- | --------------- |
| `current_schema` | Returns a character string representing the current unqualified schema name. | Schema Name     |

> **Note:** This is part of the SQL standard and does not use parenthesis.