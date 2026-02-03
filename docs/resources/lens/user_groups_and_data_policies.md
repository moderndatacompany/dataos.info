# Working with user groups and data policies

In Lens, different users have different responsibilities and access requirements.
For example:

- Analysts may explore data freely

- Engineers may need operational or ingestion-level access

- Consumers may only view curated or restricted results

To support these use cases, Lens provides a structured access and governance model that allows you to:

- Organize users into groups

- Control which APIs and platform features they can access

- Secure how data is exposed to them

This is achieved using user groups and data policies, which together define Lens’s access and data governance model.

## User groups

User groups define:

- Which users belong to a group

- Which Lens APIs and platform capabilities those users can access

- Which Lens Studio UI features are available to them

It answers: "Who is this user and which api can they access in semantic model?".

## Data policies

Data policies are applied at the model level (dimensions and segments) and always reference existing user groups.

Data policies define:

- How data is presented to users, based on their user group

- Whether data should be masked, hashed, or filtered

It answers "How should data behave for users in a given group?"

**How they work together**

1. A user authenticates into Lens.

2. Lens determines the user’s user group membership.

3. API and UI access are granted based on the group’s configuration.

4. Data policies are applied based on the same user groups.

5. The user sees only the APIs and features they are allowed to use.

## Procedure

Follow these steps to create and manage user groups:

### **Create a `user_groups.yml` file in your model folder**

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

### **Define `user_group.yaml`**

Define `user_group.yaml` file using following template:

=== "Syntax"

    ```yaml
    user_groups: # List of user groups
      - name: ${{user_group_1}} # Name of the group (check regex)
        description: ${{description for user group}} # Description of the group
        api_scopes:
          - ${{meta}}
          - ${{data}}
          - ${{graphql}}
          # - jobs
          # - source
        includes: # Users to include in this group
          - ${{users:id:username}}
          - ${{users:id:ironman}}
        excludes: # Users to exclude from this group
          - $[[users:id:blackwidow]]

      - name: ${{user_group_2}}
        ##..
    ```

=== "Example"

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

      - name: analyst
    ```

This user group will serve three main purposes:

- **API access control** – It defines which Lens APIs a group can access using api_scopes.

- **Data security reference** – The same user group is reused in data policies to:

      - Secure table dimensions (mask or hash data)

      - Secure table segments (row-level filtering)

Let's explore different use cases:

### **Using user groups for API access control**

Different user groups can be given different API permissions.

When defining a user group, you explicitly list:

- Which users belong to the group

- Which Lens APIs they are allowed to access

**Example 1: Reader group can only read and access lens but cannot explore it**

```yaml
user_groups:
  - name: reader
    description: Data analysts who explore data
    api_scopes:
      - meta
    includes:
      - users:id:analyst1

  - name: analyst
    description: Data engineers with operational access
    api_scopes:
      - meta
      - data
      - graphql
    includes:
      - users:id:engineer1
```

This user group will serve three main purposes:

- Analysts can query data and use GraphQL

- Engineers can access metadata and data APIs but not GraphQL

- API access is controlled without writing custom authorization logic

At this stage, only API access is being controlled.


**Example 2: Private semantic model for a specific team**

In this example, only users in the `dataconsumer` group can access and explore the semantic model, while all other users fall under the default group and are not intended to use it. This setup is used to keep a semantic model private to a specific team or project.

```yaml
user_groups:
  - name: dataconsumer
    description: Data analysts who explore data
    api_scopes:
      - meta
      - data
      - graphql
      - job
    includes:
      - users:id:analyst1

# In this case, leave the default group blank
  - name: default
    description: Data engineers with operational access
    api_scopes:
      - meta
      - data
      - graphql

```


### **Secure a table dimension using user group and data policy** 

Once user groups exist, you can reference them in data policies using the `meta.secure` block which defines to which user groups the masking rule applies to.

A data masking policy has two key parts:

  - **The masking function (`func`)** — defines how the data is transformed. 

  - **User group rules (`user_groups`)** — define who the transformation applies to

**Supported data masking functions**

Lens currently supports the following masking functions:

| Function | Description | Use Case |
|--------|-------------|----------|
| `redact` | Replaces the value with `--redact--` | Hide sensitive data completely |
| `md5` | Hashes the value using the MD5 algorithm | Obfuscate data while preserving uniqueness |

**Example: Masking a dimension for a specific user group**

Assume the following requirement:

- Users in the `analyst` group should see masked values for the `gender` dimension.

- Users in the `engineer` group should see the original (unmasked) values.

To achieve this, include the `analyst` group in the `meta.secure.user_groups.includes` list and explicitly exclude the `engineer` group.

```yaml 
tables: 
#...
#...
  - name: gender
    description: Flag indicating whether the consumer is male or female
    sql: gender
    type: string
    meta:
      secure:
        func: redact
        user_groups:
          includes:  
            - analyst  #security rules applies to analyst 
          excludes:
            - engineer
```

On the basis of this, members of the `analyst` group will see the `gender` column value as `--redact--`. All members of the `engineer` group will see the gender column value as it is. 

### **Use the user group to secure table's segment**

In Lens, row-level data security is defined using the `meta.secure` block on table segments. This mechanism controls which rows of data are visible to users based on their user group.

Row-level security allows you to filter data at query time so that different users see different subsets of rows from the same table.

A row-level security policy has two main parts:

  - **The segment condition (`sql`)** — defines which rows qualify. It acts like a `WHERE` clause.

  - **User group rules (`user_groups`)** — define who the filter applies to.

Unlike dimension masking, row-level security includes or excludes rows entirely rather than transforming values.

**Example 1: Apply a row filter based on user group**

**Requirement:** Only non-reader users should see online sales data.

```yaml
segments:
  - name: online_sales
    sql: "{TABLE.order_mode} = 'online'"
    meta:
      secure:
        user_groups:
          includes:
            - "*"
          excludes:
            - reader
