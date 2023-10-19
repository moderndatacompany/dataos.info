# Policy Configuration Templates

## Access Policy

**Enabling specific predicates on a particular API Path for a subject possessing a specific tag**

The provided template defines an access policy for REST APIs within DataOS. The sample given below authorizes users with the `dataos:u:user` tag to execute `GET`, `POST`, and `PUT` predicates on the designated API path, `/city/api/v1`. Please remember to customize the template by replacing the placeholder values with the necessary details based on your specific requirements.

**Template**

```yaml
name: {{access-policy-api-path}}
version: v1
type: policy
tags:
  - {{dataos:type:resource}}
description: {{allow user to access rest apis}}
layer: system 
policy:
  access:
    subjects:
      tags:
        - - {{dataos:u:user}}
    predicates:
      - {{get}}
      - {{post}}
      - {{put}}
      - {{options}}
    objects:
      paths:
        - {{/city/api/v1}}
    allow: {{true}}
```

**Enabling Specific Predicates on a Particular Dataset within a Depot for a Subject Possessing a Specified Tag**

The provided template defines an access policy for a [Depot](../depot.md) within DataOS. The sample given below authorizes users with the `roles:id:healthcaredatauser` tag to `READ` predicate on the dataset stored at the UDL address, `dataos://icebase:test/customer_test`. Please remember to customize the template by replacing the placeholder values with the necessary details based on your specific requirements.

**Template**

```yaml
name: {{test-access-healthcaredata}}
version: v1
type: policy
tags:
  - {{dataos:type:resource}}
  - {{dataos:type:cluster-resource}}
description: {{policy allowing users to read healthcare data.}}
layer: user 
policy:
  access:
    subjects:
      tags:
        - - {{roles:id:healthcaredatauser}}
    predicates:
      - {{read}}
    objects:
      paths:
        - {{dataos://icebase:test_healthcare/patients}}
    allow: {{true}}
```

**Enabling Specific Predicates on a Particular Collection within a Depot for a Subject Possessing a Specified Tag**

The provided template defines an access policy for a Collection within a Depot. The sample given below authorizes users with the `dataos:u:people-DW:user` tag to perform `READ` predicate on the collection stored at the UDL address, `dataos://icebase:people_dw/*`. Please remember to customize the template by replacing the placeholder values with the necessary details based on your specific requirements.

**Template**

```yaml
name: {{people-dw-access-policy}}
version: v1
type: policy
layer: user
description: {{Policy allows users having people-DW:user tag to read data from people_dw collection}}
policy:
  access:
    subjects:
      tags:
        - {{dataos:u:people-DW:user}}
    predicates:
      - {{read}}
    objects:
      paths:
        - {{dataos://icebase:people_dw/*}}
    allow: {{true}}
```

**Denying all possible Predicates on a particular dataset within a Depot for a Subject Possessing a Specified Tag**

The provided template defines a policy that denies access to a dataset stored within a Depot. The sample given below denies users with the `roles:id:tag:selective-restricted-access` tag to execute any predicates on the dataset stored at the UDL address, `dataos://icebase:test/customer_test`. Please remember to customize the template by replacing the placeholder values with the necessary details based on your specific requirements.

**Template**

```yaml
name: {{deny-schema-policy}}
version: v1
type: policy
tags:
  - {{dataos:type:resource}}
  - {{dataos:type:cluster-resource}}
description: {{policy denying users to access a dataset}}
layer: user
policy:
  access:
    subjects:
      tags:
        - - {{roles:id:tag:selective-restricted-access}}
    predicates:
      - {{'**'}}
    objects:
      paths:
        - {{dataos://icebase:test/customer_test}}
    allow: {{false}}
```

**Enabling Predicates on a particular collection within a Depot for Subjects whose tags follow a Specific RegeX**

The provided template defines a policy that allows access to a dataset stored within a Depot. The sample given below allows users with tags following the regex `roles:id:**` OR `users:id:**` tag to execute any predicates on the dataset stored at the UDL address, `dataos://icebase:test_healthcare/**`. Please remember to customize the template by replacing the placeholder values with the necessary details based on your specific requirements.

