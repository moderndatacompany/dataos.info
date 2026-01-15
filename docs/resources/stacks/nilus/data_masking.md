# Data Masking in Nilus

Data masking in Nilus enables the protection of sensitive information during data ingestion by replacing or transforming sensitive values with non-sensitive equivalents. 

These transformations are applied in-flight, ensuring that source data remains unmodified while preserving its analytical and structural integrity. This process is essential for handling production-grade data in non-production, shared, or compliance-sensitive environments.

## Common Use Cases

- **Compliance** – Satisfies regulatory requirements such as GDPR, CCPA, HIPAA, and PCI DSS by masking sensitive data elements.

- **Security** – Enables the use of production-grade data in testing or staging environments without exposing sensitive information.

- **Privacy** – Prevents the disclosure of personally identifiable information (PII) and other confidential data.

- **Data Sharing** – Facilitates secure access for external teams or partners by masking sensitive content prior to distribution.


## Sample Manifest Configuration

To apply column-level masking, define a `mask` section under the `source.options` block in the Nilus configuration file, as shown below:

```yaml
source:
  address: postgres://user:pass@localhost/db
  options:
    source-table: "public.users"
    mask:
      email: hash
      phone: partial:3
      ssn: redact
      salary: round:5000
sink:
  address: dataos://postgresdepot
  options:
    dest-table: "public.masked_users"
    incremental-strategy: append

```

**Attribute Details**

Three key attributes must be defined to configure data masking in Nilus. These should be specified in the following format:

```yaml
mask:
  column_name: algorithm[:parameter]
```

| Field | Description |
| --- | --- |
| `column_name` | The name of the column to mask (required). |
| `algorithm` | The masking algorithm to apply (required). |
| `parameter` | Optional argument for algorithms that support configuration (e.g., `partial:2`, `round:1000`). |


!!! tip "Data Masking and Access Restrictions in Nilus"

    - Data is masked during ingestion, resulting in the destination dataset containing only the masked version.
    - There is no separate unmasked dataset stored; hence, it is not possible to grant access to unmasked data for different users or groups.
    - Nilus does not support dynamic data masking, which means masking cannot be applied or removed on-demand.
    - To access unmasked data, the dataset must be **re-ingested** directly from the source **without** applying masking rules.

## Masking Algorithms

Nilus supports a comprehensive set of masking algorithms, categorized by functional purpose. Each algorithm enables specific masking behavior to meet varying privacy, security, and compliance requirements.


### **1. Irreversible Masking Algorithms**

Transforms data using one-way functions.

- **`hash` / `sha256`**

    Generates a SHA-256 hash. Produces consistent output for identical input values.

    ```yaml
    mask:
      user_id: hash
    # john.doe@example.com → a94a8fe5ccb19ba61c4c0873d391e987982fbbd3
    ```

- **`md5`**

    Produces an MD5 hash. Offers faster processing but lower security than SHA-256.

    ```yaml
    mask:
      session_id: md5
    ```

- **`hmac`**

    Applies an HMAC using a shared secret key. Enables consistent anonymization across systems.

    ```yaml
    mask:
      customer_id: hmac:my-secret-key
    ```

- **`redact`**

    Replaces the entire value with the constant string `"REDACTED"`.

    ```yaml
    mask:
      comments: redact
    # "Customer complaint..." → "REDACTED"
    ```



### **2. Format-Preserving Algorithms**

Preserves recognizable data structure or formatting while masking sensitive content.

- **`email`**

    Masks characters before the “@”, retaining only the first and last.

    ```yaml
    mask:
      email: email
    # john.doe@example.com → j******e@example.com
    ```

- **`phone`**

    Retains country and area codes; masks remaining digits.

    ```yaml
    mask:
      phone: phone
    # +1-555-123-4567 → +1-555-***-****
    ```

- **`credit_card`**

    Reveals only the last four digits.

    ```yaml
    mask:
      card_number: credit_card
    # 4111-1111-1111-1111 → ****-****-****-1111
    ```

- **`ssn`**

    Displays only the last four digits of U.S. Social Security Numbers.

    ```yaml
    mask:
      ssn: ssn
    # 123-45-6789 → ***-**-6789
    ```



