# Filter Operators: Example Scenarios

!!! info "Information"
    This document provides a detailed overview of various filter operators that you can use in query payloads. It explains how each operator functions and includes example payloads and results to illustrate their application.

## 1. `equals`

Use it when you need an exact match. It supports multiple values.

**Example Payload and Result**

Retrieving the customer IDs and countries for customers based in the USA, limited to 10 results.

![equal.png](/quick_guides/working_with_payload/filter_operator_example_scenarios/equal.png)

---

## 2. `notEquals`

The opposite operator of `equals`. It supports multiple values.

- Applied to measures.
- Dimension types: `string`, `number`, `time`.

**Example Payload**

**Result**

![not_equal.png](/quick_guides/working_with_payload/filter_operator_example_scenarios/not_equal.png)

---

## 3. `contains`

The `contains` filter functions as a wildcard, case-insensitive LIKE operator. It typically utilizes the ILIKE operator in SQL backends, with values enclosed in `%`. This filter supports multiple values.

- Dimension types: `string`.

![contains.png](/quick_guides/working_with_payload/filter_operator_example_scenarios/contains.png)

---

## 4. `notContains`

The opposite operator of `contains`. Supports multiple values.

- Data Type: `string`.

![notcontains.png](/quick_guides/working_with_payload/filter_operator_example_scenarios/notcontains.png)

---

## 5. `startsWith`

The `startsWith` filter acts as a case-insensitive `LIKE` operator with a wildcard at the end. Supports multiple values.

- Dimension types: `string`.

**Example Payload and Result**

This query retrieves up to 10 product IDs and their associated designer names, filtering for designers whose names start with "Ja."

![startswith.png](/quick_guides/working_with_payload/filter_operator_example_scenarios/startswith.png)

---

## 6. `notStartsWith`

The opposite operator of `startsWith`.

**Example Payload and Result**

This query retrieves up to 10 product IDs and their associated designer names, filtering for designers whose names do not start with "Ja."

![notstartswith.png](/quick_guides/working_with_payload/filter_operator_example_scenarios/notstartswith.png)

---

## 7. `endsWith`

The `endsWith` filter acts as a case-insensitive `LIKE` operator with a wildcard at the beginning. Supports multiple values.

- Dimension types: `string`.

**Example Payload and Result**

This query retrieves up to 10 product IDs and their associated designer names, filtering for designers whose names end with "e.”

![endwith.png](/quick_guides/working_with_payload/filter_operator_example_scenarios/endwith.png)

---

## 8. `notEndsWith`

The opposite operator of `endsWith`.

**Example Payload and Result**

![notendwith.png](/quick_guides/working_with_payload/filter_operator_example_scenarios/notendwith.png)

---

## 9. `gt`

The `gt` operator means **greater than** and is used with measures or dimensions of type `number`.

- Applied to measures.
- Dimension types: `number`.

**Example Payload and Result**

Retrieves records where the product price is greater than 100.

![gt.png](/quick_guides/working_with_payload/filter_operator_example_scenarios/gt.png)

---

## 10. `gte`

The `gte` operator means **greater than or equal to** and is used with measures or dimensions of type `number`.

- Applied to measures.
- Dimension types: `number`.

**Example Payload and Result**

Filter products based on their price, returning details for products priced more than `125.51`.

![gte.png](/quick_guides/working_with_payload/filter_operator_example_scenarios/gte.png)

---

## 11. `lt`

The `lt` operator means **less than** and is used with measures or dimensions of type `number`.

- Applied to measures.
- Dimension types: `number`.

**Example Payload and Result**

Filter products based on their price, returning details for products priced below `125.51`.

![lt.png](/quick_guides/working_with_payload/filter_operator_example_scenarios/lt.png)

---

## 12. `lte`

The `lte` operator means **less than or equal to** and is used with measures or dimensions of type `number`.

- Applied to measures.
- Dimension types: `number`.

**Example Payload and Result**

Filter products based on their price, returning details for products priced at or below `125.51`.

![lte.png](/quick_guides/working_with_payload/filter_operator_example_scenarios/lte.png)

---

## 13. `set`

Operator `set` checks whether the value of the member **is not** `NULL`. You don't need to pass `values` for this operator.

- Applied to measures.
- Dimension types: `number`, `string`, `time`.

**Example Payload and Result**

The query retrieves products where the price information is not missing (NOT NULL).

![set.png](/quick_guides/working_with_payload/filter_operator_example_scenarios/set.png)

---

## 14. `notSet`

The opposite of `set`. It checks whether the value of the member **is** `NULL`.

- Applied to measures.
- Dimension types: `number`, `string`, `time`.

**Example Payload and Result**

The query retrieves products where the price information is missing (NULL).

![notset.png](/quick_guides/working_with_payload/filter_operator_example_scenarios/notset.png)

---

## 15. `inDateRange`

The operator `inDateRange` is used for filtering dates within a given range. The `values` array should contain the start and end dates.

- Applied to dimensions of type `time`.

**Example Payload and Result**

Retrieve order details within a specific date range.

![isdaterange.png](/quick_guides/working_with_payload/filter_operator_example_scenarios/isdaterange.png)

---

## 16. `beforeDatenotInDateRange`

Opposite operator to `inDateRange`, use it when you want to exclude specific
dates. The values format is the same as for `inDateRange`.

- Dimension types: `time`.
    
    **Example Payload and Results:**
    
    ![image.png](/quick_guides/working_with_payload/filter_operator_example_scenarios/notindaterange.png)
    

## 17. `beforeDate`

The `beforeDate` operator filters for dates that occur before the provided date. The `values` array should contain only one date.

- Applied to dimensions of type `time`.

**Example Payload and Result**

Retrieve orders placed before a specific date.

![beforedate.png](/quick_guides/working_with_payload/filter_operator_example_scenarios/beforedate.png)

---

## 18. `afterDate`

The `afterDate` operator filters for dates that occur after the provided date. The `values` array should contain only one date.

- Applied to dimensions of type `time`.

**Example Payload and Result**

Retrieve orders placed after a specific date.

![afterdate.png](/quick_guides/working_with_payload/filter_operator_example_scenarios/afterdate.png)