**Template**

```yaml
name: {{test-phi-deny-access}}
version: v1
type: policy
tags:
  - {{dataos:type:resource}}
  - {{dataos:type:cluster-resource}}
description: {{policy denying access to all users}}
layer: user
policy:
  access:
    subjects:
      tags:
        - - {{roles:id:**}}
        - - {{users:id:**}}
    predicates:
      - {{create}}
      - {{read}}
      - {{write}}
      - {{put}}
      - {{update}}
      - {{delete}}
      - {{post}}
    objects:
      paths:
        - {{dataos://icebase:spend_analysis/**}}
    allow: {{false}}
```

## Data Policy

### Masking Policy

#### **Bucket Number**

The templates below given below define a Data Masking Policy for bucketing values. It replaces individual values with the lowest value of the respective bucket. Please note that you should replace the placeholder values with the appropriate details based on your specific requirements.

**Template 1**

```yaml
name: {{age}}
version: v1
type: policy
tags:
  - {{dataos:type:resource}}
  - {{dataos:type:cluster-resource}}
description: >-
  {{An age bucket is formed by grouping the ages together. Based on defined age
  buckets, the age of individuals is redacted and anonymized. If an individual’s
  age falls under a defined bucket, it is replaced with the lowest value of the
  bucket.}}
owner: {{iamgroot}}
layer: user
policy:
  data:
    priority: {{100}}
    type: mask
    mask:
      bucket_number:
        buckets:
          - {{5}}
          - {{12}}
          - {{18}}
          - {{25}}
          - {{45}}
          - {{60}}
          - {{70}}
      operator: bucket_number
    selector:
      column:
        tags:
          - {{PII.Age}}
      user:
        match: {{any}}
        tags:
          - {{roles:id:user}}
```

**Template 2**

```yaml
name: {{agephi}}
version: v1
type: policy
tags:
  - {{dataos:type:resource}}
  - {{dataos:type:cluster-resource}}
description: >-
  {{An age bucket is formed by grouping the ages together. Based on defined age
  buckets, the age of individuals is redacted and anonymized. If an individual’s
  age falls under a defined bucket, it is replaced with the lowest value of the
  bucket.}}
owner: {{dataos-manager}}
layer: user
policy:
  data:
    priority: {{100}}
    type: mask
    mask:
      bucket_number:
        buckets:
          - {{5}}
          - {{12}}
          - {{18}}
          - {{25}}
          - {{45}}
          - {{60}}
          - {{70}}
      operator: bucket_number
    selector:
      column:
        tags:
          - {{PHI.Age}}
      user:
        match: {{any}}
        tags:
          - {{roles:id:user}}
```

**Template 3**

```yaml
name: {{income}}
version: v1
type: policy
tags:
  - {{dataos:type:resource}}
  - {{dataos:type:cluster-resource}}
  - {{dataos:resource:policy}}
description: >-
  Incomes are grouped into buckets to represent different income ranges. An
  individual's income is redacted and anonymized with the lowest value in the
  bucket.
owner: {{dataos-manager}}
layer: user
policy:
  data:
    priority: {{100}}
    type: mask
    mask:
      bucket_number:
        buckets:
          - {{1000}}
          - {{2000}}
          - {{5000}}
          - {{10000}}
          - {{50000}}
          - {{100000}}
          - {{200000}}
          - {{500000}}
      operator: bucket_number
    selector:
      column:
        tags:
          - {{PII.Income}}
      user:
        match: {{any}}
        tags:
          - {{roles:id:user}}
```

**Template 4**

