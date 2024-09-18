# Defining Data Policies for Lens Model

!!! info "Information"
    Data policies help control access to specific data, either by masking sensitive information or filtering rows based on user groups. This guide outlines how to apply **data masking** and **row filtering** policies to control data access for your Lens model based on user groups.


## Data Masking Policy on a Table’s Dimension

Data masking ensures that sensitive data is obscured according to the defined policies. To protect data in your Lens model, you have two masking functions available to hide sensitive information:

- **Redact**: It replaces the value with `redact`.
- **md5**: It hashes the value using the MD5 algorithm.

## Define the Data Masking Function

To apply data masking, add the masking function to the **`dimension`** definition in your table manifest file.

Use the `secure` property in the `meta` section. Specify which user groups the data masking applies to.

- `includes`: Groups that will see masked data.
- `excludes`: Groups that will not see masked data.

**Example Configuration**:

```yaml
- name: full_name
  description: Full name of the customer
  sql: full_name
  type: string
  meta:
    secure:
      func: md5
      user_groups:
        includes:
          - dataconsumer
        excludes:
          - default
```

---

## Configure User Group Policies

Here’s how to set up masking for different user groups:

1. **Apply Masking to All Users**
    
    ```yaml
    meta:
      secure:
        func: redact # or md5
        user_groups: "*"
    ```
    
2. **Apply Masking to Everyone Except Certain Groups**
    
    ```yaml
    meta:
      secure:
        func: redact # or md5
        user_groups:
          includes: "*"
          excludes:
            - default
    ```
    
3. **Apply Masking to Specific Groups Only**
    
    ```yaml
    meta:
      secure:
        func: redact # or md5
        user_groups:
          includes:
            - reader
          excludes:
            - default
    
    ```
    

## Example Scenarios

**Example:** The following configuration shows how the masking policy is applied to the `annual_income` dimension of the `customer` table in the **Retail360** data model:

```yaml
- name: annual_income
  type: string
  description: Annual income of the customer.
  sql: annual_income
  meta:
    secure:
      func: redact
      user_groups:
        includes: "*" # secure for everyone
        excludes:
          - type_analyst   # except default 
```

### **Viewing Data: Type_analyst Group vs. Other Users**

1. Users in the `type_analyst` group will see the `annual_income` data, as this group is listed in the `excludes` property. Other users will see masked data.
    
    ![data_for_excluded_user.png](/quick_guides/apply_data_policy_lens/data_for_excluded_user.png)
    
    To see which users belong to the `type_analyst` group, check `user-groups.yaml`:
    
    ```yaml
    user_groups:
      - name: type_analyst
        api_scopes:
          - meta
          - data
          - graphql
          - jobs
          - source
        includes:
          - users:id:aayushisolanki
          - users:id:piyushjoshi
          - users:id:nandapage
    ```
    
2. For users not in the `type_analyst` group, the data is masked as specified.
    
    ![redact_data.png](/quick_guides/apply_data_policy_lens/redact_data.png)
    
    The applied policy can be seen in the model overview.
    
    ![redact_column_info.png](/quick_guides/apply_data_policy_lens/redact_column_info.png)
    

## Inherited Masking Policies from the Physical Table

Notice that even though no policy is defined for the `last_name` column in the data model, it’s still masked. This is because the masking policy is applied to the physical table from which the logical table is derived.

![col_masked_parent_policy.png](/quick_guides/apply_data_policy_lens/col_masked_parent_policy.png)

## Fine-Tuning Data Visibility with Row Filters

To define a row filter policy, create a segment for your table. In the `meta` section, use the `secure` property to specify which user groups should have restricted data visibility.

**Example**: This segment displays only online sales to all user groups except `reader`.

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

To learn more, refer to [Pre-defined Filtering with Segments](/quick_guides/working_with_segments/).