```

**Example 2: Filtering rows to show only online sales data to all user groups except `reader`**

  ```yaml
  segments:
    - name: online_sales
      sql: "{TABLE.order_mode} = 'online'"
      meta:
        secure:
          user_groups:
            includes:
              - *
            excludes:
              - reader
  ```

**Example 3:** In this example, user groups represent regional marketing teams. Each team should only see data related to the country they are running campaigns for.

- The `usa` group represents the US marketing team and is intended to see only US-specific campaign and customer data.

- The `india` group represents the India marketing team and is intended to see only India-specific data.

- The `default` group includes all users and they all will be able to see data of all countries.

These user groups can be referenced in row-level filtering policies so that marketing teams only analyze data for their assigned region, while using the same Data Product and semantic model.

```yaml
user_groups:
  - name: usa
    api_scopes:
      - meta
      - data
      - graphql
      - jobs
      - source
    includes: 
      - users:id:iamgroot

  - name: india
    api_scopes:
      - meta
      - data
      - graphql
      - jobs
      - source
    includes: 
      - users:id:ironman

  - name: default
    api_scopes:
      - meta
      - data
      - graphql
      - jobs
      - source
    includes: "*"
```
 
## User group configuration 

| **Attribute** | **Description** | **Requirement** | **Best Practice** |
| --- | --- | --- | --- |
| `user_groups` | The top-level mapping contains the list of user groups. Each user group defines a set of users and respective access controls.  | mandatory |  |
| `name` | The name of the user group. | mandatory | - It should be unique and descriptive to identify the group's purpose, or role such as `data analyst`, `developer`, etc.<br> &nbsp; - Maintain a consistent naming convention across all user groups. For example, use underscores or hyphens consistently, and stick with it across all groups (e.g., `data_analyst` or `data-analyst`).<br> &nbsp; - Avoid using abbreviations or acronyms that might be unclear. For example, instead of `name: eng_grp`, use `name: engineer_group`. Use `name: data_engineer` instead of `name: de`. |
| `description` | A brief description of the user group. | optional | - The description should explain the user group’s purpose and the type of users it contains. <br> E.g., "This group contains data analysts who are responsible for reporting and data visualization tasks." |
| `api_scopes`** | A list of API scopes that the user group members are allowed to access. Each scope represents specific endpoints or functionality. To kow more about **`api_scopes_and_their_endpoints`** click [here](/resources/lens/api_endpoints_and_scopes/) | optional (by default all api_scopes are included if not explicitly specified) | - Follow the principle of least privilege and grant users the minimum level of access required to perform their job functions. <br><br> - The following `api_scopes` are currently supported:<br> &nbsp;&nbsp; • `meta`: Provides access to metadata-related endpoints.<br> &nbsp;&nbsp; • `data`: Allows access to data endpoints. This scope enables users to retrieve, and analyze data.<br> &nbsp;&nbsp; • `graphql`: Grants access to GraphQL endpoints.<br> &nbsp;&nbsp; <br> &nbsp;&nbsp; |
| `includes` | A list of users to be included in the user group. This can be specific user IDs or patterns to include multiple users. Use `"*"` to include all users or specify user IDs. | mandatory | - If the number of users is small, prefer using explicit user identifiers (e.g., `users:id:johndoe`) over generic patterns (e.g., `*`). <br> &nbsp;&nbsp;<br> - Example:<br> includes:<br> - `"*"`<br> |
| `excludes` | A list of users to be excluded from the user group. This can be specific user IDs or patterns to exclude certain users from the group. | optional | - If including all users, use `excludes` to remove specific users who should not have access.<br> &nbsp;&nbsp;<br> - Example:<br> excludes:<br> - `users:id:johndoe`<br> |

`api_scopes`** Know more about the [API scopes and their endpoints](/resources/lens/api_endpoints_and_scopes/)


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
      - users:id:analyst1
      - users:id:analyst2

  - name: engineer
    description: Data engineer
    api_scopes:
      - meta
      - data
    includes:
      - users:id:engineer1
      - users:id:engineer2
```

In this example:

- `exampleuser` is included in both the `analyst` and `engineer` groups.
- Since the `analyst` group is listed before the `engineer` group, `exampleuser` will have the permissions of the `analyst` group.

### **Configure user group policies**

You can configure user group policies to control access:

```yaml
# 1. Security rule applies to everyone
meta:
  secure:
    func: redact | md5
    user_groups: "*"

# 2. Security rule applies to everyone, except for default
meta:
  secure:
    func: redact | md5
    user_groups:
      includes: "*"
      excludes:
        - default

# 3. Security rule applies to reader user group and exclude default
meta:
  secure:
    func: redact | md5
    user_groups:
      includes:
        - reader
      excludes:
        - default
```

> <b>Note:</b> When you apply any data policy in Lens, it automatically propagates from the Lens model to all BI tool syncs. For example, if you redact the email column for a specific user group using a data policy in Lens, that column will remain redacted when users from that group sync their Lens model with BI tools like Tableau or Power BI. 