```yaml
name: {{test-phi-bucket-age}}
version: v1
type: policy
tags:
  - {{dataos:type:resource}}
  - {{dataos:type:cluster-resource}}
  - {{dataos:resource:policy}}
  - {{dataos:layer:user}}
description: {{Dummy rule for demonstration}}
owner: {{iamgroot}}
layer: user
policy:
  data:
    priority: {{40}}
    type: mask
    mask:
      bucket_number:
        buckets:
          - {{20}}
          - {{40}}
          - {{60}}
          - {{80}}
      operator: bucket_number
    selector:
      column:
        tags:
          - {{PHI.age}}
      user:
        match: {{any}}
        tags:
          - {{roles:id:system-dev}}
          - {{roles:id:data-dev}}
```

#### **Bucket Date**

**Template 1**

```yaml
name: {{date-of-birth}}
version: v1
type: policy
tags:
  - {{dataos:type:resource}}
  - {{dataos:type:cluster-resource}}
  - {{dataos:resource:policy}}
  - {{dataos:layer:user}}
description: >-
  {{Groups the date of births into buckets and redacts it to
  either(hour/day/week/month). By replacing the Date of Birth with the bucket's
  lower value, an individual's Date of Birth is hidden.}}
owner: {{iamgroot}}
layer: user
policy:
  data:
    priority: {{99}}
    type: mask
    mask:
      bucket_date:
        precision: {{month}}
      operator: bucket_date
    selector:
      column:
        tags:
          - {{PII.DateOfBirth}}
      user:
        match: {{any}}
        tags:
          - {{roles:id:user}}
```

**Template 2**

```yaml
name: {{phi-date-of-birth}}
version: v1
type: policy
tags:
  - {{dataos:type:resource}}
  - {{dataos:type:cluster-resource}}
  - {{dataos:resource:policy}}
  - {{dataos:layer:user}}
description: >-
  {{Groups the date of births into buckets and redacts it to
  either(hour/day/week/month). By replacing the Date of Birth with the bucket's
  lower value, an individual's Date of Birth is hidden.}}
owner: iamgroot
layer: user
policy:
  data:
    priority: {{99}}
    type: mask
    mask:
      bucket_date:
        precision: {{month}}
      operator: bucket_date
    selector:
      column:
        tags:
          - {{PHI.DateOfBirth}}
      user:
        match: {{any}}
        tags:
          - {{roles:id:user}}
```

#### **Hashing**

**Template 1**

```yaml
name: {{email}}
version: v1
type: policy
tags:
  - {{dataos:type:resource}}
  - {{dataos:layer:user}}
description: >-
  {{Masks an individual’s email address by replacing it with a generated hash
  against the value.}}
owner: {{iamgroot}}
layer: user
policy:
  data:
    priority: {{98}}
    type: mask
    mask:
      hash:
        algo: {{sha256}}
      operator: hash
    selector:
      column:
        tags:
          - {{PII.Email}}
      user:
        match: {{any}}
        tags:
          - {{roles:id:user}}
```

**Template 2**

```yaml
name: {{name}}
version: v1
type: policy
tags:
  - {{dataos:type:resource}}
  - {{dataos:type:cluster-resource}}
description: >-
  {{Masks an individual’s name by replacing it with a generated hash against the
  value.}}
owner: {{iamgroot}}
layer: user
policy:
  data:
    priority: {{100}}
    type: mask
    mask:
      hash:
        algo: {{sha256}}
      operator: hash
    selector:
      column:
        tags:
          - {{PII.Name}}
      user:
        match: {{any}}
        tags:
          - {{roles:id:user}}
```

**Template 3**

```yaml
name: {{pii-hash}}
version: v1
type: policy
tags:
  - {{dataos:type:resource}}
description: {{default data policy to hash any column tagged with fingerprint pii}}
owner: {{iamgroot}}
layer: user
policy:
  data:
    priority: {{100}}
    type: mask
    mask:
      hash:
        algo: {{sha256}}
      operator: hash
    selector:
      column:
        tags:
          - {{PII.Sensitive}}
      user:
        match: {{any}}
        tags:
          - {{roles:id:user}}
```

**Template 4**

