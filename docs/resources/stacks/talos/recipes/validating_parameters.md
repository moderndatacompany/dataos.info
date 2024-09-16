# Validating API parameters

Validators are tools used to ensure that the input parameters of API requests meet predefined criteria and formats before they are processed. Validators enforce rules on the data provided by users, helping to maintain data integrity, improve security, and ensure consistent behavior of the API. In this section, you can find techniques to apply and manage the validators.


## Applying validators

Apply validators with the validation filters to validate API parameters. Each validator has a corresponding filter with an `is_` prefix, such as the `is_integer` filter for the integer validator.

To use these filters, chain them after your parameters:

```sql
-- orders.sql
SELECT *FROM
orders
WHERE order_id = {{ context.params.order_id | is_required | is_uuid }}

```

## Setting arguments for validators

To set arguments for validators, use Python's keyword arguments syntax:

```sql
-- orders.sql
SELECT *FROM
orders
WHERE create_date = {{ context.params.create_date | is_date(format='YYYY-MM-DD') }}
AND price = {{ context.params.price | is_integer(min=0, max=1000000) }}

```

## Handling error responses for invalid requests

If a request doesn't meet the validator requirements, Talos rejects the request and returns an error response. Here's an example:

```sql
-- orders.sql
SELECT *FROM
orders
where price = {{ context.params.price | is_integer(min=0, max=1000000) }}

```

If you send a request with `GET<endpoint>/api/orders?price=1000001`, Talos returns an HTTP status code 400 along with the following message:

```json
{
  "code": "userError",
  "message": "The input parameter is invalid, it should be integer type",
}

```

This approach ensures that only valid requests are processed, providing better error handling and more informative feedback to clients.

## Supported validators

### **`is_required` - Required validator**

Makes the request parameter field required, using Joi for validation.

| Argument | Required | Description |
| --- | --- | --- |
| disallow | false | Array type. Specifies disallowed input values. If the parameter value appears in the disallow value, an error message is sent in the response. |

=== "Example 1: Required Validator"

    ```sql
    -- orders.sql
    SELECT *FROM
    orders
    WHERE order_id = {{ context.params.order_id | is_required }}

    ```

=== "Example 2: Required Validator with Disallowed Values"

    ```sql
    -- orders.sql
    SELECT *FROM
    orders
    WHERE order_id = {{ context.params.order_id | is_required(disallow=['']) }}

    ```

### **Error response**

When sending a request with `GET<endpoint>/api/dep_users?department=null`, it returns an HTTP status code 400 and the following message:

```json
{
  "code": "userError",
  "message": "The input parameter is invalid, it should be required",
}

```

### **`is_uuid` - UUID validator**

Validates the UUID format for the request parameter.

| Argument | Required | Description |
| --- | --- | --- |
| version | false | String type. Specifies the UUID version (uuidv1, uuidv4, or uuidv5). |

=== "Example 1: UUID Validator"
    ```sql
    -- orders.sql
    SELECT *FROM
    orders
    WHERE order_id = {{ context.params.order_id | is_uuid }}

    ```

=== "Example 2: UUID Validator with Version"

    ```sql
    -- orders.sql
    SELECT *FROM
    orders
    WHERE order_id = {{ context.params.order_id | is_uuid(version='uuidv4') }}

    ```

---

### `is_date` - Date validator

Validates the date format for the request parameter.

| Argument | Required | Description |
| --- | --- | --- |
| format | false | String type. Specifies the date format, supporting ISO_8601 tokens (e.g., 'YYYYMMDD', 'YYYY-MM-DD', 'YYYY-MM-DD HH:mm'). |

=== "Example 1: Date Validator"
    ```sql
    -- orders.sql
    SELECT *FROM
    orders
    WHERE create_date = {{ context.params.create_date | is_date }}

    ```

=== "Example 2: Date Validator with Format"
    ```sql
    -- orders.sql
    SELECT *FROM
    orders
    WHERE create_date = {{ context.params.create_date | is_date(format='YYYY-MM-DD') }}

    ```

---

### `is_string` - String validator

Validates the string format for the request parameter.

| Argument | Required | Description |
| --- | --- | --- |
| format | false | String type. Specifies the string format, supporting regular expressions. Uses Joi pattern for validation. |
| length | false | Number type. Specifies the exact length of the string. |
| max | false | Number type. Specifies the maximum number of string characters. |
| min | false | Number type. Specifies the minimum number of string characters. |

=== "Example 1: String Validator"
    ```sql
    -- orders.sql
    SELECT *FROM
    orders
    WHERE order_id = {{ context.params.order_id | is_string }}

    ```

=== "Example 2: String Validator with Format"
    ```sql
    -- orders.sql
    SELECT *FROM
    orders
    WHERE order_id = {{ context.params.order_id | is_string(format='^[a-zA-Z0-9]{3,30}$') }}

    ```

=== "Example 3: String Validator with Length"
    ```sql
    -- orders.sql
    SELECT *FROM
    orders
    WHERE order_id = {{ context.params.order_id | is_string(length=10) }}

    ```

=== "Example 4: String Validator with Min & Max"
    ```sql
    -- orders.sql
    SELECT *FROM
    orders
    WHERE order_id = {{ context.params.order_id | is_string(min=3, max=30) }}

    ```


### **`is_integer` - Integer validator**

Validates the integer format for the request parameter.

| Argument | Required | Description |
| --- | --- | --- |
| max | false | Number type. Specifies the maximum integer value. |
| min | false | Number type. Specifies the minimum integer value. |
| greater | false | Number type. Specifies that the value must be greater than the limit. |
| less | false | Number type. Specifies that the value must be less than the limit. |

=== "Example 1: Integer Validator"
    ```sql
    -- orders.sql
    SELECT *FROM
    orders
    WHERE price = {{ context.params.price | is_integer }}

    ```

=== "Example 2: Integer Validator with Min & Max"

    ```sql
    -- orders.sql
    SELECT *FROM
    orders
    WHERE price = {{ context.params.price | is_integer(min=0, max=1000000) }}

    ```

=== "Example 3: Integer Validator with Greater & Less"
    ```sql
    -- orders.sql
    SELECT *FROM
    orders
    WHERE price = {{ context.params.price | is_integer(greater=0, less=1000000) }}

    ```

---

### **`is_enum` - Enum Validator**

Validates the enum format for the request parameter.

| Argument | Required | Description |
| --- | --- | --- |
| items | true | Array type. Specifies the whitelist. Must add at least one element to this array. Enum validator does not care about the data type, so both [1] and ["1"] allow the value 1 no matter if it is a string or number. |

Example: Enum Validator

```sql
-- orders.sql
SELECT *FROM
orders
WHEREstatus = {{ context.params.status | is_enum(items=['pending', 'paid', 'shipped']) }}

```