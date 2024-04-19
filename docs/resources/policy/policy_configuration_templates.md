# Policy Configuration Templates

## Access Policy

**Enabling specific predicates on a particular API Path for a subject possessing a specific tag**

The provided template defines an access policy for REST APIs within DataOS. The sample given below authorizes users with the `dataos:u:user` tag to execute `GET`, `POST`, and `PUT` predicates on the designated API path, `/city/api/v1`. Please remember to customize the template by replacing the placeholder values with the necessary details based on your specific requirements.

**Template**

```yaml 
--8<-- "examples/resources/policy/access_policy/access_policy1.yaml"
```

**Enabling Specific Predicates on a Particular Dataset within a Depot for a Subject Possessing a Specified Tag**

The provided template defines an access policy for a [Depot](../depot.md) within DataOS. The sample given below authorizes users with the `roles:id:healthcaredatauser` tag to `READ` predicate on the dataset stored at the UDL address, `dataos://icebase:test/customer_test`. Please remember to customize the template by replacing the placeholder values with the necessary details based on your specific requirements.

**Template**

```yaml
--8<-- "examples/resources/policy/access_policy/access_policy2.yaml"
```

**Enabling Specific Predicates on a Particular Collection within a Depot for a Subject Possessing a Specified Tag**

The provided template defines an access policy for a Collection within a Depot. The sample given below authorizes users with the `dataos:u:people-DW:user` tag to perform `READ` predicate on the collection stored at the UDL address, `dataos://icebase:people_dw/*`. Please remember to customize the template by replacing the placeholder values with the necessary details based on your specific requirements.

**Template**

```yaml
--8<-- "examples/resources/policy/access_policy/access_policy3.yaml"
```

**Denying all possible Predicates on a particular dataset within a Depot for a Subject Possessing a Specified Tag**

The provided template defines a policy that denies access to a dataset stored within a Depot. The sample given below denies users with the `roles:id:tag:selective-restricted-access` tag to execute any predicates on the dataset stored at the UDL address, `dataos://icebase:test/customer_test`. Please remember to customize the template by replacing the placeholder values with the necessary details based on your specific requirements.

**Template**

```yaml
--8<-- "examples/resources/policy/access_policy/access_policy4.yaml" 
``` 

**Enabling Predicates on a particular collection within a Depot for Subjects whose tags follow a Specific RegeX**

The provided template defines a policy that allows access to a dataset stored within a Depot. The sample given below allows users with tags following the regex `roles:id:**` OR `users:id:**` tag to execute any predicates on the dataset stored at the UDL address, `dataos://icebase:test_healthcare/**`. Please remember to customize the template by replacing the placeholder values with the necessary details based on your specific requirements.

**Template**

```yaml
--8<-- "examples/resources/policy/access_policy/access_policy5.yaml"
```

## Data Policy

### Masking Policy

#### **Bucket Number**

The templates below given below define a Data Masking Policy for bucketing values. It replaces individual values with the lowest value of the respective bucket. Please note that you should replace the placeholder values with the appropriate details based on your specific requirements.

**Template 1**

```yaml
--8<-- "examples/resources/policy/data_policy/masking/bucket_number/bucket_number1.yaml"
```

**Template 2**

```yaml
--8<--  "examples/resources/policy/data_policy/masking/bucket_number/bucket_number2.yaml"
```

**Template 3**

```yaml
--8<-- "examples/resources/policy/data_policy/masking/bucket_number/bucket_number3.yaml"
```

**Template 4**

```yaml
--8<-- "examples/resources/policy/data_policy/masking/bucket_number/bucket_number3.yaml"
```

#### **Bucket Date**

**Template 1**

```yaml
--8<-- "examples/resources/policy/data_policy/masking/bucket_date/bucket_date1.yaml"
```

**Template 2**

```yaml
--8<-- "examples/resources/policy/data_policy/masking/bucket_date/bucket_date1.yaml"
```

#### **Hashing**

**Template 1**

```yaml
--8<-- "examples/resources/policy/data_policy/masking/hashing/hashing1.yaml"
```

**Template 2**

```yaml
--8<-- "examples/resources/policy/data_policy/masking/hashing/hashing2.yaml"
```

**Template 3**

```yaml
--8<-- "examples/resources/policy/data_policy/masking/hashing/hashing3.yaml"
```

**Template 4**

```yaml
--8<-- "examples/resources/policy/data_policy/masking/hashing/hashing4.yaml"
```

#### **Redact**

**Template 1**

```yaml
--8<-- "examples/resources/policy/data_policy/masking/redact/redact1.yaml"
```

**Template 2**

```yaml
--8<-- "examples/resources/policy/data_policy/masking/redact/redact2.yaml"
```

**Template 3**

```yaml
--8<-- "examples/resources/policy/data_policy/masking/redact/redact3.yaml"

```

**Template 4**

```yaml
--8<-- "examples/resources/policy/data_policy/masking/redact/redact4.yaml"
```

#### **Random Pattern**

**Template 1**

```yaml
--8<-- "examples/resources/policy/data_policy/masking/random_pattern/random_number2.yaml"
```

**Template 2**

```yaml
--8<-- "examples/resources/policy/data_policy/masking/random_pattern/random_number2.yaml"
```

#### **Regex Replace**

**Template 1**

```yaml
--8<-- "examples/resources/policy/data_policy/masking/regex_replace/regex_replace1.yaml"
```

**Template 2**

```yaml
--8<-- "examples/resources/policy/data_policy/masking/regex_replace/regex_replace2.yaml"
```

**Template 3**

```yaml
--8<-- "examples/resources/policy/data_policy/masking/regex_replace/regex_replace3.yaml"
```

#### **Pass Through**

**Template 1**

```yaml
--8<-- "examples/resources/policy/data_policy/masking/pass_through/pass_through1.yaml"
```

**Template 2**

```yaml
--8<-- "examples/resources/policy/data_policy/masking/pass_through/pass_through2.yaml"
```

**Template 3**

```yaml
--8<-- "examples/resources/policy/data_policy/masking/pass_through/pass_through3.yaml"

```

**Template 4**

```yaml
--8<-- "examples/resources/policy/data_policy/masking/pass_through/pass_through4.yaml"

```

**Template 5**

```yaml
--8<-- "examples/resources/policy/data_policy/masking/pass_through/pass_through5.yaml"

```

### **Filtering Policy**

**Template 1**

```yaml
--8<-- "examples/resources/policy/data_policy/filter/filter_data_policy.yaml"
```

**Template 2**

```yaml
--8<-- "examples/resources/policy/data_policy/filter/filter_data_policy.yaml"
```