```yaml
name: {{test-phi-mask}}
version: v1
type: policy
tags:
  - {{dataos:type:resource}}
  - {{dataos:type:cluster-resource}}
description: {{data policy to hash PHI columns by tags}}
owner: {{iamgroot}}
layer: user
policy:
  data:
    dataset: {{patients}}
    collection: {{test_healthcare}}
    depot: {{icebase}}
    priority: {{40}}
    type: mask
    mask:
      hash:
        algo: {{sha256}}
      operator: hash
    selector:
      column:
        tags:
          - {{PHI.sensitive}}
      user:
        match: {{any}}
        tags:
          - {{roles:id:healthcaredatauser}}
```

#### **Redact**

**Template 1**

```yaml
name: {{gender}}
version: v1
type: policy
tags:
  - {{dataos:layer:user}}
description: >-
  {{The gender of all individuals is redacted and replaced with a constant value
  ‘REDACTED’}}
owner: {{iamgroot}}
layer: user
policy:
  data:
    priority: {{97}}
    type: mask
    mask:
      hash:
        algo: {{sha256}}
      operator: redact
    selector:
      column:
        tags:
          - {{PII.Gender}}
      user:
        match: {{any}}
        tags:
          - {{roles:id:user}}
```

**Template 2**

```yaml
name: {{location}}
version: v1
type: policy
tags:
  - {{dataos:type:resource}}
description: >-
  {{The location of all individuals is redacted and replaced with a constant value
  ‘REDACTED’. Location can be classified as an individual’s address, zip code,
  state, or country.}}
owner: {{iamgroot}}
layer: user
policy:
  data:
    priority: {{100}}
    type: mask
    mask:
      hash:
        algo: {{sha256}}
      operator: redact
    selector:
      column:
        tags:
          - {{PII.Location}}
      user:
        match: {{any}}
        tags:
          - {{roles:id:user}}
```

**Template 3**

```yaml
name: {{policy-test-hash}}
version: v1
type: policy
tags:
  - {{dataos:type:resource}}
description: {{'policy to hash on column '}}
owner: {{iamgroot}}
layer: user
policy:
  data:
    dataset: {{sample_ride}}
    collection: {{data_uber}}
    depot: {{icebase}}
    priority: {{90}}
    type: mask
    mask:
      operator: redact
    selector:
      column:
        names:
          - {{payment_method}}
      user:
        match: {{any}}
        tags:
          - {{users:id:iamgroot}}
```

**Template 4**

```yaml
name: {{test-phi-redact}}
version: v1
type: policy
tags:
  - {{dataos:type:resource}}
description: {{data policy to redact PHI columns by tags}}
owner: {{iamgroot}}
layer: user
policy:
  data:
    dataset: {{patients}}
    collection: {{test_healthcare}}
    depot: {{icebase}}
    priority: {{40}}
    type: mask
    mask:
      hash:
        algo: {{sha256}}
      operator: redact
    selector:
      column:
        tags:
          - {{PHI.int_sensitive}}
          - {{PHI.confidential}}
      user:
        match: {{any}}
        tags:
          - {{roles:id:healthcaredatauser}}
```

#### **Random Pattern**

**Template 1**

```yaml
name: {{license-number}}
version: v1
type: policy
tags:
  - {{dataos:type:resource}}
description: >-
  {{By replacing an individual's license number with a random string of the same
  length, it masks their identity. The column data type is preserved.}}
owner: {{iamgroot}}
layer: user
policy:
  data:
    priority: {{100}}
    type: mask
    mask:
      operator: rand_pattern
      rand_pattern:
        pattern: {{'####-####-####'}}
    selector:
      column:
        tags:
          - {{PII.LicenseNumber}}
      user:
        match: {{any}}
        tags:
          - {{roles:id:user}}
```

**Template 2**

```yaml
name: {{social-security-number}}
version: v1
type: policy
tags:
  - {{dataos:type:resource}}
description: >-
  {{By replacing an individual's Personal ID number with a random string of the
  same length, it masks their identity. The column data type is preserved.}}
owner: {{iamgroot}}
layer: user
policy:
  data:
    priority: {{100}}
    type: mask
    mask:
      operator: rand_pattern
      rand_pattern:
        pattern: {{'####-###-####-##'}}
    selector:
      column:
        tags:
          - {{PII.SocialSecurityNumber}}
      user:
        match: {{any}}
        tags:
          - {{roles:id:user}}
```

