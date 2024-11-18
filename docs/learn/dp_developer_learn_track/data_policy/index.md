# Defining data policies for Lens semantic model

This topic outlines how to apply data masking and row filtering policies to control data access for your Lens model based on user groups.

## Data masking policy on a table’s dimension

Data masking ensures that sensitive data is obscured according to the defined policies. To protect data in your Lens model, you have two masking functions available to hide sensitive information:

- **Redact**: It replaces the value with `redact`. It applied to string-based data like personal identifiers, email addresses, or any textual information that needs to be obscured for security or privacy reasons. 
- **md5**: It hashes the value using the MD5 algorithm. 

For our use-case, let's suppose you decide to mask the `marital_status` using the redact data policy.

## Define the data masking function

You begin to add the masking function to the `dimension` definition in your table manifest file.

You use the `secure` property in the `meta` section. Specify which user groups the data masking applies to.

- `includes`: Groups that will be able to surpass the masked data.
- `excludes`: Groups that will not be surpass the masked data.

**Example:** The following configuration shows how the masking policy is applied to the `marital_status` dimension of the `customer` table in the **Product360** data model:

```yaml title="customer.yml"
#dimension

- name: marital_status
  type: string
  description: Annual marital_status of the customer.
  sql: marital_status
  meta:
    secure:
      func: redact
      user_groups:
        includes: 
          - dataconsumer # secure for everyone
        excludes:
          - default   # except default 
```

### **Viewing data: dataconsumer group vs. other users**

1. Users in the `dataconsumer` group will see the `marital_status` data as masked, as this group is listed in the `excludes` property. Other users will be able to see the actual data in the `marital_status` column.
    
Remember you have created a user group  in the create Lens folder topic of the create semantic model module. Let's again check it out to see which users belong to the which group
    
```yaml title="user_groups.yml"
user_groups:
  - name: dataconsumer
    api_scopes:
      - meta
      - data
      - graphql
      - jobs
      - source
    includes:
      - users:id:iamgroot
      - users:id:thor

  - name: default
    api_scopes:
      - meta
      - data
      - graphql
      - jobs
      - source
    includes: "*"      
```

In this case, there are two groups dataconsumer and default group. For users in the `dataconsumer` group, the data is masked as specified.
    
![redact_column_info.png](/learn/dp_developer_learn_track/data_policy/user_group.png)
  
<aside class="callout">
It’s important to note that even if you don’t explicitly define a masking policy for certain columns in the data model, they may still be masked if the policy is inherited from the source.
</aside>

## Fine-tuning data visibility with row filters

you can also define a row filter policy, on a segment in your table. In the `meta` section, use the `secure` property to specify which user groups should have restricted data visibility.

**Example**: This segment displays only online sales to all user groups except `dataconsumer`.

```yaml
segments:
  - name: {DIMENSION_NAME}
    sql: "{TABLE}.{DIMENSION_NAME} = '{DIMENSION_VALUE_TO_FILTER}'"
    meta:
      secure:
        user_groups:
          includes:
            - "*"
          excludes:
            - {dataconsumer}
```
In our use-case we have not defined the segments but you can use the above syntax to apply row filter policy on your segment.
