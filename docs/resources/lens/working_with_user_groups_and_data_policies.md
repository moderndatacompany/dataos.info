# Working with User Groups and Data Policies

In Lens, you can secure data in logical tables by defining data policies on their dimensions and segments. This guide will walk you through the steps to create user groups and apply data policies effectively.

## Creating User Groups

User groups are a way to organize users for managing access to various API scopes and easier application of data policies for different categories of users.

Follow these steps to create and manage user groups:

### **Step 1: Create the `user_groups.yml` File**

Create a `user_groups.yml` file in your model folder.

```latex
model/
├── sqls/
│   └── account.sql
├── tables/
│   └── account.yml
├── views/
│   └── engagement.yml
└── **user_groups.yml**
```

### **Step 2: Define User Groups**

Add user groups to the `user-group.yml` file using the following format:

```yaml
user_groups: # List of user groups
  - name: reader # Name of the group (check regex)
    description: # Description of the group
    api_scopes:
      - meta
      - data
      - graphql
      - jobs
      - source
    includes: # Users to include in this group
      - users:id:thor
      - users:id:ironman
    excludes: # Users to exclude from this group
      - users:id:blackwidow
```

| **Attribute** | **Description** | **Requirement** | **Best Practice** |
| --- | --- | --- | --- |
| `user_groups` | The top-level mapping contains the list of user groups. Each user group defines a set of users and respective access controls.  | mandatory |  |
| `name`      | The name of the user group.                                                                                                                   | mandatory                                                                                                               | - It should be unique and descriptive to identify the group's purpose, or role such as `data analyst`, `developer`, etc.<br> &nbsp; - Maintain a consistent naming convention across all user groups. For example, use underscores or hyphens consistently, and stick with it across all groups (e.g., `data_analyst` or `data-analyst`).<br> &nbsp; - Avoid using abbreviations or acronyms that might be unclear. For example, instead of `name: eng_grp`, use `name: engineer_group`. Use `name: data_engineer` instead of `name: de`. |
| `includes`  | A list of users to be included in the user group. This can be specific user IDs or patterns to include multiple users. Use `"*"` to include all users or specify user IDs. | mandatory                                                                                                               | - If the number of users is small, prefer using explicit user identifiers (e.g., `users:id:johndoe`) over generic patterns (e.g., `*`).<br> &nbsp &nbsp &nbsp &nbsp; - Example:<br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>includes:<br> - `"*"`<br>|
| `excludes`  | A list of users to be excluded from the user group. This can be specific user IDs or patterns to exclude certain users from the group.           | optional                                                                                                                | - If including all users, use `excludes` to remove specific users who should not have access.<br> &nbsp; &nbsp;&nbsp;&nbsp; - Example:<br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>excludes:<br> - `users:id:johndoe`<br>|



## Group Priority

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

## Defining Data Policies

Data policies can be applied to dimensions and segments of tables to control data access and masking.

### **Defining Data Masking Policy on a Table’s Dimension**

You can mask data on a table's dimension using the `secure` property in the meta section. Two data masking functions are available:

- **Redact**: Replaces the value with the string `redact`.
- **md5**: Hashes the value using the MD5 algorithm.

#### **Step 1: Define the Data Masking Function**

Include the masking function in the `meta` section of your dimension definition:

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

#### **Step 2: Configure User Group Policies**

You can configure user group policies to control access:

```yaml
# 1. Secure for everyone
meta:
  secure:
    func: redact | md5
    user_groups: "*"

# 2. Secure for everyone, except for specific user_group
meta:
  secure:
    func: redact | md5
    user_groups:
      includes: "*"
      excludes:
        - default

# 3. Secure for specific user_group and exclude some
meta:
  secure:
    func: redact | md5
    user_groups:
      includes:
        - reader
      excludes:
        - default

```

### **Defining Row Filter Policy on a Table’s Segment**

Apply a row filter policy to show specific data based on user groups.

#### **Step 1: Define the Row Filter Policy**

Add the filter policy to the `segments` section of your table definition:

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

**Example:** Filtering rows to show only online sales data to all user groups except `reader`.