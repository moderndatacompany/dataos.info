# Working with user groups and data policies

Lens allows you to secure data in logical tables by defining data policies on their dimensions and segments. User groups are used to manage both data access and API scopes, which control access to specific functionalities and endpoints. This forms part of the access policy, ensuring users interact only with the data and features they are authorized to use.

Additionally, this governance extends to the Lens Studio Interface, where access to specific tabs and functionalities can be controlled. This setup helps in enforcing granular access controls and permissions, supporting compliance with organizational and regulatory standards.

## Procedure

Follow these steps to create and manage user groups:

### **Step 1** Create a `user_groups.yml` file in your model folder.

```latex
model/
├── sqls/
│   └── account.sql
├── tables/
│   └── account.yml
├── views/
│   └── engagement.yml
└── user_groups.yml
```

### **Step 2**  Define user groups using the following format:

```yaml
user_groups: # List of user groups
  - name: reader # Name of the group (check regex)
    description: # Description of the group
    api_scopes:
      - meta
      - data
      - graphql
      # - jobs
      # - source
    includes: # Users to include in this group
      - users:id:thor
      - users:id:ironman
    excludes: # Users to exclude from this group
      - users:id:blackwidow
```

| **Attribute** | **Description** | **Requirement** | **Best Practice** |
| --- | --- | --- | --- |
| `user_groups` | The top-level mapping contains the list of user groups. Each user group defines a set of users and respective access controls.  | mandatory |  |
| `name` | The name of the user group. | mandatory | - It should be unique and descriptive to identify the group's purpose, or role such as `data analyst`, `developer`, etc.<br> &nbsp; - Maintain a consistent naming convention across all user groups. For example, use underscores or hyphens consistently, and stick with it across all groups (e.g., `data_analyst` or `data-analyst`).<br> &nbsp; - Avoid using abbreviations or acronyms that might be unclear. For example, instead of `name: eng_grp`, use `name: engineer_group`. Use `name: data_engineer` instead of `name: de`. |
| `description` | A brief description of the user group. | optional | - The description should explain the user group’s purpose and the type of users it contains. <br> E.g., "This group contains data analysts who are responsible for reporting and data visualization tasks." |
| `api_scopes`** | A list of API scopes that the user group members are allowed to access. Each scope represents specific endpoints or functionality. To kow more about **`api_scopes_and_their_endpoints`** click [here](/resources/lens/api_endpoints_and_scopes/) | optional (by default all api_scopes are included if not explicitly specified) | - Follow the principle of least privilege and grant users the minimum level of access required to perform their job functions. <br><br> - The following `api_scopes` are currently supported:<br> &nbsp;&nbsp; • `meta`: Provides access to metadata-related endpoints.<br> &nbsp;&nbsp; • `data`: Allows access to data endpoints. This scope enables users to retrieve, and analyze data.<br> &nbsp;&nbsp; • `graphql`: Grants access to GraphQL endpoints.<br> &nbsp;&nbsp; <br> &nbsp;&nbsp; |
| `includes` | A list of users to be included in the user group. This can be specific user IDs or patterns to include multiple users. Use `"*"` to include all users or specify user IDs. | mandatory | - If the number of users is small, prefer using explicit user identifiers (e.g., `users:id:johndoe`) over generic patterns (e.g., `*`). <br> &nbsp;&nbsp;<br> - Example:<br> includes:<br> - `"*"`<br> |
| `excludes` | A list of users to be excluded from the user group. This can be specific user IDs or patterns to exclude certain users from the group. | optional | - If including all users, use `excludes` to remove specific users who should not have access.<br> &nbsp;&nbsp;<br> - Example:<br> excludes:<br> - `users:id:johndoe`<br> |

`api_scopes`** To know more about the api scopes and their endpoints click [here](/resources/lens/api_endpoints_and_scopes/)

## Group priority

When a user is included in multiple user groups, the group listed first in the configuration file will determine the user's access level. This means that the permissions of the first group take precedence over any subsequent groups.

**Example**

Consider the following configuration:

```yaml
user_groups:
  - name: analyst
    description: Data analyst
    api_scopes:
      - meta
      - graphql
      - data
    includes:
      - users:id:exampleuser

  - name: engineer
    description: Data engineer
    api_scopes:
      - meta
      - data
    includes:
      - users:id:exampleuser
```

In this example:

- `exampleuser` is included in both the `analyst` and `engineer` groups.
- Since the `analyst` group is listed before the `engineer` group, `exampleuser` will have the permissions of the `analyst` group.

## Data policies

Data policies can be applied to dimensions and segments of tables to control data access and masking.

### **Defining data masking policy on a Table’s dimension**

You can mask data on a table's dimension using the `secure` property in the meta section. Two data masking functions are available:

- **Redact**: Replaces the value with the string `redact`.
- **md5**: Hashes the value using the MD5 algorithm.

#### **Step 1 Define the data masking function** 

- Include the masking function in the `meta` section of your dimension definition. Here we have masked the gender column for the  specific group `dataconsumer` but the same column is not redacted for the users in the default group. That means everybody can see the row values of gender column except for the users in `dataconsumer` group.

  ```yaml
  - name: gender
    description: Flag indicating whether the consumer is male or female
    sql: gender
    type: string
    meta:
      secure:
        func: redact
        user_groups:
          includes:
            - dataconsumer
          excludes:
            - default
  ```

#### **Step 2: Configure user group policies**

- You can configure user group policies to control access:

    ```yaml
    # 1. Secure for everyone
    meta:
      secure:
        func: redact | md5
        user_groups: "*"

    # 2. Secure for everyone, except for specific user_group (default)
    meta:
      secure:
        func: redact | md5
        user_groups:
          includes: "*"
          excludes:
            - default

    # 3. Secure for specific user_group (reader) and exclude some (default)
    meta:
      secure:
        func: redact | md5
        user_groups:
          includes:
            - reader
          excludes:
            - default

    ```

### **Defining row filter policy on a Table’s Segment**

You can apply a row filter policy to show specific data based on user groups.

#### **Step 1: Define the row filter policy**

- Add the filter policy to the `segments` section of your table definition:

**Example:** Filtering rows to show only online sales data to all user groups except `reader`.

  ```yaml
  segments:
    - name: online_sales
      sql: "{TABLE}.order_mode = 'online'"
      meta:
        secure:
          user_groups:
            includes:
              - *
            excludes:
              - reader
  ```



> <b>Note:</b> When you apply any data policy in Lens, it automatically propagates from the Lens model to all BI tool syncs. For example, if you redact the email column for a specific user group using a data policy in Lens, that column will remain redacted when users from that group sync their Lens model with BI tools like Tableau or Power BI. 