#### **Regex Replace**

**Template 1**

```yaml
name: {{phone-number}}
version: v1
type: policy
tags:
  - {{dataos:type:resource}}
description: >-
  {{Replaces the last five digits of an individual’s phone number with ‘XXXX’ to
  mask the contact information}}
owner: {{iamgroot}}
layer: user
policy:
  data:
    priority: {{{{100}}}}
    type: mask
    mask:
      operator: regex_replace
      regex_replace:
        pattern: {{.{5}$}}
        replacement: {{xxxxx}}
    selector:
      column:
        tags:
          - {{PII.PhoneNumber}}
      user:
        match: {{any}}
        tags:
          - {{roles:id:user}}
```

**Template 2**

```yaml
name: {{policy-test-regex-replace}}
version: v1
type: policy
tags:
  - {{dataos:type:resource}}
description: {{mask policy on a column using regex_replace operator}}
owner: {{iamgroot}}
layer: user
policy:
  data:
    dataset: {{sample_driver}}
    collection: {{data_uber}}
    depot: {{icebase}}
    priority: {{90}}
    type: mask
    mask:
      operator: regex_replace
      regex_replace:
        pattern: {{'[0-9]'}}
        replacement: {{'#'}}
    selector:
      column:
        names:
          - {{d_ph_n}}
      user:
        match: {{any}}
        tags:
          - {{users:id:iamgroot}}
```

**Template 3**

```yaml
name: {{test-phi-regex-replace-cc}}
version: v1
type: policy
tags:
  - {{dataos:type:resource}}
description: {{Masking for credit card info}}
owner: {{iamgroot}}
layer: user
policy:
  data:
    dataset: {{patients}}
    collection: {{test_healthcare}}
    depot: {{icebase}}
    priority: {{40}}
    type: mask
    mask:
      operator: regex_replace
      regex_replace:
        pattern: {{'[0-9](?=.*.{4})'}}
        replacement: {{'#'}}
    selector:
      column:
        tags:
          - {{PHI.ccn}}
      user:
        match: {{all}}
        tags:
          - {{roles:id:healthcaredatauser}}
```

#### **Pass Through**

**Template 1**

```yaml
name: {{pii-reader}}
version: v1
type: policy
tags:
  - {{dataos:type:resource}}
  - {{dataos:type:cluster-resource}}
  - {{dataos:resource:policy}}
  - {{dataos:layer:user}}
description: >-
  {{default data policy to allow access to the value of columns tagged with
  fingerprint pii if they are pii-readers}}
owner: {{iamgroot}}
layer: user
policy:
  data:
    priority: {{90}}
    type: mask
    mask:
      operator: pass_through
    selector:
      column:
        tags:
          - {{PII.Sensitive}}
      user:
        match: {{any}}
        tags:
          - {{roles:id:pii-reader}}
```

**Template 2**

```yaml
name: {{test-phi-reader-doctor}}
version: v1
type: policy
tags:
  - {{dataos:type:resource}}
  - {{dataos:type:cluster-resource}}
  - {{dataos:resource:policy}}
  - {{dataos:layer:user}}
description: {{policy to allow doctors with a PHI-doctor tag to view patient's data}}
owner: {{iamgroot}}
layer: user
policy:
  data:
    dataset: {{patients}}
    collection: {{test_healthcare}}
    depot: {{icebase}}
    priority: {{30}}
    type: mask
    mask:
      operator: pass_through
    selector:
      column:
        tags:
          - {{PHI.id}}
          - {{PHI.name}}
          - {{PHI.confidential}}
      user:
        match: {{all}}
        tags:
          - {{roles:id:doctor}}
          - {{roles:id:healthcaredatauser}}
```

**Template 3**