### **3. Partial Masking Algorithms**

Exposes limited portions of a value, with the remainder masked.

- **`partial`**

    Reveals the first and last *N* characters, masking the middle.

    ```yaml
    mask:
      name: partial:2
    # "Jonathan" → "Jo****an"
    ```

- **`first_letter`**

    Retains only the first character, masking the rest.

    ```yaml
    mask:
      first_name: first_letter
    # "Alice" → "A****"
    ```

- **`stars`**

    Replaces all characters with asterisks of equal length.

    ```yaml
    mask:
      password: stars
    # "secret123" → "*********"
    ```

- **`fixed`**

    Replaces the value with a constant placeholder.

    ```yaml
    mask:
      api_key: fixed:MASKED_KEY
    # "sk_live_abc123" → "MASKED_KEY"
    ```



### **4. Tokenization Algorithms**

Substitutes sensitive values with generated identifiers to maintain uniqueness or referential integrity.

- **`uuid`**

    Replaces values with deterministic UUIDs.

    ```yaml
    mask:
      customer_id: uuid
    # "CUST001" → "550e8400-e29b-41d4-a716-446655440000"
    ```

- **`sequential`**

    Assigns incremental numeric IDs, starting from 1.

    ```yaml
    mask:
      account_number: sequential
    # "ACC-2024-001" → 1
    ```

- **`random`**

    Replaces values with randomly generated values of the same type.

    ```yaml
    mask:
      age: random
    # 35 → 67
    ```



### **5. Numeric Masking Algorithms**

Modifies numeric data while preserving approximate magnitude or distribution.

!!! warning
    
    These algorithms require explicit type definitions using the `type-hints` configuration.

- **`round`**

    Rounds numeric values to the nearest specified multiple.
    
    This algorithm requires the destination column to be of type `TEXT`. You need to define the column inside `type-hints`.

    ```yaml
    source:
      address: dataos://testawslh
      options:
          source-table: "masking_test.aws_masking_data"
          type-hints:
            salary: text
          mask:
            salary: round:5000
            age: round:10
          # salary: 52300 → 50000
          # age: 34 → 30
    ```

- **`range`**

    Maps numeric values to defined buckets (e.g., income bands).

    This algorithm requires the destination column to be of type `TEXT`. You need to define the column inside `type-hints`.

    ```yaml
    source:
      address: dataos://testawslh
      options:
          source-table: "masking_test.aws_masking_data"
          type-hints:
            income: text
          mask:
            income: range:10000
          # 45000 → "40000–50000"
    ```

- **`noise`**

    Applies a random variation within a defined percentage range.
    
    This algorithm requires the destination column to be of type `DOUBLE`. You need to define the column inside `type-hints`.

    ```yaml
    source:
      address: dataos://testawslh
      options:
          source-table: "masking_test.aws_masking_data"
          type-hints:
            revenue: double
          mask:
            revenue: noise:0.1
          # 100000 → 91234 (±10% variation)
    ```



### **6. Date Masking Algorithms**

Transforms date or datetime values while preserving logical time intervals.

!!! warning
    Date masking algorithms require explicit type definitions for columns, specified as `TEXT` in the `type-hints` configuration.


- **`date_shift`**

    Randomly shifts dates by up to *N* days.

    `date_shift` requires the destination column to be of type `TEXT` as shown below inside `type-hints`:

    ```yaml
    source:
      address: dataos://testawslh
      options:
          source-table: "masking_test.aws_masking_data"
          type-hints:
            birth_date: text
            registration_date: text
            purchase_date: text
          mask:
            birth_date: date_shift:30
          # 1990-05-15 → 1990-06-02
    ```

- **`year_only`**

    Retains only the year component.

    `year_only` requires the destination column to be of type `TEXT` as shown below inside `type-hints`:
    

    ```yaml
    source:
      address: dataos://testawslh
      options:
          source-table: "masking_test.aws_masking_data"
          type-hints:
            registration_date: text
          mask:
            registration_date: year_only
          # 2024-03-15 → 2024
    ```

