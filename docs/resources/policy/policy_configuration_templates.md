# Policy Configuration Templates

## Access Policy

#### **API Path Access**

The provided template defines an access policy for REST APIs within DataOS. The sample given below authorizes users with the `dataos:u:user` tag to execute `GET`, `POST`, and `PUT` predicates on the designated API path, `/city/api/v1`. Please remember to customize the template by replacing the placeholder values with the necessary details based on your specific requirements.

```yaml 
--8<-- "examples/resources/policy/access_policy/access_policy1.yaml"
```

#### **Dataset Access**

The provided template defines an access policy for a [Depot](/resources/depot/) within DataOS. The sample given below authorizes users with the `roles:id:healthcaredatauser` tag to `READ` predicate on the dataset stored at the UDL address, `dataos://icebase:test/customer_test`. Please remember to customize the template by replacing the placeholder values with the necessary details based on your specific requirements.

```yaml
--8<-- "examples/resources/policy/access_policy/access_policy2.yaml"
```

#### **Collection Access**

The provided template defines an access policy for a Collection within a Depot. The sample given below authorizes users with the `dataos:u:people-DW:user` tag to perform `READ` predicate on the collection stored at the UDL address, `dataos://icebase:people_dw/*`. Please remember to customize the template by replacing the placeholder values with the necessary details based on your specific requirements.

```yaml
--8<-- "examples/resources/policy/access_policy/access_policy3.yaml"
```

#### **Deny All Predicates on Dataset by Tag**

The provided template defines a policy that denies access to a dataset stored within a Depot. The sample given below denies users with the `roles:id:tag:selective-restricted-access` tag to execute any predicates on the dataset stored at the UDL address, `dataos://icebase:test/customer_test`. Please remember to customize the template by replacing the placeholder values with the necessary details based on your specific requirements.

```yaml
--8<-- "examples/resources/policy/access_policy/access_policy4.yaml"
```

#### **Collection Access by Regex-Filtered Tags**

The provided template defines a policy that allows access to a dataset stored within a Depot. The sample given below allows users with tags following the regex `roles:id:**` OR `users:id:**` tag to execute any predicates on the dataset stored at the UDL address, `dataos://icebase:test_healthcare/**`. Please remember to customize the template by replacing the placeholder values with the necessary details based on your specific requirements.

```yaml
--8<-- "examples/resources/policy/access_policy/access_policy5.yaml"
```

## Data Policy

### **Masking Policy**

!!! note

    Certain predefined tags such as `pii.dateofbirth`, pii.age, and pii.location have default policies already created for them, each assigned a priority of 99. These policies are not applied automatically — they only take effect when the tag is manually applied to a column.

    Once a tag is applied, its associated default policy (e.g., data bucketing or masking logic) will take effect.

    For more information refer the [How to implement masking policy guide](/resources/policy/how_to_guide/implementing_masking_data_policy/).


#### **Bucketing Age**

```yaml
--8<--  "examples/resources/policy/data_policy/masking/bucket_number/bucket_number2.yaml"
```

#### **Bucketing Income**

```yaml
--8<-- "examples/resources/policy/data_policy/masking/bucket_number/bucket_number3.yaml"
```


#### **Bucketing Date**

**1. Bucket Date with month precision**

```yaml
--8<-- "examples/resources/policy/data_policy/masking/bucket_date/bucket_date1.yaml"
```

**2. Bucket Date with week precision**

```yaml
--8<-- "examples/resources/policy/data_policy/masking/bucket_date/bucket_date1.yaml"
```

#### **Hashing**

**1. Hashing Email**

```yaml
--8<-- "examples/resources/policy/data_policy/masking/hashing/hashing1.yaml"
```

**2. Hashing Name**

```yaml
--8<-- "examples/resources/policy/data_policy/masking/hashing/hashing2.yaml"
```

**3.Hashing Sensitive Information**

```yaml
--8<-- "examples/resources/policy/data_policy/masking/hashing/hashing3.yaml"
```

**Hashing Health related sensitive information**

```yaml
--8<-- "examples/resources/policy/data_policy/masking/hashing/hashing4.yaml"
```

#### **Redact**

**1. Redacting Gender**

```yaml
--8<-- "examples/resources/policy/data_policy/masking/redact/redact1.yaml"
```

**2. Redacting Location**

```yaml
--8<-- "examples/resources/policy/data_policy/masking/redact/redact2.yaml"
```


**Redacting columns having given tags**

```yaml
--8<-- "examples/resources/policy/data_policy/masking/redact/redact4.yaml"
```

#### **Random Pattern**

**Mapping Random Values to Security Number Format**

```yaml
--8<-- "examples/resources/policy/data_policy/masking/random_pattern/random_number2.yaml"
```



#### **Regex Replace**

**Replace last five digits of phone number**

```yaml
--8<-- "examples/resources/policy/data_policy/masking/regex_replace/regex_replace1.yaml"
```

**Replace whole phone number with regex replace pattern**

```yaml
--8<-- "examples/resources/policy/data_policy/masking/regex_replace/regex_replace2.yaml"
```

**Masking All Digits Except Last Four**

```yaml
--8<-- "examples/resources/policy/data_policy/masking/regex_replace/regex_replace3.yaml"
```

#### **Pass Through**


```yaml
--8<-- "examples/resources/policy/data_policy/masking/pass_through/pass_through1.yaml"
```

### **Filtering Policy**


```yaml
--8<-- "examples/resources/policy/data_policy/filter/filter_data_policy.yaml"
```