```yaml
name: {{test-phi-reader-finance}}
version: v1
type: policy
tags:
  - {{dataos:type:resource}}
  - {{dataos:type:cluster-resource}}
  - {{dataos:resource:policy}}
  - {{dataos:layer:user}}
description: >-
  {{policy to allow research team with role:id:research tag to view patient's
  medical information but patient ID is hidden}}
owner: {{iamgroot}}
layer: user
policy:
  data:
    dataset: {{patients}}
    collection: {{test_healthcare}}
    depot: {{icebase}}
    priority: {{30}}
    type: mask
    mask:
      operator: pass_through
    selector:
      column:
        tags:
          - {{PHI.financial}}
          - {{PHI.id}}
          - {{PHI.dor}}
          - {{PHI.name}}
      user:
        match: {{all}}
        tags:
          - {{roles:id:finance}}
          - {{roles:id:healthcaredatauser}}
```

**Template 4**

```yaml
name: {{test-phi-reader-research}}
version: v1
type: policy
tags:
  - {{dataos:type:resource}}
  - {{dataos:type:cluster-resource}}
  - {{dataos:resource:policy}}
  - {{dataos:layer:user}}
description: >-
  {{policy to allow research team with role:id:research tag to view patient's
  medical information but patient ID is hidden}}
owner: {{iamgroot}}
layer: user
policy:
  data:
    dataset: {{patients}}
    collection: {{test_healthcare}}
    depot: {{icebase}}
    priority: {{30}}
    type: mask
    mask:
      operator: pass_through
    selector:
      column:
        tags:
          - {{PHI.research}}
      user:
        match: {{all}}
        tags:
          - {{roles:id:research}}
          - {{roles:id:healthcaredatauser}}
```

**Template 5**

```yaml
name: {{test-phi-reader-staff}}
version: v1
type: policy
tags:
  - {{dataos:type:resource}}
  - {{dataos:type:cluster-resource}}
  - {{dataos:resource:policy}}
  - {{dataos:layer:user}}
description: {{policy to allow staff with role:id:staff tag to view patient's data}}
owner: {{iamgroot}}
layer: user
policy:
  data:
    dataset: {{patients}}
    collection: {{test_healthcare}}
    depot: {{icebase}}
    description: {{policy to allow staff with role:id:staff tag to view patient's data
    name: test-phi-reader-staff}}
    priority: {{30}}
    type: mask
    mask:
      operator: pass_through
    selector:
      column:
        tags:
          - {{PHI.contact}}
          - {{PHI.name}}
          - {{PHI.id}}
      user:
        match: all
        tags:
          - {{roles:id:staff}}
```

### **Filtering Policy**

**Template 1**

```yaml
name: {{filter-health-persons}}
version: v1
type: policy
tags:
  - {{dataos:type:resource}}
  - {{dataos:type:cluster-resource}}
  - {{dataos:resource:policy}}
  - {{dataos:layer:user}}
description: {{data policy to filter according to ethnicity type is equals Not Span/Hispanic}}
owner: {{iamgroot}}
layer: user
policy:
  data:
    dataset: {{procedure_codes}}
    collection: {{emr_healthcare}}
    depot: {{postgres}}
    priority: {{75}}
    type: filter
    filters:
      - column: {{proc_code}}
        operator: {{equals}}
        value: {{CAR004}}
    selector:
      user:
        match: {{any}}
        tags:
          - {{roles:id:limited-access}}
```

**Template 2**

```yaml
name: {{filter-to-florida}}
version: v1
type: policy
tags:
  - {{dataos:type:resource}}
  - {{dataos:type:cluster-resource}}
  - {{dataos:resource:policy}}
  - {{dataos:layer:user}}
description: {{data policy to filter just FL data}}
owner: {{iamgroot}}
layer: user
policy:
  data:
    depot: {{icebase}}
    priority: {{10}}
    type: filter
    filters:
      - column: {{vehicle_id}}
        operator: {{not_equals}}
        value: {{FL}}
    selector:
      user:
        match: {{any}}
        tags:
          - - {{users:**}}
          - - {{roles:**}}
```