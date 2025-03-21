# GraphQL query format and examples

## Query Properties

A Query has the following properties:

* `measures`: An array of measures.

* `dimensions`: An array of dimensions.

* `limit`: A row limit for your query.

* `offset`: The number of initial rows to be skipped for your query. The default value is `0`.

* `order`: An object, where the keys are measures or dimensions to order by and their corresponding values are either `asc` or `desc`. The order of the fields to order on is based on the order of the keys in the object. If not provided, \[default ordering]\[ref-default-order] is applied. If an empty object (`[]`) is provided, no ordering is applied.

* `timezone`: A time zone for your query. You can set the desired time zone in the [TZ Database Name](https://en.wikipedia.org/wiki/Tz_database)
  format, e.g., `America/Los_Angeles`. Default is `UTC`.

### **Default order**

When the order property is not explicitly defined in the query, the results are sorted by default according to the following sequence:

- **Time Dimension:** Results are first ordered by the initial time dimension with granularity, in ascending order. If no time dimension with granularity is present.

- **Measure:** Next, results are sorted by the first measure found, in descending order. If no measure is specified.

- **Dimension:** Finally, if neither of the above are available, results are ordered by the first dimension, in ascending order.

### **Alternative order format**

Alternatively, you can control the sequence of the order specification using an alternative format for ordering, which is an array of tuples:

```graphql
query LensQuery {
  table(
    limit: 10
    offset: 0
    timezone: "UTC"
    orderBy: {customers: {annual_income: asc, customer_name: desc}}
  ) {
    customers {
      annual_income
      customer_name
      education_level
    }
  }
}
```

This query retrieves up to 10 customers, sorted first by annual income and then by customer name, with results

Following are examples of GraphQL queries with different filters for analytical needs.

### **`equals`**

Use it when you need an exact match. It supports multiple values.

* Applied to measures.

* Dimension types: `string`, `number`, `time`.

This query retrieves the first 10 users from the US.

```graphql
query LensQuery {
  table(limit: 10) {
    users(
      where: { country: { equals: "US" } }
    ) {
      country
    }
  }
}
```

### **`notEquals`**

The opposite operator of `equals`. It supports multiple values.

* Applied to measures.

* Dimension types: `string`, `number`, `time`.

This query retrieves the first 10 users whose country is not France

```graphql
query LensQuery {
  table(limit: 10) {
    users(
      where: { country: { notEquals: "France" } }
    ) {
      country
    }
  }
}
```

<aside class="callout">
💡To check if a value is not `NULL`, use the `set` operator instead.
</aside>

### **`contains`**

The `contains` filter acts as a wildcard case-insensitive `LIKE` operator. In
the majority of SQL backends it uses `ILIKE` operator with values being
surrounded by `%`. It supports multiple values.

* Dimension types: `string`.

This query retrieves the customers whose names contain either "MR. ADRIAN STEWART" or "MR. AARON ROSS,".

```graphql
query LensQuery {
  table {
    customers(
      where: { customer_name: { contains: ["MR. ADRIAN STEWART", "MR. AARON ROSS"] } }
    ) {
      customer_name
      marital_status
      customer_key
    }
  }
}
```

### **`notContains`**

The opposite operator of `contains`. It supports multiple values.

* Dimension types: `string`.

This query retrieves the first 10 customers whose names do not contain "MR. ADRIAN STEWART" or "MR. AARAV ROSS," useful for excluding specific customers from the results based on their names.

```graphql
query LensQuery {
  table(limit: 10) {
    customers(
      where: {customer_name: {notContains: ["MR. ADRIAN STEWART", "MR. AARAV ROSS"]}}
    ) {
      customer_name
      marital_status
    }
  }
}
```

### **`startsWith`**

The `startsWith` filter acts as a case-insensitive `LIKE` operator with a
wildcard at the end. In the majority of SQL backends, it uses the `%` at the end of each value. It supports multiple values.

* Dimension types: `string`.

This query retrieves the first 10 customers whose names start with "MRS.," allowing you to filter for female customers based on the title.

```graphql
query LensQuery {
  table(limit: 10) {
    customers(
      where: {customer_name: {startsWith: "MRS."}}
    ) {
      customer_name
      marital_status
    }
  }
}
```

### **`notStartsWith`**

The opposite operator of `startsWith`.

### **`endsWith`**

The `endsWith` filter acts as a case-insensitive `LIKE` operator with a wildcard at the beginning. In the majority of SQL backends, it uses the
`%` at the beginning of each value. It supports multiple values.

* Dimension types: `string`.

This query retrieves the first 10 customers whose names end with "FERNANDEZ," allowing you to filter customers based on their last name.

```graphql
query LensQuery {
  table(limit: 10) {
    customers(
      where: {customer_name: {endsWith: "FERNANDEZ"}}
    ) {
      customer_name
      marital_status
      customer_key
    }
  }
}
```

### **`notEndsWith`**

The opposite operator of `endsWith`.

### **`gt`**

The `gt` operator means **greater than** and is used with measures or dimensions
of type `number`.

* Applied to measures.

* Dimension types: `number`.

This query retrieves the first 10 customers with an annual income greater than $10,000.

```graphql
query LensQuery {
  table(limit: 10) {
    customers(
      where: { annual_income: { gt: 10000 } }
    ) {
      customer_name
    }
  }
}
```

### **`gte`**

The `gte` operator means **greater than or equal to** and is used with measures or dimensions of type `number`.

* Applied to measures.

* Dimension types: `number`.

This query retrieves the first 10 customers with an annual income greater than or equal to $100, along with their marital status and customer key.

```graphql
query LensQuery {
  table(limit: 10) {
    customers(
      where: { annual_income: { gte: 100 } }
    ) {
      customer_name
      marital_status
      customer_key
    }
  }
}

```

Similarly, if you want to apply multiple filters using OR or other conditions, here’s an extended example:

This query retrieves the first 10 customers who meet two conditions:

1. Their annual income is greater than or equal to $10,000.

2. Their marital status is "Married".

```graphql
query LensQuery {
  table(limit: 10) {
    customers(
      where: { AND: [{ annual_income: { gte: 10000 } },
       { marital_status: { equals: "M"} }
      ] 
      } 
    ) {
      customer_name
      customer_key
    }
  }
}
```

### **`lt`**

The `lt` operator means **less than** and is used with measures or dimensions of
type `number`.

* Applied to measures.

* Dimension types: `number`.

This query retrieves the first 10 customers whose annual income is less than $15,000 and returns their customer names.

```graphql
query LensQuery {
  table(limit: 10) {
    customers(
      where: {  annual_income: { lt: 15000 } }
    ) {
      customer_name
    }
  }
}
```

### **`lte`**

The `lte` operator means **less than or equal to** and is used with measures or
dimensions of type `number`.

* Applied to measures.

* Dimension types: `number`.

This query retrieves the first 10 customers whose annual income is less than or equal to $15,000.

```graphql
query LensQuery {
  table(limit: 10) {
    customers(
      where: {  annual_income: { lte: 15000 } }
    ) {
      customer_name
      customer_key
    }
  }
}
```

### **`set`**

Operator `set` checks whether the value of the member **is not** `NULL`. You
don't need to pass `values` for this operator.

* Applied to measures.

* Dimension types: `number`, `string`, `time`.

This will return customers where the customer\_name field is not set.

```graphql
query LensQuery {
  table(limit: 10) {
    customers(
      where: { customer_name: { set: false } }
    ) {
      customer_name
    }
  }
}
```

### **`inDateRange`**

The operator `inDateRange` is used to filter a time dimension into a specific date range. The values must be an array of dates with the format 'YYYY-MM-DD' or `YYYY-MM-DDTHH:mm:ss.SSS` format. If only one date specified the filter would be set exactly to this date.

* `granularity`: A granularity for a time dimension. It supports the following values `second`, `minute`, `hour`, `day`, `week`, `month`, `quarter`, `year`. If you pass value to the granularity, Lens will only perform filtering by the given date itself without grouping.

* Dimension types: `time`.

This query retrieves the first 10 customers whose `birth_date` falls within the year 2000, and returns their `customer_name` and `annual_income`.

```graphql
query LensQuery {
  table(limit: 10) {
    customers(
      where: { birth_date: { inDateRange: ["2000-01-01", "2000-12-31"] } }
    ) {
      customer_name
      annual_income
    }
  }
}
```

### **`notInDateRange`**

An opposite operator to `inDateRange`, use it when you want to exclude specific dates. The values format is the same as for `inDateRange`.

* Dimension types: `time`.

This query retrieves the first 10 customers whose `birth_date` does not fall within the year 2000, and returns their `customer_name` and `annual_income`.

```graphql
query LensQuery {
  table(limit: 10) {
    customers(
      where: { birth_date: { notInDateRange: ["2000-01-01", "2000-12-31"] } }
    ) {
      customer_name
      annual_income
    }
  }
}
```

### **`beforeDate`**

Use it when you want to retrieve all results before some specific date. The
values should be an array of one element in `YYYY-MM-DD` timestamp format.

* Dimension types: `time`.

This query retrieves the first 10 customers whose `birth_date` is before January 1, 2000, and returns their `customer_name`, `annual_income`, and `birth_date` (with the date value).

```graphql
query LensQuery {
  table(limit: 10) {
    customers(
      where: { birth_date: { beforeDate: "2000-01-01" } }
    ) {
      customer_name
      annual_income
      birth_date {
          value
      }
    }
  }
}
```

### **`afterDate`**

The same as `beforeDate`, but is used to get all results after a specific date.

* Dimension types: `time`.

This query retrieves the first 10 customers whose `birth_date` is after January 1, 2000, and returns their `customer_name`, `annual_income`, and `birth_date` (with the date value).

```graphql
query LensQuery {
  table(limit: 10) {
    customers(
      where: { birth_date: { afterDate: "2000-01-01" } }
    ) {
      customer_name
      annual_income
      birth_date {
          value
      }
    }
  }
}
```

## Boolean logical operators

Filters can contain `or` and `and` logical operators. Logical operators have
only one of the following properties:

* `or` An array with one or more filters or other logical operators

* `and` An array with one or more filters or other logical operators

This query will return customers who either meet the income or marital status condition, but must also meet the "MR" in their name and be homeowners.

```graphql
query LensQuery {
  table(limit: 10) {
    customers(
      where: {
        OR: [
          { annual_income: { gte: 10000 } }        # Customers with income >= 50k
           # Customers who are married
        ],
        AND: [
   { customer_name: { contains: "MR" } }            # Customers who are homeowners
            # Customers in the US
        ]
      }
    ) {
      customer_name
      marital_status
      annual_income
      
      home_owner
      
    }
  }
}
```

You can not put dimensions and measures filters in the same logical operator. When Lens generates a SQL query to the data source, dimension and measure filters are translated to expressions in WHERE and HAVING clauses, respectively.

In other words, dimension filters apply to raw (unaggregated) data and measure filters apply to aggregated data, so it's not possible to express such filters in SQL semantics.

In such case you can use the nested AND and OR to query the dimension filter and measure filter together:

```graphql
query LensQuery {
  table(
    limit: 10
    offset: 0
    timezone: "UTC"
    orderBy: {}
    where: {AND: {AND: [{customers: {total_customer: {set: true}}}]}, OR: {AND: [{OR: [{customers: {annual_income: {in: [100000]}}}]}]}}
  ) {
    customers {
      annual_income
      total_customer
      
    }
  }
}
```