- **`month_year`**

    Preserves the month and year components.

    `month_year` requires the destination column to be of type `TEXT` as shown below inside `type-hints`:


    ```yaml
    source:
      address: dataos://testawslh
      options:
          source-table: "masking_test.aws_masking_data"
          type-hints:
            purchase_date: text
          mask:
            purchase_date: month_year
          # 2024-03-15 → "2024-03"
    ```

??? note "Applying Masking to Sensitive Columns in an Iceberg Table on AWS-backed DataOS Lakehouse"

    ## Example Case Scenario

    A Nilus pipeline is configured to apply column-level data masking on a source table stored in an Apache Iceberg format within a DataOS Lakehouse environment backed by AWS. The goal is to protect sensitive information before writing it to a downstream sink while preserving analytical usability.

    The table below lists of the source table’s schema, which includes a variety of sensitive fields across data types:

    | **Data Type** | **Columns**    | 
    | ------------- | ------------- |
    | `varchar`     |   `user_id`, `customer_id`, `session_id`, `first_name`, `last_name`, `email`, `phone`, `ssn`, `card_number`, `api_key`, `password`, `address`, `comments`, `account_number`   |
    | `bigint`      |   `age`, `income`, `salary`, `score`   |
    | `double`      |   `revenue`, `temperature`   |
    | `date`        |   `birth_date`, `registration_date`, `purchase_date`   |
    

    ### **Sample Manifest Configuration**

    ```yaml
    source:
      address: dataos://testawslh
      options:
        source-table: "masking_test.aws_masking_data"
        type-hints:
          income: text
          salary: text
          score: text
          revenue: double
          temperature: double
          birth_date: text
          registration_date: text
          purchase_date: text
        mask:
          user_id: "hash"
          customer_id: "hmac:my-secret-key"
          session_id: "md5"
          email: "email"
          phone: "phone"
          ssn: "ssn"
          card_number: "credit_card"
          api_key: "fixed:MASKED_KEY"
          password: "stars"
          comments: "redact"
          first_name: "first_letter"
          last_name: "partial:2"
          address: "partial:4"
          account_number: "sequential"
          age: "round:10"
          income: "range:10000"
          salary: "round:5000"
          score: "range:100"
          revenue: "noise:0.1"
          temperature: "noise:0.05"
          birth_date: "date_shift:30"
          registration_date: "year_only"
          purchase_date: "month_year"

    sink:
      address: dataos://mssqldepot5
      options:
        dest-table: "dbo.aws_masking_mssql9"
        incremental-strategy: append
    ```

    This configuration ensures that:

    - Sensitive fields such as `ssn`, `card_number`, and `password` are anonymized using irreversible or obfuscating algorithms.

    - Format-preserving and partial masking are used where structural integrity is required (e.g., `email`, `address`).

    - Numeric and date values are transformed using rounding, ranges, or temporal shifts to maintain analytical usability while preventing exposure.


## Selecting Masking Algorithm

The following table outlines recommended algorithms based on common data handling scenarios:

| **Scenario**                | **Recommended Masking Algorithms**           |
| --------------------------- | -------------------------------------------- |
| **PII Protection**          | `hash`, `redact`, `email`, `phone`, `ssn`    |
| **Development and Testing** | `uuid`, `random`, `partial`                  |
| **Analytical Workloads**    | `round`, `range`, `date_shift`, `month_year` |
| **Regulatory Compliance**   | `hash`, `redact`, `uuid`, `credit_card`      |




### **Performance Considerations**

- **Hash-based algorithms** provide high performance with consistent output.

- **Format-preserving masking** incurs moderate CPU overhead due to pattern retention.

- **Randomized masking** introduces minimal processing latency.

- **Multiple masking rules** can be applied via Nilus in a single processing pass effectively.


### **Security Considerations**

- Hashing supports one-way anonymization; however, common input values may be susceptible to reverse mapping.

- Partial masking may expose data patterns and is not recommended for highly sensitive fields.

- Date shifting retains relative intervals and must be used with caution to avoid inference risks.

- Consistent tokenization methods (e.g., `hash`, `uuid`) preserve referential integrity but may expose relational patterns across datasets.

- All masking strategies must be validated against organizational data protection and compliance policies.


### **Processing Behavior**

- Masking is performed in-memory during ingestion, without altering the original source data.

- Processing overhead increases proportionally with dataset size and the number of columns subjected to masking.